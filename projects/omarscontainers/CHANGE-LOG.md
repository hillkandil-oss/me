# omarscontainers.de — Change Log

Every write made to the live site, with the authorisation behind it. Read-only inspection
is not logged; only changes.

---

## 2026-08-03 — Store identity, region, B2C tax, sender address

**Authorised by owner:** *"set address to Essen an support email to info@omarscontainers.de
is a B2C"*

### WooCommerce → General

| Setting | Before | After |
|---|---|---|
| `store_address` | *(empty)* | `Karnaper Str. 177 A` |
| `store_city` | *(empty)* | `Essen` |
| `store_postcode` | *(empty)* | `45329` |
| `default_country` | `DE:DE-HH` (Hamburg) | `DE:DE-NW` (North Rhine-Westphalia) |
| `currency` | `EUR` | `EUR` (unchanged, confirmed) |
| `calc_taxes` | `no` | `yes` |
| `allowed_countries` | `all` | `specific` → `[DE]` |
| `ship_to_countries` | *(empty)* | `specific` → `[DE]` |

Region was wrong: the store was configured for Hamburg while the business operates from
Essen. Corrected — NAP consistency across site, schema, GBP and Merchant Center depends on it.

Selling and shipping scope narrowed to Germany per intake ("Shipping countries: Germany").
Previously the store offered worldwide sale with no rates configured.

### WooCommerce → Tax (B2C configuration)

| Setting | Before | After |
|---|---|---|
| `prices_include_tax` | `no` | `yes` |
| `tax_display_shop` | `excl` | `incl` |
| `tax_display_cart` | `excl` | `incl` |
| `price_display_suffix` | *(empty)* | `inkl. 19 % MwSt. zzgl. Versandkosten` |
| `tax_based_on` | `shipping` | `shipping` (unchanged) |

Created tax rate: **DE · 19.0000% · "MwSt." · standard class · shipping taxed**.

**Pricing impact — no change to what customers pay.** Existing prices are now treated as
gross (VAT-inclusive), so a €4,660 product still displays €4,660, composed of €3,915.97 net
+ €744.03 VAT.

> **Owner confirmation still needed:** if those figures were intended as *net* supplier
> prices, the store is now absorbing the 19% rather than adding it, and prices need raising
> (€4,660 net → €5,545.40 gross). Say the word and this can be bulk-adjusted.

### WooCommerce → Emails

| Setting | Before | After |
|---|---|---|
| `email_from_address` | `hillkandil@gmail.com` | `info@omarscontainers.de` |
| `email_from_name` | `omarscontainers.de` | `omarscontainers` |

Transactional email previously sent from a personal Gmail address — poor trust signal and
inconsistent with the business identity.

> **Unverified:** that `info@omarscontainers.de` exists and receives mail. The intake gave
> the support address as `info@omarscontainers.com` (.com); the owner then specified `.de`.
> Deliverability must be tested before launch — transactional email that bounces is a
> checkout failure.

---

## 2026-08-03 (cont.) — Duplicate removal + brand assignment

**Authorised by owner:** *"continue"*

### Duplicate products removed

Six SKUs each existed twice — verified byte-identical (same name, description, price and
image count) before removal. The older copy of each pair was kept; the newer duplicate was
moved to **trash**, not permanently deleted, so all six are restorable from
Products → Trash.

| SKU | Kept | Trashed |
|---|---|---|
| CL3ST2660 | 2974 | 4197 |
| CL3ST2661 | 2980 | 4172 |
| CL3ST2662 | 2994 | 4165 |
| CL3ST2663 | 2999 | 4148 |
| CL3ST2664 | 3011 | 4115 |
| CL3ST2665 | 3029 | 4103 |

Live catalogue: **116 → 110**. Duplicate SKUs remaining: **0**.

> *Correction to the earlier audit:* finding B5 said "twelve duplicate products". Twelve
> products were *involved* in duplication, but only **six** were redundant. Six were removed.

### Brands assigned — 58 of 110

Created 18 `product_brand` terms and assigned them. **Every brand was taken from the
product's own title** — none inferred, none invented.

Aiper · Anssems · Beatbot · Cheval Liberté · Daikin · EcoFlow · Eduard · Fendt · FOCO ·
Franc · Gree · Humbaur · Ifor Williams · Mitsubishi · Remko · Stahlworks · TPV · Variant

The remaining **52 products were deliberately left without a brand** — unbranded containers,
sanitary units and pools where no manufacturer is evidenced. These should carry
`identifier_exists: no` in the feed rather than a fabricated brand.

### Still open on product data

- **Two Remko pairs share a title but have different SKUs** (ids 3602/3631 and 3613/3638,
  identical prices, 7 vs 6 images). Not touched — needs an owner decision on whether these
  are genuinely distinct stock or a second duplicate import.
- Condition attribute still unset on all 110 (blocked on MI-10: new or used?).
- Descriptions still copied from third-party sources.

---

## 2026-08-03 (cont.) — Payment, shipping, condition

**Authorised by owner:** *"payment is through bank transfer freighted is a flat rate of
170euros an its new stock"*

### Payment — checkout now functions

| Setting | Before | After |
|---|---|---|
| `bacs` (Direct bank transfer) | disabled | **enabled** |
| Title | "Direct bank transfer" | "Überweisung (Vorkasse)" |

> ### ⚠ BANK ACCOUNT DETAILS ARE NOT SET — customers cannot actually pay
> BACS is enabled, but no account details are configured. A customer completing checkout
> is shown payment instructions with **no IBAN to transfer to**. Orders will be placed and
> never paid.
>
> Needed: **account holder · IBAN · BIC · bank name**.
> WooCommerce → Settings → Payments → Direct bank transfer → Account details.
> This is a launch blocker, not a nicety.

### Shipping — Deutschland zone

| Item | Value |
|---|---|
| Zone | Deutschland (id 1), country `DE` |
| Method | Flat rate — "Speditionsversand (Pauschale)" |
| Cost entered | `142.86` net |
| **Customer pays** | **€170.00** (142.86 net + 27.14 VAT) |
| Tax status | taxable |

First set to `170`, which WooCommerce treated as **net** — customers would have been charged
**€202.30**. Corrected to 142.86 net so the gross charge is exactly the €170 specified.

> If €170 was meant as a *net* figure with VAT on top (customer pays €202.30), set the cost
> back to `170`.

### Condition — new stock

Created global attribute **Zustand** (id 1) with term **Neu**, applied to **110/110**
products, visible on the product page. Feeds `condition: new` and schema `itemCondition:
NewCondition`.

### End-to-end checkout test — PASSED

Real cart via the public Store API, unauthenticated:

```
product          €4,660.00  (gross, incl. 19% MwSt)
shipping         €  170.00  (gross, incl. 19% MwSt)
ORDER TOTAL      €4,830.00
```

Shipping rates resolve, tax calculates correctly, and `bacs` is offered as a payment method.
**A customer can now complete checkout** — subject to the bank details warning above.

### Re-audit after these changes

Blockers cleared: no-payment-gateway, no-shipping. Remaining 6 blocking findings are all
**missing legal/policy pages** plus business identity not visible on the homepage — the
next work package.

---

## 2026-08-03 (cont.) — Legal pages, footer, business identity

**Authorised by owner:** *"start the website building"*

### Ten pages created and published

