# Uitleg uitwisselspecificatie 

Om in het kader van DDAS gegevens aan het CBS te kunnen leveren versturen schuldhulpverleners gegevens over schuldhulptrajecten via een zogenaamd JSON-uitwisselbestand. De structuur van dit bestand wordt in technische zin beschreven onder het kopje [Uitwisselspecificatie](uitwisselspecificatie.md). Voor schuldhulpverleners is het belangrijk dat zij de juiste gegevens in hun systemen administreren, anders wordt het aanleveren van de benodigde informatie bemoeilijkt. In de volgende paragrafen wordt in (niet technische taal) beschreven welke gegevens  schuldhulpverleners moeten vastleggen om juist en volledig gegevens conform DDAS aan het CBS te kunnen leveren.

## Algemene gegevens

Bij ieder schuldhulptraject zijn de hieronder weergegeven gegevens van belang.

### Cliëntgegevens

- Burgerservicenummer (BSN)
- Geboortedatum
- Geslacht (mogelijke waarden: Man, Vrouw, Onbekend, Leeg)
- Postcode
- Huisnummer en eventueel huisnummertoevoeging

Er kunnen minimaal één en maximaal twee personen per traject worden opgevoerd. 

!!! danger "Let op: persoonsgegevens zijn van belang"
    Het is belangrijk dat, of het BSN, of alle andere gegevens zijn vastgelegd. 


### Schulden

Voor elke schuld die in het schuldhulptraject wordt meegenomen:

- Bedrag
- Peildatum - Peildatum <abbr title="Peildatum dat de schuld is vastgesteld.">❓</abbr>
- Soort schuld (mogelijke waarden: Zorg, Publiek, Nuts, Overig)
- Is het een zakelijke schuld? (ja/nee)
- Gegevens van de schuldeiser (naam, KvK, postcode, privépersoon ja/nee)

## Schuldhulptraject

Het schuldhulptraject kent conform het NVVK-Referentieproces een aantal fases. Van deze fases is steeds een aantal gegevens van belang. Deze worden in de volgende paragrafen beschreven.

Naast de gegevens van de verschillende fases zijn per schuldhulptraject een aantal gegevens van belang die betrekking hebben op het schuldhulptraject als geheel:

- Startdatum van het schuldhulptraject
- Einddatum (alleen als het schuldhulptraject is afgerond)
- Toekenningsdatum (toekenningsdatum bevat de datum waarop de schuldregeling is toegekend)
- Gemeentecode (gemeente onder wiens verantwoordelijkheid het traject wordt uitgevoerd)
- Totaal schuldbedrag bij aanvang traject 


### Aanmelding

??? note "Definitie Aanmelding"
    Moment dat een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn.

Hiervan worden de volgende zaken vastgelegd:

- Startdatum van de aanmelding <abbr title="Datum waarop een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn. ">❓</abbr>
- Einddatum van de aanmeldfase (optioneel)
- Is er sprake van crisisinterventie? (ja/nee) <abbr title="Is er sprake van een crisisinterventie? Indicator crisisinterventie. "Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te cre&#235;ren om de klant te helpen via de reguliere schuldhulpverlening.
Volgens de Wgs gaat het in elk geval om de volgende situaties:
■ gedwongen woningontruiming;
■ be&#235;indiging van de levering van gas, water, elektriciteit of stadsverwarming;
■ opzegging of ontbinding van de zorgverzekering.
Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals:
■ aangekondigde boedelverkoop of verkoop van de eigen woning;
■ loon- of bankbeslag;
■ een faillissementsaanvraag.
En voor ondernemers:
■ beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt;
■ opzegging van het bankkrediet."">❓</abbr>


### Intake

??? note "Definitie Intake"
    Dit is de fase tussen het eerste gesprek en het Plan van Aanpak. Tijdens de<br>intakefase wordt geinventariseerd welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een duurzaam financieel<br>evenwicht te bereiken.

Hiervan worden de volgende zaken vastgelegd:

