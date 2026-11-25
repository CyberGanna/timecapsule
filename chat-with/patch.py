"""Gabriele 2026-11-23: the chat icon on a person pop-up opens Chats with that person's chat already open
(not the list of all chats). Link: chats.html#with=<name>. Chats page opens the chat (or a new empty one).
Idempotent, markers "tc-chatwith". Re-run after rebuilding pages with the person pop-up or Chats."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ('node_modules', '.git')
# 1) receiver on the Chats page
OLD = '})()||\n(matchMedia("(min-width:821px)").matches&&open("gregory"));'
NEW = ('})()||\n/*tc-chatwith*/(function(){const h=new URLSearchParams((location.hash||"").slice(1));const n=(h.get("with")||"").trim();if(!n)return false;'
       'let c=C.find(x=>x.kind==="person"&&x.name.toLowerCase()===n.toLowerCase());'
       'if(!c){c={id:"new-"+n.toLowerCase().replace(/[^a-z0-9]+/g,"-"),kind:"person",name:n,online:false,seen:"",unread:0,ctx:"Say hello to <b data-noi18n>"+n.replace(/[<>&"]/g,"")+"</b>",m:[]};C.unshift(c)}'
       'try{history.replaceState(history.state,"",location.pathname+location.search)}catch(e){}'
       'open(c.id);return true})()||\n(matchMedia("(min-width:821px)").matches&&open("gregory"));')
# 2) sender: the pop-up chat icon
RX = re.compile(r'href="((?:\$\{URL_CHATS\}|[^"#]*chats\.html))" (target="_top" aria-label="Chat with \$\{u\.name\}")')
for d, _, fs in os.walk(ROOT):
    if any(s in d for s in SKIP): continue
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf8').read(); o = s
        if OLD in s and 'tc-chatwith' not in s: s = s.replace(OLD, NEW)
        s = RX.sub(lambda m: 'href="%s#with=${encodeURIComponent(u.name)}" %s' % (m.group(1), m.group(2)), s)
        if s != o: open(p, 'w', encoding='utf8').write(s); print(os.path.relpath(p, ROOT))
