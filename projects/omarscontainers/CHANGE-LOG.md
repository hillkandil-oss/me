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

## Verified during this session, no change required

- **Sale pricing is genuine.** 9 of 116 products are discounted, 6.8%–38.7%, no uniform
  pattern, and **zero** cases of `sale_price == regular_price` (fake strikethrough). No
  misleading-discount exposure.
  *Note:* German PAngV §11 requires that an advertised reduction also state the lowest price
  charged in the preceding 30 days. Needs handling before these discounts run publicly.

---

## Not yet done — still blocking submission

1. No payment gateway enabled — **checkout still cannot complete**
2. No shipping zone or freight rates for Germany
3. No legal pages (Impressum, Datenschutz, Widerruf, AGB, Versand, Zahlung, Kontakt)
4. Condition attribute unset on all 110 products (brands now done)
5. 110 descriptions still copied from third-party sites
