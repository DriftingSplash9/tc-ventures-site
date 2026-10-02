# Copy review 010 — the ledger hero

**Written:** 2026-10-02
**Why:** PL-6 names Awwwards. Thomas, 2026-10-02: "I do not intend to submit it unless it is spectacular. so
far it feels plain." The agent's read, from the live site in the app's browser pane: the first screen is a
well-set page of text, and the one idea no other portfolio has, the build ledger, sits under the hero as
faint lines. This proposal makes the ledger the home page's first screen, as a 3D scene.
**Status:** H-0, the proposal, for Thomas to rule. Nothing is built.

Same format and marks as copy-review-001 to 009: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## Rulings before the proposal (2026-10-02)

The agent asked whether the home hero may (1) load a WebGL scene or a library at page load, and (2) use a
library such as Three.js. It recommended both, for the home hero, under a page-weight ceiling he rules, and
keeping "content renders without JavaScript".

Thomas, verbatim: **"both ok, write the proposal"**. Read as:
- **"Nothing heavy loads before a click" no longer binds the home hero.** It may load its scene and a library
  as the page loads. Everywhere else the rule stands (the graph on `/work/influence-graph` stays behind its
  click).
- **"No dependencies" is lifted:** a library may be used, as a pinned, vendored file served from `/assets/`
  (the way `3d-force-graph.min.js` already is). Still no build step.
- **Kept:** content renders without JavaScript. The words, the links and the ledger's list are in the HTML.
- **Kept:** the home page has a ceiling in `budget.py`. Its new number is ruled after the scene is measured
  (Q-H5).

These replace the two lines in handoff-033 §3 ("Standing rules", "Demo and embed rules") from the next
handoff on.

---

## H-0 — the proposal (not copy)

**To rule:** H-0 as a whole (OK / FIX), plus Q-H1 to Q-H5. Any new words (the ledger's caption, a hover
label) come later, as numbered blocks.

### 1. Where the hero stands (read 2026-10-02, `main` at `23e1da1`)

- **The first screen** (the pane at about 800px wide, dark): the label, the H1, the lede, R5 and the two
  buttons. The ledger starts below the fold.
- **The ledger** is two SVGs written by `export-ledger.py`, landscape and portrait. A count of `lg__t`
  elements gives 304 across the two, so about 150 threads a picture. Seven item bands, then the TRAPS band
  from `ledger/traps.json` (55 traps, 12 still carried). One column per ruled handoff.
- **Its motion:** `ledger.js` (5.4 kB) runs the scrubber and M2's draw-in, 0.11s a handoff, once 35% of the
  ledger is in view.
- **Weight:** home is 360 of its 390 kB ceiling (`budget.py --live`, 2026-10-02). Most of every page is the
  fonts.

### 2. The scene

**The ledger becomes a landscape of light behind the headline.**
- **Time runs into depth.** Handoff 001 is far away; the newest is nearest the viewer. Each handoff is a
  thin gate across the floor, carrying its number.
- **The bands are lanes,** side by side across the floor (PLAN, COPY, DESIGN, PROJECTS, A11Y, INFRA,
  DOMAIN). Each item is a filament in its lane, from the gate where it opened to the gate where it closed:
  - **carried:** it runs to the front edge and glows teal;
  - **closed:** it stops with a square cap at its gate;
  - **parked:** dotted, as now.
- **The traps are a second layer under a translucent floor.** You glimpse them through it. Each trap is a
  thread from its start; into code ends in a square, retired in a bar, and an open point where it helped, the
  same marks as the TRAPS band.
- **The headline stays HTML,** over the left of the scene, on a soft scrim, so it reads at once and the
  label, H1, lede, R5 and buttons are unchanged.

**What it does:**
- **On load (Motion Full):** the camera starts high over 001. The ledger builds itself gate by gate toward the
  viewer, the M2 draw-in as the opening, about three seconds. The camera settles low at the newest handoff,
  looking back down every session.
- **The scrubber stays,** the same native slider and label LS1, under the headline. Moving it moves the
  camera along time and shows that handoff's ruled line, as now. A thread that closed later is drawn open
  there (Q-S5-1 B, as now).
