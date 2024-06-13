# Informatiemodel in detail

## Objecttypen Schulhulpverlening

### Aanmelding

Het objecttype Aanmelding kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                   |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Aanmelding                                                                                                                                               |
| definitie  | Moment dat een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn. |
| bron       | <https://www.nvvk.nl/kennisbank-detail/2021/04/13/Module-Aanmelding>                                                                                     |
| version    | 1.0                                                                                                                                                      |

Attributen van objecttype Aanmelding:

| Attribuut         | Datatype | Omschrijving | Verplicht |
|-------------------|----------|--------------|-----------|
| crisisinterventie | boolean  |              | Nee       |
| einddatum         | Datum    |              | Nee       |
| startdatum        | Datum    |              | Nee       |

### Begeleiding

Het objecttype Begeleiding kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Begeleiding                                                                                                                                        |
| definitie  | Begeleiding voor clienten in het kader van schuldhulpdienstverlening, die kan bestaan uit: 1. budgetbeheer 2. beschermingsbewind 3. budgetcoaching |
| bron       | <https://www.nvvk.nl/ons-werkveld/gedragscodes-en-modules>                                                                                         |
| version    | 1.0                                                                                                                                                |

Attributen van objecttype Begeleiding:

| Attribuut  | Datatype                            | Omschrijving | Verplicht |
|------------|-------------------------------------|--------------|-----------|
| einddatum  | Datum                               |              | Nee       |
| soort      | Enumeratie: “EnumBegeleidingssoort” |              | Nee       |
| startdatum | Datum                               |              | Nee       |

### Begeleidingssoort

Het objecttype Begeleidingssoort kent de volgende eigenschappen:

| Eigenschap | Waarde                                                 |
|------------|--------------------------------------------------------|
| name       | Begeleidingssoort                                      |
| definitie  | Soort begeleiding in het kader van schuldhulpverlening |
| bron       |                                                        |
| version    | 1.0                                                    |

Attributen van objecttype Begeleidingssoort:

| Attribuut | Datatype             | Omschrijving | Verplicht |
|-----------|----------------------|--------------|-----------|
| soort     | BegeleidingsoortEnum |              | Nee       |

### Contactpersoon

Het objecttype Contactpersoon kent de volgende eigenschappen:

| Eigenschap | Waarde                             |
|------------|------------------------------------|
| name       | Contactpersoon                     |
| definitie  | Contactpersoon van een organisatie |
| bron       |                                    |
| version    | 1.0                                |

Attributen van objecttype Contactpersoon:

| Attribuut | Datatype | Omschrijving | Verplicht |
|-----------|----------|--------------|-----------|

### Crisisinterventie

Het objecttype Crisisinterventie kent de volgende eigenschappen:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Eigenschap</th>
<th>Waarde</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>name</td>
<td>Crisisinterventie</td>
</tr>
<tr class="even">
<td>definitie</td>
<td>Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te creëren om de klant te helpen via de reguliere schuldhulpverlening. Volgens de Wgs gaat het in elk geval om de volgende situaties:
■ gedwongen woningontruiming;
■ beëindiging van de levering van gas, water, elektriciteit of stadsverwarming;
■ opzegging of ontbinding van de zorgverzekering.
Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals:
■ aangekondigde boedelverkoop of verkoop van de eigen woning;
■ loon- of bankbeslag;
■ een faillissementsaanvraag. En voor ondernemers:
■ beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt;
■ opzegging van het bankkrediet.</td>
</tr>
<tr class="odd">
<td>bron</td>
<td></td>
</tr>
<tr class="even">
<td>version</td>
<td>1.0</td>
</tr>
</tbody>
</table>

Attributen van objecttype Crisisinterventie:

| Attribuut  | Datatype | Omschrijving | Verplicht |
|------------|----------|--------------|-----------|
| einddatum  | datum    |              | Nee       |
| startdatum | datum    |              | Nee       |

### Inkomen

