"""Table page states Full and Cancelled (prototype bar): the seat ring graphic is replaced by the
table's photo in the card style, with the row of faces (Full) or a dimmed photo (Cancelled),
and the question in Literata (Karim 2026-11-23). Idempotent, marker "tce-v2". Run after patch_cardlook.py."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["table-detail/timecapsule-table.html"]  # only this copy has the edge states

NEW_STAGE = r'''function stage(people,off,cap){ /* tce-v2 */
 const img=typeof TD_IMG!=="undefined"?TD_IMG.open:"";
 const faces=off?"":`<span class="e-faces">${Array.from({length:8},(_,i)=>people[i]?`<span>${av(people[i])}</span>`:`<em></em>`).join("")}</span>`;
 return `<div class="e-stage2${off?' e-off':''}"><img src="${img}" alt=""><div class="e-st-in">${faces}<div class="e-cap">${cap}</div></div></div>`}
'''
CSS = '''<style id="tce-v2">
.e-stage2{position:relative;overflow:hidden;border-radius:22px;aspect-ratio:1/1;background:#252B52;isolation:isolate}
.e-stage2::after{content:"";position:absolute;inset:0;border:1px solid #323A6C;border-radius:inherit;pointer-events:none;z-index:3}
.e-stage2 img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2}
.e-stage2::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(20,25,54,0) 35%,rgba(20,25,54,.88))}
.e-stage2.e-off img{filter:grayscale(1) brightness(.6)}
.e-st-in{position:absolute;left:0;right:0;bottom:0;padding:22px 24px 22px;display:flex;flex-direction:column;gap:12px}
.e-faces{display:flex;justify-content:space-between;gap:6px}
.e-faces>span,.e-faces>em{flex:0 1 40px;min-width:0;aspect-ratio:1;border-radius:50%;overflow:hidden;display:block;box-sizing:border-box}
.e-faces svg{width:100%;height:100%;display:block}
.e-faces>em{border:1.5px dashed rgba(238,241,255,.35)}
.e-stage2 .e-cap{font-size:13.5px;color:#C9CFF0;text-align:center}
.e-stage2 .e-cap b{color:#EEF1FF;font-weight:500}
.e-stage2.e-off .e-cap{font-size:15px;color:#EEF1FF}
.e-td h1{font-family:Literata,Georgia,serif!important;font-weight:500!important;letter-spacing:-.01em!important;line-height:1.22!important;padding-bottom:.08em}
@media (max-width:960px){.e-stage2{aspect-ratio:16/10}}
</style>'''

for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding="utf-8").read()
    if "tce-v2" not in s:
        m = re.search(r'function stage\(people,off,cap\)\{.*?\n(?=const host=)', s, flags=re.S)
        assert m, "stage() not found"
        s = s[:m.start()] + NEW_STAGE + s[m.end():]
        i = s.rindex("</body>"); s = s[:i] + CSS + s[i:]
        open(p, "w", encoding="utf-8").write(s)
    print("ok", rel)
