# Transportlaag

## Gebruik FSC standaard

Het transport van de berichten verloopt volgens de [FSC-standaard](https://fsc-standaard.nl/). De belangrijkste aspecten van deze standaard zijn:

- Dubbelzijdig versleuteling van het transport (mTLS). NB: Dit vereist aan beide zijden van het transport certificaten die door alle betrokken partijen vertrouwd worden.

- Gebruik van PKIo certificaten. Deze zijn aan te vragen bij door [Logius geautoriseerde aanbieders](https://www.logius.nl/domeinen/toegang/pkioverheid/pkioverheidcertificaat-aanvragen).

- De autorisatie van verbindingen wordt gedaan met een specifieke FSC-header: Fsc-Authorization. Hierin is een aantal componenten opgenomen die specifiek zijn voor FSC (o.a. de grant hash die in de transactielogging opgenomen wordt).  
Deze specifieke header geeft de ruimte om eventueel een extra autorisatie toe te voegen bijvoorbeeld op basis van een ingelogde gebruiker.

- Berichten lopen via FSC-componenten "outway" van de afnemer (CBS) en "inway" van de gegevensleverancier met de API.

- De "directory" van FSC waarin alle services van de gegevensleveranciers staan wordt beheerd door [RINIS](https://www.rinis.nl/nl/).

- Geen gebruik van Diginetwerk - de betrokken organisaties zijn daar niet op aangesloten. Transport gaat via het “open” internet.

## Inrichting koppelvlak

De inrichting van de transportlaag volgt de stappen die in de [FSC standaard](https://fsc-standaard.nl/adoptie) genoemd worden:

- Ontwerp, bouw en implementatie van de API die beschikbaar gesteld gaat worden, conform de [OAS3 beschrijving](#messages).

- Keuze inrichting en implementatie van FSC componenten in de eigen omgeving. Hiervoor kan gebruik gemaakt worden van de [documentatie]((https://docs.open-fsc.nl/introduction/)) en de [referentie-implementatie](https://gitlab.com/rinis-oss/fsc/open-fsc) van FSC.

  Bij het inrichten en testen van de FSC componenten kan het helpen om aan te sluiten op de [Demo groep](https://fsc-standaard.nl/groepen#demo) van VNG-Realisatie. Hiervoor zijn geen PKIo certificaten nodig, maar kunnen ["self-signed" certificaten](https://certportal.demo.open-fsc.nl/) gebruikt worden.

## Directory

Er wordt gebruik gemaakt van de directory die RINIS beheerd. Hier worden de services gepubliceerd, zodat CBS deze vindt en kan gebruiken.
Om gebruik te maken van de directory moeten de volgende stappen doorlopen worden:

- Aanmelden bij [Acceptatie groep](https://fsc-standaard.nl/groepen#digikoppeling-acceptatie) van RINIS en publiceren van acceptatie versie van de service. NB: hiervoor zijn geen PKIo certificaten nodig, maar kunnen ["self-signed" certificaten](https://certportal.demo.open-fsc.nl/) gebruikt worden.

  *LET OP*: de naamgeving van de RINIS omgevingen is eind januari 2026 aangepast. De juiste instellingen voor de acceptatieomgeving zijn:

  | Parameter | Waarde |
  | --------- | ------ |
  | Directory URL | https://acc-digikoppeling.fsc-directory.nl:8443 |
  | Peer ID | 01765373141930780586 |
  | Directory UI | https://index.acc-digikoppeling.fsc-directory.nl/ |
  | Groepsnaam | acc-digikoppeling |

- Testen van verbinding en service in overleg met CBS. Zij moeten een contract afsluiten met de gegevensleverancier via de FSC Manager, die de service in de directory opzoekt.

  In deze stap kan de API ook inhoudelijk getest worden: worden de juiste gegevens in het juiste formaat beschikbaar gesteld?

- Als de testen het gewenste resultaat leveren, aanmelden bij [Productie groep](https://fsc-standaard.nl/groepen#digikoppeling-productie) van RINIS. NB: hiervoor is een [PKIo certificaat](https://www.logius.nl/onze-dienstverlening/toegang/pkioverheid/pkioverheidcertificaat-aanvragen) nodig.

  *LET OP*: de naamgeving van de RINIS omgevingen is eind januari 2026 aangepast. De juiste instellingen voor de productieomgeving zijn:

  | Parameter | Waarde |
  | --------- | ------ |
  | Directory URL | https://digikoppeling.fsc-directory.nl |
  | Peer ID | 00000001805544434000 |
  | Directory UI | https://index.digikoppeling.fsc-directory.nl/ |
  | Groepsnaam | digikoppeling |

- Publiceren van de productieversie van de service en afsluiten van een contract met de consumer (CBS).

## Naamsconventie

Gebruik voor het publiceren van services een duidelijke naam, die de functie en afzender van de services bevat. De afspraak is als volgt:

- Voor schuldhulpverleningsgegevens: DDAS-schuldhulpverlening-ophaal-[gegevensleverancier]  
  [gegevensleverancier] is de naam van de leverancier van gegevens (om er zeker van te zijn dat dit tot een unieke naam leidt, is het verstandig dit met het programma DDAS af te stemmen)  

- Voor vroegsignaleringsgegevens: DDAS-vroegsignalering-ophaal-[gegevensleverancier]  
  [gegevensleverancier] is de naam van de leverancier van gegevens (om er zeker van te zijn dat dit tot een unieke naam leidt, is het verstandig dit met het programma DDAS af te stemmen)  

NB: het versienummer van de service zit niet in de naam, om te voorkomen dat er bij ieder nieuwe versie opnieuw een contract afgesloten moet worden. We gaan ervan uit dat met nieuwe versies er geen nieuwe functionaliteit of gegevens beschikbaar worden gesteld. Als dat wel gebeurt, moet er een nieuwe service met een andere naam gepubliceerd worden.  
Als het versienummer verandert, stem dan wel met CBS af welke versie wanneer gebruikt moet worden!  
