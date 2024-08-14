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

**Gebruik Digikoppeling REST profiel**

  *Rationale*

  - Dit profiel is het minst complexe profiel voor API's en past het beste bij een stelsel waar veel partijen aan deelnemen en in eigen tempo kunnen aansluiten.

  *Implicaties*

  - Alle leverende deelnemers dienen een API conform het REST profiel beschikbaar te stellen.

  - Omdat het Digikoppeling REST profiel nog geen keuze heeft gemaakt voor signing en encryptie, moet hier expliciet een keuze in gemaakt worden.


**Gebruik JWS voor signen**

  *Rationale*

  - Omdat het REST profiel van Digikopeling (nog) geen standaard voor signen heeft vastgesteld, moet er eentje gekozen worden.

  - JWS is een breed gebruikte standaard met een grote community die het onderhoud ervan verzekert.

  - De Digikoppeling standaard noemt [JWS als mogelijke optie](https://gitdocumentatie.logius.nl/publicatie/dk/restapi/#bijlage-gebruik-van-signing-encryptie-in-de-context-van-http-rest-api) (JSON Web Signature).

  *Implicaties*

  - *nog uitzoeken (ook hoe FSC hiermee omgaat)*


**Gebruik JWE voor encryptie *(NB: als encryptie vereist is - DPIA is nog in wording)***

  *Rationale*

  - Omdat het REST profiel van Digikopeling (nog) geen standaard voor encryptie heeft vastgesteld, moet er eentje gekozen worden.

  - JWE is een breed gebruikte standaard met een grote community die het onderhoud ervan verzekert.

  - De Digikoppeling standaard noemt [JWE als mogelijke optie](https://gitdocumentatie.logius.nl/publicatie/dk/restapi/#bijlage-gebruik-van-signing-encryptie-in-de-context-van-http-rest-api).

  *Implicaties*

  - *nog uitzoeken (ook hoe FSC hiermee omgaat)*


**Federatieve Services Communicatie voor de architectuur - [FSC](https://docs.fsc.nlx.io/introduction)**

  *Rationale*

  - Deze architectuur is de standaard voor 1-op-1 koppelingen voor gemeenten. Hoewel de standaard nog niet heel breed gebruikt wordt, is dit wel de standaard voor de toekomst.

  - Er bestaat een referentie implementatie die het ontwikkelen van de API sterk vereenvoudigd. Verder is er bij VNG Realisatie (waar de standaard is ontwikkeld) kennis die gebruikt kan worden.

  *Implicaties*

  - Alle deelnemers dienen de FSC componenten te installeren en in te richten. Er bestaat een algemene referentie implementatie, maar om de inrichting verder te vereenvoudigen is het aan te raden om een specifieke referentie implementatie aan te bieden voor DDAS.


**JSON formaat voor berichten**

  *Rationale*

  - Het informatiemodel en het uitwisselmodel voor DDAS zijn in het JSON formaat ontwikkeld. Het is het eenvoudigst als de berichten dan ook in JSON formaat uitgewisseld worden.

  - JSON is goed leesbaar voor mensen, maar toch voldoende klein om ook grotere berichten uit te kunnen wisselen.

  *Implicaties*

  - De gegevens moeten in JSON formaat uitgewisseld worden.


**Gebruik Diginetwerk voor transport**

  *Rationale*

  - Het Diginetwerk is een gesloten netwerk waar alleen overheidsorganisaties toegang toe hebben. Dit beperkt de risico's van onbevoegde toegang tot de gegevens enorm.

  *Implicaties*

  - Alle deelnemers moeten toegang tot het Diginetwerk hebben of krijgen. Dit vereist toegang via een [koppelnetwerkaanbieder](https://www.logius.nl/domeinen/infrastructuur/diginetwerk/aansluiten).


**Gebruik [PKIoverheid certificaten](https://www.logius.nl/domeinen/toegang/pkioverheid) voor authenticatie, signing en encryptie**

  *Rationale*

  - Voor identicatie, authenticatie, signen en encryptie is een middel nodig dat door het stelsel vertrouwd wordt (de "Trusted Third Party"). PKIoverheid certificaten worden door de Nederlandse overheid uitgegeven, die daarmee de Trusted Third Party voor DDAS wordt.

  - PKIoverheid certificaten worden door Logius (namens de rijksoverheid) uitgegeven en beheerd. Er is daarom geen organisatie nodig om certificaten voor het DDAS stelsel te beheren.

  - PKIoverheid certificaten kunnen voor veel  diensten binnen de overheid gebruikt worden. De investering is daarom niet alleen voor DDAS, maar ook voor eventuele andere diensten die de deelnemer afneemt.

  *Implicaties*

  - Alle deelnemers moeten een PKIoverheid certificaat hebben of krijgen. NB: Het is niet altijd mogelijk om een PKIoverheid certificaat dat al in gebruik is, te hergebruiken.


**Beveiligingsniveau BBN2** (NB: DPIA is nog in wording) 

  *Rationale*

  - In de DPIA wordt dit vereist.

  *Implicaties*

  - De BIO maatregelen moeten gericht zijn op het behalen van het beveiligingsniveau BBN2.
