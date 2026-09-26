# bareyourrare.org — do AI agents get through? (re-check, 2026-09-25)

**Why:** the 2026-09-20 crawl audit (`byr-crawl-audit.md` §1) found the host refusing automated
fetchers. handoff-011 recorded the move behind Cloudflare as the fix ("§1 (host blocking) is
fixed by O-10"). Before the Bare Your Rare case study says so, Thomas asked for it to be checked
(copy-review-004, BYR0).

**Method:** `scripts/byr_bot_check.py`. One request every 6–7 s from one cloud network, cycling
seven user-agents (a Chrome browser string, curl, and ClaudeBot, Claude-User, GPTBot,
ChatGPT-User and PerplexityBot by their published strings) over five condition guides, `/about/`,
`/robots.txt` and `/llms.txt`. Run A adds a unique query string to every URL, which forces a
LiteSpeed cache miss so the request reaches WordPress at the origin. Run B fetches the plain URLs.
Times are UTC.

**Limits:** one network, one evening, spoofed user-agents. A real crawler comes from its own
published IP ranges, and the origin may treat it differently. This shows what the origin does
with these user-agents through Cloudflare; it does not show what any real crawler received.

---

## Result

**Every cached page was served to every agent. Uncached requests from three AI agents were
refused at the origin, not by Cloudflare.**

Tally of runs A and B (42 requests), counted from the logs below:

| | 200 | 403 "Bot Verification" | 429, empty body |
|---|---|---|---|
| LiteSpeed cache hit | 16 | 0 | 0 |
| not a cache hit | 19 | 4 (Claude-User 2, PerplexityBot 2) | 3 (GPTBot 3) |

- **GPTBot:** 429 on all three uncached requests, and on a fourth fetched to read its headers.
  200 on all three cached ones.
- **Claude-User:** 403 on two of three uncached requests. **PerplexityBot:** 403 on two of four.
- **ClaudeBot and ChatGPT-User:** 200 every time. **Chrome and curl:** 200 every time at this pace.
- **Faster traffic trips it for a browser too.** Earlier the same evening, a Chrome user-agent
  fetching six guides back to back (each GET followed by a HEAD), with a cache-busting query,
  got the 403 on four of the six GETs.
- **Where it comes from:** the 429 carries `platform: hostinger`, `panel: hpanel` and
  `x-turbo-charged-by: LiteSpeed`. The 403 carries `x-turbo-charged-by: LiteSpeed` and serves
  LiteSpeed's reCAPTCHA page (`<title>Bot Verification</title>`, form `lsrecaptcha-form`). Both
  pass through Cloudflare with `cf-cache-status: DYNAMIC`. Cloudflare's bot settings do not reach
  this filter.

**What it means for a patient.** A page an assistant fetches on someone's behalf gets through if
LiteSpeed has it cached, and may not if it doesn't. A cache purge, the routine after a deploy on
this site, empties the cache and reopens the gap until the pages are fetched again.

**Not established:** what setting at Hostinger does this, or whether it can be turned off. The
audit's advice stands: ask Hostinger, naming the symptom (uncached requests from AI user-agents
get a 429 or a LiteSpeed reCAPTCHA 403 through Cloudflare).

---

## Raw logs

Columns: time, status, agent, path, LiteSpeed cache, Cloudflare cache, page title or BOTVERIFY.

**Run A** — 6 s gap, cache-busting query:

