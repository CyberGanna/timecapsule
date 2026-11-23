# Adds the "Mind-blown" reaction (option A Burst, Karim 2026-11-23) to the Live Table.
# Karim: not a button in the bottom bar; you send it TO a person. So each other person's
# video tile gets a small round mind-blown button (bottom-right; on hover/focus on desktop,
# after tapping the tile on phones). Sending pops the emoji calmly over THAT person's tile
# with a small "from <name>" caption. Re-run after rebuilding the Live Table. Idempotent.
import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
f = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "live-table/timecapsule-live-table.html"
s = f.read_text()
if "MB_SVG" in s:
    print("already patched"); sys.exit()
svg = (root / "emoji-mindblown/mind-blown.svg").read_text()
svg = re.sub(r"\s*\n\s*", "", svg).replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg aria-hidden="true" ')

# 1. i18n
s = s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={"Mind-blown":["Sbalordito","Alucinante","Εντυπωσιακό"],"from":["da","de","από"],"from you":["da te","de ti","από εσένα"],', 1)

# 2. CSS
css = """
/* mind-blown reaction, sent to one person from their tile */
.mbb{z-index:3;position:absolute;right:8px;bottom:8px;width:34px;height:34px;border-radius:50%;border:0;background:rgba(14,20,48,.72);display:grid;place-items:center;padding:0;cursor:pointer;opacity:0;transform:scale(.9);transition:opacity .15s,transform .15s,background .15s}
.mbb svg{width:22px;height:22px;display:block}
.mbb:hover{background:rgba(14,20,48,.95);transform:scale(1.06)}
.tile:hover .mbb,.tile:focus-within .mbb,.tile.open .mbb{opacity:1;transform:none}
.mbb.sent{background:rgba(23,195,200,.3);opacity:1}
.mbfloat{position:fixed;z-index:40;pointer-events:none;display:flex;flex-direction:column;align-items:center;gap:3px;animation:mbpop 2.4s cubic-bezier(.2,.7,.3,1) forwards}
.mbfloat svg{display:block}
.mbfloat em{font-style:normal;font-size:11px;font-weight:600;line-height:1;padding:3px 7px;border-radius:6px;background:rgba(14,20,48,.78);color:var(--fg);white-space:nowrap}
@keyframes mbpop{0%{opacity:0;transform:translateY(0) scale(.5)}14%{opacity:1;transform:translateY(-6px) scale(1.12)}26%{transform:translateY(-10px) scale(1)}75%{opacity:1}100%{opacity:0;transform:translateY(-60px) scale(.95)}}
@media (prefers-reduced-motion:reduce){.mbfloat{animation:mbfade 2s ease forwards}@keyframes mbfade{0%,80%{opacity:1}100%{opacity:0}}}
@media (max-width:720px){.mbb{right:4px;bottom:4px;width:26px;height:26px}.mbb svg{width:17px;height:17px}.mbfloat em{font-size:9.5px;padding:2px 5px}}
"""
s = s.replace("</style>", css + "</style>", 1)

# 3. Button on every other person's tile (template in renderStage), before the acts block
anchor = '      ${me?"":`<div class="acts">'
assert anchor in s
btn = ('      ${me?"":`<button class="mbb" type="button" data-mb="${p.n}" title="Mind-blown" aria-label="Mind-blown: ${p.n}">${MB_SVG}</button>`}\n')
s = s.replace(anchor, btn + anchor, 1)

# 4. JS (before renderStage so MB_SVG exists when tiles render)
js = """const MB_SVG='""" + svg + """';
function mindBlown(to,from){const t=document.querySelector('.tile[data-n="'+to+'"]');if(!t)return;const r=t.getBoundingClientRect();
  const z=Math.round(Math.min(52,r.width*.34)),el=document.createElement("div");el.className="mbfloat";
  el.innerHTML=MB_SVG+'<em>'+(from===ME?'<span>from you</span>':'<span>from</span> '+from)+'</em>';
  el.querySelector("svg").style.cssText="width:"+z+"px;height:"+z+"px";
  document.body.appendChild(el);const w=el.offsetWidth,h=el.offsetHeight;
  el.style.left=(r.left+r.width/2-w/2+(Math.random()-.5)*r.width*.2)+"px";el.style.top=(r.top+r.height*.42-h/2)+"px";
  setTimeout(()=>el.remove(),2500)}
document.addEventListener("click",e=>{const b=e.target.closest("[data-mb]");
  if(!b){const t=e.target.closest(".tile");if(t&&S.role!=="mod"&&t.dataset.n!==ME){const o=t.classList.contains("open");document.querySelectorAll(".tile.open").forEach(x=>x.classList.remove("open"));if(!o)t.classList.add("open")}return}e.stopPropagation();
  if(b.classList.contains("sent"))return;mindBlown(b.dataset.mb,ME);b.classList.add("sent");setTimeout(()=>b.classList.remove("sent"),1500)},true);
setTimeout(()=>mindBlown("Omar","Priya"),6000);
"""
anchor2 = "function renderStage(){"
assert anchor2 in s
s = s.replace(anchor2, js + anchor2, 1)
f.write_text(s)
print("patched", f)
