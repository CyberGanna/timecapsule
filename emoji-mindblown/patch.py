# Adds the "Mind-blown" reaction (option A Burst, Karim 2026-11-23) to the Live Table.
# Button next to Raise hand; a calm one-shot pop floats up over the sender's tile.
# Re-run after rebuilding the Live Table. Idempotent.
import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
f = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "live-table/timecapsule-live-table.html"
s = f.read_text()
if "id=\"myblown\"" in s:
    print("already patched"); sys.exit()
svg = (root / "emoji-mindblown/mind-blown.svg").read_text()
svg = re.sub(r"\s*\n\s*", "", svg).replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg aria-hidden="true" ')

# 1. i18n
s = s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={"Mind-blown":["Sbalordito","Alucinante","Εντυπωσιακό"],', 1)

# 2. CSS
css = """
/* mind-blown reaction */
.cb .mbico{display:inline-flex}.cb .mbico svg{width:22px;height:22px}
.cb.sent{border-color:rgba(23,195,200,.5);background:rgba(23,195,200,.14)}
.mbfloat{position:fixed;z-index:40;width:48px;height:48px;pointer-events:none;animation:mbpop 2.2s cubic-bezier(.2,.7,.3,1) forwards}
.mbfloat svg{width:100%;height:100%;display:block}
@keyframes mbpop{0%{opacity:0;transform:translateY(0) scale(.5)}14%{opacity:1;transform:translateY(-6px) scale(1.12)}26%{transform:translateY(-10px) scale(1)}75%{opacity:1}100%{opacity:0;transform:translateY(-70px) scale(.95)}}
@media (prefers-reduced-motion:reduce){.mbfloat{animation:mbfade 1.8s ease forwards}@keyframes mbfade{0%,80%{opacity:1}100%{opacity:0}}}
"""
s = s.replace("</style>", css + "</style>", 1)

# 3. Button after Raise hand
s = s.replace('<button class="cb" id="myhand" type="button"></button>',
  '<button class="cb" id="myhand" type="button"></button>\n      <button class="cb" id="myblown" type="button" title="Mind-blown" aria-label="Mind-blown"><b class="mbico">' + svg + '</b><span>Mind-blown</span></button>', 1)

# 4. JS
js = """
let MB_SVG=document.querySelector("#myblown .mbico").innerHTML;
function mindBlown(n){const t=document.querySelector('.tile[data-n="'+n+'"]');if(!t)return;const r=t.getBoundingClientRect();
  const el=document.createElement("div");el.className="mbfloat";el.innerHTML=MB_SVG;
  const z=Math.round(Math.min(48,r.width*.36));el.style.width=el.style.height=z+"px";
  el.style.left=(r.right-z-10-Math.random()*z*.3)+"px";el.style.top=(r.bottom-z-14)+"px";
  document.body.appendChild(el);setTimeout(()=>el.remove(),2300)}
document.getElementById("myblown").onclick=e=>{const b=e.currentTarget;if(b.classList.contains("sent"))return;
  mindBlown(ME);b.classList.add("sent");setTimeout(()=>b.classList.remove("sent"),1500)};
setTimeout(()=>mindBlown("Priya"),6000);
"""
anchor = 'document.getElementById("mycam").onclick='
assert anchor in s
s = s.replace(anchor, js.strip() + "\n" + anchor, 1)
f.write_text(s)
print("patched", f)
