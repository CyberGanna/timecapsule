"""Create a table: with no picture added, the Preview card and the "Your table is open!" header
show just the topic icon on the topic colour, like before (Gabriele 2026-11-23). The picture shows only
when the host adds one. Idempotent, marker "tc-plain". Run after patch_cards.py and patch_preview.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']

PLAIN = '`<div class="tcplain"><svg viewBox="0 0 24 24" aria-hidden="true">${TICON[t.theme]||""}</svg></div>`'
REPL = [
    # preview card
    ('<div class="pvc-hd"><img src="${img}" alt="">',
     '<div class="pvc-hd">${nt.img!=null?`<img src="${img}" alt="">`:' + PLAIN + '}'),
    # success screen header
    ('<img alt="" src="${(()=>{const P=window.CKBD;return t.img!=null?IMGS[t.img]:P[t.id%P.length]})()}">',
     '${t.img!=null?`<img alt="" src="${IMGS[t.img]}">`:' + PLAIN + '}'),
]
CSS = '''<style id="tc-plain">
.tcplain{position:absolute;inset:0;z-index:1;display:grid;place-items:center;background:var(--c)}
.tcplain svg{width:52px;height:52px;fill:none;stroke:#1B1F3B;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;opacity:.85}
.cok .ckph .tcplain{z-index:1}
</style>'''

for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-plain' in s:
        continue
    for a, b in REPL:
        assert s.count(a) == 1, (rel, a[:40])
        s = s.replace(a, b)
    i = s.rindex('</body>'); s = s[:i] + CSS + s[i:]
    open(p, 'w', encoding='utf8').write(s); print(rel, 'plain')
