Dit deel van de documentatie bevat de koppelvlakspecificatie voor de API waarmee schuldhulporganisaties gegevens beschikbaar kunnen stellen aan het CBS.  

De koppelvlakspecificatie bestaat uit de volgende onderdelen:  
- [Uitgangspunten](uitgangspunten.md): de kaders die gevolgd zijn en de 10 keuzes die gemaakt zijn;  
- [Overzicht](overzicht.md): overzicht van de oplossing met de relevante componenten;  
- [Transportlaag](transport.md): specificatie van de transportlaag - de inrichting van het koppelvlak, endpoints van de centrale directory en naamsconventie voor de services;  
- [Identificatie, Authenticatie en Autorisatie](iam.md): afspraken rond identificatie, authenticatie en autorisatie;  
- [Signing en encryptie](signing-encryptie.md): afspraken rond het ondertekenen en versleutelen van berichten;  
- [Berichten](berichten.md): de inhoud van de berichten met OAS3 beschrijving;  
- [Niet-functionele eisen](non-functionals.md): de niet-functionele eisen aan de services.  

**LET OP**: de koppelvlakspecificatie voor het beschikbaarstellen van schuldhulpverleningsgegevens is hetzelfde als die voor het beschikbaarstellen van vroegsignaleringsgegevens - alleen de [naamsconventie](transport.md#naamsconventie) en de [inhoud van de berichten](berichten.md) zijn verschillend. Let er daarom op dat u bij deze onderwerpen de juiste keuze maakt.
