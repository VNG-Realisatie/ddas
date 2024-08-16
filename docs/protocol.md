# Gebruik van de specificatie

## Aansluitprotocol

Iedere schuldhulpverleningsorganisatie of gemeente (hierna: "deelnemer") die gegevens beschikbaar gaat stellen aan CBS, moet het aansluitprotocol doorlopen. Dit protocol valt onder verantwoordelijkheid van het programma DDAS. Voor vragen hierover kan altijd contact opgenomen worden met [contactadres].

Het protocol kan aangepast worden als hiervoor aanleiding is. Na aanpassingen wordt de meest recente versie met versienummer en versiedatum gepubliceerd op [documentatiewebsite].

De stappen die de deelnemer moet doorlopen, zijn:

- De deelnemer meldt zich bij de stelselbeheerder (CBS of DDAS?) via het aanmeldformulier [waar staat dit? wie beheert dit?], waarin in elk geval het volgende ingevuld:

  - Naam van de deelnemer + contactgegevens

  - Naam van de gegevensleverancier + contactgegevens

  - Endpoint waar de productiegegevens beschikbaar komen

  - Endpoint waar de testgegevens beschikbaar komen

  - Akkoord met de aansluitvoorwaarden, waaronder de verwerkersovereenkomst met CBS

  - Eventuele verzoeken om de aansluiting tot stand te krijgen, zoals een gewenste publicatiedatum, specifieke testdata of specifieke beschikbaarheid

- *Indien PKIo certificaten niet mogelijk zijn: de stelselbeheerder (DDAS of CBS?) genereert een certificaat voor de TLS verbinding, signing en encryptie, en levert deze aan de deelnemer.*

- De deelnemer richt in de testomgeving de API, conform de AOS documentatie [yaml-bestand, nog toe te voegen] in. Voor de installatie van FSC komt een handleiding en een referentie implementatie beschikbaar.

- De deelnemer voert CBS op in de management module van FSC, om toegang te verlenen.

- CBS voert enkele bevragingen uit in de testomgeving en beoordeelt de kwaliteit van de gegevens. Op basis van de bevindingen wordt de API aangepast.

- Indien er geen blokkerende bevindingen zijn, krijgt de deelnemer vrijgave van de stelselbeheer (DDAS of CBS?) en wordt de API in de productieomgeving ingericht en beschikbaar gesteld.

- CBS voert de deelnemer op in de management module van FSC, zodat de API bevraagd wordt bij het ophalen van alle gegevens.

Ten behoeve van de testen stelt DDAS een set testgegevens beschikbaar [wie maakt deze set? waar komt dit te staan?].

Voor ondersteuning bij de aansluiting is een referentie implementatie en documentatie beschikbaar [waar?] en kan contact opgenomen worden met [contactadres]. Als er bij de aansluiting bevindingen zijn, die niet door de deelnemer opgelost kunnen worden, kan een wijzigingsverzoek ingediend worden.


## Aanleverprotocol

Stappen bij het aanleveren van gegevens: 

- CBS roept systeem van schuldhulpverlener (gegevensleverancier) aan om JWT voor signing en encryptie te krijgen 

- CBS roept API van de gegevensleverancier aan (eventueel met parameters) 

- CBS controleert response technisch (signing, viruscontrole, berichtformaat) 

- CBS controleert response functioneel (verplichte velden, vreemde waarden, etc.)

- CBS stuurt een verwerkingsverslag naar de gegevensleverancier

- Indien OK, dan worden de gegevens ingelezen in de database 

- CBS loopt alle gerapporteerde trajecten af en combineert trajecten van dezelfde BSN tot één “traject” 

- Bij het combineren wordt de volledigheid en kwaliteit van de gegevens gecontroleerd – op basis daarvan krijgt het traject een "betrouwbaarheidsindicator"" 

- CBS genereert de gewenste rapporten 

*NB: Als er bij deze stappen algoritmen gebruikt worden, moeten deze voldoen aan de Europese AI-verordening (definitieve tekst nog niet gevonden) en aangemeld worden bij het [Algoritmeregister van de Nederlandse overheid](https://algoritmes.overheid.nl/nl).*
