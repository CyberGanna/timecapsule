"""Tables page on phones: no pictures (Gabriele 2026-11-22, "Lose the pictures also on tables on mobile").
Phones only (max-width 640px): the table cards drop the left picture (ring of chairs) and the
list rows drop the small topic icon tile, so text uses the full width. Desktop unchanged.
Idempotent: re-run after any rebuild of the Tables page.  python3 tables-phone/patch.py
"""
import os, re
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'help', 'live-pages', 'agenda.html')
CSS = """<style id="tc-tblphone">@media (max-width:640px){
body .tbl .ttop{display:none!important}
body .tbl{grid-template-columns:minmax(0,1fr)!important;grid-template-rows:auto!important;flex-direction:column}
body .tbl .tb{width:auto!important;grid-column:1/-1!important}
body .ei .th{display:none!important}
body .ei{gap:0!important}
}</style>"""
s = open(P, encoding='utf-8').read()
s = re.sub(r'<style id="tc-tblphone">.*?</style>', '', s, flags=re.S)
i = s.rfind('</body>'); assert i > 0
open(P, 'w', encoding='utf-8').write(s[:i] + CSS + s[i:]); print('patched agenda.html')
