"""Table page states Full and Cancelled (prototype bar) built on the Open table template
(Gabriele 2026-11-23): photo card on the left with the state message where the buttons go,
Who's coming + Details on the right, Tables with free chairs below.
Idempotent, marker "tce-v3". Run after patch_cardlook.py (uses its CSS and TD_IMG)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["table-detail/timecapsule-table.html"]  # only this copy has the edge states

HELPERS = r'''/* tce-v3: Full and Cancelled on the Open table template */
const V3C={Gregory:'Switzerland',Lena:'Germany',Omar:'Morocco',Mia:'France',Priya:'India',Kofi:'Ghana',Noah:'Canada',Ruth:'United Kingdom'};
const v3img=()=>typeof TD_IMG!=="undefined"?TD_IMG.open:"";
const v3host=`<div class="cc-host"><span>with</span> <b>Gregory</b> · <span>Switzerland</span> <span class="e-trust">${I.tshield}Trusted</span></div>`;
const v3facts=w=>{let f=typeof factsHTML==="function"?factsHTML():"";return f.replace(/(<dt>When<\/dt>)<dd>[\s\S]*?<\/dd>/,`$1<dd>${w}</dd>`)};
const v3who=(h,ppl,n)=>`<div class="tds-who"><h2>${h} <small>${ppl.length} / ${n}</small></h2><ul class="who2">${ppl.map((p,i)=>`<li><span class="pa">${av(p)}</span><div><b>${p}</b><small>${i===0?'<i class="mt">Host</i> · ':''}${V3C[p]||''}</small></div></li>`).join('')}</ul></div>`;
const v3=(o)=>`<div class="wrap e-v3"><a class="back" href="${U.agenda}" target="_top">← Back to tables</a><section class="td tdc2${o.off?' v3-off':''}" style="--c:${T.Philosophy}">
 <article class="tdc"><div class="tdhd"><img src="${v3img()}" alt=""></div><div class="tdm">
  <div class="cc-top"><span class="cc-topic"><i></i>Philosophy</span>${o.when}</div>
  <h1>Is free will an illusion?</h1>${v3host}
  <div class="tda"><div class="e-note v3-note">${o.note}</div></div></div></article>
 <aside class="tdside">${o.side}</aside></section>${simRows()}</div>`;
'''
FULL = r''' full(){return v3({when:`<span class="cc-when">Tomorrow · 19:00</span><span class="v3-tag">Full</span>`,
  note:`<h2><span class="e-ni e-t">${I.seat}</span>This table is full</h2><p>All 8 chairs are taken. People sometimes give their chair back before it starts, so one may still open up.</p>
  <div class="e-acts" id="e-wl"><button class="e-btn e-pri" type="button" data-wl>${I.bell}Join the waitlist</button>${A(U.agenda,'See other tables','e-lnk')}</div>
  <p class="e-hint" id="e-wlh">${I.bell}If a chair opens, we ring your bell.</p>`,
  side:v3who("Who's coming",['Gregory','Lena','Omar','Mia','Priya','Kofi','Noah','Ruth'],8)+`<div class="tds-facts"><h2>Details</h2>${v3facts('Tomorrow, 19:00 – 20:00<span>your time</span>')}</div>`})},
 cancelled(){return v3({off:1,when:`<span class="v3-tag v3-x">Cancelled</span>`,
  note:`<h2><span class="e-ni e-r">${I.off}</span>Gregory cancelled this table</h2><p class="e-say">Sorry everyone, I'm unwell tonight. Same question next Thursday, and I'll invite you first.<span class="e-by">Gregory, 2 hours ago</span></p><p>Your chair is free again. There's nothing you need to do.</p>
  <div class="e-acts">${A(U.agenda,'Find another table')}<button class="e-lnk" type="button" data-fol>Follow Gregory</button></div><p class="e-hint" id="e-folh" hidden>${I.bell}We'll tell you when Gregory hosts next.</p>`,
  side:v3who("Who was coming",['Gregory','Lena','Omar','Mia','Priya'],8)+`<div class="tds-facts"><h2>Details</h2>${v3facts('Was tomorrow, 19:00 – 20:00<span>Cancelled by the host</span>')}</div>`})},
'''
CSS = '''<style id="tce-v3">
.e-v3{padding:8px 20px 80px!important;line-height:1.5}.e-v3 .back{margin-top:22px}
.e-v3 .td.tdc2{margin-bottom:64px}
.v3-note{margin:0!important;padding:0!important;border:0!important;background:none!important}
.v3-note h2{font-size:18px!important}
.tdm .v3-tag{font-size:13px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#F2C14E}
.tdm .v3-tag.v3-x{color:#FF9AA5}
.v3-off .tdhd img{filter:grayscale(1) brightness(.6)}
.v3-off .tdm h1{color:#A9B0D6}
.e-v3 .e-trust{margin-left:8px}
.e-v3 .e-more{margin-top:8px}
</style>'''

for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding="utf-8").read()
    if "tce-v3" not in s:
        m = re.search(r'\n full\(\)\{return .*?\n(?= removed\(\)\{)', s, flags=re.S)
        assert m, "full/cancelled not found"
        s = s[:m.start()] + "\n" + FULL + s[m.end():]
        k = s.index("const S={")
        s = s[:k] + HELPERS + s[k:]
        i = s.rindex("</body>"); s = s[:i] + CSS + s[i:]
        open(p, "w", encoding="utf-8").write(s)
    print("ok", rel)
