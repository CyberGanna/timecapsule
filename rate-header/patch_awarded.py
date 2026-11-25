"""Gabriele 2026-11-23: in the Thanks summary "Awarded" row, "Gregory 1" sits too close: use "Gregory: 1". Idempotent."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = 'p[0]+" "+val[people.indexOf(p)]'; B = 'p[0]+": "+val[people.indexOf(p)]'
for rel in ['rate-tip/timecapsule-rate-tip.html', 'help/live-pages/mytables.html', 'invite/pages/mytables.html']:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if A in s: open(p, 'w', encoding='utf8').write(s.replace(A, B)); print(rel)
