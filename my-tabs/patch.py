"""Unify the view switch on the "My ..." pages (Karim 2026-11-22).
Karim 2026-11-22: view switch = BOXES like the Tables page day filter (36px, radius 10,
solid light box when selected, outlined otherwise); topic filters = round outlined pills.
- My tables: Upcoming / Past boxes sized exactly like the Tables page, counts and purple dot kept,
  16px under the subtitle, no divider line.
- My universe: Books / Films use the same boxes, 16px under the subtitle.
- My universe / My conversations: topic pills start exactly on the page's left edge (was +2px).
- Phones (Karim 2026-11-22, "My tables on mobile is unreadable"): every page gets the viewport
  meta tag (My tables had none, so phones showed the desktop layout shrunk down), and the
  scrolling topic pills bleed exactly to the 20px gutter instead of 22px, so no page is 2px
  wider than the screen (My universe, My conversations, Host tables).
Idempotent: re-run after any rebuild of these pages.  python3 my-tabs/patch.py
"""
import os, re
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'help', 'live-pages')

BOX = "height:36px;padding:0 14px;border-radius:10px;border:1px solid var(--line);background:none;font-size:14px;display:inline-flex;align-items:center;gap:8px;color:var(--fg);cursor:pointer;box-sizing:border-box"
ON = "background:var(--fg);border-color:var(--fg);color:var(--bg)"

TABLES = """<style id="tc-mytabs">
.hero{padding-bottom:0!important}
.wrap>.bar{padding-block:16px 18px;border-bottom:0}
.tabs{gap:4px}
.tabs .tab{%s;flex:none}
.tabs .tab b{font-weight:500}
.tabs .tab span{font-size:12px;color:var(--mute)}
.tabs .tab[aria-pressed=true]{%s}
.tabs .tab[aria-pressed=true] span{color:#4A5180}
.tabs .tab:focus-visible{outline:2px solid var(--teal,#17C3C8);outline-offset:2px}
.tab .todo{top:-4px;right:-4px;width:10px;height:10px;background:var(--teal,#17C3C8)!important}
@media (max-width:700px){.tabs .tab{flex:none;justify-content:center}}
</style>""" % (BOX, ON)

PHONE = "@media (max-width:640px){.mu .pills{margin:0 -20px;padding:2px 20px}}"
MU = """<style id="tc-mytabs">@media (min-width:641px){.mu .pills{margin-left:-2px}}%s</style>""" % PHONE

HT = """<style id="tc-mytabs">@media (max-width:640px){.ht .pills{margin:18px -20px 0;padding:2px 20px}}</style>"""

UNI = """<style id="tc-mytabs">@media (min-width:641px){.mu .pills{margin-left:-2px}}%s
.mu .sw{gap:4px;margin:16px 0 0}
.mu .sw button{all:unset;%s;font-weight:500}
.mu .sw button[aria-selected=true]{%s}
.mu .sw button:focus-visible{outline:2px solid var(--teal);outline-offset:2px;border-radius:10px}
@media(max-width:700px){.mu .sw button{font-size:14px}}
</style>""" % (PHONE, BOX, ON)

VP = '<meta name="viewport" content="width=device-width, initial-scale=1">'

def put(fn, css):
    p = os.path.join(R, fn); s = open(p, encoding='utf-8').read()
    # the viewport tag must be at the top level, not only inside a <template> or srcdoc
    head = s.split('<template', 1)[0].split('srcdoc', 1)[0]
    if not re.search(r'<meta name="?viewport"?', head):
        s = VP + '\n' + s
    s = re.sub(r'<style id="tc-mytabs">.*?</style>', '', s, flags=re.S)
    i = s.rfind('</body>'); assert i > 0, fn
    s = s[:i] + css + s[i:]
    open(p, 'w', encoding='utf-8').write(s); print('patched', fn)

put('mytables.html', TABLES)
put('myuniverse.html', UNI)
put('myconversations.html', MU)
put('hosttables.html', HT)
