import re,json
L='/mnt/project-files/help/live-pages/settings.html'
s=open(L,encoding='utf8').read()
m0=re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n(.*?)</script>',s,re.S)
D=json.loads(m0.group(1).replace('<\\/','</'))
core=m0.group(2)
for ln in open('dict-edge.txt',encoding='utf8'):
  if ln.strip():
    parts=ln.rstrip('\n').split('|');assert len(parts)==3,ln;D[parts[0]]=parts[1:]
js='window.TCI18N_DICT='+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';\n'
tag='<script id="tc-i18n">'+js.replace('</','<\\/')+core+'</script>'
s=s[:m0.start()]+tag+s[m0.end():]
head,rest=s.split('<style>\n/* Settings */',1)
def rep(a,b):
  global head
  assert a in head,a[:60]; head=head.replace(a,b)
rep('<title>TimeCapsule Settings</title>','<title>TimeCapsule Edge Screens</title>')
rep('<a href="#" aria-current="page" data-tch="close">Settings</a>','<a href="https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy" target="_top">Settings</a>')
m=re.search(r'(const HAIR=.*?\nconst P=.*?\nfunction av\(n\).*?\n)',rest,re.S)
foot=rest[rest.index('<style id="tcf-css">'):]
foot=foot[:foot.index('</footer>')+9]+'\n</body></html>\n'
body=open('body.html',encoding='utf8').read().replace('/*AVATARS*/',m.group(1))
out=head+body+foot
open('timecapsule-edge.html','w',encoding='utf8').write(out)
print(len(D),len(out))
