import re,json,io
S=open('settings.html',encoding='utf8').read().split('\n')
doc='\n'.join(S[1:])  # drop publish skeleton line
# dictionary
D={}
for f in ['dict1.txt','dict2.txt','dict3.txt','dict4.txt','dict5.txt','dict6.txt']:
  for ln in open(f,encoding='utf8'):
    if not ln.strip():continue
    e,i,s=ln.rstrip('\n').split('|');D[e]=[i,s]
js='window.TCI18N_DICT='+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';\n'+open('i18n-core.js',encoding='utf8').read()
tag='<script id="tc-i18n">'+js.replace('</','<\\/')+'</script>'
doc=re.sub(r'<script id="tc-i18n">.*?</script>',lambda m:tag,doc,count=1,flags=re.S)
doc=doc.replace('<title>TimeCapsule Settings</title>','<title>TimeCapsule Notifications</title>')
head,rest=doc.split('<style>\n/* Settings */',1)
def rep(a,b):
  global head
  assert a in head,a[:60]; head=head.replace(a,b)
# bell = this page; no dropdown here
rep('<button class="tch-ic" type="button" data-tch="ntf" aria-haspopup="true" aria-expanded="false" aria-label="Notifications, new">','<button class="tch-ic here" type="button" data-tch="ntfhere" aria-current="page" aria-label="Notifications, new">')
head=re.sub(r'<div class="tch-pop" data-tchp="ntf" hidden>.*?\n</div>\n','',head,count=1,flags=re.S)
rep('<a href="#" aria-current="page" data-tch="close">Settings</a>','<a href="https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy" target="_top">Settings</a>')
# avatar helpers from settings script
m=re.search(r'(const HAIR=.*?\nconst P=.*?\nfunction av\(n\).*?\n)',rest,re.S)
body=open('body.html',encoding='utf8').read().replace('/*AVATARS*/',m.group(1))
out=head+body
open('/mnt/project-files/notifications/timecapsule-notifications.html','w',encoding='utf8').write(out) if False else None
open('notifications.html','w',encoding='utf8').write(out)
print(len(D),len(out))
