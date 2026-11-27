"""Gabriele 2026-11-23: Conversations page cards (and the big featured box on top) get a soft shadow like the Tables page cards.
PR #211 first version, lighter version after "less shadow, also on the big box on top". Re-runnable: replaces the tc-convshadow block.
2026-11-27: same shadow on the My conversations page cards (.mu .card), which had none. Re-run after rebuilding either page."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def css(sel):
    a = ','.join(f'{s}' for s in sel); h = ','.join(f'{s}:hover' for s in sel)
    return ('<style id="tc-convshadow">' + a + '{box-shadow:0 1px 0 rgba(255,255,255,.04) inset,0 8px 22px rgba(4,6,20,.32)}'
            + h + '{box-shadow:0 1px 0 rgba(255,255,255,.05) inset,0 10px 26px rgba(4,6,20,.4)}</style>')
PAGES = {'help/live-pages/discussions.html': ['.dp .card', '.dp .feat'],
         'library/disc-body.html': ['.dp .card', '.dp .feat'],
         'help/live-pages/myconversations.html': ['.mu .card']}
for rel, sel in PAGES.items():
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read(); CSS = css(sel)
    if 'tc-convshadow' in s:
        s = re.sub(r'<style id="tc-convshadow">.*?</style>', lambda m: CSS, s, flags=re.S)
    else:
        k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel)
