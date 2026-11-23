"""Karim 2026-11-22 "use this format": the Table page sheets (Ready to join? / Welcome back / Save a chair) show the table
as a compact row like the Tables page list: a rounded tile (picture, or white topic icon on the topic-colour glow),
then the title and the topic with its dot. Replaces the wide card from patch_sumcard.py. Idempotent, marker "tc-sumrow"."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['table-detail/timecapsule-table.html', 'help/live-pages/table.html', 'invite/pages/table.html']
NEW = ('function sumHTML(){/*tc-sumcard*//*tc-sumrow*/const t=T(),c=TOPIC_C[t.topic]||"#A9B0D6";let im=null;'
       'if(st.kind==="host"){try{im=JSON.parse(sessionStorage.getItem("tc-created")||"{}").img}catch(e){}}else im=TD_IMG[st.kind]||TD_IMG.open;'
       'return `<div class="sth" style="background:radial-gradient(circle at 35% 30%,${c},${c}66 75%,#252B52)">${im?`<img src="${im}" alt="">`:`<svg viewBox="0 0 24 24" aria-hidden="true">${TICON[t.topic]||""}</svg>`}</div>'
       '<div class="si" style="--c:${c}"><b>${t.title}</b><span class="sumtp"><i></i>${t.topic}</span></div>`}')
CSS = '''<style id="tc-sumrow">
.sum{display:flex!important;align-items:center;gap:16px;padding:14px!important;overflow:visible;background:var(--field,#20264A)!important;border:1px solid var(--line)!important;border-radius:16px}
.sum::after{display:none}
.sum .sth{flex:none;width:64px;height:64px;border-radius:16px;overflow:hidden;display:grid;place-items:center}
.sum .sth img{width:100%;height:100%;object-fit:cover;display:block}
.sum .sth svg{width:46%;height:46%;fill:none;stroke:#fff;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;opacity:.9;filter:drop-shadow(0 1px 4px rgba(0,0,0,.3))}
.sum .si{padding:0!important;min-width:0}
.sum b{font-family:inherit!important;font-weight:600!important;font-size:17px!important;line-height:1.3!important;margin:0 0 6px!important;color:#EEF1FF}
.sum .sumtp{display:flex;align-items:center;gap:8px;font-size:13.5px;color:#C9CFF0}
.sum .sumtp i{width:8px;height:8px;border-radius:50%;background:var(--c)}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-sumrow' in s: continue
    m = re.search(r'function sumHTML\(\)\{/\*tc-sumcard\*/.*?</div>`\}', s, flags=re.S)
    assert m, rel
    s = s[:m.start()] + NEW + s[m.end():]
    k = s.rfind('</body>'); s = (s[:k] + CSS + s[k:]) if k >= 0 else (s + CSS)
    open(p, 'w', encoding='utf8').write(s); print(rel)
