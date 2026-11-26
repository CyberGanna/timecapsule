"""Gabriele 2026-11-23, Tables page join sheet ("Ready to join?" / "Welcome back") and Save a chair sheet:
- live badge = the card's LIVE line (green LIVE + "41 of 60 min"), no green box
- table summary = the list view row: 64px tile (photo or topic icon on topic glow), title, topic dot · with host
- drop the "Listen first and speak in turns..." note
Idempotent, marker "tc-joinsheet". Re-run after seat-ok/patch.py when agenda/create are rebuilt."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
BADGE_OLD = '<span class="badge live" style="margin-bottom:12px"><span class="blink"></span>Live · ${-t.when} min</span>'
BADGE_NEW = '<span class="cc-live shlive">LIVE<span>${t.live!=null?t.live:-t.when} of 60 min</span></span>'
NOTE = '\n    <p class="anote" style="margin-top:16px">Listen first and speak in turns. The host can mute anyone to keep the table calm.</p>'
SUM_NEW = ('function sumHTML(t){/*tc-joinsheet*/const c=THEMES[t.theme]||"#A9B0D6";'
           'return `<div class="sth" style="background:radial-gradient(circle at 35% 30%,${c},${c}66 75%,#252B52)">${t.img!=null?`<img src="${IMGS[t.img]}" alt="">`:`<svg viewBox="0 0 24 24" aria-hidden="true">${TICON[t.theme]||""}</svg>`}</div>'
           '<div class="si"><b>${t.title}</b><span class="sumtp"><i></i>${t.theme}<span class="sumw"> · with <em>${t.host}</em></span></span></div>`;}')
CSS = '''<style id="tc-joinsheet">
#sheet .shlive{display:inline-block;margin:0 0 12px;font-size:13px}
#sheet .sum{display:flex!important;align-items:center;gap:16px;padding:14px!important;overflow:visible;background:var(--field,#20264A)!important;border:1px solid var(--line)!important;border-radius:16px}
#sheet .sum::after{display:none}
#sheet .sum .sth{flex:none;width:64px;height:64px;border-radius:16px;overflow:hidden;display:grid;place-items:center}
#sheet .sum .sth img{width:100%;height:100%;object-fit:cover;display:block}
#sheet .sum .sth svg{width:46%;height:46%;fill:none;stroke:#fff;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;opacity:.9;filter:drop-shadow(0 1px 4px rgba(0,0,0,.3))}
#sheet .sum .si{padding:0!important;min-width:0}
#sheet .sum b{display:block;font-family:inherit!important;font-weight:600!important;font-size:17px!important;line-height:1.3!important;margin:0 0 6px!important;color:#EEF1FF}
#sheet .sum .sumtp{display:flex;align-items:center;gap:8px;font-size:13.5px;color:#C9CFF0;flex-wrap:wrap}
#sheet .sum .sumtp i{width:8px;height:8px;border-radius:50%;background:var(--c)}
#sheet .sum .sumw{color:var(--mute,#A9B0D6);margin-left:-4px}
#sheet .sum .sumw em{font-style:normal;color:#EEF1FF;font-weight:600}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-joinsheet' in s: continue
    m = re.search(r'function sumHTML\(t\)\{.*?\n\}', s, flags=re.S)
    assert m and BADGE_OLD in s and NOTE in s, rel
    s = s[:m.start()] + SUM_NEW + s[m.end():]
    s = s.replace(BADGE_OLD, BADGE_NEW).replace(NOTE, '')
    k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel)