Het objecttype Inkomen kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                                                                                                                                    |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Inkomen                                                                                                                                                                                                                                                                                                                                                                   |
| definitie  | Inkomen dat door een persoon wordt verworven uit verschillende mogelijke inkomstenbronnen: inkomen uit arbeid, inkomen uit eigen onderneming, uitkering inkomensverzekeringen en uitkering sociale voorzieningen (m.u.v. kinderbijslag en kindgebonden budget). Premies inkomensverzekeringen (m.u.v. premies voor volksverzekeringen) zijn hierop in mindering gebracht. |
| bron       |                                                                                                                                                                                                                                                                                                                                                                           |
| version    | 1.0                                                                                                                                                                                                                                                                                                                                                                       |

Attributen van objecttype Inkomen:

| Attribuut         | Datatype | Omschrijving | Verplicht |
|-------------------|----------|--------------|-----------|
| brutoBedrag       | Bedrag   |              | Nee       |
| einddatum         | Datum    |              | Nee       |
| inkomenscategorie | int      |              | Nee       |
| inkomstenbron     | int      |              | Nee       |
| nettoBedrag       | Bedrag   |              | Nee       |
| startdatum        | Datum    |              | Nee       |

### Intake

Het objecttype Intake kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                 |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Intake                                                                                                                                                                                                                                 |
| definitie  | Dit is de fase tussen het eerste gesprek en het Plan van Aanpak. Tijdens de intakefase wordt geinventariseerd welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een duurzaam financieel evenwicht te bereiken. |
| bron       | <https://www.nvvk.nl/kennisbank-detail/2021/04/15/Module-Intake>                                                                                                                                                                       |
| version    | 1.0                                                                                                                                                                                                                                    |

Attributen van objecttype Intake:

| Attribuut             | Datatype | Omschrijving | Verplicht |
|-----------------------|----------|--------------|-----------|
| einddatum             | Datum    |              | Nee       |
| startdatum            | Datum    |              | Nee       |
| toelatingsbeschikking | Datum    |              | Nee       |

### Koopwoning

Het objecttype Koopwoning kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Koopwoning                                                                                                                                            |
| definitie  | Een koopwoning is een woning die eigendom is van een individu of een entiteit, die het heeft gekocht en waarvoor meestal een hypotheek is afgesloten. |
| bron       |                                                                                                                                                       |
| version    | 1.0                                                                                                                                                   |

Attributen van objecttype Koopwoning:

| Attribuut  | Datatype | Omschrijving | Verplicht |
|------------|----------|--------------|-----------|
| einddatum  | Datum    |              | Nee       |
| startdatum | Datum    |              | Nee       |
| waarde     | Bedrag   |              | Nee       |

### Leefsituatie

Het objecttype Leefsituatie kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                                                                            |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Leefsituatie                                                                                                                                                                                                                                                                                                      |
| definitie  | Leefsituatie is de combinatie van factoren zoals schulden, ondernemerschap, aanwezigheid van een partner, en inkomen, die samen de sociale en economische omstandigheden van een individu bepalen. Deze wordt in het kader van schuldhulpverlening gebruikt om alle relevante zaken van clienten aan te koppelen. |
| bron       |                                                                                                                                                                                                                                                                                                                   |
| version    | 1.0                                                                                                                                                                                                                                                                                                               |

Attributen van objecttype Leefsituatie:

| Attribuut        | Datatype | Omschrijving | Verplicht |
|------------------|----------|--------------|-----------|
| datumGeldigTot   | datum    |              | Nee       |
| datumGeldigVanaf | datum    |              | Nee       |

### Moratorium

Het objecttype Moratorium kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Moratorium                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| definitie  | Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter. Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is. Het moratorium is bedoeld om het minnelijke traject te kunnen voortzetten. Het moratorium kan in de volgende situaties worden ingezet: - gedwongen woningontruiming; - beëindiging van de levering van gas, water elektriciteit of stadsverwarming; - opzegging dan wel ontbinding van de zorgverzekering. Het moratorium duurt maximaal zes maanden. |
| bron       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| version    | 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

