"""Rejoining the same table keeps the name you first used there (Karim 2026-11-19).
After you press "Join the table", the camera check for that table shows "Welcome back" and your
name or alias locked, for 3 hours (prototype stand-in for "until the table ends").
Idempotent. Files: Tables page copies + Table page."""
import re,sys
FILES=sys.argv[1:] or ["help/live-pages/agenda.html","invite/pages/agenda.html","table-detail/timecapsule-table.html"]
JS=r'''<script id="tc-sat">
/* tc-sat: same name when you rejoin a table */
function tcSatAll(){try{return JSON.parse(localStorage.getItem("tc-sat")||"{}")}catch(e){return {}}}
function tcSatGet(t){const r=tcSatAll()[t&&t.title];return r&&Date.now()-r.at<3*3600e3?r:null}
function tcSatSet(t){if(!t)return;const a=tcSatAll();a[t.title]={mode:me.mode,alias:me.alias,col:me.col,at:Date.now()};try{localStorage.setItem("tc-sat",JSON.stringify(a))}catch(e){}}
function tcSatHTML(t){const r=tcSatGet(t);me.mode=r.mode;me.alias=r.alias||me.alias;if(r.col)me.col=r.col;
  const al=r.mode==="alias",nm=al?r.alias:"Gabriele",face=al?mono(nm,me.col,40):av("You");
  return `<div class="opt sat"><label class="l">You're back as</label>
    <div class="satrow">${face}<b data-noi18n>${nm}</b>${al?'<span class="satal">Alias</span>':""}<svg class="satlk" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 11V8a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></div>
    <p class="satn">You keep the same name until this table ends, so everyone knows who's back and the record stays clear.</p></div>`}
document.addEventListener("click",e=>{const b=e.target.closest&&e.target.closest("#enter");if(b)tcSatSet(window.__satT)},true);
</script>'''
CSS='''<style id="tc-sat-css">
.opt.sat .satrow{display:flex;align-items:center;gap:12px;margin-top:8px;padding:10px 14px;border:1px solid var(--line,rgba(255,255,255,.12));border-radius:14px;background:rgba(255,255,255,.03)}
.opt.sat .satrow>:first-child{width:40px;height:40px;flex:none;border-radius:50%;overflow:hidden}
.opt.sat .satrow b{font-size:15px;font-weight:600}
.opt.sat .satal{font-size:11px;font-weight:600;letter-spacing:.04em;padding:2px 8px;border-radius:999px;background:rgba(124,92,255,.18);color:#B9A8FF}
.opt.sat .satlk{width:16px;height:16px;margin-left:auto;color:var(--muted,#9AA3C7)}
.opt.sat .satlk{flex:none}
.opt.sat .satn{margin:8px 2px 0;font-size:13px;line-height:1.45;color:var(--muted,#9AA3C7)}
</style>'''
DICT={"Welcome back":["Bentornato","Bienvenido de nuevo"],"You're back as":["Rientri come","Vuelves como"],
"You keep the same name until this table ends, so everyone knows who's back and the record stays clear.":["Mantieni lo stesso nome finché il tavolo non finisce, così tutti sanno chi è tornato e il resoconto resta chiaro.","Mantienes el mismo nombre hasta que termine la mesa, así todos saben quién ha vuelto y el registro queda claro."]}
for f in FILES:
    s=open(f).read();o=s
    s=re.sub(r'\$\{aliasHTML\(\)\}(\s*<p class="anote")',r'${(window.__satT=t,tcSatGet(t)?tcSatHTML(t):aliasHTML())}\1',s,count=1)
    s=s.replace('<h2 id="sh-t">Ready to join?</h2>','<h2 id="sh-t">${tcSatGet(t)?"Welcome back":"Ready to join?"}</h2>',1)
    if 'getElementById("ain")) return;' not in s: s=re.sub(r'function wireAlias\(\)\{\n?','function wireAlias(){if(!document.getElementById("ain")) return;',s,count=1)
    if 'id="tc-sat"' not in s:
        i=s.rfind('</body>'); s=s[:i]+CSS+'\n'+JS+'\n'+s[i:]
    for k,v in DICT.items():
        m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
        if '"%s":['%k not in s and '"%s": ['%k not in s:
            s=s[:m.end()]+'"%s":["%s","%s"],'%(k,v[0],v[1])+s[m.end():]
    print(f, "patched" if s!=o else "unchanged", s.count('tcSatGet(t)?tcSatHTML'), s.count('if(!document.getElementById("ain")) return;'))
    open(f,'w').write(s)
