"""'Your table is open!' smaller so the whole card fits on a laptop screen (Gabriele 2026-11-23).
Idempotent, marker "tc-cok6". Run last of the create-success patches."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']
CSS = '''<style id="tc-cok6">
.cok{max-width:500px!important;margin:16px auto 0!important;padding:0 24px 22px!important}
.cok .cktop.ckph{height:120px!important;margin:0 -24px 16px!important}
.cok .tcplain svg{width:44px;height:44px}
.cok h2{font-size:22px!important}
.cok .ckmeta{margin-top:8px!important;font-size:13px!important}
.cok .cktitle{margin-top:6px!important;font-size:20px!important}
.cok .ckfaces{margin-top:14px!important;max-width:360px!important;gap:6px!important}
.cok .ckfaces>span,.cok .ckfaces>em{flex-basis:32px!important}
.cok .ckseats{margin-top:6px!important;font-size:12.5px!important}
.cok .ckcd{margin-top:12px!important}.cok .ckcd .u b{font-size:24px!important}
.cok .ckwhen{margin-top:2px!important;font-size:12.5px!important}
.cok .ntinv{margin-top:14px!important;height:38px!important;font-size:14px!important}
.cok .acts{margin-top:16px!important}.cok .acts .cta{min-height:42px!important;height:42px!important}
@media (max-width:640px){.cok{padding:0 18px 20px!important}.cok .cktop.ckph{margin:0 -18px 14px!important}}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-cok6' in s:
        continue
    i = s.rindex('</body>'); s = s[:i] + CSS + s[i:]
    open(p, 'w', encoding='utf8').write(s); print(rel, 'compact')
