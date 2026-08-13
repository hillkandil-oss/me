/* omarscontainers — interim German labels.
 *
 * STOPGAP, NOT LOCALISATION. The correct fix is Settings > General > Site
 * Language > Deutsch (Sie), which loads the real language pack and translates
 * everything at the source. That cannot be done over the REST API, so until it
 * is set this rewrites the customer-visible English that WooCommerce and core
 * emit.
 *
 * Design constraints:
 *   - Exact whole-string matches only. No partial or fuzzy replacement, so a
 *     product description containing "Total" is never touched.
 *   - Rewrites the real text node, not a CSS ::after overlay, so screen readers
 *     get German too rather than hearing English while sighted users see German.
 *   - Idempotent and self-disabling: once the language pack is installed there
 *     are no English strings left to match and this becomes a no-op.
 *   - Skips script, style, textarea and input so nothing functional is altered.
 */
(function () {
  "use strict";

  var MAP = {
    "Add to cart": "In den Warenkorb",
    "Select options": "Optionen wählen",
    "Read more": "Weiterlesen",
    "View cart": "Warenkorb ansehen",
    "Description": "Beschreibung",
    "Additional information": "Weitere Informationen",
    "Reviews": "Bewertungen",
    "Sale!": "Reduziert",
    "Subtotal": "Zwischensumme",
    "Total": "Gesamt",
    "Home": "Startseite",
    "Skip to content": "Zum Inhalt springen",
    "Your cart is currently empty": "Ihr Warenkorb ist derzeit leer",
    "Your cart is currently empty!": "Ihr Warenkorb ist derzeit leer.",
    "No products in the cart.": "Keine Produkte im Warenkorb.",
    "Products in cart": "Produkte im Warenkorb",
    "Product": "Produkt",
    "Details": "Details",
    "Available on backorder": "Lieferbar auf Bestellung",
    "Previous price:": "Vorheriger Preis:",
    "Discounted price:": "Reduzierter Preis:",
    "Sort by popularity": "Nach Beliebtheit sortieren",
    "Sort by average rating": "Nach Bewertung sortieren",
    "Sort by latest": "Nach Neuheit sortieren",
    "Sort by price: low to high": "Preis aufsteigend",
    "Sort by price: high to low": "Preis absteigend",
    "Default sorting": "Standardsortierung",
    "Search": "Suchen",
    "Search results": "Suchergebnisse",
    "Related products": "Ähnliche Produkte",
    "Proceed to Checkout": "Zur Kasse",
    "Continue shopping": "Weiter einkaufen",
    "Quantity": "Menge",
    "Remove item": "Artikel entfernen"
  };

  // "Showing 1–16 of 110 results" and its single-result variant.
  var RESULTS = [
    [/^Showing\s+(\d+)[–-](\d+)\s+of\s+(\d+)\s+results$/,
     function (m) { return "Ergebnisse " + m[1] + "–" + m[2] + " von " + m[3]; }],
    [/^Showing\s+all\s+(\d+)\s+results$/,
     function (m) { return "Alle " + m[1] + " Ergebnisse"; }],
    [/^Showing\s+the\s+single\s+result$/, function () { return "Ein Ergebnis"; }]
  ];

  var SKIP = { SCRIPT: 1, STYLE: 1, TEXTAREA: 1, INPUT: 1, NOSCRIPT: 1, CODE: 1, PRE: 1 };

  function translate(raw) {
    var s = raw.trim();
    if (!s) return null;
    if (Object.prototype.hasOwnProperty.call(MAP, s)) return MAP[s];
    for (var i = 0; i < RESULTS.length; i++) {
      var m = s.match(RESULTS[i][0]);
      if (m) return RESULTS[i][1](m);
    }
    return null;
  }

  function walk(root) {
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        // NB: the logical-AND operator appears nowhere in this file. WordPress
        // escapes it to a numeric HTML entity inside a wp:html block, which
        // breaks the script at parse time. Use sequential guards instead.
        if (!n.parentNode) return NodeFilter.FILTER_REJECT;
        if (SKIP[n.parentNode.nodeName]) return NodeFilter.FILTER_REJECT;
        if (!n.nodeValue) return NodeFilter.FILTER_REJECT;
        if (!n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var n, hits = 0;
    while ((n = w.nextNode())) {
      var out = translate(n.nodeValue);
      if (out !== null) {
        // preserve the original surrounding whitespace
        n.nodeValue = n.nodeValue.replace(n.nodeValue.trim(), out);
        hits++;
      }
    }
    // accessible names carried on attributes rather than in text
    // NOTE: `value` is deliberately excluded. On a form control it is submitted
    // data, not a label — rewriting it could change what the server receives.
    var els = root.querySelectorAll ? root.querySelectorAll("[aria-label],[placeholder],[title]") : [];
    for (var i = 0; i < els.length; i++) {
      ["aria-label", "placeholder", "title"].forEach(function (a) {
        var v = els[i].getAttribute(a);
        if (v) { var t = translate(v); if (t !== null) { els[i].setAttribute(a, t); hits++; } }
      });
    }
    return hits;
  }

  function run() { try { walk(document.body); } catch (e) { /* never break the page */ } }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }

  // WooCommerce re-renders the mini-cart and product grids after AJAX.
  try {
    var mo = new MutationObserver(function (recs) {
      for (var i = 0; i < recs.length; i++) {
        for (var j = 0; j < recs[i].addedNodes.length; j++) {
          var n = recs[i].addedNodes[j];
          if (n.nodeType === 1) { try { walk(n); } catch (e) {} }
        }
      }
    });
    mo.observe(document.documentElement, { childList: true, subtree: true });
  } catch (e) {}
})();
