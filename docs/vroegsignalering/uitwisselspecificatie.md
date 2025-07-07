# Uitwisselmodel

## Inleiding

De uitwisselspecificatie specificeert welke gegevens en in welke vorm de gegevens aan het CBS aangeleverd dienen te worden. Hiertoe is een specificatie in [JSON-schema](https://json-schema.org) gespecificeerd. De inhoud van deze JSON-schema is afgeleid van het [informatiemodel Vroegsignalering](./Hoofdlijnen_Model Vroegsignalering.md). 

De uitwisselspecificatie kent de volgende opbouw: 

1. Op het hoofdniveau is het Uitwisselmodel gedefinieerd. Dit met een aantal attributen die informatie geven over de levering: start- en einddatum van de levering en de aanleverdattum en tijd;
2. Op het tweede niveau worden zowel de vroegsignalen als de vroegsignaalzaken uitgevraagd. 
3. Vroegsignalen hebben een ID waarmee ze binnen de levering **en ook buiten de levering** te identificeren zijn.
4. In de vroegsignaalzaken wordt verwezen naar de vroegsignalen via een lijst ID's naar vroegsignalen

Aan het eind van de specficatie staan de gebruikte datatypes en waardenlijsten (enumeraties) die worden gebruikt opgenomen. 

## Encoding

Alle bestanden dienen te worden aangeleverd in [UTF-8-formaat](https://www.forumstandaardisatie.nl/open-standaarden/utf-8). 

## Uitwisselspecificatie

Onderstaand de definitie van de uitwisselspecificatie. Van deze definitie is ook een [downloadversie](https://raw.githubusercontent.com/VNG-Realisatie/ddas/refs/heads/Vroegsignalering/vroegsignalering/v0.1/json_schema_Uitwisselmodel.json) beschikbaar.

```
{!../vroegsignalering/v0.1/json_schema_Uitwisselmodel.json!}

```

## Voorbeelden

### Enkelvoudig voorbeeld

Onderstaand een voorbeeld JSON-bestand conform de uitwisselspecificatie. Dit voorbeeld kun je ook [downloaden](https://raw.githubusercontent.com/VNG-Realisatie/ddas/refs/heads/Vroegsignalering/vroegsignalering/v0.1/enkelvoudigVoorbeeld.json).

```
{!../vroegsignalering/v0.1/enkelvoudigVoorbeeld.json!}

```