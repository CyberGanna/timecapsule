"""FAQ: 'When can I rate a table?' (Gabriele 2026-11-19). Idempotent."""
import re
Q="When can I rate a table?"
A="When the table ends, if you sat at it for at least 10 minutes. Leaving early is fine: you can still rate once it's over. You have 7 days, and the bell reminds you the day before rating closes."
T={Q:["Quando posso votare un tavolo?","¿Cuándo puedo valorar una mesa?","Πότε μπορώ να βαθμολογήσω ένα τραπέζι;"],
A:["Quando il tavolo finisce, se ci sei rimasto almeno 10 minuti. Puoi anche uscire prima: voti comunque quando è finito. Hai 7 giorni, e la campanella te lo ricorda il giorno prima della chiusura.","Cuando termina la mesa, si estuviste al menos 10 minutos. Puedes irte antes: igual valoras cuando acabe. Tienes 7 días, y la campana te lo recuerda el día antes del cierre.","Όταν τελειώσει το τραπέζι, αν έμεινες σε αυτό τουλάχιστον 10 λεπτά. Μπορείς να φύγεις νωρίτερα: βαθμολογείς κανονικά όταν τελειώσει. Έχεις 7 ημέρες, και το κουδουνάκι σού το θυμίζει την παραμονή του κλεισίματος."]}
HTML='<details><summary><span>%s</span><svg><use href="#i-plus"/></svg></summary><p>%s</p></details>\n'%(Q,A)
anchor='<details><summary><span>Why did some of my coins disappear?'
for f in ['help/faq-body.html','help/timecapsule-faq.html']:
    s=open(f).read()
    if Q in s.split('TCI18N_DICT')[-1] or ('<span>%s</span>'%Q) in s: print('skip',f); continue
    i=s.find(anchor); s=s[:i]+HTML+' '+s[i:]
    m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
    if m:
        import json
        s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k,ensure_ascii=False),json.dumps(v[:2],ensure_ascii=False)) for k,v in T.items())+s[m.end():]
    open(f,'w').write(s); print('patched',f)
d=open('help/dict-help.txt').read()
if Q not in d: open('help/dict-help.txt','a').write(''.join('%s|%s|%s\n'%(k,v[0],v[1]) for k,v in T.items()))
e=open('i18n/dict-el.txt').read()
if Q+'|' not in e: open('i18n/dict-el.txt','a').write(''.join('%s|%s\n'%(k,v[2]) for k,v in T.items()))
