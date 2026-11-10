import json, sys, importlib
sys.path.insert(0, '.')
SVG = '<svg viewBox="0 -6 110 82" aria-hidden="true"><defs><clipPath id="ID"><circle cx="35" cy="35" r="30"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z"/></clipPath></defs><circle cx="35" cy="35" r="30" fill="#7C5CFF"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z" fill="#7C5CFF"/><circle cx="75" cy="35" r="30" fill="#17C3C8"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#17C3C8"/><g clip-path="url(#ID)"><circle cx="75" cy="35" r="30" fill="#3B2A9E"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#3B2A9E"/></g><g fill="#fff"><circle cx="36" cy="35" r="4.6"/><circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g></svg>'
from cutout import cut
SVG = cut(SVG, 'IDm')  # PDFs and presentations use the cut-out logo (transparent link)
WT = '<span class="wt"><b>time</b><i>capsule</i></span>'
EXTRA = """
.cover .intro{font-family:'Sora',sans-serif;font-weight:300;font-size:22px;color:#C9CCE4;margin-bottom:6px}
.cover .edition{font-family:'Sora',sans-serif;font-weight:300;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--teal);margin-top:22px}
.cover .toc{list-style:none;margin:16mm 0 0;padding-top:8mm;border-top:1px solid rgba(255,255,255,.12);font-family:'Sora',sans-serif;font-weight:300;font-size:11.5px;letter-spacing:.06em;color:#B9BCD6;columns:2;column-gap:12mm}
.cover .toc li{padding:0;margin:0 0 7px;font-size:11.5px;line-height:1.4}
.cover .toc li::before{display:none}
.cover .toc b{color:var(--teal);font-weight:600;margin-right:10px}
h1 .sub{display:block;font-size:20px;font-weight:300;color:var(--muted);margin-top:3mm}
h2{font-family:'Sora',sans-serif;font-weight:600;font-size:15px;color:var(--navy);margin:7mm 0 3mm;letter-spacing:-.005em}
h2:first-child{margin-top:0}
h3.q{font-family:'Sora',sans-serif;font-weight:600;font-size:13.5px;color:var(--navy);margin:7mm 0 3mm;line-height:1.35}
h3.q:first-child{margin-top:0}
p i{font-style:italic;color:var(--deep)}
.bel{position:relative;padding-left:12mm;font-size:12.5pt;line-height:1.55;margin-bottom:4mm}
.bel span{position:absolute;left:0;top:.3em;font-family:'Sora',sans-serif;font-size:9pt;font-weight:600;letter-spacing:.12em;color:var(--violet)}
.it{position:relative;padding-left:9mm;font-size:12.5pt;line-height:1.55;margin-bottom:4mm}
.it::before{content:"";position:absolute;left:0;top:.42em;width:10px;height:10px;border-radius:50%;border:2px solid var(--teal);background:#fff}
.it b{font-family:'Sora',sans-serif;font-weight:600;font-size:11.5pt;color:var(--navy)}
.body{position:absolute;left:26mm;right:26mm;top:30mm;bottom:24mm}
.page.cont .body{top:26mm}
/* compact (short edition) */
.compact p,.compact .bel,.compact .it{font-size:11.6pt;line-height:1.5;margin-bottom:3.2mm}
.compact p.lead{font-size:13pt;line-height:1.45}
.compact h1{font-size:30px;margin-bottom:7mm}
.compact h2{margin:5mm 0 2.4mm}
.compact .bel{font-size:11.2pt;line-height:1.45;margin-bottom:2.6mm}
.compact h1 .sub{font-size:17px;margin-top:2mm}
"""

def esc(s): return s

def blocks_html(sec):
    out = []
    for t, v in sec['blocks']:
        if t == 'lead': out.append('<p class="lead">%s</p>' % v)
        elif t == 'p': out.append('<p>%s</p>' % v)
        elif t == 'h2': out.append('<h2 data-keep="1">%s</h2>' % v)
        elif t == 'q': out.append('<h3 class="q" data-keep="1">%s</h3>' % v)
        elif t == 'ul':
            for a, b in v: out.append('<div class="it"><b>%s</b> %s</div>' % (a, b))
        elif t == 'bel':
            for i, b in enumerate(v): out.append('<div class="bel"><span>%02d</span>%s</div>' % (i + 1, b))
    return out

def build(lang, edition):
    C = importlib.import_module('content_' + lang)
    secs = C.FULL if edition == 'full' else C.SHORT
    css = open('base.css').read() + EXTRA
    data = [{'h1': s['h1'], 'foot': s['foot'], 'blocks': blocks_html(s)} for s in secs]
    import re
    toc = ''.join('<li><b>%02d</b>%s</li>' % (i + 1, s['foot']) for i, s in enumerate(secs))
    cover = ('<section class="page cover"><div class="logo">%s</div><div class="big"><div class="rule"></div>'
             '<div class="intro">%s</div><div class="logo">%s</div>%s</div>'
             '<ul class="toc">%s</ul></section>') % (
        SVG.replace('ID', 'cv'), C.COVER['title'], WT,
        ('<div class="edition">%s</div>' % C.COVER['short']) if edition == 'short' else '', toc)
    head = '<div class="head"><div class="logo">%s%s</div></div>' % (SVG, WT)
    js = """
const DATA=%s, HEAD=%s;
window.paginate=function(){
let n=1, cid=0;
function newPage(sec, first){
  n++; const s=document.createElement('section'); s.className='page'+(first?'':' cont');
  s.innerHTML=HEAD.replace(/ID/g,'h'+(cid++))+'<div class="body">'+(first?'<div class="eyebrow"></div><h1>'+sec.h1+'</h1>':'')+'</div><div class="pagefoot"><span>'+sec.foot+'</span><span>'+n+'</span></div>';
  document.body.appendChild(s); return s.querySelector('.body');
}
const over=b=>b.scrollHeight>b.clientHeight+1;
for(const sec of DATA){
  let body=newPage(sec,true);
  for(const h of sec.blocks){
    const t=document.createElement('div'); t.innerHTML=h; const el=t.firstChild;
    body.appendChild(el);
    if(over(body)){
      body.removeChild(el);
      const moved=[];
      while(body.lastElementChild && body.lastElementChild.dataset.keep){moved.unshift(body.lastElementChild); body.removeChild(body.lastElementChild);}
      body=newPage(sec,false); moved.forEach(m=>body.appendChild(m)); body.appendChild(el);
      if(over(body)) console.log('OVERFLOW', sec.foot);
    }
  }
}
window.PAGES=n;};
""" % (json.dumps(data), json.dumps(head))
    html = ('<!doctype html><html lang="%s"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head>'
            '<body class="%s">%s<script>%s</script></body></html>') % (
        lang, C.COVER['title'] + ' TimeCapsule', css, 'compact', cover, js)
    name = C.UI['file'] + ('-short' if edition == 'short' else '')
    open(name + '.html', 'w').write(html)
    return name

if __name__ == '__main__':
    for lang in ('en', 'es'):
        for ed in ('full', 'short'):
            print(build(lang, ed))
