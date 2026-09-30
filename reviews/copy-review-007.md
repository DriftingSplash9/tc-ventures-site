# Copy review 007 — Phase 3, craft

**Written:** 2026-09-29
**Why:** Phase 3 (PL-6): motion, type and the built-in accessibility controls, plus the layout jobs logged
for it: DESIGN-2, DESIGN-1, G-7, and the ledger's later layers (PL-9). Propose before building.
**Status:** Step 1 (P3-0, the proposal) **ruled 2026-09-29: "p3-0 ok, all A"** (see "Rulings" at the end of
P3-0). Step 2 (the groundwork) built and checked, and it ships on Thomas's word.

Same format and marks as copy-review-001 to 006: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## P3-0 — Step 1: the proposal (not copy)

**To rule:** P3-0 as a whole (OK / FIX), plus Q-P3-1 to Q-P3-7.

**The brief, Thomas, 2026-09-22 (PL-6):** "Awwwards - novel designs and motions, it needs all the
accessibility toggles, I don't want a generic app like A11y taking over the features." The controls are
motion full/reduced/off, theme, contrast and text size. They are built into the site, the OS settings are
the defaults, and a choice overrides them and is remembered. In the 2026-09-22 audit (handoff-015 §2),
design and creativity scored lowest. Phase 3 is aimed at those two.

**Read and measured 2026-09-29:**
- **Read:** plan-001; handoff-015 §2 (the audit); PL-6 and PL-9; `style.css`, `nav.js` and
  `graph-demo.js`; `_headers`; the home hero markup.
- **Measured:** Chromium, through a scratchpad script, on the local `public/` at `main` (135f6e8).
  Candidate layouts were tried by injecting CSS into the loaded page. Nothing on disk or on the site
  changed.

### 1. Where the site stands

- **Theme:** dark mode follows the OS only, through one `prefers-color-scheme` block of tokens. There is
  no way to choose.
- **Motion:** almost none.
  - The sub-menu caret turns, and buttons fade their colours on hover.
  - One rule switches every transition off when the OS asks for reduced motion.
  - The 3D graph solves its layout before the first frame under reduced motion (`graph-demo.js`
    L211).
  - On `/`, `/method` and `/work/influence-graph`, nothing is animating once the page has loaded.