```
21:40:35 200 chrome        /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
21:40:43 200 curl          /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
21:40:50 200 ClaudeBot     /sps/                  ls=miss  cf=dynamic  Stiff Person Syndrome (SPS): S
21:40:57 200 Claude-User   /ecd/                  ls=miss  cf=dynamic  Erdheim-Chester Disease (ECD):
21:41:04 429 GPTBot        /fechtner/             ls=-     cf=dynamic  
21:41:11 200 ChatGPT-User  /about/                ls=-     cf=dynamic  About Bare Your Rare | Patient
21:41:18 200 PerplexityBot /robots.txt            ls=miss  cf=miss     
21:41:24 200 chrome        /llms.txt              ls=-     cf=dynamic  
21:41:32 200 curl          /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
21:41:39 200 ClaudeBot     /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
21:41:45 403 Claude-User   /sps/                  ls=-     cf=dynamic  BOTVERIFY
21:41:52 429 GPTBot        /ecd/                  ls=-     cf=dynamic  
21:41:59 200 ChatGPT-User  /fechtner/             ls=-     cf=dynamic  Fechtner Syndrome (MYH9-Relate
21:42:07 200 PerplexityBot /about/                ls=miss  cf=dynamic  About Bare Your Rare | Patient
21:42:13 200 chrome        /robots.txt            ls=miss  cf=miss     
21:42:20 200 curl          /llms.txt              ls=-     cf=dynamic  
21:42:27 200 ClaudeBot     /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
21:42:33 403 Claude-User   /poems/                ls=-     cf=dynamic  BOTVERIFY
21:42:40 429 GPTBot        /sps/                  ls=-     cf=dynamic  
21:42:47 200 ChatGPT-User  /ecd/                  ls=-     cf=dynamic  Erdheim-Chester Disease (ECD):
21:42:53 403 PerplexityBot /fechtner/             ls=-     cf=dynamic  BOTVERIFY
```

**Run B** — 6 s gap, plain URLs:

```
21:43:34 200 chrome        /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
21:43:40 200 curl          /poems/                ls=hit   cf=dynamic  POEMS Syndrome: Symptoms, Diag
21:43:47 200 ClaudeBot     /sps/                  ls=hit   cf=dynamic  Stiff Person Syndrome (SPS): S
21:43:53 200 Claude-User   /ecd/                  ls=hit   cf=dynamic  Erdheim-Chester Disease (ECD):
21:43:59 200 GPTBot        /fechtner/             ls=hit   cf=dynamic  Fechtner Syndrome (MYH9-Relate
21:44:07 200 ChatGPT-User  /about/                ls=-     cf=dynamic  About Bare Your Rare | Patient
21:44:13 200 PerplexityBot /robots.txt            ls=hit   cf=expired  
21:44:19 200 chrome        /llms.txt              ls=-     cf=dynamic  
21:44:25 200 curl          /hcs-guide/            ls=hit   cf=dynamic  Hajdu-Cheney Syndrome Symptoms
21:44:32 200 ClaudeBot     /poems/                ls=hit   cf=dynamic  POEMS Syndrome: Symptoms, Diag
21:44:38 200 Claude-User   /sps/                  ls=hit   cf=dynamic  Stiff Person Syndrome (SPS): S
21:44:44 200 GPTBot        /ecd/                  ls=hit   cf=dynamic  Erdheim-Chester Disease (ECD):
21:44:51 200 ChatGPT-User  /fechtner/             ls=hit   cf=dynamic  Fechtner Syndrome (MYH9-Relate
21:44:57 403 PerplexityBot /about/                ls=-     cf=dynamic  BOTVERIFY
21:45:03 200 chrome        /robots.txt            ls=hit   cf=hit      
21:45:10 200 curl          /llms.txt              ls=-     cf=dynamic  
21:45:16 200 ClaudeBot     /hcs-guide/            ls=hit   cf=dynamic  Hajdu-Cheney Syndrome Symptoms
21:45:22 200 Claude-User   /poems/                ls=hit   cf=dynamic  POEMS Syndrome: Symptoms, Diag
21:45:28 200 GPTBot        /sps/                  ls=hit   cf=dynamic  Stiff Person Syndrome (SPS): S
21:45:35 200 ChatGPT-User  /ecd/                  ls=hit   cf=dynamic  Erdheim-Chester Disease (ECD):
21:45:41 200 PerplexityBot /fechtner/             ls=hit   cf=dynamic  Fechtner Syndrome (MYH9-Relate
```

**GPTBot 429, headers** (fetched separately after run A; `date`, `cf-ray`, reporting headers
dropped):

