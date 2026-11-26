"""Gabriele 2026-11-22: topics in Create a table = one line of smaller pills, no colour dots, scroll sideways
(mouse wheel scrolls it too; soft fade at the edge shows there is more). Idempotent, marker "tc-trow". Run after create-tidy/patch.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
CSS = '''<style id="tc-trow">
#cpage .ntchips{display:flex!important;flex-wrap:nowrap!important;gap:6px;overflow-x:auto;scrollbar-width:none;padding:1px 28px 1px 0;margin-right:-1px;
 -webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 36px),transparent);mask-image:linear-gradient(90deg,#000 calc(100% - 36px),transparent)}
#cpage .ntchips.end{-webkit-mask-image:none;mask-image:none}
#cpage .ntchips::-webkit-scrollbar{display:none}
#cpage .ntchips .fch{flex:none;width:auto;height:32px;padding:0 13px;font-size:13.5px;gap:0}
#cpage .ntchips .fch i{display:none}
@media (max-width:640px){#cpage .ntchips{grid-template-columns:none}}
</style><script>/* tc-trow: wheel scrolls the topic row; fade hides at the end */
document.addEventListener("wheel",e=>{const r=e.target.closest&&e.target.closest("#cpage .ntchips");if(!r||r.scrollWidth<=r.clientWidth)return;if(Math.abs(e.deltaY)>Math.abs(e.deltaX)){r.scrollLeft+=e.deltaY;e.preventDefault()}},{passive:false});
document.addEventListener("scroll",e=>{const r=e.target;if(r&&r.classList&&r.classList.contains("ntchips"))r.classList.toggle("end",r.scrollLeft+r.clientWidth>=r.scrollWidth-2)},true);
</script>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-trow' in s: continue
    k = s.rindex('</body>'); s = s[:k] + CSS + s[k:]
    open(p, 'w', encoding='utf8').write(s); print(rel)
