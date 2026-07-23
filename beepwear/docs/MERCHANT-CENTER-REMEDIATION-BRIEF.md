# BeepWear — Remediation Work Order (for a Claude Code session with WordPress access)

**Goal:** Close the remaining gaps from `MERCHANT-CENTER-LIVE-AUDIT-2026-07-23.md` so
beepwear.com is submit-ready. Unlike trenchsafety.org, this is a **finish-and-polish**, not
a rebuild — the live site's identity story, policies, contact, and checkout already hold up.

**Platform:** WordPress + WooCommerce 10.9.4, Rank Math SEO. Admin: WordPress Application
Password (per `LIVE-STATUS.md`). 269 products imported; some may still be draft.

---

## ⛔ RULE FOR THE AGENT — read first

This is a **Google Merchant Center compliance** job; misrepresentation is the risk. **NEVER
invent business facts.** Do not fabricate a brand, GTIN, product spec, legal entity name, or
any identity/contact detail. If a required real value is missing from "Owner inputs" below,
**stop and ask the owner.** An invented value is the exact thing Google bans stores for.

---

## 🔑 ACCESS THE AGENT NEEDS (owner provides)

- WordPress **Application Password** for the admin user, and/or WooCommerce **REST API** keys
  (Read/Write) — WooCommerce → Settings → Advanced → REST API.
- **Back up first**; prefer working on staging if available.

---

## 📋 OWNER INPUTS REQUIRED (fill before the agent starts)

1. **Identity reconciliation (the one real P1).** The audit confirmed the business identity is
   currently inconsistent across surfaces. Provide:
   - The single legal entity behind BeepWear (existing entity + **"BeepWear" as a DBA**, or a
     new BeepWear LLC/sole prop).
   - The exact business name + address to show on the site, Merchant Center, and the payment
     processor.
   - The payment processor legal name and the **checkout/statement descriptor** (should read
     "BEEPWEAR").
   > Note: founder/operator/owner may be different real people; domain WHOIS may stay private.
   > Only the website ⇄ Merchant Center ⇄ payment-processor identity must match.
2. **Brands for the 47 unbranded products.** They're flagged in `data/products-mc-audit.csv`.
   Provide the true brand for each (or mark genuinely unbranded).
3. **GTIN/UPC** only where they genuinely exist per product (else identifier-exists = no).
4. **Founder story choice:** Charles Beep is confirmed real, so you may **keep/restore the
   named About story** or keep the de-personified version in `content/about.md`. Say which.
5. Confirm the **return window / shipping / hours** shown live are final (they currently read
   as complete: 30-day returns, 5–10 business-day refunds, $120 US flat shipping).

---

## 🛠 PHASE 1 — Business-identity consistency (P1)

- Add a footer + Terms line stating the legal entity / DBA (e.g. "BeepWear is a trading name
  of <Entity>."), matching Owner input #1.
- Ensure **WooCommerce → Settings** store name/address and **Merchant Center business info**
  match the site exactly, and the **payment gateway** account/descriptor reads as BeepWear.
- No `/about/` change required for the founder (he's real); apply Owner input #4 if restoring
  the named story.

## 🏷 PHASE 2 — Products: brand, condition, identifiers (P1–P2, via REST API)

- **Assign brand** to the 47 flagged products from the owner's list (WooCommerce Brands
  taxonomy / `product_brand`).
- **Condition:** live product pages show condition under "Additional information" — ensure the
  **Merchant Center feed carries `condition`** (used/new) matching each page exactly. Fix any
  product whose page and feed disagree.
- **GTIN/MPN:** set where the owner supplied real values; otherwise set identifier-exists = no.
  Never invent.
- Confirm **price = landing page = checkout** and availability is accurate on all 269.
- **Publish** any products still in draft (only after Phases 1–3 pass).

## ✍️ PHASE 3 — Description quality (P2)

- The descriptions are original but thin/formulaic ("rewards a closer look", "dive-ready
  build"). Enrich the **top-value / best-selling** listings first with real specifics: case
  size, movement (auto/quartz), materials, reference, box/papers status, condition detail.
- Keep copy original and accurate; if AI-assisted, place it in the **`structured_description`**
  attribute. Do not copy manufacturer marketing text.

## 🔧 PHASE 4 — Minor polish (P3)

- Add a real **"Last updated" date** to `/privacy-policy/` and `/terms/`.
- On `/contact/`, either add **real, active social links** or remove the empty "Social"
  heading (don't fabricate profiles).

## 🔎 PHASE 5 — Final QA sweep (before Merchant Center)

Confirm:
- No `[confirm:` / placeholder / empty `** **` on any published page (sweep below).
- Every product has: true brand, accurate condition, a price, a real image ≥ 500×500.
- Business name/contact identical across site, policies, Merchant Center, payment processor.
- Google product category mapped to **Apparel & Accessories > Jewelry > Watches (201)**.
- Retain authenticity/sourcing documentation for the luxury inventory (Google may request it).

**Then:** connect Google for WooCommerce on the verified `beepwear.com`, set condition = as per
product, and request review **once**. Luxury watches may still get manual review; approval is
never guaranteed.

---

## Appendix — verification commands (for the agent)

```bash
# 1) sweep live pages for leftover placeholders (expect no output):
for url in / /about /contact /returns /shipping-policy /privacy-policy /terms /authenticity-guarantee; do
  curl -s "https://beepwear.com$url" | grep -Eio "\[confirm:|lorem ipsum|\*\* *\*\*|tbd" | sort -u | sed "s|^|$url: |"
done

# 2) list the 47 unbranded products to assign (from the repo audit file):
#    open data/products-mc-audit.csv and filter rows flagged as missing brand.
```
