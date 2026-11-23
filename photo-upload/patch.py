"""Karim 2026-11-22: a photo uploaded in Create a table didn't show on the new table's page.
Cause: the full-size photo (data URL) was too big for sessionStorage, so the hand-off fell back to no picture.
Fix: shrink the photo to at most 1600px on its long side as JPEG (about 200-400 KB) when it is picked.
Idempotent, marker "tc-shrink"."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
OLD = 'r.onload=()=>{IMGS.push(r.result);'
NEW = ('r.onload=()=>tcShrink(r.result,u=>{/*tc-shrink*/IMGS.push(u);')
FN = ('<script>function tcShrink(src,cb){const i=new Image();i.onload=()=>{try{const m=1600,k=Math.min(1,m/Math.max(i.width,i.height)),'
      'c=document.createElement("canvas");c.width=Math.round(i.width*k);c.height=Math.round(i.height*k);'
      'c.getContext("2d").drawImage(i,0,0,c.width,c.height);cb(c.toDataURL("image/jpeg",.82))}catch(e){cb(src)}};i.onerror=()=>cb(src);i.src=src}</script>')
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-shrink' in s: continue
    i = s.index(OLD); j = s.index('};', i)  # end of the onload body
    assert s[j:j+2] == '};'
    s = s[:i] + NEW + s[i+len(OLD):j] + '});' + s[j+2:]
    k = s.rindex('</body>'); s = s[:k] + FN + s[k:]
    open(p, 'w', encoding='utf8').write(s); print(rel)
