## Objecttypen Model Schuldhulpverlening


### Aanmelding
> **Definitie Aanmelding:** 
>
> Moment dat een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn.

Het objecttype Aanmelding kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Aanmelding |
| bron | [https://www.nvvk.nl/kennisbank-detail/2021/04/13/Module-Aanmelding](https://www.nvvk.nl/kennisbank-detail/2021/04/13/Module-Aanmelding) |
| version | 1.0 |


Attributen van objecttype Aanmelding:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| crisisinterventie | boolean | Is er sprake van een crisisinterventie? Indicator crisisinterventie. "Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te cre&#235;ren om de klant te helpen via de reguliere schuldhulpverlening.<br>Volgens de Wgs gaat het in elk geval om de volgende situaties:<br>• gedwongen woningontruiming;<br>• be&#235;indiging van de levering van gas, water, elektriciteit of stadsverwarming;<br>• opzegging of ontbinding van de zorgverzekering.<br>Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals:<br>• aangekondigde boedelverkoop of verkoop van de eigen woning;<br>• loon- of bankbeslag;<br>• een faillissementsaanvraag.<br>En voor ondernemers:<br>• beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt;<br>• opzegging van het bankkrediet." | Nee |
| einddatum | Datum |  | Nee |
| startdatum | Datum | Datum waarop een persoon met een hulpvraag komt rondom (dreigende) schulden, en het eerste contact met schuldhulpverlening is geweest. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn. | Nee |



### Begeleiding
> **Definitie Begeleiding:** 
>
> Begeleiding voor clienten in het kader van schuldhulpdienstverlening.

Het objecttype Begeleiding kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Begeleiding |
| bron | [https://www.nvvk.nl/ons-werkveld/gedragscodes-en-modules](https://www.nvvk.nl/ons-werkveld/gedragscodes-en-modules) |
| version | 1.0 |


Attributen van objecttype Begeleiding:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Date |  | Nee |
| soort | Enumeratie: "EnumBegeleidingssoort" |  | Nee |
| startdatum | Date |  | Nee |



### Begeleidingssoort
> **Definitie Begeleidingssoort:** 
>
> Soort begeleiding in het kader van schuldhulpverlening

Het objecttype Begeleidingssoort kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Begeleidingssoort |
| bron |  |
| version | 1.0 |


Attributen van objecttype Begeleidingssoort:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| soort | BegeleidingsoortEnum |  | Nee |



### Client
> **Definitie Client:** 
>
> Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente.

Het objecttype Client kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Client |
| bron |  |
| version | 1.5 |


Attributen van objecttype Client:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| burgerservicenummer | AN9 |  | Nee |
| Geboortedatum | Datum | De datum waarop de ander natuurlijk persoon is geboren. | Nee |
| geslachtsaanduiding | Enumeratie: "geslacht" | Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. | Nee |
| Huisnummer | AN5 |  | Nee |
| Huisnummertoevoeging | AN4 |  | Nee |
| Postcode | AN6 |  | Nee |



### Contactpersoon
> **Definitie Contactpersoon:** 
>
> Contactpersoon van de organisatie waarvan de gegevens worden aangeleverd.

Het objecttype Contactpersoon kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Contactpersoon |
| bron |  |
| version | 1.0 |


Attributen van objecttype Contactpersoon:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| email | email |  | Nee |
| functietitel | AN200 |  | Nee |
| naam | AN200 |  | Nee |
| telefoonnummer | AN200 |  | Nee |



### Crisisinterventie
> **Definitie Crisisinterventie:** 
>
> Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te cre&#235;ren om de klant te helpen via de reguliere schuldhulpverlening.<br>Volgens de Wgs gaat het in elk geval om de volgende situaties:<br>• gedwongen woningontruiming;<br>• be&#235;indiging van de levering van gas, water, elektriciteit of stadsverwarming;<br>• opzegging of ontbinding van de zorgverzekering.<br>Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals:<br>• aangekondigde boedelverkoop of verkoop van de eigen woning;<br>• loon- of bankbeslag;<br>• een faillissementsaanvraag.<br>En voor ondernemers:<br>• beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt;<br>• opzegging van het bankkrediet.

Het objecttype Crisisinterventie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Crisisinterventie |
| bron |  |
| version | 1.0 |


Attributen van objecttype Crisisinterventie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | datum |  | Nee |
| startdatum | datum |  | Nee |



### InformatieEnAdvies
> **Definitie InformatieEnAdvies:** 
>
> <font color="#1e1d3a">Het betreft hier de activiteiten die in het kader van Informatie en advies worden uitgevoerd. Het doel van Informatie en Advies is inwoners zelf in staat te stellen een duurzaam financieel evenwicht te bereiken. Het kan een beroep op uitgebreidere vormen van dienstverlening overbodig maken.</font>

Het objecttype InformatieEnAdvies kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | InformatieEnAdvies |
| bron |  |
| version | 1.0 |


Attributen van objecttype InformatieEnAdvies:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Inkomen
> **Definitie Inkomen:** 
>
> Inkomen dat door een persoon wordt verworven uit verschillende mogelijke inkomstenbronnen: inkomen uit arbeid, inkomen uit eigen onderneming, uitkering inkomensverzekeringen en uitkering sociale voorzieningen (m.u.v. kinderbijslag en kindgebonden budget). Premies inkomensverzekeringen (m.u.v. premies voor volksverzekeringen) zijn hierop in mindering gebracht.

Het objecttype Inkomen kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Inkomen |
| bron |  |
| version | 1.0 |


Attributen van objecttype Inkomen:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| brutoBedrag | Bedrag |  | Nee |
| einddatum | Date |  | Nee |
| inkomenscategorie | int |  | Nee |
| inkomstenbron | int |  | Nee |
| nettoBedrag | Bedrag |  | Nee |
| startdatum | Date |  | Nee |



### Intake
> **Definitie Intake:** 
>
> Dit is de fase tussen het eerste gesprek en het Plan van Aanpak. Tijdens de intakefase wordt geinventariseerd welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een duurzaam financieel evenwicht te bereiken.

Het objecttype Intake kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Intake |
| bron | [https://www.nvvk.nl/kennisbank-detail/2021/04/15/Module-Intake](https://www.nvvk.nl/kennisbank-detail/2021/04/15/Module-Intake) |
| version | 1.0 |


Attributen van objecttype Intake:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| beschikkingsdatum | Datum | De datum waarop de beschikking is afgegeven. | Nee |
| beschikkingssoort | Enumeratie: "EnumBeschikkingssoort" |  | Nee |
| einddatum | Datum | De datum van afronding van de intake. Een klant ontvangt een gemotiveerde afwijzing of een toelatingsbeschikking. | Nee |
| startdatum | Datum | Het gesprek dat plaatsvindt na aanmelding of na ontvangst hulpvraag (bijv. bij doorverwijzing vanuit vroegsignalering). Doel van dit gesprek is om de hulpvraag vast te stellen en te beoordelen welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een persoon te helpen om een duurzaam financieel evenwicht te bereiken. | Nee |



### Leefsituatie
> **Definitie Leefsituatie:** 
>
> Leefsituatie is de combinatie van factoren zoals schulden, ondernemerschap, aanwezigheid van een partner, en inkomen, die samen de sociale en economische omstandigheden van een individu bepalen. Deze wordt in het kader van schuldhulpverlening gebruikt om alle relevante zaken van clienten aan te koppelen.

Het objecttype Leefsituatie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Leefsituatie |
| bron |  |
| version | 1.0 |


Attributen van objecttype Leefsituatie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datumGeldigTot | date |  | Nee |
| datumGeldigVanaf | date |  | Nee |



### Moratorium
> **Definitie Moratorium:** 
>
> Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter.<br>Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is. Het moratorium is bedoeld om het minnelijke traject te kunnen voortzetten.<br>Het moratorium kan in de volgende situaties worden ingezet:<br>• gedwongen woningontruiming;<br>• be&#235;indiging van de levering van gas, water elektriciteit of stadsverwarming;<br>• opzegging dan wel ontbinding van de zorgverzekering.<br>Het moratorium duurt maximaal zes maanden.

Het objecttype Moratorium kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Moratorium |
| bron |  |
| version | 1.0 |


Attributen van objecttype Moratorium:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datumAanvraag | Datum |  | Nee |
| datumGoedkeuring | Datum |  | Nee |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Nazorg
> **Definitie Nazorg:** 
>
> Ondersteuning die een persoon ontvangt n&#225; een schuldhulptraject, om zo bij de start van een schuldenvrij leven zelfredzaamheid verder te bevorderen &#233;n recidive (terugval) te voorkomen.

Het objecttype Nazorg kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Nazorg |
| bron | [https://www.nvvk.nl/kennisbank-detail/2022/07/07/Module-Nazorg?originNode=1401](https://www.nvvk.nl/kennisbank-detail/2022/07/07/Module-Nazorg?originNode=1401) |
| version | 1.0 |


Attributen van objecttype Nazorg:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Ondernemer
> **Definitie Ondernemer:** 
>
> Een ondernemer is een individu die die goederen of diensten levert aan anderen om winst te maken.

Het objecttype Ondernemer kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Ondernemer |
| bron | [https://ondernemersplein.kvk.nl/inschrijven-bij-kvk/](https://ondernemersplein.kvk.nl/inschrijven-bij-kvk/) |
| version | 1.0 |


Attributen van objecttype Ondernemer:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Oplossing
> **Definitie Oplossing:** 
>
> <font color="#0e0e0e">In de schuldhulpverlening verwijst een “oplossing” naar een regeling waarbij schulden op een beheersbare manier worden afgelost of kwijtgescholden, met als doel de financi&#235;le situatie van de schuldenaar te stabiliseren. Er worden verschillende oplossingsvormen onderscheiden, waaronder saneringskrediet, schuldbemiddeling, herfinanciering, betalingsregelingen en schuldregelingen zonder afloscapaciteit. Bij een saneringskrediet ontvangt de schuldenaar een lening om alle schuldeisers in &#233;&#233;n keer af te betalen, waarna hij deze lening aflost aan de kredietverstrekker. Schuldbemiddeling houdt in dat de schuldenaar gedurende een afgesproken periode periodiek bedragen aflost aan de schuldeisers. Herfinanciering betreft het vervangen van bestaande schulden door een nieuwe lening met gunstigere voorwaarden. Een betalingsregeling is een afspraak tussen schuldenaar en schuldeiser om de schuld in termijnen af te lossen. Bij een schuldregeling zonder afloscapaciteit wordt vastgesteld dat de schuldenaar geen financi&#235;le ruimte heeft om af te lossen, wat kan leiden tot kwijtschelding van de schuld. Deze oplossingsvormen worden ingezet afhankelijk van de specifieke situatie van de schuldenaar en zijn gericht op een duurzame oplossing van de schuldenproblematiek.  </font>

Het objecttype Oplossing kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Oplossing |
| bron | [https://www.nvvk.nl/l/library/download/urn:uuid:eba70d82-a0a0-40c4-9dd2-4c4aee7f0ed9/nvvk-module-12-oplossingen-221219.pdf](https://www.nvvk.nl/l/library/download/urn:uuid:eba70d82-a0a0-40c4-9dd2-4c4aee7f0ed9/nvvk-module-12-oplossingen-221219.pdf) |
| version | 1.0 |


Attributen van objecttype Oplossing:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum | Het gaat om het moment dat een schuldregeling (saneringskrediet/schuldbemiddeling) of volledige afbetalingsregeling (betalingsregeling/herfinanciering) daadwerkelijk eindigt. Dit kan zijn na de formele afgesproken periode of een voortijdige beeindiging. | Nee |
| soort | Enumeratie: "EnumOplossingssoort" |  | Nee |
| startdatum | Datum | Het gaat om het moment dat een schuldregeling (saneringskrediet/schuldbemiddeling) of volledige afbetalingsregeling (betalingsregeling/herfinanciering) daadwerkelijk start na goedkeuring van de aanvraag. | Nee |
| vtlb | Bedrag | Het “Vrij te laten bedrag” (VTLB) is het bedrag (in hele euro's per maand) dat een persoon of huishouden met schulden mag behouden om in de basisbehoeften te voorzien. Dit bedrag wordt vastgesteld tijdens schuldhulpverleningstrajecten. Het VTLB zorgt ervoor dat iemand niet verder in de problemen komt door schulden af te lossen en tegelijkertijd nog kan voorzien in noodzakelijke kosten van levensonderhoud. | Nee |



### Oplossingssoort
> **Definitie Oplossingssoort:** 
>
> De soort oplossing in het kader van Schuldhulpverlening

Het objecttype Oplossingssoort kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Oplossingssoort |
| bron |  |
| version | 1.0 |


Attributen van objecttype Oplossingssoort:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| soort | SchuldregelingsoortEnum |  | Nee |



### Partner
> **Definitie Partner:** 
>
> Een partner is een persoon met wie iemand een romantische en vaak langdurige relatie heeft, gebaseerd op wederzijdse liefde, steun en commitment.

Het objecttype Partner kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Partner |
| bron |  |
| version | 1.0 |


Attributen van objecttype Partner:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| burgerservicenummer | AN9 |  | Nee |
| Geboortedatum | Datum | De datum waarop de ander natuurlijk persoon is geboren. | Nee |
| geslachtsaanduiding |  | Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. | Nee |
| Huisnummer | AN5 |  | Nee |
| Huisnummertoevoeging | AN4 |  | Nee |
| Postcode | AN6 |  | Nee |



### PlanVanAanpak
> **Definitie PlanVanAanpak:** 
>
> Een document waarin in elk geval het volgende staat:<br>• de hulpvraag van de persoon;<br>• de voorgestelde ondersteuning;<br>• eventueel de organisatie(s) waarnaar je hebt doorverwezen;<br>• de voorwaarden voor schuldhulpverlening (bijvoorbeeld dat de persoon geen nieuwe schulden mag maken).<br>De hoogte van beslagvrije voet voor de persoon (zie artikel 4a:5 van de Wgs) moet in acht worden genomen.

Het objecttype PlanVanAanpak kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | PlanVanAanpak |
| bron |  |
| version | 1.0 |


Attributen van objecttype PlanVanAanpak:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datumAfronding | Datum |  | Nee |



### Schuld
> **Definitie Schuld:** 
>
> Een schuld is een financi&#235;le verplichting waarbij een persoon nu of in de toekomst een bedrag moet betalen aan een derde. In het kader van schuldhulpverlening wordt over een schuld gesproken als de persoon niet aan deze verplichting kan voldoen. .

Het objecttype Schuld kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuld |
| bron |  |
| version | 1.0 |


Attributen van objecttype Schuld:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| bedrag | Bedrag | Bedrag in hele euro's nauwkeurig | Nee |
| peildatum | Date | Datum dat de schuld is vastgesteld. Het betreft hier het moment dat de vaststelling door de schuldhulpverlener in het kader van het schuldhulptraject is gedaan. | Nee |
| schuldsoort | Enumeratie: "EnumSchuldensoort" |  | Nee |
| zakelijkeSchuld | boolean | Betreft het een zakelijke schuld | Nee |



### Schuldeiser
> **Definitie Schuldeiser:** 
>
> Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar. In de meeste gevallen is de prestatie het betalen van geld. Dit geldbedrag is dan de schuld die de schuldenaar aan de schuldeiser moet betalen. De schuld is meestal het gevolg van het niet nakomen van een verplichting uit een overeenkomst tussen de partijen. De schuldeiser kan de schuldenaar dwingen om de schuld te voldoen.

Het objecttype Schuldeiser kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldeiser |
| bron | [https://www.ris-rijkschroeff.nl/Kennisbank/Verbintenissenrecht/Schuldeiser](https://www.ris-rijkschroeff.nl/Kennisbank/Verbintenissenrecht/Schuldeiser) |
| version | 1.0 |


Attributen van objecttype Schuldeiser:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| KVKnummer | AN20 |  | Nee |
| naam | AN200 |  | Nee |
| postcode | AN6 |  | Nee |
| privepersoon | boolean |  | Nee |



### Schuldhulporganisatie
> **Definitie Schuldhulporganisatie:** 
>
> Een schuldhulporganisatie is een instantie die individuen en gezinnen helpt met het beheren, verminderen en oplossen van hun schulden door middel van advies, begeleiding en bemiddeling.<br>Het betreft een gemeenten of een SHV-organisatie die de gemeentelijke schuldhulpverleningstaak vanuit een gemeente gemandateerd of gedelegeerd heeft.

Het objecttype Schuldhulporganisatie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldhulporganisatie |
| bron |  |
| version | 1.0 |


Attributen van objecttype Schuldhulporganisatie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| gemeentecode | AN4 | De gemeentecode als de aanleverende organisatie een gemeente is. | Nee |
| postcode | AN6 |  | Nee |



### Schuldhulptraject
> **Definitie Schuldhulptraject:** 
>
> Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert.

Het objecttype Schuldhulptraject kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldhulptraject |
| bron |  |
| version | 1.0 |


Attributen van objecttype Schuldhulptraject:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | date |  | Nee |
| gemeentecode | AN4 | De gemeentecode van de gemeente onder wiens verantwoordelijkheid het schuldhulptraject wordt uitgevoerd. | Nee |
| omschrijving | text |  | Nee |
| startdatum | date |  | Nee |
| toekenningsdatum | date |  | Nee |
| totaalSchuldbedragBijAanvangSchuld | Bedrag | Bedrag in hele euro's nauwkeurig voor elke schuld die meegaat in de schuldregeling. Per schuldeiser kunnen er meerdere openstaande schulden zijn. Deze afzonderlijk meenemen. | Nee |



### Schuldregeling
> **Definitie Schuldregeling:** 
>
> De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit (of op andere wijze vastgestelde minimale afdracht) lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt. Voordat de schuldregeling start, sluit je een schuldregelingsovereenkomst met de schuldenaar. Daarin staan de rechten en plichten van beide partijen. Een schuldregeling kan met een saneringskrediet of een schuldbemiddeling gerealiseerd worden. Als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregeling, informeer je de schuldenaar over mogelijke vervolgstappen, zoals het aanvragen van een dwangakkoord (artikel 287a Fw) of toelating tot de Wsnp.

Het objecttype Schuldregeling kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldregeling |
| bron | [https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Schuldregeling](https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Schuldregeling) |
| version | 1.0 |


Attributen van objecttype Schuldregeling:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| afgewezen | Datum | Datum waarop afwijzingheeft plaatgevonden. Leeg betekent: (nog) geen afwijzing plaatgevonden | Nee |
| datum | Datum | Datum dat schuldregeling door de schuldhulpverlener is ingediend. | Nee |
| datumVerzoekDwangakkoord | Datum |  | Nee |
| dwangakkoord | boolean | Een vervolgstap die mogelijk is als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregelingaanvragen. Dit verzoek wordt ingediend bij de rechtbank (artikel 287a Fw). | Nee |
| ingetrokken | Datum | Datum waarop schuldregeling is ingetrokken. Leeg betekent: (nog) geen intrekking plaatgevonden | Nee |
| toegekend | Datum | Datum waarop toekenning heeft plaatgevonden. Leeg betekent: (nog) geen toekenning plaatgevonden | Nee |



### Stabilisatie
> **Definitie Stabilisatie:** 
>
> Fase van het schuldhulpverleningstraject met als doel de inkomsten en uitgaven van een persoon in evenwicht te brengen. De stabilisatie van inkomen en uitgaven is een resultaat van werkzaamheden uit het plan van aanpak. Als stabilisatie bereikt is kan een betalingsregeling, herfinanciering of schuldregeling worden opgezet. Een belangrijk tweede doel is om de hulpvrager hierbij schuldenrust te bieden: stress wegnemen en tijd maken voor oplossingen naar een schuldenzorgvrije toekomst.<br>In de stabilisatiefase kan een schuldhulpverlener andere instrumenten, activiteiten of ondersteuning inzetten, die bijdragen aan de duurzame oplossing van het financi&#235;le probleem, zoals budgetcoaching, budgetbeheer, beschermingsbewind of flankerende hulp.

Het objecttype Stabilisatie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Stabilisatie |
| bron | [https://www.nvvk.nl/kennisbank-detail/2021/08/16/Module-Stabilisatie](https://www.nvvk.nl/kennisbank-detail/2021/08/16/Module-Stabilisatie) |
| version | 1.0 |


Attributen van objecttype Stabilisatie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Uitstroom
> **Definitie Uitstroom:** 
>
> Het betreft hier de gegevens die worden vastgelegd bij uitstroom en dus be&#235;indiging van een schuldhulptraject.

Het objecttype Uitstroom kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Uitstroom |
| bron |  |
| version | 1.0 |


Attributen van objecttype Uitstroom:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datum | date | Datum dat clienten uit het schuldhulptraject zijn uitgestroomd. Deze datum is gelijk aan de datum be&#235;indigingsbeschikking. | Nee |
| datumBeeindigingsbeschikking | Datum | Datum dat de Be&#235;indigingsbeschikking is afgegeven. | Nee |
| omschrijving | text |  | Nee |
| reden | Enumeratie: "EnumUitstroomreden" | Reden dat de hulpverlening op enig moment na aanmelding bij schuldhulpverlening eindigt. | Nee |



### VoorlopigeVoorziening 
> **Definitie VoorlopigeVoorziening :** 
>
> <font color="#0e0e0e">Een voorlopige voorziening is een tijdelijke regeling die de hulpvrager beschermt tegen verslechtering van zijn financi&#235;le situatie of het verlies van essenti&#235;le voorzieningen (zoals energie, woning, zorg), totdat een schuldregelingstraject is gestart of er meer duidelijkheid is over de vervolgstappen.</font><br><font color="#0e0e0e"><br></font><font color="#0e0e0e">Voorbeelden van voorlopige voorzieningen:</font><br><font color="#0e0e0e">	•	Tijdelijke betalingsregelingen met schuldeisers</font><br><font color="#0e0e0e">	•	Een moratorium (tijdelijke opschorting van afbetalingen)</font><br><font color="#0e0e0e">	•	Het aanvragen van uitstel van betaling bij woningcorporaties of energiebedrijven</font><br><font color="#0e0e0e">	•	Hulp bij het voorkomen van afsluiting van gas, water, licht of ontruiming</font><br><font color="#0e0e0e">	•	Budgetbeheer of beschermingsbewind als tijdelijke maatregel</font>

Het objecttype VoorlopigeVoorziening  kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | VoorlopigeVoorziening |
| bron |  |
| version | 1.0 |


Attributen van objecttype VoorlopigeVoorziening :

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Woningbezit
> **Definitie Woningbezit:** 
>
> Een koopwoning is een woning die eigendom is van een individu of een entiteit, die het heeft gekocht en waarvoor meestal een hypotheek is afgesloten.

Het objecttype Woningbezit kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Woningbezit |
| bron |  |
| version | 1.0 |


Attributen van objecttype Woningbezit:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| soort |  |  | Nee |
| startdatum | Datum |  | Nee |



### WSNP-traject
> **Definitie WSNP-traject:** 
>
> Een WSNP-traject (Wet schuldsanering natuurlijke personen) is een wettelijk regeling in Nederland waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen.

Het objecttype WSNP-traject kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | WSNP-traject |
| bron |  |
| version | 1.0 |


Attributen van objecttype WSNP-traject:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datumGoedkeuring | Datum |  | Nee |
| datumVerzoek | Datum |  | Nee |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### WSNP-verklaring
> **Definitie WSNP-verklaring:** 
>
> Een WSNP-verklaring is een officieel document dat bevestigt dat een persoon toegelaten is tot de Wet Schuldsanering Natuurlijke Personen (WSNP) om hun schulden onder toezicht van een bewindvoerder af te lossen.

Het objecttype WSNP-verklaring kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | WSNP-verklaring |
| bron |  |
| version | 1.0 |


Attributen van objecttype WSNP-verklaring:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |






## Enumeraties Model Schuldhulpverlening


### EnumBegeleidingssoort
> **Definitie EnumBegeleidingssoort:** 
>
> Lijst met alle soorten begeleiding die worden onderkend.

Het enumeratie EnumBegeleidingssoort kent de volgende waarden:


  
  * **Beschermingsbewind**: Beschermingsbewind is een wettelijke maatregel die bedoeld is om iemands financi&#235;le belangen, volledig of gedeeltelijk, te beschermen als diegene daar zelf niet toe in staat is. Het is bedoeld voor meerderjarigen die niet in staat zijn om hun eigen vermogen te beheren doordat ze:<br>• een lichamelijke of geestelijke beperking hebben;<br>• hun bezit (dreigen te) verkwisten of problematische schulden hebben.<br>De kantonrechter beslist of iemand beschermingsbewind nodig heeft. Na uitspraak van de kantonrechter wordt<br>een bewindvoerder verantwoordelijk om  alle handelingen te verrichten die<br>aan een goed bewind bijdragen en om betrokkene in en buiten rechte te<br>vertegenwoordigen.
  

  
  * **Budgetbegeleiding**: Verbeteren financi&#235;le kennis en vaardigheden, door: verhogen van zelfredzaamheid door de financiele vaardigheden, kennis en inzicht van de hulpvrager te ontwikkelen d.m.v. budgetbegeleiding en training.
  

  
  * **Budgetbeheer**: Het beheren van de inkomsten en het verrichten van betalingen. Dit met als doel om vaste lasten op tijd te betalen om zo te voorkomen dat schulden en betalingsachterstanden ontstaan en/of oplopen.
  

  
  * **Budgetcoaching**: Het bijbrengen van financi&#235;le kennis en vaardigheden zodat een persoon in staat is om zijn eigen geldzaken zelfstandig te regelen (al dan niet met medewerking van derden).
  

  
  * **Lange Termijn Begeleiding (DFD)**: <font color="#1e1d3a">Het doel van Duurzame Financi&#235;le Dienstverlening (DFD) is om de inkomsten en uitgaven van een inwoner in evenwicht te brengen als de schulden (nog) niet duurzaam opgelost kunnen worden.</font>
  


De enumeratie EnumBegeleidingssoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumBegeleidingssoort |
| bron |  |
| version | 1.0 |



### EnumBeschikkingssoort
> **Definitie EnumBeschikkingssoort:** 
>
> Lijst met alle soorten beschikkingen die worden onderkend.

Het enumeratie EnumBeschikkingssoort kent de volgende waarden:


  
  * **Afwijzingsbeschikking**: <Geen Definities>
  

  
  * **Toelatingsbeschikking**: <Geen Definities>
  


De enumeratie EnumBeschikkingssoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumBeschikkingssoort |
| bron |  |
| version | 1.0 |



### EnumOplossingssoort
> **Definitie EnumOplossingssoort:** 
>
> Lijst met alle soorten oplossingen in het kader van schuldhulpverleniung die worden onderkend.

Het enumeratie EnumOplossingssoort kent de volgende waarden:


  
  * **0%-aanbod**: In een 0%-regeling erkent men dat de schuldenaar geen financi&#235;le ruimte heeft om schulden af te lossen, en daarom wordt er geen aflossing van de schulden gevraagd gedurende de looptijd van de regeling. Na afloop van de afgesproken periode kunnen de schulden, mits aan alle voorwaarden is voldaan, worden kwijtgescholden.
  

  
  * **Betalingsregeling**: Het volledig (100%) betalen van de vordering(en) in een aantal termijnen.
  

  
  * **Herfinanciering**: Een financieringsovereenkomst waarmee de vastgestelde vordering(en) ineens en volledig (100%) wordt/worden voldaan.
  

  
  * **Saneringskrediet**: Het ineens afkopen van de totale schuldenlast tegen finale kwijting, op basis van betaling van een percentage van de totale schuldenlast.De afbetaling aan de schuldeisers is ineens en wordt gedaan met een krediet. De afsluiting van een saneringskrediet gaat via de eigen organisatie als dat een gemeentelijke of andere kredietbank is of de schuldhulpverlener bemiddelt naar een (gemeentelijke) kredietbank, een reguliere bank of een andere financieringsmogelijkheid (bijv. priv&#233;persoon of werkgever), die vervolgens het saneringskrediet verstrekt.
  

  
  * **Schuldbemiddeling**: Het gedeeltelijk, in termijnen terugbetalen van de totale schuldenlast naar draagkracht, tegen finale kwijting.
  


De enumeratie EnumOplossingssoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumOplossingssoort |
| bron |  |
| version | 1.0 |



### EnumSchuldensoort
> **Definitie EnumSchuldensoort:** 
>
> Lijst met alle cattegori&#235;n van soorten schulden die worden onderkend in het kader van schuldhulpverlening.

Het enumeratie EnumSchuldensoort kent de volgende waarden:


  
  * **Nuts**: Bij organisaties die werken met meterstanden wordt het kenmerk 'Nuts' geregistreerd. De schuldhulpverlenende organisatie is dan verplicht om de meterstanden mee te sturen als een schuldregeling wordt opgestart.
  

  
  * **Overig**: Alle schulden die niet onder &#233;&#233;n van de andere categorie&#235;n zijn in te delen.
  

  
  * **Publiek**: Publieke organisaties krijgen het kenmerk 'Publiek' ; als een schuldregeling wordt opgestart wordt dan altijd het BSN meegestuurd.
  

  
  * **Zorg**: Mogelijke zorgkosten omvatten premies ziektskostenverzekering, kosten eigen bijdragen, en niet verzekerde zorg zoals voor: fysiotherapie, psychologische hulp, tandartszorg, hulpmiddelen en kraamzorg.
  


De enumeratie EnumSchuldensoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumSchuldensoort |
| bron |  |
| version | 1.0 |



### EnumUitstroomreden
> **Definitie EnumUitstroomreden:** 
>
> Lijst met alle soorten uitstroom die bij schuldhulptrajecten worden onderkend.

Het enumeratie EnumUitstroomreden kent de volgende waarden:


  
  * **Afgerond**: Schuldtraject positief doorlopen en afgerond
  

  
  * **Ingetrokken**: Client trekt aanvraag in
  

  
  * **Niet passend**: Dienstverlening niet (meer) passend
  

  
  * **Nietverschenen**: Client is niet verschenen
  

  
  * **Overig**: <Geen Definities>
  

  
  * **Overleden**: Client is overleden
  

  
  * **Verhuisd**: Client is verhuisd naar een andere gemeente
  

  
  * **Voldoet niet**: Client voldoet niet aan verplichtingen
  

  
  * **Zelf**: Client heeft schulden zelf geregeld
  


De enumeratie EnumUitstroomreden heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumUitstroomreden |
| bron |  |
| version | 1.0 |



### geslacht
> **Definitie geslacht:** 
>
> Geen Definitie

Het enumeratie geslacht kent de volgende waarden:


  
  * **Leeg**: <Geen Definities>
  

  
  * **Man**: <Geen Definities>
  

  
  * **Onbekend**: <Geen Definities>
  

  
  * **Vrouw**: <Geen Definities>
  


De enumeratie geslacht heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | geslacht |
| bron |  |
| version | 1.4 |




