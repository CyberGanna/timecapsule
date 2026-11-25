"""Gabriele 2026-11-23: Live Table top bar.
1) LIVE mark like the Tables page cards: green LIVE text + pulsing dot, no filled box; elapsed time quiet next to it.
2) Language switch (EN|IT|ES|EL) moves from the header into the prototype bar, so the title gets the room.
Idempotent: re-run after rebuilding live-table/timecapsule-live-table.html."""
import sys
F=sys.argv[1] if len(sys.argv)>1 else "live-table/timecapsule-live-table.html"
s=open(F).read()
if 'tc-live-topbar' in s: print('unchanged',F); sys.exit()
o='<span class="lpill"><i></i><span id="clock">Live · 41:00</span></span>'
n='<span class="lpill" data-noi18n><i></i><b>Live</b><span id="clock">41:00</span></span>'
assert s.count(o)==1; s=s.replace(o,n)
o='document.getElementById("clock").textContent=`Live · ${'
assert s.count(o)==1; s=s.replace(o,'document.getElementById("clock").textContent=`${')
CSS='''<style id="tc-live-topbar">/* Gabriele 2026-11-23: LIVE as on the cards, language in the prototype bar */
.lpill{background:none;padding:0;border-radius:0;gap:8px;color:#3DDC84;font-size:13px;font-weight:700;letter-spacing:.1em;white-space:nowrap}
.lpill i{width:8px;height:8px;background:#3DDC84;position:relative;animation:none}
.lpill i::after{content:"";position:absolute;inset:0;border-radius:50%;background:#3DDC84;animation:tclpulse 1.8s ease-out infinite}
@keyframes tclpulse{0%{transform:scale(1);opacity:.7}100%{transform:scale(2.6);opacity:0}}
.lpill b{font-weight:700}
.lpill #clock{color:var(--mute);font-weight:500;letter-spacing:.02em;font-size:13px}
@media (prefers-reduced-motion:reduce){.lpill i::after{animation:none;opacity:0}}
.proto .tc-lp{margin:0;gap:6px}
.proto .tc-seg{display:inline-flex;padding:2px;border-radius:8px;background:var(--surface);border:1px solid var(--line)}
.proto .tc-seg button{border:0;background:none;color:var(--mute);font:inherit;font-size:12px;padding:3px 9px;border-radius:6px;cursor:pointer}
.proto .tc-seg button[aria-pressed="true"]{background:var(--raise)!important;color:var(--fg)!important;font-weight:400!important}
</style>
<script id="tc-live-lang">(function(){function mv(){var p=document.getElementById("proto"),lp=document.querySelector("header .tc-lp, .top .tc-lp");if(!p||!lp)return false;var l=document.createElement("label");l.className="tc-plang";l.setAttribute("data-noi18n","");var t=document.createElement("span");t.className="tc-lpl";l.appendChild(t);lp.classList.remove("h");l.appendChild(lp);var sk=document.getElementById("skipEnd");p.insertBefore(l,sk||null);var LB={en:"Language",it:"Lingua",es:"Idioma",el:"Γλώσσα"};function sy(){t.textContent=LB[(window.TCI18N&&TCI18N.lang)||"en"]}sy();lp.addEventListener("click",function(){setTimeout(sy,0)});return true}
function go(){if(!mv()){var n=0,iv=setInterval(function(){if(mv()||++n>40)clearInterval(iv)},50)}}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",function(){setTimeout(go,0)});else setTimeout(go,0)})();</script>
'''
i=s.rfind('</body>'); s=s[:i]+CSS+s[i:]
open(F,'w').write(s); print('patched',F)
