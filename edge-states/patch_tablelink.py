"""Edge states page: "Table full" and "Cancelled" open the Table page's own Full / Cancelled states,
which use the current card look (Gabriele 2026-11-23: no more ring-of-chairs graphic anywhere).
The page now opens on "Removed". Idempotent, marker "tc-edge-tl"."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'edge-states/timecapsule-edge.html')
s = open(P, encoding='utf8').read()
if 'tc-edge-tl' not in s:
    a = "function show(s,push){if(!S[s])s='full';cur=s;"
    b = ("function show(s,push){/* tc-edge-tl */if(s==='full'||s==='cancelled'){const m=location.hash.match(/[#&]lang=[a-z]+/);"
         "location.href=U.table+'#'+s+(m?'&'+m[0].slice(1):'');return}if(!S[s])s='removed';cur=s;")
    c = "show((location.hash.slice(1).split('&')[0])||'full',false);"
    d = "show((location.hash.slice(1).split('&')[0])||'removed',false);"
    for x, y in [(a, b), (c, d)]:
        assert s.count(x) == 1, x
        s = s.replace(x, y)
    open(P, 'w', encoding='utf8').write(s); print('edge: table states link to the Table page')
