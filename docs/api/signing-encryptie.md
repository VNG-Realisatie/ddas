# Ondertekenen en Versleuteling

## Ondertekenen (Signing)

Alle berichten moeten ge-signed worden om de authenticiteit, integriteit
en bewijsbaarheid van herkomst van het berichtenverkeer te garanderen.

Signing gebeurt op basis van [ADR-HTTP Message and payload signing with
JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) -
zie [Uitgangspunten](uitgangspunten.md#gebruik-jades-voor-signen) voor
de onderbouwing hiervoor.

Het signeren van het bericht gebeurt met de privé sleutel van de
verzender van het bericht, zodat de controle met de publieke sleutel van
de verzender kan gebeuren en iedere partij met toegang tot de
PKIoverheid trust anchors de handtekening kan verifiëren. Iedere
deelnemer van het DDAS-stelsel heeft dus een certificaat nodig voor het
ondertekenen van de berichten. Dit moet een ander certificaat zijn dan
welke voor het transport gebruikt wordt! Ook dit certificaat is een
"services" certificaat, maar met EKU (Extended Key Usage) "Digital
Signature". Er is gekozen voor het gebruik van PKIo certificaten - zie
[Uitgangspunten](uitgangspunten.md#gebruik-pkioverheid-certificaten-voor-authenticatie-signing-en-encryptie)
voor de onderbouwing hiervan.

Voor de ondertekening is gekozen om enkel de **payload** te ondertekenen
conform de [richtlijnen van
ADR](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/#payload-signing).
Volledige message ondertekening is niet nodig voor DDAS.

Conform de richtlijnen van ADR wordt het **PS256** algoritme gebruikt.
Voor payload signing wordt eerst met SHA-256 een digest van de HTTP-body
berekend. Deze digest wordt opgenomen in de HTTP-header `Digest`:

```{=html}
<pre><code>Digest: SHA-256=[base64-gecodeerde SHA-256 digest van de HTTP-body]</code></pre>
```
De JAdES-handtekening ondertekent vervolgens conform het JAdES
`HttpHeaders`-mechanisme deze `Digest`-header. Hiermee wordt de
integriteit van de HTTP-body cryptografisch beschermd.

Er is gekozen voor een zo eenvoudig mogelijke JAdES payload signing
conform de ADR, zonder trusted timestamp of ingebedde
validatie-informatie. Zwaardere JAdES-profielen zijn voor DDAS niet
nodig.

De publieke sleutel om de ondertekening te controleren wordt meegestuurd
via het veld `x5c` in de protected header van de JWS. `x5c` bevat het
signingcertificaat, gevolgd door de CA-certificaten die nodig zijn om
het certificatiepad op te bouwen. Het signingcertificaat staat als
eerste element. De PKIoverheid trust anchor wordt niet ontleend aan
`x5c`, maar aan de lokaal vertrouwde trust store van de ontvanger.

De handtekening wordt opgenomen in de HTTP-header:

```{=html}
<pre><code>nlgov-adr-payload-sig: [JWS Compact Serialization]</code></pre>
```
Waarin *JWS Compact Serialization* de base64url-gecodeerde waarden
conform [RFC 7515](https://www.rfc-editor.org/rfc/rfc7515) van de
protected header en de ondertekening bevat:

```{=html}
<pre><code>BASE64URL(ProtectedHeader)..BASE64URL(Signature)</code></pre>
```
*(Let op de dubbele punt (`..`): het payload-gedeelte is leeg in de
verzonden JWS, omdat gebruik wordt gemaakt van een detached payload.)*

De protected header bevat voor DDAS in elk geval de volgende velden:

```{=html}
<pre><code>{
  "alg": "PS256",
  "b64": false,
  "crit": ["sigD", "b64"],
  "kid": "[Key identifier]",
  "x5c": [
    "[end-entity-cert-base64-der]",
    "[intermediate-cert-base64-der]"
  ],
  "sigD": {
    "mId": "http://uri.etsi.org/19182/HttpHeaders",
    "pars": ["digest"]
  }
}</code></pre>
```
De velden `sigD`, `b64` en `crit` zijn onderdeel van de
JAdES-constructie voor detached payload signing:

-   `sigD` geeft aan welk mechanisme wordt gebruikt om de detached data
    in de ondertekening te betrekken.
-   `mId` heeft voor DDAS de door de ADR voorgeschreven waarde
    `http://uri.etsi.org/19182/HttpHeaders`.
-   `pars` bevat uitsluitend `digest`. Daarmee wordt aangegeven dat de
    HTTP-header `Digest` in de JWS payload wordt opgenomen.
-   `b64` staat op `false`, omdat de volgens het
    `HttpHeaders`-mechanisme opgebouwde JWS payload niet eerst met
    Base64URL wordt gecodeerd.
-   `crit` geeft aan dat een ontvanger `sigD` en `b64` moet begrijpen om
    de handtekening geldig te kunnen verwerken.
-   `kid` identificeert de gebruikte sleutel.
-   `x5c` bevat het signingcertificaat en de benodigde certificaatketen.

Er wordt geen `jku` of JWKS gebruikt voor het ophalen van de publieke
sleutel.

Bij ontvangst moet de ontvanger het volgende doen om de ondertekening te
controleren:

-   Lees de `Digest`-header en bereken zelf de SHA-256 digest over de
    ontvangen HTTP-body.
-   Controleer of de berekende digest overeenkomt met de waarde in de
    `Digest`-header.
-   Decodeer de protected header uit `nlgov-adr-payload-sig`.
-   Controleer dat `alg`, `b64`, `crit` en `sigD` voldoen aan het
    DDAS-profiel.
-   Haal het signingcertificaat uit het eerste element van `x5c`.
-   Bouw en valideer de certificaatketen tot een vertrouwde PKIoverheid
    trust anchor uit de lokale trust store.
-   Controleer de geldigheidsduur van het certificaat en voer OCSP- of
    CRL-validatie uit.
-   Reconstrueer conform `sigD` het te verifiëren JWS payload-gedeelte
    uit de `Digest`-header.
-   Verifieer de PS256-handtekening met de publieke sleutel uit het
    signingcertificaat.

Zowel requests als responses met een payload bevatten dus de volgende
twee headers:

```{=html}
<pre><code>Digest: SHA-256=[base64-gecodeerde digest]
nlgov-adr-payload-sig: [detached JWS]</code></pre>
```
## Versleuteling (Encryptie)

De inhoud van de berichten wordt niet versleuteld. Zie
[Uitgangspunten](uitgangspunten.md#berichten-worden-niet-versleuteld)
voor de onderbouwing hiervan.