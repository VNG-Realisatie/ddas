# Berichten

## Schuldhulpverleningsgegevens

De technische beschrijving van de API is in het volgende OAS3-bestand beschreven:

- [Bekijk specificatie](https://VNG-Realisatie.github.io/ddas/api/v1.0/DDAS-VS.yaml)  
- [Download YAML](https://raw.githubusercontent.com/VNG-Realisatie/ddas/main/v1.0/DDAS-SHV.yaml)  

## Vroegsignaleringsgegevens

De technische beschrijving van de API is in het volgende OAS3-bestand beschreven:  

- [Bekijk specificatie](https://VNG-Realisatie.github.io/ddas/api/v1.0/DDAS-VS.yaml)  
- [Download YAML](https://raw.githubusercontent.com/VNG-Realisatie/ddas/main/v1.0/DDAS-VS.yaml)  



Hieronder worden de berichten die in het OAS-bestand technisch beschreven zijn, toegelicht.


## Encoding

Conform de specificaties voor de bestandsuitwisseling voor [schuldhulpverlening](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/) en [vroegsignalering](https://vng-realisatie.github.io/ddas-vroegsignalering/v1.0/uitwisselspecificatie/), is de encoding van de berichten UTF-8.


## Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS via de "Outway" naar de "Inway" van de schuldhulpverlener gestuurd wordt. Dit is een POST request waarbij alleen gegevens opgevraagd worden. Er worden geen GET requests gebruikt, omdat hierbij de parameters in de URL zitten en mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen.

Parameters die meegestuurd kunnen worden (allemaal optioneel):

- Startdatum (date, default leeg - schuldhulpverlener bepaalt dan startdatum)

- Einddatum (date, default leeg - schuldhulpverlener bepaalt dan einddatum)

- Aanleverende_organisatie (string, default alle – alleen relevant als over meer dan 1 organisatie (gemeente/ schuldhulpverlener) gegevens aangeleverd worden)

Het bericht wordt met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) ondertekend met de private sleutel van de verzender van het vraagbericht - in dit geval CBS. Zie het hoofdstuk [Signing en Versleuteling](signing-encryptie.md) voor de specificaties van de ondertekening.


## Antwoordbericht (response)

Dit is het antwoordbericht van de gegevensbeheerder (systeem dat de bron beheert) met de gewenste gegevens in JSON formaat.
De payload is gebaseerd op het uitwisselformaat zoals dat is beschreven voor [schuldhulpgegevens](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/) en [vroegsignaleringsgegevens](https://vng-realisatie.github.io/ddas-vroegsignalering/v1.0/uitwisselspecificatie/).

Ook dit bericht wordt ondertekend met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) met gebruik van de eigen private sleutel.
Versleutelen van de payload is niet nodig.

Mogelijke responses:

- 200: bericht goed verwerkt (met versleutelde en gesigneerde payload)

- Foutberichten conform de FSC standaard:

  - Gegenereerd door de [FSC Manager](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes)

  - Gegenereerd door de [gekozen methode van FSC](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-0)

  - Gegenereerd door de [de FSC Inway](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-1)
