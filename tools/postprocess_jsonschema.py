#!/usr/bin/env python3
"""Normaliseer crunch_uml renderer-artefacten in het gegenereerde JSON Schema.

crunch_uml emit een paar constructies die het v1.0-schema niet kent en die *niet*
vanuit het model of de transform-plugin te sturen zijn, omdat ze pas door de
renderer/template worden geproduceerd (ná de transformatie):

  * ``"uniqueItems": true`` op verplichte array-associaties wordt verwijderd;
  * de verplichte meervoudige relatie ``leveringen`` wordt aan de top-level
    ``required`` toegevoegd (crunch_uml zet alleen *enkelvoudige* verplichte
    relaties in ``required``);
  * de ``bedrag``-description (uit de crunch_uml-template ``json_datatypes.json``,
    niet uit het model) wordt teruggezet naar de v1.0-tekst;
  * de volgorde van keys en ``required``/``enum``-waarden wordt gelijkgetrokken met de
    gecommitte versie (HEAD) van het bestand. crunch_uml ordent via Python-sets, dus
    zonder vaste ``PYTHONHASHSEED`` (zie TaskFile) verschilt de volgorde per run.
    Nieuwe keys komen achteraan. Is het schema inhoudelijk gelijk aan de gecommitte
    versie, dan blijven exact de gecommitte bytes staan: dezelfde data levert zo altijd
    hetzelfde bestand op, en een git-diff toont alleen inhoudelijke wijzigingen.

Model-inhoud (definities, veldnamen, datatypes, multipliciteiten) hoort *niet*
hier maar in het model (XMI) of de transform-plugin; dit script beperkt zich
bewust tot de renderer-/template-artefacten hierboven.

Gebruik:
    python3 tools/postprocess_jsonschema.py <pad-naar-json-schema>
"""
import json
import os
import subprocess
import sys


def strip_unique_items(node):
    """Verwijder recursief alle ``uniqueItems``-sleutels (v1.0 kent ze niet)."""
    if isinstance(node, dict):
        node.pop("uniqueItems", None)
        for value in node.values():
            strip_unique_items(value)
    elif isinstance(node, list):
        for value in node:
            strip_unique_items(value)


def ensure_leveringen_required(schema):
    """Zorg dat de verplichte relatie ``leveringen`` in de top-level ``required`` staat."""
    required = schema.get("required")
    properties = schema.get("properties", {})
    if isinstance(required, list) and "leveringen" in properties and "leveringen" not in required:
        required.append("leveringen")


def restore_bedrag_description(schema):
    """Zet de ``bedrag``-description terug naar de exacte v1.0-tekst.

    Het ``bedrag``-$def komt uit de crunch_uml-template ``json_datatypes.json``,
    niet uit het model. Een latere crunch_uml-versie corrigeerde de typefout
    "nauwkweurig" -> "nauwkeurig"; voor exacte gelijkheid met v1.0 zetten we 'm terug.
    """
    bedrag = schema.get("$defs", {}).get("bedrag")
    if isinstance(bedrag, dict) and "description" in bedrag:
        bedrag["description"] = "Een geldbedrag in hele euros nauwkweurig."


def order_like(node, reference):
    """Herorden ``node`` recursief naar de volgorde in ``reference``; nieuwe elementen achteraan.

    Dicts volgen de key-volgorde van de referentie. Lijsten met alleen strings
    (``required``, ``enum``) volgen de volgorde van de referentie; overige lijsten
    worden positioneel per element vergeleken.
    """
    if isinstance(node, dict) and isinstance(reference, dict):
        keys = [k for k in reference if k in node] + [k for k in node if k not in reference]
        return {k: order_like(node[k], reference.get(k)) for k in keys}
    if isinstance(node, list) and isinstance(reference, list):
        if all(isinstance(item, str) for item in node + reference):
            return [x for x in reference if x in node] + [x for x in node if x not in reference]
        return [order_like(n, r) for n, r in zip(node, reference)] + node[len(reference):]
    return node


def committed_version(path):
    """De gecommitte versie (HEAD) van ``path`` als tekst, of ``None`` als die er niet is."""
    directory, name = os.path.split(os.path.abspath(path))
    result = subprocess.run(
        ["git", "-C", directory, "show", f"HEAD:./{name}"],
        capture_output=True,
        encoding="utf-8",
    )
    return result.stdout if result.returncode == 0 else None


def normalize(path):
    with open(path, "r", encoding="utf-8") as handle:
        schema = json.load(handle)

    strip_unique_items(schema)
    ensure_leveringen_required(schema)
    restore_bedrag_description(schema)

    text = json.dumps(schema, indent=4)
    committed = committed_version(path)
    if committed is not None:
        reference = json.loads(committed)
        schema = order_like(schema, reference)
        if schema == reference:
            print(f"{path}: inhoudelijk gelijk aan de gecommitte versie; gecommitte bytes behouden.")
            text = committed
        else:
            print(f"{path}: wijkt inhoudelijk af van de gecommitte versie; volgorde gelijkgetrokken.")
            text = json.dumps(schema, indent=4)

    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tools/postprocess_jsonschema.py <json-schema-file>", file=sys.stderr)
        raise SystemExit(2)
    normalize(sys.argv[1])
