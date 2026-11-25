"""Gabriele 2026-11-23: alias suggestions (join sheet, "An alias") become a dropdown like Create a table's Suggestions:
a "Suggestions ▾" button opens a menu (alias + the book it comes from); picking one fills the box and closes the menu.
Idempotent, marker "tc-aliasmenu". Re-run after rebuilding agenda/create."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
OLD = 'document.getElementById("sugg").innerHTML=`<span class="kfrom">Suggestions</span>`+[...set].map(a=>`<button data-sugg="${a}" title="${KB[a][1]} · ${KB[a][2]}">${a}<small>${KB[a][1]}</small></button>`).join("");'
NEW = ('/*tc-aliasmenu*/for(let n=0;set.size<6&&n<60;n++)set.add(rndAlias());'
       'document.getElementById("sugg").innerHTML=`<button type="button" class="sgbtn" aria-expanded="false" aria-haspopup="true"><span>Suggestions</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>'
       '<div class="sgl" role="menu" hidden>`+[...set].map(a=>`<button role="menuitem" data-sugg="${a}" title="${KB[a][1]} · ${KB[a][2]}"><span>${a}</span><small>${KB[a][1]}</small></button>`).join("")+`</div>`;')
CSS = '''<style id="tc-aliasmenu">
#sugg.sugg{display:block!important;position:relative;margin-top:10px}
#sugg .sgbtn{display:inline-flex!important;flex-direction:row!important;align-items:center;gap:6px;height:32px;padding:0 12px 0 14px!important;border-radius:999px!important;border:1px solid var(--line);background:none;color:var(--text);font:inherit;font-size:13.5px!important;cursor:pointer;line-height:1}
#sugg .sgbtn:hover,#sugg .sgbtn[aria-expanded="true"]{border-color:rgba(238,241,255,.35)}
#sugg .sgbtn svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;transition:transform .15s}
#sugg .sgbtn[aria-expanded="true"] svg{transform:rotate(180deg)}
#sugg .sgl{position:static;margin-top:8px;max-width:420px;padding:6px;border-radius:12px;background:#262C55;border:1px solid var(--line);box-shadow:0 14px 34px rgba(0,0,0,.35)}
#sugg .sgl[hidden]{display:none}
#sugg .sgl button{display:flex!important;flex-direction:row!important;align-items:center;justify-content:space-between;gap:12px;width:100%;min-height:40px;padding:8px 10px!important;border:0!important;border-radius:8px!important;background:none!important;color:var(--text);font:inherit;font-size:14px!important;text-align:left;cursor:pointer}
#sugg .sgl button:hover,#sugg .sgl button:focus-visible{background:rgba(255,255,255,.06)!important;outline:none}
#sugg .sgl small{font-size:12px!important;color:var(--mute);font-style:italic;flex:none}
</style><script>/* tc-aliasmenu */
document.addEventListener("click",e=>{const t=e.target.closest&&e.target.closest("#sugg .sgbtn");
  document.querySelectorAll("#sugg .sgl").forEach(l=>{const b=l.parentNode.querySelector(".sgbtn");const open=!!(t&&b===t&&l.hidden);l.hidden=!open;b.setAttribute("aria-expanded",String(open))})},true);
document.addEventListener("keydown",e=>{if(e.key==="Escape")document.querySelectorAll("#sugg .sgl:not([hidden])").forEach(l=>{l.hidden=true;const b=l.parentNode.querySelector(".sgbtn");b.setAttribute("aria-expanded","false");b.focus()})});
</script>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-aliasmenu' in s: continue
    assert s.count(OLD) == 1, rel
    s = s.replace(OLD, NEW)
    k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel)
