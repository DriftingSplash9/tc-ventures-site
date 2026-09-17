#!/usr/bin/env python3
"""
export-gp-budget.py  —  regenerate public/assets/gp-budget-graph.json

What this does
--------------
Walks the dependency closure UPWARD from `gp-budget` (the City of Grande
Prairie's budget report) through the Economic Report Influence Graph corpus,
and writes the nodes and edges the projects-page demo draws.

How to run it
-------------
    git clone --depth 1 https://github.com/DriftingSplash9/Reports-Clustering
    pip install json5
    python export-gp-budget.py /path/to/Reports-Clustering \
        public/assets/gp-budget-graph.json

Why it reads the data this way
------------------------------
The corpus is the research slices in `src/data/research/*.json` PLUS the seed
arrays in `src/data/reports.ts` and `src/data/dependencies.ts`. The repo's own
loader (`src/data/index.ts`) assembles those with tsx after `npm run gen`
writes `public/corpus-data.json`. That is the canonical path and is what the
validator uses. This script does the same join in Python instead — the slices
are plain JSON, and the two seed files are parsed with json5, which handles
the TypeScript object literals (unquoted keys, single quotes, trailing commas,
comments) without a Node toolchain. If the seed files ever stop being plain
literals, run the repo's own loader and feed it the same closure walk below.

Last run: 2026-09-16 — 54 reports, 76 dependencies, 22 A / 48 B / 6 C.
Those counts move as the corpus grows. They are NOT published on the site;
site copy rounds ("fifty-odd", "seventy-odd"). See handoff §3.

The `basis` clean-up
--------------------
`basis` is written for the corpus's own audit trail, so a handful of entries
open with a research-log prefix or trail off into how the PDF was fetched.
Neither belongs in a panel a hiring manager reads. This strips the prefix,
drops trailing sentences that are about retrieval rather than about what the
document says, and caps the rest at 520 characters with the source link left
underneath. It never rewrites a claim, and it never touches the grade.
"""
import collections
import json
import os
import re
import sys

ROOT_ID = 'gp-budget'

LOG = re.compile(r'^RESEARCHED\s+\d{4}-\d{2}-\d{2}\s*\([^)]*\)\.\s*')
CHATTER = re.compile(
    r'(\bcurl\b|pdftotext|HTTP \d{3}|\.md\b|notes/|\bThomas\b|minted this session|\bISBN\b)',
    re.I)


def sentences(text):
    return [p for p in re.split(r'(?<=[.!?])\s+(?=[`A-Z“"\'(])', text) if p.strip()]


def clean_basis(text, hard=520):
    text = LOG.sub('', text).strip()
    keep = []
    for s in sentences(text):
        if keep and CHATTER.search(s):
            break
        keep.append(s)
    text = ' '.join(keep).strip() or text
    text = text.replace('`', '')
    if len(text) > hard:
        text = text[:hard].rsplit(' ', 1)[0].rstrip(' ,;:—-') + '…'
    return text


def load_corpus(repo):
    import glob
    import json5

    data = os.path.join(repo, 'src', 'data')
    reports, deps = {}, []

    for path in glob.glob(os.path.join(data, 'research', '*.json')):
        if 'retired' in os.path.basename(path):
            continue
        slice_ = json.load(open(path, encoding='utf8'))
        for r in slice_.get('reports') or []:
            reports.setdefault(r['id'], r)
        deps.extend(slice_.get('dependencies') or [])

    for name, bucket in (('reports.ts', 'reports'), ('dependencies.ts', 'deps')):
        src = open(os.path.join(data, name), encoding='utf8').read()
        start = src.index('= [', src.index('export const'))
        arr = json5.loads(src[start + 2:].rstrip().rstrip(';'))
        if bucket == 'reports':
            for r in arr:
                reports.setdefault(r['id'], r)
        else:
            deps.extend(arr)

    return reports, deps


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else '.'
    out_path = sys.argv[2] if len(sys.argv) > 2 else 'gp-budget-graph.json'

    reports, deps = load_corpus(repo)

    outgoing = collections.defaultdict(list)
    global_in = collections.Counter()
    for e in deps:
        outgoing[e['source_report_id']].append(e)
        global_in[e['target_report_id']] += 1

    # Closure: everything gp-budget depends on, transitively.
    seen, stack, edges = {ROOT_ID}, [ROOT_ID], []
    while stack:
        n = stack.pop()
        for e in outgoing.get(n, []):
            edges.append(e)
            t = e['target_report_id']
            if t not in seen:
                seen.add(t)
                stack.append(t)

    # Hops from the budget, breadth-first. Not drawn yet; kept because any
    # future layering or staged reveal wants it and it is free here.
    depth, queue = {ROOT_ID: 0}, [ROOT_ID]
    while queue:
        n = queue.pop(0)
        for e in outgoing.get(n, []):
            t = e['target_report_id']
            if t not in depth:
                depth[t] = depth[n] + 1
                queue.append(t)

    missing = [n for n in seen if n not in reports]
    if missing:
        raise SystemExit('closure references reports with no record: %s' % missing)

    nodes = [{
        'id': n,
        'title': reports[n]['title'],
        'publisher': reports[n]['publisher'],
        'tier': reports[n].get('jurisdiction_level'),
        'region': reports[n].get('region'),
        'country': reports[n].get('country'),
        'url': reports[n].get('url'),
        'depth': depth[n],
        # `rests` is in-degree across the WHOLE corpus, not just this slice:
        # it is what the node's size means, and a report's authority is not a
        # property of the slice you happen to be looking at.
        'rests': global_in[n],
    } for n in sorted(seen)]

    links = [{
        'source': e['source_report_id'],
        'target': e['target_report_id'],
        'rel': e['relationship_type'],
        'grade': e['evidence_grade'],
        'basis': clean_basis(e['basis']),
        'url': e.get('evidence_url'),
    } for e in edges]

    blob = json.dumps({'root': ROOT_ID, 'nodes': nodes, 'links': links},
                      separators=(',', ':'), ensure_ascii=False)
    open(out_path, 'w', encoding='utf8').write(blob)

    grades = collections.Counter(l['grade'] for l in links)
    print('%d reports, %d dependencies, %s — %d bytes to %s'
          % (len(nodes), len(links),
             ' / '.join('%d %s' % (grades[g], g) for g in 'ABC'),
             len(blob), out_path))


if __name__ == '__main__':
    main()
