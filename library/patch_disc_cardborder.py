# Conversations page: slightly thicker card border (Gabriele 2026-11-22). Safe to run twice.
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = '<style id="disc-cardborder">.dp .card,.dp .feat{border-width:2px!important}</style>'
for rel in ('library/disc-body.html', 'help/live-pages/discussions.html'):
    F = os.path.join(R, rel); s = open(F, encoding='utf8').read()
    if 'id="disc-cardborder"' in s: print(rel, 'already'); continue
    i = s.index('<style id="disc-sort">'); s = s[:i] + CSS + s[i:]
    open(F, 'w', encoding='utf8').write(s); print(rel, 'patched')
