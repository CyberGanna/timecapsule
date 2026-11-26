"""Apply the Invite picker (Gabriele 2026-11-18). Idempotent, marker "tc-ipk".
Run from the repo root: python3 invite-picker/patch.py  (after the table-detail patch chain)."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from picker import snippet, add_strings

def rep(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:90]); return s.replace(a, b)

def table():
    p = os.path.join(ROOT, 'table-detail/timecapsule-table.html'); s = open(p, encoding='utf8').read()
    if 'id="tc-ipk"' in s: return
    s = add_strings(s); s = s.replace('</title>', '</title>' + snippet(), 1)
    s = rep(s, '<h2 id="sh-t">Share this table</h2><p class="sub">${t.title}</p></div>',
            '<h2 id="sh-t">Invite people</h2><p class="sub">${t.title}</p></div>\n    <div id="ipkw"></div><p class="iporl">Or send the link</p>')
    s = rep(s, '<p class="fine">Anyone with the link can see this table. They need a TimeCapsule account to take a chair.</p>`,"#scopy");',
            '<p class="fine">Anyone with the link can see this table. They need a TimeCapsule account to take a chair.</p>`,"#ipkq");\n  window.tcIPK&&tcIPK(document.getElementById("ipkw"));document.getElementById("ipkq").focus();')
    s = rep(s, '<button class="btn" data-act="share">${I.share}<span>Share</span></button>', '<button class="btn" data-act="share">${I.share}<span>Invite</span></button>')
    open(p, 'w', encoding='utf8').write(s); print('table page: invite picker')

def create(rel):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'id="tc-ipk"' in s: return
    s = add_strings(s); s = s.replace('</title>', '</title>' + snippet(), 1)
    s = s.replace(" is on the home page. You host", " is on the Tables page. You host")
    s = rep(s, 'Share</button></div>\n      <div class="nsopts" id="ntsopts" hidden>',
            'Invite</button></div>\n      <div id="ntsopts" hidden style="max-width:400px;margin:16px auto 0"><div id="ntipk"></div><p class="iporl">Or send the link</p><div class="nsopts" style="justify-content:flex-start;margin:0">')
    s = rep(s, 'data-t="${t.title.replace(/"/g,"&quot;")}">More</button></div>', 'data-t="${t.title.replace(/"/g,"&quot;")}">More</button></div></div>')
    s = rep(s, 'if(b.id==="ntshare"){const o=sh.querySelector("#ntsopts");o.hidden=!o.hidden;',
            'if(b.id==="ntshare"){const o=sh.querySelector("#ntsopts");o.hidden=!o.hidden;if(!o.hidden&&window.tcIPK&&!o.dataset.ok){o.dataset.ok=1;tcIPK(sh.querySelector("#ntipk"))}if(!o.hidden)sh.querySelector("#ipkq").focus();')
    open(p, 'w', encoding='utf8').write(s); print(rel, ': invite picker')

table()
for r in ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']:
    create(r)