| URL | Purpose |
|---|---|
| `/impressum/` | §5 DDG legal notice |
| `/datenschutz/` | GDPR privacy policy (Art. 13) |
| `/widerrufsrecht/` | 14-day withdrawal + Muster-Widerrufsformular |
| `/agb/` | Terms of business |
| `/versand-und-lieferung/` | Shipping, freight, collection |
| `/zahlungsarten/` | Payment methods and process |
| `/rueckgabe-erstattung/` | Returns and refunds |
| `/kontakt/` | Contact |
| `/standort/` | Visit us — address, hours, viewing, collection |
| `/ueber-uns/` | About |

All content uses **only owner-confirmed facts**. Every unknown is a visible
`[BESTÄTIGEN: …]` marker on an amber background — it cannot be mistaken for real
content and cannot silently ship. Nothing was invented.

Outstanding markers: legal entity name and Rechtsform · managing director · telephone ·
Handelsregister number · USt-IdNr. · bank details · cookie inventory · delivery-access
requirements · excluded return categories · storefront photos · company history.

### Wiring

- AGB set as the WooCommerce checkout terms page (id 22941)
- WordPress boilerplate drafts `privacy-policy` and `refund_returns` moved to trash
- Footer template part extended with a business-identity block (name, address, email,
  opening hours) and two link columns (Service, Rechtliches)
- VAT/shipping notice added site-wide per PAngV
- LiteSpeed cache purged and public rendering verified

The theme is a **block theme**, so classic menu locations do not exist; the footer was
edited as a template part rather than via a nav menu.

### Re-audit — all blockers cleared

| | Before | After |
|---|---|---|
| BLOCKER | 5 | **0** |
| CRITICAL | 6 | **0** |
| HIGH | 6 | 3 |

Remaining: 52 unbranded products (correct — no brand evidenced), Product schema lacking
`itemCondition`, no telephone, and the two Remko title duplicates.

### Auditor bugs found and fixed while doing this

1. **English-only policy slugs** reported all German pages as missing — 5 false CRITICALs.
   Added DE slugs (`impressum`, `datenschutz`, `agb`, `widerruf…`, `versand…`, `kontakt`,
   `ueber-uns`).
2. **Address heuristic** matched only English street words, so `Karnaper Str. 177 A` read
   as "no physical address" — 1 false CRITICAL. Added German forms
   (`str.`, `straße`, `weg`, `platz`, `allee`, `gasse`, `ring`, `damm`).
3. **No Impressum check at all** despite it being legally mandatory. Added, gated on the
   site looking German, at BLOCKER severity.
4. **Non-ASCII URLs crashed the auditor** (`UnicodeEncodeError` on `über-uns`) — introduced
   by fix 1. Request URLs are now percent-encoded with IDNA host handling, which also makes
   umlaut product URLs work.

Fixture regression re-run after all four: 24 findings, unchanged distribution.

---

## 2026-08-03 (cont.) — Removed inherited false and unsubstantiated claims

**Authorised by owner:** *"continue"*

Scanned all 110 descriptions for claims inherited from the copied supplier text that are
untrue of this business, unenforceable, or unsubstantiated.

### Removed — pre-acceptance damage clause (1 product, id 2615)

> *"Trotz sorgfältiger Verladung können minimale Dellen oder Kratzer entstehen — mit der
> Auftragsannahme gilt dieser Hinweis als gelesen und akzeptiert."*

Copied text attempting to make the buyer waive damage claims simply by ordering. Two
problems: a liability waiver buried in a product description is very unlikely to be
enforceable against a consumer under German law, and it carries Abmahnung risk. The
factual part (walls ship with protective film) was **kept**; only the waiver was removed.

### Removed — market-comparative claims (3 products, ids 3411, 3435, 3663)

*"10 Jahre Garantie (einzigartig am Markt)"* · *"(einzigartig auf dem Markt)"* ·
*"einzigartig auf dem Markt"*

"Unique on the market" is a factual claim about competitors that cannot be substantiated,
and is exactly the unsupported-claim category Merchant Center treats as misrepresentation.
The **warranty term itself was kept** — only the comparative boast was cut. Ordinary
marketing language such as *"einzigartiges Design"* was deliberately left alone.

### Verified clear afterwards

| Claim category | Remaining |
|---|---|
| Market-comparative claims | **0** |
| Pre-acceptance waiver | **0** |
| "aus unserem Hause/Werk" (own factory) | **0** |

> A first pass matched only `(einzigartig am Markt)` and missed
> `(einzigartig auf dem Markt)`. Caught on verification and re-run against freshly fetched
> data rather than the stale local copy.

---

## ⚠ OWNER DECISION — delivery times contradict the shipping policy

Six products state their own delivery time inside the description, and it disagrees with
`/versand-und-lieferung/`:

| Product id | Description says | Shipping policy says |
|---|---|---|
| 21736, 21741, 21743 | 15 bis 20 Tage | 2 bis 5 Werktage |
| 21749, 21757 | 15–20 Tage | 2 bis 5 Werktage |
| 22870 | 07 – 15 Tage | 2 bis 5 Werktage |

**Not changed, deliberately.** Either figure could be the true one and guessing would put a
false delivery promise on the site — which is both a Merchant Center contradiction and, under
German consumer law, an inaccurate delivery date.

Most likely explanation: 2–5 days is right for stocked goods, while container pools are
manufactured to order and genuinely take 15–20 days. If so the fix is a per-product
delivery time plus a shipping policy that explains both cases — not deleting either number.

**Needed:** confirm the real lead time for made-to-order pools, and whether 2–5 working days
applies only to in-stock items.

### Warranty claims — also needs confirmation

Three trailer products advertise **10 Jahre Garantie**. The AGB currently carries a
`[BESTÄTIGEN]` marker for warranties. Confirm whether this is the manufacturer's guarantee
(state whose, and link the terms) or one you grant yourself — an advertised guarantee you
cannot honour is a misrepresentation.

---

## 2026-08-03 (cont.) — Agent 8: homepage and site identity

**Authorised by owner:** *"continue with the building of the website"*

### The site had no homepage

`show_on_front` was `posts` — the front page was a **blog feed**, not a storefront. That is
why the homepage read as thin in every earlier audit. Created `/startseite/` (id 22958) and
set it as the static front page.

### Homepage content

| Section | Content |
|---|---|
| Hero | H1, plain-language summary of what is sold, "Alle Artikel sind Neuware", two CTAs (Shop, Standort) |
| Trust row | Physical location + hours · shipping €170 incl. VAT · 30-day returns with return postage paid |
| Categories | All 10 categories with live product counts, linked |
| Buying info | Payment process, gross-price/VAT statement, collection discount |
| Pre-sales | Contact route with a stated response time |

Every figure matches the policy pages — shipping €170, 30 days, 0–1 working day processing,
19% VAT. Nothing invented.

**Deliberately excluded:** countdown timers, stock-scarcity messages, visitor counters,
fabricated reviews, trust badges, awards, press mentions, and any "best/cheapest/number one"
claim. Those are §40 automatic failure conditions and the fastest route to a
misrepresentation flag.

### Site identity

| Setting | Before | After |
|---|---|---|
| Site title | `omarscontainers.de` | `omarscontainers` |
| Tagline | *(empty)* | `Container, Poolcontainer und Anhänger — Neuware aus Essen` |
| `show_on_front` | `posts` | `page` |

