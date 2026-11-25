"""My tables: an unrated past table (guest) shows "N days left to rate" (7-day window, Gabriele 2026-11-19). Idempotent."""
import re,json
IT={1:"Ancora 1 giorno per votare"};ES={1:"Queda 1 día para valorar"};EL={1:"Απομένει 1 μέρα για βαθμολόγηση"}
T={}
for n in range(1,8):
    k="1 day left to rate" if n==1 else "%d days left to rate"%n
    T[k]=[IT.get(n,"Ancora %d giorni per votare"%n),ES.get(n,"Quedan %d días para valorar"%n),EL.get(n,"Απομένουν %d μέρες για βαθμολόγηση"%n)]
for f in ["help/live-pages/mytables.html","invite/pages/mytables.html"]:
    s=open(f).read()
    if 'left to rate' in s: print('unchanged',f); continue
    a='if(isHost(t)) return `<small><b>${t.people.length-1} guests</b> · ★'
    assert a in s,f
    s=s.replace(a,'if(!isHost(t)&&!t.rated){const d=Math.min(7,Math.max(1,7-Math.floor((Date.now()-(+t.at))/864e5)));return `<small><b>${t.host}</b> hosted · <span class="unsv">${d===1?"1 day":d+" days"} left to rate</span></small>`}\n    '+a,1)
    m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
    s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k,ensure_ascii=False),json.dumps(v,ensure_ascii=False)) for k,v in T.items())+s[m.end():]
    open(f,'w').write(s); print('patched',f)
e=open('i18n/dict-el.txt').read()
add=''.join('%s|%s\n'%(k,v[2]) for k,v in T.items() if k+'|' not in e)
if add: open('i18n/dict-el.txt','a').write(add)
