# Conversations page: small cards get the same topic-coloured shading as the big "Picked up again" card. Safe to run twice.
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('<style id="disc-cardshade">.dp .card{background:radial-gradient(110% 120% at 0% 0%,color-mix(in srgb,var(--c) 24%,transparent),transparent 62%),#18204A!important}'
       '.dp .card:hover{background:radial-gradient(110% 120% at 0% 0%,color-mix(in srgb,var(--c) 30%,transparent),transparent 66%),#18204A!important}</style>')
for rel in ('library/disc-body.html', 'help/live-pages/discussions.html'):
    F = os.path.join(R, rel); s = open(F, encoding='utf8').read()
    if 'id="disc-cardshade"' in s: print(rel, 'already'); continue
    i = s.index('<style id="disc-chips">')
    s = s[:i] + CSS + s[i:]
    open(F, 'w', encoding='utf8').write(s); print(rel, 'patched')
