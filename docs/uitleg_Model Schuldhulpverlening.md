# Uitleg uitwisselspecificatie 

Schuldhulporganisaties leveren gegevens aan het CBS via een speciaal digitaal bestand (JSON-bestand). In dit bestand staan gegevens over schuldhulptrajecten. Hoe dit bestand technisch is opgebouwd, wordt uitgelegd onder het kopje ‘Uitwisselspecificatie’.
Voor schuldhulporganisaties is het belangrijk om de juiste gegevens goed vast te leggen in hun eigen systemen. Als dat niet goed gebeurt, wordt het moeilijker om de gegevens op de juiste manier aan te leveren.
Op deze pagina leggen we in niet-technische taal uit welke informatie je als organisatie moet vastleggen, zodat je de gegevens goed en volledig kunt aanleveren volgens de DDAS-richtlijnen aan het CBS.

## Algemene gegevens

Bij ieder schuldhulptraject zijn de hieronder weergegeven gegevens van belang.

### Cliëntgegevens

- Burgerservicenummer (BSN)
- Geboortedatum
- Geslacht (we houden de volgende waarden aan: Man, Vrouw, Onbekend, Leeg)
- Postcode
- Huisnummer en eventueel huisnummertoevoeging

Er kunnen minimaal één en maximaal twee personen per traject worden opgevoerd. 

!!! danger "Let op: persoonsgegevens zijn van belang"
    Het is belangrijk dat, of het BSN, of alle andere gegevens zijn vastgelegd. Dit maakt het mogelijk om doublures te corrigeren, om aansluiting te maken met andere data-aanleveringen en om gegevens op individu-niveau te verrijken met andere CBS-data


### Gegevens over schulden

Voor elke schuld die in het schuldhulptraject wordt meegenomen:

- Bedrag
- Peildatum <button onclick="alert('Definitie peildatum: Datum dat de schuld is vastgesteld. Het betreft hier het moment dat de vaststelling door de schuldhulpverlener in het kader van het schuldhulptraject is gedaan.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Soort schuld (we houden de volgende waarden aan: Zorg, Publiek, Nuts, Overig - dit is gelijk aan het Schuldenknooppunt)
- Is het een zakelijke schuld? (ja/nee)
- Gegevens van de schuldeiser (naam, KvK-nummer, postcode, privépersoon ja/nee)

## Gegevens over het schuldhulptraject

Het schuldhulptraject kent conform het NVVK-Referentieproces een aantal fases. Van deze fases is steeds een aantal gegevens van belang. Deze worden in de volgende paragrafen beschreven.

Naast de gegevens van de verschillende fases zijn per schuldhulptraject een aantal gegevens van belang die betrekking hebben op het schuldhulptraject als geheel:

- Startdatum van het schuldhulptraject
- Einddatum (als het schuldhulptraject is afgerond)
- Toekenningsdatum (toekenningsdatum bevat de datum waarop de schuldregeling is toegekend)
- Gemeentecode (gemeente onder wiens verantwoordelijkheid het traject wordt uitgevoerd)
- Totaal schuldbedrag bij aanvang traject 


### Aanmelding

??? note "Definitie Aanmelding"
    Moment dat een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn.

Hiervan worden de volgende zaken vastgelegd:

- Startdatum van de aanmelding <button onclick="alert('Definitie startdatum: Datum waarop een persoon met een hulpvraag komt rondom (dreigende) schulden, en het eerste contact met schuldhulpverlening is geweest. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Einddatum van de aanmeldfase (optioneel)
- Is er sprake van crisisinterventie? (ja/nee + start- en einddatum crisisinterventie)


### Intake

??? note "Definitie Intake"
    Dit is de fase tussen het eerste gesprek en het Plan van Aanpak. Tijdens de intakefase wordt geinventariseerd welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een duurzaam financieel evenwicht te bereiken.

Hiervan worden de volgende zaken vastgelegd:

