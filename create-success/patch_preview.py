"""Create a table: the Preview card is the new Tables page card (Karim 2026-11-23).
Photo header (the picture the host adds, else the same backdrop the success screen uses), hour bar when
"now", topic dot + LIVE / Starts in, the question in Literata, "with Gabriele · Switzerland",
a full row of chairs (you + dashed free chairs), "N chairs free", "You're hosting".
Idempotent, marker "tc-pvc". Run after patch_cards.py (needs window.CKBD)."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']

OLD = '<div class="pcard"><span class="pbadge">Preview</span>${card(Object.assign(t,{people:["You"]}))}</div>'
NEW = '<div class="pcard"><span class="pbadge">Preview</span>${pvCard(t)}</div>'

JS = r'''<script id="tc-pvc">
function pvCard(t){
  const c=THEMES[t.theme],now=nt.whenK==="now",n=Math.max(2,+(t.seats||nt.seats||8)),f=n-1;
  const id=Math.max(...T.map(x=>+x.id||0))+1,P=window.CKBD||IMGS;
  const img=nt.img!=null?IMGS[nt.img]:P[id%P.length];
  const q=(nt.title||"").trim()||"What you want to discuss";
  const e=s=>String(s).replace(/[&<>"]/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[ch]));
  let when;
  if(now) when=`<span class="cc-live">LIVE</span>`;
  else{const m=Math.max(1,Math.round(t.when||0));when=`<span class="cc-when">${m<=60?`Starts in ${m} min`:longWhen(t.when)}</span>`}
  return `<article class="pvc" style="--c:${c}"><div class="pvc-hd"><img src="${img}" alt="">${now?`<div class="pvc-hour"><i></i></div>`:""}</div>
   <div class="pvc-in"><div class="cc-top"><span class="cc-topic"><i></i>${t.theme}</span>${when}</div>
   <h3 data-noi18n>${e(q)}</h3><div class="cc-host">with <b>Gabriele</b> · Switzerland</div>
   <div class="pvc-foot"><span class="pvc-faces"><span>${av("You")}</span>${"<em></em>".repeat(f)}</span><span class="pvc-seats">${f} ${f===1?"chair":"chairs"} free</span>
   <span class="pvc-btn">You're hosting</span></div></div></article>`;
}
</script>'''

CSS = '''<style id="tc-pvc-css">
.pcard .pvc{position:relative;display:flex;flex-direction:column;border-radius:20px;overflow:hidden;background:radial-gradient(120% 70% at 0% 0%,color-mix(in srgb,var(--c) 9%,transparent),transparent 60%),#20264A;box-shadow:0 1px 0 rgba(255,255,255,.04) inset,0 12px 30px rgba(5,8,25,.25)}
.pcard .pvc::after{content:"";position:absolute;inset:0;border:1px solid #323A6C;border-radius:inherit;pointer-events:none;z-index:4}
.pvc-hd{position:relative;height:160px;overflow:hidden;background:#252B52}.pvc-hd img{width:100%;height:100%;object-fit:cover;display:block}
.pvc-hd::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,25,54,0) 55%,rgba(32,38,74,.55))}
.pvc-hour{position:absolute;left:0;right:0;bottom:0;height:3px;background:rgba(238,241,255,.10);z-index:2}.pvc-hour i{display:block;width:2%;height:100%;background:#3DDC84}
.pvc-in{padding:20px 22px 20px}
.pvc .cc-top{display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:13px;color:#C9CFF0}
.pvc .cc-topic{display:flex;align-items:center;gap:8px}.pvc .cc-topic i{width:8px;height:8px;border-radius:50%;background:var(--c)}
.pvc .cc-live{font-size:13px;font-weight:600;letter-spacing:.14em;color:#3DDC84}
.pvc .cc-when{font-size:12.5px;color:#A9B0D6}
.pvc h3{font-family:Literata,Georgia,serif;font-weight:500;font-size:22px;line-height:1.28;padding-bottom:.1em;margin:14px 0 4px;color:#EEF1FF;overflow-wrap:anywhere}
.pvc .cc-host{font-size:13.5px;color:#A9B0D6}.pvc .cc-host b{color:#C9CFF0;font-weight:500}
.pvc-foot{margin-top:20px;display:flex;flex-direction:column;gap:10px}
.pvc-faces{display:flex;justify-content:space-between;gap:5px;width:100%}
.pvc-faces>span,.pvc-faces>em{flex:0 1 40px;min-width:0;aspect-ratio:1;border-radius:50%;overflow:hidden;display:block;box-sizing:border-box}
.pvc-faces svg,.pvc-faces img{width:100%;height:100%;display:block}
.pvc-faces>em{border:1.5px dashed rgba(238,241,255,.28)}
.pvc-seats{font-size:13px;color:#A9B0D6;text-align:center}
.pvc-btn{display:flex;align-items:center;justify-content:center;height:42px;margin-top:4px;border-radius:10px;font-size:14.5px;font-weight:600;color:#C9CFF0;background:rgba(238,241,255,.06);box-shadow:inset 0 0 0 1px #323A6C}
</style>'''
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap">'

for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-pvc' in s:
        continue
    assert s.count(OLD) == 1, rel
    s = s.replace(OLD, NEW)
    i = s.rindex('</body>'); s = s[:i] + CSS + s[i:]
    k = s.rfind('<script', 0, s.index('function ntPreview('))
    import re as _re
    m = _re.search(r'<script id="tc-cok5-bd">.*?</script>', s, flags=_re.S)
    bd = m.group(0); s = s[:m.start()] + s[m.end():]
    k = s.rfind('<script', 0, s.index('function ntPreview('))
    s = s[:k] + bd + JS + s[k:]  # backdrops + pvCard must exist before ntPreview first runs
    if 'family=Literata' not in s:
        s = s.replace('</title>', '</title>' + FONT, 1)
    open(p, 'w', encoding='utf8').write(s); print(rel, 'preview')
