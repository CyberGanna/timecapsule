"""'Your table is open!': button says "Show table"; no top-left Back to tables (the big button does it); card higher (Gabriele 2026-11-18).
Idempotent, marker "tc-cok3". Run after patch.py and patch_back.py."""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = '<style id="tc-cok3">.cwrap:has(>.cok){padding-top:0}.cwrap>.cok{margin-top:0!important}@media(max-width:640px){.cwrap>.cok{margin-top:-4px!important}}</style>'
def run(rel):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-cok3' in s: return
    a = 'sh.innerHTML=`<div class="cwrap"><button class="back" data-close>← Back to tables</button>\n    <div class="ok cok">'
    assert s.count(a) == 1, rel
    s = s.replace(a, 'sh.innerHTML=`<div class="cwrap">\n    <div class="ok cok">')
    n = s.count('id="ntgo">Go to my table</button>'); assert n == 2, (rel, n)
    s = s.replace('id="ntgo">Go to my table</button>', 'id="ntgo">Show table</button>')
    s = s.replace('</title>', '</title>' + CSS, 1)
    s = s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={' + '"Show table":["Mostra il tavolo","Ver la mesa","Δες το τραπέζι"],', 1)
    open(p, 'w', encoding='utf8').write(s); print(rel, 'tidy')
for r in ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']:
    run(r)
