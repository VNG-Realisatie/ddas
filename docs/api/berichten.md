# Berichten

## Schuldhulpverleningsgegevens

De technische beschrijving van de API is in het volgende OAS3-bestand beschreven:

<details><summary>Toon OAS3 beschrijving</summary>
``` { .yaml .copy }
{!../v1.0/DDAS-SHV.yaml!}
```
</details>

- [Klik hier om het bestand te downloaden](https://raw.githubusercontent.com/VNG-Realisatie/ddas-vroegsignalering/main/v1.0/DDAS-SHV.yaml)  


## Vroegsignaleringsgegevens

De technische beschrijving van de API is in het volgende OAS3-bestand beschreven:  

<details><summary>Toon OAS3 beschrijving</summary>
``` { .yaml .copy }
{!../v1.0/DDAS-VS.yaml!}
```
</details>

- [Klik hier om het bestand te downloaden](https://raw.githubusercontent.com/VNG-Realisatie/ddas-vroegsignalering/refs/heads/main/v1.0/DDAS-VS.yaml)  


Hieronder worden de berichten die in het OAS-bestand technisch beschreven zijn, toegelicht.


## Encoding

Conform de specificaties voor de bestandsuitwisseling voor [schuldhulpverlening](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/) en [vroegsignalering](https://vng-realisatie.github.io/ddas-vroegsignalering/v1.0/uitwisselspecificatie/), is de encoding van de berichten UTF-8.


## Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS via de "Outway" naar de "Inway" van de schuldhulpverlener gestuurd wordt. Dit is een POST request waarbij alleen gegevens opgevraagd worden. Er worden geen GET requests gebruikt, omdat hierbij de parameters in de URL zitten en mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen.

Parameters die meegestuurd kunnen worden (allemaal optioneel):

- aanleverperiodeStartdatum (date - startdatum van rapportageperiode, default leeg: gegevensleverancier bepaalt dan startdatum<sup>*</sup>)

- aanleverperiodeEinddatum (date - startdatum van rapportageperiode, default leeg: gegevensleverancier bepaalt dan einddatum<sup>*</sup>)

- Aanleverende_organisatie (string - organisatie waarvan de gegevens geleverd worden, default alle; alleen relevant als over meer dan 1 organisatie (gemeente/ schuldhulpverlener) gegevens aangeleverd worden)

- page (integer - de gewenste pagina, als er meerdere pagina's aan gegevens zijn; zie ook [niet-functionele eisen](non-functionals.md#performance), default de eerste pagina)

- pageSize (integer - aantal records (vroegsignalen/schuldhulptrajecten) dat in één responsebericht meegestuurd wordt, default leeg: gegevensleverancier bepaalt dan het aantal met een maximum zoals bepaald in de [niet-functionele eisen](non-functionals.md#performance))


><sup>*</sup>: als de schuldhulpverlener de start- en einddatum van de rapportageperiode bepaalt, worden de start- en einddatum van de afgelopen rapportageperiode gebruikt. NB: de definitie van de rapportageperiode (start- en einddatum en welke gegevens meegenomen moeten worden) wordt in een aparte beschrijving vastgesteld.   
>Voorbeeld: als CBS in juli een request voor gegevens verstuurt zonder start- en einddatum en er halfjaarlijks gerapporteerd wordt, dan worden de start- en einddatum waarover gegevens geleverd worden 1 januari, resp. 30 juni van het huidige jaar. Als er per kwartaal gerapporteerd wordt, dan zijn in dit geval de start- en einddatum 1 maart, resp. 30 juni van het huidige jaar.

Het bericht wordt met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) ondertekend met de private sleutel van de verzender van het vraagbericht - in dit geval CBS. Zie het hoofdstuk [Signing en Versleuteling](signing-encryptie.md) voor de specificaties van de ondertekening.


## Antwoordbericht (response)

Dit is het antwoordbericht van de gegevensbeheerder (systeem dat de bron beheert) met de gewenste gegevens in JSON formaat.
De payload is gebaseerd op het uitwisselformaat zoals dat is beschreven voor [schuldhulpgegevens](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/) en [vroegsignaleringsgegevens](https://vng-realisatie.github.io/ddas-vroegsignalering/v1.0/uitwisselspecificatie/).

Naast de vroegsignalen worden gegevens voor de **paginering** meegegeven. Deze zijn nodig als niet alle gegevens in één responsebericht passen - zie de [niet-functionele eisen](non-functionals.md#performance) voor meer uitleg. Als alle gegevens in één responsebericht passen, hoeven de paginering gegevens niet in het bericht opgenomen te worden.

Ook dit bericht wordt ondertekend met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) met gebruik van de eigen private sleutel. Zie het hoofdstuk [Signing en Versleuteling](signing-encryptie.md) voor de specificaties van de ondertekening.
Versleutelen van de payload is niet nodig.

Mogelijke responses:

- 200: bericht goed verwerkt (met gesigneerde payload)

- Foutberichten conform de FSC standaard:

  - Gegenereerd door de [FSC Manager](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes)

  - Gegenereerd door de [gekozen methode van FSC](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-0)

  - Gegenereerd door de [de FSC Inway](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-1)
