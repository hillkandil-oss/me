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
