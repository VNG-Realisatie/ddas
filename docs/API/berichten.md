# Berichten

De technische beschrijving van de API is het volgende OAS3-bestand beschreven. Hiervan is ook een [downloadbare versie](https://github.com/brienen/ddas/blob/Goverts-Place/API-v0.0.3/DDAS_opzetje_v0.0.3.yaml) van.
```
{!../API-v0.0.3/DDAS_opzetje_v0.0.3.yaml!}

```
Hieronder worden de berichten die daar technisch beschreven zijn, toegelicht.

## Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen - daarom liever een POST.

NB: Dit bericht wordt in een JWT verwerkt, voor signen en versleutelen (als versleutelen nodig is – met een BSN in het bericht zou dat waarschijnlijk moeten).

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel):

- Startdatum (default leeg - deelnemer bepaalt dan startdatum)

- Einddatum (default leeg - deelnemer bepaalt dan einddatum)

- Gemeente (default alle – alleen relevant als over meer dan 1 gemeente gegevens aangeleverd worden)


## Antwoordbericht (response)

Dit is het antwoordbericht van de schuldhulpverlener met de gewenste gegevens in JSON formaat.

Als versleutelen nodig is, in een JWT vorm (versleuteld conform JWE).

Payload is gebaseerd op [uitwisselspecificatie](https://brienen.github.io/ddas/latest/uitwisselspecificatie/)!

Mogelijke responses:

- 200: bericht goed verwerkt (met payload)

- Foutberichten moeten nog bepaald worden - waarschijnlijk 401 (unauthorized), 404 (not found), 500 (internal server error) en 503 (service unavailable)
