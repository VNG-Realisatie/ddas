## Objecttypen Model Schuldhulpverlening


### Aanmelding

Het objecttype Aanmelding kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Aanmelding |
| definitie | Moment dat een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn.  |
| bron | [https://www.nvvk.nl/kennisbank-detail/2021/04/13/Module-Aanmelding](https://www.nvvk.nl/kennisbank-detail/2021/04/13/Module-Aanmelding) |
| version | 1.0 |


Attributen van objecttype Aanmelding:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| crisisinterventie | boolean | Is er sprake van een crisisinterventie? Indicator crisisinterventie. "Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te cre&#235;ren om de klant te helpen via de reguliere schuldhulpverlening. Volgens de Wgs gaat het in elk geval om de volgende situaties: ■ gedwongen woningontruiming; ■ be&#235;indiging van de levering van gas, water, elektriciteit of stadsverwarming; ■ opzegging of ontbinding van de zorgverzekering. Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals: ■ aangekondigde boedelverkoop of verkoop van de eigen woning; ■ loon- of bankbeslag; ■ een faillissementsaanvraag. En voor ondernemers: ■ beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt; ■ opzegging van het bankkrediet." | Nee |
| einddatum | Datum |  | Nee |
| startdatum | Datum | Datum waarop een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn.  | Nee |



### Begeleiding

Het objecttype Begeleiding kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Begeleiding |
| definitie | Begeleiding voor clienten in het kader van schuldhulpdienstverlening, die kan bestaan uit: 1. budgetbeheer 2. beschermingsbewind 3. budgetcoaching  |
| bron | [https://www.nvvk.nl/ons-werkveld/gedragscodes-en-modules](https://www.nvvk.nl/ons-werkveld/gedragscodes-en-modules) |
| version | 1.0 |


Attributen van objecttype Begeleiding:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Date |  | Nee |
| soort | Enumeratie: "EnumBegeleidingssoort" |  | Nee |
| startdatum | Date |  | Nee |



### Begeleidingssoort

Het objecttype Begeleidingssoort kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Begeleidingssoort |
| definitie | Soort begeleiding in het kader van schuldhulpverlening |
| bron |  |
| version | 1.0 |


Attributen van objecttype Begeleidingssoort:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| soort | BegeleidingsoortEnum |  | Nee |



### Client

Het objecttype Client kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Client |
| definitie | Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente binnen de sociaal domein. |
| bron |  |
| version | 1.0 |


Attributen van objecttype Client:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| Burgerservicenummer | AN9 |  | Nee |
| Geboortedatum | AN22 | De datum waarop de ander natuurljjk persoon is geboren. | Nee |
| Geslachtsaanduiding |  | Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. | Nee |
| Huisnummer | AN5 |  | Nee |
| Huisnummertoevoeging | AN4 |  | Nee |
| Postcode | AN6 |  | Nee |



### Contactpersoon

Het objecttype Contactpersoon kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Contactpersoon |
| definitie | Contactpersoon van de organisatie waarvan de gegevens worden aangeleverd. |
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

Het objecttype Crisisinterventie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Crisisinterventie |
| definitie | Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te cre&#235;ren om de klant te helpen via de reguliere schuldhulpverlening. Volgens de Wgs gaat het in elk geval om de volgende situaties: ■ gedwongen woningontruiming; ■ be&#235;indiging van de levering van gas, water, elektriciteit of stadsverwarming; ■ opzegging of ontbinding van de zorgverzekering. Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals: ■ aangekondigde boedelverkoop of verkoop van de eigen woning; ■ loon- of bankbeslag; ■ een faillissementsaanvraag. En voor ondernemers: ■ beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt; ■ opzegging van het bankkrediet.  |
| bron |  |
| version | 1.0 |


Attributen van objecttype Crisisinterventie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | datum |  | Nee |
| startdatum | datum |  | Nee |



### InformatieEnAdvies

Het objecttype InformatieEnAdvies kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | InformatieEnAdvies |
| definitie |  |
| bron |  |
| version | 1.0 |


Attributen van objecttype InformatieEnAdvies:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Inkomen

Het objecttype Inkomen kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Inkomen |
| definitie | Inkomen dat door een persoon wordt verworven uit verschillende mogelijke inkomstenbronnen: inkomen uit arbeid, inkomen uit eigen onderneming, uitkering inkomensverzekeringen en uitkering sociale voorzieningen (m.u.v. kinderbijslag en kindgebonden budget). Premies inkomensverzekeringen (m.u.v. premies voor volksverzekeringen) zijn hierop in mindering gebracht. |
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

Het objecttype Intake kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Intake |
| definitie | Dit is de fase tussen het eerste gesprek en het Plan van Aanpak. Tijdens de intakefase wordt geinventariseerd welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een duurzaam financieel evenwicht te bereiken. |
| bron | [https://www.nvvk.nl/kennisbank-detail/2021/04/15/Module-Intake](https://www.nvvk.nl/kennisbank-detail/2021/04/15/Module-Intake) |
| version | 1.0 |


Attributen van objecttype Intake:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| beschikkingsdatum | Datum | De datum waarop de beschikking is afgegeven. Het kan hierom verschillende typen beschikking gaan, zoals: afwijzings- toewijsings- of beeindigingsbeschikking.  | Nee |
| beschikkingssoort | Enumeratie: "EnumBeschikkingssooort" |  | Nee |
| einddatum | Datum | De datum van afronding van de intake. Een klant ontvangt een gemotiveerde afwijzing of een toelatingsbeschikking.  | Nee |
| startdatum | Datum | Het gesprek dat plaatsvindt na aanmelding of na ontvangst hulpvraag (bijv. bij doorverwijzing vanuit vroegsignalering). Doel van dit gesprek is om de hulpvraag vast te stellen en te beoordelen welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een persoon te helpen om een duurzaam financieel evenwicht te bereiken.    | Nee |



### Leefsituatie

Het objecttype Leefsituatie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Leefsituatie |
| definitie | Leefsituatie is de combinatie van factoren zoals schulden, ondernemerschap, aanwezigheid van een partner, en inkomen, die samen de sociale en economische omstandigheden van een individu bepalen. Deze wordt in het kader van schuldhulpverlening gebruikt om alle relevante zaken van clienten aan te koppelen. |
| bron |  |
| version | 1.0 |


Attributen van objecttype Leefsituatie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datumGeldigTot | date |  | Nee |
| datumGeldigVanaf | date |  | Nee |



### Moratorium

Het objecttype Moratorium kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Moratorium |
| definitie | Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter.  Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is. Het moratorium is bedoeld om het minnelijke traject te kunnen voortzetten.  Het moratorium kan in de volgende situaties worden ingezet: - gedwongen woningontruiming; - be&#235;indiging van de levering van gas, water elektriciteit of stadsverwarming; - opzegging dan wel ontbinding van de zorgverzekering.  Het moratorium duurt maximaal zes maanden. |
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

Het objecttype Nazorg kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Nazorg |
| definitie | Ondersteuning die een persoon ontvangt n&#225; een schuldhulptraject, om zo bij de start van een schuldenvrij leven zelfredzaamheid verder te bevorderen &#233;n recidive (terugval) te voorkomen. |
| bron | [https://www.nvvk.nl/kennisbank-detail/2022/07/07/Module-Nazorg?originNode=1401](https://www.nvvk.nl/kennisbank-detail/2022/07/07/Module-Nazorg?originNode=1401) |
| version | 1.0 |


Attributen van objecttype Nazorg:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Ondernemer

Het objecttype Ondernemer kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Ondernemer |
| definitie | Een ondernemer is een individu die die goederen of diensten levert aan anderen om winst te maken. |
| bron | [https://ondernemersplein.kvk.nl/inschrijven-bij-kvk/](https://ondernemersplein.kvk.nl/inschrijven-bij-kvk/) |
| version | 1.0 |


Attributen van objecttype Ondernemer:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Oplossing

Het objecttype Oplossing kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Oplossing |
| definitie | De Oplossing beschrijft in 5 submodules wat de schuldhulpverlener doet om een oplossing te realiseren, en kent de volgende submodules:  - submodule Herfinanciering; - submodule Betalingsregeling; - submodule Saneringskrediet; - submodule Schuldbemiddeling. Het kan ook gaan om een 0%-aanbod |
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

Het objecttype Oplossingssoort kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Oplossingssoort |
| definitie | De soort oplossing in het kader van Schuldhulpverlening |
| bron |  |
| version | 1.0 |


Attributen van objecttype Oplossingssoort:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| soort | SchuldregelingsoortEnum |  | Nee |



### Partner

Het objecttype Partner kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Partner |
| definitie | Een partner is een persoon met wie iemand een romantische en vaak langdurige relatie heeft, gebaseerd op wederzijdse liefde, steun en commitment. |
| bron |  |
| version | 1.0 |


Attributen van objecttype Partner:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| Burgerservicenummer | AN9 |  | Nee |
| Geboortedatum | AN22 | De datum waarop de ander natuurljjk persoon is geboren. | Nee |
| Geslachtsaanduiding | Enumeratie: "geslacht" | Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. | Nee |
| Huisnummer | AN5 |  | Nee |
| Huisnummertoevoeging | AN4 |  | Nee |
| Postcode | AN6 |  | Nee |



### PlanVanAanpak

Het objecttype PlanVanAanpak kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | PlanVanAanpak |
| definitie | Een document waarin in elk geval het volgende staat: ■ de hulpvraag van de persoon; ■ de voorgestelde ondersteuning; ■ eventueel de organisatie(s) waarnaar je hebt doorverwezen; ■ de voorwaarden voor schuldhulpverlening (bijvoorbeeld dat de persoon geen nieuwe schulden mag maken).  De hoogte van beslagvrije voet voor de persoon (zie artikel 4a:5 van de Wgs) moet in acht worden genomen. |
| bron |  |
| version | 1.0 |


Attributen van objecttype PlanVanAanpak:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datumAfronding | Datum |  | Nee |



### Schuld

Het objecttype Schuld kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuld |
| definitie | Een schuld is een financi&#235;le verplichting waarbij een persoon nu of in de toekomst een bedrag moet betalen aan een derde. In het kader van schuldhulpverlening wordt over een schuld gesproken als de persoon niet aan deze verplichting kan voldoen. .  |
| bron |  |
| version | 1.0 |


Attributen van objecttype Schuld:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| bedrag | Bedrag | Bedrag in hele euro's nauwkeurig | Nee |
| peildatum | Date | Peildatum dat de schuld is vastgesteld. | Nee |
| schuldsoort | Enumeratie: "EnumSchuldensoort" |  | Nee |
| zakelijkeSchuld | boolean | Betreft het een zakelijke schuld | Nee |



### Schuldeiser

Het objecttype Schuldeiser kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldeiser |
| definitie | Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar. In de meeste gevallen is de prestatie het betalen van geld. Dit geldbedrag is dan de schuld die de schuldenaar aan de schuldeiser moet betalen. De schuld is meestal het gevolg van het niet nakomen van een verplichting uit een overeenkomst tussen de partijen. De schuldeiser kan de schuldenaar dwingen om de schuld te voldoen. |
| bron | [https://www.ris-rijkschroeff.nl/Kennisbank/Verbintenissenrecht/Schuldeiser](https://www.ris-rijkschroeff.nl/Kennisbank/Verbintenissenrecht/Schuldeiser) |
| version | 1.0 |


Attributen van objecttype Schuldeiser:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| kvknummer | AN20 |  | Nee |
| naam | AN200 |  | Nee |
| Naam | AN200 | De benaming van het SUBJECT | Nee |
| postcode | AN6 |  | Nee |
| privepersoon | boolean |  | Nee |



### Schuldhulporganisatie

Het objecttype Schuldhulporganisatie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldhulporganisatie |
| definitie | Een schuldhulporganisatie is een instantie die individuen en gezinnen helpt met het beheren, verminderen en oplossen van hun schulden door middel van advies, begeleiding en bemiddeling. Het betreft een gemeenten of een SHV-organisatie die de gemeentelijke schuldhulpverleningstaak vanuit een gemeente gemandateerd of gedelegeerd heeft.   |
| bron |  |
| version | 1.0 |


Attributen van objecttype Schuldhulporganisatie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| (Statutaire) Naam | AN500 | Naam van de niet-natuurlijke persoon zoals deze is vastgelegd in de statuten (rechtspersoon) of in de vennootschapsovereenkomst is overeengekomen (Vennootschap onder firma of Commanditaire vennootschap). | Nee |
| gemeentecode | AN4 | De gemeentecode als de aanleverende organisatie een gemeente is. | Nee |
| KvK-nummer | AN8 | Landelijk uniek identificerend administratienummer van een MAATSCHAPPELIJKE ACTIVITEIT behorend bij een SUBJECT zoals toegewezen door de Kamer van Koophandel (KvK). | Nee |
| postcode | AN6 |  | Nee |



### Schuldhulptraject

Het objecttype Schuldhulptraject kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldhulptraject |
| definitie | Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert. |
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

Het objecttype Schuldregeling kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Schuldregeling |
| definitie | De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit (of op andere wijze vastgestelde minimale afdracht) lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt. Voordat de schuldregeling start, sluit je een schuldregelingsovereenkomst met de schuldenaar. Daarin staan de rechten en plichten van beide partijen. Een schuldregeling kan met een saneringskrediet of een schuldbemiddeling gerealiseerd worden. Als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregeling, informeer je de schuldenaar over mogelijke vervolgstappen, zoals het aanvragen van een dwangakkoord (artikel 287a Fw) of toelating tot de Wsnp. |
| bron | [https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Schuldregeling](https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Schuldregeling) |
| version | 1.0 |


Attributen van objecttype Schuldregeling:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| afgewezen | Datum | Datum waarop afwijzingheeft plaatgevonden. Leeg betekent: (nog) geen afwijzing plaatgevonden   | Nee |
| datum | Datum | Datum dat schuldregeling is ingediend. | Nee |
| datumVerzoekDwangakkoord | Datum |  | Nee |
| dwangakkoord | boolean | Een vervolgstap die mogelijk is als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregelingaanvragen. Dit verzoek wordt ingediend bij de rechtbank (artikel 287a Fw). | Nee |
| ingetrokken | Datum | Datum waarop schuldregeling is ingetrokken. Leeg betekent: (nog) geen intrekking plaatgevonden   | Nee |
| toegekend | Datum | Datum waarop toekenning heeft plaatgevonden. Leeg betekent: (nog) geen toekenning plaatgevonden  | Nee |



### Stabilisatie

Het objecttype Stabilisatie kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Stabilisatie |
| definitie | Fase van het schuldhulpverleningstraject met als doel de inkomsten en uitgaven van een persoon in evenwicht te brengen. De stabilisatie van inkomen en uitgaven is een resultaat van werkzaamheden uit het integrale plan van aanpak. Als stabilisatie bereikt is kan een betalingsregeling, herfinanciering of schuldregeling worden opgezet. Een belangrijk tweede doel is om de hulpvrager hierbij schuldenrust te bieden: stress wegnemen en tijd maken voor oplossingen naar een schuldenzorgvrije toekomst. In de stabilisatiefase kan een schuldhulpverlener andere instrumenten, activiteiten of ondersteuning inzetten, die bijdragen aan de duurzame oplossing van het financi&#235;le probleem, zoals budgetcoaching, budgetbeheer, beschermingsbewind of flankerende hulp. |
| bron | [https://www.nvvk.nl/kennisbank-detail/2021/08/16/Module-Stabilisatie](https://www.nvvk.nl/kennisbank-detail/2021/08/16/Module-Stabilisatie) |
| version | 1.0 |


Attributen van objecttype Stabilisatie:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Uitstroom

Het objecttype Uitstroom kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Uitstroom |
| definitie | Motivatie voor uitstroom |
| bron |  |
| version | 1.0 |


Attributen van objecttype Uitstroom:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datum | date |  | Nee |
| omschrijving | text |  | Nee |
| reden | Enumeratie: "EnumUitstroomreden" | Reden dat de hulpverlening op enig moment na aanmelding bij schuldhulpverlening eindigt.   | Nee |



### VoorlopigeVoorziening 

Het objecttype VoorlopigeVoorziening  kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | VoorlopigeVoorziening  |
| definitie |  |
| bron |  |
| version | 1.0 |


Attributen van objecttype VoorlopigeVoorziening :

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| startdatum | Datum |  | Nee |



### Woningbezit

Het objecttype Woningbezit kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Woningbezit |
| definitie | Een koopwoning is een woning die eigendom is van een individu of een entiteit, die het heeft gekocht en waarvoor meestal een hypotheek is afgesloten. |
| bron |  |
| version | 1.0 |


Attributen van objecttype Woningbezit:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| einddatum | Datum |  | Nee |
| soort |  |  | Nee |
| startdatum | Datum |  | Nee |



### WSNP-traject

Het objecttype WSNP-traject kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | WSNP-traject |
| definitie | Een WSNP-traject (Wet schuldsanering natuurlijke personen) is een wettelijk regeling in Nederland waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen. |
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

Het objecttype WSNP-verklaring kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | WSNP-verklaring |
| definitie | Een WSNP-verklaring is een officieel document dat bevestigt dat een persoon toegelaten is tot de Wet Schuldsanering Natuurlijke Personen (WSNP) om hun schulden onder toezicht van een bewindvoerder af te lossen. |
| bron |  |
| version | 1.0 |


Attributen van objecttype WSNP-verklaring:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |






## Enumeraties Model Schuldhulpverlening


### EnumBegeleidingssoort
Geen Definitie

Het enumeratie EnumBegeleidingssoort kent de volgende waarden:

* **Budgetcoaching**: Het bijbrengen van financi&#235;le kennis en vaardigheden zodat een persoon in staat is om zijn eigen geldzaken zelfstandig te regelen (al dan niet met medewerking van derden). 
* **Budgetbeheer**: Het beheren van de inkomsten en het verrichten van betalingen. Dit met als doel om vaste lasten op tijd te betalen om zo te voorkomen dat schulden en betalingsachterstanden ontstaan en/of oplopen.
* **Beschermingsbewind**: Beschermingsbewind is een wettelijke maatregel die bedoeld is om iemands financi&#235;le belangen, volledig of gedeeltelijk, te beschermen als diegene daar zelf niet toe in staat is. Het is bedoeld voor meerderjarigen die niet in staat zijn om hun eigen vermogen te beheren doordat ze:
■ een lichamelijke of geestelijke beperking hebben;
■ hun bezit (dreigen te) verkwisten of problematische schulden hebben.

De kantonrechter beslist of iemand beschermingsbewind nodig heeft. Na uitspraak van de kantonrechter wordt
een bewindvoerder verantwoordelijk om  alle handelingen te verrichten die
aan een goed bewind bijdragen en om betrokkene in en buiten rechte te
vertegenwoordigen.
* **Lange Termijn Begeleiding (DFD)**: <font color="#1e1d3a">Het doel van Duurzame Financi&#235;le Dienstverlening (DFD) is om de inkomsten en uitgaven van een inwoner in evenwicht te brengen als de schulden (nog) niet duurzaam opgelost kunnen worden.</font>
* **Budgetbegeleiding**: Verbeteren financi&#235;le kennis en vaardigheden, door: verhogen van zelfredzaamheid door de financiele vaardigheden, kennis en inzicht van de hulpvrager te ontwikkelen d.m.v. budgetbegeleiding en training.


De enumeratie EnumBegeleidingssoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumBegeleidingssoort |
| definitie | None |
| bron | None |
| version | None |



### EnumBeschikkingssooort
Geen Definitie

Het enumeratie EnumBeschikkingssooort kent de volgende waarden:

* **Afwijzingsbeschikking**: <Geen Definities>
* **Toewijzingsbeschikking**: <Geen Definities>
* **Beeindigingsbeschikking**: <Geen Definities>


De enumeratie EnumBeschikkingssooort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumBeschikkingssooort |
| definitie | None |
| bron | None |
| version | None |



### EnumOplossingssoort
Geen Definitie

Het enumeratie EnumOplossingssoort kent de volgende waarden:

* **Betalingsregeling**: Het volledig (100%) betalen van de vordering(en) in een aantal termijnen.
* **Herfinanciering**: Een financieringsovereenkomst waarmee de vastgestelde vordering(en) ineens en volledig (100%) wordt/worden voldaan.
* **Saneringskrediet**: Het ineens afkopen van de totale schuldenlast tegen finale kwijting, op basis van betaling van een percentage van de totale schuldenlast.De afbetaling aan de schuldeisers is ineens en wordt gedaan met een krediet. De afsluiting van een saneringskrediet gaat via de eigen organisatie als dat een gemeentelijke of andere kredietbank is of de schuldhulpverlener bemiddelt naar een (gemeentelijke) kredietbank, een reguliere bank of een andere financieringsmogelijkheid (bijv. priv&#233;persoon of werkgever), die vervolgens het saneringskrediet verstrekt.
* **Schuldbemiddeling**: Het gedeeltelijk, in termijnen terugbetalen van de totale schuldenlast naar draagkracht, tegen finale kwijting.
* **0%-aanbod**: In een 0%-regeling erkent men dat de schuldenaar geen financi&#235;le ruimte heeft om schulden af te lossen, en daarom wordt er geen aflossing van de schulden gevraagd gedurende de looptijd van de regeling. Na afloop van de afgesproken periode kunnen de schulden, mits aan alle voorwaarden is voldaan, worden kwijtgescholden.


De enumeratie EnumOplossingssoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumOplossingssoort |
| definitie | None |
| bron | None |
| version | None |



### EnumSchuldensoort
Geen Definitie

Het enumeratie EnumSchuldensoort kent de volgende waarden:

* **Zorg**: 
Mogelijke zorgkosten omvatten premies ziektskostenverzekering, kosten eigen bijdragen, en niet verzekerde zorg zoals voor: fysiotherapie, psychologische hulp, tandartszorg, hulpmiddelen en kraamzorg.
* **Publiek**: Kosten voor: Belastingdienst, Dienst Toeslagen, Gemeentebelastingen, CJIB etc
* **Nuts**: <font color="#3f3f3f">Nutsvoorzieningen zijn essenti&#235;le diensten zoals water, gas en elektriciteit die worden geleverd aan huishoudens en bedrijven voor dagelijks gebruik.</font>
* **Overig**: <Geen Definities>


De enumeratie EnumSchuldensoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumSchuldensoort |
| definitie | None |
| bron | None |
| version | None |



### EnumUitstroomreden
Geen Definitie

Het enumeratie EnumUitstroomreden kent de volgende waarden:

* **Overleden**: Client is overleden
* **Verhuisd**: Client is verhuisd naar een andere gemeente
* **Nietverschenen**: Client is niet verschenen
* **Ingetrokken**: Client trekt aanvraag in
* **Niet passend**: Dienstverlening niet (meer) passend
* **Overig**: <Geen Definities>
* **Voldoet niet**: Client voldoet niet aan verplichtingen
* **Afgerond**: Schuldtraject positief doorlopen en afgerond
* **Zelf**: Client heeft schulden zelf geregeld


De enumeratie EnumUitstroomreden heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumUitstroomreden |
| definitie | None |
| bron | None |
| version | None |



### geslacht
Geen Definitie

Het enumeratie geslacht kent de volgende waarden:

* **Man**: <Geen Definities>
* **Vrouw**: <Geen Definities>
* **Onbekend**: <Geen Definities>
* **Leeg**: <Geen Definities>


De enumeratie geslacht heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | geslacht |
| definitie | None |
| bron | None |
| version | None |




