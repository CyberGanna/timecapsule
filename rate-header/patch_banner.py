"""Gabriele 2026-11-23 "try with the banner": the Table ended header shows the table's photo banner
(like the Tables cards' photo header) instead of the 64px tile; title and details stack under it, left-aligned.
Run after rate-header/patch.py. Idempotent, marker "tc-ratebanner". Photo: banner.b64 (free-will card photo, 1000px)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['rate-tip/timecapsule-rate-tip.html', 'help/live-pages/mytables.html', 'invite/pages/mytables.html']
B64 = open(os.path.join(ROOT, 'rate-header', 'banner.b64')).read().strip()
BANNER = '<div class="tbanner" aria-hidden="true"><img src="data:image/jpeg;base64,' + B64 + '" alt=""></div>'
CSS = '''<style id="tc-ratebanner">
.card.tbl .ttl,.compact .card.tbl .ttl,.rtpop .card.tbl .ttl{flex-direction:column!important;align-items:stretch!important;gap:14px!important}
.card.tbl .ttl>div{flex:none!important}
.card.tbl .ttl>div:not(.tbanner){gap:6px!important}
.card.tbl .tbanner{display:block!important;position:relative;height:150px;border-radius:16px;overflow:hidden;background:#252B52}
.card.tbl .tbanner::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,25,54,0) 55%,rgba(32,38,74,.55))}
.card.tbl .tbanner img{width:100%;height:100%;object-fit:cover;display:block}
.rtpop .card.tbl .tbanner,.compact .card.tbl .tbanner{height:120px}
@media (max-width:640px){.card.tbl .tbanner{height:128px}}
.card.tbl .ttl h1{font-size:21px!important}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-ratebanner' in s: continue
    s, n = re.subn(r'<span class="ttile"[^>]*><svg viewBox="0 0 24 24">.*?</svg></span>', lambda m: BANNER, s, count=1, flags=re.S)
    assert n, rel
    k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel)
