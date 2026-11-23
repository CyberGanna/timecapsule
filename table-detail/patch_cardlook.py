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
function tdSection(){
  const t=T(),c=TOPIC_C[t.topic],m=isLive()?Math.round((Date.now()-st.liveSince)/60000):0;
  return `<section class="td tdc${isLive()?" live":""}" style="--c:${c}">
    <div class="tdhd"><img src="${TD_IMG[st.kind]}" alt="">${isLive()?`<div class="cc-hour tdhour"><i style="width:${Math.min(100,m/60*100)}%%"></i></div>`:""}</div>
    <div class="tdin">
     <div class="tdm">${tdTop()}<h1>${t.title}</h1>${tdHost()}<p class="desc">${t.desc}</p>${tdFaces()}</div>
     <div class="tda">${isLive()?"":cdHTML()}${actionsHTML()}</div>
    </div>
   </section>`;
}
</script>'''

CSS = r'''<style id="td-card-css">
.td.tdc{display:block;position:relative;padding:0;margin:24px 0 8px;border-radius:22px;overflow:hidden;background:radial-gradient(120%% 70%% at 0%% 0%%,color-mix(in srgb,var(--c) 9%%,transparent),transparent 60%%),#20264A;box-shadow:0 1px 0 rgba(255,255,255,.04) inset,0 12px 30px rgba(5,8,25,.25)}
.td.tdc::after{content:"";position:absolute;inset:0;border:1px solid #323A6C;border-radius:inherit;pointer-events:none;z-index:4}
.tdhd{position:relative;height:280px;overflow:hidden;background:#252B52}
.tdhd img{width:100%%;height:100%%;object-fit:cover;display:block}
.tdhd::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,25,54,0) 55%%,rgba(32,38,74,.6))}
.tdhd .tdhour{position:absolute;left:0;right:0;top:auto;bottom:0;height:3px;background:rgba(238,241,255,.10);z-index:2}
.tdhd .tdhour i{display:block;height:100%%;background:var(--c);border-radius:0 3px 3px 0}
.tdin{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:44px;padding:30px 34px 32px;align-items:start}
.tdm .cc-top{display:flex;align-items:center;flex-wrap:wrap;gap:10px 18px;font-size:14px;color:#C9CFF0}
.tdm .cc-topic{display:flex;align-items:center;gap:8px}.tdm .cc-topic i{width:9px;height:9px;border-radius:50%%;background:var(--c)}
.tdm .cc-live{font-size:12.5px;font-weight:600;letter-spacing:.14em;color:#3DDC84;white-space:nowrap}
.tdm .cc-live span{color:#A9B0D6;font-weight:400;letter-spacing:0;margin-left:6px}
.tdm .cc-when{font-size:13.5px;color:#A9B0D6}
.tdm h1{font-family:Literata,Georgia,serif;font-weight:500;font-size:clamp(28px,3.4vw,38px);line-height:1.22;letter-spacing:-.01em;padding-bottom:.08em;margin:16px 0 6px;color:#EEF1FF}
.tdm .cc-host{display:flex;align-items:center;flex-wrap:wrap;gap:0 5px;font-size:15px;color:#A9B0D6}
.tdm .cc-host b{color:#C9CFF0;font-weight:500;cursor:pointer}.tdm .cc-host .tchip{margin-left:8px}
.tdm .desc{margin:18px 0 0;color:var(--soft);font-size:16px;line-height:1.6;max-width:640px}
.tdf{margin-top:26px;display:flex;flex-direction:column;gap:10px}
.tdf-row{display:grid;grid-auto-flow:column;grid-auto-columns:40px;gap:8px;justify-content:start}
.tdf-row>span,.tdf-row>em,.tdf-row>i{width:100%%;aspect-ratio:1;border-radius:50%%;overflow:hidden;display:block;box-sizing:border-box}
.tdf-row>span{cursor:pointer}.tdf-row svg,.tdf-row img{width:100%%;height:100%%;display:block}
.tdf-row>span.talk{box-shadow:0 0 0 2px #20264A,0 0 0 4px #17C3C8}
.tdf-row>i{background:rgba(238,241,255,.14)}
.tdf-row>em{border:1.5px dashed rgba(238,241,255,.28)}
.tdf-cap{font-size:13.5px;color:#A9B0D6}
.tda{padding:22px;border-radius:16px;background:rgba(14,18,44,.35);border:1px solid #2C3366}
.tda .cd{margin:0 0 4px}
.tda .acts2{margin:0;flex-direction:column;align-items:stretch;gap:10px}
.tda .cd+.acts2{margin-top:18px}
.tda .acts2 .btn{width:100%%;height:46px}
.tda .acts2 .lnk{align-self:center}
.tda .hint{margin-top:14px;font-size:13px;line-height:1.5}
.tda .gate h3{margin-top:0}
@media (max-width:960px){.tdin{grid-template-columns:1fr;gap:26px}.tdhd{height:220px}}
@media (max-width:640px){.td.tdc{margin-top:16px;border-radius:18px}.tdhd{height:170px}.tdin{padding:20px 18px 20px;gap:22px}.tdm h1{font-size:25px;margin-top:12px}.tdm .desc{font-size:15px}.tdf-row{grid-auto-columns:32px;gap:6px}.tda{padding:16px}}
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
