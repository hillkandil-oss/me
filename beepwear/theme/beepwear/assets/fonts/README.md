# Fonts (self-hosted, installed)

Variable woff2 files, referenced by `style.css` / `inc/enqueue.php`:

- `cormorant-garamond.woff2` — display serif, variable (weights 300–600). ✅ present
- `manrope.woff2` — body/UI sans, variable (weights 300–700). ✅ present

Both are the latin-subset variable fonts from Google Fonts (SIL Open Font License),
self-hosted for performance and privacy (no Google CDN calls). To refresh or add more
subsets (e.g. latin-ext, cyrillic), re-export from Google Fonts and replace in place —
the `@font-face` weight ranges already cover the full axis.
