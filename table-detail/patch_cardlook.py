"""Table page redesigned to match the new Tables page cards (Karim 2026-11-23).

Photo header (same photo as the table's card), hour bar, topic dot + LIVE / time line,
the question in Literata, "with Host · Country", a row of seat faces with dashed free chairs,
and the actions in a panel on the right. Replaces the old seat ring stage.
Idempotent: run on the three copies of the Table page after any rebuild.
"""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["table-detail/timecapsule-table.html", "help/live-pages/table.html", "invite/pages/table.html"]

ag = open(os.path.join(ROOT, "help/live-pages/agenda.html"), encoding="utf-8").read()
m = re.search(r'const CCPOOL=\[\.\.\.IMGS,"(data:[^"]+)","(data:[^"]+)"', ag)
assert m, "CCPOOL not found in agenda.html"
IMG_OPEN, IMG_INV = m.group(1), m.group(2)   # galaxy = free will card (id 1), sunset for the private invite

JS = r'''<script id="td-card">
const TD_IMG={open:"%s",inv:"%s"};
function tdFaces(){
  const t=T(),ppl=people(),hide=isOut()||(st.kind==="inv"&&!st.accepted),free=Math.max(0,t.seats-ppl.length);
  const f=ppl.map(p=>hide?`<i aria-hidden="true"></i>`:`<span${p!=="You"?` data-u="${p}" tabindex="0"`:""}${isLive()&&p===t.talk?' class="talk"':""}>${av(p)}</span>`).join("")+Array.from({length:free},()=>`<em aria-hidden="true"></em>`).join("");
  return `<div class="tdf"><span class="tdf-row">${f}</span><span class="tdf-cap"><span>${ppl.length} at the table</span> · <span>${free?free+(free===1?" chair free":" chairs free"):"Table full"}</span></span></div>`;
}
function tdTop(){
  const t=T();let w;
  if(isLive()) w=`<span class="cc-live">LIVE<span class="lmin" data-of="1">${Math.round((Date.now()-st.liveSince)/60000)} of 60 min</span></span>`;
  else{const d=new Date(st.startAt);w=`<span class="cc-when">${dayLabel(d)} · ${hhmm(d)}</span>`}
  return `<div class="cc-top"><span class="cc-topic"><i></i>${t.topic}</span>${w}${st.kind==="inv"?`<span class="ppill">${I.lock}<span>Private</span></span>`:""}</div>`;
}
function tdHost(){
  const t=T(),p=PROF[t.host];
  return `<div class="cc-host"><span>with</span> <b data-u="${t.host}" tabindex="0">${t.host}</b> · <span>${p[0]}</span>${p[4]?` <span class="tchip" title="Trusted host">${SHIELD}<span>Trusted</span></span>`:""}</div>`;
}
function tdHdImg(){ /* new table: host's picture from Create, else topic icon on topic colour */
  const t=T();if(st.kind==="host"){let im=null;try{im=JSON.parse(sessionStorage.getItem("tc-created")||"{}").img}catch(e){}
   return im?`<img src="${im}" alt="">`:`<div class="tcplain"><svg viewBox="0 0 24 24" aria-hidden="true">${TICON[t.topic]||TICON.Philosophy}</svg></div>`}
  return `<img src="${TD_IMG[st.kind]||TD_IMG.open}" alt="">`;
}
function tdSection(){
  const t=T(),c=TOPIC_C[t.topic],m=isLive()?Math.round((Date.now()-st.liveSince)/60000):0;
  /* two sections (Karim 2026-11-23): the card on the left, people and details on the right */
  return `<section class="td tdc2${isLive()?" live":""}" style="--c:${c}">
    <article class="tdc">
     <div class="tdhd">${tdHdImg()}${isLive()?`<div class="cc-hour tdhour"><i style="width:${Math.min(100,m/60*100)}%%"></i></div>`:""}</div>
     <div class="tdm">${tdTop()}<h1>${t.title}</h1>${tdHost()}
      <div class="tda">${isLive()?"":cdHTML()}${actionsHTML()}</div></div>
    </article>
    <aside class="tdside">
     <div class="tds-who">${whoHTML()}</div>
     <div class="tds-facts"><h2>Details</h2>${factsHTML()}</div>
    </aside>
    <div class="tds-good">${goodHTML()}</div>
   </section>`;
}
</script>'''