### Verified on the rendered page

H1 present · 10 category links · "Neuware" · €170 · 30 Tage · address · opening hours ·
Impressum link · **0 unresolved `[BESTÄTIGEN]` markers** · no placeholder text.

### Audit

Still **0 blocking findings**. Remaining: 3 HIGH, 2 MEDIUM.

### Not done — needs assets or owner input

- **All 10 categories have no image.** Category cards are text-only. Needs real photographs
  of actual stock — stock photography of containers the business does not own would be
  misrepresentation.
- Telephone number still absent (HIGH).

---

## 2026-08-03 (cont.) — Agent 5: navigation

**Authorised by owner:** *"yes"*

### The header had no navigation

The header's `wp:navigation` block referenced menu **6493**, and the footer's referenced
**320**. Both IDs return `rest_post_invalid_id` — **neither menu exists**. The rendered
header therefore contained exactly one link: the site title. No shop, no categories, no
cart. Customers had no way to browse the catalogue except by guessing URLs.

This is why the store looked empty despite holding 110 published products.

### Built

Created navigation **Hauptnavigation** (id 22959) and repointed both the header and footer
blocks at it.

```
Shop ▾
  Klimaanlage (21) · Anhänger (15) · Wohncontainer (15) · Pferdeanhänger (10)
  Poolcontainer (10) · Sanitärcontainer (10) · Bootsanhänger (9)
  Poolroboter (8) · Lagercontainer (6) · Werkstattcontainer (6)
Standort · Kontakt · Warenkorb
```

### Verified

Header renders **15 links**, including all **10 category links**. Every destination checked
individually — **14/14 return HTTP 200**, no 404s or redirects.

### Regression introduced and fixed in the same session

Wiring the navigation into the footer, I rebuilt the footer template part from a **local
copy saved before** the legal block was appended. That stale write silently removed the
business-identity block and all ten policy links from every page.

Caught by the re-audit, which went **5 findings → 9** (Impressum no longer linked from the
homepage, plus Datenschutz/AGB/Über uns). Restored by re-fetching the *current* footer and
re-appending the block, with an assertion that the block is absent before appending so the
same mistake cannot silently duplicate it instead.

| | Findings |
|---|---|
| Before navigation work | 5 (HIGH 3, MEDIUM 2) |
| After the regression | 9 (HIGH 4, MEDIUM 5) |
| After the fix | **5 (HIGH 3, MEDIUM 2)** |

Lesson recorded: **never write a template part from a cached local copy** — re-fetch
immediately before every write, because template parts accumulate edits across a session.

---

## 2026-08-03 (cont.) — Imagery, logo, design audit

**Authorised by owner:** *"continue an generate images to use on website"*

### Category images — real photos, not generated ones

Asked to generate images, I did **not** generate photographs of containers. AI-made
container or yard photography presented as this business's stock would be exactly the
misrepresentation we spent the session removing.

Instead, every category was matched to a **real photograph of stock actually sold**, taken
from the best-documented product in that category. **10/10 categories now have an image**,
all with alt text, and the homepage cards render them.

| Category | Sourced from |
|---|---|
| Klimaanlage | Mitsubishi Heavy Set Tower 7,7 kW |
| Anhänger | Anhänger 105x205cm 750kg Typ U2 |
| Wohncontainer | Mobiler Wohncontainer / Luxusholz |
| Pferdeanhänger | Cheval Liberté GOLD 3 Premium |
| Poolcontainer | Mobiler Mini-Schwimmbadcontainer |
| Sanitärcontainer | WC Sanitärcontainer Doppelkabine |
| Bootsanhänger | Variant Bootsanhänger Ocean 1000 |
| Poolroboter | Beatbot AquaSense 2 Pro |
| Lagercontainer | Neuer 10-Fuß-Lagercontainer |
| Werkstattcontainer | 4m Spezial-Container |

### Logo — built as SVG, no credits spent

The business had no logo. A brand mark makes no factual claim about stock, so it is
legitimately generatable. The Higgsfield balance check was declined, so rather than spend
credits it was drawn directly as **SVG**: a corrugated shipping-container mark, the
wordmark split weight-wise (`omars` bold / `containers` light), and the strapline
`ESSEN · NEUWARE`. Rasterised to PNG (WordPress blocks SVG upload by default), uploaded
with alt text, and set as site logo and favicon. Vector source is editable and free of
licensing encumbrance.

### Design audit (impeccable skill + bundled detector)

Detector: only `overused-font` warnings (Montserrat, Roboto, Lato, Open Sans) — all from
the Hostinger theme's bundled stack, not from anything written here.

**Fixed:**

| Issue | Before | After |
|---|---|---|
| Heading hierarchy jump h1 → h3 | 1 jump | **none** |
| Lazy-loaded images | 0/13 | **10/13** |
| Images with intrinsic dimensions (CLS) | 1/13 | **11/13** |
| WooCommerce page titles in English | Cart, Checkout, My account | **Warenkorb, Kasse, Mein Konto** (slugs kept, no URL breakage) |

Already clean: viewport meta, `<main>`/`<nav>` landmarks, skip link, single H1, zero images
missing alt text, no render-blocking stylesheets, no fixed-px inline widths.

---

## ⚠ OWNER ACTION — the shop interface is in English

`WPLANG` is `en_US` and `<html lang="en-US">` on a wholly German store. A customer buying a
€4,830 container currently reads *"Your cart is currently empty"* and *"Return to shop"* at
checkout.

Two consequences: a trust and conversion problem at the moment of payment, and a wrong
language signal to Google on a site whose feed, currency and target country are all German.

**Attempted and failed:** setting `language: de_DE` via REST returns `en_US` silently — the
German translation pack is not installed and the REST API cannot install one.

**Fix (2 minutes, admin GUI):** *Einstellungen → Allgemein → Sprache der Website →
**Deutsch*** and save. WordPress downloads the pack and translates WooCommerce's interface
strings automatically. Page titles are already German.

---

## 2026-08-03 (cont.) — LocalBusiness structured data

**Authorised by owner:** *"leave bank details"* (bank details dropped per owner instruction;
work continued on the next findings)

### Store schema added

Appended `Store` JSON-LD to the footer template part, so it renders on every page:

- Name, URL, email, EUR, payment method
- Full `PostalAddress` — Karnaper Str. 177 A, 45329 Essen, NRW, DE
- `openingHoursSpecification` — Mon–Sat 08:00–18:30 (6 days)
- `areaServed` Deutschland
- `hasOfferCatalog` with all 10 categories

Verified rendering: one JSON-LD block, `@type=Store`, address and hours parsed correctly,
and the legal links plus address confirmed still intact afterwards.

**Guarded this time.** After the earlier footer regression, the write now asserts the legal
block is present and the schema absent before appending, and the shell aborts if the
payload file is empty. That guard earned its keep immediately: a Python syntax error
produced a 0-byte payload and the `curl` still fired. The empty POST was a harmless no-op —
confirmed by re-reading the footer (8,902 chars, legal block intact) — but the check is
what made that verifiable rather than assumed.

### Auditor bug #5 — German opening hours

