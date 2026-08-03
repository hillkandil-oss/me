#!/usr/bin/env python3
"""Rebuild /kontakt/ with a DSGVO-safe (Zwei-Klick) Google Maps block.

Every factual line is copied verbatim from the page as it stands live —
address, opening hours, email, the [BESTÄTIGEN] telephone marker. Nothing
about the business is invented here; the only new material is the map
loader and the corrected block markup.
"""
import json, os, subprocess, sys, urllib.parse

SITE = "https://omarscontainers.de"
USER = os.environ["WP_USER"]
PASS = os.environ["WP_PASS"]
PAGE = 22942

ADDR = "Karnaper Str. 177 A, 45329 Essen, Deutschland"
q = urllib.parse.quote_plus(ADDR)
EMBED = f"https://www.google.com/maps?q={q}&amp;output=embed&amp;hl=de"
SEARCH = f"https://www.google.com/maps/search/?api=1&amp;query={q}"
ROUTE = f"https://www.google.com/maps/dir/?api=1&amp;destination={q}"

# --- read what is live now, so we fail loudly if it is not what we expect ---
cur = json.loads(subprocess.run(
    ["curl", "-sS", "-u", f"{USER}:{PASS}",
     f"{SITE}/wp-json/wp/v2/pages/{PAGE}?context=edit"],
    capture_output=True, text=True, check=True).stdout)
old = cur["content"]["raw"]

for fact in ["Karnaper Str. 177 A, 45329 Essen",
             "info@omarscontainers.de",
             "Montag bis Samstag, 08:00 – 18:30 Uhr",
             "BESTÄTIGEN: Telefonnummer",
             "hostinger-ai-theme/contact-form-block"]:
    assert fact in old, f"expected fact missing from live page: {fact}"
assert "oc-map" not in old, "map block already present — refusing to double-insert"

# --- the map block ---------------------------------------------------------
# No iframe in the initial HTML. The visitor's IP reaches Google only after
# they press the button. The two plain links below work without JavaScript.
MAP = f'''<!-- wp:html -->
<div class="oc-map" id="oc-map">
  <div class="oc-map__frame">
    <div class="oc-map__inner">
      <p class="oc-map__addr">omarscontainers · {ADDR}</p>
      <p class="oc-map__note">Aus Datenschutzgründen wird die Google-Karte erst nach Ihrer Zustimmung geladen. Beim Laden werden Daten – unter anderem Ihre IP-Adresse – an Google übertragen. Einzelheiten in unserer <a href="/datenschutz/">Datenschutzerklärung</a>.</p>
      <button type="button" class="oc-map__btn" id="oc-map-load">Karte laden</button>
    </div>
  </div>
  <p class="oc-map__links">
    <a href="{SEARCH}" target="_blank" rel="noopener noreferrer">In Google Maps öffnen</a>
    <a href="{ROUTE}" target="_blank" rel="noopener noreferrer">Route planen</a>
  </p>
</div>
<script>
(function(){{
  var btn = document.getElementById('oc-map-load');
  if(!btn) return;
  btn.addEventListener('click', function(){{
    var wrap = document.getElementById('oc-map');
    var frame = wrap.querySelector('.oc-map__frame');
    var f = document.createElement('iframe');
    f.src = "{EMBED.replace('&amp;', '&')}";
    f.title = "Karte: {ADDR}";
    f.loading = "lazy";
    f.referrerPolicy = "no-referrer-when-downgrade";
    f.setAttribute('allowfullscreen','');
    frame.innerHTML = '';
    frame.appendChild(f);
    wrap.classList.add('oc-map--live');
  }});
}})();
</script>
</div>
<!-- /wp:html -->'''
MAP = MAP.replace('</div>\n<!-- /wp:html -->', '<!-- /wp:html -->')

form = old[old.index('<!-- wp:hostinger-ai-theme/contact-form-block'):
           old.index('/-->', old.index('<!-- wp:hostinger-ai-theme/contact-form-block')) + 4]

new = (
    '<!-- wp:paragraph --><p>Sie erreichen uns persönlich in Essen oder per '
    'E-Mail. Wir antworten in der Regel innerhalb eines Werktages.</p>'
    '<!-- /wp:paragraph -->'
    + form +
    '<!-- wp:paragraph {"fontSize":"small"} --><p class="has-small-font-size">'
    'Hinweis zum Datenschutz: Ihre Angaben werden ausschließlich zur Bearbeitung '
    'Ihrer Anfrage verwendet und nicht an Dritte weitergegeben. Mehr dazu in der '
    '<a href="/datenschutz/">Datenschutzerklärung</a>.</p><!-- /wp:paragraph -->'

    '<!-- wp:heading --><h2>Anschrift</h2><!-- /wp:heading -->'
    '<!-- wp:paragraph --><p>omarscontainers<br>Karnaper Str. 177 A, 45329 Essen, '
    'Deutschland</p><!-- /wp:paragraph -->'

    '<!-- wp:heading --><h2>E-Mail</h2><!-- /wp:heading -->'
    '<!-- wp:paragraph --><p><a href="mailto:info@omarscontainers.de">'
    'info@omarscontainers.de</a></p><!-- /wp:paragraph -->'

    '<!-- wp:heading --><h2>Telefon</h2><!-- /wp:heading -->'
    '<!-- wp:paragraph --><p style="background:#fff8e1;border-left:4px solid #f5a623;'
    'padding:12px 16px;margin:16px 0;color:#0F172A"><strong>[BESTÄTIGEN: '
    'Telefonnummer – Kunden erwarten bei Investitionsgütern dieser '
    'Größenordnung eine telefonische Erreichbarkeit]</strong><br>'
    '<em>Dieser Platzhalter muss vor der Veröffentlichung durch die '
    'tatsächliche Angabe ersetzt werden.</em></p><!-- /wp:paragraph -->'

    '<!-- wp:heading --><h2>Öffnungszeiten</h2><!-- /wp:heading -->'
    '<!-- wp:paragraph --><p>Montag bis Samstag, 08:00 – 18:30 Uhr<br>'
    'Sonntags geschlossen.</p><!-- /wp:paragraph -->'

    '<!-- wp:heading --><h2>Anfahrt</h2><!-- /wp:heading -->'
    '<!-- wp:paragraph --><p>Unser Standort befindet sich in Essen-Karnap. Eine '
    'Besichtigung vor Ort ist während der Öffnungszeiten möglich '
    '– bitte vereinbaren Sie einen Termin per E-Mail.</p><!-- /wp:paragraph -->'
    + MAP
)

# --- fact-preservation check: nothing may be lost in the rewrite -----------
for fact in ["Karnaper Str. 177 A, 45329 Essen", "info@omarscontainers.de",
             "Montag bis Samstag, 08:00 – 18:30 Uhr", "Sonntags geschlossen.",
             "BESTÄTIGEN: Telefonnummer", "Essen-Karnap",
             "hostinger-ai-theme/contact-form-block"]:
    assert fact in new, f"rewrite dropped: {fact}"
assert new.count("<!-- wp:heading -->") == new.count("<!-- /wp:heading -->") == 5
assert new.count("<div") == new.count("</div>"), "unbalanced divs in map block"

payload = json.dumps({"content": new}, ensure_ascii=False)
open("/tmp/kontakt_payload.json", "w", encoding="utf-8").write(payload)
print("payload bytes:", len(payload.encode()))
print("old len", len(old), "-> new len", len(new))
