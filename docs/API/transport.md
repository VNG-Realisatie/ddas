# Transportlaag

Hoe ziet de technische uitwisseling van berichten eruit. 

Vragen: 

- Gebruik van Diginetwerk? Kunnen alle organisaties die gegevens gaan leveren hierop aansluiten? Wordt waarschijnlijk niet mogelijk... Dan via “open” internet: vereist mogelijk extra maatregelen, zoals versleuteling van de gegevens. Dit hangt af van de DPIA. 

- Dubbelzijdig TLS (wordt voorgeschreven in Digikoppeling en FSC standaard) NB: Dit vereist een certificaat dat door alle betrokken partijen vertrouwd wordt. 

- Gebruik van PKIo certificaten voor authenticatie op basis van het [Nederlandse profiel van OAuth](https://gitdocumentatie.logius.nl/publicatie/api/oauth/)? Het is de vraag of alle partijen een PKIo certificaat mogen aanvragen. Als dit niet mogelijk is, moet een “trust anchor” gevonden worden: de autoriteit die certificaten kan uitgeven, die door alle betrokken partijen vertrouwd worden. 
