# Builds the Terms and privacy page (Community guidelines, Terms of service, Privacy policy).
# Usage: python3 build.py <LEGAL_URL>   Header/footer/i18n come from guides-live.html (a fresh read of the live Guides artifact).
import re,json,sys,html
U=sys.argv[1] if len(sys.argv)>1 else 'LEGAL_URL'
G='https://claude.ai/artifact/WHk7qYCmXBgugxJW1kqevd'
src=open('guides-live.html',encoding='utf8').read()
src=src[src.find('<!doctype html><html lang="en">'):]
head=src.split('<style>\n/* Guides page */',1)[0]
foot=re.search(r'<style id="tcf-css">.*?</footer>',src,re.S).group(0)
def rep(h,a,b):
  assert a in h,a[:80]; return h.replace(a,b,1)
head=rep(head,'<title>TimeCapsule Guides</title>','<title>TimeCapsule Terms and Privacy</title>')
head=rep(head,'href="'+G+'" target="_top" aria-current="page">Help</a>','href="'+G+'" target="_top">Help</a>')
# dictionary
m=re.search(r'window\.TCI18N_DICT=(\{.*?\});\n',head,re.S)
D=json.loads(m.group(1))
for ln in open('dict-legal.txt',encoding='utf8'):
  if ln.strip():e,i,s=ln.rstrip('\n').split('|');D[e]=[i,s]
docs={};order=[];cur=None
for ln in open('content.txt',encoding='utf8'):
  ln=ln.rstrip('\n')
  if not ln.strip():continue
  p=ln.split('|')
  if p[0]=='DOC':cur=p[1];order.append(cur);docs[cur]=[];continue
  assert len(p)==4,ln[:60]
  D[p[1]]=[p[2],p[3]];docs[cur].append((p[0],p[1]))
js=json.dumps(D,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
head=head[:m.start(1)]+js+head[m.end(1):]
E_=html.escape
DRAFT='<p class="draft"><svg><use href="#i-draft"/></svg><span><b>Draft for review.</b> A lawyer must check these texts before launch, and the details in square brackets still need filling in.</span></p>'
TITLES={'guidelines':'Community guidelines','terms':'Terms of service','privacy':'Privacy policy'}
EXTRA={'guidelines':'<div class="help"><a href="'+G+'#report" target="_top">Report someone</a><a href="'+G+'" target="_top">Read the Guides</a></div>',
 'terms':'','privacy':'<div class="help"><a href="https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy#danger" target="_top">Open Settings</a></div>'}
out=[]
for n,k in enumerate(order):
  it=docs[k];a=['<article class="art" id="d-'+k+'" hidden>','<a class="back" href="#"><svg><use href="#i-left"/></svg>All pages</a>']
  ul=False;sec=False
  def close():
    global ul,sec
    if ul:a.append('</ul>');ul=False
  for t,x in it:
    if t!='B':close()
    if t=='T':a.append('<h1>'+E_(x)+'</h1>')
    elif t=='L':a.append('<p class="lede">'+E_(x)+'</p><p class="meta">Draft of 8 November 2026</p>'+DRAFT)
    elif t=='S':a.append('<div class="inshort"><small>In short</small><p>'+E_(x)+'</p></div>')
    elif t=='H':
      if sec:a.append('</section>')
      a.append('<section><h2>'+E_(x)+'</h2>');sec=True
    elif t=='P':a.append('<p>'+E_(x)+'</p>')
    elif t=='B':
      if not ul:a.append('<ul>');ul=True
      a.append('<li>'+E_(x)+'</li>')
  close()
  if sec:a.append('</section>')
  a.append(EXTRA[k])
  pv=order[n-1] if n>0 else None;nx=order[n+1] if n+1<len(order) else None
  a.append('<div class="next">'+('<a href="#'+pv+'"><small>Previous</small><b>'+TITLES[pv]+'</b></a>' if pv else '<span></span>')+('<a class="r" href="#'+nx+'"><small>Next</small><b>'+TITLES[nx]+'</b></a>' if nx else '')+'</div>')
  a.append('</article>')
  out.append('\n'.join(a))
# footer: add legal links
NAV_END='<a href="https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy" target="_top">Settings</a></nav>'
LEG='<a href="{u}#guidelines" target="_top">Community guidelines</a><a href="{u}#terms" target="_top">Terms</a><a href="{u}#privacy" target="_top">Privacy</a>'
ft=rep(foot,NAV_END,NAV_END.replace('</nav>','')+LEG.format(u=U)+'</nav>')
ft=ft.replace('href="'+U+'#','href="#').replace('href="#guidelines" target="_top"','href="#guidelines"').replace('href="#terms" target="_top"','href="#terms"').replace('href="#privacy" target="_top"','href="#privacy"')
body=open('body.html',encoding='utf8').read().replace('<!--DRAFT-->',DRAFT).replace('<!--DOCS-->','\n'.join(out)).replace('<!--FOOTER-->',ft)
res=head+body
open('timecapsule-legal.html','w',encoding='utf8').write(res)
open('footer-legal-snippet.txt','w',encoding='utf8').write(LEG.format(u=U))
print(len(res),len(D))