Attributen van objecttype Moratorium:

| Attribuut        | Datatype | Omschrijving | Verplicht |
|------------------|----------|--------------|-----------|
| datumAanvraag    | Datum    |              | Nee       |
| datumGoedkeuring | Datum    |              | Nee       |
| einddatum        | Datum    |              | Nee       |
| startdatum       | Datum    |              | Nee       |

### Nazorg

Het objecttype Nazorg kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                        |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Nazorg                                                                                                                                                                                        |
| definitie  | Ondersteuning die een persoon ontvangt ná een schuldregelingstraject, om zo bij de start van een schuldenvrij leven zelfredzaamheid verder te bevorderen én recidive (terugval) te voorkomen. |
| bron       | <https://www.nvvk.nl/kennisbank-detail/2022/07/07/Module-Nazorg?originNode=1401>                                                                                                              |
| version    | 1.0                                                                                                                                                                                           |

Attributen van objecttype Nazorg:

| Attribuut  | Datatype | Omschrijving | Verplicht |
|------------|----------|--------------|-----------|
| einddatum  | Datum    |              | Nee       |
| startdatum | Datum    |              | Nee       |

### Ondernemer

Het objecttype Ondernemer kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                            |
|------------|---------------------------------------------------------------------------------------------------|
| name       | Ondernemer                                                                                        |
| definitie  | Een ondernemer is een individu die die goederen of diensten levert aan anderen om winst te maken. |
| bron       | <https://ondernemersplein.kvk.nl/inschrijven-bij-kvk/>                                            |
| version    | 1.0                                                                                               |

Attributen van objecttype Ondernemer:

| Attribuut  | Datatype | Omschrijving | Verplicht |
|------------|----------|--------------|-----------|
| einddatum  | Datum    |              | Nee       |
| startdatum | Datum    |              | Nee       |

### Oplossing

Het objecttype Oplossing kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                          |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Oplossing                                                                                                                                                                                                                                                       |
| definitie  | De Oplossing beschrijft in 4 submodules wat de schuldhulpverlener doet om een oplossing te realiseren, en kent de volgende submodules: - submodule Herfinanciering; - submodule Betalingsregeling; - submodule Saneringskrediet; - submodule Schuldbemiddeling. |
| bron       | <https://www.nvvk.nl/l/library/download/urn:uuid:eba70d82-a0a0-40c4-9dd2-4c4aee7f0ed9/nvvk-module-12-oplossingen-221219.pdf>                                                                                                                                    |
| version    | 1.0                                                                                                                                                                                                                                                             |

Attributen van objecttype Oplossing:

| Attribuut  | Datatype                          | Omschrijving | Verplicht |
|------------|-----------------------------------|--------------|-----------|
| einddatum  | Datum                             |              | Nee       |
| soort      | Enumeratie: “EnumOplossingssoort” |              | Nee       |
| startdatum | Datum                             |              | Nee       |

### Oplossingssoort

Het objecttype Oplossingssoort kent de volgende eigenschappen:

| Eigenschap | Waarde                                                  |
|------------|---------------------------------------------------------|
| name       | Oplossingssoort                                         |
| definitie  | De soort oplossing in het kader van Schuldhulpverlening |
| bron       |                                                         |
| version    | 1.0                                                     |

Attributen van objecttype Oplossingssoort:

| Attribuut | Datatype                | Omschrijving | Verplicht |
|-----------|-------------------------|--------------|-----------|
| soort     | SchuldregelingsoortEnum |              | Nee       |

### Partner

Het objecttype Partner kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                            |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Partner                                                                                                                                           |
| definitie  | Een partner is een persoon met wie iemand een romantische en vaak langdurige relatie heeft, gebaseerd op wederzijdse liefde, steun en commitment. |
| bron       |                                                                                                                                                   |
| version    | 1.0                                                                                                                                               |

