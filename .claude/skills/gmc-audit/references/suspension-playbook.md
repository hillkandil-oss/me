# Suspension & reinstatement playbook

How Merchant Center enforcement actually works, so you audit and advise without
burning the merchant's limited review attempts.

## Disapproval vs. suspension (don't confuse them)

- **Item disapproval** = specific products rejected; the account still serves the
  approved ones. Fix the flagged items and they re-review automatically.
- **Account suspension** = the whole account stops serving (all Shopping ads and
  free listings). This is the serious one and the focus of this skill.

## The AI-led review (April 2026 onward)

When you request review, Googlebot fetches your pages, a language model reads the
crawler's **rendered** view, summarizes it, and that summary drives the
reinstatement decision. Implications for the audit:

- Judge the **public, rendered** site — not CMS drafts or logged-in views. If a
  policy page isn't published, or renders a placeholder, the model sees that.
- The model reads for coherence: does the business identity, contact info, and
  policy set hang together and look like a real, trustworthy merchant? Internal
  contradictions (free-shipping banner vs. checkout fee; two different return
  windows) are exactly what it catches.
- Fix the *substance*, not keywords. There's no phrase that placates a reviewer
  reading a genuinely incomplete store.

## Review attempts are scarce — don't waste them

- After a misrepresentation suspension you typically get about **three** review
  attempts. Each "Request review" clicked without real fixes burns one. After
  they're gone, the option usually disappears and reinstatement gets much harder.
- Therefore: **only request review once the audit is fully clean.** Run the
  pre-submission checklist and resolve every P0/P1 first. A review request is a
  claim that the problems are fixed — treat it that way.
- Reviews commonly take up to ~7 business days; complex/luxury cases longer.

## Filing a reinstatement (if already suspended)

1. Run the full audit; fix every finding on the live, public site.
2. Wait for the fixes to be crawlable (published, cache cleared, sitemap fresh).
3. Document what you changed (for your own records and any appeal notes).
4. Then request review once. Don't re-submit repeatedly hoping for a different
   result — that just burns attempts.
5. If attempts are exhausted, options narrow to Google support escalation or,
   in some cases, a new compliant account/domain — but a new account that repeats
   the same violations gets suspended again, so fix the root cause first.

## Account & structure hygiene

- Submit only on the **verified, claimed store domain** — never a preview,
  staging, myshopify-style default, or builder subdomain you haven't claimed.
- Verify and claim the website URL in Merchant Center; keep the business info in
  Merchant Center consistent with the site.
- Don't operate multiple accounts to evade a suspension — cross-account
  association can extend enforcement.

## What to tell the merchant (expectation-setting)

- You can maximize approval odds; **you cannot guarantee approval.** Google's
  review is discretionary and, for high-risk categories, conservative.
- The goal of the audit is to make the store *genuinely* trustworthy and
  policy-complete, because that's what the review actually rewards — not to find
  a trick.
