# Evens out the shared header (#tch) icons: one 24-grid icon set (search, chats, bell) with the
# same size, stroke and colour; one badge position for the chat count and the bell dot; even spacing
# on desktop and phone. Re-runnable: replaces its own <style id="tch-even"> and the three icons.
# Unread marks (rule, Karim 2026-11-22): every unread / needs-attention dot or count is teal:
# header dropdown rows, Chats page counts, Notifications page dots.
# Phones (Karim 2026-11-23): search, Chats and bell are quiet boxes the same size as the + button.
# Run after rebuilding any page with the header: python3 header-icons/patch.py
import re, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ('node_modules/',)
SW = 'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"'
CHAT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" %s aria-hidden="true">'
        '<path d="M7.5 4.5h9a4 4 0 0 1 4 4v4.5a4 4 0 0 1-4 4H12l-4.5 3.5v-3.5A4 4 0 0 1 3.5 13V8.5a4 4 0 0 1 4-4z"/></svg>') % SW
BELL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" %s aria-hidden="true">'
        '<path d="M12 3.5a6 6 0 0 0-6 6v3.8l-1.5 2.9h15L18 13.3V9.5a6 6 0 0 0-6-6z"/>'
        '<path d="M9.8 18.8a2.2 2.2 0 0 0 4.4 0"/></svg>') % SW
SEARCH = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" %s aria-hidden="true">'
          '<circle cx="10.75" cy="10.75" r="6.25"/><path d="M15.5 15.5l4.5 4.5"/></svg>') % SW
CSS = '''<style id="tch-even">
#tch .tch-ib,#tch .tch-ic{width:40px;height:40px;color:var(--tch-soft)}
#tch .tch-ib svg,#tch .tch-ic svg{width:22px;height:22px;display:block}
#tch .tch-ic+.tch-ic{margin-left:-8px}
#tch .tch-create+.tch-ic{margin-left:4px}
#tch .tch-me{width:36px;height:36px;margin-left:4px}
#tch .tch-ic .tch-n,#tch .tch-ic .tch-d{position:absolute;top:auto;right:auto;box-shadow:0 0 0 2px var(--tch-bg);background:var(--tch-teal,#17C3C8)}
#tch .tch-ic .tch-n{left:21.5px;top:4.5px;min-width:15px;height:15px;padding:0 4px;border-radius:8px;color:#0F1530;font-size:9.5px;font-weight:700;line-height:15px;letter-spacing:0;display:block;text-align:center;font-style:normal}
#tch .tch-ic .tch-d{left:25px;top:8px;width:8px;height:8px;border-radius:50%}
#tch.over .tch-ic .tch-n,#tch.over .tch-ic .tch-d{box-shadow:none}
#tch .tch-pop li.un time{color:var(--tch-teal,#17C3C8)}
#tch .tch-pop li.un .tch-tx b::after{background:var(--tch-teal,#17C3C8)}
body .cv .un{background:var(--teal,#17C3C8);color:#0F1530}
body .it.un .end time::before{background:var(--teal,#17C3C8)}
body .fl .c{color:var(--teal,#17C3C8)}
body .fl[aria-pressed=true] .c{color:#0E7F83}
@media (max-width:640px){
#tch .tch-bar{gap:8px}
#tch .tch-ib,#tch .tch-ic{width:36px;height:36px;border-radius:10px;background:var(--tch-field);box-shadow:inset 0 0 0 1px var(--tch-line);color:var(--tch-fg)}
#tch .tch-ib svg,#tch .tch-ic svg{width:20px;height:20px}
#tch .tch-ic .tch-n{left:auto;right:-6px;top:-6px}
#tch .tch-ic .tch-d{left:auto;right:-4px;top:-4px;width:10px;height:10px}
#tch .tch-create{width:36px;height:36px;margin-left:0}
#tch .tch-create+.tch-ic,#tch .tch-ic+.tch-ic{margin-left:0}
#tch .tch-me{width:36px;height:36px;margin-left:4px}
}
</style>'''
STYLE = re.compile(r'<style id="tch-even">.*?</style>\n?', re.S)
IC = re.compile(r'(<(?:a|button) class="tch-ic[^"]*"[^>]*>)<svg\b.*?</svg>', re.S)
SR = re.compile(r'(<button class="tch-ib"[^>]*data-tch="search"[^>]*>)<svg\b.*?</svg>', re.S)
changed = []
for f in glob.glob(os.path.join(ROOT, '**/*.html'), recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith(SKIP):
        continue
    s = open(f, encoding='utf8').read(); o = s
    if '<header id="tch"' not in s:
        continue
    s = STYLE.sub('', s)
    s = s.replace('<header id="tch"', CSS + '\n<header id="tch"', 1)
    s = IC.sub(lambda m: m.group(1) + (CHAT if 'data-tch="msg"' in m.group(1) else BELL), s)
    s = SR.sub(lambda m: m.group(1) + SEARCH, s)
    if s != o:
        open(f, 'w', encoding='utf8').write(s); changed.append(rel)
print(len(changed)); print('\n'.join(sorted(changed)))
