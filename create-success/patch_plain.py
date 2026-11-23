"""Create a table: with no picture added, the Preview card and the "Your table is open!" header
show just the topic icon on the topic colour, like before (Karim 2026-11-23). The picture shows only
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
.tcplain{position:absolute;inset:0;display:grid;place-items:center;background:radial-gradient(45% 65% at 18% 30%,color-mix(in srgb,var(--c) 60%,transparent),transparent 70%),radial-gradient(50% 70% at 85% 75%,rgba(124,92,255,.5),transparent 70%),radial-gradient(40% 55% at 70% 12%,rgba(23,195,200,.33),transparent 70%),radial-gradient(45% 65% at 25% 95%,color-mix(in srgb,var(--c) 36%,transparent),transparent 70%),#252B52}
.tcplain svg{width:56px;height:56px;fill:none;stroke:#fff;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;opacity:.92}
.pvc-hd .tcplain+*,.cok .ckph .tcplain{z-index:0}
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