- **Drag on the scene** does the same as the slider. **The pointer** tilts the view a few degrees.
- **Hover a thread** and it lights, with its gates; the rest dims (Q-H3 for words).
- **Scroll:** see Q-H2.
- **Off-screen or in a hidden tab** the scene stops drawing.

**The Display panel:**
- **Motion Full:** everything above.
- **Reduced:** the scene, still. No opening, no tilt; the slider jumps the camera without travelling.
- **Off:** as Reduced, and nothing animates.
- **Theme:** dark is light on black. Light is ink filaments on paper, the teal for carried threads.
- **Contrast More:** thicker filaments, no glow, the floor opaque.
- **Text size:** the HTML scales as now; gate numbers are drawn at a size read from the root.

**When the scene can't run** (no JavaScript, no WebGL, the library fails to load), the page is what it is
today: the SVGs, the scrubber with scripts, the list. The SVGs stay in the HTML and are hidden only once the
scene has drawn its first frame.

### 3. What it rests on

- **Three.js** (Q-H1), vendored under `public/assets/vendor/three/` with its MIT licence, pinned by the sha512
  the CDN publishes, as axe-core is. The newest on cdnjs is **0.186.1**, as `three.module.min.js` plus
  `three.core.min.js`. **Their minified size isn't listed in the metadata read; it's measured and stated when
  the download is asked for.**
