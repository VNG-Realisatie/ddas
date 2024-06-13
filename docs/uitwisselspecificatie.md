# Uitwisselmodel

## Inleiding

De uitwisselspecificatie specificeert welke gegevens en in welke vorm de gegevens aan het CBS aangeleverd dienen te worden. Hiertoe is een specificatie in [JSON-schema](https://json-schema.org) gespecificeerd. De inhoud van deze JSON-schema is afgeleid van het [informatiemodel schuldhulpverlening](./rapport_1.md).

De uitwisselspecificatie kent de volgende opbouw: 

1. Op het hoofdniveau is een aantal attributen opgenomen die informatie geven over de levering, zoals: start- en einddatum van de aanleverperiode, en de aanleverende [organisatie](./rapport_1.md/#organisaties). Er wordt vanuit gegaan dat er steeds door precies één schuldhulporganisatie gegevens wordenb aangeleverd. 
2. Op detailniveau wordt een aantal schuldhultrajecten aangeleverd. Dit met de verschillende fases die de trajecten hebben doorlopen volgens het [procesmodel](./rapport_1.md/#processen), en de [client(en)](./rapport_1.md/#clienten) die het betreft, met hun leefsituatie. Per client worden de schulden opgegeven.

Aan het eind van de specficatie staan de gebruikte datatypes en waardenlijsten (enumeraties) die worden gebruikt opgenomen. 

## Uitwisselspecificatie

Onderstaand de definitie van de uitwisselspecificatie. Van deze definitie is ook een [downloadversie](https://raw.githubusercontent.com/brienen/ddas/main/json_schema_Uitwisselmodel.json) beschikbaar.

```
{!../json_schema_Uitwisselmodel.json!}

```

## Voorbeeld

Onderstaand een voorbeeld JSON-bestand conform de uitwisselspecificatie. Dit voorbeeld kun je ook [downloaden](https://raw.githubusercontent.com/brienen/ddas/main/voorbeelddata.json).

```
{!../voorbeelddata.json!}

```
