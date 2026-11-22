# Conversations page: drop the constellation map (the universe now means books and films on the profile).
# Topics become one wrapping row of chips with counts that filter the list in place.
# Patches library/disc-body.html and help/live-pages/discussions.html. Safe to run twice.
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('<style id="disc-chips">.dp .sky{display:none!important}'
       '.dp .hero{padding-bottom:4px}'
       '.dp .tools{align-items:flex-start}'
       '.dp .pills{flex-wrap:wrap;overflow:visible;-webkit-mask-image:none;mask-image:none;row-gap:8px}'
       '.dp .pills button .n{font-weight:400;color:var(--mute);opacity:.8;font-size:12.5px}'
       '.dp .pills button[aria-pressed=true] .n{color:var(--soft);opacity:1}'
       '@media (max-width:640px){.dp .pills{margin:0;padding:2px 0}.dp .pills button{height:32px;padding:0 11px;font-size:13px}}'
       '</style>')
REP = [
 ("TOP.map(t=>'<button type=\"button\" data-t=\"'+esc(t.n)+'\" style=\"--c:'+t.c+'\" aria-pressed=\"false\"><i></i><span>'+esc(t.n)+'</span></button>')",
  "TOP.map(t=>'<button type=\"button\" data-t=\"'+esc(t.n)+'\" style=\"--c:'+t.c+'\" aria-pressed=\"false\"><i></i><span>'+esc(t.n)+'</span> <b class=\"n\">'+t.d.length+'</b></button>')"),
 ("'\" aria-pressed=\"'+(!S.s)+'\"><i></i><span>All in</span> <span>'+esc(S.t)+'</span></button>'",
  "'\" aria-pressed=\"'+(!S.s)+'\"><i></i><span>All in</span> <span>'+esc(S.t)+'</span> <b class=\"n\">'+T.d.length+'</b></button>'"),
 ("'\" aria-pressed=\"'+(S.s===x.n)+'\"><i></i><span>'+esc(x.n)+'</span></button>'",
  "'\" aria-pressed=\"'+(S.s===x.n)+'\"><i></i><span>'+esc(x.n)+'</span> <b class=\"n\">'+x.d.length+'</b></button>'"),
]
for rel in ('library/disc-body.html', 'help/live-pages/discussions.html'):
    F = os.path.join(R, rel); s = open(F, encoding='utf8').read()
    if 'id="disc-chips"' in s:
        print(rel, 'already'); continue
    for a, b in REP:
        assert s.count(a) == 1, (rel, a[:60])
        s = s.replace(a, b)
    i = s.index('</head>') if '</head>' in s else 0
    s = s[:i] + CSS + s[i:]
    open(F, 'w', encoding='utf8').write(s); print(rel, 'patched')