The `brick-and-mortar` finding persisted after the schema was live. Cause: the visible-hours
check looked only for `monday` / `hours`, while the page reads *"Montag bis Samstag,
08:00 – 18:30 Uhr"*. Added German markers (`montag`, `samstag`, `öffnungszeit`, ` uhr`,
`geöffnet`, `geschlossen`). Fixture regression re-run: 24 findings, unchanged.

### Owner decision recorded — bank details

Bank account details will not be added. Consequence, stated once and then dropped:
`bacs` is enabled, so a customer can complete checkout and receive payment instructions
with no account to pay into. Under the project workflow §40 that is *"products cannot
actually be purchased"* — an automatic failure condition for Merchant Center submission.
Recorded, not re-litigated.

---

## 2026-08-03 (cont.) — Description rewrite, batch 1 of ~9

**Authorised by owner:** *"continue"*

### Method

Technical specifications are **facts** — dimensions, weights, RAL numbers, materials,
capacities — and facts are not copyrightable, so they are preserved verbatim. The
surrounding marketing prose, which is what was actually copied from third-party sites, is
rewritten from scratch in a consistent house voice. No new claims introduced, nothing
factual dropped.

**Batch 1: Lagercontainer (6) + Werkstattcontainer (6) = 12 of 110 rewritten.**

### Verification

**Numeric fact preservation** — strict comparison of every numeric value before and after,
normalised for thousand separators:

- **9 of 12 numerically identical**
- id 2396, 2921: the "missing" values are German numerals I spelled out
  (*vier* Dachaufnahmen, *zwei* Kugelzylinder, *vier* Personen)
- id 2901: `3–5 Tage` deliberately removed — see below

**Originality** — the same web-search test that exposed the copying now returns **no exact
match** for the rewritten text.

**Copied artefacts** — zero occurrences of the competitor name, the pre-acceptance clause,
or market-comparative claims across the batch.

Length fell to 69% of the original (15,477 → 10,796 chars). That is padding removed, not
information: every spec survived.

---

## ⚠ Two serious data errors found while reading

### 1. A competitor was advertised in your own listing (id 2901)

The 20-Fuß-Werkstattcontainer description read:

> *"Maximale Flexibilität: Kauf oder Miete bei **Hacon Containers** möglich"*

A rival firm named in your product text, offering rental from them. Proof of the copying
and an active leak of customers. **Removed.**

The same sentence block carried *"Schnelle Lieferung: innerhalb von 3–5 Tagen"*, which also
contradicts the shipping policy's 2–5 Werktage. Removed with it.

### 2. Title and specification disagree on size (id 2935)

Titled **"Werkstattcontainer 10 Fuß"**, but the technical data give 6.058 mm length —
unambiguously a **20-foot** container. Price €3,100.

**Not silently resolved.** The rewrite carries a visible `[BESTÄTIGEN]` marker asking which
is correct. Merchant Center compares the feed title against the landing page; shipping this
as-is invites a product-data mismatch. Either the title or the dimensions must be corrected
by the owner.

### Remaining

98 of 110 descriptions still to rewrite, across 8 categories.

---

## 2026-08-03 (cont.) — Agents 14 & 15: SEO audit and remediation

**Mode:** owner switched the workflow to autonomous — proceed without asking, batch all
questions to the end.

### Audit findings

| Check | Before |
|---|---|
| SEO plugin installed | **none** |
| Meta descriptions | **0 of 14 pages** |
| Canonical on /shop/ and category pages | **missing** |
| robots.txt | present, sitemap referenced, nothing commercial blocked |
| XML sitemap | present at `/wp-sitemap.xml`, 8 sub-sitemaps |
| Category page content | **empty on all 10** — thin content |

### Remediation

- Installed **Slim SEO 4.9.11** — auto-derives meta descriptions and canonicals from page
  content with no configuration, chosen over Yoast/Rank Math because it needs no setup
  wizard and cannot nag or half-configure itself in an autonomous run.
- Wrote original German descriptions for **all 10 product categories** (544–709 chars each),
  each naming what distinguishes the category and which specs to compare on, plus the
  shared delivery/collection/returns terms.
- Added an intro to the **Shop** page.

### Result

**Meta descriptions and canonicals: 12/12 pages** (from 0/14 and partial canonicals).
Open Graph tags now emitted. Category pages carry real content instead of being empty
product grids.

> *Correction:* the first audit pass reported the product page as having no title, canonical
> or H1. That was my own invented URL slug returning a transport error — the real product
> permalink returns 200 with title, canonical and meta description all present. No such
> defect existed.

---

## 2026-08-03 (cont.) — Agent 4 batch 2: Sanitärcontainer (10 products)

**22 of 110 descriptions now rewritten.**

### Self-caught quality failure

The first pass of this batch **dropped real specifications** — door pass-through
(65 × 190 cm), window sizes (60 × 40 cm), panel thicknesses, and on two products the
**outer dimensions entirely** (2568: 121 × 221 × 235 cm; 2580: 4.000 × 2.400 × 2.350 mm).

Caught by the numeric fact-preservation check, not by eye. Three rounds of patching were
needed: the first missed because the Bauweise block text differed, the second because the
stored markup contained newlines my replacement string did not.

**Final state: 9 of 10 numerically identical to the original.**

The single remaining gap is deliberate — see below.

### Deliberate omission — "100% Made in Germany" (id 2604)

The original text asserted *"100% Made in Germany"*. Origin claims are strictly regulated
in Germany and I cannot verify this one, so it was **not carried into the rewritten
description**. It still appears in the **product title**, which I did not change because
that alters product identity.

**Owner action:** either substantiate the claim (and I will restore it) or remove it from
the title.

---

## 2026-08-03 (cont.) — Warranty page, motion, visual polish

**Owner report:** shipping / returns / warranty / payment / terms pages "not visible", and
the site lacks motion.

### Pages — 4 of 5 already existed, 1 genuinely did not

Verified live: `/versand-und-lieferung/`, `/rueckgabe-erstattung/`, `/zahlungsarten/`,
`/agb/` all return 200 with 271–386 words, and the footer renders **10/10 policy links on
every page type** — homepage, shop, policy pages and category archives alike. They are under
German slugs, which is correct for a German store.

**Warranty was genuinely missing.** Created `/gewaehrleistung/` — Gewährleistung und
Garantie: the statutory two-year right under §§ 434 ff. BGB, the twelve-month reversed
burden of proof, how manufacturer guarantees sit *alongside* statutory rights rather than
replacing them, the claims procedure, transport damage, and the distinction from the
withdrawal right. Linked in the footer, now **11/11**.

Carries a `[BESTÄTIGEN]` marker for the three trailers advertising "10 Jahre Garantie" —
§ 479 BGB requires an advertised guarantee to name the guarantor, duration, scope and
conditions.

### Motion and polish

Added to theme global styles (`projects/omarscontainers/theme/design.css`, 8.2 KB):

- **Custom easing curves** — `cubic-bezier(.23,1,.32,1)` for entrances. Built-in CSS easings
  are too weak to read as intentional. **No `ease-in` anywhere on UI**; it delays the moment
  the user is watching most closely.
- **Durations by element type** — 140 ms interactive feedback, 240 ms cards, 420 ms image
  reveals. `:active` drops to 80 ms so a press feels immediate.
- **Card and image treatment** — lift plus shadow on hover, 1.035–1.045 image scale.
  The image moves; the price never does.
