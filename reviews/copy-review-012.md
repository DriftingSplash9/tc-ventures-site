# Copy review 012 — the header that collapses

**Written:** 2026-10-03
**Why:** Thomas asked for the header to change as the page scrolls: "Can we have a way to make the header
transform when we scroll down so that it is sticky or some sort of animation sequence?"
**Status:** built on branch `header-collapse`, recorded, for Thomas to rule the look and the words below.

Same format and marks as copy-review-001 to 011: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## How it was ruled, verbatim, in order

1. The agent offered four ways (sticky and condensing; a quiet sticky bar; hide on the way down; an animation
   sequence with a TC monogram). Thomas: "I think 4 sounds best. Can you take it to a deeper level?"
2. The agent proposed the deeper sequence. Thomas: "I'd like the header to collapse the menu items together
   into a menu dropdown button. It is bizarre but I want the header to collapse into the tc moniker on the left
   and a menu button on the right. The menu button can have a slight "wobble" giving it "life" and the button
   can be glassy with the teal border and lettering that changes gradient like the chapter numbers do. On
   mobile the menu should always be collapsed and when scrolling down the name can change to the fancy moniker.
   If you can, make the menu button responsive to the tilt and orientation of the mobile device. It could have
   gimbal feel to it can't it?"
3. The agent put six decisions. Thomas: "1 yes, 2 display needs to be a symbol- the accessibility on like what
   A11y uses except in my colors and same glassy look already being implemented on the menu button. While at it
   we should have a matching scroll to top button made and put sticky on the bottom left. We need a way to know
   what page we are on so when we scroll down can we have in faint colour the page name behind the monogram,
   menu button, and accessibility button. 3&4 yes, 5 yes- combine with the above, just don't say "you are here"
   that's cheesy af"

**Read as:**
- 1 yes: the button says "Menu" (HD1).
- 2: Display becomes a glass button with the accessibility symbol, in the site's teal, with no visible word. Its
  name for screen readers stays "Display".
- New: a matching glass "back to top" button, sticky at the bottom left (HD2).
- New: the page's name, faint, behind the slim bar.
- 3 yes: an iPhone asks for motion and orientation once, on the first tap of Menu.
- 4 yes: on a computer, the Menu button leans toward the pointer.
- 5 yes, combined: on a case study or `/method`, the section being read sits beside the faint page name. No
  label of any kind, and never "you are here".
- 6 (Reduced, Off, no script) wasn't answered: read as the standing rules. Reduced and Off switch the bar at
  once, with no wobble, lean or progress line; without JavaScript the bar is the plain one.

## What it does (assets/header.js, the end of style.css)

- **Sticky, and it folds as the page scrolls** (wide screens; the first 160px of scroll, eased):
  - "Thomas Cheesman" folds into a TC monogram: the other letters fall away, each word's last letters first.
    The T and C grow and take the drifting teal gradient of the section numbers.
  - The nav folds into the glass Menu button on the right.
  - The bar slims and turns to frosted glass.
  - The page's name shows faintly behind it.
  - A progress line runs along the foot, notched at each section.
  - Scrolling back plays it in reverse. Hovering or focusing the monogram unfolds the name.
- **On a phone:** the bar is always the monogram-or-name, the Display button and Menu. The name becomes the
  monogram once the page scrolls.
- **Menu:** a glass pill, a teal gradient rim and lettering that drift like the section numbers. Now and then
  it wobbles. It leans like a gimbal: toward the pointer, or with the phone's tilt. It opens the nav as a panel
  (the case studies listed under Projects); Esc, a click outside, or Tab past it closes it.
- **Display:** the same glass, with the accessibility symbol. It opens the Display panel as before.
- **Back to top:** the same glass, an arrow, at the bottom left once the page has scrolled a screen.
- **Contrast More:** solid, no glass, no gradient. **Forced colours:** the system's own colours.

**Found and fixed while building:** the bar's glass was see-through. The bar's view-transition name (for page
changes) makes it a backdrop root, so a glass layer inside it blurred nothing. The blur is now on the bar
itself, and the Menu panel, which can't blur through it, is nearly opaque.

**Contrast:** "Menu" is small text, so its lettering uses a darker light-theme patch (`--grad-3t`, `#11808C`,
4.6:1); the large monogram and the rims keep the section numbers' range (3:1 or better).

## The words

| # | Where | Words | Note |
|---|---|---|---|
| HD1 | The Menu button | "Menu" | Ruled: "1 yes". |
| HD2 | The back-to-top button, for screen readers (the button shows an arrow) | "Back to top" | New. |
| HD3 | The monogram | "TC" | From option 4, which Thomas chose ("I think 4 sounds best"). The link's name stays "Thomas Cheesman". |
| HD4 | The Display button, for screen readers (it shows the symbol) | "Display" | Unchanged: DP1's word. |

**Q-HD:** the look OK / FIX, and HD2 OK / FIX.

## Found and fixed by the checks, before Thomas ruled

- **On a phone with 200% text the full name covered Menu**, so Menu couldn't be tapped (`site_check.py`'s
  sub-menu click at 375px). Where the name doesn't fit beside the buttons, the bar shows the monogram from the
  start and doesn't peek. The room Display leaves for Menu is Menu's own width, not a fixed 6.25rem.
