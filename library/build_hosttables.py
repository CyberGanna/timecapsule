# Builds help/live-pages/hosttables.html ("Gregory's tables": a host's live, upcoming and past tables, seen by someone else)
# from the My tables page shell. Linked from "See all" in the profile's Tables tab. Run: python3 library/build_hosttables.py (build.py runs it too)
import re, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from data import R, TX, TOPIC_COL
MON = {m: i for i, m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(), 1)}
MONTH = 'January February March April May June July August September October November December'.split()

def past():
    out = []
    for rid, top, sub, title, rounds, priv, outn in R:
        if priv: continue  # private tables are never shown to other people
        for k, (d, n) in enumerate(rounds):
            wd, day, mon = d.split(); names = TX[rid][min(k, len(TX[rid]) - 1)]['names']
            out.append(dict(id=rid, topic=top, title=title, col=TOPIC_COL[top], round=k + 1, people=n, names=names,
                            wd=wd, day=int(day), mon=mon, month=MONTH[MON[mon] - 1], key=MON[mon] * 100 + int(day), saved=k == len(rounds) - 1))
    out.sort(key=lambda r: -r['key'])
    return out

def upcoming():
    return [dict(id='free-will', live=True, since='41 min in', topic='Philosophy', title='Is free will an illusion?', col=TOPIC_COL['Philosophy'], round=4, people=6,
                 names=['Gregory', 'Lena', 'Tom', 'Ana', 'Nikos', 'Gabriele'], free=2),
            dict(id='faith', live=False, wd='Tue', day=24, mon='Nov', time='19:00', topic='Religion', title='Is faith a choice?', col=TOPIC_COL['Religion'], round=2, people=3,
                 names=['Gregory', 'Ines', 'Maya'], free=5)]

def load_dict(path):
    D = {}
    for ln in open(path, encoding='utf8'):
        if ln.strip(): p = ln.rstrip('\n').split('|'); D[p[0]] = p[1:]
    return D

def build():
    s = open(os.path.join(ROOT, 'help/live-pages/mytables.html'), encoding='utf8').read()
    helpers = re.search(r'\nconst HAIR=.*?\nconst P=.*?\nfunction av\(n\).*?\n', s, re.S).group(0)
    head = s[:s.index('<div class="wrap">\n  <section class="hero">')]
    foot = s[s.index('<style id="tcf-css">'):s.index('<style id="tce-css">')] + s[s.index('<footer class="tcf"'):]
    head = re.sub(r'<title>[^<]*</title>', "<title>TimeCapsule Gregory's tables</title>", head, count=1)
    if '<meta name="viewport"' not in head[:2000]:
        head = '<!doctype html>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + head
    head = head.replace('<a href="#" data-tch="noop" aria-current="page" style="color:var(--tch-teal)">My tables</a>', '<a href="mytables.html" target="_top">My tables</a>')
    head = head.replace('Search my tables', 'Search tables')
    D1 = load_dict(os.path.join(HERE, 'dict-hosttables.txt')); DE = load_dict(os.path.join(HERE, 'dict-hosttables-el.txt'))
    m0 = re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n', head, re.S)
    D = json.loads(m0.group(1).replace('<\\/', '</'))
    for k, v in D1.items(): D[k] = v[:2] + [DE.get(k, [v[0]])[0]]
    head = head[:m0.start()] + '<script id="tc-i18n">window.TCI18N_DICT=' + json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n' + head[m0.end():]
    body = open(os.path.join(HERE, 'hosttables-body.html'), encoding='utf8').read()
    body = body.replace('/*UP*/null', json.dumps(upcoming(), ensure_ascii=False)).replace('/*PAST*/null', json.dumps(past(), ensure_ascii=False)).replace('/*HELPERS*/', helpers)
    out = os.path.join(ROOT, 'help/live-pages/hosttables.html')
    open(out, 'w', encoding='utf8').write(head + body + foot)
    subprocess.run(['python3', os.path.join(ROOT, 'i18n/add-greek.py'), out], check=True)
    return out, len(past())

if __name__ == '__main__':
    print(build())
