"""Tables page: a live table you're in shows "Go back in" (opens the Welcome back camera check),
instead of a gold "You're in" that silently made you leave (Karim 2026-11-19). Idempotent; run after satlock/patch.py."""
import re,json,sys
FILES=sys.argv[1:] or ["help/live-pages/agenda.html","invite/pages/agenda.html"]
for f in FILES:
    s=open(f).read(); o=s
    a='mine?`<button class="jbtn on" data-id="${t.id}">You\'re in</button>`'
    b='mine?(t.live?`<button class="jbtn on" data-id="${t.id}">Go back in</button>`:`<button class="jbtn on" data-id="${t.id}">You\'re in</button>`)'
    if 'Go back in</button>' not in s: s=s.replace(a,b)
    a='if(!on){t.live?openJoin(t):openSheet(t);return}'
    if a in s and 'tc-goback' not in s:
        s=s.replace(a,a+'\n    if(t.live){/* tc-goback */if(!tcSatGet(t))tcSatSet(t);openJoin(t);return}',1)
    m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
    if '"Go back in":' not in s: s=s[:m.end()]+'"Go back in":["Rientra","Volver a entrar","Ξαναμπές"],'+s[m.end():]
    open(f,'w').write(s); print(f,'patched' if s!=o else 'unchanged', s.count('Go back in</button>'))
