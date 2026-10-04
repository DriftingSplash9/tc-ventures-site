# Copy review 013 — the third pass: spectacular

**Written:** 2026-10-03
**Why:** Thomas: "go ahead and tell me what can be spectacular, remember I need to show off some skills so
give me links to some award winning sites that use modern and "spectacular" effects." Q-SP5 stands at "5
none yet" (no award picked). The ceilings were doubled the same day ("headroom can be increased 100%"), so
weight is not what holds a piece back.
**Status:** ruled 2026-10-03 (see the end). Being built in Q-TP2's order, TP-A first.

Same format and marks as copy-review-001 to 012: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## TP-0 — the proposal (not copy)

**To rule:** TP-0 as a whole (OK / FIX), plus Q-TP1 to Q-TP4. Any new words (labels, alt text) come after,
as numbered blocks.

### 1. Where it stands (`main` at `5bffd55`)

- **The home page** has the one big moment: the 3D ledger behind the headline. It draws in, tilts to the
  pointer, and under Full the camera rises as the hero leaves. It is the only WebGL on the site.
- **Every page** has the page change (M1: the page sinks back as the new one lifts, 0.7 s), the header that
  folds onto the slab, and the pills.
- **The case studies** have the opener's settle, the picture carried from `/projects`, the drifting section
  numbers and the rail.
- **The Display panel** works on every page, and is four plain rows of radio buttons: a change happens at
  once, with nothing to see. It is the site's argument (PL-6: "it needs all the accessibility toggles"),
  and it looks like a form.
- **So:** the motion is refined and small everywhere except the hero, which a reader leaves in one screen.

### 2. The pieces, in the order recommended

**TP-A: the ledger as a journey (home). The big one.**
- The hero holds its place while the reader scrolls about two screens. The camera travels the ledger's time
  axis from 001 to the newest gate, and each gate's ruled line shows beside it as the camera passes. Threads
  light as they open and close. At the end the camera pulls up to the whole ledger and the page carries on.
- **Native scroll drives it** (a sticky hero and the scroll position), so the page scrolls at the reader's
  speed: no scroll-jacking. The scrubber stays in step (the same `lg:show` events).
- **Shows:** Three.js scene direction, scroll-linked animation and storytelling from real data.
- **Reduced and Off:** no hold and no travel, the whole ledger still, as now. The list carries every line.
  Without JavaScript: as now.
- **Rests on:** the scene that's there, and the ruled lines. No new library and no new words.

**TP-B: accessibility as the show (every page).**
- **Theme:** the new theme sweeps out from the Display button as a growing circle (a same-document view
  transition). **Contrast More** sharpens in with a wipe. **Motion** previews itself on a small live sample
  inside the panel. **Text size** grows the page, and the header re-measures as it does.
- The panel itself opens from the button as a smoked-glass sheet, like the pills.
- **Shows:** accessibility engineering presented as design, the View Transitions API, and a token-based
  colour system that can animate between themes.
- **Every effect follows the motion setting it changes:** under Reduced the sweep is a fade; under Off, at
  once. Browsers without view transitions switch as now.

**TP-C: the page change as a dissolve (every page).**
- M1 keeps its sink and lift. The new page arrives through an animated mask: a teal-edged ink bleed or
  noise dissolve, in CSS, on the cross-document view transition M1 already uses (Chrome and Edge 126+,
  Safari 18.2+).
- No script, and no delay added to the click.
- **Shows:** cross-document view transitions with animated masks.
- **Reduced:** the cross-fade, as now. **Off:** none, as now.

**TP-D: the work as particles (`/projects`).**
- Behind the six builds, a field of particles. Focus or hover a build and the particles gather into its
  picture (sampled into points: the graph, the farm, the desk, the pages); move to the next and they fly
  there. Three.js, with instanced points and a shader that moves them.
- **Shows:** GLSL shaders, GPU instancing, sampling an image into particles.
- **Decorative** (`aria-hidden`); keyboard focus does what hover does. **Reduced and Off:** no particles,
  the pictures as now. Without JavaScript or WebGL: as now.
- **Weight:** Three.js is 808 kB decoded. `/projects` measured 874.6 kB on 2026-10-03, so about 1,683 kB
  with it: under its new ceiling, 1,750. **It changes PW3** (`/work/this-site`'s range, "220 to 790 kB",
  with `/projects` the heaviest): a copy review (TH3e) when it ships.
- **It breaks a ruled rule:** "Nothing heavy loads before a click, except the home page's 3D hero." Q-TP3.

**Smaller extras, each optional (Q-TP4):**
- **TP-E, the pointer's light:** a soft teal light follows the pointer and catches the pills' metal and the
  slab (the sun and moon of the header, carried across the page). The pills lean a little toward the
  cursor. Full only, mouse and trackpad only.
- **TP-F, a kinetic headline:** the home H1's weight follows the pointer along the line. The display face's
  `@font-face` already declares weights 400 to 700 from one file, so no new font.
- **TP-G, the work moving:** short, muted loops of the Back Quarter's drive and the desk menu on their case
  studies, in place of stills. Video is heavy, and the same rule as TP-D stands in the way.

### 3. What it rests on

- **No new library and no build step.** Three.js is already vendored and pinned. No inline script.
- **Every piece follows the Display panel's motion setting,** and the words and links render without
  JavaScript (standing rules).
