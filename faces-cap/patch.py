"""Tables page list rows: at most 10 circles in a face stack; beyond that, 9 faces + a "+N" chip.
Idempotent. Re-run after rebuilding agenda/create pages."""
import sys
OLD='const fc=t.people.map((p,i)=>`<span data-u="${p}" tabindex="0" style="z-index:${t.people.length+1-i}">${av(p)}</span>`).join("")+(mine?`<span class="you" style="z-index:0">${av("You")}</span>`:"");'
NEW='/*tc-facecap*/const _fa=t.people.concat(mine?["You"]:[]),_fx=_fa.length>10?_fa.length-9:0,_fs=_fx?_fa.slice(0,9):_fa;const fc=_fs.map((p,i)=>p==="You"&&mine&&i===_fa.length-1?`<span class="you" style="z-index:0">${av("You")}</span>`:`<span data-u="${p}" tabindex="0" style="z-index:${_fs.length+1-i}">${av(p)}</span>`).join("")+(_fx?`<span class="fmore" data-x="${_fx}" style="z-index:0">+${_fx}</span>`:"");'
CSS='<style id="tc-facecap">.fc .fmore{display:inline-grid;place-items:center;background:#2E3563;color:#EEF1FF;font-size:11px;font-weight:600;letter-spacing:-.02em;cursor:default}.fc .fmore:hover{transform:none}.chairs .lf{min-width:0;max-width:100%}</style>'
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    if 'tc-facecap' in s: continue
    assert OLD in s,f
    s=s.replace(OLD,NEW)
    i=s.rfind('</body>'); s=s[:i]+CSS+s[i:] if i>=0 else s+CSS
    open(f,'w',encoding='utf-8').write(s); print('patched',f)

# Part 2: if the stack is still wider than its column (phone list rows), hide faces from the right
# and grow the "+N" chip so the faces never run under the button.
JS='<script id="tc-facefit">(function(){function fit(){document.querySelectorAll(".chairs .fc").forEach(function(fc){var c=fc.closest(".chairs");if(!c)return;var W=c.clientWidth;var fs=[].filter.call(fc.children,function(x){return !x.classList.contains("fmore")});var m=fc.querySelector(".fmore");var base=m?+(m.getAttribute("data-x")||0):0;fs.forEach(function(x){x.style.display=""});var tot=fs.length+(base?1:0);var n=Math.max(2,Math.floor((W-26)/18)+1);var t;if(tot<=n){if(m){t=base?"+"+base:"";if(m.textContent!==t)m.textContent=t;m.style.display=base?"":"none"}return}var keep=n-1;fs.slice(keep).forEach(function(x){x.style.display="none"});if(!m){m=document.createElement("span");m.className="fmore";m.setAttribute("data-x","0");m.style.zIndex="0";fc.appendChild(m)}m.style.display="";t="+"+(base+fs.length-keep);if(m.textContent!==t)m.textContent=t})}var busy=false;function q(){if(busy)return;busy=true;requestAnimationFrame(function(){busy=false;fit()})}new MutationObserver(q).observe(document.documentElement,{childList:true,subtree:true});addEventListener("resize",q);if(document.readyState!=="loading")q();else document.addEventListener("DOMContentLoaded",q)})();</script>'
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    if 'tc-facefit' in s: continue
    s=s.replace('<span class="fmore" style="z-index:0">+${_fx}</span>','<span class="fmore" data-x="${_fx}" style="z-index:0">+${_fx}</span>')
    i=s.rfind('</body>'); s=s[:i]+JS+s[i:] if i>=0 else s+JS
    open(f,'w',encoding='utf-8').write(s); print('fit',f)
