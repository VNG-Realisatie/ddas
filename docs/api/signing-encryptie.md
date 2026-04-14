# Ondertekenen en Versleuteling

## Ondertekenen (Signing)

Alle berichten moeten ge-signed worden om de authenticiteit, integriteit en bewijsbaarheid van herkomst van het berichtenverkeer te garanderen.

Signing gebeurt op basis van [ADR-HTTP Message and payload signing with JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) - zie "Uitgangspunten" voor de onderbouwing hiervoor.

Het signeren van het bericht gebeurt met de privé sleutel van de verzender van het bericht, zodat de controle met de publieke sleutel van de verzender kan gebeuren en iedere partij met toegang tot de PKIoverheid trust anchors de handtekening kan verifiëren. Iedere deelnemer van het DDAS-stelsel heeft dus een certificaat nodig voor het ondertekenen van de berichten. Dit moet een ander certificaat zijn dan welke voor het transport gebruikt wordt! Ook dit certificaat is een "services" certificaat, maar met EKU (Extended Key Usage) "Digital Signature".
Er is gekozen voor het gebruik van PKIo certificaten - zie [Uitgangspunten](#kaders) voor de onderbouwing hiervan.

Voor de ondertekening is gekozen om enkel de **payload** te ondertekenen conform de [richtlijnen van ADR](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/#payload-signing). Volledige message ondertekening is niet nodig voor DDAS.
Conform de richtlijnen van ADR wordt het PS256 algoritme gebruikt. De signature wordt berekend over de exacte byte-representatie van de HTTP body zoals verzonden.  
Er is gekozen voor het **JAdES-B** profiel van ondertekenen. JAdES-B betekent dat de handtekening en de ondertekeningscertificaten worden opgenomen, zonder trusted timestamp of ingebedde validatie-informatie. Zwaardere profielen, waarbij ook een trusted timestamp en verificatie informatie geregistreerd wordt, zijn voor DDAS niet nodig.
De publieke sleutel om de ondertekening te controleren wordt meegestuurd in de header van het bericht via het veld x5c. De hele X.509 certificaatketen wordt meegestuurd, waarbij de eerste waarde gebruikt wordt voor de controle van de ondertekening.
In de header komen dus het volgende te staan:

<pre><code>nlgov-adr-payload-sig: [JWS Compact Serialization]</code></pre>

Waarin *JWS Compact Serialization* de base64url-gecodeerde waarden conform [RFC 7515](https://www.rfc-editor.org/rfc/rfc7515) van de header en de ondertekening bevatten:

<pre><code>BASE64URL(ProtectedHeader)..BASE64URL(Signature)</code></pre>

*(Let op de dubbele punt (..): het payload-gedeelte is leeg, omdat de payload in de HTTP body zit.)*

De header bevat in elk geval de volgende velden:

<pre><code>{  
  "alg": "PS256",  
  "typ": "JOSE",  
  "kid": "[Key identifer]",  
  "x5c": [  
    "[end-entity-cert-base64-der]",  
    "[intermediate-cert-base64-der]"  
  ],  
  "x5t#S256": "[sha256-thumbprint]"  
}</code></pre>

*(Het veld x5t#S256 is niet verplicht, maar wordt wel aanbevolen)*



Bij ontvangst moet de ontvanger het volgende doen om de ondertekening te controleren:

- Decode protected header

- Haal eerste certificaat uit x5c

- Valideer certificaatketen tot PKIoverheid root

- Controleer:

  - Geldigheid

  - OCSP of CRL

- Verifieer signature over HTTP body


## Versleuteling (Encryptie)

De inhoud van de berichten wordt niet versleuteld. Zie [Uitgangspunten](#kaders) voor de onderbouwing hiervan.