```
HTTP/2 429 
content-length: 0
server: cloudflare
platform: hostinger
panel: hpanel
content-security-policy: upgrade-insecure-requests
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
referrer-policy: strict-origin-when-cross-origin
permissions-policy: geolocation=(), microphone=(), camera=()
x-turbo-charged-by: LiteSpeed
cf-cache-status: DYNAMIC
```

---

## Addendum — after the cache purge, the same night

Thomas purged the LiteSpeed cache after the `NGO` fix (`bareyr` `6e07481`). Right after that, a
Chrome user-agent fetched ten pages, one every 7 s, to re-check the schema. None of the pages
were cached yet. The output below is trimmed to the status and the LiteSpeed cache header; the
script's `botverify=1` is shown as "(Bot Verification)", and times weren't logged:

```
/ 200 x-litespeed-cache: miss
/poems/ 403  (Bot Verification)
/sps/ 200 x-litespeed-cache: miss
/ecd/ 403  (Bot Verification)
/fechtner/ 200 x-litespeed-cache: miss
/hajdu-cheney-syndrome/ 200 x-litespeed-cache: miss
/hcs-guide/ 200 x-litespeed-cache: miss
/about/ 200 x-litespeed-cache: miss
/llms.txt 200
/privacy/ 200 x-litespeed-cache: miss
```

`/poems/` and `/ecd/` both answered 200 on a retry 20 s later. So right after a purge, with
nothing cached, the filter also refused a browser user-agent at this pace, on 2 of 10 pages.

---

## Addendum 2 — after the Hostinger "LLM" toggle, and a control on GPRS (2026-09-26, UTC)

**Why:** Thomas turned off a toggle in the Hostinger plugin on bareyourrare.org (Tools, LLM
Optimization; the screenshot shows "Create LLMs.txt file" off). His other Hostinger sites have it off
and, as far as he'd seen, don't have the problem. He asked whether that fixed it.

**Result: it did not, and the control site has the same refusal.**

| | 200 | 403 "Bot Verification" | 429 | no connection |
|---|---|---|---|---|
| BYR, run C (after the toggle, cache-busting) | 17 | 2 (PerplexityBot 1, Chrome 1) | 3 (GPTBot 3) | 0 |
| GPRS, run G (toggle off, not behind Cloudflare, cache-busting) | 14 | 0 | 3 (GPTBot 3) | 4 (Claude-User 1, PerplexityBot 2, Chrome 1) |

- **GPTBot got a 429 on every uncached request on both sites.** GPRS has the toggle off, so the
  toggle isn't what refuses it. It looks account-wide, or at least the same on both.
- **GPRS sits straight on Hostinger, with no Cloudflare,** and some of its requests got no answer at
  all (status 000). That's the connection-drop symptom the 2026-09-20 audit found on both sites
  before BYR moved behind Cloudflare.
- **The toggle is still worth leaving off.** Hostinger's own note says switching "Create LLMs.txt"
  on "will replace" the existing `llms.txt`. BYR's is the hand-written one: 7,640 bytes, last
  modified 2026-04-19, still served as written.
- **Script bug found in this run (rule 3):** on a dropped connection the script printed the previous
  page's title, because it read the old body file. The 000 lines below show it. Fixed in
  `scripts/byr_bot_check.py` the same hour: it now deletes the body before each request and prints
  "NO CONNECTION". The script also takes `BASE` from the environment now. The GPRS run used a
  scratch copy with GPRS's paths.

**Run C, BYR** (6 s gap, cache-busting):

