# Conversations page, inside a topic (Gabriele 2026-11-23, option A):
# the chosen topic is a small heading (dot + name + count) under "‹ All topics",
# and its subtopics are underlined text tabs ("All" first), not pills, so they
# no longer look like topics. On phones the tabs are one line that scrolls; the
# selected tab is scrolled into view. Run after patch_disc_chips.py. Safe to run twice.
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBS = ("subsOf(S.t).map(x=>'<button type=\"button\" data-s=\"'+esc(x.n)+'\" aria-pressed=\"'+(S.s===x.n)+'\"><span>'+esc(x.n)+'</span> <b class=\"n\">'+x.d.length+'</b></button>').join(\"\")")
NEW = (" return '<button type=\"button\" class=\"back\" data-back=\"1\"><span aria-hidden=\"true\">‹</span> <span>All topics</span></button>"
       "<div class=\"tph\" style=\"--c:'+T.c+'\"><i></i><span>'+esc(S.t)+'</span> <b class=\"n\">'+T.d.length+'</b></div>"
       "<div class=\"stabs\"><button type=\"button\" data-s=\"\" aria-pressed=\"'+(!S.s)+'\"><span>All</span></button>'+" + SUBS + "+'</div>';")
SCROLL = ('$("pills").innerHTML=pillsHtml();',
          '$("pills").innerHTML=pillsHtml();{const w=document.querySelector(".stabs"),z=w&&w.querySelector("[aria-pressed=true]");if(z)w.scrollLeft=z.offsetLeft-w.offsetLeft-(w.clientWidth-z.offsetWidth)/2}')
CSS = ('<style id="disc-subtabs">'
 '.dp .tools .pills.in{display:block!important}'
 '.dp .pills .back{all:unset;cursor:pointer;display:inline-flex;align-items:center;gap:6px;font-size:13px;color:var(--mute)}'
 '.dp .pills .back:hover{color:var(--fg)}'
 '.dp .pills .back:focus-visible{outline:2px solid var(--teal);outline-offset:2px}'
 '.dp .pills .tph{display:flex;align-items:center;gap:9px;margin:10px 0 4px;font-size:20px;font-weight:600;color:var(--fg);letter-spacing:-.01em}'
 '.dp .pills .tph i{width:10px;height:10px;border-radius:50%;background:var(--c);flex:none}'
 '.dp .pills .tph .n{font-weight:400;font-size:15px;color:var(--mute);opacity:1}'
 '.dp .pills .stabs{display:flex;gap:22px;overflow-x:auto;overflow-y:hidden;overscroll-behavior-x:contain;scrollbar-width:none;border-bottom:1px solid var(--line);margin-top:6px;padding-right:28px;-webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 28px),transparent);mask-image:linear-gradient(90deg,#000 calc(100% - 28px),transparent)}'
 '.dp .pills .stabs::-webkit-scrollbar{display:none}'
 '.dp .pills .stabs button{all:unset;cursor:pointer;flex:none;display:inline-flex;align-items:center;gap:6px;padding:10px 0 10px;border-bottom:2px solid transparent;font-size:14px;color:var(--mute)}'
 '.dp .pills .stabs button:hover{color:var(--fg)}'
 '.dp .pills .stabs button[aria-pressed=true]{color:var(--fg);border-bottom-color:var(--fg)}'
 '.dp .pills .stabs button .n{font-size:12px}'
 '.dp .pills .stabs button:focus-visible{outline:2px solid var(--teal);outline-offset:2px}'
 '</style>')
for rel in ('library/disc-body.html', 'help/live-pages/discussions.html'):
    F = os.path.join(R, rel); s = open(F, encoding='utf8').read()
    if 'id="disc-subtabs"' in s:
        print(rel, 'already'); continue
    i = s.index("function pillsHtml(){")
    a = s.index(" return '<button type=\"button\" class=\"back\"", i); b = s.index('\n', a)
    s = s[:a] + NEW + s[b:]
    assert s.count(SCROLL[0]) == 1, rel
    s = s.replace(SCROLL[0], SCROLL[0] + '$("pills").classList.toggle("in",!!S.t);' + SCROLL[1][len(SCROLL[0]):])
    j = s.index('<div class="wrap dp">')
    s = s[:j] + CSS + s[j:]
    open(F, 'w', encoding='utf8').write(s); print(rel, 'patched')
