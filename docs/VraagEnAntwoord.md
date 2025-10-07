# Vraag en Antwoord 

Kijk hier voor vragen en verduidelijkingen rond het uitwisselmodel. Voor meer algemene vragen over DDAS-project,  kijk hier: https://www.divosa.nl/projecten/data-delen-armoede-en-schulden 

??? question "Moet het aan CBS aan te leveren JSON-bestand worden versleuteld?"
    Nee, het aan CBS aan te leveren JSON-bestand hoeft niet te worden versleuteld. In een van de eerdere versie van de DPIA stond een zinssnede met de term '(versleuteld)' die tot verwarring leidde. Deze is in de DPIA aangepast. 

??? question "In het informatiemodel zijn oa. Woningbezit en Inkomen opgenomen, waarom zitten deze niet in het uitwisselmodel?"
    Inkomen, Woningbezit en een aantal andere kenmerken zijn i.d.d. onderdeel van het informatiemodel, maar worden niet bij de schuldhulpverleners uitgevraagd omdat deze gegevens al bij het CBS beschikbaar zijn. Het is dus correct dat deze niet in het uitwisselmodel staan beschreven.

??? question "In de 'description' van Intake worden 3 soorten beschikkingen genoemd terwijl de EnumBeschikkingsoort maar 2 opties heeft, wat is hier aan de hand?"
    In de Intake zijn maar twee beschikkingssoorten mogelijk: (Afwijzingsbeschikking en Toelatingsbeschikking). In de description van beschikkingsdatum staat abusievelijk ook Beëindigingsbeschikking genoemd, deze zullen we uit de tekst verwijderen in de eerst volgende release. De informatie over de beëindigingsbeschikking is onderdeel van het onderdeel Uitstroom.

??? question "In de 'description' van Begeleiding staan 3 soorten begeleiding genoemd terwijl de EnumBegeleidingssoort 5 soorten begeleiding kent, wat is hier aan de hand?"
    In de description van Begeleiding staan ten onrechte 3 soorten begeleiding, terwijl er 5 soorten mogelijk zijn volgens EnumBegeleidingssort. We zullen de description van Begeleiding in de volgende release aanpassen naar 5 opties.

??? question "In de intake staat zowel Beschikkingsdatum als einddatum, is dit niet dubbelop?"
    Beschikkingsdatum en einddatum lijken i.d.d. dubbel te zijn. In principe geldt de beschikkingsdatum als leidend, en gaan we ervanuit dat de einddatum dezelfde waarde krijgt als de beschikkingsdatum. In de volgende release zal de einddatum worden verwijderd.

??? question "Wanneer moet de boolean 'dwangakkoord' binnen het het object 'schuldregeling' de waarde true hebben?"
    De boolean 'dwangakkoord' heeft alleen de waarde true als de datum 'toegekend' een waarde heeft.

??? question "Er wordt bij objecttype schuldeiser 2 keer om 'naam' gevraagd, wat is hier het verschil tussen?"
    Het betreft hier een fout in de uitwisselspecificatie: het zou 1x 'naam' moeten zijn. Aanbieders wordt gevraagd beide velden te vullen met dezelfde waarde.

??? question "Het objecttype 'InformatieEnAdvies' bevat geen definitie, welke definitie moet ik hier hanteren?"
    Voor wat betreft InformatieEnAdvies kun je de volgende definitie hanteren: 'Sommige inwoners kunnen met een beetje hulp hun (dreigende) financiële problemen zelfstandig oplossen. Bij Informatie en Advies geef je iemand met informatie inzicht in financiële keuzes. Dat kan ook digitaal. Sluit aan op iemands vragen, behoeftes en mogelijkheden en stimuleer de inwoner zo veel mogelijk zelf te doen.' 
    
    Bron: https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Informatie--Advies

