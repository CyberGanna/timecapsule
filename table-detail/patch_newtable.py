"""Karim 2026-11-18: "Go to my table" on the Create a table success screen opens the Table page of the new table.

Table page: #new=1&q=<title>&th=<topic>&seats=N&tl=<language>&tr=1|0&vis=open|private&now=1 shows that table in the host view.
Run after patch_mytables_link.py and patch_mytables_past.py (idempotent, marker "tc-new").
"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TP = os.path.join(ROOT, 'table-detail/timecapsule-table.html')
s = open(TP, encoding='utf8').read()
if 'tc-new' not in s:
    a = 'addEventListener("hashchange",()=>{if(/[#&]t=\\d+/.test(location.hash))location.reload()});'
    assert s.count(a) == 1
    s = s.replace(a, '''/* tc-new: the table you just created (Karim 2026-11-18) */
(function(){const h=new URLSearchParams((location.hash||"").slice(1));if(!h.has("new"))return;
  const q=h.get("q")||"What you want to discuss";
  TABLES.host={title:q,topic:h.get("th")||"Philosophy",host:"You",seats:+h.get("seats")||8,lang:h.get("tl")||"English",transcript:h.get("tr")!=="0",
    people:["You"],talk:"You",slug:q.toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"").slice(0,40),invites:0,desc:""};
  st.kind="host";st.isNew=1;if(h.get("now")==="1"){st.time="live";st.liveSince=Date.now()}else if(+h.get("at"))st.startAt=+h.get("at")})();
''' + a)
    b = '  if(isLive()) return `<div class="cd live" id="cd"><span class="lab">Talking for</span>'
    assert s.count(b) == 1
    s = s.replace(b, '  if(isLive()&&st.isNew) return `<div class="cd live" id="cd"><span class="lab">Starting now</span></div>`;\n' + b)
    s = s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={"Starting now":["Si comincia ora","Empieza ahora","Ξεκινά τώρα"],', 1)
    open(TP, 'w', encoding='utf8').write(s); print('new table patched')
