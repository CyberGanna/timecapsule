"""Gabriele 2026-11-23: picking a suggestion in Create a table scrolls the topic row so the auto-selected topic is in view.
Idempotent, marker "tc-sugscroll". Run after create-tidy/patch_sugmenu.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
JS = '''<script>/* tc-sugscroll */(function(){
function show(smooth){document.querySelectorAll("#cpage .ntchips").forEach(function(r){var b=r.querySelector('.fch[aria-pressed="true"]');if(!b)return;
 var L=b.getBoundingClientRect().left-r.getBoundingClientRect().left+r.scrollLeft,W=b.offsetWidth,pad=28;
 if(L>=r.scrollLeft&&L+W<=r.scrollLeft+r.clientWidth-pad)return;
 var x=Math.max(0,L-(r.clientWidth-W)/2);if(r.scrollTo)r.scrollTo({left:x,behavior:smooth?"smooth":"auto"});else r.scrollLeft=x;});}
document.addEventListener("click",function(e){if(e.target.closest&&e.target.closest("[data-spark]")){setTimeout(function(){show(true)},40)}},true);
})();</script>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-sugscroll' in s: continue
    k = s.rindex('</body>'); s = s[:k] + JS + s[k:]
    open(p, 'w', encoding='utf8').write(s); print(rel)