- **Contrast:** nothing responds to the OS's "more contrast" setting. Computed from the tokens:
  - Every text colour token (ink, ink-soft, muted, accent, accent-ink) already reaches 4.5:1 on both
    grounds, in both themes. The lowest is muted text on the tinted ground in light, at 5.0:1.
  - Short of 7:1:
    - muted text in light (5.4:1 on paper, 5.0:1 on the tint);
    - muted text on the tint in dark (6.6:1);
    - the accent on the tint in light (6.7:1).
  - The rules (borders) are 1.2:1 in light and 1.3:1 in dark. That's fine for decoration, and faint
    wherever a rule carries meaning (A-1 already notes the diagrams' connectors).
- **Text size:** body text is fixed at 18px. Of the stylesheet's 79 `font-size` declarations, 28 are in
  px, and so are four type tokens (`--t-label`, `--t-tag`, `--t-mono`, `--t-body`).
  - A browser set to twice the default text size was simulated by doubling the root size.
  - On `/method`, body prose stayed 18px, the nav 13px, labels 12px and the footer list 13px. Of what
    was measured, only the headings grew (the H1 went from 65.6 to 83.2px).
  - So today, a reader's own browser setting does almost nothing here.
- **Scripts:** the CSP allows no inline script (`_headers`). Any code that must run before the first
  paint has to be a small file in `/assets/`.

### 2. The controls

- **One "Display" button in the top bar, on every page.** It opens a small panel, using the same
  disclosure pattern as the Projects sub-menu: Enter opens it, Esc closes it, and it overlays the page
  without moving anything. Inside are four native radio groups:
  - **Motion:** System · Full · Reduced · Off
  - **Theme:** System · Light · Dark
  - **Contrast:** System · Standard · More
  - **Text size:** Standard · Large · Larger
- **System follows the OS,** and it is the default for each group.
- **A choice is remembered in this browser only** (`localStorage`). No cookie, and nothing is sent
  anywhere. If storage is blocked, the site quietly falls back to the OS settings.
- **Applied before the first paint:**
  - A small file, `/assets/prefs.js`, loads in each page's `<head>` and marks `<html>` with the
    choices. The CSS reads those marks, so no page flashes the wrong theme.
  - It's the only script that has to run before the page draws.
  - An inline script with a CSP hash would do the same, but the hash would have to change in `_headers`
    with every edit. That's one more thing to drift.
- **Without JavaScript:** there's no button, since it can't work. The OS settings still apply, because
  they are plain CSS. Words and links are unchanged.
- **What each setting does:**
  - **Motion Full:** everything in section 4.
  - **Motion Reduced:** fades and colour changes only. Nothing moves, scales or draws in, and the ledger
    appears whole.
  - **Motion Off:** nothing animates at all, and pages change the way they do now.
  - **Contrast Standard:** today's palette, unchanged.
  - **Contrast More:** every text pair to 7:1, rules to 3:1, and thicker focus rings, in both themes.
    Windows high contrast (forced colours) is handled whatever this is set to.
  - **Text size:** each step scales every size on the page, on top of the reader's own browser setting.
    That needs the px sizes converted to rem first (step 2). The ledger's SVG labels scale with the
    picture, not the text size; its list is the text equivalent, and that does scale.
- **The header has to fit the button.** At 375px the top bar already takes two lines (the name, then the
  nav). The button must fit without a third, and that's checked at build.

**Q-P3-1:** where the controls live.
> **A (recommended):** a "Display" button at the end of the top bar on every page, as above.
>
> **B:** a "Display" section in every page's footer. There's no header change, but it's far from where
> people look first.

**Q-P3-2:** what the OS's "reduce motion" setting maps to, under System.
> **A (recommended):** Reduced, which still allows fades. That's the common reading of the setting:
> reduce, not remove. Today that setting switches off every transition, so for those readers this is a
> small change.
>
> **B:** Off, which keeps today's behaviour exactly.

**Q-P3-3:** the text-size steps.
> **A (recommended):** Large is 1.125 times Standard and Larger is 1.25 times. Both apply on top of the
> browser's own setting, which starts working once the sizes are in rem.
>
> **B:** a single Large step.

### 3. Layout: DESIGN-2, DESIGN-1, G-7

**DESIGN-2, the ledger against the fold.** The home lede is capped at 34ch (`style.css` L330), so at
1280px it runs to 10 lines and 348px. The table shows where the top of the ledger picture sits against
the bottom of the first screen: "below" means off the first screen by that much, and "on" means that
much of it shows.

| Screen | Now | A: lede 52ch | B: A, and the hero's top padding 64px at most |
|---|---|---|---|
| 1280×900 | 86px below | 53px on | 93px on |
| 1440×900 | 86px below | 53px on | 93px on |
| 1920×1080 | 94px on | 233px on | 273px on |
| 1024×768 | 203px below | 64px below | 23px below |
| 375×812 | 136px below | 107px below | 91px below |

At 52ch the lede takes 6 lines and 209px at 1280. Screenshots of now, A and B went to Thomas in the chat.
They're in the scratchpad, not the repo.

**Q-P3-4:** DESIGN-2.
> **A (recommended):** widen the lede to 52ch, the measure `.pagehead` ledes already use. The ledger's
> column numbers and first band then show on a 1280×900 screen: a glimpse that invites the scroll. The
> H1, the words and the order are unchanged (LG0 §4).
>
> **B:** A, and also trim the hero's top padding, so more of the ledger shows.
>
> **C:** leave it.

**DESIGN-1, the sub-menu at 375px:**
- **Now:** the open list runs from x=4 to x=379, so the page is 379px wide on a 375px screen.
- **Candidate:** capping the list at the screen's width, with labels allowed to wrap, stops the sideways
  scroll (375 wide).
  - The first try wrapped the labels into a 240px box, narrower than it needs to be. The build sizes
    it to the screen.
- **The check:** since 2026-09-29, `site_check.py` checks this on every page as a known fault. When the
  fix lands, that check starts failing until its DESIGN-1 mark is taken off, which proves the fix from
  outside.

**G-7, the graph's paragraph:** on `/work/influence-graph` there's 0px between the paragraph and the
graph's frame, at 1280 and at 375 (the frame's top margin is 0). The fix gives it the case study's
standard block gap (`--block`). The frame and its panel below stay joined, as now.

