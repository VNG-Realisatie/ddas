# Uitgangpunten

## Kaders

Het koppelvlak moet voldoen aan de volgende wetten, afspraken en standaarden: 

- [NORA](https://www.noraonline.nl/wiki/NORA_online) 

- [BIO](https://www.bio-overheid.nl/)

- [Digikoppeling – REST-API profiel](https://logius-standaarden.github.io/Digikoppeling-Koppelvlakstandaard-REST-API/) 

- [Nederlandse API strategie](https://docs.geostandaarden.nl/api/API-Strategie/) 

- [NL Gov REST-API Design Rules](https://logius-standaarden.github.io/API-Design-Rules/) 

- [Algemene verordening gegevensbescherming](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=celex%3A32016R0679) 

- [Wet op het Centraal Bureau voor de Statistiek](https://wetten.overheid.nl/BWBR0015926/2022-03-02) 

## Keuzes

De volgende keuzes zijn gemaakt: 

**Gegevensleveranciers bieden een API aan die rechtstreeks door CBS wordt bevraagd**

  *Rationale*

  - Dit uitwisselpatroon past het best bij het [Federatief Datastelsel](https://realisatieibds.nl/page/view/564cc96c-115e-4e81-b5e6-01c99b1814ec/de-ontwikkeling-van-het-federatief-datastelsel).

  - Gegevens blijven in de bron en worden bevraagd als ze nodig zijn.

  - De API waarmee gegevens beschikbaar gesteld worden, kan hergebruikt worden voor andere toepassingen.

  - Dit patroon is besproken in de stuurgroep van 17 maart 2025 en als voorkeurspatroon geaccepteerd (rekening houdend met de risico's en maatregelen die in de besproken beslisnotitie zijn meegegeven).

  *Implicaties*

  - Alle gegevensleveranciers moeten een API als service beschikbaar stellen waar de DDAS-gegevens opgevraagd kunnen worden.

  - De service moet voldoende beschikbaar zijn om CBS op de afgesproken momenten te faciliteren.

  - Er is geen centrale routeervoorziening of gegevensopslag nodig. Wel is een centrale "directory" nodig waar de services gepubliceerd worden, waarmee CBS de gegevens kan ophalen. Hiervoor wordt de directory van RINIS gebruikt (zie de keuze "Gebruik van FSC directory van RINIS" voor de onderbouwing daarvan).



**Gebruik [Digikoppeling](https://www.logius.nl/domeinen/gegevensuitwisseling/digikoppeling) REST profiel**

  *Rationale*

  - De Digikoppeling standaard is de overheidsstandaard voor gegevensuitwisseling.

  - Het REST profiel is het minst complexe profiel voor API's en past het beste bij een stelsel waar veel partijen aan deelnemen en in eigen tempo kunnen aansluiten.

  *Implicaties*

  - Alle leverende deelnemers dienen een API conform het REST profiel beschikbaar te stellen.

  - Het REST profiel stelt de FSC standaard als verplicht voor de inrichting van het koppelvlak - hier moet dus ook aan voldaan worden.



**Gebruik [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) voor signen**

  *Rationale*

  - Het [REST profiel van Digikopeling](https://logius-standaarden.github.io/Digikoppeling-Koppelvlakstandaard-REST-API/#signing) stelt JAdES verplicht als de inhoud of de header van een bericht gesigned wordt.

  - JAdES is als standaard voorgesteld door het [Kennisplatform API's](https://www.geonovum.nl/themas/kennisplatform-apis).

  - JAdES is gebaseerd op [JWS](https://datatracker.ietf.org/doc/html/rfc7515), de standaard voor signing van REST/JSON berichten die wereldwijd breed toegepast wordt.

  - JAdES plaatst het signen "naast" het bericht, zodat het bericht zelf niet beïnvloed wordt en ook zonder de signing gebruikt kan worden.

  *Implicaties*

  - Alle berichten krijgen een ondertekening door de partij die het bericht verstuurd.

  - Voor ondertekenen is een certificaat nodig; alle deelnemers moeten een certificaat hebben dat vertrouwd wordt.  
    NB: dit moet een ander certificaat zijn dan diegene die nodig is voor dubbelzijdig versleuteld transport (mTLS). Dit zijn immers verschillende functies die elkaar niet mogen beïnvloeden; het beheer gebeurt gescheiden en eventuele problemen met de ene mogen geen impact hebben op de andere.



**Berichten worden niet versleuteld***

  *Rationale*

  - Omdat het berichtenverkeer rechtstreeks tussen aanbieder en afnemer verloopt, is een "Man-in-the-Middle" aanval niet waarschijnlijk.

  - De transportlaag wordt "end-to-end" versleuteld. Dit levert voldoende zekerheid dat de gegevens niet door ongeautoriseerde partijen gelezen kunnen worden.

  *Implicaties*

  - Berichten hoeven niet versleuteld en ontsleuteld te worden.



**Federatieve Services Connectiviteit voor de connectiviteit - [FSC](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/)**

  *Rationale*

  - Deze standaard is verplicht als het REST profiel van Digikoppeling wordt gebruikt.

  - Door te kiezen voor een standaard, vereenvoudigt de complexiteit waar gemeenten met veel koppelingen mee te maken hebben.

  - Er bestaat een referentie implementatie die de inrichting en het gebruik van de API sterk vereenvoudigt. Verder is er bij VNG Realisatie (waar de standaard is ontwikkeld), het Federatief Datastelsel en RINIS kennis die gebruikt kan worden.

  - FSC is onderdeel van het Federatief Datastelsel, het stelsel dat door het [OBDO vastgesteld is](https://www.digitaleoverheid.nl/nieuws/obdo-stelt-afsprakenstelsel-federatief-datastelsel-vast/) als basis om data overheidsbreed te vinden, delen en verantwoord te gebruiken.

  *Implicaties*

  - Alle deelnemers dienen de FSC componenten te installeren en in te richten. Deze componenten zijn onder de naam [OpenFSC](https://gitlab.com/commonground/fsc/open-fsc) als Open Source beschikbaar (maar de deelnemers mogen deze componenten ook zelf inrichten, als ze zich aan de standaard houden).

  - Alle deelnemers moeten een domein via het internet bereikbaar maken voor hun manager (bv. manager.organisatie.nl) en hun inway (bv. inway.organisatie.nl) en/of outway (bv. outway.organisatie.nl) componenten.

  - FSC gaat uit van dubbelzijdig versleuteld transport (mTLS). Hiervoor hebben alle deelnemers van het DDAS-stelsel een certificaat nodig dat vertrouwd wordt.  
  Er is een certificaat voor ieder domein dat via het internet beschikbaar komt: de manager en de inway en/of outway . NB: voor de verschillende domeinen kan hetzelfde certificaat gebruikt worden.



**Gebruik van FSC directory van RINIS**

  *Rationale*

  - Er is een centrale directory nodig waar gegevensleveranciers hun services kunnen publiceren, zodat deze vindbaar zijn.

  - RINIS biedt een FSC directory aan voor alle overheidspartijen die de Digikoppeling standaard voor REST API's toepassen. Ook het DDAS stelsel mag daar gebruik van maken.

  - Door gebruik te maken van de directory bij RINIS is er geen beheer nodig voor de centrale directory.

  - RINIS wordt gezien als onafhankelijke partner, die door alle deelnemers vertrouwd wordt.

  - Door gebruik te maken van de directory van RINIS zijn de services (in principe) makkelijk te hergebruiken voor andere diensten binnen de overheid.


  *Implicaties*

  - Het koppelvlak moet voldoen aan het REST profiel van de Digikoppeling standaard en gebruik maken van PKIo certificaten. De voorziening van RINIS volgt deze standaard en dwingt dit daarom af.

  - Alle deelnemers moeten hun endpoint (laten) registreren bij RINIS. Dit gebeurt als onderdeel van het aansluitprotocol en wordt gefaciliteerd door de stelselbeheerder (gedurende het programma is dit het programma DDAS).

  - Omdat de directory door alle overheidspartijen gebruikt mag worden, is het belangrijk afspraken te maken over de naamgeving van de services, zodat deze eenvoudig vindbaar zijn. Zie [paragraaf 3.4](https://govert-claus.github.io/DDAS-API/#naamsconventie) hiervoor.

  - Voor het ophalen van de gegevens, moet CBS de directory van RINIS bevragen om de services van de gegevensleveranciers te vinden. Daarmee sluit CBS een contract af met de gegevensleverancier om toegang te krijgen tot de service en de gegevens.



**[JSON formaat](https://json-schema.org/draft/2020-12/json-schema-validation) voor berichten**

  *Rationale*

  - Het informatiemodel en het uitwisselmodel voor DDAS zijn in het JSON formaat ontwikkeld. Het is het eenvoudigst als de berichten dan ook in JSON formaat uitgewisseld worden.

  - JSON is goed leesbaar voor mensen, maar toch voldoende klein om ook grotere berichten uit te kunnen wisselen.

  - Vrijwel alle moderne informatiesystemen kunnen goed overweg met JSON berichten, wat de inrichting en het beheer vereenvoudigt.

  *Implicaties*

  - De gegevens moeten in JSON formaat uitgewisseld worden.



**Gebruik "open" internet voor transport**

  *Rationale*

  - Een (groot) aantal deelnemers in het DDAS-stelsel heeft geen toegang tot [Diginetwerk](https://www.logius.nl/domeinen/infrastructuur/diginetwerk) en aansluiten via een [koppelnetwerkaanbieder](https://www.logius.nl/domeinen/infrastructuur/diginetwerk/aansluiten) zal onevenredig veel inspanning, doorlooptijd en kosten met zich meebrengen.

  - Er zijn geen routeervoorzieningen of andere "tussenstations" in het stelsel voorzien, waardoor "Man in the Middle" aanvallen onwaarschijnlijk zijn.

  - Het transport wordt met dubbelzijdig mTLS versleuteld, wat voldoende beveiliging geeft.

  - Middels de directory van RINIS worden alleen vertrouwde endpoints aangeroepen en krijgen alleen vertrouwde consumers (in dit geval enkel CBS) toegang tot de services.

  - Alleen afnemers die een contract hebben voor een specifieke API (in ons geval CBS) kunnen de mTLS verbinding opzetten met de Inway (een afnemer krijgt alleen een token met een geldig contract).

  - Het certificaat waarmee het contract is getekend moet hetzelfde zijn als het certificaat waarmee het contract is opgezet.


  *Implicaties*

  - Aansluiten op het stelsel vereist geen toegang tot een gesloten netwerk.

  - Het transport moet met dubbelzijdig versleuteling (mTLS) beveiligd worden.

  - Alleen endpoints die in de directory van FSC zijn vastgelegd en waarvoor een contract is afgesloten tussen CBS en gegevensleverancier, worden bevraagd.



**Gebruik [PKIoverheid certificaten](https://www.logius.nl/domeinen/toegang/pkioverheid) voor authenticatie, signing en encryptie**

  *Rationale*

  - Voor identicatie, authenticatie, signen en encryptie is een middel nodig dat door alle deelnemers van het stelsel vertrouwd wordt.

  - PKIoverheid certificaten worden door de Nederlandse overheid uitgegeven, die daarmee de "Trust Anchor" voor het DDAS-stelsel wordt.

  - PKIoverheid certificaten worden door Logius (namens de rijksoverheid) via [Logius geautoriseerde aanbieders](https://www.logius.nl/domeinen/toegang/pkioverheid/pkioverheidcertificaat-aanvragen) uitgegeven en beheerd. Er is daarom geen organisatie nodig om certificaten voor het DDAS-stelsel te beheren.

  *Implicaties*

  - Alle deelnemers moeten PKIoverheid certificaten hebben of krijgen.
  NB: er zijn certificaten nodig voor de transportlaag en het ondertekenen van berichten (hiervoor mag niet hetzelfde certificaat gebruikt worden). Mogelijk kunnen bestaande certificaten hergebruikt worden, maar hier moet voorzichtig mee omgegaan worden om beveiligingsniveaus gescheiden te houden.



**Beveiligingsniveau BBN2**

  *Rationale*

  - BBN2 is het niveau dat volgens [GEMMA](https://www.gemmaonline.nl/wiki/Basisbeveiligingsniveau_van_referentiecomponenten) geldt voor gegevensverwerkingen in de schuldhulpverlening.

  *Implicaties*

  - De [BIO maatregelen](https://www.bio-overheid.nl/handreiking-indeling-bio-v104zv-aan-isoiec-270022022/) moeten gericht zijn op het behalen van het beveiligingsniveau BBN2.