Attributen van objecttype Partner:

| Attribuut                      | Datatype | Omschrijving | Verplicht |
|--------------------------------|----------|--------------|-----------|
| datumTot                       | Datum    |              | Nee       |
| datumVanaf                     | Datum    |              | Nee       |
| getrouwdOfGeregistreerdPartner | boolean  |              | Nee       |
| samenwonend                    | boolean  |              | Nee       |

### PlanVanAanpak

Het objecttype PlanVanAanpak kent de volgende eigenschappen:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Eigenschap</th>
<th>Waarde</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>name</td>
<td>PlanVanAanpak</td>
</tr>
<tr class="even">
<td>definitie</td>
<td>Een document waarin in elk geval het volgende staat:
■ de hulpvraag van de persoon;
■ de voorgestelde ondersteuning;
■ eventueel de organisatie(s) waarnaar je hebt doorverwezen;
■ de voorwaarden voor schuldhulpverlening (bijvoorbeeld dat de persoon geen nieuwe schulden mag maken).
De hoogte van beslagvrije voet voor de persoon (zie artikel 4a:5 van de Wgs) moet in acht worden genomen.</td>
</tr>
<tr class="odd">
<td>bron</td>
<td></td>
</tr>
<tr class="even">
<td>version</td>
<td>1.0</td>
</tr>
</tbody>
</table>

Attributen van objecttype PlanVanAanpak:

| Attribuut      | Datatype | Omschrijving | Verplicht |
|----------------|----------|--------------|-----------|
| datumAfronding | Datum    |              | Nee       |

### Project

Het objecttype Project kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Project                                                                                                                                                                                  |
| definitie  | Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat. |
| bron       |                                                                                                                                                                                          |
| version    | 1.0                                                                                                                                                                                      |

Attributen van objecttype Project:

| Attribuut         | Datatype          | Omschrijving | Verplicht |
|-------------------|-------------------|--------------|-----------|
| einddatum         | datum             |              | Nee       |
| omschrijving      | text              |              | Nee       |
| resultaat         | ResultaatSHV      |              | Nee       |
| startdatum        | datum             |              | Nee       |
| toekennningsdatum | datum             |              | Nee       |
| uitstroomreden    | UitstroomredenSHV |              | Nee       |

### Projectsoort

Het objecttype Projectsoort kent de volgende eigenschappen:

| Eigenschap | Waarde                   |
|------------|--------------------------|
| name       | Projectsoort             |
| definitie  | Typering van een project |
| bron       |                          |
| version    | 1.0                      |

Attributen van objecttype Projectsoort:

| Attribuut    | Datatype | Omschrijving | Verplicht |
|--------------|----------|--------------|-----------|
| naam         | AN80     |              | Nee       |
| omschrijving | text     |              | Nee       |

### Resultaat

Het objecttype Resultaat kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                          |
|------------|---------------------------------------------------------------------------------|
| name       | Resultaat                                                                       |
| definitie  | De uitkomst van iets, bijvoorbeeld een berekening of een onderzoek. een gevolg. |
| bron       |                                                                                 |
| version    | 1.0                                                                             |

Attributen van objecttype Resultaat:

| Attribuut    | Datatype | Omschrijving | Verplicht |
|--------------|----------|--------------|-----------|
| datum        | datum    |              | Nee       |
| naam         | AN80     |              | Nee       |
| omschrijving | text     |              | Nee       |

### Resultaatsoort

Het objecttype Resultaatsoort kent de volgende eigenschappen:

| Eigenschap | Waarde                     |
|------------|----------------------------|
| name       | Resultaatsoort             |
| definitie  | Typering van een resultaat |
| bron       |                            |
| version    | 1.0                        |

Attributen van objecttype Resultaatsoort:

| Attribuut    | Datatype | Omschrijving | Verplicht |
|--------------|----------|--------------|-----------|
| naam         | AN80     |              | Nee       |
| omschrijving | text     |              | Nee       |

