"""Gabriele 2026-11-23: no topic-coloured card border on phones. The border came from :hover, which sticks after a tap
on touch screens. On touch devices the card border stays neutral. Idempotent, marker "tc-cchover"."""
import sys
CSS='<style id="tc-cchover">@media (hover:none),(max-width:640px){main .live article.tbl.cc:hover{border-color:#323A6C!important}main .live article.tbl.cc:hover::after{border-color:#323A6C!important}}</style>'
for f in sys.argv[1:]:
    s=open(f,encoding='utf8').read()
    if 'tc-cchover' in s: continue
    k=s.rfind('</body>'); s=s[:k]+CSS+s[k:] if k>=0 else s+CSS
    open(f,'w',encoding='utf8').write(s); print(f)
