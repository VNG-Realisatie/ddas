# Niet functionele eisen

Dit onderwerp vraagt nog verdere uitwerking!

## Beschikbaarheid

De toepassing is niet kritisch: er is geen hoge beschikbaarheid vereist.
De services moeten beschikbaar zijn op de momenten dat CBS de gegevens verzameld. Hierover moeten nog afspraken gemaakt worden.

## Performance

De berichtenuitwisseling is synchroon. De API moet daarom binnen de "time-out" tijd reageren op een request. Er is nog geen afspraak over de maximale response tijd die geaccepteerd wordt.

Om belasting van de productiesystemen te beperken mag een cache gebruikt worden, onder de volgende voorwaarden:

- De cache wordt minimaal dagelijks ververst.

- De integriteit van de gegevens in de cache kan gegarandeerd worden. De gegevensleverancier bepaalt zelf hoe deze garantie gegeven kan worden (bijvoorbeeld met controles, checksums, logging of andere maatregelen).

## Logging en Monitoring

Verantwoordelijkheid voor monitoring ligt bij partij die verantwoording hierover moet afleggen.

FSC vereist dat er transactielogging bijgehouden wordt. Hiervoor wordt de logging module van OpenFSC gebruikt. Deze vorm van logging bevat geen persoonsgegevens en vereist daarom geen specifieke privacy maatregelen.

Bij de logging van de vragende en leverende systemen, moet er rekening gehouden worden met de AVG als persoonsgegevens (zoals het BSN) gelogd worden. De [DPIA](https://www.divosa.nl/sites/default/files/2025-11/DPIA%20DDAS%20versie%203.0%20%28november%202025%29.pdf) heeft uitgewezen dat de uitgewisselde BSN's niet individueel gelogd hoeven te worden om te voldoen aan het inzagerecht (een algemene vermelding dat schuldhulpverleningsgegevens aan CBS beschikbaar gesteld worden, is voldoende). Dit wordt daarom afgeraden - logging met individuele BSN's vormen immers een nieuwe verwerking met daaraan gekoppelde risico's.
