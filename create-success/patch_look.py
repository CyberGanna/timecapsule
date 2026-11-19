"""'Your table is open!': title under the heading, no extra copy; gold countdown for later tables, green "Live now" for now (Karim 2026-11-18).
Idempotent, marker "tc-cok4". Run after patch_tidy.py."""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = '''<style id="tc-cok4">.cok .cktitle{margin:10px auto 0!important;max-width:440px;font-family:'Newsreader',Georgia,serif;font-size:22px!important;line-height:1.35!important;color:var(--text)!important}
.cok .cklive{display:flex;width:max-content;margin:16px auto 0;align-items:center;gap:8px;height:30px;padding:0 14px;border-radius:999px;background:rgba(61,220,132,.14);color:#3DDC84;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase}
.cok .cklive i{width:8px;height:8px;border-radius:50%;background:#3DDC84;box-shadow:0 0 0 0 rgba(61,220,132,.6);animation:ckp 1.8s infinite}@keyframes ckp{70%{box-shadow:0 0 0 8px rgba(61,220,132,0)}100%{box-shadow:0 0 0 0 rgba(61,220,132,0)}}
.cok .ckcd{display:flex;justify-content:center;align-items:baseline;gap:14px;margin-top:16px}.cok .ckcd .lab{font-size:13px;color:var(--mute)}.cok .ckcd .u b{font-size:30px;font-weight:500;color:#F2C14E;font-variant-numeric:tabular-nums;letter-spacing:-.02em}.cok .ckcd .u small{margin-left:3px;font-size:12px;color:var(--mute)}
.cok .ckwhen{margin:6px 0 0!important;font-size:13px!important;color:var(--mute)!important}</style>'''
STR = {"Starts in": ["Inizia tra", "Empieza en", "Ξεκινά σε"], "Live now": ["Live ora", "Live ahora", "Live τώρα"]}
JS = '''<script id="tc-cok4-js">setInterval(function(){document.querySelectorAll(".ckcd[data-at]").forEach(function(e){var s=Math.max(0,Math.floor((+e.dataset.at-Date.now())/1000)),d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),x=s%60,p=function(n){return String(n).padStart(2,"0")};
var v=d?[d,h,m]:[h,p(m),p(x)],u=e.querySelectorAll(".u");if(d){u[0].lastChild.textContent="d";u[1].lastChild.textContent="h";u[2].lastChild.textContent="min"}u.forEach(function(el,i){el.firstChild.textContent=v[i]})})},1000);</script>'''

def run(rel):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-cok4' in s: return
    a = s[s.index('      <span class="when">${now?"Live now":longWhen(t.when)}'):]
    a = a[:a.index('</p>\n') + 5]
    assert a.count('\n') == 2, a
    b = ('      <p class="cktitle" data-noi18n>${esc(t.title)}</p>\n'
         '      ${now?`<span class="cklive"><i></i><span>Live now</span></span>`:`<div class="ckcd" data-at="${Math.round((Date.now()+t.when*60000)/9e5)*9e5}"><span class="lab">Starts in</span>'
         '<span class="u"><b>0</b><small>h</small></span><span class="u"><b>00</b><small>min</small></span><span class="u"><b>00</b><small>sec</small></span></div>'
         '<p class="ckwhen">${longWhen(t.when)}${t.rep&&t.rep!=="none"?` · ${REP[t.rep].toLowerCase()}`:""}</p>`}\n')
    assert s.count(a) == 1
    s = s.replace(a, b)
    s = s.replace('</title>', '</title>' + CSS, 1)
    s = s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={' + ''.join('%s:%s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in STR.items()), 1)
    i = s.rindex('</body>'); s = s[:i] + JS + s[i:]
    open(p, 'w', encoding='utf8').write(s); print(rel, 'look')
for r in ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']:
    run(r)
