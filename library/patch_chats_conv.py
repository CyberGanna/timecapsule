"""Chats: #compose&kind=conv&q=&th=&host=&rounds=&r= opens New message with a conversation card
(Share this conversation → Send in a chat, Karim 2026-11-19). Run after invite-picker/patch_chats.py. Idempotent."""
import re,json,sys
FILES=sys.argv[1:] or ["help/live-pages/chats.html","invite/pages/chats.html"]
CONV='''function convCard(t){return `<div class="inv ccv" style="--c:${THEMES[t.theme]}"><div class="top2"><div class="ico">${icon(t.theme)}</div></div><div class="b"><div class="k"><span>Conversation</span> · ${t.rounds} <span>${t.rounds===1?"round":"rounds"}</span></div><h3>${esc(t.title)}</h3><div class="m">${t.theme} · <span>hosted by</span> ${esc(t.host)}</div><a class="go" href="../../library/timecapsule-library.html#r=${encodeURIComponent(t.r)}&as=visitor" target="_top" style="display:flex;align-items:center;justify-content:center;text-decoration:none">Read the conversation</a></div></div>`}
function invCard(id,mine){
  const t=MYTABLES.find(x=>x.id===id); if(t&&t.conv) return convCard(t);'''
T={"Conversation":["Conversazione","Conversación","Συζήτηση"],"round":["giro","ronda","γύρος"],"rounds":["giri","rondas","γύροι"],"hosted by":["con host","con anfitrión","με οικοδεσπότη"],"Read the conversation":["Leggi la conversazione","Leer la conversación","Διάβασε τη συζήτηση"],"Send to":["Invia a","Enviar a","Στείλε σε"],"Shared a conversation":["Ha condiviso una conversazione","Compartió una conversación","Κοινοποίησε μια συζήτηση"]}
for f in FILES:
    s=open(f).read(); o=s
    if 'function convCard' not in s:
        a='function invCard(id,mine){\n  const t=MYTABLES.find(x=>x.id===id);'
        assert a in s,f; s=s.replace(a,CONV,1)
        a='if(!THEMES[TT.theme])TT.theme="Philosophy"; MYTABLES.push(TT);'
        assert a in s,f
        s=s.replace(a,'if(h.get("kind")==="conv"){TT.conv=1;TT.host=h.get("host")||"";TT.rounds=+h.get("rounds")||1;TT.r=h.get("r")||""}\n  '+a,1)
        a='<span class="pvl">Invite card</span>'; assert a in s,f
        s=s.replace(a,'<span class="pvl">\'+(TT.conv?"Conversation":"Invite card")+\'</span>',1)
        a='<span>Send invite to</span>'; assert a in s,f
        s=s.replace(a,'<span>\'+(TT.conv?"Send to":"Send invite to")+\'</span>',1)
        a='if(x.inv)return {who:x.from,t:"Invited you to a table",at:x.at};'; assert a in s,f
        s=s.replace(a,'if(x.inv){const it=MYTABLES.find(y=>y.id===x.inv);return {who:x.from,t:it&&it.conv?"Shared a conversation":"Invited you to a table",at:x.at}}',1)
        m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
        s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k,ensure_ascii=False),json.dumps(v,ensure_ascii=False)) for k,v in T.items() if '"%s":['%k not in s and '"%s": ['%k not in s)+s[m.end():]
    if s!=o: open(f,'w').write(s); print('patched',f)
    else: print('unchanged',f)
