import re,json
N=open('../invite/pages/notifications.html',encoding='utf8').read()
head=N.split('<style>\n/* Notifications page */',1)[0]
D={}
for f in ['dict1.txt','dict2.txt','dict3.txt','dict4.txt','dict5.txt','dict6.txt']:
  for ln in open('../i18n/'+f,encoding='utf8'):
    if ln.strip():e,i,s=ln.rstrip('\n').split('|');D[e]=[i,s]
for f in ['../invite/dict-invite.txt','dict-coins.txt']:
  for ln in open(f,encoding='utf8'):
    if ln.strip():e,i,s=ln.rstrip('\n').split('|');D[e]=[i,s]
js='window.TCI18N_DICT='+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';\n'+open('../i18n/i18n-core.js',encoding='utf8').read()
tag='<script id="tc-i18n">'+js.replace('</','<\\/')+'</script>'
head=re.sub(r'<script id="tc-i18n">.*?</script>',lambda m:tag,head,count=1,flags=re.S)
def rep(a,b):
  global head
  assert a in head,a[:70]; head=head.replace(a,b)
rep('<title>TimeCapsule Notifications</title>','<title>TimeCapsule TimeCoins</title>')
rep('<button class="tch-ic here" type="button" data-tch="ntfhere" aria-current="page" aria-label="Notifications, new">','<a class="tch-ic" href="https://claude.ai/artifact/SggBcVnWacDjzBsZeke1D1" target="_top" aria-label="Notifications, new">')
head=re.sub(r'(<a class="tch-ic" href="https://claude.ai/artifact/SggBcVnWacDjzBsZeke1D1".*?<i class="tch-d"></i>)</button>',r'\1</a>',head,count=1,flags=re.S)
out=head+open('body.html',encoding='utf8').read()
open('timecapsule-timecoins.html','w',encoding='utf8').write(out)
print(len(D),len(out))
