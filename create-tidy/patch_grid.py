"""Karim 2026-11-22: Seats and Language boxes in Create a table are the same size (height 48, radius 12, equal columns).
Idempotent, marker "tc-ntgrid"."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
CSS = ('<style id="tc-ntgrid">#cpage .ntgrid{display:grid!important;grid-template-columns:1fr 1fr!important;gap:12px!important;align-items:end}'
       '#cpage .ntgrid .opt{min-width:0}'
       '#cpage .ntgrid .step,#cpage .ntgrid select{box-sizing:border-box;height:48px!important;min-height:48px;border-radius:12px!important;width:100%!important;margin:0!important}'
       '#cpage .ntgrid .step{padding:0 4px!important}#cpage .ntgrid select{padding:0 14px!important;font-size:15px!important}</style>')
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-ntgrid' in s: continue
    k = s.rindex('</body>'); s = s[:k] + CSS + s[k:]
    open(p, 'w', encoding='utf8').write(s); print(rel)