No question for DESIGN-1 or G-7: both are fixes, not choices.

### 4. Motion

**The rule for all of it:** motion shows something true about the site, never a stock effect (plan-001
§4c). It sits on top of the words and never carries them. Each motion is named here, and each has its
Reduced and Off states.

- **M1, page to page.**
  - When a page changes, the top bar stays still and the content cross-fades.
  - **The signature move:** a case study's sub-menu label is its H1 (a standing rule). With a native
    CSS feature, cross-document view transitions, the label you click grows into the H1 of the page
    that opens.
  - No JS, and no library. Browsers without the feature change pages as they do now. Which browsers
    support it gets checked at build, not from memory.
  - Reduced: the cross-fade only. Off: none.
- **M2, the ledger draws itself** (PL-9's motion layer). The first time the ledger scrolls into view,
  the threads draw in session by session, 001 to the newest, in a few seconds. Reduced and Off: it
  appears whole.
- **M3, the method loop (optional).** On `/method`, the loop diagram's arrows trace the loop once, brief
  to next session, when it scrolls into view. Reduced and Off: static.

**Q-P3-5:** which motions.
> **A (recommended):** M1 and M2 now. M3 after, if the first two earn their place.
>
> **B:** all three now.
>
> **C:** M2 only.

### 5. The ledger's later layers (PL-9)

LG0 left three layers out of the static ledger: motion (M2 above), click a column to read its line, and
traps.

- **Reading a column: a scrubber, not clickable columns.**
  - Under the picture sits a native slider (`<input type="range">`), one step per handoff. Moving it
    highlights that column and shows its ruled line underneath, like "017 · 2026-09-24 · …".
  - A native slider already works with a keyboard, touch and a screen reader. The picture stays a
    `role="img"` with nothing to click inside it, which answers A-1's doubt about links inside an SVG.
  - M2's draw-in is the same scrubber running from 001 to the newest.
  - Without JS there's no slider, and the list below carries every line, as now.
- **Traps:** handoffs only list the traps new to each session from 019 on. Drawing them means a
  curation pass and its own copy review.

**Q-P3-6:** PL-9.
> **A (recommended):** the scrubber and the draw-in now. Traps later, in their own review.
>
> **B:** all three now.
>
> **C:** the draw-in only.

### 6. How each step is checked (rule 5)

Every new check gets a control that must fail.

- **Converting px to rem, and restructuring the theme tokens, must change nothing at the default
  settings.** The proof: screenshots of every page, light and dark, at 1280 and 375, pixel-identical
  before and after.
- **Contrast is measured, not asserted.** A script computes the WCAG ratio for every text and background
  token pair, in each theme at each contrast setting. Standard must reach 4.5:1 (it does today), and More
  must reach 7:1 for text and 3:1 for rules. The control is one token pushed past the line, which must
  fail.
- **`site_check.py` gains:**
  - each stored setting is on `<html>` before the first paint, and it carries to the next page;
  - with Motion Off, nothing is animating after load and after opening the menu and the panel;
  - at Larger text, and at twice the browser's text size, no page scrolls sideways at 375 or 1280;
  - the panel's keyboard path, as the sub-menu's is checked now;
  - JS off: no button, and the OS settings still apply.
- **Looked at, not only scripted:** each step goes to Thomas as screenshots, and on a local preview if
  he wants one.

**Q-P3-7:** how it ships.
> **A (recommended):** one step at a time, each live-checked and on Thomas's word (section 7). Each step
> stands on its own, and the first changes nothing visible.
>
> **B:** all of it together, at the end.

### 7. The steps

1. **Step 1:** this proposal, ruled.
2. **Step 2, the groundwork, with no visible change:**
   - px to rem;
   - the theme and contrast tokens restructured;
   - the pixel-identical proof, and the contrast script.
3. **Step 3, the Display panel:**
   - `prefs.js`, the button on the 13 files and the new checks;
   - the panel's labels as copy blocks here (DP1 onward), for ruling;
   - a local preview.
4. **Step 4, the layout:** DESIGN-2 as ruled, DESIGN-1 (with its DESIGN-1 mark taken off the check),
   and G-7.
5. **Step 5, the motion:** M1 and M2 as ruled, and the scrubber. The scrubber's words come from the
   ruled ledger lines, so there's no new copy, except its label, which is a copy block here.

**Not in Phase 3:**
- **Phase 4:** headers, schema, a link-preview image per page, the budget script.
- **A-1, Thomas's accessibility pass:** his, when design and content are final.
- **The 3D graph's own motion:** it gets one change. It reads the site's motion setting instead of only
  the OS's, and it keeps its dark ground.
- **Copy beyond the panel's labels and the scrubber's label.**

### Rulings, P3-0 (2026-09-29)

Thomas, verbatim: **"p3-0 ok, all A"**. Read as:
- P3-0 OK as proposed.
- Q-P3-1 A: a "Display" button at the end of the top bar on every page.
- Q-P3-2 A: under System, the OS's "reduce motion" maps to Reduced, which still allows fades.
- Q-P3-3 A: text size Standard, Large (1.125×) and Larger (1.25×), on top of the browser's setting.
- Q-P3-4 A: the home lede widens to 52ch.
- Q-P3-5 A: M1 (page to page, the label into the H1) and M2 (the ledger draws itself) now; M3 later.
- Q-P3-6 A: the scrubber and the draw-in now; traps later, in their own review.
- Q-P3-7 A: one step at a time, each live-checked and on Thomas's word.

---

## Step 2 — the groundwork, built (2026-09-29)

**Nothing looks different at the default settings.** Every page is pixel-identical before and after (below).
What changes is underneath. It isn't copy, so there's nothing to rule here, only the ship.

**What changed:**
- **`style.css`, px to rem:**
  - 24 `font-size` declarations and the four px type tokens are now in rem, at the same sizes (18px is
    1.125rem, 13px is 0.8125rem, and so on; every value is an exact sixteenth).
  - The four SVG label rules (the method loop and the ledger) stay in px. They're in the picture's own
    units and scale with it.
  - In `404.html`'s own style block, `.lost__code` goes to rem, and its diagram label stays in px.
  - So a reader's browser text size now reaches every piece of HTML text. At default settings nothing
    moves.
- **`style.css`, the theme hooks:**
  - The dark colours are written once, as `--dark-*`.
  - Two rules switch to them: the OS's dark mode unless `data-theme="light"` is on `<html>`, or
    `data-theme="dark"`.
  - Nothing sets `data-theme` yet. `prefs.js` does that in step 3, so for now the OS decides, as
    before.
  - The draft banner's dark rule follows the same two routes.
- **Moved to step 3, with a reason:** the Contrast More colours.
  - They're new colour choices Thomas hasn't seen. They go in with the panel, where the local preview
    shows them.
  - So this step changes nothing for anyone, including readers whose OS asks for more contrast.
- **`scripts/shots_diff.py` (new):** every page, light and dark, at 1280 and 375, shot whole from two
  copies of `public/` and compared pixel for pixel.
  - The clock is fixed, animations are held, and images are decoded before each shot.
  - Its first stability control failed: on `main` against itself, 38 of 48 pairs matched. Lazy,
    async-decoded images sometimes painted as an empty box. After forcing the decode: 48 of 48.
- **`scripts/site_check.py` gains three kinds of check:**
  - **Every page:** all text outside SVG grows when the browser's text size doubles. Screen-reader-only
    text is left out: it's never seen, and the one in the sub-menu button takes the browser's fixed
    button size.
  - **The theme:** `data-theme` gives exactly the OS's colours, dark on a light OS and light on a dark
    one.
  - **Contrast, light and dark:** from the colours the browser resolves, every text colour token on both
    grounds, and the solid button's text, is 4.5:1 or more. The lowest are 5.01 in light and 6.56 in
    dark, both muted text on the tinted ground.

**How it was checked:**
- **`shots_diff.py`, `main` against this branch:** 48 of 48 pairs identical.
  - `main` against itself: 48 of 48 (the shots are stable).
  - A 1px shift of the name in the top bar, injected: 0 of 48 identical (a change is found).
- **`site_check.py` on this branch:** 133 of 133, plus 12 known DESIGN-1 faults. That's 16 new checks:
  12 text-size checks, 2 theme, 2 contrast.
- **The new checks, each against a copy with one fault:**
  - **`main` itself:** fails text size on all 12 pages and both theme checks; contrast passes.
  - **`.label` back to 12px:** fails text size on all 12 pages, naming only `.label`.
  - **The data-theme route mapping one token wrong:** fails the dark-route check only.
  - **Light muted text at `#8A93A0`:** fails light contrast only (3.03 and 2.83).

**Shipped:** #20, merged at Thomas's word ("merge 20"), merge `7242c7f`.
- The build check-run completed with success.
- Curl, cache-busted: `/assets/style.css`, `/` and `/404` are byte-identical to `main`. As a control,
  the live CSS and `/404` differ from the pre-merge `135f6e8`.
- `site_check.py --live` passed 133 of 133, plus 12 known DESIGN-1 faults.

---

## Step 3 — the Display panel, built (2026-09-29), for Thomas to look at and rule

**To rule:** DP1 to DP3 (the panel's words), and a look at the preview screenshots. Nothing is live.

### What it is

- **The button:** "Display" at the end of the top bar on all 13 files, with the same caret as Projects.
  - At 720px and under, it moves up to the name's line.
  - At 700px the bar is then two lines, which is the same as a phone today. At 760px everything fits
    on one line.
  - Without scripts it doesn't show.
- **The panel:** four rows of choices, each starting at System, and one line of note under them.
  - It hangs under the bar at the right, and overlays the page without moving anything.
  - Each row is a set of native radio buttons, drawn as a segmented bar. Arrow keys move along a row,
    and Tab goes to the next.
  - Esc closes it and puts focus back on the button, as the sub-menu does.
- **`/assets/prefs.js`:** loaded without `defer` in each `<head>`. It puts the saved choices on `<html>`
  before the page draws.
  - Measured on `/method` with Dark saved: the mark was set 8.4ms in, and the first paint came at 44ms.
  - The choices are stored under one key in this browser's `localStorage`. Nothing is sent.
- **`/assets/display.js`:** builds the panel next to the button and writes the choices.
- **The CSS:**
  - **Motion:** a Reduced and an Off level.
    - Moving things (the carets, the 404's drift) stop under Reduced.
    - Fades (the buttons' colour changes) stop only under Off.
    - Under System, the OS's "reduce motion" means Reduced (Q-P3-2 A). Today that setting stops the
      button fades too, so readers who have it on will now see them fade.
  - **Theme:** `color-scheme` now follows the theme, so scrollbars and form controls turn dark with
    it. For a reader whose OS is dark, that's a visible change: the scrollbar is dark now.
  - **Contrast More:** the colours short of 7:1 for text or 3:1 for rules, each mixed toward the ink
    until it passes on both grounds, and 3px focus rings. In light: muted text `#5F6A79` → `#4A5360`,
    the accent `#0F5F6B` → `#0F5B67`, rules `#E2E6EB` → `#878B91`. In dark: muted text `#939DAC` →
    `#99A3B1`, rules `#222A34` → `#60666F`.
  - **Text size:** Large 112.5% and Larger 125%, on top of the browser's own setting.
  - In Windows high contrast (forced colours), the chosen option shows as a system-colour ring, since
    the fill is painted over.
- **The 3D graph** reads the site's motion setting: Reduced or Off solves its layout before the first
  frame. The 404's drift follows the setting too.

### The words (copy)

**DP1 — the button.**
> Display

**DP2 — the rows and their choices.** These are as P3-0 §2 proposed, and it was ruled OK as a whole.
They're listed here so the words themselves get a ruling.
> **Motion:** System · Full · Reduced · Off
> **Theme:** System · Light · Dark
> **Contrast:** System · Standard · More
> **Text size:** Standard · Large · Larger

**DP3 — the note under the rows.**
> Saved in this browser only.

### Found while building it

- **DESIGN-3 (new): text at 200% on a 375px screen scrolls sideways,** on every page, 426 to 566px wide.
  - What runs off the edge: long unbroken strings (the email address, URLs such as
    `github.com/DriftingSplash9/Reports-Clustering`, receipt links), the footer's lists and the spec
    lists.
  - Larger text (125%) doesn't do it at 375 or 1280, and neither does 200% at 1280.
  - It has been reachable only since step 2, which let the browser's text size work at all. Before
    that, text never grew.
  - It's layout work, so it goes to step 4. `site_check.py` checks it as a known fault.

### How it was checked

- **`site_check.py` on this branch:** 169 of 169, plus 12 DESIGN-1 and 12 DESIGN-3 known faults.
- **`shots_diff.py`, live `main` (`7242c7f`) against this branch with the button hidden:** 48 of 48
  identical.
  - So at default settings, at 1280 and 375, the button is the only visible change.
  - Between 700 and 720px the bar does change: it becomes two lines (screenshot at 700).
- **The new checks:**
  - on every page: the button shows, and no sideways scroll with Larger text at 1280 and 375, or
    200% text at 1280;
  - the panel's keyboard path;
  - a choice applies at once, carries to the next page, and is set before its first paint;
  - the motion times at every level, chosen and under System;
  - Off stops everything, while under Full the 404's drift runs;
  - Contrast More by both routes, text at 7:1 and rules at 3:1;
  - with JS off: no button, and the OS's dark mode still applies.
- **Controls:** three copies, each carrying faults that touch different checks. Every fault was caught by
  its check.
  - **Copy A:**
    - `prefs.js` delayed by 300ms: "before its first paint" fails (320.7ms against the paint).
    - The standard grey as the More grey: More light fails (5.36 and 5.01).
    - The button gone from `/contact`: that page's button check fails.
    - The home H1 unbreakable under Larger: the Larger checks fail on `/` and on `/404`, which shares
      the hero style.
  - **Copy B:**
    - The Reduced rule removed: the motion-times check fails.
    - The button shown with scripting off: the JS-off check fails.
  - **Copy C:**
    - The Off rule removed: the times check and "Off: nothing animating" both fail.
    - `display.js` not loaded on the home page: the panel's keyboard checks and "a choice applies"
      fail.
- **Looked at:** screenshots of the header at 1280, 760, 700 and 375, the panel open at 1280 and 375,
  Dark chosen on a light OS, More in light and dark next to Standard, Larger at 375 and 1280, and the
  panel in forced colours.
### Rulings, step 3 (2026-09-29)

Thomas, verbatim: **"dp1-3 ok, merge 21, then wrap"**. Read as:
- DP1, DP2 and DP3 OK as written.
- Ship #21. The preview screenshots were in front of him, so this is read as his look too.

- **Found by control C, not fixed:**
  - If `display.js` failed to load while scripts run, the button would still show and do nothing. That's
    the same trade the Projects caret makes.
  - Showing the button only after `display.js` runs could shift the bar on every page load, which is
    worse.

---

## Step 4 — the layout, built (2026-09-30), for Thomas to look at and rule

Started at Thomas's word, "go straight to Phase 3 step 4". No copy changes: CSS, one class on the home
hero, and the checks.

### What changed

- **DESIGN-2 (Q-P3-4 A):** the home lede is 52ch (`.hero--home .hero__lede`). It's 6 lines at 1280, and
  the ledger's column numbers and first band show on a 1280×900 screen. The 404 shares the hero style
  and keeps 34ch, so the class scopes the change to the home page. At 375 the lede now fills the column.
- **DESIGN-1:** at 720px and under, the open sub-menu is capped to the screen, with the same 4px margin
  on each side, and a label may wrap ("…written by a patient" takes two lines at 375). From 390px up it's
  unchanged.
- **G-7:** the graph's paragraph gets the `--block` gap above its frame (44px at 1280, 30 at 375).
- **DESIGN-3, text at 200% on a 375px screen:**
  - `overflow-wrap: break-word` on `body`: a word breaks only when it would otherwise run off its line.
  - Grid columns `1fr` → `minmax(0, 1fr)` in the footer, the spec lists and the proof cards. A `1fr`
    column never shrinks below its longest word, so one long address widened the whole footer.
  - Receipts are `inline-block`: one still moves to the next line whole, as `nowrap` did, but one wider
    than the whole line wraps inside itself.
  - The stacked rules table (640px and under) is `table-layout: fixed`, so it keeps its 100%.

### How it was checked

- **`site_check.py`:** 193 of 193, with no known faults left.
  - With the DESIGN-1 and DESIGN-3 marks still on, both checks failed on all 12 pages with "passes
    now: take the mark off". Then the marks came off.
  - **Control:** `main`'s `public/` fails the same 24 checks.
- **`shots_diff.py`, `main` against this branch:** 16 of 48 pairs identical.
  - Identical: `/projects`, `/background`, `/contact`, `/404`, light and dark, 1280 and 375.
  - Differ as intended: the home page (DESIGN-2) and `/work/influence-graph` (G-7).
  - **Differ, not intended: six pages with receipts are 5 to 36px shorter.** As an inline `nowrap` box the
    mono receipt made each line holding one slightly taller; as an `inline-block` it doesn't. Seen side
    by side on `/work/gprs`, the receipts and their dotted rules look the same.
  - `--self`: 48 of 48. `--inject` was not re-run this session.
- **Looked at:** the home page's first screen at 1280×900, the open sub-menu at 375, the graph's gap at
  1280, the footer and a receipt at 375 with text at 200%, each before and after.

### Found while building it

- **DESIGN-4 (new): text at 200% between 375 and 1280 still scrolls sideways.** No check covers these
  widths; `site_check.py` tests 200% only at 375 and 1280.
  - 480 to 600px: every page is 632 to 638px wide. The top bar's links don't wrap.
  - 660 to 960px: `/method` is about 950px wide. The rules table only stacks at 640 and under.
  - 760 to 1024px: the open sub-menu runs past the edge. Labels stay on one line above 720.
  - Nothing at 414, 1024 (menu closed) or 1180.

**Q-S4-1:** DESIGN-4.
> **A (recommended):** fix it in step 4 before it ships, and add a 200% sweep at 480 and 760 to
> `site_check.py`, with a control.
>
> **B:** ship step 4 as it is; DESIGN-4 goes to §4 with a known-fault check.

**Q-S4-2:** the receipts' few pixels.
> **A (recommended):** accept. Nothing a reader would see moves, and the line spacing is now even.
>
> **B:** keep receipts inline and find another fix for them.

### Rulings, step 4 (2026-09-30)

Thomas, verbatim: **"s4-1 A, s4-2 A"**. Read as:
- Q-S4-1 A: DESIGN-4 is fixed in step 4 before it ships, with a 200% sweep at 480 and 760 added to
  `site_check.py`, and a control.
- Q-S4-2 A: the receipts' few pixels are accepted.

### DESIGN-4, built (2026-09-30)

- **The fix:** every width breakpoint is in `em` now, not `px`: 17 in `style.css` and the one in the
  404's own `<style>` (px ÷ 16, so `640px` is `40em`). At the default text size an em breakpoint is the
  same width. With the browser's text size raised, it moves with the text, so the layout reflows as it
  already does under page zoom:
  - the top bar's links wrap (the 420px rule, now 26.25em);
  - the header takes its phone layout, which caps the open sub-menu to the screen (45em);
  - the rules table stacks (40em).
- **The check:** `site_check.py` now sets "text at 200%" the way the browser's own text-size setting
  does (CDP `Page.setFontSizes`), because a `:root` font-size override doesn't reach a media query. It
  checks 375, 480, 760 and 1280px, with the sub-menu shut and open.
- **How it was checked:**
  - `site_check.py`: 193 of 193.
  - **Controls:** `main` fails the new check on all 12 pages. `962efe8`, step 4 without the em
    breakpoints, fails it only at 480 and 760 on all 12 pages.
  - `shots_diff.py`, `962efe8` against this tree: 48 of 48 identical, so the em change is invisible at
    default text. `--inject` (1px on the footer): 0 of 48, so the diff can fail.
  - **Looked at, at 200%:** the home page at 480, the open sub-menu at 1024, `/method`'s table at 760,
    before and after.
- **Found:** a Playwright full-page screenshot drops the CDP text size (the root went from 32px to
  16px). Viewport shots keep it. The first set of 200% screenshots was at default size for that reason,
  and was redone.

---
