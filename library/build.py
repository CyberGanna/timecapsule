# Builds library/timecapsule-library.html (After the table + Saved discussion) and patches the Profile.
# Run from anywhere: python3 library/build.py
import re, json, os, posixpath, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from data import R, TX, TOPIC_COL

def records():
    out = {}
    for rid, top, sub, title, rounds, priv, outn in R:
        tx = TX[rid]; rr = []
        for k, (date, people) in enumerate(rounds):
            t = tx[k]
            rr.append(dict(date=date, people=people, out=t.get('out', 0), names=t['names'], notes=t['notes'], open=t['open'], my=t.get('my'), tx=[list(x) for x in t['tx']]))
        out[rid] = dict(id=rid, topic=top, sub=sub, title=title, col=TOPIC_COL[top], private=priv, rounds=rr)
    return out

def load_dict(path):
    D = {}
    for ln in open(path, encoding='utf8'):
        if ln.strip():
            p = ln.rstrip('\n').split('|'); assert len(p) == 3, ln; D[p[0]] = p[1:]
    return D

LIBD = load_dict(os.path.join(HERE, 'dict-library.txt'))

def add_dict(s, extra):
    m0 = re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n(.*?)</script>', s, re.S)
    D = json.loads(m0.group(1).replace('<\\/', '</'))
    for k, v in extra.items():
        if k not in D: D[k] = v
    js = 'window.TCI18N_DICT=' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';\n'
    tag = '<script id="tc-i18n">' + js.replace('</', '<\\/') + m0.group(2) + '</script>'
    return s[:m0.start()] + tag + s[m0.end():]

def page():
    L = os.path.join(ROOT, 'help/live-pages/settings.html')
    s = open(L, encoding='utf8').read()
    s = add_dict(s, LIBD)
    head, rest = s.split('<style>\n/* Settings */', 1)
    foot = rest[rest.index('<style id="tcf-css">'):]
    foot = foot[:foot.index('</footer>') + 9] + '\n</body></html>\n'
    head = head.replace('<title>TimeCapsule Settings</title>', '<title>TimeCapsule Library</title>')
    head = head.replace('<a href="#" aria-current="page" data-tch="close">Settings</a>', '<a href="settings.html" target="_top">Settings</a>')
    # header/footer links are relative to help/live-pages/: rebase them to library/
    def rebase(m):
        u = m.group(2)
        if re.match(r'(https?:|#|data:|mailto:|javascript:)', u) or not u: return m.group(0)
        path, frag = (u.split('#', 1) + [''])[:2]
        np = posixpath.relpath(posixpath.normpath(posixpath.join('help/live-pages', path)), 'library')
        return m.group(1) + np + ('#' + frag if frag else '') + '"'
    head = re.sub(r'(href=")([^"]*)"', rebase, head)
    foot = re.sub(r'(href=")([^"]*)"', rebase, foot)
    body = open(os.path.join(HERE, 'body.html'), encoding='utf8').read()
    recs = records()
    data = dict(byId=recs, col=TOPIC_COL)
    body = body.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    out = os.path.join(HERE, 'timecapsule-library.html')
    open(out, 'w', encoding='utf8').write(head + body + foot)
    subprocess.run(['python3', os.path.join(ROOT, 'i18n/add-greek.py'), out], check=True)
    return recs

if __name__ == '__main__':
    recs = page()
    import patch_profile
    patch_profile.run(ROOT, recs, LIBD, add_dict)
