# Vraag en Antwoord 

Kijk hier voor vragen en verduidelijkingen rond het uitwisselmodel. Voor meer algemene vragen over DDAS-project,  kijk hier: https://www.divosa.nl/projecten/data-delen-armoede-en-schulden/vraag-en-antwoord 

??? question "Moet het aan CBS aan te leveren JSON-bestand worden versleuteld?"
    Nee, het aan CBS aan te leveren JSON-bestand hoeft niet te worden versleuteld. In een van de eerdere versie van de DPIA stond een zinssnede met de term '(versleuteld)' die tot verwarring leidde. Deze is in de DPIA aangepast. 

??? question "In het informatiemodel zijn oa. Woningbezit en Inkomen opgenomen, waarom zitten deze niet in het uitwisselmodel?"
    Inkomen, Woningbezit en een aantal andere kenmerken zijn i.d.d. onderdeel van het informatiemodel, maar worden niet bij de schuldhulpverleners uitgevraagd omdat deze gegevens al bij het CBS beschikbaar zijn. Het is dus correct dat deze niet in het uitwisselmodel staan beschreven.

??? question "In de 'description' van Intake worden 3 soorten beschikkingen genoemd terwijl de EnumBeschikkingsoort maar 2 opties heeft, wat is hier aan de hand?"
    In de Intake zijn maar twee beschikkingssoorten mogelijk: (Afwijzingsbeschikking en Toelatingsbeschikking). In de description van beschikkingsdatum staat abusievelijk ook Beëindigingsbeschikking genoemd, deze zullen we uit de tekst verwijderen in de eerst volgende release. De informatie over de beëindigingsbeschikking is onderdeel van het onderdeel Uitstroom.

??? question "In de 'description' van Begeleiding staan 3 soorten begeleiding genoemd terwijl de EnumBegeleidingssoort 5 soorten begeleiding kent, wat is hier aan de hand?"
    In de description van Begeleiding staan ten onrechte 3 soorten begeleiding, terwijl er 5 soorten mogelijk zijn volgens EnumBegeleidingssort. We zullen de description van Begeleiding in de volgende release aanpassen naar 5 opties.