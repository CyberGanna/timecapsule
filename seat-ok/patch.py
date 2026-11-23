"""'You're in!' after Save chair (Tables page): the old ring-of-chairs picture is replaced by the card look
(Karim 2026-11-23): the table's photo header (or the solid topic colour with its icon) across the top of the
sheet, then a row of all the chairs (faces, you, dashed free chairs) under the date.
Idempotent, marker "tc-seatok". Run after card-v2/patch.py and create-success/patch_plain.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']

OLD_A = 'const ringHtml=ring(t,true);'
NEW_A = 'const ringHtml=okTop(t);'
OLD_B = '<div class="done-ring">${ringHtml}</div>'
NEW_B = '${ringHtml}'
OLD_C = '<span class="when">${longWhen(t.when)}</span>'
NEW_C = '<span class="when">${longWhen(t.when)}</span>${okFaces(t)}'

JS = r'''<script id="tc-seatok">
function okTop(t){
  const P=typeof CCPOOL!=="undefined"?CCPOOL:null, k=(typeof CCIMG!=="undefined"&&CCIMG[t.id]!=null)?CCIMG[t.id]:t.id;
  const src=t.img!=null?IMGS[t.img]:P?P[k%P.length]:null;
  return `<div class="okhd" style="--c:${THEMES[t.theme]}">${src?`<img src="${src}" alt="">`:`<div class="tcplain"><svg viewBox="0 0 24 24" aria-hidden="true">${TICON[t.theme]||""}</svg></div>`}</div>`;
}
function okFaces(t){
  const ppl=[...t.people]; if(!ppl.includes("You")) ppl.push("You"); const left=Math.max(0,t.seats-ppl.length);
  return `<div class="okfaces">${ppl.map(p=>`<span${p==="You"?' class="me"':''}>${av(p)}</span>`).join("")}${"<em></em>".repeat(left)}</div><div class="okseats">${left>0?`${left} ${left===1?"chair":"chairs"} free`:"Table full"}</div>`;
}
</script>'''
CSS = '''<style id="tc-seatok-css">
#sheet .ok .okhd{position:relative;height:130px;margin:-26px -26px 18px!important;width:calc(100% + 52px)!important;max-width:none!important;border-radius:21px 21px 0 0;overflow:hidden;background:var(--c)}
#sheet:has(.okhd){position:relative}#sheet:has(.okhd) .ok{margin-top:0!important;padding-top:0!important}#sheet:has(.okhd) .x{position:absolute!important;float:none;top:14px;right:14px;margin:0;z-index:3;background:rgba(20,25,54,.6);border-color:rgba(255,255,255,.25);color:#EEF1FF}
.ok .okhd img{width:100%;height:100%;object-fit:cover;display:block}
.okfaces{display:flex;justify-content:center;gap:6px;margin:18px auto 0;max-width:360px}
.okfaces>span,.okfaces>em{flex:0 1 34px;min-width:0;aspect-ratio:1;border-radius:50%;overflow:hidden;display:block;box-sizing:border-box}
.okfaces svg,.okfaces img{width:100%;height:100%;display:block}
.okfaces>em{border:1.5px dashed rgba(238,241,255,.28)}
.okseats{margin-top:6px;font-size:12.5px;color:#A9B0D6}
@media (max-width:640px){#sheet .ok .okhd{margin:-22px -18px 16px!important;width:calc(100% + 36px)!important}}
</style>'''

for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-seatok' in s:
        continue
    for a, b in [(OLD_A, NEW_A), (OLD_B, NEW_B), (OLD_C, NEW_C)]:
        assert s.count(a) == 1, (rel, a)
        s = s.replace(a, b)
    i = s.rindex('</body>'); s = s[:i] + JS + CSS + s[i:]
    open(p, 'w', encoding='utf8').write(s); print(rel, 'seat ok')