- Startdatum van het intakegesprek  <abbr title="Het gesprek dat plaatsvindt na aanmelding of na ontvangst hulpvraag (bijv. bij doorverwijzing vanuit vroegsignalering). Doel van dit gesprek is om de hulpvraag vast te stellen en te beoordelen welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een persoon te helpen om een duurzaam financieel evenwicht te bereiken.">❓</abbr>
- Einddatum van de intake  <abbr title="De datum van afronding van de intake. Een klant ontvangt een gemotiveerde afwijzing of een toelatingsbeschikking. ">❓</abbr>
- Beschikkingsdatum  <abbr title="De datum waarop de beschikking is afgegeven. Het kan hierom verschillende typen beschikking gaan, zoals: afwijzings- toewijsings- of beeindigingsbeschikking. ">❓</abbr>
- Soort beschikking  (mogelijke waarden: Afwijzingsbeschikking, Toelatingsbeschikking)


### Plan van aanpak

??? note "Definitie Planvanaanpak"
    Een document waarin in elk geval het volgende staat:<br>• de hulpvraag van de persoon;<br>• de voorgestelde ondersteuning;<br>• eventueel de organisatie(s) waarnaar je hebt doorverwezen;<br>• de voorwaarden voor schuldhulpverlening (bijvoorbeeld dat de persoon geen nieuwe schulden mag maken).<br>De hoogte van beslagvrije voet voor de persoon (zie artikel 4a:5 van de Wgs) moet in acht worden genomen.

Hiervan worden de volgende zaken vastgelegd:

- Datum afronding plan van aanpak


### Stabilisatie

??? note "Definitie Stabilisatie"
    Fase van het schuldhulpverleningstraject met als doel de inkomsten en uitgaven van een persoon in evenwicht te brengen. De stabilisatie van inkomen en uitgaven is een resultaat van<br>werkzaamheden uit het integrale plan van aanpak. Als stabilisatie bereikt is kan een betalingsregeling, herfinanciering of schuldregeling worden opgezet. Een belangrijk tweede doel is om de hulpvrager hierbij schuldenrust te bieden: stress wegnemen en tijd maken voor oplossingen naar een schuldenzorgvrije toekomst. In de stabilisatiefase kan een schuldhulpverlener andere instrumenten, activiteiten of ondersteuning inzetten, die bijdragen aan de duurzame oplossing van het financiële probleem, zoals budgetcoaching, budgetbeheer, beschermingsbewind of flankerende hulp.

Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum van de stabilisatiefase


### Schuldregeling

??? note "Definitie Schuldregeling"
    De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit (of op andere wijze vastgestelde minimale afdracht) lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt. Voordat de schuldregeling start, sluit je een schuldregelingsovereenkomst met de schuldenaar. Daarin staan de rechten en plichten van beide partijen. Een schuldregeling kan met een saneringskrediet of een schuldbemiddeling gerealiseerd worden. Als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregeling, informeer je de schuldenaar over mogelijke vervolgstappen, zoals het aanvragen van een dwangakkoord (artikel 287a Fw) of toelating tot de Wsnp.

Hiervan worden de volgende zaken vastgelegd:

- Datum aanvraag <abbr title="Datum dat schuldregeling is ingediend.">❓</abbr>
- Afgewezen, toegekend of ingetrokken? Geef de juiste datum
- Is er een dwangakkoord aangevraagd? (ja/nee) <abbr title="Een vervolgstap die mogelijk is als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregelingaanvragen. Dit verzoek wordt ingediend bij de rechtbank (artikel 287a Fw).">❓</abbr>
- Datum verzoek dwangakkoord


### Oplossing