### Schuld

Het objecttype Schuld kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                           |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Schuld                                                                                                                                                                                           |
| definitie  | Een financiële schuld is een verplichting waarbij een individu, bedrijf of instelling een geldbedrag verschuldigd is aan een ander partij en dit bedrag op een later tijdstip moet terugbetalen. |
| bron       |                                                                                                                                                                                                  |
| version    | 1.0                                                                                                                                                                                              |

Attributen van objecttype Schuld:

| Attribuut       | Datatype                        | Omschrijving | Verplicht |
|-----------------|---------------------------------|--------------|-----------|
| bedrag          | Bedrag                          |              | Nee       |
| peildatum       | Datum                           |              | Nee       |
| soort           | Enumeratie: “EnumSchuldensoort” |              | Nee       |
| zakelijkeSchuld | boolean                         |              | Nee       |

### Schuldeiser

Het objecttype Schuldeiser kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Schuldeiser                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| definitie  | Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar. In de meeste gevallen is de prestatie het betalen van geld. Dit geldbedrag is dan de schuld die de schuldenaar aan de schuldeiser moet betalen. De schuld is meestal het gevolg van het niet nakomen van een verplichting uit een overeenkomst tussen de partijen. De schuldeiser kan de schuldenaar dwingen om de schuld te voldoen. |
| bron       | <https://www.ris-rijkschroeff.nl/Kennisbank/Verbintenissenrecht/Schuldeiser>                                                                                                                                                                                                                                                                                                                                                                |
| version    | 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                         |

Attributen van objecttype Schuldeiser:

| Attribuut | Datatype                           | Omschrijving | Verplicht |
|-----------|------------------------------------|--------------|-----------|
| peildatum | Datum                              |              | Nee       |
| soort     | Enumeratie: “EnumSchuleiserssoort” |              | Nee       |

### Schuldhulporganisatie

Het objecttype Schuldhulporganisatie kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Schuldhulporganisatie                                                                                                                                                                     |
| definitie  | Een schuldhulporganisatie is een instantie die individuen en gezinnen helpt met het beheren, verminderen en oplossen van hun schulden door middel van advies, begeleiding en bemiddeling. |
| bron       |                                                                                                                                                                                           |
| version    | 1.0                                                                                                                                                                                       |

Attributen van objecttype Schuldhulporganisatie:

| Attribuut | Datatype | Omschrijving | Verplicht |
|-----------|----------|--------------|-----------|

### Schuldhulptraject

Het objecttype Schuldhulptraject kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                        |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Schuldhulptraject                                                                                                                                                                                                             |
| definitie  | Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert. |
| bron       |                                                                                                                                                                                                                               |
| version    | 1.0                                                                                                                                                                                                                           |

Attributen van objecttype Schuldhulptraject:

| Attribuut                          | Datatype | Omschrijving | Verplicht |
|------------------------------------|----------|--------------|-----------|
| einddatum                          | datum    |              | Nee       |
| naam                               | AN80     |              | Nee       |
| omschrijving                       | text     |              | Nee       |
| startdatum                         | datum    |              | Nee       |
| toekenningsdatum                   | datum    |              | Nee       |
| totaalSchuldbedragBijAanvangSchuld | Bedrag   |              | Nee       |

### Schuldregeling

Het objecttype Schuldregeling kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Schuldregeling                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| definitie  | De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit (of op andere wijze vastgestelde minimale afdracht) lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt. Voordat de schuldregeling start, sluit je een schuldregelingsovereenkomst met de schuldenaar. Daarin staan de rechten en plichten van beide partijen. Een schuldregeling kan met een saneringskrediet of een schuldbemiddeling gerealiseerd worden. Als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregeling, informeer je de schuldenaar over mogelijke vervolgstappen, zoals het aanvragen van een dwangakkoord (artikel 287a Fw) of toelating tot de Wsnp. |
| bron       | <https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Schuldregeling>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| version    | 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

