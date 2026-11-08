import re,json,sys,os
D='/mnt/project-files/edge-states/'
LIVE=sys.argv[1]; OUT=sys.argv[2]
css=open(D+'inject.css').read(); parts=open(D+'inject_parts.js').read()
av=re.search(r'(const HAIR=.*?\nconst P=.*?\nfunction av\(n\).*?\n)',open('/mnt/project-files/help/live-pages/settings.html').read(),re.S).group(1)
parts=parts.replace('/*AVATARS*/',av)
CFG={
 'table':dict(hide=['#page'],states=['full','cancelled','removed'],ctl='table'),
 'mytables':dict(hide=['body>div.wrap','#main'],newu='new-mytables',ctl='chip'),
 'people':dict(hide=['body>div.wrap','body>div.filters','body>main.wrap'],newu='new-following',ctl='chip'),
 'notifications':dict(hide=['body>div.wrap'],newu='new-notifications',ctl='chip'),
 'chats':dict(hide=['#app'],newu='new-chats',ctl='chip'),
 'profile':dict(hide=['#vprofile'],newu='new-profile',ctl='profile'),
}
dicts=[l.rstrip('\n').split('|') for l in open(D+'dict-edge.txt',encoding='utf8') if l.strip()]
ctl=r'''
const CFG=%s;
let box=null,cur='';
function sync(){document.querySelectorAll('[data-e]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.e===cur))}
function show(s){cur=s||'';const els=CFG.hide.map(q=>document.querySelector(q)).filter(Boolean);
 if(!cur){els.forEach(e=>e.style.removeProperty('display'));if(box){box.remove();box=null}document.body.classList.remove('tce-newu');sync();return}
 if(!els.length)return;
 els.forEach(e=>e.style.setProperty('display','none','important'));
 if(!box){box=document.createElement('div');box.id='tce';els[0].parentNode.insertBefore(box,els[0]);
  box.addEventListener('click',onClick);box.addEventListener('submit',onSubmit)}
 box.innerHTML=S[cur]();document.body.classList.toggle('tce-newu',cur.startsWith('new-'));
 if(cur==='new-mytables')mt('up');sync();window.scrollTo(0,0)}
function ui(){
 if(CFG.ctl==='chip'){const d=document.createElement('div');d.className='e-chip';d.setAttribute('role','group');d.setAttribute('aria-label','Prototype');
  d.innerHTML='<b>Prototype</b><span class="e-seg"><button type="button" data-e="">Regular</button><button type="button" data-e="'+CFG.newu+'">New user</button></span>';document.body.appendChild(d)}
 if(CFG.ctl==='table'){const w=document.querySelector('.proto .wrap');if(w)w.insertAdjacentHTML('beforeend','<span class="pg" role="group" aria-label="State"><button type="button" data-e="">Open table</button><button type="button" data-e="full">Full</button><button type="button" data-e="cancelled">Cancelled</button><button type="button" data-e="removed">Removed</button></span>')}
 if(CFG.ctl==='profile'){const w=document.getElementById('proto');if(w)w.insertAdjacentHTML('beforeend','<span class="pseg" role="group" aria-label="Account" style="margin-left:12px"><button type="button" data-e="">Established</button><button type="button" data-e="new-profile">New member</button></span>')}
 document.addEventListener('click',e=>{const b=e.target.closest('[data-e]');if(!b)return;e.preventDefault();show(b.dataset.e)});
 const tk=(location.hash||'').replace(/^#/,'').split(/[&,]/);
 let s='';if(CFG.newu&&tk.includes('new'))s=CFG.newu;(CFG.states||[]).forEach(x=>{if(tk.includes(x))s=x});
 sync();if(s)show(s)}
'''
def build(key):
  h=open(LIVE+'/'+key+'.html',encoding='utf8').read()
  h=re.sub(r'<style id="tce-css">.*?</script><!--/tce-->','',h,flags=re.S)
  m0=re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n',h,re.S)
  dct=json.loads(m0.group(1))
  for e,i,s in dicts:dct[e]=[i,s]
  nd='window.TCI18N_DICT='+json.dumps(dct,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+';\n'
  h=h[:m0.start()]+'<script id="tc-i18n">'+nd+h[m0.end():]
  c=CFG[key]
  # convert body handlers to named functions
  p=parts
  js='(function(){\n'+p+ctl%json.dumps(c)+'\nif(document.readyState==="loading")document.addEventListener("DOMContentLoaded",ui);else ui();\n})();'
  sheet='<div class="e-toast" id="e-toast" role="status"></div><div class="e-scrim" id="e-scrim" hidden><div class="e-sheet" role="dialog" aria-modal="true" aria-labelledby="e-sh-t"><h2 id="e-sh-t">Tell us what happened</h2><p>A person on our team will read it. The host won\'t see what you write.</p><textarea id="e-sh-x" placeholder="What happened at the table?" aria-label="What happened"></textarea><div class="e-acts"><button class="e-btn e-sm" type="button" id="e-sh-c">Cancel</button><button class="e-btn e-sm e-pri" type="button" id="e-sh-s">Send</button></div></div></div>'
  snip='<style id="tce-css">'+css+'</style>'+sheet+'<script id="tce-js">'+js.replace('</script','<\\/script')+'</script><!--/tce-->'
  i=h.rfind('<footer class="tcf"')
  if i<0:i=h.rfind('</body>')
  h=h[:i]+snip+'\n'+h[i:]
  open(OUT+'/'+key+'.html','w',encoding='utf8').write(h)
  print(key,len(h))
for k in (sys.argv[3:] or CFG):build(k)

import subprocess
subprocess.run(["python3","/mnt/project-files/i18n/add-greek.py"]+[OUT+"/"+k+".html" for k in (sys.argv[3:] or CFG)],check=True)
