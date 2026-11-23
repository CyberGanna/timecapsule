"""Karim 2026-11-23: People page gets a "Crossing universes" filter: people who share books and films
from your universe, most in common first, each card showing what you share.
Sample data: Gabriele's universe (MINE) and the books/films each person shares (WL).
Idempotent, marker "tc-wavelength". Re-run after rebuilding the People page."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/people.html', 'invite/pages/people.html']
REP = [
 ('const F=[["all","Everyone"],',
  '/*tc-wavelength*/const WL={Priya:[["b","The Myth of Sisyphus"],["b","Siddhartha"],["f","Before Sunrise"],["f","Perfect Days"]],'
  'Gregory:[["b","Meditations"],["b","Being and Time"],["f","The Seventh Seal"]],'
  'Yuki:[["f","Perfect Days"],["b","Siddhartha"]],Amara:[["b","The Human Condition"],["f","Arrival"]],'
  'Mia:[["b","Meditations"],["f","Perfect Days"]],Omar:[["b","Thinking, Fast and Slow"]],Elif:[["f","The Seventh Seal"]],Noah:[["b","The Human Condition"]]};\n'
  'const wl=u=>WL[u.n]||[];\n'
  'function wlHTML(u){const L=wl(u),b=L.filter(x=>x[0]==="b").length,f=L.length-b,parts=[];'
  'if(b)parts.push(`<b>${b}</b> <span>${b===1?"book":"books"}</span>`);if(f)parts.push(`<b>${f}</b> <span>${f===1?"film":"films"}</span>`);'
  'return `<div class="wl"><div class="wlh"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12c2.5-5 5-5 7.5 0s5 5 7.5 0 3.8-3.4 5-1.5"/></svg>${parts.join(" · ")} <span>in common</span></div>'
  '<ul>${L.map(([k,t])=>`<li class="${k}" data-noi18n>${esc(t)}</li>`).join("")}</ul></div>`}\n'
  'const F=[["all","Everyone"],["wave","Crossing universes"],'),
 ('    if(S.f==="trusted"&&!u.t)return false;',
  '    if(S.f==="wave"&&!wl(u).length)return false;\n    if(S.f==="trusted"&&!u.t)return false;'),
 ('  return L.sort((a,b)=>k(a)-k(b)||b.co-a.co);',
  '  if(S.f==="wave")return L.sort((a,b)=>wl(b).length-wl(a).length||k(a)-k(b));\n  return L.sort((a,b)=>k(a)-k(b)||b.co-a.co);'),
 ('    <div class="tags">${u.tags.map(t=>`<span class="tag"><i style="--c:${C[t]}"></i>${t}</span>`).join("")}</div>',
  '    <div class="tags">${u.tags.map(t=>`<span class="tag"><i style="--c:${C[t]}"></i>${t}</span>`).join("")}</div>\n    ${S.f==="wave"?wlHTML(u):""}'),
]
DICT = {"Crossing universes": ["Universi che si incrociano", "Universos que se cruzan", "Σύμπαντα που συναντιούνται"],
        "in common": ["in comune", "en común", "κοινά"],
        "book": ["libro", "libro", "βιβλίο"], "books": ["libri", "libros", "βιβλία"],
        "film": ["film", "película", "ταινία"], "films": ["film", "películas", "ταινίες"]}
CSS = '''<style id="tc-wavelength">
.pc .wl{margin:12px 0 2px;padding:10px 12px;border-radius:12px;background:rgba(124,92,255,.08);border:1px solid rgba(124,92,255,.28)}
.pc .wlh{display:block;font-size:12.5px;line-height:1.5;color:#C9CFF0}
.pc .wlh b{color:#EEF1FF;font-weight:600}
.pc .wlh svg{width:16px;height:16px;vertical-align:-3px;fill:none;stroke:#B9A8FF;stroke-width:1.8;stroke-linecap:round;margin-right:6px}
.pc .wl ul{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.pc .wl li{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 9px;border-radius:12px;background:var(--raise);font-size:12px;color:var(--fg);font-style:italic}
.pc .wl li::before{content:"";width:6px;height:6px;border-radius:50%;flex:none;background:#F2C14E}
.pc .wl li.f::before{background:#17C3C8}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-wavelength' in s: continue
    for a, b in REP:
        assert s.count(a) == 1, (rel, a[:40]); s = s.replace(a, b)
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});', s, flags=re.S)
    if m:
        d = json.loads(m.group(1)); d.update({k: v for k, v in DICT.items() if k not in d})
        s = s[:m.start(1)] + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + s[m.end(1):]
    k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
    open(p, 'w', encoding='utf8').write(s); print(rel, 'dict' if m else 'NO DICT')
for path, fmt in (('help/dict-help.txt', lambda k, v: f'{k}|{v[0]}|{v[1]}'), ('i18n/dict-el.txt', lambda k, v: f'{k}|{v[2]}')):
    p = os.path.join(ROOT, path); s = open(p, encoding='utf8').read()
    add = [fmt(k, v) for k, v in DICT.items() if not re.search(r'^' + re.escape(k) + r'\|', s, flags=re.M)]
    if add: open(p, 'a', encoding='utf8').write(('' if s.endswith('\n') else '\n') + '\n'.join(add) + '\n')
