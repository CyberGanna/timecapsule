# Builds Guides + FAQ pages. Usage: python3 build.py <GUIDES_URL> <FAQ_URL>
# Live: Guides https://claude.ai/artifact/WHk7qYCmXBgugxJW1kqevd  FAQ https://claude.ai/artifact/LTQdD5XzBLaDbCRrhHttMK
import re,json,sys
G,F=sys.argv[1],sys.argv[2]
N=open('../invite/pages/notifications.html',encoding='utf8').read()
head=N.split('<style>\n/* Notifications page */',1)[0]
D={}
for f in ['dict1.txt','dict2.txt','dict3.txt','dict4.txt','dict5.txt','dict6.txt']:
  for ln in open('../i18n/'+f,encoding='utf8'):
    if ln.strip():e,i,s=ln.rstrip('\n').split('|');D[e]=[i,s]
for f in ['../invite/dict-invite.txt','../timecoins/dict-coins.txt','dict-help.txt','dict-host.txt']:
  for ln in open(f,encoding='utf8'):
    if ln.strip():e,i,s=ln.rstrip('\n').split('|');D[e]=[i,s]
# Moderator -> Host rename (2026-11-08): drop old moderator strings, dict-host.txt carries the host ones
D={k:v for k,v in D.items() if not re.search(r'moderat|open circle',k+v[0]+v[1],re.I)}
js='window.TCI18N_DICT='+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';\n'+open('../i18n/i18n-core.js',encoding='utf8').read()
tag='<script id="tc-i18n">'+js.replace('</','<\\/')+'</script>'
head=re.sub(r'<script id="tc-i18n">.*?</script>',lambda m:tag,head,count=1,flags=re.S)
def rep(h,a,b):
  assert a in h,a[:70]; return h.replace(a,b)
head=rep(head,'<button class="tch-ic here" type="button" data-tch="ntfhere" aria-current="page" aria-label="Notifications, new">','<a class="tch-ic" href="https://claude.ai/artifact/SggBcVnWacDjzBsZeke1D1" target="_top" aria-label="Notifications, new">')
head=re.sub(r'(<a class="tch-ic" href="https://claude.ai/artifact/SggBcVnWacDjzBsZeke1D1".*?<i class="tch-d"></i>)</button>',r'\1</a>',head,count=1,flags=re.S)
SET='<a href="https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy" target="_top">Settings</a>'
foot=open('footer.html',encoding='utf8').read().replace('GUIDES_URL',G).replace('FAQ_URL',F)
for name,title,body,cur in [('guides','TimeCapsule Guides','guides-body.html',G),('faq','TimeCapsule FAQ','faq-body.html',F)]:
  h=rep(head,'<title>TimeCapsule Notifications</title>','<title>'+title+'</title>')
  h=rep(h,SET,SET+'<a href="'+G+'" target="_top"'+(' aria-current="page"' if name=='guides' else '')+'>Help</a>')
  ft=foot.replace('<a href="'+cur+'" target="_top">','<a href="'+cur+'" target="_top" aria-current="page">',1)
  b=open(body,encoding='utf8').read().replace('GUIDES_URL',G).replace('FAQ_URL',F).replace('<!--FOOTER-->',ft)
  out=h+b
  open('timecapsule-'+name+'.html','w',encoding='utf8').write(out)
  print(name,len(out))