CSS = r'''<style id="td-card-css">
.td.tdc2{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:44px;align-items:start;padding:0;margin:24px 0 64px}
.tdc{position:relative;border-radius:22px;overflow:hidden;background:radial-gradient(120%% 70%% at 0%% 0%%,color-mix(in srgb,var(--c) 9%%,transparent),transparent 60%%),#20264A;box-shadow:0 1px 0 rgba(255,255,255,.04) inset,0 12px 30px rgba(5,8,25,.25)}
.tdc::after{content:"";position:absolute;inset:0;border:1px solid #323A6C;border-radius:inherit;pointer-events:none;z-index:4}
.tdhd{position:relative;height:190px;overflow:hidden;background:#252B52}
.tdhd img{width:100%%;height:100%%;object-fit:cover;display:block}
.tdhd::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,25,54,0) 55%%,rgba(32,38,74,.6))}
.tdhd .tdhour{position:absolute;left:0;right:0;top:auto;bottom:0;height:3px;background:rgba(238,241,255,.10);z-index:2}
.tdhd .tdhour i{display:block;height:100%%;background:var(--c);border-radius:0 3px 3px 0}
.tdm{padding:26px 28px 28px}
.tdm .cc-top{display:flex;align-items:center;flex-wrap:wrap;gap:10px 18px;font-size:14px;color:#C9CFF0}
.tdm .cc-topic{display:flex;align-items:center;gap:8px}.tdm .cc-topic i{width:9px;height:9px;border-radius:50%%;background:var(--c)}
.tdm .cc-live{font-size:12.5px;font-weight:600;letter-spacing:.14em;color:#3DDC84;white-space:nowrap}
.tdm .cc-live span{color:#A9B0D6;font-weight:400;letter-spacing:0;margin-left:6px}
.tdm .cc-when{font-size:13.5px;color:#A9B0D6}
.tdm h1{font-family:Literata,Georgia,serif;font-weight:500;font-size:clamp(26px,2.8vw,34px);line-height:1.24;letter-spacing:-.01em;padding-bottom:.08em;margin:14px 0 6px;color:#EEF1FF}
.tdm .cc-host{display:flex;align-items:center;flex-wrap:wrap;gap:0 5px;font-size:15px;color:#A9B0D6}
.tdm .cc-host b{color:#C9CFF0;font-weight:500;cursor:pointer}.tdm .cc-host .tchip{margin-left:8px}
.tdm .desc{margin:16px 0 0;color:var(--soft);font-size:15.5px;line-height:1.6}
.tda{margin-top:24px;padding-top:22px;border-top:1px solid #2C3366}
.tda .cd{margin:0 0 18px}
.tda .acts2{margin:0;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.tda .acts2 .btn{width:100%%;height:46px;padding:0 14px}
.tda .acts2>:only-child{grid-column:1/-1}
.tda .acts2 .lnk{justify-self:center;align-self:center}
.tda .hint{margin-top:14px;font-size:13px;line-height:1.5}
.tda .gate h3{margin-top:0}.tda .gate{padding:0;border:0;background:none}
.tcplain{position:absolute;inset:0;display:grid;place-items:center;background:radial-gradient(45%% 65%% at 18%% 30%%,color-mix(in srgb,var(--c) 60%%,transparent),transparent 70%%),radial-gradient(50%% 70%% at 85%% 75%%,rgba(124,92,255,.5),transparent 70%%),radial-gradient(40%% 55%% at 70%% 12%%,rgba(23,195,200,.33),transparent 70%%),radial-gradient(45%% 65%% at 25%% 95%%,color-mix(in srgb,var(--c) 36%%,transparent),transparent 70%%),#252B52}
.tcplain svg{width:52px;height:52px;fill:none;stroke:#fff;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;opacity:.92}
.tdside{display:flex;flex-direction:column;gap:36px;min-width:0;padding-top:4px}
.tdside h2{font-size:18px;font-weight:500;margin:0 0 14px;letter-spacing:-.2px}
.tdside h2 small{font-size:13px;color:var(--mute);font-weight:400;margin-left:8px}
.tdside .who2{grid-template-columns:repeat(3,minmax(0,1fr));gap:2px 12px}.tdside .who2 li{gap:10px}.tdside .who2 .pa{width:34px;height:34px}
.tdside{gap:28px}
.tdside .facts2{margin:0;grid-template-columns:1fr;border-top:1px solid var(--line)}
.tdside .facts2>div:nth-child(2){display:none} /* chairs: already shown in At the table */
.tdside .facts2>div{padding:10px 0;gap:14px}
.tdside .facts2>div:last-child{border-bottom:0}
.tdc2.live .tda .hint{display:none}
.td.tdc2{align-items:stretch}.tdc{display:flex;flex-direction:column}.tdm{flex:1;display:flex;flex-direction:column}.tdm .tda{margin-top:auto}.tdm .cc-host{margin-bottom:24px}.tds-good{align-self:start} /* Karim 2026-11-23: no camera/turns line under Join table */
.tdside .facts2>div>div{display:grid;grid-template-columns:110px minmax(0,1fr);column-gap:12px;flex:1}
.tdside .facts2 dt{font-size:13.5px;color:var(--mute);margin-top:1px}
.tdside .facts2 dd{margin:0;font-size:14.5px}
.tds-good{grid-column:1/-1;padding-top:30px;border-top:1px solid var(--line)}
.tds-good h2{font-size:18px;font-weight:500;margin:0 0 16px;letter-spacing:-.2px}
.tds-good .gk{grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
@media (max-width:960px){.tds-good .gk{grid-template-columns:1fr;gap:14px}}
@media (max-width:640px){.tdside .facts2>div>div{grid-template-columns:1fr}}
@media (max-width:960px){.td.tdc2{grid-template-columns:1fr;gap:36px}.tdhd{height:180px}}
@media (max-width:640px){.td.tdc2{margin-top:16px}.tdc{border-radius:18px}.tdhd{height:170px}.tdm{padding:20px 18px 20px}.tdm h1{font-size:25px;margin-top:12px}.tdm .desc{font-size:15px}.tdside .who2{grid-template-columns:1fr 1fr}}
</style>'''

