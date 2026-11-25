"""Gabriele 2026-11-23: "make it more calm so the attention is focused on the rating part; the user just came
from the table so he doesn't need much info". Banner becomes a thin strip, title smaller, one quiet line,
no Hosted by row. Run after patch.py and patch_banner.py. Re-runnable (replaces block "tc-ratecalm")."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['rate-tip/timecapsule-rate-tip.html', 'help/live-pages/mytables.html', 'invite/pages/mytables.html']
CSS = '''<style id="tc-ratecalm">
.card.tbl .tbanner,.rtpop .card.tbl .tbanner,.compact .card.tbl .tbanner{height:72px!important;border-radius:12px!important;opacity:.85}
.card.tbl .ttl,.compact .card.tbl .ttl,.rtpop .card.tbl .ttl{gap:12px!important}
.card.tbl .ttl>div:not(.tbanner){gap:4px!important}
.card.tbl .ttl h1{font-size:16px!important;font-weight:500!important;margin:0!important;color:#D3D8F5!important}
.card.tbl .ttl .sub{font-size:13px!important;color:var(--mute)!important}
.card.tbl .ttl .stp{color:var(--mute)!important}
.card.tbl .mod{display:none!important}
.card.tbl,.rtpop .card.tbl{padding-bottom:18px!important}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-ratecalm' in s: s = re.sub(r'<style id="tc-ratecalm">.*?</style>', lambda m: CSS, s, flags=re.S)
    else:
        k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel)
