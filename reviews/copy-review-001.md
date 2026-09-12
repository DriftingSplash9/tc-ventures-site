# Copy review 001 — everything currently public on tc-ventures.ca

**Written:** 2026-09-11
**Why:** `handoff-001.md` §4 items 1 and 2. Every word below is live right now at
https://tc-ventures.ca and none of it has been read by Thomas.
**Scope:** all body copy from `index.html`, `projects.html`, `background.html`,
plus the shared footer and the `404.html` page. HTML entities have been converted
to real characters (— ' " etc.) for readability; wording is otherwise verbatim.

---

## How to answer this without typing much

Every block has a number. Reply in chat with just the number and a mark:

- `OK` — ships as written
- `CUT` — delete the block
- `FIX` — wrong or needs rewriting, tell me what's wrong in a few words
- `SOFTEN` / `HARDEN` — right content, wrong strength

So a full pass can look like: *"H1 OK, H2 FIX — it's been 3 years not 18 months,
B4 CUT, B9 OK, Q3 yes, Q7 name it."*

Blocks I have concerns about are marked **⚠ FLAG** with the reason. Everything
unmarked I think is good as-is — you can skim those.

---

# PART 1 — index.html (the home page)

### H1 — page title and meta description

> **Title:** Thomas Cheesman
> **Description:** Thomas Cheesman - I specify software, direct AI to build it, and own the result. Looking for remote work in web development, digital operations, accessibility or nonprofit technology.

**⚠ FLAG.** The `<title>` is just your name. A recruiter with eleven tabs open sees
only "Thomas Cheesman" and nothing about what you do. Also, there are no Open Graph
tags anywhere on the site — when you paste tc-ventures.ca into LinkedIn, an email,
or a message to a hiring manager, it renders as a bare grey link with no title,
description or image. For a site whose entire job is being sent to people, that is
the single cheapest fix available.

### H2 — hero

> Grande Prairie, Alberta · remote
>
> # Thomas Cheesman
>
> I specify software precisely, direct AI to build it, and own everything that comes out the other end — the design calls, the evidence rules, the physics, and the mistakes.

### H3 — hero, second paragraph

> Seventeen years running kitchens, then a career change. In about eighteen months I have shipped three live sites and a research application that maps **3,632** official statistical reports and the documented dependencies between them. I am looking for remote work in web development, digital operations, accessibility, or nonprofit technology.

**⚠ FLAG — factual conflict.** "In about eighteen months" contradicts two other
places on the site: block H6 says the three WordPress sites have been "Running since
2023", and B11 dates your GPRS board seat to June 2023. If the sites went live in
2023 that is roughly three years, not eighteen months. One of these numbers is
wrong and a careful reader will catch it. Which is right?

### H4 — call to action buttons

> See the projects   ·   Email me

### H5 — section heading

> ## Three things I have built

### H6 — proof card 1

> ### The Economic Report Influence Graph
>
> A browser-based 3D map of where official numbers come from: which published report is calculated from which other report, across more than a hundred countries. Every line has to be backed by a quotable sentence in a real document, or it does not get drawn.
>
> **Scale** — 3,632 reports · 3,272 dependencies
> **Built with** — TypeScript, React, Three.js · ~24,700 lines

**⚠ FLAG — minor.** "~24,700 lines" is the only vanity metric on the site. Line
count is the one software number that experienced readers actively distrust, because
it measures volume, not quality. Everything else in this card is a real claim. Worth
considering whether it earns its place.

### H7 — proof card 2

> ### Rocket Lander
>
> A rocket that falls belly-down through layered wind, flips, burns, and has to land on a drifting droneship. Real aerodynamics rather than arcade physics — and the tuning knobs are the interface, so a child learns the forces by flying against them.
>
> **Built with** — Godot 4.7 · GDScript · Jolt physics
> **Status** — Flies; landing it is the hard part

### H8 — proof card 3

> ### Three live WordPress sites
>
> Custom Astra child themes, written and maintained solo: bareyourrare.org for rare-disease patients, gpresidentialsociety.com for a volunteer-run nonprofit providing 87 units of barrier-free housing, and thomascheesman.ca. Accessibility and plain language are requirements on all three, not polish applied at the end.
>
> **Built with** — PHP, CSS, JavaScript, WordPress
> **Running since** — 2023

**⚠ FLAG.** "87 units" is a specific, checkable claim about someone else's
organisation, on which you sit as a board member. Confirm the number is current.

### H9 — "How I work", item one

> **One — Specify before building**
>
> The specification is the work. I decide what "good" means, write the standard down where the next person can find it, and hold every change to it. My repositories carry protocols and playbooks because a standard that only lives in someone's head drifts within a week.

### H10 — "How I work", item two

> **Two — Evidence over assertion**
>
> On the influence graph the rule is *no document, no edge*: a dependency exists only if a published source says so in words I can quote. Leads I cannot source go to a dropped list with a reason. Every drawn line carries a grade for how well its citation actually supports it, and the grade is visible in the app.

### H11 — "How I work", item three

> **Three — Verify by measuring**
>
> I check work against a clean rig rather than trusting that it looks right. A layout force I had already shipped turned out to have been calibrated against a measurement script with a bug in it. I found that, threw out the calibration, and rebuilt it.

**⚠ FLAG — deliberate risk, your call.** This paragraph tells a hiring manager, on
your home page, that you shipped something built on a broken measurement. I think
it is the most credible paragraph on the site — almost nobody volunteers a mistake,
and catching your own bad calibration is exactly the signal you want to send. But
it is a choice, not an accident, and a minority of readers will only see "shipped
a bug." Confirm you want it.

### H12 — what I am looking for

> ## What I am looking for
>
> Remote work in web development, digital operations, accessibility, or nonprofit technology. I am most useful where a small product needs someone to own it end to end — deciding what it should be, building it, and being accountable for whether it actually works.
>
> I am comfortable being the only person on a thing, and comfortable being the one who says a result is not good enough yet. Available now. More about the route I took here.

**⚠ FLAG.** "Available now" appears here and in the footer of all four pages — five
times total. It is true today. It is a claim with a shelf life, and a stale
"available now" on a portfolio reads worse than no availability statement at all.
See Q1.

---

# PART 2 — projects.html

### P1 — page title and meta

> **Title:** Projects - Thomas Cheesman
> **Description:** The Economic Report Influence Graph, Rocket Lander, and three live WordPress sites - what they are, what was hard, and what I got wrong.

### P2 — page head

> Work
> # Projects
> Two built in the open, in detail — what they are, what was hard, and what I got wrong.

**⚠ FLAG — minor.** "Two built in the open" then the page shows three things (graph,
rocket, and the WordPress sites section). Reads like a miscount.

### P3 — graph, status label

> In active development · TypeScript, React, Three.js

### P4 — graph, opening

> ## The Economic Report Influence Graph
>
> Every important number in public life — inflation, a disability payment, how much your city gets for road repair — is calculated from some other number, which was calculated from another, back to a handful of foundational statistical releases. Almost nobody can see that structure, including the people who depend on it.
>
> This draws it. Each sphere is a real published report, each line a documented dependency between two of them, and a report's size is how much everything else rests on it. It runs in a browser, in 3D, with no backend.

This is the best writing on the site. It explains a genuinely abstract project to a
non-specialist in two paragraphs without dumbing it down.

### P5 — figure caption 1

> Everything at once. Colour is which system publishes — reds Canada, blues the United States, greens the European Union, violets Africa and the international bodies.

### P6 — the rule

> ### The rule the whole project runs on
>
> *No document, no edge.* A line is drawn only if a published document says, in words I can quote, that one report uses the other as an input. Leads I cannot source go to a dropped list with a reason attached. Every existing line has since been graded on how well its cited document actually supports it — 1,256 A, 1,404 B, 612 C — and the grade is visible in the app, because a map that hides its own weak spots is worse than no map.

**Arithmetic checks out:** 1,256 + 1,404 + 612 = 3,272, which matches the dependency
count exactly, and 1,256/3,272 = 38.4%. Nothing to fix. Flagging it only so you know
I checked.

**⚠ FLAG — strategic.** Publishing your own grade distribution is the most unusual
idea on this site and I would fight to keep it. But be aware what a hostile reader
does with it: 38.4% A means 61.6% *not* A, and someone looking for a reason to pass
can quote that back at you. The defence is in the sentence already ("a map that
hides its own weak spots is worse than no map"). I think you win that exchange. Your
call whether you want to have it at all.

### P7 — what's hard

> ### What is actually hard about it
>
> Not the 3D. The hard part is holding one standard across eighty-odd research sessions without drift, which is why the repository carries a fixed extraction protocol, two lane playbooks and exactly one handoff file rather than a pile of notes — and why a validator runs on every data change and refuses to pass on a dangling reference.
>
> The other hard part is drawing 3,600 nodes without lying. Cluster spacing, node size scaling and camera framing all change what a viewer believes about the data, so each is measured rather than eyeballed.

### P8 — figure caption 2

> Filtered to national-tier reports. Sphere size is weighted authority — how much of everything else traces back through that one release.

### P9 — graph spec table

> **Corpus** — 3,632 reports · 3,272 documented dependencies
> **Evidence grades** — 1,256 A · 1,404 B · 612 C — 38.4% A-share
> **Coverage** — 130+ countries; national, state, municipal and institutional tiers
> **Code** — ~24,700 lines of TypeScript across 50 source files
> **Stack** — Vite · React · three-forcegraph · d3-force-3d · no backend
>
> Source: github.com/DriftingSplash9/Reports-Clustering

**⚠ FLAG — check this yourself before anything else on this page.** The repo link is
public and the site invites people to click it. Two things to verify: (a) that the
repo is actually public and not private — a dead link here is worse than no link;
(b) that what a visitor finds there matches what this page claims. If the public
repo still holds the ~302-report data, the page says 3,632 and the repo says 302.

### P10 — rocket, status label

> Flying, not yet landable · Godot 4.7, GDScript

**⚠ FLAG.** This is the first thing a skimmer reads about your second project, and it
leads with what it cannot do. Contrast with the home page's version of the same
status — "Flies; landing it is the hard part" — which carries identical information
and reads as confidence rather than apology. I would use the home page's framing in
both places.

### P11 — rocket, opening

> ## Rocket Lander
>
> Land a rocket, gently, with the fuel you were given. It falls belly-down through layered, gusting wind, flips, burns, and has to sit down on a droneship that is bobbing on swell and drifting away from you. A run lasts twenty to sixty seconds. Failure is instant and obviously your own fault.
>
> The teaching idea came first: the tuning knobs *are* the interface, so a nine-to-twelve-year-old learns the physics by flying against it rather than reading about it. There are 38 of them behind one key — gravity, thrust, gimbal authority, drag, wind, fuel, pad tolerances — and the panel builds itself from a spec table, so adding a knob is one variable and one row.

### P12 — three things the build taught me

> **Thrust from the tail does nothing on its own.** A nozzle pointing down the body axis pushes straight through the centre of mass and produces no torque — which is exactly why a real rocket's engine being at the bottom does not tip it over. Gimballing the nozzle is what makes it steer.
>
> **Drag had to be split in two.** Along-hull and across-hull flow are dragged separately, and across is about twelve times along. That split is the entire reason the belly-flop is worth doing: tilting off broadside produces lift, and that glide is the only way to reach a barge that is not directly beneath you.
>
> **A restoring force without a damper is a pendulum.** The weathervane moment that settles the ship belly-down is a spring; with no aerodynamic damper against it, the ship swings forever. Easy to forget, extremely obvious the moment it is missing.

### P13 — where it is

> ### Where it is
>
> It flies. Landing it is brutally hard — which is the direction, not the bug: real physics and real logic, difficult but winnable, the way the actual thing is difficult but winnable. What is left is tuning and time.

### P14 — rocket spec table

> **Engine** — Godot 4.7.1 · GDScript · Jolt physics
> **Flight model** — Gimballed thrust, weak RCS, four hinged flaps, finite fuel
> **Weather** — Density falling with altitude; wandering wind layers, out-of-phase gusts
> **Tuning** — 38 live knobs, spec-driven panel, presets saved to disk
> **Numbers** — Terminal 61 m/s flat · flip committed by 300 m · landing costs half the tank

**⚠ FLAG — minor.** Rocket Lander has no source link, while the graph does. A reader
who just read three paragraphs of real physics will want to look. If the repo is
private or the code is not in a state you want read, that is a fine answer — but the
asymmetry is noticeable.

### P15 — the three sites

> ## And three live sites
>
> Custom WordPress child themes on the Astra parent, written and maintained solo. **Bare Your Rare** is a patient-led site for ultra-rare conditions, built because most people searching for one of them find almost nothing. **The Grande Prairie Residential Society** site serves a volunteer-run nonprofit providing 87 units of barrier-free housing — accessibility and plain language are first-order requirements there, not decoration. **thomascheesman.ca** is the personal one, and the place I try things that are too strange for a client site.

**⚠ FLAG — small but real.** "the place I try things that are too strange for a client
site" invites a hiring manager to go and look at thomascheesman.ca, which is your
personal and family site — heritage archive, kids, pinball game. You built this
domain specifically to keep those apart. This one sentence is the door between them,
and it's phrased as an invitation.

---

# PART 3 — background.html

### B1 — page title and meta

> **Title:** Background - Thomas Cheesman
> **Description:** Seventeen years in professional kitchens, then a career change. Experience, skills, education and resume.

### B2 — page head

> About
> # Background
> Seventeen years in professional kitchens, then a career change that was not optional.

**⚠ FLAG — health disclosure, 1 of 3.** "not optional" is the first hint of the
medical reason, in the page's opening line, in large type. It does not name anything,
but it sets up B4 two paragraphs later. If you decide to remove the disclosure
entirely this line changes too.

### B3 — kitchens

> I cooked from 2002 to 2019 — line cook to kitchen manager and executive chef, including a semester teaching culinary coursework in the Hospitality and Tourism diploma at what was then GPRC. What I actually did all day was run an operation: budgets, purchasing, suppliers, scheduling, and the custom Excel systems I built to keep cost, ordering and waste under control.

### B4 — the career change

> I left the line in 2019 when a connective-tissue condition made kitchen work unsustainable. I spent the next years on family care and self-directed study, and then started building and shipping things in public. The useful half of the kitchen years transferred intact: decide what good means, write the standard down, and hold every plate that leaves to it.

**⚠ FLAG — health disclosure, 2 of 3. This is §4 item 2 and it is the single decision
I most need from you.** An agent decided, on your behalf and without asking, to put
a medical condition on your hiring-facing site in an unnamed, generic form. There are
three defensible options and they are genuinely different:

1. **Name it.** "Hajdu-Cheney syndrome." You already name it publicly elsewhere, you
   run a rare-disease advocacy site, and a named condition is a fact rather than a
   shadow. A reader can look it up and stop speculating.
2. **Keep it unnamed** as it is now — signals "there is a medical reason" without
   detail. My honest view: this is the weakest of the three. It raises the question
   and refuses to answer it, which is exactly the space a nervous hiring manager
   fills in badly.
3. **Say nothing medical at all.** "I left the line in 2019 and moved into family
   care and self-directed study." A career change needs no justification, and you
   are under no obligation to disclose anything to a stranger deciding whether to
   interview you.

This is yours to decide and I have no business defaulting it. Q7 below asks it
directly.

### B5 — what I do now

> What I do now is specify software and direct AI to build it — which is a real skill with real failure modes, and the difference between a working result and a plausible-looking one is entirely in the specifying, the reviewing and the refusing to ship. The code is written with assistance. The design calls, the evidence rules and the judgement about what is good enough are mine, and so are the mistakes.

**⚠ FLAG — the biggest strategic call on the site, bigger than the health one.**
"The code is written with assistance," stated plainly, on the page a hiring manager
reads to decide about you. Two populations read that sentence in opposite directions:
one sees an honest practitioner of how software is actually built in 2026; the other
stops reading and files you as someone who does not write code. You cannot have both
readers. The current copy chose the first, deliberately and without asking you.
I think it chose right — and it is still your call, not its. See Q8.

### B6 — skills, Web

> **Web** — HTML, CSS, JavaScript, TypeScript, PHP, WordPress child themes, accessible UI, Git and GitHub

### B7 — skills, AI-assisted building

> **AI-assisted building** — Specify, review, debug and ship; prompt and protocol design; editorial control over generated code; keeping a standard across long multi-session work

### B8 — skills, Data & operations

> **Data & operations** — Custom Excel systems for inventory, sales, scheduling and budget tracking; research extraction with strict sourcing rules

### B9 — skills, Leadership

> **Leadership** — Kitchen management, remote supplier coordination, nonprofit board work, disability advocacy

**⚠ FLAG — health disclosure, 3 of 3, and easy to miss.** "disability advocacy" is a
disclosure by implication, sitting in a skills list where nobody is looking for one.
If you choose option 3 on B4 and remove the medical reference, this line quietly
puts it back. It may well be a credential you want to claim — Bare Your Rare is real
work — but it should be a decision, not a leftover.

### B10 — skills, Writing

> **Writing** — Plain language for people who did not come for the jargon — patient-facing, nonprofit and technical documentation

### B11 — experience, GPRS

> **June 2023 – present**
> ### Board Member — Grande Prairie Residential Society
> Own the public website; contribute to outreach, planning and governance for accessible housing, including through the post-fire rebuild of Margaret Edgson Manor.

**⚠ FLAG.** Two things. First, "Own the public website" — you are a non-executive
board member; confirm that is how the board would describe your role, since this is
public and attached to their name. Second, the Margaret Edgson Manor fire is a real
event involving real residents. Using it as a line on your own CV is defensible
(you did the work) but worth a conscious look at the phrasing.

### B12 — experience, caregiver

> **March – December 2023**
> ### Caregiver — private client, Grande Prairie
> Daily schedules, dietary tracking, appointments and medication timing.

**⚠ FLAG — inconsistency.** B4 says "family care." This says "private client." If
this is the same work, a reader who notices sees either an inflated job title or two
different jobs. Pick one framing and use it in both places. ("Private client" is
the more professional-sounding of the two and also the less accurate one, if it was
family.)

### B13 — experience, kitchens

> **February 2002 – March 2019**
> ### Kitchen Manager / Executive Chef — hospitality operations, Alberta
> Including Ric's Grill, and instruction at GPRC (now Northwestern Polytechnic). Led kitchen teams, owned budgets and purchasing, coordinated suppliers remotely, and built the inventory and sales tracking systems the operation ran on.

### B14 — education and tickets

> **Journeyman Chef** — SAIT, 2012
> **B.Sc. Prepharmacy** — Credits toward, 1999–2002
> **Self-directed** — freeCodeCamp and related, plus daily AI-assisted build practice on live sites
> **Also held** — Power Engineering 3B and 4th Class · Gas Plant Operator Level 2

**⚠ FLAG.** Three separate things here:
- "B.Sc. Prepharmacy — Credits toward" is an unfinished degree listed as education.
  Honest, and some readers count it as a negative signal. Your call.
- "Also held" reads as "these have expired." If they have, that is fine but say it
  plainly; if they are current, "Also held" undersells them.
- Power Engineering and Gas Plant Operator tickets on a web-development portfolio
  raise a question rather than answer one. They do show a pattern of getting
  certified in technical fields, which is a real argument for keeping them — but
  right now they sit there unexplained.

### B15 — résumé download button

> Download my résumé   ·   Email me
> (links to `/assets/Thomas-Cheesman-Resume.docx`)

**⚠ FLAG — fix regardless of anything else.** This is a `.docx`. Corporate mail
gateways and some browsers treat Word documents as a mild risk, phones render them
badly, and formatting shifts between Word versions — so the document a hiring
manager sees may not be the one you laid out. PDF is the expected format for a
résumé everywhere. I can convert it; the only question is whether the .docx should
stay alongside it for people who want to paste from it.

### B16 — practicalities

> ## Practicalities
>
> Based in Grande Prairie, Alberta. Work is remote-capable and I am available now. I am happy to talk about accommodations; they are straightforward and have not stopped me shipping anything on this site.

**⚠ FLAG.** "I am happy to talk about accommodations" is a fourth disclosure, and
the most consequential one, because it is the one that touches hiring law and
employer nervousness directly. The second half of the sentence does good work
("straightforward", "have not stopped me shipping anything on this site"). But
volunteering the topic before anyone has asked, on a public page, is a strategic
choice — in most hiring advice the answer is to raise accommodations after an offer,
not before an introduction. Strong candidate for CUT even if you keep B4.

Also note this page does not mention your time zone, which the brief correctly
identifies as a real hesitation for remote hires. That belongs on the contact page.

---

# PART 4 — site-wide

### S1 — the footer (identical on all four pages)

> **Get in touch**
> thomasmcheesman@gmail.com
> Grande Prairie, Alberta · remote-capable · available now
>
> **Elsewhere**
> github.com/DriftingSplash9
> thomascheesman.ca — personal
> bareyourrare.org
> gpresidentialsociety.com

**⚠ FLAG.** "personal" next to thomascheesman.ca is doing the right job — it warns
a professional reader what they are clicking. Combined with P15's "too strange for a
client site" though, the family site is linked from every single page of the hiring
site. Deliberate, or drift?

### S2 — primary nav (all four pages)

> Thomas Cheesman   |   Projects   ·   Background   ·   Contact

**⚠ FLAG.** "Contact" is a `mailto:` link, not a page. Clicking it fires the
visitor's email client at them unannounced, which on a work machine often means
Outlook opening cold, and on a phone can mean nothing visible happening at all. This
is the exact "lame afterthought" from your brief, sitting in the nav of every page.
It is what the contact page fixes.

### S3 — 404 page

> 404
> # That page is not here
> The link is wrong, or the page has moved.
> Back to the start   ·   See the projects

Fine. Note the footer's "available now" appears here too, so a stale availability
claim would live on the error page as well.

### S4 — things absent from every page

- **No Open Graph / Twitter card tags.** Link previews render blank. See H1.
- **No favicon.** Browser tab shows a default page icon.
- **No `robots.txt`, no `sitemap.xml`.** Minor for four pages.
- **No time zone stated anywhere**, despite remote work being the ask.
- **No indication of what happens after someone emails you.** The brief's central
  point about contact pages.
- **Fonts load from Google Fonts** on every page, which is a third-party request
  before your text renders, and a privacy note some organisations care about.
  Self-hosting three font files removes an external dependency and speeds up first
  paint. Low priority, genuinely easy.

---

# PART 5 — the three conflicts I found

Listed separately because each needs one answer from you, not a copy edit.

| # | Conflict | Where |
|---|---|---|
| X1 | "about eighteen months" of shipping vs. sites "Running since 2023" vs. board seat from June 2023 | H3 / H8 / B11 |
| X2 | "family care" vs. "Caregiver — private client" for what looks like the same 2023 work | B4 / B12 |
| X3 | Site claims a 3,632-report corpus; the deployed graph bundle on thomascheesman.ca holds ~302, and the public repo may too | H3, H6, P9 vs. handoff §4 item 8 |

X3 matters most, because the graph is both your strongest claim and the intended
basis of the "wow". If the number on the page and the number a visitor can reach
disagree, the evidence-discipline argument — which is the whole positioning of this
site — takes the damage.

---

# PART 6 — questions I need answered

**Q1 — "Available now."** Five instances. Keep as-is, soften to "open to work", or
cut? And if you keep it: this is a claim that rots. Do you want me to put a dated
line on it instead ("Available — last updated September 2026") so it degrades
honestly rather than silently?

**Q2 — The eighteen months.** X1. What is the real figure, and which date do you
want to count from?

**Q3 — The résumé.** Convert to PDF (yes/no), and keep the .docx alongside it
(yes/no)?

**Q4 — Rocket Lander source link.** Is there a public repo? If yes I'll add it. If
the code isn't in a state you want read, say so and I'll leave it.

**Q5 — Reports-Clustering repo.** Is it public right now, and does the data in it
match the 3,632 figure? I can check if you want, but you'll know faster than I will.

**Q6 — thomascheesman.ca.** Should the hiring site link to the family site at all?
Options: keep it as-is (footer on every page + the P15 invitation), keep the footer
link but cut the P15 sentence, or drop it entirely.

**Q7 — The health disclosure.** B4, and the knock-on decisions in B2, B9 and B16.
Name it / keep it unnamed / remove it entirely. And separately: does B16
("happy to talk about accommodations") stay?

**Q8 — "The code is written with assistance."** B5, and the same framing in H2, H3,
B7. This positions the whole site. Keep it explicit, soften it, or restructure so
the work leads and the method is mentioned further down? I have a view — keep it
explicit — but it is a strategic bet on which kind of employer you want to attract,
and you should place that bet yourself.

**Q9 — Anything in here that is simply wrong about you?** The whole document exists
because an agent wrote confident sentences in your voice. Factual errors matter more
than style.

---

# PART 7 — questions about the "wow"

These do not block the contact page. Answer when you have a view.

**W1 — Which of the two candidates?**
- **(a) The graph, live and interactive.** Strongest, hardest, and the thing you have
  actually built. Blocked on the corpus rebuild (X3).
- **(b) The evidence grading, made visible.** A portfolio that visibly grades its own
  claims — every assertion on the site carrying an A/B/C and a source you can open.
  Cheaper, stranger, entirely unique, and it makes the *method* the wow rather than
  the artefact. No dependency on the graph rebuild.

The brief says pick one and execute to an unreasonable standard. My instinct is (b)
is the better site and (a) is the better demo. Which matters more to you?

**W2 — If the graph: full corpus or a hero subgraph?** 3,600 nodes is a lot to ask of
a phone. A curated 150-node subgraph — say, one country's dependency chain traced to
its foundational releases — loads instantly, is legible, tells a story, and a "open
the full graph" link handles the people who want scale.

**W3 — Does the wow live on the home page or its own page?** Home page means every
visitor sees it and every visitor pays for it. Its own `/graph` page means only
interested people load it, and the home page stays the fast, calm document it is now.

**W4 — Do you want to keep the current visual design?** The brief says I may argue
for changing it but not change it silently. I am not going to argue: the paper-white
document look is the right call for a hiring site, it contrasts properly with the
family site, and calm-plus-one-extraordinary-moment is a stronger composition than
maximalism everywhere. Confirm and I'll stop raising it.

**W5 — The form question.** I recommend no form: on this stack a form means adding a
Worker script, which turns "files on a CDN" into "an application" permanently, and
a form is the least trustworthy element on any contact page anyway. Confirm and I'll
build the contact page around better answers instead of a better input box.

