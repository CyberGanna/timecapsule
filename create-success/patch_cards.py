"""'Your table is open!' in the style of the new Tables page cards (Gabriele 2026-11-23).
Photo header (the host's photo, else the same stand-in photo the card uses), topic dot + LIVE,
the question in Literata, a row with your face and dashed free chairs, "N chairs free".
Idempotent, marker "tc-cok5". Run after patch_look.py and patch_start.py."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ag = open(os.path.join(ROOT, 'help/live-pages/agenda.html'), encoding='utf8').read()
_bd = re.findall(r'"(data:[^"]+)"', re.search(r'const CCPOOL=\[\.\.\.IMGS,((?:"data:[^"]+",?)+)\]', _ag).group(1))
CKBD = '<script id="tc-cok5-bd">window.CKBD=["%s","%s"];</script>' % (_bd[1], _bd[3])  # sunset, eclipse (Profile backdrops)
FILES = ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']

OLD_TOP = '<div class="ttop cktop" style="--c:${THEMES[t.theme]}">${t.img!=null?`<div class="tbg" style="background-image:url(\'${IMGS[t.img]}\')"></div>`:genBg(THEMES[t.theme])}${ring(t,true)}</div>'
NEW_TOP = ('<div class="cktop ckph" style="--c:${THEMES[t.theme]}"><img alt="" src="${(()=>{const P=window.CKBD;return t.img!=null?IMGS[t.img]:P[t.id%P.length]})()}">'
           '${now?`<div class="ckhour"><i></i></div>`:""}</div>')
OLD_TITLE = '<p class="cktitle" data-noi18n>${esc(t.title)}</p>'
NEW_TITLE = ('<div class="ckmeta" style="--c:${THEMES[t.theme]}"><span class="cktopic"><i></i>${t.theme}</span>${now?`<span class="cklv">LIVE</span>`:""}</div>'
             '<p class="cktitle" data-noi18n>${esc(t.title)}</p>'
             '${(()=>{const n=Math.max(2,+(t.seats||nt.seats||8)),f=n-1;return `<div class="ckfaces"><span>${av("You")}</span>${"<em></em>".repeat(f)}</div><p class="ckseats">${f} ${f===1?"chair":"chairs"} free</p>`})()}')
OLD_LIVE = '${now?`<span class="cklive"><i></i><span>Live now</span></span>`:'
NEW_LIVE = '${now?``:'

CSS = '''<style id="tc-cok5">
.cok .cktop.ckph{position:relative;height:190px;padding:0!important;overflow:hidden;background:#252B52}
.cok .ckph img{width:100%;height:100%;object-fit:cover;display:block}
.cok .ckph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,25,54,0) 55%,rgba(32,38,74,.6))}
.cok .ckhour{position:absolute;left:0;right:0;bottom:0;height:3px;background:rgba(238,241,255,.10);z-index:2}.cok .ckhour i{display:block;width:2%;height:100%;background:#3DDC84}
.cok .ckmeta{display:flex;justify-content:center;align-items:center;gap:14px;margin-top:14px;font-size:13.5px;color:#C9CFF0}
.cok .cktopic{display:flex;align-items:center;gap:8px}.cok .cktopic i{width:8px;height:8px;border-radius:50%;background:var(--c)}
.cok .cklv{font-size:12px;font-weight:600;letter-spacing:.14em;color:#3DDC84}
.cok .cktitle{margin:10px auto 0!important;max-width:460px;font-family:Literata,Georgia,serif!important;font-size:23px!important;font-weight:500!important;line-height:1.28!important;padding-bottom:.1em;color:#EEF1FF!important}
.cok .ckfaces{display:flex;justify-content:center;gap:8px;margin:20px auto 0;max-width:420px}
.cok .ckfaces>span,.cok .ckfaces>em{flex:0 1 38px;min-width:0;aspect-ratio:1;border-radius:50%;overflow:hidden;display:block;box-sizing:border-box}
.cok .ckfaces svg,.cok .ckfaces img{width:100%;height:100%;display:block}
.cok .ckfaces>em{border:1.5px dashed rgba(238,241,255,.28)}
.cok .ckseats{margin:10px 0 0;font-size:13px;color:#A9B0D6;text-align:center}
@media (max-width:640px){.cok .cktop.ckph{height:150px}.cok .cktitle{font-size:20px!important}.cok .ckfaces{gap:6px}}
</style>'''
FONT = 'family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400'

for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-cok5' in s:
        continue
    for a, b in ((OLD_TOP, NEW_TOP), (OLD_TITLE, NEW_TITLE), (OLD_LIVE, NEW_LIVE)):
        assert s.count(a) == 1, (rel, a[:50])
        s = s.replace(a, b)
    i = s.rindex('</body>'); s = s[:i] + CSS + CKBD + s[i:]
    if 'family=Literata' not in s:
        s = s.replace('</title>', '</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?%s&display=swap">' % FONT, 1)
    open(p, 'w', encoding='utf8').write(s); print(rel, 'cards')
