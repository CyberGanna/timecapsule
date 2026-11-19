"""Back from Send in a chat / Email returns to the "Your table is open!" screen (Karim 2026-11-18).
The screen is kept as #created + sessionStorage "tc-created". Idempotent, marker "tc-created". Run after patch.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def rep(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:100]); return s.replace(a, b)

RESTORE = '''
if(location.hash==="#created"){try{const c=JSON.parse(sessionStorage.getItem("tc-created")||"null");if(c){openCreate();Object.assign(nt,c.nt);if(c.img){IMGS.push(c.img);nt.img=IMGS.length-1}else nt.img=null;doCreate(c.link)}else showPage(false,false)}catch(e){}}
else if(location.hash==="#new")openCreate();'''

def run(rel):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if '"tc-created"' in s: return
    s = rep(s, 'function doCreate(){\n  const t=ntObj();', 'function doCreate(L){\n  const snap=JSON.parse(JSON.stringify(nt)), simg=nt.img!=null?IMGS[nt.img]:null;\n  const t=ntObj();')
    s = rep(s, 'const link=`timecapsule.app/t/${t.id}${Math.random().toString(36).slice(2,6)}`', 'const link=L||`timecapsule.app/t/${t.id}${Math.random().toString(36).slice(2,6)}`')
    s = rep(s, 'Object.assign(nt,{title:"",img:null,rep:"none"});',
            'try{sessionStorage.setItem("tc-created",JSON.stringify({nt:snap,img:simg,link}))}catch(e){try{sessionStorage.setItem("tc-created",JSON.stringify({nt:Object.assign(snap,{img:null}),img:null,link}))}catch(x){}}\n'
            '  try{history.replaceState({c:1},"",location.pathname+location.search+"#created")}catch(e){}\nObject.assign(nt,{title:"",img:null,rep:"none"});')
    s = rep(s, '  if(!on&&location.hash==="#new") try{', '  if(!on&&/^#(new|created)$/.test(location.hash)) try{')
    s = rep(s, 'addEventListener("popstate",()=>{if(location.hash!=="#new"&&', 'addEventListener("popstate",()=>{if(!/^#(new|created)$/.test(location.hash)&&')
    s = rep(s, '\nif(location.hash==="#new")openCreate();', RESTORE)
    if '\nopenCreate();\n</script>' in s: s = rep(s, '\nopenCreate();\n</script>', '\nif(location.hash!=="#created")openCreate();\n</script>')
    open(p, 'w', encoding='utf8').write(s); print(rel, 'back to the success screen')

for r in ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']:
    run(r)