Attributen van objecttype Schuldregeling:

| Attribuut                | Datatype | Omschrijving | Verplicht |
|--------------------------|----------|--------------|-----------|
| afgewezen                | Datum    |              | Nee       |
| datum                    | Datum    |              | Nee       |
| datumVerzoekDwangakkoord | Datum    |              | Nee       |
| dwangakkoord             | boolean  |              | Nee       |
| ingetrokken              | Datum    |              | Nee       |
| toegekend                | Darum    |              | Nee       |

### Stabilisatie

Het objecttype Stabilisatie kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | Stabilisatie                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| definitie  | Fase van het schuldhulpverleningstraject met als doel de inkomsten en uitgaven van een persoon in evenwicht te brengen. De stabilisatie van inkomen en uitgaven is een resultaat van werkzaamheden uit het integrale plan van aanpak. Als stabilisatie bereikt is kan een betalingsregeling, herfinanciering of schuldregeling worden opgezet. Een belangrijk tweede doel is om de hulpvrager hierbij schuldenrust te bieden: stress wegnemen en tijd maken voor oplossingen naar een schuldenzorgvrije toekomst. In de stabilisatiefase kan een schuldhulpverlener andere instrumenten, activiteiten of ondersteuning inzetten, die bijdragen aan de duurzame oplossing van het financiële probleem, zoals budgetcoaching, budgetbeheer, beschermingsbewind of flankerende hulp. |
| bron       | <https://www.nvvk.nl/kennisbank-detail/2021/08/16/Module-Stabilisatie>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| version    | 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

Attributen van objecttype Stabilisatie:

| Attribuut  | Datatype | Omschrijving | Verplicht |
|------------|----------|--------------|-----------|
| einddatum  | Datum    |              | Nee       |
| startdatum | Datum    |              | Nee       |

### Uitstroomreden

Het objecttype Uitstroomreden kent de volgende eigenschappen:

| Eigenschap | Waarde                   |
|------------|--------------------------|
| name       | Uitstroomreden           |
| definitie  | Motivatie voor uitstroom |
| bron       |                          |
| version    | 1.0                      |

Attributen van objecttype Uitstroomreden:

| Attribuut    | Datatype | Omschrijving | Verplicht |
|--------------|----------|--------------|-----------|
| datum        | datum    |              | Nee       |
| omschrijving | text     |              | Nee       |

### Uitstroomredensoort

Het objecttype Uitstroomredensoort kent de volgende eigenschappen:

| Eigenschap | Waarde                          |
|------------|---------------------------------|
| name       | Uitstroomredensoort             |
| definitie  | Typering van een uitstroomreden |
| bron       |                                 |
| version    | 1.0                             |

Attributen van objecttype Uitstroomredensoort:

| Attribuut    | Datatype | Omschrijving | Verplicht |
|--------------|----------|--------------|-----------|
| naam         | AN80     |              | Nee       |
| omschrijving | text     |              | Nee       |

### WSNP-traject

Het objecttype WSNP-traject kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                                                                                                  |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | WSNP-traject                                                                                                                                                                                                                                                                            |
| definitie  | Een WSNP-traject (Wet schuldsanering natuurlijke personen) is een wettelijk regeling in Nederland waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen. |
| bron       |                                                                                                                                                                                                                                                                                         |
| version    | 1.0                                                                                                                                                                                                                                                                                     |

Attributen van objecttype WSNP-traject:

| Attribuut        | Datatype | Omschrijving | Verplicht |
|------------------|----------|--------------|-----------|
| datumGoedkeuring | Datum    |              | Nee       |
| datumVerzoek     | Datum    |              | Nee       |
| einddatum        | Datum    |              | Nee       |
| startdatum       | Datum    |              | Nee       |

### WSNP-verklaring

Het objecttype WSNP-verklaring kent de volgende eigenschappen:

