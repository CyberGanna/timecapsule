"""Live Table: a guest who leaves early sees "You left the table" (Go back in / Done), not Rate and tip.
Rating opens when the table ends (Karim 2026-11-19). Prototype bar gets "Skip to the end ›". Idempotent."""
import re,json
f='live-table/timecapsule-live-table.html'; s=open(f).read()
if 'id="leftov"' not in s:
    CSS='''<style id="tc-left-css">
#leftov{position:fixed;inset:0;z-index:60;display:flex;align-items:center;justify-content:center;padding:24px 16px;background:var(--bg,#141B34)}
#leftov[hidden]{display:none!important}
#leftov .lcard{max-width:420px;text-align:center}
#leftov .lic{display:inline-flex;width:64px;height:64px;border-radius:50%;align-items:center;justify-content:center;background:rgba(45,212,191,.12);color:#2DD4BF;margin-bottom:18px}
#leftov .lic svg{width:28px;height:28px}
#leftov h2{margin:0 0 10px;font-size:26px;font-weight:600}
#leftov p{margin:0 auto;color:var(--muted,#9AA3C7);font-size:15px;line-height:1.5}
#leftov p.lsm{margin-top:14px;font-size:13px}
#leftov .lacts{display:flex;gap:10px;justify-content:center;margin-top:26px}
#leftov .lbtn{display:inline-flex;align-items:center;justify-content:center;height:46px;min-width:150px;padding:0 20px;border-radius:12px;font:inherit;font-size:15px;font-weight:600;text-decoration:none;cursor:pointer}
#leftov .lbtn.ghost{border:1px solid var(--line,rgba(255,255,255,.14));background:transparent;color:inherit}
#leftov .lbtn.go{border:0;background:#1BC3C7;color:#0B1430}
.proto{position:relative;z-index:70}
.proto .pskip{margin-left:10px;border:1px dashed currentColor;background:transparent;color:inherit;font:inherit;font-size:12px;padding:3px 10px;border-radius:999px;cursor:pointer;opacity:.85}
</style>'''
    OV='''<div id="leftov" hidden role="region" aria-labelledby="leftt"><div class="lcard">
<span class="lic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4H6a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h8M10 12h10M17 9l3 3-3 3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
<h2 id="leftt">You left the table</h2>
<p>The table is still going. You can go back in while it's live.</p>
<p class="lsm">Rating and tips open when the table ends. You'll have 7 days.</p>
<div class="lacts"><a class="lbtn ghost" href="../help/live-pages/agenda.html" target="_top">Done</a><button class="lbtn go" type="button" id="goback">Go back in</button></div>
</div></div>'''
    s=s.replace('</head>',CSS+'\n</head>',1)
    s=s.replace('<button type="button" data-role="mod" aria-pressed="false">Host</button></span></label>','<button type="button" data-role="mod" aria-pressed="false">Host</button></span></label><button type="button" class="pskip" id="skipEnd">Skip to the end ›</button>',1)
    old="location.href=role()==='mod'?'../library/timecapsule-library.html#save&as=host':'../rate-tip/timecapsule-rate-tip.html#as=guest'},true)"
    assert old in s
    s=s.replace(old,"if(role()==='mod'){location.href='../library/timecapsule-library.html#save&as=host'}else{document.getElementById('leftov').hidden=false;document.getElementById('goback').focus()}},true);\n"
      "document.getElementById('goback').addEventListener('click',function(){document.getElementById('leftov').hidden=true});\n"
      "document.getElementById('skipEnd').addEventListener('click',function(){location.href=role()==='mod'?'../library/timecapsule-library.html#save&as=host':'../rate-tip/timecapsule-rate-tip.html#as=guest'})",1)
    i=s.rfind('<script id="tc-flow">'); s=s[:i]+OV+'\n'+s[i:]
    T={"You left the table":["Hai lasciato il tavolo","Has salido de la mesa"],
    "The table is still going. You can go back in while it's live.":["Il tavolo continua. Puoi rientrare finché è in corso.","La mesa sigue. Puedes volver a entrar mientras esté en directo."],
    "Rating and tips open when the table ends. You'll have 7 days.":["Voti e mance si aprono quando il tavolo finisce. Avrai 7 giorni.","Las valoraciones y propinas se abren cuando termina la mesa. Tendrás 7 días."],
    "Go back in":["Rientra","Volver a entrar"],"Done":["Fatto","Listo"],"Skip to the end ›":["Vai alla fine ›","Ir al final ›"]}
    m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
    s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k,ensure_ascii=False),json.dumps(v,ensure_ascii=False)) for k,v in T.items() if '"%s":'%k not in s)+s[m.end():]
    open(f,'w').write(s); print('patched')
else: print('unchanged')
