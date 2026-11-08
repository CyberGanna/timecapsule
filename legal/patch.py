# Adds the Terms and privacy links to a live page copy.
# Usage: python3 patch.py <LEGAL_URL> <in.html> <out.html> [settings|signin|plain]
import re,json,sys
U,src,dst=sys.argv[1],sys.argv[2],sys.argv[3]
kind=sys.argv[4] if len(sys.argv)>4 else 'plain'
h=open(src,encoding='utf8').read()
i=h.find('<!doctype html><html lang="en">')
if i>0:h=h[i:]
h=re.sub(r'(</body></html>\s*)+$','</body></html>\n',h.rstrip()+'\n')
NEW={}
for ln in open('/mnt/project-files/legal/dict-patch.txt',encoding='utf8'):
  if ln.strip():e,a,b=ln.rstrip('\n').split('|');NEW[e]=[a,b]
m=re.search(r'window\.TCI18N_DICT=(\{.*?\});\n',h,re.S)
D=json.loads(m.group(1));D.update({k:v for k,v in NEW.items() if k not in D})
h=h[:m.start(1)]+json.dumps(D,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+h[m.end(1):]
LEG='<a href="{u}#guidelines" target="_top">Community guidelines</a><a href="{u}#terms" target="_top">Terms</a><a href="{u}#privacy" target="_top">Privacy</a>'.format(u=U)
if '<footer class="tcf"' in h and U not in h[h.find('<footer class="tcf"'):]:
  f=h.find('<footer class="tcf"');n=h.find('</nav>',f);h=h[:n]+LEG+h[n:]
  print('footer patched')
if kind=='settings':
  A='<p class="foot">'
  assert h.count(A)==1
  row='<div class="row"><div class="tx"><b>{t}</b><span>{d}</span></div><a class="lnk" href="'+U+'#{k}" target="_top">Read</a></div>'
  sec=('<section class="sec" id="legal" data-t="Terms and privacy">\n        <h2>Terms and privacy</h2>\n        <div class="rows">\n          '
   +row.format(t='Community guidelines',d='How we look after each other at the table.',k='guidelines')+'\n          '
   +row.format(t='Terms of service',d='The agreement between you and TimeCapsule.',k='terms')+'\n          '
   +row.format(t='Privacy policy',d='What we collect, who can see it and how you stay in control.',k='privacy')
   +'\n        </div>\n      </section>\n      ')
  h=h.replace(A,sec+A);print('settings section added')
open(dst,'w',encoding='utf8').write(h);print(dst,len(h))
