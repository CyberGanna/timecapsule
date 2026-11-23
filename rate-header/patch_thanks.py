"""Karim 2026-11-23: the "Thanks for your feedback" screen header is too big, especially the coin logo.
Smaller coin badge, smaller title, tighter spacing. Re-runnable (replaces block "tc-ratethanks")."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['rate-tip/timecapsule-rate-tip.html', 'help/live-pages/mytables.html', 'invite/pages/mytables.html']
CSS = '''<style id="tc-ratethanks">
.step.thanks{padding-top:4px!important;gap:12px!important}
.step.thanks .badge{width:48px!important;height:48px!important;border-width:1px!important}
.step.thanks .badge svg{width:26px!important;height:26px!important}
.step.thanks h2{font-size:19px!important;margin-top:2px!important}
.step.thanks .lead{font-size:14px!important;margin-top:-6px!important}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-ratethanks' in s: s = re.sub(r'<style id="tc-ratethanks">.*?</style>', lambda m: CSS, s, flags=re.S)
    else:
        k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel)
