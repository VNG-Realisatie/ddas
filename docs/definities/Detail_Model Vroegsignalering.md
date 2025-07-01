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
| burgerservicenummer | AN9 |  | Nee |
| Geboortedatum | Datum | De datum waarop de ander natuurlijk persoon is geboren. | Nee |
| geslachtsaanduiding |  | Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. | Nee |
| Huisnummer | AN5 |  | Nee |
| Huisnummertoevoeging | AN4 |  | Nee |
| Postcode | AN6 |  | Nee |



### Contactpoging
> **Definitie Contactpoging:** 
>
> <font color="#0e0e0e">Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).</font>

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
> <font color="#0e0e0e"><i>Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders.</i></font><br><font color="#0e0e0e"><i><br></i></font><font color="#0e0e0e"><i>Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.</i></font>

Het objecttype Signaalpartner kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Signaalpartner |
| bron |  |
| version | 1.0 |


Attributen van objecttype Signaalpartner:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| postcode | AN6 |  | Nee |



### Vroegsignaal
> **Definitie Vroegsignaal:** 
>
> <font color="#0e0e0e">Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden.</font><br><font color="#0e0e0e"><br></font><font color="#0e0e0e"><i>De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de </i></font><font color="#0e0e0e"><i>Wet gemeentelijke schuldhulpverlening (Wgs)</i></font><font color="#0e0e0e"><i>. Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.</i></font>

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
> <font color="#0e0e0e">Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van &#233;&#233;n of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.</font>

Het objecttype Vroegsignaalzaak kent de volgende eigenschappen:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Vroegsignaalzaak |
| bron |  |
| version | 1.0 |


Attributen van objecttype Vroegsignaalzaak:

| Attribuut | Datatype | Omschrijving | Verplicht |
| :--- | :--- | :--- | :--- |
| archiefnominatie | AN1 | <font color="#610e6a">Indicatie of het zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) gearchiveerd dient te worden</font> | Nee |
| datum_opgepakt | Date |  | Nee |
| datumEinde |  | <font color="#610e6a">De datum waarop de uitvoering van de zaak afgerond is.</font> | Nee |
| datumEindeGepland |  | <font color="#610e6a">De datum waarop volgens de planning verwacht wordt dat de zaak afgerond wordt.</font> | Nee |
| datumEindeUiterlijkeAfdoening |  | <font color="#610e6a">De laatste datum waarop volgens wet- en regelgeving de zaak afgerond dient te zijn.</font> | Nee |
| datumLaatsteBetaling |  | <font color="#610e6a">De datum waarop de meest recente betaling is verwerkt van kosten die gemoeid zijn met behandeling van de zaak.</font> | Nee |
| datumPublicatie | datum | <font color="#610e6a">Datum waarop (het starten van) de zaak gepubliceerd is of wordt.</font> | Nee |
| datumRegistratie |  | <font color="#610e6a">De datum waarop de zaakbehandelende organisatie de ZAAK heeft geregistreerd</font> | Nee |
| datumStart |  | <font color="#610e6a">De datum waarop met de uitvoering van de zaak is gestart.</font> | Nee |
| datumVernietigingDossier |  | <font color="#610e6a">De datum waarop het, al dan niet gearchiveerde, zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) vernietigd mag worden.</font> | Nee |
| document |  |  | Nee |
| duurVerlenging | N3 |  | Nee |
| einddatum_matchingperiode | Date |  | Nee |
| indicatieBetaling | AN12 | <font color="#610e6a">Indicatie of de, met behandeling van de zaak gemoeide, kosten betaald zijn door de desbetreffende betrokkene.</font> | Nee |
| indicatieDeelzaken | A1 | <font color="#610e6a">De aanduiding of een ZAAK behandeld wordt in deelzaken.</font> | Nee |
| indicatieOpschorting | AN1 |  | Nee |
| leges | AN100 |  | Nee |
| matchingsdatum | Date |  | Nee |
| omschrijving | AN80 | <font color="#610e6a">Een korte omschrijving van de zaak.</font> | Nee |
| omschrijvingResultaat | AN80 | <font color="#610e6a">Een korte omschrijving wat het resultaat van de zaak inhoudt.</font> | Nee |
| redenOpschorting | AN200 |  | Nee |
| redenVerlenging | AN200 |  | Nee |
| resultaat | Enumeratie: "EnumEindresultaat" |  | Nee |
| startdatum_matchtingperiode | Date |  | Nee |
| status |  |  | Nee |
| toelichting | AN1000 | <font color="#610e6a">Een toelichting op de zaak.</font> | Nee |
| toelichtingResultaat | AN1000 | <font color="#610e6a">Een toelichting op wat het resultaat van de zaak inhoudt.</font> | Nee |
| type |  |  | Nee |
| vertrouwelijkheid | AN40 |  | Nee |
| zaakidentificatie | AN40 | <font color="#610e6a">Een identificatie van de zaak.</font> | Nee |
| zaakniveau | N1 | <font color="#610e6a">Het niveau van een ZAAK in de hierarchie van hoofdzaak met deelzaken.</font> | Nee |






