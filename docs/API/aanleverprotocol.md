# Aanleverprotocol

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

NB: Als er bij deze stappen algoritmen gebruikt worden, moeten deze voldoen aan de Europese AI-verordening (definitieve tekst nog niet gevonden) en aangemeld worden bij het [Algoritmeregister van de Nederlandse overheid](https://algoritmes.overheid.nl/nl).