??? question "Het objecttype 'Nazorg' bevat geen definitie, welke definitie moet ik hier hanteren?"
    Voor wat betreft Nazorg kun je de volgende definitie hanteren: 'Nazorg is een essentieel onderdeel van schuldhulpverlening dat tot doel heeft om klanten na een schuldregelingstraject te ondersteunen bij het opbouwen van een schuldenvrij leven, zelfredzaamheid te bevorderen en terugval te voorkomen. Dit omvat het versterken van financieel zelfvertrouwen, het helpen bij het vasthouden van gezonde financiële gewoonten en het bieden van maatwerkondersteuning, zoals periodieke checks op inkomsten en uitgaven, anticiperen op veranderingen en advies bij toekomstige financiële vraagstukken.' 
    
    Bron: https://www.nvvk.nl/kennisbank-detail/2022/07/07/Module-Nazorg?originNode=1401

??? question "Wat is het verschil tussen 'beschikkingsdatum' en 'einddatum' bij objecttype 'Intake'?"
    De beschikkingsdatum is de datum waarop de beschikking is afgegeven, en de einddatum is de datum waarop de intake is afgelopen. In de praktijk zullen deze twee data bijna altijd hetzelfde zijn, maar in theorie kunnen deze data van elkaar verschillen.

??? question "Wat moet worden opgegeven bij 'code gegevensleverancier'?"
    Dit is een code die het CBS nodig heeft om onderscheid te kunnen maken tussen de leveranciers die de gegevens aanbieden. Voor nu een goede optie de naam in te vullen van de softwareleverancier die de aanpassing in de software doet. Mocht het CBS een andere verwachten dan laten we dat weten.

??? question "Wat moet worden opgegeven bij 'omschrijving' in 'Schuldhulptraject'?"
    Omschrijving is een optioneel veld die iets zeggen over individuele trajecten. Dit veld is echter niet relevant voor de levering aan CBS en kan leeg gelaten worden.

??? question "Wat moet worden opgegeven bij 'toekenningsdatum' in 'Schuldhulptraject'?"
    Toekenningsdatum bevat de datum waarop de schuldregeling is toegekend, en is dus hetzelfde als het veld ‘toegekend’ uit Schuldregeling. Wij vragen om hier dezelfde waarde op te voeren.

??? question "Wat moet worden opgegeven bij 'geslachtsaanduiding' bij 'client'?"
    De geslachtsaanduiding hoort van het type 'geslacht' te zijn, en niet alleen een string. Dit staat nu niet goed in de uitwisselspecificatie. Bij geslachtsaanduiding moet dus een van de waarden uit 'geslacht' te staan: ['Man','Vrouw','Onbekend','Leeg']

??? question "Een 0%-aanbod (bij EnumOplossingssoort) heet niet meer zo, maar een Schuldregeling zonder Afloscapaciteit (ook wel SA). Moet ik 0%-aanbod blijven hanteren?"
    Ja, de term 0%-aanbod blijft gehanteerd tot een nieuwe versie van de uitwisselspecificatie wordt uitgebracht. De huidige uitwisselspecificatie is vastgesteld voordat deze nieuwe term is geïntroduceerd, daarom wordt de oude term nog gehanteerd.
 
??? question "Overlap in de schuldhulptrajecten in de aanlevering aan CBS"
    In sommige gevallen kan er overlap ontstaan tussen (delen van) schuldhulptrajecten in de aanlevering aan het CBS. bijvoorbeeld omdat een deel van de schuldhulpverlening wordt uitgevoerd door een andere partij. Hoe gaat het CBS hier mee om? 
    Als er overlap in de tijd is in de aangeleverde informatie, dan wordt dit samengevoegd tot één (deel)traject. Is er geen overlap in de tijd, dan ontstaan twee losse (deel)trajecten. 
    Als voorbeeld: stel dat er losse BBR-begeleidingssoorten worden aangeleverd bij het CBS? Dus bijvoorbeeld:

        * aanlevering over 2020: BBR 01-01-2020 tot 31-12-2020
        * aanlevering over 2023: BBR 01-12-2023 tot 20-12-2023  &  BBR 15-12-2023 tot [leeg]
        * aanlevering over 2024: BBR 15-12-2023 tot 15-01-2024  &  BBR 10-01-2024 tot [leeg]  

    In dit geval vat het CBS dat op als twee begeleingstrajecten:
    
        * aanlevering over 2020: BBR 01-01-2020 tot 31-12-2020
        * aanlevering over 2023: BBR 01-12-2023 tot [leeg]
 
 