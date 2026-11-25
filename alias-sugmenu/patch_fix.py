"""Gabriele 2026-11-23: the alias Suggestions menu on Create a table did not open. Two click handlers
(tc-sugmenu for the topic Suggestions, tc-aliasmenu for aliases) both toggled the alias list, so it opened
and closed in the same click. Scope tc-sugmenu's handlers to its own box (.sgm). Idempotent.
Re-run after create-tidy/patch_sugmenu.py and alias-sugmenu/patch.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = [('closest("#cpage .sgbtn")', 'closest("#cpage .sgm .sgbtn")'),
       ('querySelectorAll("#cpage .sgl")', 'querySelectorAll("#cpage .sgm .sgl")'),
       ('querySelectorAll("#cpage .sgl:not([hidden])")', 'querySelectorAll("#cpage .sgm .sgl:not([hidden])")')]
for rel in ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html', 'create-tidy/patch_sugmenu.py']:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read(); n = s
    for a, b in REP: n = n.replace(a, b)
    if n != s: open(p, 'w', encoding='utf8').write(n); print(rel)
