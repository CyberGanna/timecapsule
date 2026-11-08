# Apply the coin wording change to a live page copy: python3 apply.py in.html out.html
import re,json,sys
h=open(sys.argv[1],encoding='utf8').read()
i=h.find('<!doctype html><html lang="en">')
if i>0:h=h[i:]
h=re.sub(r'(</body></html>\s*)+$','</body></html>\n',h.rstrip()+'\n')
R=[l.rstrip('\n').split('|') for l in open('/mnt/project-files/legal/coin-sweep/replacements.txt',encoding='utf8') if l.strip()]
m=re.search(r'window\.TCI18N_DICT=(\{.*?\});\n',h,re.S)
D=json.loads(m.group(1));n=0
for old,new,it,es in R:
  D[new]=[it,es]
  body_before=h.count(old)
  if body_before: n+=body_before
js=json.dumps(D,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
h=h[:m.start(1)]+js+h[m.end(1):]
for old,new,it,es in R:
  for v in (old, old.replace("'","&#39;"), old.replace("'","’")):
    h=h.replace(v,new)
open(sys.argv[2],'w',encoding='utf8').write(h)
left=[o for o,_,_,_ in R if o in h]
print(sys.argv[1].split('/')[-1],'hits',n,'left',left)