for f in FILES:
    p = os.path.join(ROOT, f)
    s = open(p, encoding="utf-8").read()
    s = re.sub(r'<script id="td-card">.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<style id="td-card-css">.*?</style>', '', s, flags=re.S)
    # render: swap the whole old section for the card-style section
    if "${tdSection()}" not in s:
        s, n = re.subn(r'<section class="td">\s*<div class="stage.*?</section>', '${tdSection()}', s, count=1, flags=re.S)
        assert n == 1, f + ": old section not found"
    s = re.sub(r'\$\{tdSection\(\)\}\s*\$\{factsHTML\(\)\}\s*<section class="low">.*?</section>', '${tdSection()}', s, count=1, flags=re.S)
    if '"Details":' not in s:
        s = s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={"Details":["Dettagli","Detalles","Λεπτομέρειες"],', 1)
    s = s.replace('Array.from({length:Math.min(free,2)},()=>`<li class="free">', 'Array.from({length:free},()=>`<li class="free">')
    s = s.replace('<button type="button" data-act="msg"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg><span>Chat with guests</span></button>', '')
    # tick: live minutes read "41 of 60 min" and the hour bar grows
    old = 'document.querySelectorAll(".lmin").forEach(x=>x.textContent=m+" min");return}'
    new = 'document.querySelectorAll(".lmin").forEach(x=>x.textContent=m+(x.dataset.of?" of 60 min":" min"));document.querySelectorAll(".tdhour i").forEach(x=>x.style.width=Math.min(100,m/60*100)+"%");return}'
    if new not in s:
        assert old in s, f + ": tick not found"
        s = s.replace(old, new, 1)
    # helpers go right before the page script that defines render()
    i = s.find("function render(){")
    k = s.rfind("<script", 0, i)
    s = s[:k] + (JS % (IMG_OPEN, IMG_INV)) + s[k:]
    j = s.rfind("</body>")
    s = s[:j] + (CSS % ()) + s[j:] if j >= 0 else s + (CSS % ())
    if "family=Literata" not in s:
        s2 = s.replace('family=Sora:wght@300;400;500;600&display=swap', 'family=Sora:wght@300;400;500;600&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap', 1)
        if s2 == s:
            s2 = s.replace("</head>", '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap">\n</head>', 1) if "</head>" in s else s.replace('<script id="td-card">', '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap"><script id="td-card">', 1)
        s = s2
    open(p, "w", encoding="utf-8").write(s)
    print("ok", f)
