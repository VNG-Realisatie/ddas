## Objecttypen Model Vroegsignalering


### Client
> **Definitie Client:** 
>
> Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente.

Het objecttype Client kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Client |
| bron |  |
| version | 1.5 |


Attributen van objecttype Client:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| Achternaam | AN200 |  | Nee |
| Burgerservicenummer | AN9 |  | Nee |
| Geboortedatum | Datum | De datum waarop de ander natuurlijk persoon is geboren. | Nee |
| Huisnummer | AN5 |  | Nee |
| Huisnummertoevoeging | AN4 |  | Nee |
| Plaatsnaam | AN200 |  | Nee |
| Postcode | AN6 |  | Nee |
| Straatnaam | AN200 |  | Nee |
| Voorletters | AN20 |  | Nee |



### Contactpoging
> **Definitie Contactpoging:** 
>
> Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).

Het objecttype Contactpoging kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Contactpoging |
| bron |  |
| version | 1.0 |


Attributen van objecttype Contactpoging:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| bereikt | boolean | Er is succesvol contact met de client gemaakt. | Nee |
| dagdeel | Enumeratie: "EnumDagdeel" | Ochtend, middag of avond | Nee |
| datum | Date |  | Nee |
| soort | Enumeratie: "EnumContactsoort" |  | Nee |



### Signaalpartner
> **Definitie Signaalpartner:** 
>
> Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders.<br>Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.

Het objecttype Signaalpartner kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Signaalpartner |
| bron |  |
| version | 1.0 |


Attributen van objecttype Signaalpartner:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| Organisatienaam | AN6 |  | Nee |
| type | Enumeratie: "EnumSignaalpartner" |  | Nee |



### Vroegsignaal
> **Definitie Vroegsignaal:** 
>
> Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden.<br>De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs). Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.

Het objecttype Vroegsignaal kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Vroegsignaal |
| bron |  |
| version | 1.0 |


Attributen van objecttype Vroegsignaal:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| bedrag | bedrag |  | Nee |
| crisissignaal | boolean | Betreft het een crisis? | Nee |
| ontstaansdatum | Date |  | Nee |
| signaaldatum | Date | Datum waarop de signaalpartner het signaal heeft verstuurd. | Nee |
| status | Enumeratie: "EnumSignaalstatus" |  | Nee |
| warmeOverdracht | boolean | Er is al contact met persoon. Betreft verzoek deze persoon op te pakken in het kader van vroegsignalering. | Nee |



### Vroegsignaalzaak
> **Definitie Vroegsignaalzaak:** 
>
> Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van &#233;&#233;n of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.

Het objecttype Vroegsignaalzaak kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Vroegsignaalzaak |
| bron |  |
| version | 1.0 |


Attributen van objecttype Vroegsignaalzaak:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| datum_opgepakt | Date |  | Nee |
| einddatum_matchingperiode | Date |  | Nee |
| matchingsdatum | Date |  | Nee |
| resultaat | Enumeratie: "EnumEindresultaat" |  | Nee |
| startdatum_matchtingperiode | Date |  | Nee |






## Enumeraties Model Vroegsignalering


### EnumContactsoort
> **Definitie EnumContactsoort:** 
>
> Enumeratie met daarin de soorten onderscheiden contactsoorten bij een contactpoging.

Het enumeratie EnumContactsoort kent de volgende waarden:


  
  * **Brief**: <Geen Definities>
  

  
  * **Huisbezoek**: <Geen Definities>
  

  
  * **Kaartje**: <Geen Definities>
  

  
  * **Mail**: <Geen Definities>
  

  
  * **Overige**: <Geen Definities>
  

  
  * **SMS/Whatsapp**: <Geen Definities>
  

  
  * **Telefoon**: <Geen Definities>
  


De enumeratie EnumContactsoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumContactsoort |
| bron |  |
| version | 1.0 |



### EnumDagdeel
> **Definitie EnumDagdeel:** 
>
> Geen Definitie

Het enumeratie EnumDagdeel kent de volgende waarden:


  
  * **Avond**: <Geen Definities>
  

  
  * **Middag**: <Geen Definities>
  

  
  * **Ochtend**: <Geen Definities>
  


