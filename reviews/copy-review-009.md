# Copy review 009 — Phase 4, the engineering pass

**Written:** 2026-10-01
**Why:** Phase 4 (PL-6): headers, schema, a link-preview image per page, and the page-weight budget script
(plan-001 §4d, §4e, §5 row 8). PL-8's numbers wait for the budget script. Started at Thomas's word, "lets see
the phase 4 proposal too". Propose before building.
**Status:** P4-0, the proposal, for Thomas to rule. Nothing is built.

Same format and marks as copy-review-001 to 008: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## P4-0 — the proposal (not copy)

**To rule:** P4-0 as a whole (OK / FIX), plus Q-P4-1 to Q-P4-7. The words come after: SD1 onward for the
structured data, OG1 onward for the cards' alt text.

### 1. Where the site stands (read and measured 2026-10-01, `main` at `91e2b71`)

- **Headers:** `public/_headers` has been live since Phase 0 (handoff-015). It sets the CSP (no inline script;
  `style-src` allows inline styles), HSTS for a year, nosniff, `X-Frame-Options: DENY`, the referrer and
  permissions policies and COOP. Fonts are `immutable`.
  - Read live by curl on `/`, `style.css`, `og-card.png` and `prefs.js`: each carries the CSP and HSTS.
  - Those four answer `Cache-Control: public, max-age=0, must-revalidate` with an ETag, Cloudflare's
    default. A repeat visit asks again and gets a small "not modified". With no build step, filenames never
    change when a file does, so a longer cache would serve stale files. **No change proposed.**
  - **No checker reads the live headers.** A search of `scripts/` for the CSP, HSTS and `_headers` found
    only the local test server writing its own. A header lost in a Cloudflare change would go unnoticed.
- **Schema:** none. No page has structured data (0 of the 13 HTML files).
- **Link previews:** every page in the sitemap has its own `og:title`, `og:description` and canonical URL,
  but **one image for all of them**, `og-card.png` (1200×630, the name and a slice of the graph), with the
  same alt text. It was rendered by hand, by the command in `og-src/og.html`'s comment. `/404` has none.
