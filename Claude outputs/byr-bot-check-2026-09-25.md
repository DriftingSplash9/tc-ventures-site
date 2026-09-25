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
