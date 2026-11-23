"""Karim 2026-11-22: after uploading a picture in Create a table, drag it to choose which part shows.
- The thumbnail takes the header's wide shape (160x67) and shows "Drag to move".
- Dragging the thumbnail or the preview header moves the picture (object-position, kept in --tcpos).
- The position travels with the new table: success screen, Tables page cards, and the Table page header.
Idempotent, marker "tc-pos". Run after photo-upload/patch.py."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
T = {"Drag to move": ["Trascina per spostare", "Arrastra para mover", "Σύρε για μετακίνηση"]}
JS = r'''<script id="tc-pos">/* tc-pos: drag the uploaded picture to choose what shows */
(function(){
  let P=[50,50];
  window.tcPos=()=>P[0]+"% "+P[1]+"%";
  window.tcSetPos=s=>{const m=String(s||"50% 50%").match(/([\d.]+)%\s+([\d.]+)%/);P=m?[+m[1],+m[2]]:[50,50];document.documentElement.style.setProperty("--tcpos",tcPos())};
  let d=null;
  document.addEventListener("pointerdown",e=>{
    const im=e.target.closest&&e.target.closest(".cvimg img,.pvc-hd img");if(!im||!im.naturalWidth)return;
    const b=im.getBoundingClientRect(),k=Math.max(b.width/im.naturalWidth,b.height/im.naturalHeight);
    d={x:e.clientX,y:e.clientY,p:P.slice(),ow:im.naturalWidth*k-b.width,oh:im.naturalHeight*k-b.height};
    try{im.setPointerCapture(e.pointerId)}catch(x){}e.preventDefault();document.body.classList.add("tcdrag");
  });
  document.addEventListener("pointermove",e=>{if(!d)return;
    const c=v=>Math.max(0,Math.min(100,v));
    P=[d.ow>1?c(d.p[0]-(e.clientX-d.x)/d.ow*100):50,d.oh>1?c(d.p[1]-(e.clientY-d.y)/d.oh*100):50].map(v=>Math.round(v*10)/10);
    document.documentElement.style.setProperty("--tcpos",tcPos());
  });
  const up=()=>{if(d){d=null;document.body.classList.remove("tcdrag")}};
  document.addEventListener("pointerup",up);document.addEventListener("pointercancel",up);
})();
</script><style id="tc-pos-css">
.cvimg{height:67px!important;aspect-ratio:auto!important;position:relative}
.cvimg img,.pvc-hd img{cursor:grab;touch-action:none;-webkit-user-drag:none;user-select:none}
body.tcdrag,body.tcdrag *{cursor:grabbing!important}
.cvimg img,.pvc-hd img,.ckph img,img[src^="data:image/jpeg"]{object-position:var(--tcpos,50% 50%)}
.cvhint{display:block;font-size:12px;color:var(--mute,#A9B0D6);margin-top:6px;text-align:center}
.cvwrap{flex:none;width:160px}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-pos' in s: continue
    def rep(a, b):
        global s
        assert s.count(a) == 1, (rel, a[:60], s.count(a)); s = s.replace(a, b)
    rep('`<div class="cvimg"><img src="${IMGS[nt.img]}" alt="Cover picture"></div>',
        '`<div class="cvwrap"><div class="cvimg"><img src="${IMGS[nt.img]}" alt="Cover picture" draggable="false"></div><small class="cvhint">Drag to move</small></div>')
    rep('/*tc-shrink*/IMGS.push(u);', '/*tc-shrink*/tcSetPos();IMGS.push(u);')
    rep('sessionStorage.setItem("tc-created",JSON.stringify({nt:snap,img:simg,link}))',
        'sessionStorage.setItem("tc-created",JSON.stringify({nt:snap,img:simg,link,pos:tcPos()}))')
    rep('if(c.img){IMGS.push(c.img);nt.img=IMGS.length-1}', 'if(c.img){IMGS.push(c.img);nt.img=IMGS.length-1;tcSetPos(c.pos)}')
    k = s.rindex('</body>'); s = s[:k] + JS + s[k:]
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, flags=re.S)
    if m:
        dd = json.loads(m.group(1)); dd.update(T)
        s = s[:m.start(1)] + json.dumps(dd, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + s[m.end(1):]
    open(p, 'w', encoding='utf8').write(s); print(rel)
# Table page: header picture uses the saved position
P = os.path.join(ROOT, 'table-detail/timecapsule-table.html'); s = open(P, encoding='utf8').read()
if 'tc-pos' not in s:
    a = 'let im=null;try{im=JSON.parse(sessionStorage.getItem("tc-created")||"{}").img}catch(e){}\n   return im?`<img src="${im}" alt="">`'
    assert s.count(a) == 1
    s = s.replace(a, 'let im=null,ps="50% 50%";try{const c=JSON.parse(sessionStorage.getItem("tc-created")||"{}");im=c.img;ps=c.pos||ps}catch(e){}/*tc-pos*/\n   return im?`<img src="${im}" alt="" style="object-position:${ps}">`')
    open(P, 'w', encoding='utf8').write(s); print('table page')
for f, line in (('help/dict-help.txt', 'Drag to move|Trascina per spostare|Arrastra para mover'), ('i18n/dict-el.txt', 'Drag to move|Σύρε για μετακίνηση')):
    q = os.path.join(ROOT, f); e = open(q, encoding='utf8').read()
    if '\nDrag to move|' not in '\n' + e: open(q, 'w', encoding='utf8').write(e.rstrip('\n') + '\n' + line + '\n')
