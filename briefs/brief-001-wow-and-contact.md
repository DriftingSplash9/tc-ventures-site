# Brief 001 — Portfolio "wow factor" + the contact page

**For:** a fresh agent picking up tc-ventures.ca
**From:** Thomas Cheesman (owner, and the person whose judgement decides what ships)
**Repo:** `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site`
**Read first:** `handoff-001.md` at repo root. It carries current state, what is
already built, what is live, and the open decisions. Do not start from this brief
alone.

---

## The ask, in Thomas's words

> "Being a bit of a portfolio it should be unique, detailed, complex, and push the
> limits of what is modern with AI-assisted web design. It needs a 'wow' factor.
> Also, the contact page is not done and will get some special attention because
> contact pages always seem like a lame afterthought and they are generic."

---

## What the site is for

tc-ventures.ca is the **hiring-facing** front. The reader is a hiring manager or a
recruiter deciding whether Thomas is worth a conversation. It is deliberately
separate from thomascheesman.ca, which is the personal/family site and is already
a maximalist "desk" experience.

So the wow has a job: it must make a hiring manager think *"this person can build
things I cannot"* within about ten seconds, and then let them read. Wow that
delays, obscures, or annoys is worse than no wow.

## Where the wow should come from

**Not** from stock effects. No particle fields, no cursor trails, no scroll-jacked
parallax, no gradient mesh blobs, no "AI-generated agency site" tropes. Those are
free, everyone has them, and they signal the opposite of craft.

The wow should come from **Thomas's own material**, which is unusually good:

- **The Economic Report Influence Graph** — 3,632 real published reports, 3,272
  documented dependencies, drawn in 3D in a browser. A built copy of it already
  exists at `assets/report-graph/` in the *other* repo (the thomascheesman.ca
  theme) and is served there at `/reports-graph`. Getting a version of that graph
  onto this site — live, interactive, not a screenshot — is the single strongest
  available move. Consider a reduced, fast-loading "hero" subgraph rather than the
  full 3,600-node corpus.
- **Rocket Lander** — a real aerodynamic flight model. Terminal 61 m/s belly-down,
  190+ nose-first, glide ratio 0.26 at 25° off broadside, flip committed by 300 m.
  Those numbers can drive something on the page rather than being listed as text.
- **The evidence discipline** — every edge in the graph carries an A/B/C grade for
  how well its citation supports it. A portfolio that visibly grades its own claims
  is a genuinely unusual idea and is true to how he works.

Pick one thing and execute it to an unreasonable standard. One extraordinary moment
beats five decent ones.

## Constraints — these are not negotiable

1. **Content renders without JavaScript.** The wow may be JS; the words may not be.
   A recruiter with a locked-down browser must still read everything.
2. **Fast on a phone on mobile data.** Budget: meaningful content painted in under
   2 seconds on a mid-range Android over 4G. Heavy assets load after, or on
   interaction, or not on small screens at all.
3. **Accessible.** Keyboard-navigable, real focus states, `prefers-reduced-motion`
   respected properly (not just "animations off" — the page must still make sense).
   Thomas maintains an accessibility-first nonprofit site; a portfolio that fails
   here embarrasses the claim.
4. **No object-fit: cover anywhere.** Always `contain`. This is a standing rule
   across all of Thomas's repos.
5. **It must still be his.** The current site is deliberately calm — paper white,
   one deep-teal accent, Familjen Grotesk / Source Serif 4 / IBM Plex Mono. You may
   argue for changing that. You may not change it silently.

## Open architectural question — decide it explicitly and say why

The site is currently hand-written HTML with no build step, deployed to Cloudflare
Workers static assets. That was the right call for four static pages. A live 3D
graph may justify a bundler, or may not (the graph is already built elsewhere and
could be embedded as a prebuilt asset).

Do not quietly introduce a toolchain. If you want one, say what it buys, what it
costs in maintenance, and let Thomas decide.

---

## The contact page — the part he actually cares about

His complaint is correct: contact pages are the most neglected page on almost every
portfolio. Usually a form nobody trusts, an email address, and three social icons.

The page has one job: **make a hiring manager who is 80% convinced actually reach
out.** That is a psychological problem, not a layout problem. Things worth thinking
about, none of them mandatory:

- What does the person hesitating actually need to know? (Is he available? Will he
  reply? What happens after I send this? Is he going to be weird about the gap in
  his résumé? Can he do the hours I need?)
- Contact pages are silent about **what happens next**. "I reply within a day, from
  a real address, and I'll tell you straight if it isn't a fit" is worth more than
  any form styling.
- Different readers want different first moves — some want email, some want to see
  code, some want a call, some want to send a job description and be told honestly
  whether it fits.
- A form that posts nowhere is a lie. Either wire it up properly (Cloudflare Workers
  can accept a POST — that is a real option on this stack) or don't have one.
- Thomas is in **Grande Prairie, Alberta (Mountain Time)** and works remote. Time
  zones are a real hesitation for remote hires and almost no contact page addresses
  it.
- Do NOT put his phone number on the page. It's in the résumé download. Public
  phone numbers collect spam.

The bar: someone should read this page and feel *more* likely to write, not merely
*able* to.

---

## How to work with Thomas

- He is not a trained programmer. He spent 17 years running kitchens. Explain the
  *why* behind architectural decisions at a medium register — don't over-explain
  git or CLI basics, don't assume framework vocabulary.
- He has hand and arm pain. Give complete, uncut code and complete file contents.
  Never "…rest unchanged". Never make him retype things.
- He wants honest assessment and will correct you firmly if you are wrong. When he
  does, acknowledge it and move on — no defensiveness, no grovelling.
- Do not remind him to commit. Committing is his own routine.
- Propose before building anything large. He will say "let's try it" more often than
  not, but he wants to be asked.

## What to deliver

1. A written direction for the wow moment — what it is, why it, what it costs,
   before you build it.
2. The contact page, built.
3. An updated `handoff-002.md` following the structure defined in `handoff-001.md`.