```
02:32:22
02:32:23 403 chrome        /hcs-guide/            ls=-     cf=dynamic  BOTVERIFY
02:32:31 200 curl          /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
02:32:38 200 ClaudeBot     /sps/                  ls=miss  cf=dynamic  Stiff Person Syndrome (SPS): S
02:32:45 200 Claude-User   /ecd/                  ls=miss  cf=dynamic  Erdheim-Chester Disease (ECD):
02:32:52 429 GPTBot        /fechtner/             ls=-     cf=dynamic  
02:32:59 200 ChatGPT-User  /about/                ls=-     cf=dynamic  About Bare Your Rare | Patient
02:33:05 200 PerplexityBot /robots.txt            ls=miss  cf=miss     
02:33:12 200 chrome        /llms.txt              ls=-     cf=dynamic  
02:33:19 200 curl          /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
02:33:26 200 ClaudeBot     /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
02:33:34 200 Claude-User   /sps/                  ls=miss  cf=dynamic  Stiff Person Syndrome (SPS): S
02:33:40 429 GPTBot        /ecd/                  ls=-     cf=dynamic  
02:33:47 200 ChatGPT-User  /fechtner/             ls=-     cf=dynamic  Fechtner Syndrome (MYH9-Relate
02:33:53 403 PerplexityBot /about/                ls=-     cf=dynamic  BOTVERIFY
02:34:00 200 chrome        /robots.txt            ls=miss  cf=miss     
02:34:06 200 curl          /llms.txt              ls=-     cf=dynamic  
02:34:13 200 ClaudeBot     /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
02:34:21 200 Claude-User   /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
02:34:27 429 GPTBot        /sps/                  ls=-     cf=dynamic  
02:34:34 200 ChatGPT-User  /ecd/                  ls=-     cf=dynamic  Erdheim-Chester Disease (ECD):
02:34:42 200 PerplexityBot /fechtner/             ls=miss  cf=dynamic  Fechtner Syndrome (MYH9-Relate
```

**Run G, GPRS** (6 s gap, cache-busting; the titles on the 000 lines are stale, see above):

```
02:34:53 200 chrome        /                      ls=miss  cf=-        Accessible Housing Grande Prai
02:35:00 200 curl          /apply/                ls=miss  cf=-        Apply For Accessible Housing |
02:35:06 200 ClaudeBot     /faq/                  ls=miss  cf=-        FAQ | GPRS Accessible Housing
02:35:23 000 Claude-User   /timeline/             ls=-     cf=-        FAQ | GPRS Accessible Housing
02:35:30 429 GPTBot        /accessibility/        ls=-     cf=-        
02:35:37 200 ChatGPT-User  /our-story/            ls=-     cf=-        Our Story — 38 Years Of Provid
02:35:54 000 PerplexityBot /robots.txt            ls=-     cf=-        Our Story — 38 Years Of Provid
02:36:11 000 chrome        /donate/               ls=-     cf=-        Our Story — 38 Years Of Provid
02:36:18 200 curl          /                      ls=miss  cf=-        Accessible Housing Grande Prai
02:36:25 200 ClaudeBot     /apply/                ls=miss  cf=-        Apply For Accessible Housing |
02:36:31 200 Claude-User   /faq/                  ls=miss  cf=-        FAQ | GPRS Accessible Housing
02:36:38 429 GPTBot        /timeline/             ls=-     cf=-        
02:36:44 200 ChatGPT-User  /accessibility/        ls=-     cf=-        Accessibility Statement | GP R
02:36:51 200 PerplexityBot /our-story/            ls=miss  cf=-        Our Story — 38 Years Of Provid
02:36:57 200 chrome        /robots.txt            ls=miss  cf=-        
02:37:04 200 curl          /donate/               ls=miss  cf=-        Donate — Support Accessible Ho
02:37:10 200 ClaudeBot     /                      ls=miss  cf=-        Accessible Housing Grande Prai
02:37:17 200 Claude-User   /apply/                ls=miss  cf=-        Apply For Accessible Housing |
02:37:23 429 GPTBot        /faq/                  ls=-     cf=-        
02:37:30 200 ChatGPT-User  /timeline/             ls=-     cf=-        GPRS Timeline — Accessible Hou
02:37:47 000 PerplexityBot /accessibility/        ls=-     cf=-        GPRS Timeline — Accessible Hou
```

---

## Addendum 3 — outside research, checked (2026-09-26)

Thomas ran a research prompt through an outside model. Its answer was checked here, not trusted:
each source was fetched, and each quote was searched for in the page text.

