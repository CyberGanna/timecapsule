"""Phone Tables page: the card border overlay (.cc::after, z-index 4) picked up the old
'Smaller cards' 60% navy wash, dimming every card. Keep the overlay a border only.
Idempotent: re-run after card-polish/patch.py and card-v2/patch.py."""
import sys
CSS='<style id="tc-cardfade">main .live article.tbl.cc::after,main.land .live article.tbl.cc::after{background:none!important}</style>'
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    if 'tc-cardfade' in s: continue
    i=s.rfind('</body>')
    s=s[:i]+CSS+s[i:] if i>=0 else s+CSS
    open(f,'w',encoding='utf-8').write(s); print('patched',f)
