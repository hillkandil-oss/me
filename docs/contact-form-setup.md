# Contact Form — manual setup required (5 minutes)

**Why manual:** Contact Form 7 exposes a REST endpoint that *reports success but does not
save*. Its post type is also not registered in the WordPress REST API. Verified by writing
the German form, reading it back, and finding the English default restored. So the form
must be edited in wp-admin. Everything else (styling, German labels, placeholders) is
already applied automatically.

## ⚠️ Important: the form currently emails the wrong address
Recipient is `[_site_admin_email]` (the admin account), **not** `info@kaisercontainers.de`.
Fix this before launch, or customer enquiries go to the wrong inbox.

## Steps
WordPress admin → **Contact** → **Contact form 1** → rename to **Kontaktformular**.

### 1. Tab "Form" — replace everything with:

```
<div class="kc-form">
<p><label>Vollständiger Name (Pflichtfeld)
[text* ihr-name autocomplete:name placeholder "Max Mustermann"] </label></p>

<p><label>E-Mail-Adresse (Pflichtfeld)
[email* ihre-email autocomplete:email placeholder "name@beispiel.de"] </label></p>

<p><label>Telefonnummer
[tel ihre-telefon autocomplete:tel placeholder "z. B. 0203 1234567"] </label></p>

<p><label>Betreff (Pflichtfeld)
[text* betreff placeholder "Worum geht es?"] </label></p>

<p><label>Bestellnummer (optional)
[text bestellnummer placeholder "falls vorhanden"] </label></p>

<p><label>Grund der Anfrage
[select anliegen "Produktfrage" "Verfügbarkeit eines Containers" "Besuch / Abholung im Geschäft" "Bestehende Bestellung" "Lieferung / Transport" "Rückgabe oder Erstattung" "Allgemeine Anfrage"] </label></p>

<p><label>Ihre Nachricht (Pflichtfeld)
[textarea* nachricht placeholder "Wie können wir Ihnen helfen?"] </label></p>

<p>[acceptance datenschutz] Ich habe die <a href="/datenschutz/">Datenschutzerklärung</a> gelesen und stimme der Verarbeitung meiner Daten zur Bearbeitung meiner Anfrage zu. [/acceptance]</p>

<p>[submit "Nachricht senden"]</p>
</div>
```

### 2. Tab "Mail"
- **To:** `info@kaisercontainers.de`
- **From:** `kaisercontainers <info@kaisercontainers.de>`
- **Subject:** `kaisercontainers – Anfrage: [betreff]`
- **Additional headers:** `Reply-To: [ihre-email]`
- **Message body:**
```
Neue Anfrage über kaisercontainers.de

Name: [ihr-name]
E-Mail: [ihre-email]
Telefon: [ihre-telefon]
Betreff: [betreff]
Bestellnummer: [bestellnummer]
Grund der Anfrage: [anliegen]

Nachricht:
[nachricht]
```

### 3. Tab "Mail" → tick **Mail (2)** (customer confirmation)
- **To:** `[ihre-email]` · **From:** `kaisercontainers <info@kaisercontainers.de>`
- **Subject:** `Ihre Anfrage bei kaisercontainers`
- **Body:**
```
Guten Tag [ihr-name],

vielen Dank für Ihre Nachricht. Wir melden uns so bald wie möglich, in der Regel
innerhalb eines Werktages.

Betreff: [betreff]
Grund der Anfrage: [anliegen]

Ihre Nachricht:
[nachricht]

Freundliche Grüße
Ihr Team von kaisercontainers
```

### 4. Tab "Messages" (German)
Sent OK: `Vielen Dank für Ihre Nachricht. Wir melden uns in der Regel innerhalb eines Werktages.`
Validation: `Bitte prüfen Sie Ihre Eingaben.` · Required: `Bitte füllen Sie dieses Pflichtfeld aus.`
Email invalid: `Die E-Mail-Adresse ist ungültig.` · Acceptance: `Bitte bestätigen Sie die Datenschutzerklärung.`

### 5. Save, then send a test message and confirm it arrives at info@kaisercontainers.de.

## Already applied automatically (no action needed)
- Form styled as a white card with visible bordered inputs, labels, focus rings, corten submit button
- Existing English labels translated to German + placeholders injected via JS
- Spam protection: consider enabling Akismet or CF7's reCAPTCHA in the same screen