- **`assets/ledger-scene.js`,** one ES module, loaded `type="module"` after first paint. It replaces
  `ledger.js` on the home page and keeps its jobs (the slider, the spoken value, DESIGN-6's mark).
- **The data:** `export-ledger.py` also writes `assets/ledger-data.json` (columns, threads, ends, parks,
  traps) from the same source as the SVGs. A file, not an inline block: only JSON-LD is allowed inline
  (Q-P4-4 A). Its `--check` covers the JSON too.
- **The CSP** needs no change: scripts from `'self'`, a WebGL canvas. Checked live by `site_check.py`.
- **Accessibility:** the canvas is `aria-hidden`. The slider, its spoken value and the list carry the
  content, as they do now. A-1's points for the ledger carry over.
- **Speed:** the device pixel ratio capped at 2, drawing paused off-screen, one draw call per layer. Frame
  times are measured in headed Chromium on Thomas's PC, and stated as that.

### 4. Checks

- **`site_check.py`:** the scene draws with scripts and WebGL; with WebGL disabled and with the library
  blocked, the SVG ledger shows whole; each motion level does what §2 says; the slider still speaks each line.
  The control for each: the same check against a page with the fallback broken must fail.
- **`budget.py`:** the home page against its new ceiling, and axe-core in both themes.
- **`shots_diff.py`:** every other page unchanged, with `--self` and `--inject` as controls.
- **Looked at:** a recording of the opening, the slider and hover, in both themes, 1280 and 375. A build
  can't judge the look (rule 4), so Thomas rules the look from the recording before anything ships.

### 5. Not in this proposal

- **The rest of the site.** Awwwards judges the site, not one screen. Once the hero is ruled, a second
  proposal for the case-study openers and the page-to-page motion.
- **New copy.** The caption under the ledger describes the SVG. If the scene makes it wrong, its new words
  come as numbered blocks.

### Questions

**Q-H1:** how the scene is drawn.
> **A (recommended):** Three.js 0.186.1 from cdnjs, vendored and pinned. The download is asked for first,
> with its name, source and size.
>
> **B:** raw WebGL2, no library. Smaller, but much more code to write and keep working.

**Q-H2:** scrolling.
> **A (recommended):** the page scrolls as normal. The scene sits behind the hero, and as the hero leaves,
> the camera rises to the whole ledger seen from above. Nothing holds the page.
>
> **B:** scrolling drives time: the page holds while the camera travels 001 to now, then lets go. More
> dramatic, and the most common complaint about award sites.

**Q-H3:** words on the scene.
> **A (recommended):** none new. Hover lights a thread and its gates; the words stay the ruled lines under
> the slider.
>
> **B:** a hover label with the item's ID and name (e.g. "C-26"). Those are internal shorthand, so each
> would need ruling as copy.

**Q-H4:** phones and tablets.
> **A (recommended):** the same scene, lighter: no glow, pixel ratio 1.5, the portrait layout (time runs
> down the screen).
>
> **B:** the SVG on phones, the scene from 45em wide up.

**Q-H5:** the home ceiling.
> **A (recommended):** build, measure with `budget.py --live`, then propose the number by Q-P4-8's rule
> (the measured weight plus 10%, up to the next 10 kB) for ruling before it ships.
>
> **B:** set a number now and build to it.

### Rulings, H-0 (2026-10-02)

Thomas, verbatim: **"h-0 ok, all A"**. Read as:
- H-0 OK as proposed.
- Q-H1 A: Three.js 0.186.1 from cdnjs, vendored and pinned; the download asked for first.
- Q-H2 A: the page scrolls as normal; the camera rises as the hero leaves; nothing holds the page.
- Q-H3 A: no new words on the scene; hover lights a thread and its gates.
- Q-H4 A: the same scene on phones, lighter, in the portrait layout.
- Q-H5 A: build, measure live, then the ceiling proposed by Q-P4-8's rule for ruling.

### The steps

1. H-0 ruled. ✓ 2026-10-02
2. The download (Thomas: "download ok") and the prototype, on branch `ledger-hero`, local only. ✓ 2026-10-02,
   below; for Thomas to rule the look.
2. The download asked for (name, source, size). Then a prototype on a branch, run locally, never pushed to
   `main`. A recording of it here for Thomas to rule the look.
3. The look ruled, or fixed and recorded again.
4. The checks built and their controls run. The measured weight and the proposed ceiling here, and any
   new caption words as numbered blocks.
5. Shipped on his word. `deploy_wait.py`, then `site_check.py --live` from an up-to-date `main`.

---

## Step 2 — the prototype (built 2026-10-02, for Thomas to rule the look)

**The download:** Thomas, verbatim: "download ok". Three.js 0.186.1 from cdnjs, both files matching cdnjs's
published sha512: `three.module.min.js` 392,497 bytes and the minified core 415,484 bytes (90 kB and 105 kB
gzipped by the agent's measure), and the MIT `LICENSE` from the r186 tag. In
`public/assets/vendor/three/`, with `SOURCE.md` (kept off the site by `.assetsignore`). `.gitattributes`
keeps the folder byte for byte.

**What's built** (branch `ledger-hero`, cut from `main` at `23e1da1`; not pushed):
- `scripts/export-ledger.py` also writes `public/assets/ledger-data.json` (4.7 kB): columns, bands, each
  thread's lane, start, end and state, and the traps. No IDs. `--check` fails when it's stale; the control
  (the file absent) failed as it should.
- `public/assets/ledger-scene.js`: the scene, as §2.
- `ledger.js`: sends each step as an `lg:show` event, and watches the hero, not the figure, for the draw-in
  while the scene loads.
- `prefs.js`: the `data-lg-scene` mark, with a 5 s fallback to the SVGs.
- `style.css`: the scene's block at the end of the ledger's, and `.topbar` given `position: relative;
  z-index: 30` (below).
- `index.html`: one `<script type="module">` line.

**Looked at** (Playwright's Chromium, software WebGL, 1280×800 and 375×812): the opening, the slider back to
010 and forward, hover, drag and the scroll rise, in dark and light. Recordings and stills in
`Claude outputs/ledger-hero/`. The fallback was seen once by accident: with the core file missing, the
mark came off and the SVGs came back. Frame times on real hardware aren't measured yet.

**Measured:**
- `budget.py` (local): **home 1,198 kB against its 390 kB ceiling**, the only failure. Three.js is about
  808 kB of that, as decoded. The other pages are unchanged.
- `site_check.py` (local): **223 of 226**. The three failures test the SVG hero: the two "picture shows"
  checks, and M2's "never shown whole first" (the draw-in now starts at load). They're rewritten in step 4.

**Where it departs from H-0, for ruling:**
- **Contrast More:** the floor is 90% opaque, not fully. An opaque floor would hide the traps layer.
- **The top bar's stacking:** the scene put itself over the Display panel and the sub-menu (found by
  `site_check.py`: the panel's options couldn't be clicked). `.topbar` now sits above it. That's on every
  page, so step 4 proves it changes nothing else with `shots_diff.py`.
- **Q-H5:** a ceiling measured `--live` needs the page live first. Proposed instead: step 4 measures it
  locally (decoded, which is what the ceiling compares), you rule the number, and the first live run after
  shipping confirms it.

**Q-S2:** the look.
> **OK:** go to step 4, the checks.
>
> **FIX:** say what to change.

### Rulings, step 2 (2026-10-02)

Thomas, verbatim: **"s2 ok, local ceiling ok"**. Read as:
- Q-S2 OK: the look, as recorded, on to step 4. Read as covering the two departures listed under it (the
  floor at 90% under Contrast More; the top bar above the scene) as well.
- The home ceiling is set from a local measurement, by Q-P4-8's rule; the first live run after shipping
  confirms it. The number itself is proposed below for ruling.

---

## Step 4 — the checks, the ceiling and the words (built 2026-10-02, for Thomas to rule)

### The checks (`site_check.py`)

- **The SVG checks run with WebGL off** (`SCENE_OFF`), so they test the fallback as they always tested the
  ledger: the two "picture shows" checks, M2's draw-in and DESIGN-6. All pass.
- **New:**
  - the scene draws at 1280 (behind the hero) and 375 (in the figure), `aria-hidden`, the SVGs hidden, and
    the picture isn't blank;
  - the served `ledger-data.json` is what `export-ledger.py` writes now;
  - **the fallback:** with WebGL refused, Three.js blocked or the data missing, the SVGs are back within
    1.5 s. **Control:** the same three with the scene's give-up line taken out each fail. They did.
  - motion: under Full the opening runs from load and the picture moves; under Reduced, Off and the OS's it
    starts at the newest and holds still. Both pictures must have something in them, so two blank ones
    can't pass as "still".
  - a drag on the scene moves the slider back, and the line and the spoken value follow.
- **Local: 233 of 233.**
- **`shots_diff.py` against `main`:** `--self` 48 of 48 identical; `--inject` found the one-pixel change on
  all 48; the real run: **44 of 48 identical, the 4 that differ are the home page.** The top bar's change is
  invisible on the other 11 pages.

**Fixed on the way:**
- Three.js now loads inside the scene's own code, so a failed load gives up at once. Before, the page
  waited out prefs.js's 5 s with no picture.
- On phones the draw-in waits for the scene to scroll into view, as before. It had been running at load,
  below the fold.
- **Own miss, in the prototype you OK'd:** it had room for 600 dots, and the parked threads need about
  1,740, so some parked threads were cut short (the right-hand bands). The room is now counted from the
  data. A mark with no room logs a console error, which `site_check.py`'s "console clean" check fails.
  Control: a copy with the room forced to 100 logged it; the real file logs nothing.
- The traps' inferred starts are now dotted, as the caption says. The prototype drew them fainter.

### The ceiling

`budget.py`, local, 2026-10-02: **home 1,199 kB** (decoded, larger of 1280 and 375). Three.js is 808 kB of
it. Q-P4-8's rule (plus 10%, up to the next 10 kB) gives **1,320 kB**. Every other page and the
accessibility rules pass (47 of 48, the 48th is this ceiling).

### The blocks

Shipping the hero makes three lines on `/work/this-site` untrue and one picture stale. They ship with it,
or the hero waits.

| # | Where | Now | Proposed |
|---|---|---|---|
| TC1 | Home, the ledger's caption (curation `copy.traps.caption`), first words | "The bottom band is the traps, mistakes written down for the next session: …" | "Under the items are the traps, mistakes written down for the next session: …" (the rest unchanged). True of both pictures: a band under the others in the SVG, a layer under the floor in the scene. |
| TH1 | `/work/this-site`, "What shipped" | "Its words and links render with JavaScript off, and the one heavy thing, the 3D graph, waits for a click. The fonts and the graph’s code library are served from the site itself, not from a third party." | "Its words and links render with JavaScript off. Two things are heavy: the home page’s build ledger, drawn in 3D as the page loads, and the 3D graph, which waits for a click. Their code libraries and the fonts are served from the site itself, not from a third party." |
| TH2 | `/work/this-site`, rules table, the R-019 row's standing rule | "Content renders without JavaScript, and nothing heavy loads before a click. Test it with JavaScript off" | "Content renders without JavaScript, and nothing heavy loads before a click except the home page’s ledger. Test it with JavaScript off" |
| TH3 | `/work/this-site`, PW3 (ruled copy) | "Measured on 2 October 2026, each page’s own files download in between about 200 kB and 600 kB, …; the heaviest is the Projects page, with its pictures." | "Measured on 2 October 2026, before the home page’s 3D ledger, each page’s own files …" (the rest unchanged). It ships the same day as the measurement, so without "before" it reads as untrue. New numbers come from the first live run, through a later block. |
| TH4 | `/work/this-site`, Fig. 1's alt text | "The home page: the heading I run a nonprofit's website, and I hold it to a written standard, above the opening paragraph, with Projects, Method, Background and Contact in the menu." | "The home page: the heading I run a nonprofit's website, and I hold it to a written standard, above the opening paragraph, with the build ledger drawn in 3D to its right, and Projects, Method, Background and Contact in the menu." With Fig. 1 retaken from the hero as built, same size (1280×720). |

- **Kept:** the handoff-016 excerpt in "What good meant" (line 177). It's a verbatim, dated quote with its
  receipt, and still says what handoff-016 said.
- **Not changed:** "no framework, no build step" (stack row, `/projects`). Three.js is a library, copied
  in as published, and the site still has no build step.

### Questions

**Q-S4-1:** the home ceiling.
> **A (recommended):** 1,320 kB, by Q-P4-8's rule, recorded in `budget.py` beside the old one.
>
> **B:** another number (say which).

**Q-S4-2:** the blocks TC1 and TH1 to TH4: OK / FIX / CUT each.

### Rulings, step 4 (2026-10-02)

Thomas, verbatim: **"s4-1 A, s4-2 all ok"**. Read as:
- Q-S4-1 A: the home ceiling is 1,320 kB, recorded in `budget.py` beside the old 390 kB.
- Q-S4-2: TC1, TH1, TH2, TH3 and TH4 all OK as proposed, with Fig. 1 retaken.

**Built after the ruling, and checked (local, 2026-10-02):**
- `budget.py`: `/` at 1,320 kB, recorded beside the old ceiling. TC1 in the curation (`copy.traps.caption`
  and its `ruled`), exported: `--check` failed before the export (the control) and passes after.
- TH1 to TH4 in `/work/this-site`. Fig. 1 retaken: the home page's first screen, 1280×720, light, the scene
  whole (Reduced, so no opening), served locally; looked at before it went in.
  - At WebP quality 82 it was 88 kB and put the page at 412 of its 400 kB. At quality 70 it's 69 kB, the
    page 392 kB, and looked at twice its size it's clean. The ceiling is unchanged.
  - The `/work/this-site` card is drawn from that picture, so `og_cards.py` was re-run: that card changed,
    the other six came out byte for byte the same. Its ruled alt text (OG6) doesn't mention the ledger and
    stays true.
- **Found, not fixed:** `og_cards.py --check` passed before the re-run. It doesn't notice a card drawn
  from an older copy of its picture.
- `site_check.py` 235 of 235, with a new check that the served Three.js files hash to cdnjs's sha512 (and a
  one-byte control); `budget.py` 48 of 48 (A-1's known fault named); `schema.py --check` and
  `og_cards.py --check` ok.
- `shots_diff.py` against `main`: 40 of 48 identical, and the 8 that differ are home and `/work/this-site`.
- `cs_check.py work/this-site`: 15 of 17. C-26's "title is the H1" (known), and
  `github.com/…/commits/main` answering 429 to this machine. It fails the same way on `main`'s copy of the
  page: this machine's view of GitHub (rule 7), not this change.

5. Ships on Thomas's word: a PR, merged when he says so; then `deploy_wait.py N` and `site_check.py --live`
   from an up-to-date `main`.
