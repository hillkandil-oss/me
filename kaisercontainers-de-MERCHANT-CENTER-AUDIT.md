# kaisercontainers.de — Google Merchant Center Audit (Germany)

**Audited property:** `https://kaisercontainers.de` (live)
**Platform:** WordPress + WooCommerce + Elementor
**What it sells:** shipping/storage containers (See-, Lager-, Garagen-, Gebrauchtcontainer) — €1,190–€3,450
**Market:** Germany (DE) · **Owner (per Impressum):** Kaiser Williams, Duisburg
**Audit date:** 2026-07-26
**Method:** `gmc-audit` skill — live fetch of home, kontakt, über-uns, impressum, widerruf, products.

> **Verdict: close — mostly compliant, but a fake theme-demo contact block must be purged.**
> The hard German requirements are already met (a **real, complete Impressum**, a
> **Widerrufsbelehrung**, all legal pages, and **real prices**). The problem is leftover
> **theme-demo content in the header/footer** — a fake "Our Address · House 35 R/A, Street",
> a `name@beispiel.de` demo email, a "Mustermann" placeholder, and an untranslated "Sing Up"
> button — shown on **every page**, contradicting the real Duisburg address. Purge those and
> it's essentially submit-ready.

---

## What's already right

- ✅ **Impressum is real & complete** (§5 DDG): "Kaiser Williams, kaisercontainers, Homberg/Ruhrort/Baerl, 47138 Duisburg". VAT status stated honestly ("USt-IdNr … liegt derzeit nicht vor"), §18 MStV responsible party named. **No placeholder in the Impressum itself.**
- ✅ **Widerrufsbelehrung** + all legal pages present (AGB, Datenschutz, Versand, Zahlung, Cookie-Richtlinie, Barrierefreiheit, FAQ).
- ✅ **Real prices** on products (€1,190–€3,450 — realistic for containers).
- ✅ **Coherent identity** — brand = domain = products (containers), title is real German.
- ✅ **Own-domain email** (info@kaisercontainers.de) + a German phone (+49 201).

---

## Findings — severity-ranked

| # | Severity | Finding |
|---|----------|---------|
| 1 | 🟠 **P1** | **Fake demo address in the header/footer on every page** — "Our Address · House 35 R/A, Street" (Elementor theme demo). Contradicts the real Duisburg address in the Impressum; the **/kontakt page shows this fake address**, not the real one. |
| 2 | 🟠 **P1** | **Demo placeholders present** — `name@beispiel.de` (demo email) and `Mustermann` (German "John Doe" placeholder) still on the site. |
| 3 | 🟡 **P2** | **Untranslated theme UI** — "Sing Up" (typo of Sign Up), "Our Address", "Call Us", "e-mail us" — English demo strings on a German storefront. |
| 4 | 🟡 **P2** | **No meta description** on the homepage. |
| 5 | 🟢 **P3** | **No reviews / trust badges** (Google best-practice #2). |

---

## Detail & fixes

### 1 — 🟠 Fake demo contact address (site-wide)
**Evidence:** header/footer render *"Our Address House 35 R/A, Street"* on home, kontakt, über-uns, impressum, widerruf — while the Impressum correctly lists Duisburg.
**Why:** Two different addresses (a fake one everywhere + the real one in the Impressum) is exactly the contact inconsistency Google's misrepresentation check flags; a fake "House 35 R/A, Street" reads as unfinished.
**Fix:** Replace the theme's demo contact block with the **real Duisburg business address** (Elementor Theme Builder header/footer + WP-CLI search-replace of the demo string). Make /kontakt show the real address. *(Owner: confirm the exact real street address to display — the Impressum lists a district, not a house number.)*

### 2 — 🟠 Demo placeholders
**Fix:** Search-replace `name@beispiel.de` → `info@kaisercontainers.de`; remove the `Mustermann` placeholder (likely a demo testimonial/contact) — replace with real content or delete.

### 3–5 — 🟡/🟢 Polish
- Translate/fix the theme UI: "Sing Up" → "Anmelden/Registrieren", "Our Address" → "Adresse", "Call Us" → "Rufen Sie uns an".
- Add a homepage **meta description** (German).
- Add **real reviews / a trust badge** (real only) to satisfy Google best-practice #2.

---

## Quick fix commands (for Codex — live-and-verify)

```
# purge the demo contact block + placeholders (serialization-safe):
wp search-replace 'House 35 R/A,Street' '<REAL DUISBURG ADDRESS>' --all-tables
wp search-replace 'name@beispiel.de'    'info@kaisercontainers.de' --all-tables
wp search-replace 'Sing Up' 'Anmelden' --all-tables
# fix the Elementor header/footer "Our Address" block in Theme Builder, then:
wp cache flush
# VERIFY (all should be 0):
for u in / /kontakt /ueber-uns /impressum; do
  curl -s "https://kaisercontainers.de$u" | grep -Eic 'House 35|beispiel\.de|Sing Up|Our Address'
done
```

---

## Verdict

Of the German stores, this is in **good shape** — the legally-mandatory Impressum + Widerruf are real and complete, prices are real, and the identity is coherent. The only real blocker is the **leftover theme-demo contact block** (fake address + demo email/name) shown site-wide. Purge that so the real Duisburg address is consistent everywhere, add a meta description + real reviews, and it's a realistic Merchant Center DE candidate.

_Internal compliance audit — not legal/tax advice. Confirm the exact displayed address and any
VAT obligations with a German advisor; Google's review is discretionary._
