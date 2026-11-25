"""Gabriele 2026-11-22: bigger field titles in Create a table (Topic, question, Picture, When, Who can join, Seats, Language, Host as...).
15.5px, weight 500, full text colour; "optional" stays small and muted. Idempotent, marker "tc-labels"."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
CSS = ('<style id="tc-labels">#cpage .cform label.l,#cpage .cform .l{font-size:15.5px!important;font-weight:500!important;color:var(--text,#EEF1FF)!important;margin-bottom:10px!important;letter-spacing:0}'
       '#cpage .cform .l .optl{font-size:12.5px;font-weight:400;color:var(--mute,#A9B0D6)}</style>')
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-labels' in s: continue
    k = s.rindex('</body>'); s = s[:k] + CSS + s[k:]
    open(p, 'w', encoding='utf8').write(s); print(rel)