**Confirmed (page answered 200, quote found):**
- **LiteSpeed docs, https://docs.litespeedtech.com/lsws/recaptcha/**
  - CAPTCHA is a server-wide switch, and "Google and Bing bots are automatically whitelisted. You
    will need to add any other bots you wish to allow."
  - "deny will return a 403, and drop will drop the connection when Max Tries is reached".
  - It can be turned off per site with the rewrite flag `[E=verifycaptcha:off]`.
  - The `LsRecaptcha` directive "cannot be used in .htaccess"; it belongs in the virtual host
    configuration, which Hostinger customers can't reach.
- **LiteSpeed blog, 2019-03-18:** Allowed Robot Hits "is the number of visits allowed by a bot to
  the server per 10 seconds", and "The default is 3".
- **WordPress.org thread "my website showing bot verification":** a Hostinger support reply calls
  the page "a security measure to prevent automated access to your website". A moderator says "The
  message is generated by the LiteSpeed server component".
- **Hostinger KB, 429 errors behind Hostinger CDN:**
  - "The hosting server applies its own per-visitor limits through LiteSpeed Web Server".
  - "Search engine and AI crawlers are subject to the same DDoS protection as other visitors and
    are never limited at normal crawl rates."
- **Stonegate Web Security, 2026:** reports the same challenge for AI crawlers on a Hostinger
  site, and points to LiteSpeed's server-level reCAPTCHA. Two things matter here:
  - The line "can't be per-bot tuned on your plan" is quoted from Kodee, Hostinger's AI chatbot,
    and the article says so. It is not a Hostinger engineer.
  - Stonegate found the trigger was the requester's IP range, not the user-agent. Our tests varied
    the user-agent from one IP: GPTBot was refused and Chrome wasn't. Both can be true.
- **Micron21 KB (a different host), and the LiteSpeed forum:**
  - Micron21 gives `RewriteRule .* - [E=verifycaptcha:off]` at the top of `.htaccess`.
  - On the forum, a Hostinger customer says they can't reach LiteSpeed's admin (port 7080) and can
    only use `.htaccess`.

**Could not check from this network** (each answered 403 here; rule 7):
- the LowEndTalk thread
- both r/Hostinger threads (the reported injected `LsRecaptcha 100` / `verifycaptcha:drop`
  lines)
- the Cloudflare community thread
- the HostingAdvice article

Treat what they say as reports only.

**Re-checked here, the same day:**
- **thomascheesman.ca:** a cache-busted GPTBot request got a 429 with an empty body, through
  Hostinger's CDN (`x-hcdn-request-id` present). Chrome got 200.
- **tc-ventures.ca:** Cloudflare's edge answers the GPTBot and ClaudeBot user-agents with 403,
  body "Your request was blocked.", on `/` and `/work/gprs`. `/robots.txt` still answers 200.
  Claude-User, ChatGPT-User and Chrome all get 200. This is a separate block from Hostinger's, in
  that zone's Cloudflare settings.

**Next, Thomas's call:**
1. Read BYR's `.htaccess` for lines with `LsRecaptcha` or `verifycaptcha`.
2. Try the LiteSpeed-documented off-switch, limited to AI agents' user-agents.
3. Re-run `scripts/byr_bot_check.py`.
4. If the 429 remains, open a ticket with Hostinger.

---

## Addendum 4 — after the `.htaccess` off-switch (2026-09-26, UTC)

Thomas added this at the top of BYR's `.htaccess` (his paste):

```
<IfModule LiteSpeed>
RewriteEngine On
RewriteCond %{HTTP_USER_AGENT} (GPTBot|ChatGPT-User|OAI-SearchBot|ClaudeBot|Claude-User|Claude-SearchBot|PerplexityBot|Perplexity-User) [NC]
RewriteRule .* - [E=verifycaptcha:off]
</IfModule>
```

The site still served (home page 200). The same test was then re-run.