| Eigenschap | Waarde                                                                                                                                                                                                             |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name       | WSNP-verklaring                                                                                                                                                                                                    |
| definitie  | Een WSNP-verklaring is een officieel document dat bevestigt dat een persoon toegelaten is tot de Wet Schuldsanering Natuurlijke Personen (WSNP) om hun schulden onder toezicht van een bewindvoerder af te lossen. |
| bron       |                                                                                                                                                                                                                    |
| version    | 1.0                                                                                                                                                                                                                |

Attributen van objecttype WSNP-verklaring:

| Attribuut | Datatype | Omschrijving | Verplicht |
|-----------|----------|--------------|-----------|

## Enumeraties Model Schulhulpverlening

### EnumBegeleidingssoort

Het enumeratie EnumBegeleidingssoort kent de volgende waarden:

- **Budgetcoaching**:
- **Budgetbeheer**:
- **Beschermingsbewind**:

De enumeratie EnumBegeleidingssoort heeft de volgende kenmerken:

| Kenmerk   | Waarde                |
|-----------|-----------------------|
| name      | EnumBegeleidingssoort |
| definitie | None                  |
| bron      | None                  |
| version   | None                  |

### EnumHuishoudenssoort

Het enumeratie EnumHuishoudenssoort kent de volgende waarden:

- **Particulier Huishouden**:
- **Instituuttioneel Huishouden**:

De enumeratie EnumHuishoudenssoort heeft de volgende kenmerken:

| Kenmerk   | Waarde               |
|-----------|----------------------|
| name      | EnumHuishoudenssoort |
| definitie | None                 |
| bron      | None                 |
| version   | None                 |

### EnumOplossingssoort

Het enumeratie EnumOplossingssoort kent de volgende waarden:

- **Betalingsregeling**:
- **Herfinanciering**:
- **Saneringskrediet**:
- **Schuldbemiddeling**:

De enumeratie EnumOplossingssoort heeft de volgende kenmerken:

| Kenmerk   | Waarde              |
|-----------|---------------------|
| name      | EnumOplossingssoort |
| definitie | None                |
| bron      | None                |
| version   | None                |

### EnumSchuldensoort

Het enumeratie EnumSchuldensoort kent de volgende waarden:

- **Zorg**:
- **Publiek (Belastingdienst, Dienst Toeslagen,CJIB etc)**:
- **Energie, water, gemeentelijke belastingen en telecom**:
- **Overig**:

De enumeratie EnumSchuldensoort heeft de volgende kenmerken:

| Kenmerk   | Waarde            |
|-----------|-------------------|
| name      | EnumSchuldensoort |
| definitie | None              |
| bron      | None              |
| version   | None              |

### EnumSchuleiserssoort

Het enumeratie EnumSchuleiserssoort kent de volgende waarden:

De enumeratie EnumSchuleiserssoort heeft de volgende kenmerken:

| Kenmerk   | Waarde               |
|-----------|----------------------|
| name      | EnumSchuleiserssoort |
| definitie | None                 |
| bron      | None                 |
| version   | None                 |

### EnumUitstroomreden

Het enumeratie EnumUitstroomreden kent de volgende waarden:

- **Succesvolle uitstroom/traject doorlopen**:
- **BRP-redenen: Klant is verhuisd/niet woonachtig in regio/overleden**:
- **Klant voldoet niet aan wettelijke verplichtingen (meewerken en (juiste) inlichtingen verstrekken) –\> hier valt ook onder: klant heeft zich misdragen**:
- **Schuldhulpverlening is niet (meer) passend**:
- **Klant kan zelfstandig verder/schulden zelf geregeld**:
- **Klant heeft zelf aanvraag ingetrokken**:
- **Overig**:

De enumeratie EnumUitstroomreden heeft de volgende kenmerken:

| Kenmerk   | Waarde             |
|-----------|--------------------|
| name      | EnumUitstroomreden |
| definitie | None               |
| bron      | None               |
| version   | None               |

