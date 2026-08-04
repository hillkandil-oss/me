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

## D. Apply theme layer (GUI)
- [ ] Appearance → Customize → **Additional CSS** → paste `theme/snippets/brand.css`
- [ ] Enqueue fonts **Archivo** + **Inter** (theme fonts / Elementor / @font-face)
- [ ] Header builder: add top info bar from `theme/snippets/header-topbar.html`
- [ ] Footer builder: add footer from `theme/snippets/footer.html`
- [ ] Assign **Main Menu** (id 28) to the **main_menu** theme location

## E. Verify after go-live
- [ ] Header phone/email/directions links work; address consistent everywhere
- [ ] Nav renders on one line desktop; Container dropdown works; mobile menu works
- [ ] Homepage sections in order; contact form is the final section before footer
- [ ] Contact form delivers to info@kaisercontainers.de (send a test)
- [ ] Google Map loads on Kontakt page as final section; Route-planen link works
- [ ] LocalBusiness + Product schema validate (see task #8)
- [ ] No 〔BITTE BESTÄTIGEN〕 markers remain anywhere public