**Result: it did not stop either refusal.**
- **Run D** (the standard 21 requests, cache-busting, from 04:26:48 UTC):
  - GPTBot got a 429 on all three of its requests.
  - PerplexityBot got "Bot Verification" on `/about/` once out of three.
  - Everything else answered 200.
- **Run E** (PerplexityBot only, `/about/` cache-busted, every 8 s, 8 requests): 7 answered 200
  and 1 got "Bot Verification" (04:30:18).
- **The 403's headers don't carry `platform: hostinger` or `panel: hpanel`,** which the WordPress
  pages and the 429 do. It has only `x-turbo-charged-by: LiteSpeed`. So the challenge is answered
  by the web server before WordPress, and the `.htaccess` flag isn't overriding it.
- **Can't tell whether it cut the rate.** Before, PerplexityBot was refused about one uncached
  request in three. After, 2 of 11. The samples are too small to call it either way.

**Next:** Hostinger. The whitelist (LiteSpeed's "Bot White List") and the per-site override
(`LsRecaptcha 0`) are both in configuration only the host can reach, according to LiteSpeed's docs.
The block Thomas added is harmless and can stay, or come out. Either way it's recorded here.

Run D:

```
04:26:51 200 chrome        /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
04:26:58 200 curl          /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
04:27:05 200 ClaudeBot     /sps/                  ls=miss  cf=dynamic  Stiff Person Syndrome (SPS): S
04:27:12 200 Claude-User   /ecd/                  ls=miss  cf=dynamic  Erdheim-Chester Disease (ECD):
04:27:19 429 GPTBot        /fechtner/             ls=-     cf=dynamic  
04:27:26 200 ChatGPT-User  /about/                ls=-     cf=dynamic  About Bare Your Rare | Patient
04:27:32 200 PerplexityBot /robots.txt            ls=miss  cf=miss     
04:27:39 200 chrome        /llms.txt              ls=-     cf=dynamic  
04:27:46 200 curl          /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
04:27:53 200 ClaudeBot     /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
04:28:00 200 Claude-User   /sps/                  ls=miss  cf=dynamic  Stiff Person Syndrome (SPS): S
04:28:07 429 GPTBot        /ecd/                  ls=-     cf=dynamic  
04:28:14 200 ChatGPT-User  /fechtner/             ls=-     cf=dynamic  Fechtner Syndrome (MYH9-Relate
04:28:21 403 PerplexityBot /about/                ls=-     cf=dynamic  BOTVERIFY
04:28:28 200 chrome        /robots.txt            ls=miss  cf=miss     
04:28:34 200 curl          /llms.txt              ls=-     cf=dynamic  
04:28:41 200 ClaudeBot     /hcs-guide/            ls=miss  cf=dynamic  Hajdu-Cheney Syndrome Symptoms
04:28:48 200 Claude-User   /poems/                ls=miss  cf=dynamic  POEMS Syndrome: Symptoms, Diag
04:28:54 429 GPTBot        /sps/                  ls=-     cf=dynamic  
04:29:02 200 ChatGPT-User  /ecd/                  ls=-     cf=dynamic  Erdheim-Chester Disease (ECD):
04:29:09 200 PerplexityBot /fechtner/             ls=miss  cf=dynamic  Fechtner Syndrome (MYH9-Relate
```

Run E:

```
04:29:32 PerplexityBot /about/?bust 200
04:29:42 PerplexityBot /about/?bust 200
04:29:51 PerplexityBot /about/?bust 200
04:30:00 PerplexityBot /about/?bust 200
04:30:09 PerplexityBot /about/?bust 200
04:30:18 PerplexityBot /about/?bust 403 BOTVERIFY
04:30:27 PerplexityBot /about/?bust 200
04:30:36 PerplexityBot /about/?bust 200
```

Headers of the 04:30:18 403 (`date`, `cf-ray` and reporting headers dropped):

```
HTTP/2 403 
content-type: text/html
vary: Accept-Encoding
server: cloudflare
cache-control: no-cache,no-store,private
x-frame-options: SAMEORIGIN
x-turbo-charged-by: LiteSpeed
cf-cache-status: DYNAMIC
```

