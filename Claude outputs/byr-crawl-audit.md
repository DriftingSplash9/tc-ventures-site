# bareyourrare.org — crawl and AI-readability audit

**Date:** 2026-09-20
**Scope:** whether search engines and AI systems can reach, read and correctly interpret the site.
**Method:** fetched every URL in the sitemap as raw HTML (pre-JavaScript, which is what a crawler sees), parsed head tags, headings, structured data and links; compared against fetches by an automated agent from outside the browser.

**Verdict:** the markup is in better shape than most sites this size — genuinely good structured data, clean canonicals, real content in the served HTML, and an `llms.txt` most sites don't have. There is one serious problem, and it is at the server, not in the pages.

---

## 1. Critical — the host blocks automated fetchers

An automated agent fetching `https://bareyourrare.org/robots.txt` from outside a browser gets a **connect timeout**. Not a 403, not a 404 — no answer at all.

Evidence:

| Site | Host | Automated fetch |
|---|---|---|
| bareyourrare.org | Hostinger | **timeout** |
| gpresidentialsociety.com | Hostinger | **timeout** |
| tc-ventures.ca | Cloudflare | 200, read fine |

Both Hostinger-hosted sites fail identically; the Cloudflare-hosted one works. This matches the note already carried in the tc-ventures handoffs, that Hostinger 403s scripted requests which succeed from a browser. It is server-level bot filtering, not anything in your HTML.

**Why it matters more than it looks.** There are two ways an AI reaches your site:

1. *Training and index crawls* (GPTBot, ClaudeBot, PerplexityBot, Google-Extended). These are well-known crawlers from published IP ranges; hosts usually let them through.
2. *Live retrieval* — a person asks ChatGPT or Claude about Hajdu-Cheney and the assistant fetches your page right then, on their behalf. That is the path that matters for a newly diagnosed patient, and it is exactly the path that just failed in testing.

Your `robots.txt` welcomes everyone. The server is overriding that decision without telling you.

**What to do:**

- Ask Hostinger support directly what bot protection is active on the account and whether it can be disabled or relaxed for known crawler user-agents. Name the symptom: connect timeouts to `/robots.txt` from non-browser clients.
- Check the server access logs for `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `Bingbot`, `Googlebot`. If the AI crawlers are absent while Googlebot appears, they are being filtered.
- If Hostinger won't or can't fix it, put the site behind Cloudflare the way tc-ventures.ca is. Free tier, DNS-only change, no migration. This is the reliable fix and you have already done it once.

Googlebot itself is clearly getting through — see §2 — so this is not an emergency for search. It is an emergency for the AI-assistant path you specifically designed the site for.

---

## 2. Search engines: indexed and ranking

Searching for the condition plus the site returns your own pages, sitting in the same result set as NORD, NIH/GARD and Cincinnati Children's. `/hcs-guide/`, `/ecd/`, `/about/` and the homepage all surface. So Googlebot crawls, renders and indexes you.

Supporting signals, all correct:

- Every page returns 200, every page self-canonicals, nothing carries `noindex`.
- `robots.txt` is the WordPress default — blocks only `/wp-admin/`, permits everything else, declares the sitemap.
- `sitemap_index.xml` → `page-sitemap.xml` (14 URLs, all live) + `category-sitemap.xml`.
- Content is in the served HTML. The five condition guides run 2,500–5,000 words of real text before any JavaScript runs. Crawlers do not have to execute anything to read you.
- Titles are descriptive and condition-first. Meta descriptions present and sensible on 12 of 14 pages.
- One `h1` per page, sensible `h2` structure (14–23 on the guides).
- Every guide carries a visible "Last reviewed: April 2026" and links out to primary sources — PubMed, MedlinePlus, Orphanet, OMIM, NORD, journal DOIs. For medical content this is the single most valuable thing on the page and you already do it.

---

## 3. AI readability: strong, with fixable gaps

**`/llms.txt` exists** (7.6 KB) and is well-written — a summary paragraph that states who runs the site and why, then an annotated list of every page. Most sites have nothing here.

**Structured data is good.** Each condition guide carries a `MedicalCondition` with `alternateName`, an ICD-10 `MedicalCode`, `cause`, `epidemiology` and a `signOrSymptom` list. The personal story carries a proper `Article` with `author`, `datePublished` and `dateModified`. The FAQ carries `FAQPage`. That is exactly the vocabulary an AI uses to decide what a page is about.

### Gaps, in order of value

**a) The guides have no authorship or review date in structured data.** "Last reviewed: April 2026" is visible to a human but invisible to a parser — the guide pages carry only `BreadcrumbList`, `NGO` and `MedicalCondition`. For health content, recency and who-wrote-this are the two things both Google's quality systems and AI models weigh hardest. Add a `MedicalWebPage` to each guide with `lastReviewed`, `author` (you, as a person, with your lived-experience credential stated) and `about` pointing at the existing `MedicalCondition`. This is the highest-value change on the list.

**b) Duplicate `BreadcrumbList`.** Every guide emits it twice — once from the theme, once from the SEO plugin. Harmless but it will throw warnings in validators, and duplicate `@id` values are the kind of thing that makes a parser discard the block. Remove one source.

**c) "POEMS" means two things on your site.** `/poems/` is POEMS syndrome. `/category/poems/` is poetry. Both are indexable, and the category page has an **empty `h1`** and only 384 words. A search engine or an AI trying to answer a question about POEMS syndrome has to guess which one you meant, and the thin one dilutes the good one. Either noindex the poetry category, or rename its slug — `/category/poetry/` costs you nothing and removes the collision entirely.

**d) Missing meta descriptions.** `/privacy/` has none; `/terms/` has 67 characters. Low stakes, two minutes.

**e) One image without alt text on nearly every page** — `handshcshero.png`, class `byr-hero-fallback-img`. If it's decorative, give it `alt=""` explicitly so it's declared decorative rather than merely unlabelled. If it carries meaning, describe it. On a site with an accessibility page, this one is worth closing.

**f) `llms.txt` is undiscoverable.** Nothing points to it. Add `<link rel="alternate" type="text/markdown" href="/llms.txt">` to the head and a comment line in `robots.txt`. Neither is a standard yet; both cost nothing.

**g) Page weight.** 123–253 KB of HTML per page before assets, and the POEMS page carries 19 images. Not a crawling problem, but it is a problem for a patient on rural Alberta mobile data — which is your actual reader.

---

## 4. Suggested order

1. Find out what Hostinger is blocking, and move to Cloudflare if the answer is unsatisfying. Nothing else on this list matters as much.
2. Add `MedicalWebPage` with `lastReviewed` and `author` to the five guides.
3. Fix the POEMS collision.
4. Sweep the small ones: duplicate breadcrumbs, two meta descriptions, the hero image alt, the `llms.txt` link.
5. Read the access logs monthly for AI crawler user-agents. That is the only way you will know whether §1 is actually fixed.

---

## 5. What is already right, and worth not breaking

Plain-language content in the served HTML. One clear topic per URL. Real citations to primary sources. Visible review dates. Correct `MedicalCondition` markup with ICD-10 codes. A hand-written `llms.txt`. Clean canonicals and a complete sitemap. Cross-linking between the guide and the personal story for the same condition.

Whoever told you a patient site can't be technically credible was wrong. The markup here is the argument.
