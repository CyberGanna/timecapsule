"""Unify the view switch on the "My ..." pages (Karim 2026-11-22).
Underline = switch view (Books | Films, Upcoming | Past); outlined pills = filter by topic.
- My tables: Upcoming / Past become underlined tabs like Books / Films on My universe
  (17px, mute -> white, 2px teal underline, 22px gap, 6px under the subtitle), counts kept,
  purple "to do" dot moved next to the Past count. Divider line under the bar removed.
- My universe / My conversations: topic pills start exactly on the page's left edge (was +2px).
Idempotent: re-run after any rebuild of these pages.  python3 my-tabs/patch.py
"""
import os, re
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'help', 'live-pages')

TABLES = """<style id="tc-mytabs">
.hero{padding-bottom:0!important}
.wrap>.bar{padding-block:6px 18px;border-bottom:0}
.tabs{gap:22px}
.tabs .tab{height:auto;padding:6px 0 7px;border:0;border-bottom:2px solid transparent;border-radius:0;background:none;font-size:17px;gap:7px;color:var(--mute);cursor:pointer;flex:none}
.tabs .tab b{font-weight:400}
.tabs .tab span{font-size:13px;color:var(--mute)}
.tabs .tab[aria-pressed=true]{background:none;color:var(--fg);border-bottom-color:var(--teal,#17C3C8)}
.tabs .tab[aria-pressed=true] span{color:var(--soft,#A9B0D6)}
.tabs .tab:focus-visible{outline:2px solid var(--teal,#17C3C8);outline-offset:4px;border-radius:2px}
.tab .todo{top:6px;right:-13px;width:9px;height:9px}
@media (max-width:700px){.tabs .tab{font-size:16px;flex:none;justify-content:flex-start}}
</style>"""

MU = """<style id="tc-mytabs">@media (min-width:641px){.mu .pills{margin-left:-2px}}</style>"""

def put(fn, css):
    p = os.path.join(R, fn); s = open(p, encoding='utf-8').read()
    s = re.sub(r'<style id="tc-mytabs">.*?</style>', '', s, flags=re.S)
    i = s.rfind('</body>'); assert i > 0, fn
    s = s[:i] + css + s[i:]
    open(p, 'w', encoding='utf-8').write(s); print('patched', fn)

put('mytables.html', TABLES)
put('myuniverse.html', MU)
put('myconversations.html', MU)
