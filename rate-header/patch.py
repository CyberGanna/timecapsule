"""Karim 2026-11-23: the "Table ended" (Rate and Tip) header gets the new graphic, like the join sheet preview:
- "Table ended" is quiet text, no grey pill
- the round topic disc becomes the list-row tile (64px rounded, topic glow + white topic icon)
- title left-aligned next to the tile; under it: topic dot + topic · Today · 58 min · 7 people
- "Hosted by" uses Gregory's real photo instead of the GP initials
Idempotent, marker "tc-rateheader". Re-run after rebuilding Rate and Tip or My tables."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['rate-tip/timecapsule-rate-tip.html', 'help/live-pages/mytables.html', 'invite/pages/mytables.html']
ICON = '<path d="M4 20h16M5 17h14M6 17V9m4 8V9m4 8V9m4 8V9M4 9h16L12 4z"/>'
TILE = ('<span class="ttile" aria-hidden="true" style="background:radial-gradient(circle at 35% 30%,#F29BD0,#F29BD066 75%,#252B52)">'
        '<svg viewBox="0 0 24 24">' + ICON + '</svg></span>')
CSS = '''<style id="tc-rateheader">
.ph .ended{background:none!important;padding:0!important;border-radius:0!important;color:var(--mute)!important;font-size:12px!important;font-weight:600!important;letter-spacing:.12em!important}
.card.tbl .ttl,.compact .card.tbl .ttl,.rtpop .card.tbl .ttl{flex-direction:row!important;align-items:center!important;text-align:left!important;gap:16px!important}
.card.tbl .ttile{flex:none;width:64px;height:64px;border-radius:16px;overflow:hidden;display:grid;place-items:center}
.card.tbl .ttile svg{width:46%;height:46%;fill:none;stroke:#fff;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;opacity:.9;filter:drop-shadow(0 1px 4px rgba(0,0,0,.3))}
.card.tbl .ttl h1{text-align:left!important;margin:0 0 6px!important;font-size:19px!important;line-height:1.3!important}
.card.tbl .ttl .sub{text-align:left!important;justify-content:flex-start!important;margin:0!important}
.card.tbl .ttl .stp{display:inline-flex;align-items:center;gap:7px;color:#C9CFF0}
.card.tbl .ttl .stp i{width:8px;height:8px;border-radius:50%;background:#F29BD0}
.card.tbl .ttl .eyebrow{display:none!important}
.card.tbl .mod summary,.rtpop .card.tbl .mod summary,.compact .card.tbl .mod summary{justify-content:flex-start!important}
.card.tbl .mod .mini.ph2{background:none!important;padding:0;overflow:hidden}
.card.tbl .mod .mini.ph2 img{width:100%;height:100%;object-fit:cover;display:block;border-radius:50%}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-rateheader' in s: continue
    s, n1 = re.subn(r'<div class="ttl"><img class="topic" src="data:image/jpeg;base64,[A-Za-z0-9+/=]+" alt=""[^>]*>', '<div class="ttl">' + TILE, s, count=1)
    s, n2 = re.subn(r'(<p class="sub">)(Today · 58 min)', r'\1<span class="stp"><i></i>Philosophy</span><span class="sep"> · </span>\2', s, count=1)
    m = re.search(r'<img class="lbpav" src="(data:image/[a-z]+;base64,[A-Za-z0-9+/=]+)"', s)
    old = '<span class="mini" aria-hidden="true">GP</span>'
    n3 = s.count(old)
    if m and n3: s = s.replace(old, '<span class="mini ph2" aria-hidden="true"><img src="' + m.group(1) + '" alt=""></span>', 1)
    assert n1 and n2 and m and n3, (rel, n1, n2, bool(m), n3)
    k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel)
