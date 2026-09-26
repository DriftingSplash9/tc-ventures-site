"""byr_bot_check.py — does bareyourrare.org answer AI agents, cached and uncached?

Usage: python byr_bot_check.py GAP_SECONDS N_REQUESTS bust|nobust

Cycles seven user-agents (a browser, curl, and five AI crawlers/agents by their
published user-agent strings) over eight paths, one request every GAP seconds.
"bust" adds a unique query string, which forces a LiteSpeed cache miss so the
request reaches WordPress at the origin; "nobust" fetches the plain URL.
Prints status, agent, path, LiteSpeed and Cloudflare cache headers, and the page
title, or BOTVERIFY when the origin served its reCAPTCHA "Bot Verification" page,
or NO CONNECTION (status 000) when the connection dropped before any answer.
BASE (env) points it at another site; PATHS are BYR's.

Limits: one network per run, and spoofed user-agents. A real crawler comes from
its own published IP ranges and may be treated differently. Keep GAP >= 6: the
origin's filter also trips on fast browser traffic.

First run 2026-09-25; results in Claude outputs/byr-bot-check-2026-09-25.md.
"""
import tempfile, os
BASE = os.environ.get("BASE", "https://bareyourrare.org")
OUT = os.path.join(tempfile.gettempdir(), "byr_bot_check.html")
import subprocess, time, re, sys, random
UAS = {
 "chrome": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
 "curl": "curl/8.5.0",
 "ClaudeBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)",
 "Claude-User": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +Claude-User@anthropic.com)",
 "GPTBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.2; +https://openai.com/gptbot",
 "ChatGPT-User": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot",
 "PerplexityBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
}
PATHS = ["/hcs-guide/", "/poems/", "/sps/", "/ecd/", "/fechtner/", "/about/", "/robots.txt", "/llms.txt"]
gap = float(sys.argv[1]); n = int(sys.argv[2]); bust = sys.argv[3] == "bust"
random.seed(1)
for i in range(n):
    ua = list(UAS)[i % len(UAS)]; p = PATHS[i % len(PATHS)]
    url = BASE + p + (f"?t={time.time_ns()}" if bust else "")
    if os.path.exists(OUT):
        os.remove(OUT)  # a dropped connection writes no body; never read the last one
    r = subprocess.run(["curl","-sS","-A",UAS[ua],"-D","-","-o",OUT,"-w","%{http_code}",url],capture_output=True,text=True)
    hdr = r.stdout.lower()
    code = r.stdout[-3:]
    ls = re.search(r"x-litespeed-cache: (\w+)", hdr); cf = re.search(r"cf-cache-status: (\w+)", hdr)
    body = open(OUT,encoding="utf-8",errors="replace").read() if os.path.exists(OUT) else ""
    t = re.search(r"<title>(.*?)</title>", body, re.S)
    print(f"{time.strftime('%H:%M:%S')} {code} {ua:13} {p:22} ls={ls.group(1) if ls else '-':5} cf={cf.group(1) if cf else '-':8} {('NO CONNECTION' if code == '000' else 'BOTVERIFY' if 'Bot Verification' in body else (t.group(1)[:30] if t else ''))}", flush=True)
    time.sleep(gap)
