#!/usr/bin/env python3
"""Host again -> Create a table, prefilled from the last table.

Idempotent. Usage: python3 patch.py <file.html> [...]
- My tables copies: the "again" action opens Create a table with the table's
  topic, question, seats, language, open/private, transcript, weekday and time
  in the hash (#again=1&th=...&q=...), next to #lang.
- Create a table copies: reads that hash, fills the form, shows a short note.
Add new strings to /mnt/project-files/i18n/dict-el.txt as well.
"""
import re, sys, json

NOTE = "Filled in from your last table. Check the date and time."
TR = {"it": "Compilato dal tuo ultimo tavolo. Controlla data e ora.",
      "es": "Rellenado a partir de tu última mesa. Revisa la fecha y la hora.",
      "el": "Συμπληρώθηκε από το τελευταίο σου τραπέζι. Έλεγξε την ημερομηνία και την ώρα."}

MT_OLD = 'case "again":go(URLS.create);return;'
MT_NEW = 'case "again":go(againURL(t));return; /*tc-again*/'
MT_FN = ('/*tc-again-fn*/function againURL(t){const p=new URLSearchParams({again:"1",th:t.theme||"",q:t.title||"",'
         'seats:String(t.seats||8),tl:t.lang||"English",vis:(t.vis==="private"||t.private)?"private":"open",'
         'tr:t.transcript===false?"0":"1"});if(t.at){p.set("tm",hhmm(t.at));p.set("wd",String(t.at.getDay()))}'
         'return URLS.create+"#"+p.toString()}\n')

CR_ANCHOR = '/* standalone create page'
CR_JS = r'''/*tc-again-fn*/ /* Host again: prefill the form from the last table (#again=1&th=...&q=...) */
(function(){try{
  const h=new URLSearchParams(location.hash.slice(1)); if(!h.has("again")) return;
  const th=h.get("th"); if(th&&THEMES[th]) nt.theme=th;
  const q=(h.get("q")||"").replace(/[<>]/g,"").slice(0,90); if(q) nt.title=q;
  const s=+h.get("seats"); if(s>=3&&s<=10) nt.seats=s;
  const tl=h.get("tl"); if(["English","Italiano","Deutsch","Français","Español"].includes(tl)) nt.lang=tl;
  const v=h.get("vis"); if(v==="open"||v==="private") nt.vis=v;
  if(h.get("tr")==="0") nt.capsule=false;
  const tm=h.get("tm")||""; if(/^([01]\d|2[0-3]):(00|15|30|45)$/.test(tm)) nt.time=tm;
  const wd=h.get("wd")||""; if(/^[0-6]$/.test(wd)){const d=new Date(); d.setDate(d.getDate()+1); while(d.getDay()!==+wd) d.setDate(d.getDate()+1); nt.whenK="date"; nt.date=ymd(d)}
  try{history.replaceState(history.state,"",location.pathname+location.search)}catch(e){}
  const oc=openCreate; openCreate=function(){oc(); const h1=document.querySelector("#cpage h1"); if(h1&&!document.getElementById("again-note")) h1.insertAdjacentHTML("afterend",'<p class="nvh" id="again-note" style="margin:12px 0 0;font-size:14px">'+"NOTE"+'</p>')};
}catch(e){}})();
'''.replace('"NOTE"', json.dumps(NOTE))

def add_dict(h):
    if json.dumps(NOTE, ensure_ascii=False) + ':' in h[:400000]:
        return h
    i = h.find('window.TCI18N_DICT={')
    if i < 0:
        sys.exit('no TCI18N_DICT')
    j = i + len('window.TCI18N_DICT={')
    m = re.search(r'"Pick a date": ?\[([^\]]*)\]', h)
    greek = (m and m.group(1).count('"') >= 6) or 'Οδηγοί' in h[:200000]
    vals = [TR["it"], TR["es"]] + ([TR["el"]] if greek else [])
    entry = json.dumps(NOTE, ensure_ascii=False) + ':' + json.dumps(vals, ensure_ascii=False) + ','
    return h[:j] + entry + h[j:]

for f in sys.argv[1:]:
    h = open(f, encoding='utf8').read(); o = h
    if MT_OLD in h or MT_NEW in h:
        h = h.replace(MT_OLD, MT_NEW)
        if '/*tc-again-fn*/' not in h:
            k = h.find('function go(u){')
            h = h[:k] + MT_FN + h[k:]
    elif CR_ANCHOR in h:
        if '/*tc-again-fn*/' not in h:
            k = h.find(CR_ANCHOR)
            h = h[:k] + CR_JS + h[k:]
        h = add_dict(h)
    else:
        print('skip (not My tables / Create):', f); continue
    if h != o:
        open(f, 'w', encoding='utf8').write(h); print('patched', f)
    else:
        print('already patched', f)
