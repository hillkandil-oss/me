# Go-Live Checklist — kaisercontainers

Everything below is **staged** (drafts / unassigned) so the live public site is unchanged.
Flip it live in this order once the owner facts are confirmed and placeholders are filled.

## A. Fill verified facts first (removes every 〔BITTE BESTÄTIGEN〕 marker)
- [ ] Store phone (Duisburg) — header, footer, all pages, schema
- [ ] Exact street + house number — address everywhere, map pin
- [ ] Impressum: responsible person name, legal form, USt-IdNr., Handelsregister (if any)
- [ ] Prices net/gross (inkl./zzgl. USt.) — AGB, Zahlung, product display, feed
- [ ] Real store/yard photo for homepage About slot (no fabricated images)

## B. One GUI step the REST API cannot do
- [ ] WordPress → Settings → General → Site Language → **Deutsch** (installs de_DE pack)

## C. Publish content (WordPress admin or via API)
- [ ] Publish pages: Startseite, Kontakt, Über uns, Impressum, Datenschutz, AGB,
      Widerruf, Versand, Zahlung, FAQ (currently draft ids: 128, 119, 120, 121, 122,
      123, 124, 125, 126, 127)
- [ ] Settings → Reading → Front page displays **a static page → "Startseite"**
- [ ] Remove/trash old English stubs: "Privacy Policy" (id 3), "Refund and Returns" (id 13);
      repoint WooCommerce privacy page → Datenschutz, terms page → AGB
- [ ] WooCommerce → Settings → Advanced → **Terms page = AGB** (id 123) — not settable via
      API; then enable the terms checkbox at checkout (WooCommerce → Settings → Advanced)
- [ ] Add a **delivery** shipping method to the "Deutschland" zone once the freight cost basis
      is known (pickup already configured); or keep "delivery quoted on request"

## D. Apply theme layer (GUI)
- [ ] Appearance → Customize → **Additional CSS** → paste `theme/snippets/brand.css`
- [ ] Enqueue fonts **Archivo** + **Inter** (theme fonts / Elementor / @font-face)
- [ ] Header builder: add top info bar from `theme/snippets/header-topbar.html`
- [ ] Footer builder: add footer from `theme/snippets/footer.html`
- [ ] Assign **Main Menu** (id 28) to the **main_menu** theme location

## D2. Rank Math SEO (installed & active — finish in GUI)
- [ ] Run the Rank Math **Setup Wizard** (Rank Math → Dashboard)
- [ ] Settings → Permalinks → **Save** (flushes rewrite → activates `sitemap_index.xml`)
- [ ] Titles & Meta: set homepage title/description + product/category title templates (German)
- [ ] **Local SEO** module: enter verified business (name, street, Duisburg, 47138, phone,
      hours Mo–Sa 08:00–18:30, geo). **Use EITHER Rank Math Local SEO OR
      `theme/snippets/schema-jsonld.php` — not both** (avoid duplicate LocalBusiness schema)
- [ ] Ensure WooCommerce module on → Product/Offer/Breadcrumb schema emitted
- [ ] Per-page SEO titles for key pages (not writable via API; set here)

## E. Verify after go-live
- [ ] Header phone/email/directions links work; address consistent everywhere
- [ ] Nav renders on one line desktop; Container dropdown works; mobile menu works
- [ ] Homepage sections in order; contact form is the final section before footer
- [ ] Contact form delivers to info@kaisercontainers.de (send a test)
- [ ] Google Map loads on Kontakt page as final section; Route-planen link works
- [ ] LocalBusiness + Product schema validate (see task #8)
- [ ] No 〔BITTE BESTÄTIGEN〕 markers remain anywhere public
