# Builds help/live-pages/discussions.html (public Conversations page, header link) from the My tables page shell.
# Run: python3 library/build_disc.py (build.py runs it too)
import re, json, os, subprocess, sys, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from data import R, TX, TOPIC_COL, SUM
from data_pub import PUB, PUB_COL, TXP
from build_myuni import load_dict, MON

def item(rid, host, top, sub, title, rounds, col, tx, summ):
    d, n = rounds[-1]; wd, day, mon = d.split()
    last = tx[-1]
    ls = [l for l in last['tx'] if l[1]]; q = ([l for l in ls if l[1] not in ('Gabriele', host)] or ls)[-1]
    return dict(id=rid, host=host, topic=top, sub=sub, title=title, col=col, rounds=len(rounds), people=n,
                names=[host] + [x for x in last['names'] if x != host], day=int(day), mon=mon, key=MON[mon]*100+int(day),
                quote=[q[1], q[2]], summary=summ)

def data():
    out = []
    for rid, top, sub, title, rounds, priv, outn in R:
        if priv: continue
        s = SUM.get(rid, [None]*len(rounds))[-1] or ('The table talked about "%s". %s' % (title, ' '.join(TX[rid][-1]['notes'])))
        out.append(item(rid, 'Gregory', top, sub, title, rounds, TOPIC_COL[top], TX[rid], s))
    for rid, host, top, sub, title, rounds, outn, trusted in PUB:
        s = 'The table talked about "%s". %s Left open: %s' % (title, ' '.join(TXP[rid][-1]['notes']), TXP[rid][-1]['open'][0])
        out.append(item(rid, host, top, sub, title, rounds, PUB_COL[top], TXP[rid], s))
    return out

def stars():
    rnd = random.Random(11); W, H = 720, 420; c = []
    for i in range(260):
        x, y = rnd.uniform(0, W), rnd.uniform(0, H); r = rnd.choice([.5, .6, .7, .8, 1, 1.2]); o = rnd.uniform(.25, .8)
        c.append('<circle cx="%.0f" cy="%.0f" r="%s" fill="%%23fff" opacity="%.2f"/>' % (x, y, r, o))
    return "url('data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%d\" height=\"%d\">%s</svg>')" % (W, H, ''.join(c))

def build():
    s = open(os.path.join(ROOT, 'help/live-pages/mytables.html'), encoding='utf8').read()
    helpers = re.search(r'\nconst HAIR=.*?\nconst P=.*?\nfunction av\(n\).*?\n', s, re.S).group(0)
    head = s[:s.index('<div class="wrap">\n  <section class="hero">')]
    foot = s[s.index('<style id="tcf-css">'):s.index('<style id="tce-css">')] + s[s.index('<footer class="tcf"'):]
    head = re.sub(r'<title>[^<]*</title>', '<title>TimeCapsule Conversations</title>', head, count=1)
    if '<meta name="viewport"' not in head[:2000]:
        head = '<!doctype html>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + head
    head = head.replace('<a href="#" data-tch="noop" aria-current="page" style="color:var(--tch-teal)">My tables</a>', '<a href="mytables.html" target="_top">My tables</a>')
    head, n = re.subn(r'<a href="discussions.html" target="_top">Conversations</a>', '<a href="#" aria-current="page">Conversations</a>', head)
    assert n >= 1, 'nav link missing in mytables shell'
    head = head.replace('Search my tables', 'Search conversations')
    D1 = load_dict(os.path.join(HERE, 'dict-disc.txt'), 3); DE = load_dict(os.path.join(HERE, 'dict-disc-el.txt'), 1)
    m0 = re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n', head, re.S)
    D = json.loads(m0.group(1).replace('<\\/', '</'))
    for k, v in D1.items(): D[k] = v[:2] + [DE.get(k, [v[0]])[0]]
    head = head[:m0.start()] + '<script id="tc-i18n">window.TCI18N_DICT=' + json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n' + head[m0.end():]
    body = open(os.path.join(HERE, 'disc-body.html'), encoding='utf8').read()
    body = body.replace('STARS', stars()).replace('/*DATA*/null', json.dumps(data(), ensure_ascii=False).replace('</', '<\\/')).replace('/*HELPERS*/', helpers)
    out = os.path.join(ROOT, 'help/live-pages/discussions.html')
    open(out, 'w', encoding='utf8').write(head + body + foot)
    subprocess.run(['python3', os.path.join(ROOT, 'i18n/add-greek.py'), out], check=True)
    return out

if __name__ == '__main__':
    print(build())
