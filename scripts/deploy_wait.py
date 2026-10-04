"""deploy_wait.py — after a merge, wait for its deploy, then prove each changed file is live (INFRA-18).

Usage: python scripts/deploy_wait.py PR            (a merged pull request's number)
       python scripts/deploy_wait.py --sha SHA     (a merge commit on main)
       add --timeout MINUTES (default 15)

1. The gate: the PR is MERGED (gh pr view), and its merge commit is on origin/main. Being told a PR is
   merged isn't the same as it having landed (handoff trap).
2. The deploy: it polls the merge commit's check-run, "Workers Builds: tc-ventures-site", until it
   completes; anything but success fails. The Cloudflare bot's "Deployment successful" comment is never
   read: the bot says that for branch pushes too, and they don't reach the site (handoff trap).
3. The files: every file under public/ that the merge changed (its first parent to the merge commit),
   less what .assetsignore keeps off the site and the two files Cloudflare parses and never serves
   (_headers, _redirects: site_check.py --live checks those). Each is fetched, and:
     - changed: byte-identical to the merge commit's copy, and different from the first parent's (the
       pre-merge control: a match there would mean the old file is still served)
     - added: byte-identical to the merge commit's copy
     - deleted: answers 404
   Pages are fetched by their clean URL (/method, not /method.html), as the site links them.
   A file that isn't right yet is fetched again, up to TRIES times, WAIT seconds apart, and each retry is
   printed: on #46 (2026-10-02) two of seven new files answered 404 just after the check-run said success,
   and 200 a minute later.
   Each fetch carries a never-used query (?cb=), but don't count on it to bypass Cloudflare's cache: on
   these static files a never-used query still came back "CF-Cache-Status: HIT" (2026-10-02). The pre-merge
   control is what shows the file is new.

Exit 1 if anything fails; every FAIL line is printed again at the end, on stderr (checklog.py). Control (CLAUDE.md rule 3): run it on an older merge whose files have changed
again since, such as #40 (ledger column 029): it must fail, because the live file is newer.
Written 2026-10-01 for Phase 4 (copy-review-009 P4-B; Q-P4-7 A).
"""
import fnmatch, json, os, subprocess, sys, time, urllib.error, urllib.request
import checklog

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
REPO = "DriftingSplash9/tc-ventures-site"
SITE = "https://tc-ventures.ca"
CHECK_RUN = "Workers Builds: tc-ventures-site"
NOT_SERVED = {"public/_headers", "public/_redirects"}
# Cloudflare adds its analytics <script> to an HTML page unless the request's Accept is */* (found
# 2026-10-01: none, or text/html, gets it). curl sends */*, so it sees the file as committed; so does this.
HEADERS = {"User-Agent": "deploy_wait.py", "Accept": "*/*"}
TRIES, WAIT = 7, 10


def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, check=True).stdout


def git(*a):
    return sh("git", "-C", ROOT, *a)


def ignored(path):
    """True if public/.assetsignore keeps this public/ path off the site."""
    rel = path[len("public/"):]
    for line in git("show", "HEAD:public/.assetsignore").decode().splitlines():
        pat = line.strip()
        if not pat or pat.startswith("#"):
            continue
        if pat.endswith("/") and rel.startswith(pat):
            return True
        if fnmatch.fnmatch(rel, pat):
            return True
    return False


def url_for(path):
    rel = path[len("public/"):]
    if rel == "index.html":
        return "/"
    if rel.endswith(".html"):
        return "/" + rel[:-5]
    return "/" + rel


def fetch(url):
    """(status, body bytes), cache-busted, no compression asked for."""
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}cb={time.time_ns()}", headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = sys.argv[1:]
    timeout = 60 * float(args[args.index("--timeout") + 1]) if "--timeout" in args else 15 * 60
    results, failed = [], checklog.failed()
    def check(name, ok, detail=""):
        results.append(ok)
        line = ("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else "")
        if not ok:
            failed.append(line)
        print(line, flush=True)

    # 1. The gate
    if "--sha" in args:
        sha = args[args.index("--sha") + 1]
    else:
        nums = [a for a in args if a.isdigit()]
        if not nums:
            sys.exit(__doc__)
        pr = json.loads(sh("gh", "pr", "view", nums[0], "--repo", REPO, "--json", "state,mergeCommit"))
        check(f"#{nums[0]} is merged", pr["state"] == "MERGED", pr["state"])
        if pr["state"] != "MERGED":
            sys.exit(1)
        sha = pr["mergeCommit"]["oid"]
    git("fetch", "--quiet", "origin")
    sha = git("rev-parse", sha).decode().strip()
    on_main = subprocess.run(["git", "-C", ROOT, "merge-base", "--is-ancestor", sha, "origin/main"]).returncode == 0
    check(f"{sha[:7]} is on origin/main", on_main)
    if not on_main:
        sys.exit(1)
    pre = git("rev-parse", f"{sha}^1").decode().strip()

    # 2. The deploy
    start, seen = time.time(), None
    while True:
        runs = json.loads(sh("gh", "api", f"repos/{REPO}/commits/{sha}/check-runs"))["check_runs"]
        run = next((r for r in runs if r["name"] == CHECK_RUN), None)
        state = (run["status"], run["conclusion"]) if run else ("not started", None)
        if state != seen:
            print(f"  {CHECK_RUN}: {state[0]}" + (f", {state[1]}" if state[1] else ""), flush=True)
            seen = state
        if run and run["status"] == "completed":
            break
        if time.time() - start > timeout:
            check("deploy finished in time", False, f"still {state[0]} after {timeout / 60:.0f} min")
            sys.exit(1)
        time.sleep(20)
    check(f"deploy of {sha[:7]} succeeded", run["conclusion"] == "success",
          f"{run['conclusion']} at {run['completed_at']}")
    if run["conclusion"] != "success":
        sys.exit(1)

    # 3. The files
    changes = []
    for line in git("diff", "--no-renames", "--name-status", pre, sha, "--", "public/").decode().splitlines():
        status, path = line.split("\t", 1)
        if path in NOT_SERVED:
            print(f"  {path} changed: Cloudflare parses it and never serves it; run site_check.py --live")
            continue
        if ignored(path):
            continue
        changes.append((status, path))
    if not changes:
        print("  the merge changed no served file under public/; nothing to compare")
    for status, path in changes:
        url = url_for(path)
        want = None if status == "D" else git("show", f"{sha}:{path}")
        right = (lambda st, body: st == 404) if status == "D" else (lambda st, body: st == 200 and body == want)
        for attempt in range(1, TRIES + 1):
            st, body = fetch(SITE + url)
            if right(st, body) or attempt == TRIES:
                break
            print(f"  {url}: status {st}, not right yet; try {attempt + 1} of {TRIES} in {WAIT}s", flush=True)
            time.sleep(WAIT)
        if status == "D":
            check(f"deleted, now 404: {url}", st == 404, str(st))
            continue
        same = right(st, body)
        check(f"live is the merge's copy: {url}", same,
              ("" if attempt == 1 else f"on try {attempt}") if same else
              f"status {st}, {len(body)} bytes served, {len(want)} in {sha[:7]}, after {attempt} tries")
        if status == "M":
            before = git("show", f"{pre}:{path}")
            check(f"control, live is not the pre-merge copy: {url}", body != before)

    print(f"\n{sum(results)} of {len(results)} checks passed")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
