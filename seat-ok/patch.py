"""'You're in!' after Save chair (Tables page): the old ring-of-chairs picture is replaced by the card look
(Gabriele 2026-11-23): the table's photo header (or the solid topic colour with its icon) across the top of the
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
(function(){const s=document.getElementById("sheet");if(!s)return;new MutationObserver(()=>s.classList.toggle("okv",!!s.querySelector(".okhd"))).observe(s,{childList:true,subtree:true})})();
</script>'''
CSS = '''<style id="tc-seatok-css">
#sheet .ok .okhd{position:relative;height:130px;margin:-26px -26px 18px!important;width:calc(100% + 52px)!important;max-width:none!important;border-radius:21px 21px 0 0;overflow:hidden;background:var(--c)}
#sheet.okv{position:relative}#sheet.okv .ok{margin-top:0!important;padding-top:0!important}#sheet.okv .x{position:absolute!important;float:none;top:14px;right:14px;margin:0;z-index:3;background:rgba(20,25,54,.6);border-color:rgba(255,255,255,.25);color:#EEF1FF}
.ok .okhd img{width:100%;height:100%;object-fit:cover;display:block}
.okfaces{display:flex;justify-content:center;gap:6px;margin:18px auto 0;max-width:360px}
.okfaces>span,.okfaces>em{flex:none;width:34px;height:34px;border-radius:50%;overflow:hidden;display:block;box-sizing:border-box}
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

# Step 2 (Gabriele 2026-11-23): the table summary at the top of "Reserve your seat" and the Join sheet used a
# round gradient orb and an uppercase coloured topic. Now it is the card look: photo header (or solid topic
# colour), topic dot + name, the question in Literata, "with host · country". Marker "tc-seatok2".
SUM_OLD = '''  const thumb= t.img!=null ? `<img src="${IMGS[t.img]}" alt="">` : art(t.theme);
  return `<div class="thumb">${thumb}</div><div class="si"><b>${t.title}</b><small>${t.theme}</small></div>`;'''
SUM_NEW = '''  /* tc-seatok2 */
  return `<div class="sumhd">${okTop(t).replace('class="okhd"','class="okhd sumimg"')}</div><div class="si"><span class="sumtp"><i></i>${t.theme}</span><b>${t.title}</b><small>with <em>${t.host}</em> · ${t.country}</small></div>`;'''
CSS2 = '''<style id="tc-seatok2">
.sum{display:block!important;padding:0!important;overflow:hidden;background:#20264A!important}
.sum .sumhd{position:relative;height:120px;overflow:hidden}
.sum .sumimg{position:absolute;inset:0;background:var(--c)}
.sum .sumimg img{width:100%;height:100%;object-fit:cover;display:block}
.sum .sumimg .tcplain svg{width:40px;height:40px}
.sum .si{padding:14px 16px 16px}
.sum .sumtp{display:flex;align-items:center;gap:8px;font-size:13px;color:#C9CFF0}
.sum .sumtp i{width:8px;height:8px;border-radius:50%;background:var(--c)}
.sum b{font-family:Literata,Georgia,serif;font-weight:500!important;font-size:19px!important;line-height:1.3!important;margin-top:8px;color:#EEF1FF}
.sum small{margin-top:4px!important;color:#A9B0D6!important;font-size:13px!important;letter-spacing:0!important;text-transform:none!important}
.sum small em{font-style:normal;color:#C9CFF0;font-weight:500}
</style>'''
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap">'
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-seatok2' in s:
        continue
    assert s.count(SUM_OLD) == 1, rel
    s = s.replace(SUM_OLD, SUM_NEW)
    i = s.rindex('</body>'); s = s[:i] + CSS2 + s[i:]
    if 'family=Literata' not in s:
        s = s.replace('</title>', '</title>' + FONT, 1)
    open(p, 'w', encoding='utf8').write(s); print(rel, 'summary card')

# Step 3 (Gabriele 2026-11-23): round the header corners on the summary (Safari clipping) and no boxes behind
# the people at the table. Marker "tc-seatok3".
CSS3 = '''<style id="tc-seatok3">
.sum{isolation:isolate}
.sum .sumhd{border-radius:15px 15px 0 0;transform:translateZ(0)}
.sum .sumimg,.sum .sumimg img{border-radius:15px 15px 0 0}
.plist li{background:none!important;padding:4px 0!important}
.sum{position:relative;border:0!important}
.sum::after{content:"";position:absolute;inset:0;border:1px solid var(--line);border-radius:inherit;pointer-events:none;z-index:3}
.sum .sumimg img{transform:scale(1.03)}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-seatok3' in s:
        continue
    i = s.rindex('</body>'); s = s[:i] + CSS3 + s[i:]
    open(p, 'w', encoding='utf8').write(s); print(rel, 'step 3')