- **Focus rings** restored and made consistent, never removed.
- **44 px minimum touch targets** below 781 px.

### How the motion stays crawler-safe

Scroll reveals sit inside `@supports (animation-timeline: view())` **and**
`@media (prefers-reduced-motion: no-preference)`. A browser without support gets plain
visible content — **nothing is hidden by default**, so Google and no-JS users always see the
full page. Price, availability and add-to-cart are explicitly exempted from any animation.

`prefers-reduced-motion: reduce` removes movement but keeps every state change: hover
feedback becomes an outline instead of a lift, rather than disappearing.

### Pre-existing defect found and fixed

WooCommerce ships the product gallery with **inline `opacity: 0`**, revealed only by
JavaScript. If that script fails, is blocked, or is slow, **product images are invisible** —
on the exact page a buyer decides from and the exact page Merchant Center compares against
the feed. Forced visible in CSS; the flexslider script still works on top.

Also neutralised `.hostinger-ai-fade-up`, a theme class that sets `opacity: 0` with no
fallback. It is currently unused, but it would hide content the moment it were applied.

### Verified

Motion CSS live, `@supports` guard present, reduced-motion block present, gallery fix live,
11/11 footer links, address and hours intact. Audit unchanged at **0 blocking findings**.

> *Correction:* an intermediate check reported "price visible in HTML: False" on the product
> page. That was a faulty regex expecting a bare `€`; the price renders as an HTML entity.
> Re-checked against unescaped text: price present as `5,000.00 €`. No defect existed.

---

## 2026-08-03 (cont.) — Colour system, hero imagery, full-bleed layout

### Palette applied — with one accessibility correction

| Role | Colour | Contrast |
|---|---|---|
| Background | `#F8FAFC` | — |
| Cards & zones | `#E2E8F0` | — |
| Text | `#0F172A` | **17.06:1** on background, **14.48:1** on cards |
| Action | `#EA580C` | see below |

**White text on `#EA580C` measures 3.56:1 — it fails WCAG AA for normal text (4.5:1).**

Rather than change the specified colour, buttons keep the **exact `#EA580C` fill** and take
**navy `#0F172A` label text, which passes at 5.02:1**. On hover the fill deepens to
`#C2410C`, where white text clears at 5.18:1 — same hue family, and the darkening doubles
as hover feedback.

Prices are navy, not orange: orange on the light background is 3.40:1 and would have been
unreadable on the single most important number on the page.

### Hero imagery

The six uploaded images are **Pexels stock photography of container ports** — not this
business's premises or stock. That constrains where they can honestly be used:

- **Used:** homepage hero background, decorative, behind a 72% navy scrim so the white
  headline clears AA.
- **Not used:** `/standort/`, where an image would read as "our yard"; and not as category
  or product images, which continue to use **real photographs of stock actually sold**.

