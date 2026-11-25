"""Success screen: when the table is live now, the right button says "Start table" and opens the Live Table (Gabriele 2026-11-19). Idempotent; run after patch_look.py."""
import sys
FILES=sys.argv[1:] or ["help/live-pages/create.html","help/live-pages/agenda.html","invite/pages/create.html","invite/pages/agenda.html"]
for f in FILES:
    s=open(f).read(); o=s
    a='id="ntgo">Show table</button>`:`'
    if a in s: s=s.replace(a,'id="ntgo" data-live="1">Start table</button>`:`',1)
    a='if(b.id==="ntgo"){/* tc-new'
    if a in s and 'b.dataset.live' not in s:
        s=s.replace(a,'if(b.id==="ntgo"&&b.dataset.live){/* tc-start (Gabriele 2026-11-19) */top.location.href=(window.TCI18N?TCI18N.u:(x=>x))("../../live-table/timecapsule-live-table.html");return true}\n  '+a,1)
    a='window.TCI18N_DICT={'
    if '"Start table":' not in s and a in s:
        s=s.replace(a,a+'"Start table":["Avvia il tavolo","Iniciar la mesa","Ξεκίνα το τραπέζι"],',1)
    if s!=o: open(f,'w').write(s); print("patched",f)
    else: print("unchanged",f)
