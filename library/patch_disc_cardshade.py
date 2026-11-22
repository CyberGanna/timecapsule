# Conversations page: small cards get a solid dark navy background (Karim found topic shading too busy). Safe to run twice.
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('<style id="disc-cardshade">.dp .card{background:#141936!important;border-color:rgba(238,241,255,.09)!important}'
       '.dp .card:hover{background:#171D3E!important;border-color:rgba(238,241,255,.18)!important}</style>')
for rel in ('library/disc-body.html', 'help/live-pages/discussions.html'):
    F = os.path.join(R, rel); s = open(F, encoding='utf8').read()
    s = re.sub(r'<style id="disc-cardshade">.*?</style>', '', s)
    i = s.index('<style id="disc-chips">')
    s = s[:i] + CSS + s[i:]
    open(F, 'w', encoding='utf8').write(s); print(rel, 'patched')
