"""Keep pages exactly as wide as a phone screen (Gabriele 2026-11-22).
Invite page: the grid column took the width of the wide pager row, so cards ran 4px past
the screen and the whole page zoomed out a little. Grid children may now shrink.
Idempotent: re-run after any rebuild of the Invite page.  python3 phone-fit/patch.py
"""
import os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CSS = '<style id="tc-phonefit">@media (max-width:640px){.view .grid>*{min-width:0}}</style>'
for rel in ('help/live-pages/invite.html', 'invite/timecapsule-invite.html'):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf-8').read()
    s = re.sub(r'<style id="tc-phonefit">.*?</style>', '', s, flags=re.S)
    i = s.rfind('</body>'); assert i > 0, rel
    open(p, 'w', encoding='utf-8').write(s[:i] + CSS + s[i:]); print('patched', rel)
