# tc-ventures.ca

Hand-written static site. No framework, no build step, no CMS.

```
public/            what gets served
  index.html       home
  projects.html    the graph, the Back Quarter, the Desk, the four sites
  background.html  experience, skills, resume
  contact.html     one address, no form
  404.html         "no document, no edge" - inline SVG, CSS only
  work/_template.html  case-study template (plan-001 session 2) - local preview only, not deployed
  _headers         security headers (CSP, HSTS...) - parsed by Cloudflare, not served
  .assetsignore    files in public/ that are never uploaded (the template, og-src/)
  og-src/og.html   source for assets/img/og-card.png, the 1200x630 link preview
  favicon.svg
  robots.txt
  sitemap.xml
  assets/style.css one stylesheet - design tokens in :root, case-study components at the end
  assets/img/      screenshots
  assets/Thomas-Cheesman-Resume.pdf
briefs/            work briefs from Thomas
reviews/           copy reviews, marked up
plans/             multi-session plans (plan-001: skeleton to showcase)
handoff-NNN.md     session state - highest number is current
wrangler.jsonc     Cloudflare static-assets config
```

Edit the HTML directly and push. Cloudflare deploys on push to `main`.

JavaScript is allowed but dependencies and a build step are not. Inline small
vanilla JS that enhances HTML which already rendered. If something needs a
library, copy a prebuilt bundle into `assets/` rather than introducing npm and a
bundler into this repo.

Standing rules: `object-fit: contain` never `cover`; content renders without
JavaScript; no phone number on the site (it is in the resume download).
