# Conversations page: topic chips get the full width; the Recent / Most rounds switch moves to the count line,
# on the right ("1,425 conversations · 12 topics ........ Recent | Most rounds"). Safe to run twice.
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = '''    <div class="sort" role="group" aria-label="Sort"><button type="button" data-s="recent" aria-pressed="true">Recent</button><button type="button" data-s="rounds" aria-pressed="false">Most rounds</button></div>
  </div>
  <p class="cnt" id="cnt"></p>'''
B = '''  </div>
  <div class="cntrow"><p class="cnt" id="cnt"></p><div class="sort" role="group" aria-label="Sort"><button type="button" data-s="recent" aria-pressed="true">Recent</button><button type="button" data-s="rounds" aria-pressed="false">Most rounds</button></div></div>'''
CSS = ('<style id="disc-sort">.dp .tools .pills{flex:1 1 100%;flex-wrap:wrap!important;overflow:visible!important;-webkit-mask-image:none!important;mask-image:none!important;margin:0!important;padding:2px!important}'
       '.dp .cntrow{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:18px 0 0}'
       '.dp .cntrow .cnt{margin:0}'
       '.dp .cntrow .sort button{font-size:13px}</style>')
for rel in ('library/disc-body.html', 'help/live-pages/discussions.html'):
    F = os.path.join(R, rel); s = open(F, encoding='utf8').read()
    if 'id="disc-sort"' in s: print(rel, 'already'); continue
    assert s.count(A) == 1, rel
    s = s.replace(A, B)
    i = s.index('<style id="disc-chips">')
    s = s[:i] + CSS + s[i:]
    open(F, 'w', encoding='utf8').write(s); print(rel, 'patched')
