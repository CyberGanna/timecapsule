"""Gabriele 2026-11-22 "big dot again": the Join / Welcome back / Save a chair sheets on the Table page showed a round orb.
Now they use the same card look as the Tables page sheets (#170): the table's picture (or topic colour + icon) across the top,
then topic, title in Literata, "with host · country". Idempotent, marker "tc-sumcard"."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'table-detail/timecapsule-table.html')
OLD = ('function sumHTML(){const t=T();return `<div class="thumb"><div style="width:100%;height:100%;background:radial-gradient(circle at 35% 30%,${TOPIC_C[t.topic]},#20264A)"></div></div>'
       '<div class="si"><b>${t.title}</b><small>${t.topic}</small></div>`}')
NEW = ('function sumHTML(){/*tc-sumcard*/const t=T(),p=PROF[t.host],h=t.host==="You"?"Gabriele":t.host;'
       'return `<div class="sumhd" style="--c:${TOPIC_C[t.topic]||"#A9B0D6"}"><div class="sumimg">${tdHdImg()}</div></div>'
       '<div class="si" style="--c:${TOPIC_C[t.topic]||"#A9B0D6"}"><span class="sumtp"><i></i>${t.topic}</span><b>${t.title}</b>'
       '<small>with <em>${h}</em>${p&&p[0]?` · ${p[0]}`:""}</small></div>`}')
CSS = '''<style id="tc-sumcard">
.sum{display:block!important;padding:0!important;overflow:hidden;background:#20264A!important;position:relative;border:0!important;isolation:isolate}
.sum::after{content:"";position:absolute;inset:0;border:1px solid var(--line);border-radius:inherit;pointer-events:none;z-index:3}
.sum .sumhd{position:relative;height:120px;overflow:hidden;border-radius:15px 15px 0 0;transform:translateZ(0)}
.sum .sumimg{position:absolute;inset:0;background:var(--c)}
.sum .sumimg img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.03);filter:none}
.sum .sumimg .tcplain svg{width:40px;height:40px}
.sum .si{padding:14px 16px 16px;min-width:0}
.sum .sumtp{display:flex;align-items:center;gap:8px;font-size:13px;color:#C9CFF0}
.sum .sumtp i{width:8px;height:8px;border-radius:50%;background:var(--c)}
.sum b{font-family:Literata,Georgia,serif;font-weight:500!important;font-size:19px!important;line-height:1.3!important;margin-top:8px;color:#EEF1FF;display:block}
.sum small{display:block;margin-top:4px!important;color:#A9B0D6!important;font-size:13px!important;letter-spacing:0!important;text-transform:none!important}
.sum small em{font-style:normal;color:#C9CFF0;font-weight:500}
</style>'''
for P in [P, os.path.join(ROOT, 'help/live-pages/table.html'), os.path.join(ROOT, 'invite/pages/table.html')]:
    s = open(P, encoding='utf8').read()
    if 'tc-sumcard' in s or OLD not in s: continue
    s = s.replace(OLD, NEW)
    k = s.rfind('</body>'); s = (s[:k] + CSS + s[k:]) if k >= 0 else (s + CSS)
    open(P, 'w', encoding='utf8').write(s); print(P, 'sum card')