De enumeratie EnumDagdeel heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumDagdeel |
| bron |  |
| version | 1.0 |



### EnumEindresultaat
> **Definitie EnumEindresultaat:** 
>
> Enumeratie met de soorten Eindresultaten van een Vroegsignaalzaak.

Het enumeratie EnumEindresultaat kent de volgende waarden:


  
  * **(Budget)advies en/of quick fix**: <Geen Definities>
  

  
  * **Geen contact (meer) kunnen krijgen**: <Geen Definities>
  

  
  * **Inwoner al bekend bij schuldhulpverlening**: <Geen Definities>
  

  
  * **Inwoner al een ander lopend traject**: <Geen Definities>
  

  
  * **Inwoner heeft al ander lopend traject**: [bijv. bij externe netwerkpartner, bij ander onderdeel sociaal domein, is onder bewind]
  

  
  * **Inwoner heeft betaald/betalingsregeling getroffen voor oppakken melding**: <Geen Definities>
  

  
  * **Inwoner heeft zelf betaald/betalingsregeling getroffen na oppakken melding**: <Geen Definities>
  

  
  * **Inwoner probeert het zelf op te lossen**: <Geen Definities>
  

  
  * **Inwoner wil geen hulp**: <Geen Definities>
  

  
  * **Niet opgepakt**: [overig]
  

  
  * **Niet opgepakt: BRP-uitsluiting**: <Geen Definities>
  

  
  * **Niet opgepakt: geen capaciteit**: <Geen Definities>
  

  
  * **Niet opgepakt: inwoner wil geen contact**: <Geen Definities>
  

  
  * **Verwijzing financieel**: [bijv. naar schuldhulpverlening, budgetcoach, bewindvoerder]
  

  
  * **Verwijzing niet-financieel**: [bijv. naar maatschappelijk werk, verslavingszorg, gezinszorg]
  

  
  * **Voorzien van informatie**: <Geen Definities>
  


De enumeratie EnumEindresultaat heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumEindresultaat |
| bron |  |
| version | 1.0 |



### EnumSignaalpartner
> **Definitie EnumSignaalpartner:** 
>
> Enumeratie met de soorten te onderscheiden Signaalpartners.

Het enumeratie EnumSignaalpartner kent de volgende waarden:


  
  * **Belastingdienst**: <Geen Definities>
  

  
  * **CAK Eigen bijdrage**: Achterstand bij het betalen van de Eigen bijdrage in het kader van WLZ, en WMO. Zie convenant CAK Wmo en WLZ.
  

  
  * **CAK Zorgverzekeringen**: Als de zorgverzekering meer dan 6 maanden niet is betaald, wordt deze door CAK overgenomen.
  

  
  * **Dienst Toeslagen**: <Geen Definities>
  

  
  * **DUO**: <Geen Definities>
  

  
  * **Energie**: <Geen Definities>
  

  
  * **Huur**: <Geen Definities>
  

  
  * **Hypotheek**: <Geen Definities>
  

  
  * **Overige**: <Geen Definities>
  

  
  * **Water**: <Geen Definities>
  

  
  * **Zorg**: <Geen Definities>
  


De enumeratie EnumSignaalpartner heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumSignaalpartner |
| bron |  |
| version | 1.0 |



### EnumSignaalstatus
> **Definitie EnumSignaalstatus:** 
>
> Geen Definitie

Het enumeratie EnumSignaalstatus kent de volgende waarden:


  
  * **Herhaalde melding**: <Geen Definities>
  

  
  * **Niet opgepakt**: <Geen Definities>
  

  
  * **Nog niet opgepakt**: <Geen Definities>
  

  
  * **Onterecht signaal**: <Geen Definities>
  

  
  * **Opgepakt**: <Geen Definities>
  

  
  * **Overleden**: <Geen Definities>
  

  
  * **Woont niet in gemeente**: <Geen Definities>
  

  
  * **Woont op een ander adres binnen gemeente**: <Geen Definities>
  


De enumeratie EnumSignaalstatus heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumSignaalstatus |
| bron |  |
| version | 1.0 |