- Startdatum van het intakegesprek  <button onclick="alert('Definitie startdatum: Het gesprek dat plaatsvindt na aanmelding of na ontvangst hulpvraag (bijv. bij doorverwijzing vanuit vroegsignalering). Doel van dit gesprek is om de hulpvraag vast te stellen en te beoordelen welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een persoon te helpen om een duurzaam financieel evenwicht te bereiken.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Einddatum van de intake  <button onclick="alert('Definitie einddatum: De datum van afronding van de intake. Een klant ontvangt een gemotiveerde afwijzing of een toelatingsbeschikking.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Beschikkingsdatum  <button onclick="alert('Definitie beschikkingsdatum: De datum waarop de beschikking is afgegeven.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Soort beschikking  (mogelijke waarden: Afwijzingsbeschikking, Toelatingsbeschikking)


### Plan van aanpak

??? note "Definitie Plan Van Aanpak"
    Een document waarin in elk geval het volgende staat:<br>• de hulpvraag van de persoon;<br>• de voorgestelde ondersteuning;<br>• eventueel de organisatie(s) waarnaar je hebt doorverwezen;<br>• de voorwaarden voor schuldhulpverlening (bijvoorbeeld dat de persoon geen nieuwe schulden mag maken).<br>De hoogte van beslagvrije voet voor de persoon (zie artikel 4a:5 van de Wgs) moet in acht worden genomen.

Hiervan worden de volgende zaken vastgelegd:

- Datum afronding plan van aanpak


### Stabilisatie

??? note "Definitie Stabilisatie"
    Fase van het schuldhulpverleningstraject met als doel de inkomsten en uitgaven van een persoon in evenwicht te brengen. De stabilisatie van inkomen en uitgaven is een resultaat van werkzaamheden uit het plan van aanpak. Als stabilisatie bereikt is kan een betalingsregeling, herfinanciering of schuldregeling worden opgezet. Een belangrijk tweede doel is om de hulpvrager hierbij schuldenrust te bieden: stress wegnemen en tijd maken voor oplossingen naar een schuldenzorgvrije toekomst.<br>In de stabilisatiefase kan een schuldhulpverlener andere instrumenten, activiteiten of ondersteuning inzetten, die bijdragen aan de duurzame oplossing van het financi&#235;le probleem, zoals budgetcoaching, budgetbeheer, beschermingsbewind of flankerende hulp.

Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum van de stabilisatiefase


### Schuldregeling

??? note "Definitie Schuldregeling"
    De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit (of op andere wijze vastgestelde minimale afdracht) lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt. Voordat de schuldregeling start, sluit je een schuldregelingsovereenkomst met de schuldenaar. Daarin staan de rechten en plichten van beide partijen. Een schuldregeling kan met een saneringskrediet of een schuldbemiddeling gerealiseerd worden. Als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregeling, informeer je de schuldenaar over mogelijke vervolgstappen, zoals het aanvragen van een dwangakkoord (artikel 287a Fw) of toelating tot de Wsnp.

Hiervan worden de volgende zaken vastgelegd:

- Datum aanvraag <button onclick="alert('Definitie datum: Datum dat schuldregeling door de schuldhulpverlener is ingediend.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Afgewezen, toegekend of ingetrokken? Geef de juiste datum
- Is er een dwangakkoord aangevraagd? (ja/nee) <button onclick="alert('Definitie dwangakkoord: Een vervolgstap die mogelijk is als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregelingaanvragen. Dit verzoek wordt ingediend bij de rechtbank (artikel 287a Fw).')" style="background:none;border:none;cursor:pointer;">❓</button>
- Datum verzoek dwangakkoord


### Oplossing

??? note "Definitie Oplossing"
    <font color="#0e0e0e">In de schuldhulpverlening verwijst een “oplossing” naar een regeling waarbij schulden op een beheersbare manier worden afgelost of kwijtgescholden, met als doel de financi&#235;le situatie van de schuldenaar te stabiliseren. Er worden verschillende oplossingsvormen onderscheiden, waaronder saneringskrediet, schuldbemiddeling, herfinanciering, betalingsregelingen en schuldregelingen zonder afloscapaciteit. Bij een saneringskrediet ontvangt de schuldenaar een lening om alle schuldeisers in &#233;&#233;n keer af te betalen, waarna hij deze lening aflost aan de kredietverstrekker. Schuldbemiddeling houdt in dat de schuldenaar gedurende een afgesproken periode periodiek bedragen aflost aan de schuldeisers. Herfinanciering betreft het vervangen van bestaande schulden door een nieuwe lening met gunstigere voorwaarden. Een betalingsregeling is een afspraak tussen schuldenaar en schuldeiser om de schuld in termijnen af te lossen. Bij een schuldregeling zonder afloscapaciteit wordt vastgesteld dat de schuldenaar geen financi&#235;le ruimte heeft om af te lossen, wat kan leiden tot kwijtschelding van de schuld. Deze oplossingsvormen worden ingezet afhankelijk van de specifieke situatie van de schuldenaar en zijn gericht op een duurzame oplossing van de schuldenproblematiek.  </font>

Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum
- Soort (mogelijke waarden: Betalingsregeling, Herfinanciering, Saneringskrediet, Schuldbemiddeling, 0%-aanbod)  
- VTLB-bedrag (per maand) van de cliënt


### Financiële begeleiding

??? note "Definitie Begeleiding"
    Begeleiding voor clienten in het kader van schuldhulpdienstverlening.

Voor elke vorm van financiële begeleiding:

- Soort begeleiding (mogelijke waarden: Budgetcoaching, Budgetbeheer, Beschermingsbewind, Lange Termijn Begeleiding (DFD), Budgetbegeleiding)
- Start- en einddatum


### Uitstroom

??? note "Definitie Uitstroom"
    Het betreft hier de gegevens die worden vastgelegd bij uitstroom en dus be&#235;indiging van een schuldhulptraject.

Het gaat hier over de gegevens ten aanzien van de uitstroom uit het schuldhulptraject. Hievan worden de volgende zaken vastgelegd:

- Datum uitstroom <button onclick="alert('Definitie datum: Datum dat clienten uit het schuldhulptraject zijn uitgestroomd. Deze datum is gelijk aan de datum be&#235;indigingsbeschikking.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Datum beëindigingsbeschikking <button onclick="alert('Definitie datumBeeindigingsbeschikking: Datum dat de Be&#235;indigingsbeschikking is afgegeven.')" style="background:none;border:none;cursor:pointer;">❓</button>
- Reden van uitstroom (mogelijke waarden: Overleden, Verhuisd, Nietverschenen, Ingetrokken, Niet passend, Overig, Voldoet niet, Afgerond, Zelf)

## Aanvullende gegevens

In sommige gevallen spelen er aanvullende zaken. De hiervoor benodigde gegevens worden in de volgende paragrafen beschreven. 


### Crisisinterventie

??? note "Definitie Crisisinterventie"
    Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te cre&#235;ren om de klant te helpen via de reguliere schuldhulpverlening.<br>Volgens de Wgs gaat het in elk geval om de volgende situaties:<br>• gedwongen woningontruiming;<br>• be&#235;indiging van de levering van gas, water, elektriciteit of stadsverwarming;<br>• opzegging of ontbinding van de zorgverzekering.<br>Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals:<br>• aangekondigde boedelverkoop of verkoop van de eigen woning;<br>• loon- of bankbeslag;<br>• een faillissementsaanvraag.<br>En voor ondernemers:<br>• beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt;<br>• opzegging van het bankkrediet.

Is er sprake geweest van één of meer crisisinterventies? Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum


### Informatie en advies

??? note "Definitie Informatie En Advies"
    <font color="#1e1d3a">Het betreft hier de activiteiten die in het kader van Informatie en advies worden uitgevoerd. Het doel van Informatie en Advies is inwoners zelf in staat te stellen een duurzaam financieel evenwicht te bereiken. Het kan een beroep op uitgebreidere vormen van dienstverlening overbodig maken.</font>

Wordt er voor de cliënt(en) informatie en advies ingezet? Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum van het informatie- en adviestraject


### Moratorium

??? note "Definitie Moratorium"
    Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter.<br>Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is. Het moratorium is bedoeld om het minnelijke traject te kunnen voortzetten.<br>Het moratorium kan in de volgende situaties worden ingezet:<br>• gedwongen woningontruiming;<br>• be&#235;indiging van de levering van gas, water elektriciteit of stadsverwarming;<br>• opzegging dan wel ontbinding van de zorgverzekering.<br>Het moratorium duurt maximaal zes maanden.

Is er sprake van één of meer moratoria? Hiervan worden de volgende zaken vastgelegd:

- Datum aanvraag
- Datum goedkeuring
- Start- en einddatum


### Voorlopige voorziening

??? note "Definitie Voorlopige Voorziening "
    <font color="#0e0e0e">Een voorlopige voorziening is een tijdelijke regeling die de hulpvrager beschermt tegen verslechtering van zijn financi&#235;le situatie of het verlies van essenti&#235;le voorzieningen (zoals energie, woning, zorg), totdat een schuldregelingstraject is gestart of er meer duidelijkheid is over de vervolgstappen.</font><br><font color="#0e0e0e"><br></font><font color="#0e0e0e">Voorbeelden van voorlopige voorzieningen:</font><br><font color="#0e0e0e">	•	Tijdelijke betalingsregelingen met schuldeisers</font><br><font color="#0e0e0e">	•	Een moratorium (tijdelijke opschorting van afbetalingen)</font><br><font color="#0e0e0e">	•	Het aanvragen van uitstel van betaling bij woningcorporaties of energiebedrijven</font><br><font color="#0e0e0e">	•	Hulp bij het voorkomen van afsluiting van gas, water, licht of ontruiming</font><br><font color="#0e0e0e">	•	Budgetbeheer of beschermingsbewind als tijdelijke maatregel</font>

Is er binnen het schuldhulptraject sprake van één of meer voorlopige voorzieningen? Hiervan worden de volgende zaken vastgelegd:

- Start- en einddatum