- **TP-A uses the ruled ledger lines.** Any new words (a panel sample's label, alt text) come as numbered
  blocks.

### 4. Checks, when built

- `site_check.py`: each piece under Full, Reduced and Off, and without JavaScript; the paint check covers
  its new states in Chromium and Chrome; `budget.py` with the doubled ceilings.
- A recording in Thomas's Chrome at every step, light and dark, and a phone.

### 5. Award winners to study

Checked 2026-10-03: each site answered 200, and each award was read on the award's own page (Awwwards' site
pages and its Sites of the Year, of the Month and Portfolio Honors listings; FWA's case data). "SOTD" is
Awwwards' Site of the Day, with its date. Not checked: CSS Design Awards (it refused the requests, 403) and
Godly.

**For TP-A, a story told by scrolling through 3D:**
- **Oryzo AI** (Lusion), https://oryzo.ai: Awwwards Site of the Month, Apr 2026, and Developer Award; SOTD
  Apr 13, 2026. One object, its story told as you scroll: the nearest model for TP-A.
- **Igloo Inc** (abeto), https://www.igloo.inc: Awwwards Site of the Year 2024 and Developer Award; SOTD
  Jul 23, 2024. Scroll-driven 3D with transitions between sections. Its page holds no text outside the
  canvas: this site's words and accessibility are where it can do better.
- **Lusion v3**, https://lusion.co: Awwwards Site of the Year 2023 and Developer Award; FWA of the Year. A
  studio portfolio built on shaders.

**For TP-B, settings that are part of the show:**
- **Bruno's Portfolio** (Bruno Simon), https://bruno-simon.com: Awwwards Site of the Month and Developer
  Award, SOTD Jan 21, 2026; FWA of the Year. You drive a car around his world, the Back Quarter's genre. His
  script carries options for sound, quality and renderer inside the world, as TP-B would treat the Display
  panel.

**For TP-C, the change of page:**
- **Dennis Snellenberg**, https://dennissnellenberg.com: SOTD Apr 4, 2022. Plain script tags and no
  framework, as here, with page transitions from a library (Barba.js). TP-C does it with the browser's own
  View Transitions; the research saw none of these fourteen sites using them.

**For TP-D, the work as WebGL:**
- **Messenger** (abeto), https://messenger.abeto.co: Awwwards Site of the Year 2025 and Developer Award; SOTD
  Nov 10, 2025. A small 3D world to walk around.
- **Robin Noguier**, https://robin-noguier.com: SOTD Oct 27, 2020. A project gallery drawn in WebGL with its
  own shaders (tagged WebGL, Three.js, GLSL).
- **Immersive Garden**, https://immersive-g.com: Awwwards Site of the Month, Jan 2025, and Developer Award;
  SOTD Jan 7, 2025. A studio's work in 3D, kept in step with smooth scrolling.

**For TP-E and TP-F, type, pointer and sound:**
- **AW Portfolio** (Antoine Wodniack), https://wodniack.dev: SOTD Dec 12, 2024, Portfolio Honors and Developer
  Award. Moving type and a 2D canvas, no WebGL at all: the model for TP-F.
- **Pacôme Pertant**, https://pacomepertant.com: SOTD Jun 9, 2026, Portfolio Honors and Developer Award.
  Small interactions everywhere, and sound (which would need its own switch in the Display panel).
- **Ponpon Mania** (Patrick Heng), https://ponpon-mania.com: Awwwards Site of the Month, Oct 2025, and
  Developer Award. One developer's interactive comic.

**Worth knowing:**
- **Lando Norris** (OFF+BRAND), https://landonorris.com: Awwwards Site of the Year 2025 and Developer Award.
  Built on Webflow with hand-added WebGL scripts: a Site of the Year doesn't need a build pipeline.
- **Jesse's Ramen** (Jesse Zhou), https://www.jesse-zhou.com: Awwwards Honorable Mention, Mar 22, 2022. The
  whole portfolio as one 3D room, the desk menu's genre.
- **Henry Heffernan's portfolio** (henryheffernan.com, the 3D computer) is live, but the research found no
  award for it, so it isn't listed.

### Questions

**Q-TP1. TP-0 as a whole.** OK / FIX.

**Q-TP2. Which pieces, in which order?**
- **A (recommended):** TP-A, then TP-B, then TP-C, then TP-D. The hero is the first thing a judge sees;
  TP-B and TP-C reach every page and cost little; TP-D is the most work.
- **B:** TP-B and TP-C first (every page, quick), then TP-A, then TP-D.
- **C:** TP-A only for now.

**Q-TP3. TP-D and the "nothing heavy before a click" rule.**
- **A (recommended):** allow Three.js on `/projects` too, loaded after the page has finished loading and
  only under Full. A reader who came from the home page has a copy already: the vendor files are served
  `max-age=0, must-revalidate`, so the browser asks again and gets a 304, not a second download.
- **B:** keep the rule; TP-D waits for a click ("Show the particles").
- **C:** no TP-D.

**Q-TP4. The extras.** TP-E, TP-F, TP-G: each yes or no. Recommended: TP-E yes, TP-F yes, TP-G no for
now (weight and the same rule as TP-D).

### Rulings, TP-0 (2026-10-03)

Thomas, verbatim: **"merge 77 and 78, LG39 yes, TP all A"**. Read as:
- **Q-TP1:** TP-0 OK as a whole.
- **Q-TP2 A:** TP-A, then TP-B, then TP-C, then TP-D, one piece per PR.
- **Q-TP3 A:** Three.js may load on `/projects` too, after the page has loaded and only under Full. The
  rule "Nothing heavy loads before a click, except the home page's 3D hero" gains `/projects`' particles.
- **Q-TP4, as recommended** (it had no A; "all A" read as the recommendation): TP-E yes, TP-F yes, TP-G no.
