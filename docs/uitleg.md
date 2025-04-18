# Uitleg uitwisselspecificatie

Om in het kader van DDAS gegevens aan het CBS te kunnen leveren versturen schuldhulpverleners gegevens over schuldhulptrajecten via een zogenaamd JSON-uitwisselbestand. De structuur van dit bestand wordt in technische zin beschreven onder het kopje [Uitwisselspecificatie](uitwisselspecificatie.md). Voor schuldhulpverleners is het belangrijk dat zij de juiste gegevens in hun systemen administreren, anders wordt het aanleveren van de benodigde informatie bemoeilijkt. In de volgende paragrafen wordt in (niet technische taal) beschreven welke gegevens  schuldhulpverleners moeten vastleggen om juist en volledig gegevens conform DDAS aan het CBS te kunnen leveren.

## Algemene gegevens

Bij ieder schuldhulptraject zijn de hieronder weergegeven gegevens van belang.

### Cliëntgegevens

- Burgerservicenummer (BSN)
- Geboortedatum
- Geslacht (Man, Vrouw, Onbekend)
- Postcode
- Huisnummer en eventueel huisnummertoevoeging

Er kunnen minimaal één en maximaal twee personen per traject worden opgevoerd. 

!!! danger "Let op: persoonsgegevens zijn van belang"
    Het is belangrijk dat, of het BSN, of alle andere gegevens zijn vastgelegd. 

### Schulden

Voor elke schuld die in het schuldhulptraject wordt meegenomen:

- Bedrag
- Peildatum
- Soort schuld (bijv. zorg, publiek, nuts)
- Is het een zakelijke schuld? (ja/nee)
- Gegevens van de schuldeiser (naam, KvK, postcode, privépersoon ja/nee)

## Schuldhulptraject

Het schuldhulptraject kent conform het NVVK-Referentieproces een aantal fases. Van deze fases is steeds een aantal gegevens van belang. Deze worden in de volgende paragrafen beschreven.

Naast de gegevens van de verschillende fases zijn per schuldhulptraject een aantal gegevens van belang die betrekking hebben op het schuldhulptraject als geheel:

- Startdatum van het schuldhulptraject
- Einddatum (alleen als het schuldhulptraject is afgerond)
- Toekenningsdatum (toekenningsdatum bevat de datum waarop de schuldregeling is toegekend.)
- Gemeentecode (gemeente onder wiens verantwoordelijkheid het traject wordt uitgevoerd)
- Totaal schuldbedrag bij aanvang traject 

### Aanmelding

- Startdatum van de aanmelding
- Einddatum van de aanmeldfase (optioneel)
- Is er sprake van crisisinterventie? (ja/nee)

### Intake

- Startdatum van het intakegesprek
- Einddatum van de intake
- Beschikkingsdatum
- Soort beschikking (Toelating of Afwijzing)

### Plan van aanpak

- Datum afronding plan van aanpak

### Stabilisatie

- Start- en einddatum van de stabilisatiefase

### Schuldregeling

- Datum aanvraag
- Afgewezen, toegekend of ingetrokken? Geef de juiste datum
- Is er een dwangakkoord aangevraagd? (ja/nee)
- Datum verzoek dwangakkoord (optioneel)

### Oplossing

- Start- en einddatum
- Soort oplossing (bijv. betalingsregeling, saneringskrediet, 0%-aanbod)
- VTLB-bedrag (per maand)

### Begeleiding

Voor elk type begeleiding:

- Soort begeleiding (bijv. budgetbeheer, beschermingsbewind)
- Start- en einddatum

### Uitstroom

Het gaat hier over de gegevens ten aanzoen van de uitstroom uit het schuldhulptraject.

- Datum uitstroom
- Datum beëindigingsbeschikking
- Reden van uitstroom (bijv. zelf, overleden, niet passend, afgerond)

## Aanvullende gegevens

In sommige gevallen spelen er aanvullende zaken. De hiervoor benodigde gegevens worden in de volgende paragrafen beschreven. 

### Crisisinterventie

Is er sprake geweest van één of meer crisisinterventies?

- Start- en einddatum

### Informatie en advies

Wordt er voor de cliënt(en) informatie en advies ingezet?

- Start- en einddatum van het informatie- en adviestraject

### Moratorium

Is er sprake van één of meer moratoria?

- Datum aanvraag
- Datum goedkeuring
- Start- en einddatum

### Voorlopige voorziening

Is er binnen het schuldhulptraject sprake van één of meer voorlopige voorzieningen?

- Start- en einddatum