## Enumeraties Model Vroegsignalering


### EnumContactsoort
> **Definitie EnumContactsoort:** 
>
> Enumeratie met daarin de soorten onderscheiden contactsoorten bij een contactpoging.

Het enumeratie EnumContactsoort kent de volgende waarden:

* **Mail**: <Geen Definities>
* **Brief**: <Geen Definities>
* **SMS/Whatsapp**: <Geen Definities>
* **Telefoon**: <Geen Definities>
* **Huisbezoek**: <Geen Definities>
* **Kaartje**: <Geen Definities>
* **Overige**: <Geen Definities>


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

* **Ochtend**: <Geen Definities>
* **Middag**: <Geen Definities>
* **Avond**: <Geen Definities>


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

* **Niet opgepakt: inwoner wil geen contact**: <Geen Definities>
* **Niet opgepakt: geen capaciteit**: <Geen Definities>
* **Niet opgepakt**: [overig]
* **Inwoner al bekend bij schuldhulpverlening**: <Geen Definities>
* **Geen contact (meer) kunnen krijgen**: <Geen Definities>
* **Inwoner wil geen hulp**: <Geen Definities>
* **Inwoner probeert het zelf op te lossen**: <Geen Definities>
* **Inwoner heeft betaald/betalingsregeling getroffen voor oppakken melding**: <Geen Definities>
* **Inwoner heeft zelf betaald/betalingsregeling getroffen na oppakken melding**: <Geen Definities>
* **(Budget)advies en/of quick fix**: <Geen Definities>
* **Inwoner al een ander lopend traject**: <Geen Definities>
* **Verwijzing financieel**: [bijv. naar schuldhulpverlening, budgetcoach, bewindvoerder]
* **Voorzien van informatie**: <Geen Definities>
* **Niet opgepakt: BRP-uitsluiting**: <Geen Definities>
* **Verwijzing niet-financieel**: [bijv. naar maatschappelijk werk, verslavingszorg, gezinszorg]
* **Inwoner heeft al ander lopend traject**: [bijv. bij externe netwerkpartner, bij ander onderdeel sociaal domein, is onder bewind]


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

* **Energie**: <Geen Definities>
* **Huur**: <Geen Definities>
* **Hypotheek**: <Geen Definities>
* **CAK Zorgverzekeringen**: Als de zorgverzekering meer dan 6 maanden niet is betaald, wordt deze door CAK overgenomen.
* **Zorg**: <Geen Definities>
* **Water**: <Geen Definities>
* **DUO**: <Geen Definities>
* **Belastingdienst**: <Geen Definities>
* **CAK Eigen bijdrage**: Achterstand bij het betalen van de Eigen bijdrage in het kader van WLZ, en WMO. Zie convenant CAK Wmo en WLZ.
* **Overige**: <Geen Definities>
* **Dienst Toeslagen**: <Geen Definities>


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

* **Nog niet opgepakt**: <Geen Definities>
* **Onterecht signaal**: <Geen Definities>
* **Overleden**: <Geen Definities>
* **Woont niet in gemeente**: <Geen Definities>
* **Herhaalde melding**: <Geen Definities>
* **Niet opgepakt**: <Geen Definities>
* **Opgepakt**: <Geen Definities>
* **Woont op een ander adres binnen gemeente**: <Geen Definities>


De enumeratie EnumSignaalstatus heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumSignaalstatus |
| bron |  |
| version | 1.0 |