- **Redirects:** `/x.html` answers 307 to `/x` (Cloudflare's own HTML handling). `/work` and `/work/` are 404:
  there is no index, ruled 2026-09-25.
- **Page weight,** measured live by a scratchpad script (Chromium, an empty cache per page, 1280 wide, before
  any click, Cloudflare's analytics beacon included; one run each, so a baseline, not a budget):

  | Page | Requests | On the wire | Of which fonts | Images |
  |---|---|---|---|---|
  | `/` | 12 | 223 KB | 169 KB | — |
  | `/projects` | 14 | 596 KB | 169 KB | 387 KB |
  | the six case studies | 11–12 | 210–217 KB | 169 KB | none before scrolling |
  | `/method`, `/background`, `/contact` | 11–12 | 208–213 KB | 169 KB | — |

  - **The fonts are most of every page,** and one file is most of the fonts: `source-serif-4-latin.woff2`,
    120 KB of the 169. The budget script will show this on every run. Changing the font files isn't part of
    this proposal.
  - Every image is `loading="lazy"`. The case studies' images sit below the first screen, so they arrive as
    the reader scrolls and aren't counted here; `/projects`' sit near the top and load at once.
  - `/404` wasn't measured.
- **Automated accessibility checks:** none run. (This is PL-8's "a11y numbers". A-1, your own pass, stays
  yours and isn't part of this.)

### 2. The pieces, in the order proposed

**P4-A — the budget script, `scripts/budget.py`.**
- For every page in the sitemap plus `/404`: a fresh browser with an empty cache, 1280 and 375 wide. It
  records what crosses the wire before any click: bytes, by type, and the number of requests. Twice: as the
  page first loads, and scrolled to the end (the lazy images).
- **The graph's payload** (after its click) is measured on its own and reported, not counted in the page.
- **A ceiling per page** (Q-P4-2), written in the script. `--live` measures tc-ventures.ca as served
  (compressed); without it, the local `public/`.
- **Automated accessibility rules** (Q-P4-3): every page in both themes.
- **Its controls:** a copy of `public/` with a heavy image added must fail the ceiling; a page with an image
  missing its alt text must fail the accessibility rules.
- It produces PL-8's numbers. They reach `/work/this-site` only through a copy review.

**P4-B — headers, redirects and the deploy script.**
- **A live header check** in `site_check.py --live`: every page and asset type served with exactly what
  `_headers` says. The control: the same check against `_headers` with one line changed must fail.
- **`public/_redirects`** (Q-P4-6): `/work` and `/work/` to `/projects`.
- **INFRA-18** (Q-P4-7): `scripts/deploy_wait.py` waits for the merge commit's check-run, then curls each
  changed page cache-busted against `main` with a pre-merge control. It replaces the ad hoc loop each merge
  has used, and carries two traps: the Cloudflare bot's "Deployment successful" on branch pushes (x = 10 at
  the next handoff) and a check warming its own cache (retired in handoff-030).

**P4-C — structured data (schema.org).**
- As plan-001 §4e: **`ProfilePage` with a `Person` on home, `CreativeWork` per case study, and a
  `BreadcrumbList`** (Home › Projects › the case study) on each case study.
- **It states only what the page already says:** name, the label's place, the site, the contact address,
  LinkedIn, and each case study's H1 and lede. No phone, no dates you haven't given, nothing familial. The
  words are copy (SD1 onward), so they go through this review.
- **The CSP question** (Q-P4-4): structured data lives in `<script type="application/ld+json">` in each
  page's `<head>`. Browsers never run it, so the CSP doesn't apply to it, but it breaks the letter of "no
  inline script".
  - **Tested 2026-10-01** in Chromium, by a scratchpad script, under the live CSP: a JSON-LD block was
    neither blocked nor reported, and its data read back. The control, an ordinary inline script beside it,
    was blocked and reported. Without the CSP the same script ran, so the CSP is what blocked it. (The
    script's first version had a harness bug that dropped the inline script from both pages; the control
    not failing is how it was caught.)
- **Checks:** each block parses as JSON, names the page's own canonical URL, and repeats only strings found
  in that page's visible text (the control is one changed string, which must fail). Chrome shows no CSP
  report. After shipping, you can run Google's Rich Results Test on one page.

**P4-D — a link-preview card per page** (Q-P4-5).
- **`og-src/og.html` becomes a template,** and `scripts/og_cards.py` renders one card per page with
  Playwright: the site's label, the page's H1 unchanged, and a picture already on that page, shown whole
  (`contain`, nothing cropped). It writes `assets/img/og/<page>.png` and each page's `og:image` and
  `og:image:alt`.
  - **The picture is the page's first image:** the graph, the Back Quarter, the desk, the GPRS home page,
    this site's home page. Two pages have no image, so they use a figure as drawn: `/method` its loop
    diagram, Bare Your Rare its schema excerpt.
- **The cards only load for link previews** (LinkedIn, Slack, iMessage), never with the page, so they add
  nothing to page weight.
- **The alt text is copy** (OG1 onward).
- **Checks:** each page's `og:image` answers 200 and is 1200×630; the card's title is the page's H1. Looked
  at: every card. After shipping, you can paste a URL into LinkedIn's Post Inspector to see the card as
  LinkedIn does.
- **Privacy:** only pictures already on the site, shown whole. Nothing new is photographed or cropped.

**Then:** PL-8's numbers into `/work/this-site` (a copy review; C-20 is on the same page). Then CSSDA and
Godly, then Awwwards (PL-6), each on your word.

### Questions

**Q-P4-1:** the order.
> **A (recommended):** A, B, C, D as above: the measuring first, so every later step is measured against
> it, and the cards last.
>
> **B:** the cards first, because they're what a CSSDA or Godly reviewer sees when the link is shared.

**Q-P4-2:** the ceilings.
> **A (recommended):** a ceiling per page, set from the baseline with some headroom, that fails the run when
> crossed (rule 5). Raising one is a ruled change, recorded in the script.
>
> **B:** report the numbers only; nothing fails.

**Q-P4-3:** the automated accessibility rules.
> **A (recommended):** axe-core, the open-source rules engine behind Lighthouse's accessibility audit, run
> by the budget script in Chromium, failing on any violation. One pinned file in `scripts/vendor/` with its
> licence, never deployed: a tool for the checks, not a dependency of the site.
>
> **B:** none now; leave all accessibility testing to A-1.

**Q-P4-4:** structured data and the "no inline script" rule.
> **A (recommended):** allow `<script type="application/ld+json">` as the one inline `<script>`, a data block
> that never runs, in `<head>`. A check fails any other inline `<script>`.
>
> **B:** no structured data.

**Q-P4-5:** which pages get their own card.
> **A (recommended):** the six case studies and `/method`. Home, Projects, Background and Contact keep the
> site card.
>
> **B:** every page in the sitemap: Home and Projects with a picture of their own, Background and Contact
> with the graph slice and their own H1.

**Q-P4-6:** `/work` and `/work/`.
> **A (recommended):** a 301 to `/projects`, where the case studies are listed. Someone who trims a case
> study's URL lands on the list instead of the 404.
>
> **B:** leave them 404.

**Q-P4-7:** INFRA-18, the deploy-and-curl script.
> **A (recommended):** build it in P4-B. If it isn't built by the next handoff, the Cloudflare trap retires
> at x = 10 instead of ending "into code".
>
> **B:** keep it separate, in INFRA.

### Rulings, P4-0 (2026-10-01)

Thomas, verbatim: **"p4-0 ok, all A"**. Read as:
- P4-0 OK as proposed.
- Q-P4-1 A: the order A, B, C, D (budget script, headers and redirects, structured data, cards).
- Q-P4-2 A: a ceiling per page that fails the run; raising one is a ruled change.
- Q-P4-3 A: axe-core, one pinned file in `scripts/vendor/` with its licence, never deployed.
- Q-P4-4 A: `<script type="application/ld+json">` is the one inline `<script>` allowed; a check fails any
  other.
- Q-P4-5 A: own cards for the six case studies and `/method`; the rest keep the site card.
- Q-P4-6 A: `/work` and `/work/` 301 to `/projects`.
- Q-P4-7 A: INFRA-18 built in P4-B.

### The steps

1. P4-0 ruled.
2. P4-A built and its controls run; the measured baseline and the proposed ceilings here, for ruling.
3. P4-B built, shipped on your word, checked live.
4. SD1 onward drafted and ruled; P4-C built, shipped, checked live.
5. OG1 onward drafted and ruled; the cards built, looked at, shipped, checked live.
6. PL-8's words, ruled; shipped.

---

## Step 2 — P4-A built (2026-10-01), for Thomas to rule

**To rule:** Q-P4-8 (the ceilings) and Q-P4-9 (the one accessibility finding).

**Built:** `scripts/budget.py`, its manual in its docstring. axe-core 4.11.4 is in `scripts/vendor/axe-core/`
(`axe.min.js` and its `LICENSE`), downloaded with Thomas's OK (2026-10-01): 564,211 and 15,921 bytes, the
same sizes jsDelivr lists, and the script's sha512 matches the one cdnjs publishes. `scripts/` is never
deployed. Nothing on the site changed.

**The controls, each run:**
- `--controls`: a heavy image planted on `/contact` and the alt text taken off `/work/gprs`'s first image.
  `/contact` failed its ceiling (475 kB against 290), `/work/gprs` failed `image-alt` in light and dark, and
  `/background`, left alone, passed. "OK, the 3 planted faults failed and nothing else did."
- The pin: a copy of the script with one byte added to its axe-core file refused to run.

**Measured, 2026-10-01, at `91e2b71`.** "Page" is the weight once scrolled to the end, the site's own files
as decoded; the ceiling applies to it. "On the wire" is what a reader downloads (compressed), from the live
run. Other origins: Cloudflare's analytics beacon, 30 kB on every page, outside the ceilings.

| Page | Page, live | On the wire | Proposed ceiling |
|---|---|---|---|
| `/` | 352 kB | 218 kB | 390 kB |
| `/projects` | 652 kB | 600 kB | 720 kB |
| `/work/influence-graph` | 605 kB | 537 kB | 670 kB |
| `/work/back-quarter` | 319 kB | 259 kB | 360 kB |
| `/work/desk-and-drawer` | 429 kB | 370 kB | 480 kB |
| `/work/bare-your-rare` | 268 kB | 206 kB | 300 kB |
| `/work/gprs` | 480 kB | 423 kB | 530 kB |
| `/work/this-site` | 357 kB | 290 kB | 400 kB |
| `/method` | 274 kB | 208 kB | 310 kB |
| `/background` | 255 kB | 203 kB | 290 kB |
| `/contact` | 255 kB | 204 kB | 290 kB |
| `/404` | 251 kB | 202 kB | 280 kB |

- **The graph,** after its click: 1,372 kB more, 365 kB on the wire. Reported, not in the page.
- **Local runs read about 2 kB more per page than live.** This checkout has Windows line endings (2,290
  carriage-return bytes across the home page's files); the repo and the site have none. The ceilings were set
  from the local numbers, so they err on the safe side.
- **The home page grows** a little with each ledger column; its headroom is 36 kB locally, 38 kB live.

**Accessibility (axe-core's WCAG 2.0 to 2.2 A and AA rules, every page, light and dark, local and live):**
one violation, on two pages. Everything else passed, colour contrast included.
- **`nested-interactive` (serious):** the loop diagram on `/method` and the one on `/work/this-site` are each
  an `<svg role="img">` that holds links. `role="img"` tells a screen reader the picture has no parts, so
  the links inside it may not be announced.
- **This is A-1's first listed point** ("the loop diagrams' links sit inside an SVG with `role="img"`"),
  found again by the check on its own.

### Questions

**Q-P4-8:** the ceilings.
> **A (recommended):** as in the table: the page's measured weight plus 10%, rounded up to the next 10 kB.
>
> **B:** another rule for the headroom (say which).

**Q-P4-9:** the `nested-interactive` finding.
> **A (recommended):** mark it a known fault under A-1, the way `site_check.py` marks one: it isn't counted
> and doesn't fail the run, the summary names it, and the day it passes the run fails until the mark comes
> off. The fix stays in your accessibility pass, where the diagrams get their screen-reader run-through.
>
> **B:** fix it now (the diagrams' markup changes, and how a screen reader meets them), in its own small
> step before P4-B.

### Rulings, step 2 (2026-10-01)

Thomas, verbatim: **"q-p4-8 a, q-p4-9 a"**. Read as:
- Q-P4-8 A: the ceilings as in the table. `CEILINGS_RULED` set in `budget.py`.
- Q-P4-9 A: `nested-interactive` on `/method` and `/work/this-site` is a known fault under A-1 (`KNOWN` in
  `budget.py`), by page and rule, so any other violation on those pages still fails.

**Built after the ruling, and checked:**
- `--controls` now plants a third fault: `/method`'s diagram fixed (`role="img"` taken off). It failed as
  "passes now: take its A-1 line off KNOWN", light and dark, with the other planted faults, and nothing else
  failed.
- **For A-1, a fact, not a fix:** with `role="img"` off `/method`'s diagram, axe found no violation on the page.
  Whether a screen reader then reads the diagram well is A-1's to find out.
- `budget.py` locally: 48 of 48, the A-1 fault named, not counted.
