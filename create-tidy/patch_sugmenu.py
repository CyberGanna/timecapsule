"""Gabriele 2026-11-22: suggestions in Create a table become a dropdown menu.
A small "Suggestions" button under the question box opens a list; picking one fills the box (and its topic) and closes it.
Idempotent, marker "tc-sugmenu". Run after create-tidy/patch.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
OLD = ('<div class="sparks"><!--tc-ctidy--><span class="sl">Suggestions</span>${SPARKS.map(([q,th])=>`<button data-spark="${q}" data-sth="${th}">${q}</button>`).join("")}</div></div>')
NEW = ('<div class="sparks sgm"><!--tc-ctidy--><!--tc-sugmenu--><button type="button" class="sgbtn" aria-expanded="false" aria-haspopup="true"><span>Suggestions</span>'
       '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>'
       '<div class="sgl" role="menu" hidden>${SPARKS.map(([q,th])=>`<button role="menuitem" data-spark="${q}" data-sth="${th}"><i style="background:${THEMES[th]||"#A9B0D6"}"></i><span>${q}</span><small>${th}</small></button>`).join("")}</div></div></div>')
CSS = '''<style id="tc-sugmenu">
#cpage .sparks.sgm{position:relative!important;display:block!important;margin:10px 0 0!important}
#cpage .sgbtn{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px 0 14px;border-radius:999px;border:1px solid var(--line);background:none;color:var(--text);font:inherit;font-size:13.5px;cursor:pointer}
#cpage .sgbtn:hover,#cpage .sgbtn[aria-expanded="true"]{border-color:rgba(238,241,255,.35)}
#cpage .sgbtn svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;transition:transform .15s}
#cpage .sgbtn[aria-expanded="true"] svg{transform:rotate(180deg)}
#cpage .sgl{position:absolute;left:0;top:38px;z-index:30;min-width:300px;max-width:100%;padding:6px;border-radius:12px;background:#262C55;border:1px solid var(--line);box-shadow:0 14px 34px rgba(0,0,0,.35)}
#cpage .sgl[hidden]{display:none}
#cpage .sgl button{display:flex!important;align-items:center;gap:10px;width:100%;height:auto!important;min-height:40px;padding:8px 10px!important;border:0!important;border-radius:8px!important;background:none!important;color:var(--text);font:inherit;font-size:14px!important;text-align:left;cursor:pointer;white-space:normal!important}
#cpage .sgl button:hover,#cpage .sgl button:focus-visible{background:rgba(255,255,255,.06)!important;outline:none}
#cpage .sgl i{width:7px;height:7px;border-radius:50%;flex:none}
#cpage .sgl span{flex:1}
#cpage .sgl small{color:var(--mute);font-size:12px;flex:none}
</style><script>/* tc-sugmenu */
document.addEventListener("click",e=>{
  const t=e.target.closest&&e.target.closest("#cpage .sgm .sgbtn");
  document.querySelectorAll("#cpage .sgm .sgl").forEach(l=>{const b=l.parentNode.querySelector(".sgbtn");
    const open=t&&b===t&&l.hidden; l.hidden=!open; b.setAttribute("aria-expanded",String(open));});
},true);/* capture: the Create page stops click bubbling */
document.addEventListener("keydown",e=>{if(e.key==="Escape")document.querySelectorAll("#cpage .sgm .sgl:not([hidden])").forEach(l=>{l.hidden=true;const b=l.parentNode.querySelector(".sgbtn");b.setAttribute("aria-expanded","false");b.focus()})});
</script>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-sugmenu' in s: continue
    assert s.count(OLD) == 1, rel
    s = s.replace(OLD, NEW)
    k = s.rindex('</body>'); s = s[:k] + CSS + s[k:]
    open(p, 'w', encoding='utf8').write(s); print(rel)
