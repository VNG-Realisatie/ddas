# Inleiding

## Data Delen Armoede en Schulden

VNG, Divosa en NVVK hebben de handen ineengeslagen en zijn in samenwerking met CBS, een initiatief gestart waarmee het delen van data in het armoede- en schuldendomein kan worden verbeterd en datagedreven beleid en uitvoering van gemeenten kan worden gestimuleerd. Dit initiatief heet DDAS, Datadelen op Armoede en Schulden, en startte in 2022 met subsidie van het ministerie van SZW.

De kern van DDAS is de uitvraag van data door de koepelorganisaties te standaardiseren (definities gelijktrekken), te optimaliseren (alleen uitvragen wat nodig is) en flexibiliseren (voor meerdere doelen te gebruiken). Door standaardisatie en optimalisatie wordt de administratieve lastendruk voor gemeenten en andere betrokken partijen verminderd en tegelijkertijd betere kwaliteit van informatie geleverd.

Belangrijk onderdeel van DDAS is het mogelijk maken van datadelen van gemeenten met CBS waardoor op termijn een betrouwbaar landelijk beeld kan worden geschetst van de schulden- en armoedeproblematiek en de ontwikkelingen daarin. Hiertoe worden gegevens over schuldhulpverlening vanuit de schuldhulpverlenende instanties aangeboden aan het CBS, die op basis van deze gegevens statistieken maakt voor het genoemde landelijk beeld.

## Informatie- en uitwisselmodel

Een informatiemodel is een gestructureerde representatie van gegevens en hun onderlinge relaties binnen een bepaald domein. Het helpt bij het standaardiseren van gegevens door uniforme definities, formats en regels vast te leggen voor hoe informatie wordt opgeslagen, uitgewisseld en geïnterpreteerd. Dit bevordert consistentie, duidelijkheid en interoperabiliteit tussen verschillende systemen en afdelingen, waardoor efficiëntie en datakwaliteit verbeteren.

Om te komen tot goed gestandaardiseerde definities over schuldhulpverlening is een informatiemodel Schuldhulpverlening opgesteld, deze is in dit document nader uitgewerkt.

Een uitwisselmodel is een gestructureerde set van afspraken en standaarden voor de manier waarop gegevens tussen organisaties wordt uitgewisseld. Dit model is afgeleid van een informatiemodel, dat de basis vormt door de gegevensstructuren en -relaties binnen een domein te definiëren. Het uitwisselmodel specificeert welke gegevenselementen uit het informatiemodel relevant zijn voor uitwisseling en in welk formaat deze moeten worden aangeleverd. Hierdoor wordt de consistentie en compatibiliteit van gegevensoverdracht tussen organisaties gewaarborgd, wat de efficiëntie en betrouwbaarheid van de data-aanlevering verbetert. In het uitwisselmodel hoeven niet alle gegevens uit het informatiemodel worden meegenomen.

In dit document worden zowel het informatiemodel als het uitwisselmodel beschreven. Op basis van het informatiemodel Schuldhulpverlening is in dit document het uitwisselmodel Schuldhulpverlening opgenomen, dat de basis vormt voor het beschikbaar stellen van schuldhulpgegevens.

## NVVK-Referentieproces

Als uitgangspunt voor het informatiemodel schuldhulpverlening is het proces dat door de NVVK is beschreven genomen. Schuldhulpverleners binnen Nederland werken conform dit proces.

[![NVVK-referentieproces](images/image6.jpeg)](images/image6.jpeg)

Figuur 1 NVVK Proceschema

Het NVVK-proces voor schuldhulpverlening, gehanteerd door de Nederlandse Vereniging voor Volkskrediet (NVVK), omvat een gestructureerde aanpak om mensen met problematische schulden te helpen. Dit proces begint met een intakefase, waarin de schuldhulpverlener samen met de schuldenaar een overzicht maakt van de leefstituatie, inclusief alle schulden, inkomsten en uitgaven. Vervolgens wordt een plan van aanpak opgesteld, waarin mogelijke oplossingen worden verkend, zoals betalingsregelingen, herstructurering van schulden of, indien noodzakelijk, wettelijke schuldsanering. In deze fase wordt ook gekeken naar de oorzaken van de schulden en worden maatregelen getroffen om herhaling te voorkomen, zoals budgetcoaching of het versterken van financiële vaardigheden.

Na de intake en planvorming volgt de uitvoeringsfase, waarin de schuldhulpverlener de afgesproken maatregelen implementeert. Dit kan onder meer inhouden het onderhandelen met schuldeisers om tot haalbare betalingsregelingen te komen, het aanvragen van schuldhulpverleningstrajecten of het begeleiden van de schuldenaar door een wettelijke schuldsaneringsregeling. Gedurende deze fase blijft de schuldhulpverlener de voortgang monitoren en ondersteunt hij de schuldenaar bij het naleven van het plan. Het proces wordt afgesloten met een nazorgfase, waarin de schuldenaar geholpen wordt om financieel stabiel te blijven en terugval te voorkomen. Het NVVK-proces is gericht op duurzame oplossingen, waarbij zowel de schuldenaar als de schuldeisers worden betrokken om tot een succesvolle afronding van het schuldhulptraject te komen.

### Routekaart Financiële Zorgen

Nu werken schuldhulpverleningspartijen conform het NVVK-model, het is echter de bedoeling dat ze op termijn conform de “basisdienstverlening SHV” gaan werken (zie ook <https://www.rijksoverheid.nl/actueel/nieuws/2024/03/21/basisdienstverlening-schuldhulpverlening-in-iedere-gemeente>).

Het in dit document opgenomen informatiemodel gaat uit de inrichting van schuldhulpverlening, zoals die nu door veel schuldhulpverleners wordt uitgevoerd. Zo kunnen de meest accurate gegevens worden ingewonnen. Aangezien de achterliggende gegevens sterk op elkaar lijken gaan we ervan uit dat op basis van de in te winnen gegevens ook uitspraken gedaan kunnen worden over dienstverlening conform de Route Kaart Financiële Zorgen.

## Overige Uitgangspunten 

Het informatiemodel Schuldhulpverlening kent de volgende uitgangspunten:

- [GEMMA](https://www.gemmaonline.nl/wiki/Hoofdpagina) (Gemeentelijke Referentiearchitectuur)

- [BIO](https://www.bio-overheid.nl/media/13kduqsi/bio-versie-104zv_def.pdf) – BBN2 of BBN3?

- [GGM](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/) (Gemeentelijk Gegevensmodel)

- [RSGB](https://www.gemmaonline.nl/wiki/GEMMA/id-bc6234c1-8db0-11e3-67ab-0050568a6153) (Informatiemodel voor gegevens uit de basisregistraties)

- [Algemene verordening gegevensbescherming](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=celex%3A32016R0679)

- [Wet op het Centraal Bureau voor de Statistiek](https://wetten.overheid.nl/BWBR0015926/2022-03-02)

- [NVVK Kennisbank](https://www.nvvk.nl/kennisbank) en [NVVK-referentieproces](https://www.nvvk.nl/ons-werkveld/gedragscodes-en-modules)

- Specificaties BVV Rekenregels bevat een gegevensmodel voor het berekenen van de Beslagvrije Voet - wordt dus al gebruikt door (incasserende afdelingen van) gemeenten.

- [Wet algemene bepalingen burgerservicenummer](https://wetten.overheid.nl/BWBR0022428/)

