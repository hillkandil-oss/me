#!/usr/bin/env python3
"""
Merchant Center readiness auditor for live WordPress/WooCommerce stores.

Runs the checks that Google's crawler can run — unauthenticated, public-surface
only — against the five Misrepresentation best practices in
MISREPRESENTATION-COMPLIANCE.md and the automatic failure conditions in the
project workflow (section 40).

Stdlib only, so it runs anywhere with Python 3.9+. Honours HTTPS_PROXY.

Usage:
    python3 audit-store.py https://example.com
    python3 audit-store.py https://example.com --json findings.json
    python3 audit-store.py https://example.com --brick-and-mortar
    python3 audit-store.py https://example.com --max-products 500

Exit status: 1 if any BLOCKER or CRITICAL finding, else 0 — so it can gate CI.

What it cannot do: anything requiring a login, a real checkout, or the Merchant
Center account itself. Those stay owner-verified. A clean run here is necessary
for submission readiness, never sufficient for approval — approval is Google's
decision alone.
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from collections import Counter
from typing import Any

TIMEOUT = 30
UA = "Mozilla/5.0 (compatible; MerchantCenterReadinessAudit/1.0)"

SEVERITIES = ["BLOCKER", "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]

# Policy pages Google expects to find, by conventional slug.
POLICY_SLUGS = {
    "privacy": ["privacy-policy", "privacy"],
    "terms": ["terms-and-conditions", "terms", "terms-of-service"],
    "returns": ["returns", "returns-refunds", "return-policy", "refund-policy"],
    "shipping": ["shipping-policy", "shipping", "delivery"],
    "contact": ["contact", "contact-us"],
    "about": ["about", "about-us"],
}

PLACEHOLDER_PATTERNS = [
    r"lorem ipsum",
    r"\bdolor sit amet\b",
    r"coming soon",
    r"under construction",
    r"\byour (?:company|business|store|brand) name\b",
    r"\[insert[^\]]{0,40}\]",
    r"\bplaceholder\b",
    r"add your (?:text|content|description) here",
    r"\bTODO\b",
    r"XXX-XXX-XXXX",
    r"123 (?:Main|Example|Fake) (?:St|Street)",
    r"\byour@email\b",
    r"example@example\.",
]

# Claims that need substantiation. Presence is not proof of violation, but each
# one needs a verifiable source, so they get surfaced for manual review.
UNSUPPORTED_CLAIM_PATTERNS = [
    r"\b(?:no\.?\s*1|number one|#1)\b",
    r"\bworld'?s (?:best|leading|largest)\b",
    r"\bbest (?:in the world|prices? (?:guaranteed|anywhere))\b",
    r"\b100% (?:authentic|guaranteed|satisfaction)\b",
    r"\baward[- ]winning\b",
    r"\bas (?:seen|featured) (?:on|in)\b",
    r"\bcertified\b",
    r"\bFDA[- ]approved\b",
    r"\bclinically proven\b",
]

FAKE_URGENCY_PATTERNS = [
    r"\bonly \d+ left\b",
    r"\bhurry[,!]? (?:only|just)\b",
    r"\d+ (?:people|others|customers) (?:are )?(?:viewing|watching|bought)",
    r"\bsale ends in\b",
    r"\bexpires in \d+",
]


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Surfaces 3xx responses instead of transparently following them."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Finding:
    __slots__ = ("severity", "category", "page", "description", "evidence", "recommendation")

    def __init__(self, severity: str, category: str, page: str,
                 description: str, evidence: str, recommendation: str):
        self.severity = severity
        self.category = category
        self.page = page
        self.description = description
        self.evidence = evidence
        self.recommendation = recommendation

    def as_dict(self) -> dict[str, str]:
        return {s: getattr(self, s) for s in self.__slots__}


class Audit:
    def __init__(self, base: str, brick_and_mortar: bool = False, max_products: int = 1000):
        self.base = base.rstrip("/")
        self.brick_and_mortar = brick_and_mortar
        self.max_products = max_products
        self.findings: list[Finding] = []
        self.notes: list[str] = []
        self._cache: dict[str, tuple[int, str, dict]] = {}

    # ---------- plumbing ----------

    def add(self, severity: str, category: str, page: str,
            description: str, evidence: str = "", recommendation: str = "") -> None:
        self.findings.append(Finding(severity, category, page, description, evidence, recommendation))

    def get(self, path: str, follow: bool = True) -> tuple[int, str, dict]:
        """Fetch a URL. Returns (status, body, headers). Status 0 means transport failure.

        follow=False reports the redirect itself rather than its destination. Needed
        for redirect assertions: urlopen follows 3xx by default, which would make a
        correctly configured 301 look like a 200 served at the original URL.
        """
        url = path if path.startswith("http") else f"{self.base}/{path.lstrip('/')}"
        key = url if follow else f"{url}#noredirect"
        if key in self._cache:
            return self._cache[key]
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        opener = (urllib.request.build_opener() if follow
                  else urllib.request.build_opener(_NoRedirect))
        try:
            with opener.open(req, timeout=TIMEOUT) as r:
                body = r.read(3_000_000).decode("utf-8", errors="replace")
                result = (r.status, body, dict(r.headers))
        except urllib.error.HTTPError as e:
            # With _NoRedirect, 3xx arrives here carrying the Location header.
            result = (e.code, "", dict(e.headers or {}))
        except (urllib.error.URLError, ssl.SSLError, TimeoutError, OSError) as e:
            result = (0, f"{type(e).__name__}: {e}", {})
        self._cache[key] = result
        return result

    def get_json(self, path: str) -> Any:
        status, body, _ = self.get(path)
        if status != 200:
            return None
        try:
            return json.loads(body)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def text_of(html: str) -> str:
        html = re.sub(r"<(script|style|noscript)\b.*?</\1>", " ", html, flags=re.S | re.I)
        return re.sub(r"<[^>]+>", " ", html)

    @staticmethod
    def jsonld(html: str) -> list[Any]:
        out = []
        for m in re.findall(
            r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
            html, re.S | re.I,
        ):
            try:
                out.append(json.loads(m.strip()))
            except ValueError:
                out.append({"__unparseable__": m[:200]})
        return out

    @staticmethod
    def walk_types(node: Any, want: str) -> list[dict]:
        """Find every dict whose @type matches `want`, at any depth."""
        found = []
        if isinstance(node, dict):
            t = node.get("@type")
            types = t if isinstance(t, list) else [t]
            if any(isinstance(x, str) and x.lower() == want.lower() for x in types):
                found.append(node)
            for v in node.values():
                found += Audit.walk_types(v, want)
        elif isinstance(node, list):
            for v in node:
                found += Audit.walk_types(v, want)
        return found

    # ---------- guideline 3: HTTPS + professional design ----------

    def check_transport(self) -> None:
        status, body, _ = self.get("/")
        if status == 0:
            self.add("BLOCKER", "availability", "/",
                     "Homepage unreachable — audit cannot proceed meaningfully.",
                     body, "Confirm DNS, hosting, and TLS certificate validity.")
            return
        if status != 200:
            self.add("BLOCKER", "availability", "/",
                     f"Homepage returned HTTP {status}.", f"status={status}",
                     "Homepage must return 200 for crawling and review.")

        if not self.base.startswith("https://"):
            self.add("BLOCKER", "https", "/",
                     "Site is not being served over HTTPS.", self.base,
                     "Install a valid TLS certificate; Merchant Center requires secure checkout.")

        # These two only mean anything on an HTTPS origin; on plain HTTP the
        # blocker above already covers it, and every URL would look "insecure".
        if not self.base.startswith("https://"):
            return

        # http -> https redirect. follow=False so a 301 reports as 301, not as
        # the 200 it lands on.
        http_url = "http://" + self.base.split("://", 1)[-1]
        st, _, hdrs = self.get(http_url, follow=False)
        loc = hdrs.get("Location", "")
        if st in (301, 308) and loc.startswith("https://"):
            self.notes.append(f"http→https redirect present ({st})")
        elif st == 200:
            self.add("HIGH", "https", "/",
                     "Plain HTTP serves content instead of redirecting to HTTPS.",
                     f"http status={st}",
                     "Force a 301 redirect from http:// to https:// site-wide.")
        elif st in (302, 307) and loc.startswith("https://"):
            self.add("LOW", "https", "/",
                     "HTTP→HTTPS redirect is temporary rather than permanent.",
                     f"status={st}", "Use a 301/308 permanent redirect.")
        elif st == 0:
            self.notes.append("http:// variant unreachable — redirect not verified")

        # Mixed content: only subresources that actually load, not anchor hrefs.
        insecure = re.findall(
            r'(?:src|srcset)=["\'](http://[^"\']+)["\']'
            r'|<link[^>]+href=["\'](http://[^"\']+)["\']', body)
        urls = [a or b for a, b in insecure]
        urls = [u for u in urls if "w3.org" not in u and "schema.org" not in u]
        if urls:
            self.add("HIGH", "https", "/",
                     f"Mixed content: {len(urls)} insecure http:// subresource(s) on the homepage.",
                     "; ".join(urls[:3]),
                     "Serve all subresources over HTTPS to avoid browser warnings.")

    # ---------- guideline 5: crawlability ----------

    def check_crawlability(self) -> None:
        status, body, _ = self.get("/robots.txt")
        if status != 200:
            self.add("MEDIUM", "crawlability", "/robots.txt",
                     "No robots.txt served.", f"status={status}",
                     "Publish robots.txt referencing the XML sitemap.")
        else:
            for line in body.splitlines():
                s = line.strip().lower()
                if s.startswith("disallow:"):
                    rule = s.split(":", 1)[1].strip()
                    if rule == "/":
                        self.add("BLOCKER", "crawlability", "/robots.txt",
                                 "robots.txt disallows the entire site.", line.strip(),
                                 "Remove the blanket Disallow: / — it prevents all crawling.")
                    elif rule.rstrip("/") in ("/product", "/shop", "/products", "/store"):
                        self.add("BLOCKER", "crawlability", "/robots.txt",
                                 "robots.txt blocks commercial/product paths.", line.strip(),
                                 "Product landing pages must be crawlable.")
            if "sitemap:" not in body.lower():
                self.add("LOW", "crawlability", "/robots.txt",
                         "robots.txt does not reference a sitemap.", "",
                         "Add a Sitemap: line.")

        for candidate in ("/wp-sitemap.xml", "/sitemap_index.xml", "/sitemap.xml"):
            if self.get(candidate)[0] == 200:
                self.notes.append(f"sitemap found at {candidate}")
                break
        else:
            self.add("HIGH", "crawlability", "/sitemap.xml",
                     "No XML sitemap found at any conventional location.", "",
                     "Publish an XML sitemap of canonical URLs.")

        _, home, _ = self.get("/")
        robots_meta = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)', home, re.I)
        if robots_meta and "noindex" in robots_meta.group(1).lower():
            self.add("BLOCKER", "crawlability", "/",
                     "Homepage carries a noindex robots meta tag.", robots_meta.group(1),
                     "Remove noindex; the store must be indexable.")

    # ---------- guideline 1: transparency ----------

    def check_policies(self) -> None:
        _, home, _ = self.get("/")
        home_lower = home.lower()
        for label, slugs in POLICY_SLUGS.items():
            hit = None
            for slug in slugs:
                if self.get(f"/{slug}/")[0] == 200:
                    hit = slug
                    break
            if not hit:
                linked = any(s in home_lower for s in slugs)
                sev = "CRITICAL" if label in ("privacy", "terms", "returns", "shipping", "contact") else "HIGH"
                self.add(sev, "policies", f"/{slugs[0]}/",
                         f"No reachable {label} page at any conventional slug.",
                         f"tried: {', '.join(slugs)}" + ("; a homepage link mentions it" if linked else ""),
                         f"Publish a {label} page on its own crawlable URL and link it from the footer.")
            else:
                if hit not in home_lower:
                    self.add("MEDIUM", "policies", f"/{hit}/",
                             f"{label.title()} page exists but is not linked from the homepage.",
                             f"/{hit}/ returns 200 but no homepage link found",
                             "Link every policy from the global footer.")
                self.check_policy_body(label, hit)

    def check_policy_body(self, label: str, slug: str) -> None:
        _, body, _ = self.get(f"/{slug}/")
        text = self.text_of(body)
        words = len(text.split())
        if words < 120:
            self.add("HIGH", "policies", f"/{slug}/",
                     f"{label.title()} page is very thin ({words} words) — reads as boilerplate.",
                     f"word count={words}",
                     "Write business-specific policy content covering the real terms.")
        for pat in PLACEHOLDER_PATTERNS:
            m = re.search(pat, text, re.I)
            if m:
                self.add("BLOCKER", "placeholder", f"/{slug}/",
                         f"Placeholder/template text left in the {label} page.",
                         f"matched: {m.group(0)!r}",
                         "Replace with real business information before submission.")
                break

    def check_business_identity(self) -> None:
        _, home, _ = self.get("/")
        text = self.text_of(home)
        has_email = bool(re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text))
        has_phone = bool(re.search(r"(?:\+\d[\d\s().-]{7,}|\(\d{3}\)\s*\d{3}[-.\s]?\d{4}|\b\d{3}[-.]\d{3}[-.]\d{4}\b)", text))
        has_postal = bool(re.search(r"\b\d{4,5}(?:-\d{4})?\b", text)) and bool(
            re.search(r"\b(?:st|street|ave|avenue|rd|road|blvd|suite|unit|way|lane|dr|drive)\b", text, re.I))

        if not has_email:
            self.add("HIGH", "identity", "/",
                     "No support email address visible on the homepage.", "",
                     "Expose a support email in the header or footer.")
        if not has_phone:
            self.add("MEDIUM", "identity", "/",
                     "No telephone number visible on the homepage.", "",
                     "Publish a support phone number, or state clearly that support is email-only.")
        if not has_postal:
            sev = "CRITICAL" if self.brick_and_mortar else "HIGH"
            self.add(sev, "identity", "/",
                     "No physical address visible on the homepage.", "",
                     "Show the business address in the footer. Required for a brick-and-mortar store.")

        for pat in PLACEHOLDER_PATTERNS:
            m = re.search(pat, text, re.I)
            if m:
                self.add("BLOCKER", "placeholder", "/",
                         "Placeholder/template text on the homepage.",
                         f"matched: {m.group(0)!r}",
                         "Remove all placeholder content — 'appears unfinished' is a failure condition.")
                break

        for pat in FAKE_URGENCY_PATTERNS:
            m = re.search(pat, text, re.I)
            if m:
                self.add("HIGH", "misrepresentation", "/",
                         "Possible artificial scarcity/urgency messaging.",
                         f"matched: {m.group(0)!r}",
                         "Remove unless the claim is literally true and verifiable.")
                break

        claims = []
        for pat in UNSUPPORTED_CLAIM_PATTERNS:
            m = re.search(pat, text, re.I)
            if m:
                claims.append(m.group(0))
        if claims:
            self.add("MEDIUM", "misrepresentation", "/",
                     "Superlative or certification claims that need substantiation.",
                     "; ".join(sorted(set(claims))[:5]),
                     "Keep only claims you can evidence on request; delete the rest.")

    # ---------- guideline 2: reputation, honestly ----------

    def check_reputation_honesty(self) -> None:
        """The bullet-2 trap: ratings in markup with nothing real behind them."""
        _, home, _ = self.get("/")
        for block in self.jsonld(home):
            for agg in self.walk_types(block, "AggregateRating"):
                count = agg.get("reviewCount") or agg.get("ratingCount") or 0
                try:
                    count = int(str(count))
                except ValueError:
                    count = 0
                if count == 0:
                    self.add("CRITICAL", "misrepresentation", "/",
                             "AggregateRating in structured data with no review count behind it.",
                             json.dumps(agg)[:200],
                             "Remove the markup. Fabricated ratings are a Misrepresentation "
                             "violation — shipping with no reviews is compliant, faking them is not.")

        text = self.text_of(home).lower()
        for phrase in ("as seen on", "as featured in", "award winning", "award-winning"):
            if phrase in text:
                self.add("MEDIUM", "misrepresentation", "/",
                         f"Reputation claim {phrase!r} present — needs a verifiable source.",
                         phrase,
                         "Link to the actual feature/award, or remove the claim.")

    # ---------- brick-and-mortar ----------

    def check_local_business(self) -> None:
        if not self.brick_and_mortar:
            return
        _, home, _ = self.get("/")
        blocks = self.jsonld(home)
        local = []
        for b in blocks:
            for t in ("LocalBusiness", "Store", "JewelryStore", "ClothingStore",
                      "HomeGoodsStore", "ElectronicsStore", "FurnitureStore"):
                local += self.walk_types(b, t)
        if not local:
            self.add("HIGH", "brick-and-mortar", "/",
                     "No LocalBusiness/Store structured data — only Organization at best.",
                     "",
                     "Emit LocalBusiness (or a specific subtype) with address, geo, "
                     "telephone, openingHoursSpecification, and sameAs → Google Business Profile.")
            return
        entity = local[0]
        if not entity.get("openingHoursSpecification"):
            self.add("HIGH", "brick-and-mortar", "/",
                     "LocalBusiness schema omits openingHoursSpecification.",
                     json.dumps({k: entity.get(k) for k in ("@type", "name")}),
                     "Add structured opening hours; a physical store with no hours reads as abandoned.")
        if not entity.get("address"):
            self.add("CRITICAL", "brick-and-mortar", "/",
                     "LocalBusiness schema omits a postal address.", "",
                     "Add a full PostalAddress matching the site, GBP, and Merchant Center exactly.")
        text = self.text_of(home).lower()
        if not any(d in text for d in ("monday", "mon ", "mon–", "mon-", "hours")):
            self.add("HIGH", "brick-and-mortar", "/",
                     "No opening hours visible to customers on the homepage.", "",
                     "Publish human-readable hours in the footer or header.")

    # ---------- product data ----------

    def check_products(self) -> None:
        products: list[dict] = []
        page = 1
        while len(products) < self.max_products:
            batch = self.get_json(f"/wp-json/wc/store/v1/products?per_page=100&page={page}")
            if not isinstance(batch, list) or not batch:
                break
            products += batch
            if len(batch) < 100:
                break
            page += 1

        if not products:
            self.add("INFO", "products", "/wp-json/wc/store/v1/products",
                     "No products readable from the public WooCommerce Store API.",
                     "",
                     "If the catalogue is not yet published this is expected; otherwise confirm "
                     "products are published and the Store API is reachable.")
            return

        self.notes.append(f"audited {len(products)} public products")
        n = len(products)

        def flag(pred, severity, category, desc, rec, sample=lambda p: p.get("name", "")):
            hits = [p for p in products if pred(p)]
            if hits:
                ev = f"{len(hits)}/{n}; e.g. " + "; ".join(str(sample(p))[:60] for p in hits[:3])
                self.add(severity, category, "/product/*", desc.format(k=len(hits), n=n), ev, rec)

        flag(lambda p: not p.get("images"), "BLOCKER", "products",
             "{k} of {n} products have no image.",
             "Every product needs a real image; broken/missing images are a failure condition.")
        flag(lambda p: p.get("images") and "woocommerce-placeholder" in p["images"][0].get("src", ""),
             "BLOCKER", "products", "{k} of {n} products use the WooCommerce placeholder image.",
             "Replace placeholders with genuine product photography.")
        flag(lambda p: not (p.get("prices", {}) or {}).get("price") or
             _as_int((p.get("prices", {}) or {}).get("price")) <= 0,
             "BLOCKER", "products", "{k} of {n} products have a missing or zero price.",
             "Every product must carry a real, positive price matching the feed.")
        flag(lambda p: not p.get("is_purchasable"), "BLOCKER", "products",
             "{k} of {n} products are not purchasable.",
             "Products that cannot be bought are an automatic failure condition.")
        flag(lambda p: p.get("is_password_protected"), "BLOCKER", "products",
             "{k} of {n} products are password protected.",
             "Feed landing pages must be publicly accessible.")
        flag(lambda p: not p.get("is_in_stock"), "HIGH", "products",
             "{k} of {n} products are out of stock.",
             "Out-of-stock items must report availability honestly in the feed, or be excluded.")
        flag(lambda p: not p.get("brands"), "HIGH", "products",
             "{k} of {n} products have no brand assigned.",
             "Set a real brand, or use the correct no-brand handling — never invent one.")
        flag(lambda p: len(re.sub(r"<[^>]+>", "", p.get("description") or "").strip()) < 50,
             "HIGH", "products", "{k} of {n} products have a missing or very thin description.",
             "Write original, factual descriptions.")

        currencies = {(p.get("prices", {}) or {}).get("currency_code") for p in products}
        currencies.discard(None)
        if len(currencies) > 1:
            self.add("BLOCKER", "products", "/product/*",
                     "Multiple currencies across the catalogue.", str(sorted(currencies)),
                     "Currency must be consistent and match the Merchant Center target country.")

        promo = re.compile(r"\b(?:sale|free ship\w*|best price|cheap|clearance|hot deal|\d+% ?off|!!)\b", re.I)
        flag(lambda p: bool(promo.search(p.get("name") or "")), "HIGH", "products",
             "{k} of {n} product titles contain promotional text.",
             "Merchant Center disallows promotional text in the title attribute.")
        flag(lambda p: (p.get("name") or "").strip() and (p["name"] == p["name"].upper()) and len(p["name"]) > 10,
             "MEDIUM", "products", "{k} of {n} product titles are entirely capitalised.",
             "Use normal capitalisation; all-caps titles get flagged.")

        dupe_titles = [t for t, c in Counter(p.get("name") for p in products).items() if c > 1 and t]
        if dupe_titles:
            self.add("MEDIUM", "products", "/product/*",
                     f"{len(dupe_titles)} product title(s) are shared by more than one product.",
                     "; ".join(str(t)[:50] for t in dupe_titles[:3]),
                     "Distinguish titles (model, reference, size) so distinct items are distinguishable.")
        skus = [(p.get("sku") or "").strip() for p in products if (p.get("sku") or "").strip()]
        dupe_skus = [s for s, c in Counter(skus).items() if c > 1]
        if dupe_skus:
            self.add("HIGH", "products", "/product/*",
                     f"{len(dupe_skus)} duplicate SKU(s).", "; ".join(dupe_skus[:5]),
                     "SKUs feeding the feed id attribute must be unique.")

        self.check_product_page(products[0])

    def check_product_page(self, product: dict) -> None:
        link = product.get("permalink")
        if not link:
            return
        status, html, _ = self.get(link)
        if status != 200:
            self.add("BLOCKER", "products", link,
                     f"Sample product page returned HTTP {status}.", f"status={status}",
                     "Feed landing pages must return 200 to Google's crawler.")
            return

        blocks = self.jsonld(html)
        prods = [x for b in blocks for x in self.walk_types(b, "Product")]
        if not prods:
            self.add("HIGH", "structured-data", link,
                     "No Product structured data on the product page.", "",
                     "Emit Product schema matching the visible price, availability, and condition.")
            return
        if len(prods) > 1:
            self.add("MEDIUM", "structured-data", link,
                     f"{len(prods)} competing Product entities on one page.", "",
                     "Emit exactly one Product entity; duplicates let Google pick the wrong one.")

        entity = prods[0]
        offers = entity.get("offers")
        offers = offers[0] if isinstance(offers, list) and offers else offers
        offers = offers if isinstance(offers, dict) else {}

        if not entity.get("itemCondition") and not offers.get("itemCondition"):
            self.add("HIGH", "structured-data", link,
                     "Product schema declares no itemCondition.", "",
                     "Declare itemCondition explicitly. Omitting it while the feed says "
                     "'used' or 'refurbished' is a feed↔page mismatch.")
        if not offers.get("availability"):
            self.add("HIGH", "structured-data", link,
                     "Offer omits availability.", "",
                     "Declare availability; it must match both the page and the feed.")

        schema_price = str(offers.get("price") or "").strip()
        api_price = (product.get("prices", {}) or {}).get("price")
        if schema_price and api_price is not None:
            try:
                minor = (product.get("prices", {}) or {}).get("currency_minor_unit", 2)
                api_major = int(api_price) / (10 ** int(minor))
                if abs(float(schema_price) - api_major) > 0.01:
                    self.add("CRITICAL", "structured-data", link,
                             "Structured-data price disagrees with the store's own price.",
                             f"schema={schema_price} store={api_major:.2f}",
                             "Price must match across page, markup, and feed.")
            except (ValueError, TypeError, ZeroDivisionError):
                pass

        if not re.search(r'<link[^>]+rel=["\']canonical["\']', html, re.I):
            self.add("MEDIUM", "seo", link, "Product page has no canonical link.", "",
                     "Add a self-referencing canonical.")
        if not self.walk_types(blocks, "BreadcrumbList"):
            self.add("LOW", "structured-data", link, "No BreadcrumbList structured data.", "",
                     "Add breadcrumb markup.")

    def check_commerce_paths(self) -> None:
        for slug, label in (("cart", "Cart"), ("my-account", "Account")):
            st = self.get(f"/{slug}/")[0]
            if st not in (200, 301, 302):
                self.add("HIGH", "checkout", f"/{slug}/",
                         f"{label} page returned HTTP {st}.", f"status={st}",
                         f"{label} must be reachable.")
        st = self.get("/checkout/")[0]
        if st not in (200, 302, 301):
            self.add("BLOCKER", "checkout", "/checkout/",
                     f"Checkout returned HTTP {st}.", f"status={st}",
                     "Checkout must work; an uncompletable checkout is an automatic failure.")
        else:
            self.notes.append(
                f"checkout returned {st} (a redirect on an empty cart is normal) — "
                "a real test order still needs manual verification")

    # ---------- run ----------

    def run(self) -> None:
        self.check_transport()
        if any(f.severity == "BLOCKER" and f.category == "availability" for f in self.findings):
            return
        self.check_crawlability()
        self.check_business_identity()
        self.check_policies()
        self.check_reputation_honesty()
        self.check_local_business()
        self.check_commerce_paths()
        self.check_products()

    def report(self) -> int:
        order = {s: i for i, s in enumerate(SEVERITIES)}
        self.findings.sort(key=lambda f: (order.get(f.severity, 99), f.category))
        counts = Counter(f.severity for f in self.findings)

        print(f"\nMerchant Center readiness audit — {self.base}")
        print(f"mode: {'brick-and-mortar' if self.brick_and_mortar else 'online-only'}")
        print("=" * 78)
        for note in self.notes:
            print(f"  note: {note}")
        print()
        if not self.findings:
            print("  No findings from public-surface checks.")
        for f in self.findings:
            print(f"[{f.severity:8}] {f.category:18} {f.page}")
            print(f"           {f.description}")
            if f.evidence:
                print(f"           evidence: {f.evidence}")
            if f.recommendation:
                print(f"           fix: {f.recommendation}")
            print()

        print("=" * 78)
        print("  " + "  ".join(f"{s}={counts.get(s, 0)}" for s in SEVERITIES if counts.get(s)))
        blocking = counts.get("BLOCKER", 0) + counts.get("CRITICAL", 0)
        if blocking:
            print(f"\n  NOT READY — {blocking} blocking finding(s) must clear before submission.")
        else:
            print("\n  No blocking findings from public checks.")
        print("""
  Still owner-verified, and not covered above: a completed real test order,
  transactional email delivery, Merchant Center business-information parity,
  shipping/return settings matching the published policies, Google Business
  Profile verification, and feed-vs-page parity across the full catalogue.

  A clean run here is necessary for submission readiness, never sufficient.
  Approval is Google's decision alone.""")
        return 1 if blocking else 0


def _as_int(v: Any) -> int:
    try:
        return int(v)
    except (ValueError, TypeError):
        return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Merchant Center readiness auditor for WooCommerce stores.")
    ap.add_argument("url", help="Base URL, e.g. https://example.com")
    ap.add_argument("--json", metavar="FILE", help="Also write findings as JSON")
    ap.add_argument("--brick-and-mortar", action="store_true",
                    help="Enable physical-store checks (LocalBusiness schema, hours, address)")
    ap.add_argument("--max-products", type=int, default=1000)
    args = ap.parse_args()

    url = args.url if "://" in args.url else "https://" + args.url
    audit = Audit(url, brick_and_mortar=args.brick_and_mortar, max_products=args.max_products)
    audit.run()
    code = audit.report()

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"site": url,
                       "brick_and_mortar": args.brick_and_mortar,
                       "notes": audit.notes,
                       "findings": [f.as_dict() for f in audit.findings]}, fh, indent=2)
        print(f"\n  JSON written to {args.json}")
    return code


if __name__ == "__main__":
    sys.exit(main())