??? note "Definitie Oplossing"
    <font color="#0e0e0e">In de schuldhulpverlening verwijst een “oplossing” naar een regeling waarbij schulden op een beheersbare manier worden afgelost of kwijtgescholden, met als doel de financiële situatie van de schuldenaar te stabiliseren. Er worden verschillende oplossingsvormen onderscheiden, waaronder saneringskrediet, schuldbemiddeling, herfinanciering, betalingsregelingen en schuldregelingen zonder afloscapaciteit. Bij een saneringskrediet ontvangt de schuldenaar een lening om alle schuldeisers in één keer af te betalen, waarna hij deze lening aflost aan de kredietverstrekker. Schuldbemiddeling houdt in dat de schuldenaar gedurende een afgesproken periode periodiek bedragen aflost aan de schuldeisers. Herfinanciering betreft het vervangen van bestaande schulden door een nieuwe lening met gunstigere voorwaarden. Een betalingsregeling is een afspraak tussen schuldenaar en schuldeiser om de schuld in termijnen af te lossen. Bij een schuldregeling zonder afloscapaciteit wordt vastgesteld dat de schuldenaar geen financiële ruimte heeft om af te lossen, wat kan leiden tot kwijtschelding van de schuld. Deze oplossingsvormen worden ingezet afhankelijk van de specifieke situatie van de schuldenaar en zijn gericht op een duurzame oplossing van de schuldenproblematiek.  </font>

Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum
- Soort oplossing (mogelijke waarden: Betalingsregeling, Herfinanciering, Saneringskrediet, Schuldbemiddeling, 0%-aanbod)  
- VTLB-bedrag (per maand) <abbr title="Het “Vrij te laten bedrag” (VTLB) is het bedrag (in hele euro's per maand) dat een persoon of huishouden met schulden mag behouden om in de basisbehoeften te voorzien. Dit bedrag wordt vastgesteld tijdens schuldhulpverleningstrajecten. Het VTLB zorgt ervoor dat iemand niet verder in de problemen komt door schulden af te lossen en tegelijkertijd nog kan voorzien in noodzakelijke kosten van levensonderhoud.">❓</abbr>


### Begeleiding

??? note "Definitie Begeleiding"
    Begeleiding voor clienten in het kader van schuldhulpdienstverlening.

Voor elk type begeleiding worden de volgende gegevens vastgelegd:

- Soort begeleiding (mogelijke waarden: Budgetcoaching, Budgetbeheer, Beschermingsbewind, Lange Termijn Begeleiding (DFD), Budgetbegeleiding)
- Start- en einddatum


### Uitstroom

??? note "Definitie Uitstroom"
    Motivatie voor uitstroom

Het gaat hier over de gegevens ten aanzien van de uitstroom uit het schuldhulptraject. Hievan worden de volgende zaken vastgelegd:

- Datum uitstroom <abbr title="Datum dat clienten uit het schuldhulptraject zijn uitgestroomd">❓</abbr>
- Datum beëindigingsbeschikking <abbr title="Datum dat de Be&#235;indigingsbeschikking is afgegeven.">❓</abbr>
- Reden van uitstroom (mogelijke waarden: Overleden, Verhuisd, Nietverschenen, Ingetrokken, Niet passend, Overig, Voldoet niet, Afgerond, Zelf)

## Aanvullende gegevens

In sommige gevallen spelen er aanvullende zaken. De hiervoor benodigde gegevens worden in de volgende paragrafen beschreven. 


### Crisisinterventie

??? note "Definitie Crisisinterventie"
    Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te creëren om de klant te helpen via de reguliere schuldhulpverlening.<br>Volgens de Wgs gaat het in elk geval om de volgende situaties:<br>• gedwongen woningontruiming;<br>• beëindiging van de levering van gas, water, elektriciteit of stadsverwarming;<br>• opzegging of ontbinding van de zorgverzekering.<br>Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals:<br>• aangekondigde boedelverkoop of verkoop van de eigen woning;<br>• loon- of bankbeslag;<br>• een faillissementsaanvraag.<br>En voor ondernemers:<br>• beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt;<br>• opzegging van het bankkrediet.

Is er sprake geweest van één of meer crisisinterventies? Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum


### Informatie en advies

??? note "Definitie Informatieenadvies"
    Geen Definitie

Wordt er voor de cliënt(en) informatie en advies ingezet? Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum van het informatie- en adviestraject


### Moratorium

??? note "Definitie Moratorium"
    Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter.<br>Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is. Het moratorium is bedoeld om het minnelijke traject te kunnen voortzetten.<br>Het moratorium kan in de volgende situaties worden ingezet:<br>• gedwongen woningontruiming;<br>• beëindiging van de levering van gas, water elektriciteit of stadsverwarming;<br>• opzegging dan wel ontbinding van de zorgverzekering.<br>Het moratorium duurt maximaal zes maanden.

Is er sprake van één of meer moratoria? Hiervan worden de volgende zaken vastgelegd:

- Datum aanvraag
- Datum goedkeuring
- Start- en einddatum


### Voorlopige voorziening

??? note "Definitie "
    Geen Definitie

Is er binnen het schuldhulptraject sprake van één of meer voorlopige voorzieningen? Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum