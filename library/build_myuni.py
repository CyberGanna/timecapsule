# Builds help/live-pages/myuniverse.html ("My universe": Readings + Discussions, avatar menu) from the My tables page shell.
# Run: python3 library/build_myuni.py (build.py runs it too)
import re, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from data import R, TX, TOPIC_COL

MON = {m: i for i, m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(), 1)}
MONTH = 'January February March April May June July August September October November December'.split()

def rows():
    out = []
    for rid, top, sub, title, rounds, priv, outn in R:
        d, n = rounds[-1]; wd, day, mon = d.split()
        names = TX[rid][-1]['names']
        ls = [l for l in TX[rid][-1]['tx'] if l[1]]; q = ([l for l in ls if l[1] not in ('Gabriele', 'Gregory')] or ls)[-1]
        out.append(dict(id=rid, topic=top, sub=sub, title=title, col=TOPIC_COL[top], private=priv,
                        rounds=len(rounds), people=n, names=names, wd=wd, day=int(day), mon=MON[mon],
                        month=MONTH[MON[mon]-1], mon3=mon, quote=[q[1], q[2]], key=MON[mon]*100+int(day)))
    out.sort(key=lambda r: -r['key'])
    return out

def readings():
    base = subprocess.run(['git', '-C', ROOT, 'show', 'f26a9a8:profile/timecapsule-profile.html'], capture_output=True, text=True, check=True).stdout
    js = re.search(r'var T=\[(.*?)\];\n', base, re.S).group(1)
    js = re.sub(r'([{,])\s*(n|c|b):', r'\1"\2":', js)
    return json.loads('[' + js + ']')

def load_dict(path, n):
    D = {}
    for ln in open(path, encoding='utf8'):
        if ln.strip():
            p = ln.rstrip('\n').split('|'); D[p[0]] = p[1:]
    return D

def build():
    src = os.path.join(ROOT, 'help/live-pages/mytables.html')
    s = open(src, encoding='utf8').read()
    # avatar helpers from the My tables script
    m = re.search(r'\nconst HAIR=.*?\nconst P=.*?\nfunction av\(n\).*?\n', s, re.S)
    helpers = m.group(0)
    # shell: everything up to the hero, plus footer
    head = s[:s.index('<div class="wrap">\n  <section class="hero">')]
    foot = s[s.index('<style id="tcf-css">'):s.index('<style id="tce-css">')] + s[s.index('<footer class="tcf"'):]
    head = head.replace('<title>TimeCapsule My tables</title>', '<title>TimeCapsule My universe</title>')
    head = re.sub(r'<title>[^<]*</title>', '<title>TimeCapsule My universe</title>', head, count=1)
    if '<meta name="viewport"' not in head[:2000]:
        head = '<!doctype html>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + head
    # menu: My tables becomes a normal link, My discussions is the current page
    head = re.sub(r'<a href="#" data-tch="noop" aria-current="page" style="color:var\(--tch-teal\)">My tables</a><a href="[^"]*" target="_top">My (?:discussions|universe)</a>',
                        '<a href="mytables.html" target="_top">My tables</a><a href="#" data-tch="noop" aria-current="page" style="color:var(--tch-teal)">My universe</a>', head)
    assert 'aria-current="page" style="color:var(--tch-teal)">My universe' in head
    head = head.replace('Search my tables', 'Search my universe')
    # dictionary
    D1 = load_dict(os.path.join(HERE, 'dict-myuni.txt'), 3)
    DE = load_dict(os.path.join(HERE, 'dict-myuni-el.txt'), 1)
    m0 = re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n', head, re.S)
    D = json.loads(m0.group(1).replace('<\\/', '</'))
    for k, v in D1.items():
        D[k] = v[:2] + [DE.get(k, [v[0]])[0]]
    head = head[:m0.start()] + '<script id="tc-i18n">window.TCI18N_DICT=' + json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n' + head[m0.end():]
    body = open(os.path.join(HERE, 'myuni-body.html'), encoding='utf8').read()
    body = body.replace('/*DATA*/null', json.dumps(rows(), ensure_ascii=False).replace('</', '<\\/'))
    body = body.replace('/*READ*/null', json.dumps(readings(), ensure_ascii=False).replace('</', '<\\/'))
    body = body.replace('/*HELPERS*/', helpers)
    out = os.path.join(ROOT, 'help/live-pages/myuniverse.html')
    open(out, 'w', encoding='utf8').write(head + body + foot)
    subprocess.run(['python3', os.path.join(ROOT, 'i18n/add-greek.py'), out], check=True)
    return out

if __name__ == '__main__':
    print(build())
