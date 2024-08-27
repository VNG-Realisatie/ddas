# API specificatie

## Inleiding

Dit onderdeel bevat de koppelvlakspecificatie voor de API waarmee schuldhulporganisaties gegevens beschikbaarstellen aan het CBS.

Naast de uitgangspunten en de technische specificatie bevat dit document een beschrijving van de niet-functionele eisen (beschikbaarheid, performance) en de monitoring behoeften.

Het [gebruik](protocol.md) en het [beheer](beheer-specificatie.md) van de specificatie worden in aparte onderdelen beschreven.

***In de huidige versie staan nog diverse vraagstukken en de keuzes die gemaakt worden, moeten nog worden bevestigd. Het document dient daarom vooral als basis voor de discussie om tot een definitieve specificatie te komen, en er kunnen geen rechten aan dit document ontleend worden.***


## Uitgangpunten

### Kaders

Het koppelvlak moet voldoen aan de volgende wetten, afspraken en standaarden: 

- [NORA](https://www.noraonline.nl/wiki/NORA_online) 

- [BIO](https://www.bio-overheid.nl/)

- [Digikoppeling – REST-API profiel](https://logius-standaarden.github.io/Digikoppeling-Koppelvlakstandaard-REST-API/) 

- [Nederlandse API strategie](https://docs.geostandaarden.nl/api/API-Strategie/) 

- [NL Gov REST-API Design Rules](https://logius-standaarden.github.io/API-Design-Rules/) 

- [Algemene verordening gegevensbescherming](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=celex%3A32016R0679) 

- [Wet op het Centraal Bureau voor de Statistiek](https://wetten.overheid.nl/BWBR0015926/2022-03-02) 

### Keuzes

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


**Federatieve Services Connectiviteit voor de architectuur - [FSC](https://docs.fsc.nlx.io/introduction)**

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


## Transportlaag

Hoe ziet de technische uitwisseling van berichten eruit. 

Vragen: 

- Gebruik van Diginetwerk? Kunnen alle organisaties die gegevens gaan leveren hierop aansluiten? Wordt waarschijnlijk niet mogelijk... Dan via “open” internet: vereist mogelijk extra maatregelen, zoals versleuteling van de gegevens. Dit hangt af van de DPIA. 

- Dubbelzijdig TLS (wordt voorgeschreven in Digikoppeling en FSC standaard) NB: Dit vereist een certificaat dat door alle betrokken partijen vertrouwd wordt. 

- Gebruik van PKIo certificaten voor authenticatie op basis van het [Nederlandse profiel van OAuth](https://gitdocumentatie.logius.nl/publicatie/api/oauth/)? Het is de vraag of alle partijen een PKIo certificaat mogen aanvragen. Als dit niet mogelijk is, moet een “trust anchor” gevonden worden: de autoriteit die certificaten kan uitgeven, die door alle betrokken partijen vertrouwd worden. 


## Identificatie, Authenticatie en Autorisatie

Hoe worden de schuldhulpverleners (gegevensleveranciers) geïdentificeerd? (o.b.v. (sub)OIN?) Als niet alle betrokken partijen een (sub)OIN kunnen krijgen, moet een systematiek gevonden worden om alle partijen uniek te kunnen identificeren. 

Hoe worden systemen geauthenticeerd? (obv PKIo certificaten? Als dat niet kan: wie wordt de “Trust Anchor” – de autoriteit die door alle partijen vertrouwd wordt?) 

Autorisatie lijkt niet heel spannend: er zal waarschijnlijk maar één service komen met een vaste set gegevens, waar maar één partij (CBS) toegang toe zal krijgen. Als fijnmaziger autorisatie nodig is, dan bestaat er een voorkeur voor PBAC (Policy Base Authorisation Control). De autorisatie wordt dan bepaald op basis van beleidsregels, zoals “organisatie X krijgt toegang tot gegeven G als de organisatie overeenkomst O getekend heeft en het gegeven is vrijgegeven door autoriteit A”. Dan is de vraag wie deze beleidsregels vaststelt en wie ze beheert. 


## Signing en Versleuteling

NB: De Digikoppeling standaard voor REST-API heeft (nog) geen standaard voor signing en encryptie vastgesteld. Daarom voorstel om JWT te gebruiken en dus eerst een JWT aan te vragen, die daarna bij het request wordt meegestuurd. Eventueel kunnen hierbij protocollen van de FSC standaard toegepast worden. 

### Signing

Voorstel: Signing op basis van JWS in een JWT conform de [FSC standaard](https://commonground.gitlab.io/standards/fsc/core/draft-fsc-core-00.html#signatures). 

### Versleuteling (Encryptie)

Is versleuteling nodig? (zou uit DPIA moeten komen – ik vermoed dat het nodig is) 

Voorstel: Versleuteling op basis van JWE in een JWT met PKIo certificaten. NB: ook hier geldt dat als niet alle betrokken partijen PKIo certificaten kunnen aanvragen, er een Trust Anchor nodig is die vertrouwde certificaten kan uitgeven. 


## Berichten

De technische beschrijving van de API is het volgende OAS3-bestand beschreven. Hiervan is ook een [downloadbare versie](https://github.com/brienen/ddas/blob/Goverts-Place/API-v0.0.3/DDAS_opzetje_v0.0.3.yaml) van.
```
{!../API-v0.0.3/DDAS_opzetje_v0.0.3.yaml!}

```
Hieronder worden de berichten die daar technisch beschreven zijn, toegelicht.

### Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen - daarom liever een POST.

NB: Dit bericht wordt in een JWT verwerkt, voor signen en versleutelen (als versleutelen nodig is – met een BSN in het bericht zou dat waarschijnlijk moeten).

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel):

- Startdatum (default leeg - deelnemer bepaalt dan startdatum)

- Einddatum (default leeg - deelnemer bepaalt dan einddatum)

- Gemeente (default alle – alleen relevant als over meer dan 1 gemeente gegevens aangeleverd worden)


### Antwoordbericht (response)

Dit is het antwoordbericht van de schuldhulpverlener met de gewenste gegevens in JSON formaat.

Als versleutelen nodig is, in een JWT vorm (versleuteld conform JWE).

Payload is gebaseerd op [uitwisselspecificatie](https://brienen.github.io/ddas/latest/uitwisselspecificatie/)!

Mogelijke responses:

- 200: bericht goed verwerkt (met payload)

- Foutberichten moeten nog bepaald worden - waarschijnlijk 401 (unauthorized), 404 (not found), 500 (internal server error) en 503 (service unavailable)


## Niet functionele eisen

### Beschikbaarheid

Niet kritische toepassing: geen hoge beschikbaarheid vereist. 

Afstemmen met CBS: wanneer willen zij gegevens verzamelen? Dan zou de beschikbaarheid wat hoger moeten zijn. BV: tijdens kantooruren  

### Performance

Geen afhankelijkheden in het primaire proces: geen hoge performance vereist. 

Wordt gebruik van cache toegestaan (volgens mij moet dat kunnen)? Onder welke voorwaarden? 

### Monitoring

Verantwoordelijkheid voor monitoring ligt bij partij die verantwoording hierover moet afleggen. Welke verantwoording verwacht het programma of SZW? 

Voor gemeenten (suggestie): 

- Aantal bevragingen naar datum en afzender (altijd CBS?) 

- Aantal en soort foute bevragingen 

- Aantal en soort meegestuurde parameters 

Voor CBS: 

- Aantal bevragingen naar datum en schuldhulpverlener 

- Aantal en soort responses