- **The T and C lagged a change of text size** (a CSS transition on `font-size`; "text grows with the browser's
  text size" failed on nine pages). `header.js` sets their size from the fold instead.
- **`site_check.py`** opens Menu first wherever the bar is compact (a phone, 200% text).
- **Weight:** `header.js` (13 kB) and its CSS (about 12 kB) put six pages over their ceilings.

## Ruled 2026-10-03

Thomas, verbatim: **"1 THE LOOK IS OK. 2 back to top yes please. increase the ceilings by 33% instead of 10%.
"Thomas Cheesman" in the header can be teal-gradient too. The glassy buttons etc would look great if they had
a smoked glass look - again with a gradient to it. I think the borders and lettering on the buttons is ok, can
you make it look bolder and metallic?"**

**Read as:**
- The look OK. HD2 OK.
- The six ceilings at the measured weight plus 33%, rounded up to the next 10 kB:

  | Page | Weight | Ceiling |
  |---|---|---|
  | `/work/back-quarter` | 368.2 kB | 360 → 490 |
  | `/work/bare-your-rare` | 317.9 kB | 300 → 430 |
  | `/method` | 319.7 kB | 310 → 430 |
  | `/background` | 300.1 kB | 290 → 400 |
  | `/contact` | 300.0 kB | 290 → 400 |
  | `/404` | 296.2 kB | 280 → 400 |

- Three changes to the look, built:
  - **The name in the teal gradient** on every page, with or without scripts. It is small text, so it uses the
    4.6:1 patch.
  - **Smoked glass:** a dark tinted gradient, the same on both themes.
  - **Bolder, metallic lettering and rims.** The lettering is the display face at 700, in a polished-metal
    gradient of the light teals with a hard highlight band. The rims are 2px of brushed metal whose highlight
    turns with the drift. The icons' strokes are heavier.
- **Contrast:** because the smoke is dark, the metal is the light teals on both themes. Every lettering stop is
  4.5:1 or better on the smoke at its lightest (88% over the light page). The rims and icons are 3:1 or better.
- **Contrast More:** solid near-black buttons with solid light-teal lettering; the name solid teal.
- **The look:** `Claude outputs/header/`, re-recorded.

**Then:** the metal CSS tipped two more pages over by under 1 kB each. Put to Thomas with the look; ruled
**"1-2 yes, open the PR and merge it when checks pass"**: `/work/desk-and-drawer` 480 → 640 (480.4 kB) and
`/work/gprs` 530 → 710 (530.4 kB), at +33%; the smoked metallic look OK; open and merge on passing checks.

## TH3d — PW3 after the header (2026-10-03)

Live after #68 (`8b044a1`), `budget.py --live` failed INFRA-23's PW3 check: the lightest page is `/404` at 216 kB on
the wire, the heaviest `/projects` at 784 kB (`header.js` and its CSS on every page). PW3 said "between about
200 kB and 780 kB". The same miss as SP-B's; this time the check found it within minutes of the deploy. Wire
weights exist only live, so no local run could have caught it.

| # | Now | Proposed |
|---|---|---|
| TH3d | "Measured on 3 October 2026, each page’s own files download in between about 200 kB and 780 kB, …" | "Measured on 3 October 2026, each page’s own files download in between about 220 kB and 790 kB, …" |

**Ruled 2026-10-03.** Thomas, verbatim: **"TH3d yes, ship it and merge when checks pass"**.

## The second form (2026-10-03, branch `header-pills`)

Thomas, verbatim, in order:
1. "see how thomas cheesman collapsed? also, i don't want a divider or fill for the header - my header is my
   name/monogram, the menu pill then the accessibility buttons only - It's unusual I think? move the
   accessibilty button to the right of the menu button. In the non-collapsed header all the menu items should
   be in matching pill buttons"
2. "keep the faint page name, drop the progress line"
3. "1 - it does need  box for the shrunken header because there is too much awkward interference naked. the
   menu button directly on legible text or pics is a bad idea lol. Can the header be a 3D rectangular bar with
   the buttons/menu on it and have it face the cursor. The surface of the rectangular bar can look like a light
   shines on it, like it is in sunshine/moonshine."
4. "the look is getting there, i want sharper edges and make it more like a square tubular rectangular bar,
   open the PR and merge it when checks pass"

**Built:**
- **The name at rest** flows as ordinary text, keeping the font's spacing. Before, each letter was a box,
  measured before the font loaded, so the name drew crowded. It becomes boxes only while it folds, and is
  measured once the fonts are ready.
- **No fill and no rule** at the top of the page. The plain no-script bar lost its rule too.
- **At the top of a wide page:** Projects (its arrow inside), Method, Background and Contact as smoked metallic
  pills, then Display. Where the four don't fit beside the name, the folded form shows from the start.
- **Folded:** TC, then Menu, then Display at the far right, on the **slab**.
- **The slab:** a square-section bar with sharp corners, a lit top face and a shaded bottom with depth. Under
  Full it turns a few degrees to face the pointer, or with a phone's tilt. Its light slides as it turns: warm
  sun on the light theme, cool moon on the dark. Reduced and Off: flat and still. Contrast More: plain and
  solid.
- **Kept:** the faint page name, with the section being read. **Dropped:** the progress line.
- **The Menu panel** is solid.
