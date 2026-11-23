"""Guides, Notes, step "Write a note": a small picture of the Live Table transcript showing the note icon
next to a line, above the example note that quotes it (Karim 2026-11-23). Idempotent, marker "gd-catch"."""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
AV = json.load(open(os.path.join(HERE, 'av.json')))
FILES = ['help/timecapsule-guides.html', 'help/guides-body.html']
ANCHOR = '<div class="mini"><div class="note"><q>Gregory: Maybe choosing is just noticing what we already are.</q>'
PIC = ('<div class="mini gd-catch" aria-hidden="true"><div class="gtr">'
       '<div class="gln"><span class="ga">%s</span><div><div class="gw"><b>Lena</b>19:24</div><p>I think habits decide most of my day.</p></div><span class="gclip">%s</span></div>'
       '<div class="gln on"><span class="ga">%s</span><div><div class="gw"><b>Gregory</b>19:25</div><p>Maybe choosing is just noticing what we already are.</p></div><span class="gclip">%s</span><span class="gtip">Add to my notes</span></div>'
       '</div></div>') % (AV['l'], AV['clip'], AV['g'], AV['clip'])
CSS = '''<style id="gd-catch">
.gd-catch .gtr{width:100%;max-width:440px;padding:6px 14px;border-radius:12px;background:var(--surface);border:1px solid var(--line)}
.gln{position:relative;display:grid;grid-template-columns:28px minmax(0,1fr) 30px;gap:10px;align-items:start;padding:8px 0}
.gln+.gln{border-top:1px solid var(--line)}
.gln .ga{width:28px;height:28px;border-radius:50%;overflow:hidden}.gln .ga svg{width:100%;height:100%;display:block}
.gln .gw{font-size:12px;color:var(--mute);margin-bottom:2px}.gln .gw b{color:var(--fg);font-weight:600;margin-right:6px}
.gln p{margin:0;font-size:14px;line-height:1.5;color:var(--soft)}
.gclip{width:30px;height:30px;border-radius:9px;border:1px solid var(--line);display:grid;place-items:center;color:var(--mute);opacity:.55}
.gclip svg{width:15px;height:15px}
.gln.on .gclip{opacity:1;color:#EEF1FF;border-color:#17C3C8;box-shadow:0 0 0 3px rgba(23,195,200,.18)}
.gtip{position:absolute;right:0;top:-24px;font-size:11.5px;padding:3px 8px;border-radius:6px;background:#EEF1FF;color:#1B1F3B;white-space:nowrap}
.gd-catch+.mini{margin-top:10px}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'gd-catch' in s:
        continue
    assert s.count(ANCHOR) == 1, rel
    s = s.replace(ANCHOR, PIC + ANCHOR)
    if '</body>' in s:
        i = s.rindex('</body>'); s = s[:i] + CSS + s[i:]
    else:
        s += CSS
    open(p, 'w', encoding='utf8').write(s); print(rel, 'catch picture')