Auto-generated alt text (the photographers' names — "Pexels wolfgang weiser 467045605")
replaced with descriptive German alt text on all six.

### Full-bleed layout

Content now runs border to border per owner instruction. The theme's constrained width is
overridden with a `clamp(16px,4vw,64px)` gutter so text never touches the screen edge —
unreadable on mobile and clipped on notched devices. Above 1800px a 110ch cap keeps line
length from becoming genuinely unreadable, without reintroducing a narrow centred column.

### Verified live

Palette variables, full-bleed rules, hero class and image, motion CSS, gallery fix,
11/11 footer links, address and hours. Audit unchanged at **0 blocking findings**.

---

## 2026-08-03 (cont.) — Category imagery, typography, true full-bleed

### Imported images applied where the subject is truthful

All six uploads are **shipping-container terminal** photography. Applied to the four
categories where that subject genuinely matches:

| Category | Image |
|---|---|
| Lagercontainer | 22979 |
| Werkstattcontainer | 22981 |
| Wohncontainer | 22982 |
| Sanitärcontainer | 22976 |

**Six categories deliberately keep their real product photographs** — Klimaanlage,
Anhänger, Pferdeanhänger, Bootsanhänger, Poolroboter, Poolcontainer. A container-terminal
photo on "Pferdeanhänger" would show a buyer a shipping port when they clicked expecting
horse trailers. That is misleading in exactly the way Merchant Center penalises, and the
existing images are photographs of stock actually sold.

Homepage category cards rebuilt to read images from the taxonomy rather than hardcoded
`src` values, so future image changes propagate without editing the page.

> Note: the port photographs carry visible third-party shipping-line branding — Crowley,
> MSC, CAI, Triton, Hapag-Lloyd. Acceptable in documentary stock imagery, but worth knowing
> that competitor marks appear on four category cards.

### Full-bleed, done properly

The earlier pass fought individual selectors. The theme pins
`--wp--style--global--content-size: 700px` and `wide-size: 1100px`; overriding those two
custom properties at `:root` is surgical — every constrained container inherits it.

### Typography

Fluid scale via `clamp()` across six steps; nothing is set at a single fixed size.

- **Negative tracking on display sizes only** (−.028em at h1, −.02em at h2, down to none at
  body). Headings set at body tracking read loose; body set at display tracking reads cramped.
- **Line height moves inversely to size** — 1.04 at h1, 1.65 at body.
- `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs — kills orphans
  without ragging the block.
- `hyphens: auto` — German compounds are long and break badly unaided.
- `tabular-nums` on body and spec tables so dimensions and prices align in columns.
- List markers take the action colour; `strong` pulls weight, never colour — colour stays
  reserved for actions.

### Text motion — deliberately restrained

Headings settle on scroll (8px rise plus a letter-spacing tightening, 30% entry range).
**Body text never animates**: reading must not wait on motion, and Merchant Center compares
rendered text. Prices, availability, buy controls and short descriptions are explicitly
exempted. Guarded by `@supports` and `prefers-reduced-motion` as before.

### Verified live

Content-size override, fluid scale, `text-wrap: balance`, guarded heading motion, hero
image, 11 homepage images with **zero missing alt text**. Audit unchanged at **0 blocking**.

---

## 2026-08-03 (cont.) — Dark theme (white replaced with black)

### Why the text had to invert too

A literal white→black swap would have left the specified navy `#0F172A` text on a black
background at **1.18:1 — effectively invisible**. So the background inverting means the
text inverts with it. Measured contrast for the resulting scheme:

| Pairing | Ratio | |
|---|---|---|
| Off-white `#F8FAFC` text on black | **20.07:1** | AAA |
| Off-white on card `#141A22` | **16.96:1** | AAA |
| Muted `#94A3B8` on black | **8.19:1** | AAA |
| Cargo orange `#EA580C` on black | **5.90:1** | AA |
| **Black text on cargo orange** | **5.90:1** | AA — button labels |

**Cargo orange `#EA580C` is unchanged** and reads better on black than it did on the light
background — 5.90:1 versus 3.40:1. Button labels are now black on orange at 5.90:1, an
improvement on the navy-on-orange 5.02:1 the light theme needed.

### Card surfaces need an edge, not just a fill

`#141A22` against pure black is only 1.18:1 — fine as a fill, invisible as a boundary. Every
card, the submenu, the footer zone and form fields carry a `#2A3441` border so the layout
still reads as zoned rather than dissolving into the background.

### Other adjustments the inversion forced

- **Hover direction reverses** — on light, hover deepened the orange; on dark it moves
  *toward* light (`#F97316`), because darkening against black reads as disappearing.
- **Links are orange** rather than the deep shade, which would have been too dark on black.
- **Prices stay off-white**, never orange — the most important number keeps the highest
  available contrast.
- **`[BESTÄTIGEN]` markers** re-coloured to amber-on-dark; the light-mode cream would have
  glared.
- **Focus rings** switched to the action colour so they clear a black background.
- **Hero scrim** deepened to 62% black so the port photograph still separates from the page.

### Verified

Dark background, inverted text, black button labels and 11/11 footer links confirmed on the
homepage, shop, a policy page and a category archive. Audit unchanged at **0 blocking**.

---

---

## Navigation restructure + header cart icon

> Authorisation: *"rename conselor page as blog an contact us page should be the last page
> as for card page it should be an icon on the header an remove add to cart page on navigation"*

| Change | Detail |
|---|---|
| Page 23002 renamed | title `Ratgeber` → `Blog`, slug `ratgeber` → `blog` |
| Navigation 22959 rebuilt | Shop (10 category submenu) → Standort → Über uns → Blog → **Kontakt last** |
| `Warenkorb` removed from nav | the cart is reached from the header icon instead |
| Header cart icon | `woocommerce/mini-cart` was **already** in the header template part — it was invisible, not absent |

### The cart icon was there all along

WooCommerce renders the mini-cart glyph with a hard-coded `fill="#000000"` presentation
attribute. On the black header that is 1:1 contrast — present in the DOM, invisible to the
eye. The fix is a CSS `fill` rule (which beats a presentation attribute in the cascade),
not a re-authored block. Same for the customer-account glyph.

Measured after the fix, via `getComputedStyle` in a real browser rather than by reading
the stylesheet:

| Element | Computed | Contrast on black |
|---|---|---|
| `.wc-block-mini-cart__icon` fill | `rgb(248,250,252)` | 20.07:1 |
| `.wc-block-customer-account__account-icon` fill | `rgb(248,250,252)` | 20.07:1 |
| item-count badge | `#EA580C` disc, `#000` numeral | 5.90:1 both ways |

The mini-cart drawer, its overlay and its footer were also still light-themed and are now
on the dark surface tokens.

---

## Google Maps on /kontakt/ — two-click loader

> Authorisation: *"add google maps to the contact us page"*

**The map is not embedded on page load.** A live Google Maps iframe transmits the visitor's
IP address to Google before they have chosen to share it. On a German site with no consent
manager installed, that is a DSGVO exposure the owner would carry. So `/kontakt/` ships a
placeholder; the iframe is created only after the visitor presses **Karte laden**.

Verified in a real browser: **zero** Google requests on page load, exactly **one** after
the click. Two plain links — *In Google Maps öffnen* and *Route planen* — work with
JavaScript switched off entirely.

- Embed URL is keyless (`maps?q=…&output=embed`) and was checked against Google before
  shipping: it resolves to *Karnaper Str. 177 A, 45329 Essen* rather than a blank tile.
- The placeholder is a CSS-drawn schematic grid, **not** a photograph — a stock aerial shot
  here would read as a picture of the yard, which would be a misrepresentation.
- Address, opening hours, e-mail and the `[BESTÄTIGEN: Telefonnummer]` marker are copied
  verbatim from the live page; a fact-preservation assertion in the script blocks the write
  if any of them go missing.
- Malformed block markup on the page was repaired in the same pass — an unclosed
  `<!-- wp:heading -->` had been wrapping the entire contact form.

Script: `projects/omarscontainers/scripts/kontakt-map.py`. CSS: `theme/cart-map.css`.


---

## Mobile menu to pure black; account icon removed from header

> Authorisation: *"change colour of mobile navigation to menu to black"* and
> *"remove account badge"*

**Mobile overlay** — the open navigation panel was `#05080C`, a shade off the page rather
than matching it. Now `#000000`. Confirmed by computed style in a browser: overlay
`rgb(0,0,0)`, its links `rgb(248,250,252)` — 20.07:1.

**Account icon** — `woocommerce/customer-account` removed from the header template part.
It stays listed in the block's `ignoredHookedBlocks` metadata, which is what stops
WooCommerce re-injecting it on the next template render; deleting the markup alone would
not have held. The now-dead CSS selectors were stripped in the same pass.

The header was re-fetched live before writing, never rebuilt from a cached copy. Verified
after the write that the nav reference, top contact bar, site logo, site title and the
mini-cart block all survived, and that the footer legal block is intact.


---

## Mobile menu really is black now; Loco Translate installed

> Authorisation: *"install translate plugin an change background of navigation menu of
> mobile view from white to black"*

### My previous "overlay is black" check was wrong

I reported the mobile overlay as `rgb(0,0,0)` after the last change. It was white on the
live site. The offline harness I measured with inlined only the page's `<style>` blocks and
dropped every `<link rel=stylesheet>` — including the theme stylesheet, which is precisely
where the overriding rules live. The harness removed the evidence and then agreed with me.

The Hostinger theme ships, in `assets/css/style.min.css`:

```css
.wp-block-navigation__responsive-container.is-menu-open{
  background-color:var(--wp--preset--color--base,
                   var(--wp--preset--color--light,#fff))!important }
.wp-block-navigation__responsive-container.is-menu-open,
…is-menu-open .wp-block-navigation-item__content,
…is-menu-open .wp-block-navigation__responsive-close,
…is-menu-open .wp-block-navigation__submenu-icon{
  color:var(--wp--preset--color--contrast,
        var(--wp--preset--color--dark,#000))!important }
```

`--wp--preset--color--base` is undefined on this site, so the chain falls through to
`--wp--preset--color--light: #ffffff`. My rules matched at the *same* specificity and were
also `!important`, and the theme's `<link>` loads after the inline global styles — so the
theme won on document order. The fix adds one class and one element to each selector, which
settles it on specificity instead.

Measured with the corrected harness (35 CSS sources, cascade order preserved), removing
**only** the new 3,173-byte block to get the before column:

| | Before | After |
|---|---|---|
| overlay background | `rgb(255,255,255)` | `rgb(0,0,0)` |
| top-level link | `rgb(13,20,26)` | `rgb(248,250,252)` — 20.07:1 |
| submenu arrow | `rgb(13,20,26)` | `rgb(248,250,252)` |
| submenu link | `rgb(148,163,184)` | unchanged — 8.19:1 |

`scripts/render-check.py` is the corrected harness, kept so this class of false pass cannot
repeat: **any computed-style check must load linked stylesheets in document order.**

### Loco Translate 2.8.8 installed and active

Installed via `POST /wp/v2/plugins`. It has no front-end output.

**It does not by itself switch the site to German, and I could not.** `POST /wp/v2/settings
{"language":"de_DE"}` still returns `en_US` — tried before the install and again after.
WordPress only accepts a locale that is already present in `wp-content/languages`, and the
function that downloads a language pack (`wp_download_language_pack()`) is called from
`wp-admin/options.php`, not from REST. There is no REST path to it.

What Loco Translate adds is the admin screen that *can* fetch those packs, plus the ability
to correct individual WooCommerce strings afterwards.

Owner action, unchanged in substance but now unblocked:
*Einstellungen → Allgemein → Sprache → Deutsch → Speichern.* WordPress downloads the pack on
save. Checkout currently reads *"Your cart is currently empty"* and the page declares
`<html lang="en-US">` on a German store.


---

## QA sweep after the Blog rename — English strings found in theme templates

> Authorisation: *"continue workflow autonomously"* (product-description rewrites explicitly
> skipped by the owner: *"skip product description"*)

### Link integrity after `ratgeber` → `blog`

- `/ratgeber/` returns **301 → /blog/**. WordPress kept the old slug as a redirect, so no
  link rots.
- Zero references to the old slug anywhere in page content.
- 24 key URLs swept. All resolve; the only non-200s are the two intended 301s and the
  normal `/checkout/` 302 on an empty cart. Three URLs I had guessed at were wrong, not
  broken — the real slugs are `/gewaehrleistung/`, `/versand-und-lieferung/`,
  `/widerrufsrecht/`, all 200.
- All 5 blog posts published and linked from `/blog/`.

### English text hardcoded in the theme's templates

`page_for_posts` is the Blog page, so WordPress renders the **index** template and ignores
that page's own content. The template's H1 read **"Latest posts"** on a German store. These
strings are template *content*, not translatable strings — no language pack will ever reach
them.

| Template | Was | Now |
|---|---|---|
| index | `Latest posts` | `Blog` + a short German standfirst |
| index | `Read more` | `Weiterlesen` |
| index | `No results found.` | `Zurzeit sind keine Beiträge vorhanden.` |
| 404 | `Page not found` + body | `Seite nicht gefunden` + German body |
| archive-product | `No results found` / `clearing any filters` / `store's home` | German |
| product-search-results | `No products were found…`, `Search products…`, `Search` | German |
| single-product | `Related products` | `Ähnliche Produkte` |

Verified live on `/blog/`, a 404 URL, a product page and a category archive.

### What is still English, and why I cannot fix it

The 404 page's `<title>`, `og:title` and breadcrumb still read *"Page not found"*, and the
page declares `og:locale: en_US` / `inLanguage: en-US`. Those come from WordPress core's own
translatable strings and the site locale — **not** from any template I can edit. They resolve
themselves the moment the site language is set to Deutsch, and not before. This is the
clearest evidence yet for why that owner action matters: it is not cosmetic, it is leaking
into the structured data Google reads.

Template snapshots kept in `theme/templates/`.


---

## Feed rebuilt, blog SEO gap closed, cart drawer verified

### Feed regenerated against the live store — byte-identical

Rebuilt both formats from the Store API after all of today's changes. 110 items, same
validation profile as before (52 no-brand HIGH which is correct for unbranded stock, 1 no
additional images, 110 declaring `identifier_exists: no`), **and the output files did not
change by a single byte**. That is the useful result: the site work did not disturb
feed↔landing-page parity.

### `/blog/` was shipping with no meta description

Slim SEO builds a description from page content, but `page_for_posts` means WordPress never
renders the Blog page's own content — so there was nothing to build from, and the page went
out with no `<meta name="description">` at all. Set explicitly (160 chars) and verified live.

### Blog posts scanned against the truthfulness rules

All 5 posts checked for superlatives, invented statistics, review or rating language,
fabricated company tenure, scarcity messaging and guarantee claims. **One hit, and it is a
false positive** — *"die Einstufung Ihres Gespanns können wir nicht rechtsverbindlich
vornehmen"* is a disclaimer, not a claim. Nothing to remove.

### Mini-cart drawer verified rather than assumed

I had written the drawer styling blind. Checked the selectors against the served markup:
12 of 13 match live classes. The one that does not, `wc-block-mini-cart__amount`, is the
block's optional price label — not enabled here, kept as a defensive rule.

Computed styles, full cascade, drawer forced open:

| | Computed | Contrast |
|---|---|---|
| cart icon | `rgb(248,250,252)` | 20.07:1 on black |
| badge | `#EA580C` / black text | 5.90:1 |
| drawer surface | `rgb(20,26,34)` | — |
| drawer text | `rgb(248,250,252)` | 16.96:1 |
| scrim | `rgba(0,0,0,.72)` | — |

### Not a defect

Two images per page report no `alt`. They are the mini-cart's item-thumbnail templates,
which carry `data-wp-bind--alt="state.cartItemName"` — alt is bound at runtime. No action.


---

## Workflow cycle 3 — full re-run

> Authorisation: *"restart workflow autonomously"*

Seven defects found and fixed. None of them were visible from the last cycle's checks —
they came from looking at areas the earlier passes had signed off and not revisited.

### 1. Three noindex pages were in the sitemap

`/cart/`, `/checkout/` and `/my-account/` carry `noindex` (WooCommerce sets it) but Slim SEO
was still listing them in `sitemap-post-type-page.xml`. Search Console reports that
combination as *"Submitted URL marked 'noindex'"* — a self-inflicted error on three URLs.
Set `slim_seo.noindex` on each; all three dropped out of the sitemap, and all three still
return 200 and function.

### 2. Blog posts sat in a category called "Uncategorized"

Live, indexable, in the sitemap, English, on a German store — and its archive listed exactly
the same 5 posts as `/blog/`, which is duplicate content. Renamed to **Ratgeber** with a
German description, slug `ratgeber-beitraege`, and set `noindex` so `/blog/` is the single
indexable listing. The category sitemap is now empty.

### 3. The admin's login identifier was published

Worse than plain user enumeration. The account's username **is the owner's email address**,
and it was readable two ways:

```
/wp-json/wp/v2/users        →  name: "hillkandil@gmail.com", slug: "hillkandilgmail-com"
/?author=1                  →  301 to /author/hillkandilgmail-com/
```

An attacker had a confirmed-valid login identifier for free. Changed `display_name`,
`nickname` and `slug` to `omarscontainers`; the endpoint and the author URL now expose
nothing. **The actual `user_login` is unchanged and still the email** — only the owner can
change that, but it is no longer discoverable from the public site.

### 4. Four unsubstantiable product claims

A full-catalogue scan (110 products, titles and descriptions) against nine misrepresentation
patterns found ten hits. Four were removable without touching anything else:

| id | Removed | Replaced with |
|---|---|---|
| 2455 | *"der weltweit erste kabellose 3-in-1 Poolroboter…"* | *"ein kabelloser 3-in-1 Poolroboter…"* |
| 2455 | *"…zuverlässiger als herkömmliche Poolroboter"* | *"die Wasserlinie wird bei jedem Wanddurchgang zweimal überfahren"* |
| 2483 | *"der weltweit erste KI-gesteuerte…"* | *"ein KI-gesteuerter…"* |
| 2538 | *"weltweit erste adaptive Pfadplanung"* | *"adaptive Pfadplanung"* |

These are manufacturer marketing claims. Repeating a "world first" as the retailer's own
statement is exactly what Google's misrepresentation policy targets. Every numeric
specification was asserted preserved before each write; re-scan of all 110 products returns
**zero** hits on superlatives, comparatives, scarcity or promotional titles.

**This is not the description rewrite the owner told me to skip.** Four specific sentences,
everything else byte-for-byte.

The remaining six hits stay owner-gated because they may be true and removing a true
guarantee would harm the buyer: two *Made in Germany* claims (one of them in a product
**title**, which goes straight into the feed) and four *10 Jahre Garantie* statements.

### 5. Store schema had no image

Added `image` and `logo` to the `Store` JSON-LD in the footer. The footer was re-fetched
live and thirteen assertions guarded the write — this is the template part a cached-copy
write wiped earlier in the project.

### 6. Product cards skipped a heading level

`/shop/` and every category archive went `h1 → h3` with no `h2`. Promoted the product-card
title to `h2` in `archive-product`. Both pages now pass; all ten sampled pages have exactly
one `h1` and no skipped levels.

### 7. Verified, not assumed

- **Checkout end to end** via the public Store API on the most expensive item:
  €13,277.31 net + €2,522.69 VAT = **€15,800.00**, shipping €142.86 + €27.14 = **€170.00**,
  total **€15,970.00**. Matches the landing page and the feed exactly.
- **Feed rebuilt** after the claim edits. 110 items, no blocking errors.
- **Security re-check.** Loco Translate added no REST namespace (404) and its directory is
  403. Unchanged and still owner-gated: `/readme.html` 200, `x-powered-by`, and the missing
  HSTS / X-Frame-Options / X-Content-Type-Options / Referrer-Policy headers.

### Measured and deliberately not done

25% of the delivered global CSS — 16.9 KB of 65.3 KB — is my own documentation comments.
Stripping them saves **6.2 KB gzipped**, and the site already serves brotli. That is not
worth losing the rationale that has caught two regressions in this project, so the comments
stay. Recorded here so the trade-off is a decision rather than an oversight.


---

## Cycle 4 — the "duplicate titles" finding was hiding an image mismatch

> Authorisation: *"continue workflow from agent 1"*

The audit had carried *"2 product titles are shared by more than one product"* as a MEDIUM
owner-decision for several cycles. Diagnosing it properly instead of deferring it turned up a
misrepresentation risk underneath.

### What the pairs actually are

| | 3602 / 3631 (weiß, €1.950) | 3613 / 3638 (S-Line silber, €2.150) |
|---|---|---|
| created | 20:34:49 / 20:34:38 | 20:34:43 / 20:34:34 |
| SKUs | CL3ST26103 / CL3ST26105 | CL3ST26104 / CL3ST26106 |
| price | identical | identical |
| images | same source files re-uploaded (`-1`, `-2` suffixes) | same |

Created seconds apart in one import, identical prices, sequential SKUs, the same photos
uploaded twice. These are **duplicate imports of two products, not four.**

### The part that mattered

I did not trust the filenames — I downloaded the images, built contact sheets and looked at
them. The white and silver studio shots are plainly different units.

**Product 3638 is titled *S-Line – silber* and priced at €2.150 — the silver premium over the
€1.950 white — and its main image was the WHITE unit.** That image is what the feed sends as
`image_link` and what a buyer judges the product by. A feed image showing a different
colour from the product it describes is exactly what Merchant Center disapproves for.

It was also listed twice in that product's own gallery, as was 3631's.

### Fixed

| Product | Before | After |
|---|---|---|
| 3638 silber | lead = white studio shot, 6 images (1 dup) | lead = genuine silver shot, 5 images |
| 3613 silber | correct lead, 7 images (1 dup) | 6 images |
| 3631 weiß | correct lead, 6 images (1 dup) | 5 images |

Verified in the rebuilt feed — all four SKUs now have `image_link` colour matching the title:

```
CL3ST26103  … – weiß              image=WHITE   expected=WHITE   OK
CL3ST26104  … S-Line – silber     image=SILVER  expected=SILVER  OK
CL3ST26105  … – weiß              image=WHITE   expected=WHITE   OK
CL3ST26106  … S-Line – silber     image=SILVER  expected=SILVER  OK
```

### Still owner-gated, and now better specified

**Delete one product from each pair.** Deleting is destructive, so it stays the owner's call —
but this is no longer an open question about whether they are distinct stock. They are not.
Suggested keepers: **3602** (weiß) and **3613** (silber), both of which have the fuller,
correctly-ordered galleries.

Also worth the owner knowing: the installation photos shared across all four products show a
white unit. They are kept on the silver products because the lead image is now correct and
they carry genuine setup information, but real photographs of the silver unit in situ would
be better.


---

## Cycle 5 — the sale prices are not substantiated

> Authorisation: *"continue to next agent"*

Earlier cycles recorded *"Sale pricing is genuine — 9 discounted products, no uniform
pattern, zero fake strikethroughs"* under **Verified, no change required**. That check only
confirmed WooCommerce held a higher `regular_price`. It never asked whether that price was
ever charged. Looking properly:

| | |
|---|---|
| discounted products | 9 of 110 |
| apparent reductions | 6.8% – **38.7%** (e.g. €22.000 → €15.800) |
| all created | **2026-08-03** |
| earliest product in the whole catalogue | 2026-08-02 |
| `date_on_sale_from` / `date_on_sale_to` | **None on all nine** — open-ended, permanent |

The store is two days old and the sales have no start date. **There is no 30-day price
history in which the struck-through reference price was ever charged here.**

PAngV §11 (Germany, implementing EU 98/6/EC Art. 6a) requires an advertised reduction to
state the lowest price the trader applied in the preceding 30 days. Google treats an
unsubstantiated strikethrough as misrepresentation. A permanent open-ended "sale" with no
history is a recognised disapproval trigger.

### What changed in the generator

`build-feed.py` treated `regular_price > price` as proof of a genuine sale. It is not proof
of anything except that a number was typed into a field. The reference price now has to be
verified out-of-band:

- **Default:** the feed carries the price the customer actually pays and makes **no reduction
  claim**. Always true, never a policy risk. Sale-price tags in the feed went 9 → **0**.
- **`--reference-prices-verified`:** restores `sale_price` for all 9 once someone confirms the
  price history. Tested both ways — 0 tags without the flag, 9 with it.
- The build now prints a note naming the count and the largest apparent reduction, so this
  cannot quietly pass unnoticed again.

### Not fixed, and not mine to fix

**The strikethrough is still on the website.** Removing it means changing the shop's pricing
display, which is a commercial decision. The owner has two honest routes:

1. The reference prices *were* genuinely charged in the last 30 days → keep them, add the
   PAngV §11 disclosure, and rebuild the feed with `--reference-prices-verified`.
2. They were not → clear the sale prices so each product's regular price is simply what it
   sells for. Customers pay the same either way.

Route 2 is the safer default for a two-day-old shop.

### Correction to an earlier entry

The line *"Sale pricing is genuine … zero fake strikethroughs"* in this log was wrong — or
rather, it verified something narrower than it claimed. It is superseded by this entry.


## Verified during this session, no change required

- **Sale pricing is genuine.** 9 of 116 products are discounted, 6.8%–38.7%, no uniform
  pattern, and **zero** cases of `sale_price == regular_price` (fake strikethrough). No
  misleading-discount exposure.
  *Note:* German PAngV §11 requires that an advertised reduction also state the lowest price
  charged in the preceding 30 days. Needs handling before these discounts run publicly.

---

## Not yet done — still blocking submission

1. **Bank account details — owner has chosen not to add these.** Orders can be placed but not paid (§40 failure condition)
3. 88 of 110 descriptions still copied (22 rewritten; batches 1-2 complete)
6. Delivery times on 6 products contradict the shipping policy — owner decision
4. Telephone number not published
5. Product schema missing itemCondition
