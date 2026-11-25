"""Conversation page Share v3 (Gabriele 2026-11-19): button above the first right-column card,
opens a modal like the Table page's Invite one (people you've met, then the link, chat, email, more).
Run after patch_share.py. Idempotent."""
import re,json,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','invite-picker'))
import picker
FILES=sys.argv[1:] or ["library/body.html","library/timecapsule-library.html"]
ICON='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 15V4M8 8l4-4 4 4M5 13v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
BTN='<div class="rshwrap"><button type="button" class="rshare" id="rShare" aria-haspopup="dialog">'+ICON+'<span>Share this conversation</span></button></div>'
SV=lambda d:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+d+'</svg>'
LINK=SV('<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1 1M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1-1"/>')
CHAT=SV('<path d="M4 5h16v11H9l-5 4z"/>');MAIL=SV('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6l8.5 7 8.5-7"/>');MORE=SV('<path d="M12 15V3M7 8l5-5 5 5M5 13v7h14v-7"/>')
MODAL='''<div class="rsm" id="rShM0" hidden><div class="rsm-s" role="dialog" aria-modal="true" aria-labelledby="rsmT">
<button type="button" class="rsm-x" data-close aria-label="Close">×</button>
<div class="rsm-h"><h2 id="rsmT">Share this conversation</h2><p class="rsm-sub" id="rsmSub" data-noi18n></p></div>
<div id="ipkw"></div><p class="iporl">Or send the link</p>
<div class="rsm-lf"><input id="rShL" readonly aria-label="Link to this conversation" data-noi18n><button type="button" class="rsm-go" data-sh="copy">'''+LINK+'''<span>Copy link</span></button></div>
<div class="rsm-o"><a data-sh="chat" id="rShC" href="../help/live-pages/chats.html" target="_top">'''+CHAT+'''<span>Send in a chat</span></a><a data-sh="mail" id="rShM" href="#" target="_top">'''+MAIL+'''<span>Email</span></a><button type="button" data-sh="more">'''+MORE+'''<span>More</span></button></div>
<p class="rsm-f">Anyone with the link can read this conversation.</p>
</div></div>'''
CSS='''<style id="tc-rshare">
.rshwrap{margin:0 0 16px}
.rshare{display:flex;width:100%;justify-content:center;align-items:center;gap:8px;height:44px;padding:0 16px;border-radius:12px;border:1px solid var(--line,#3A4175);background:transparent;color:var(--fg,#EEF1FF);font:inherit;font-size:14px;font-weight:500;cursor:pointer}
.rshare svg{width:17px;height:17px}.rshare:hover{border-color:#17C3C8}
.rsm{position:fixed;inset:0;z-index:80;background:rgba(9,11,28,.62);backdrop-filter:blur(3px);-webkit-backdrop-filter:blur(3px);display:flex;align-items:flex-start;justify-content:center;padding:6vh 20px 20px}
.rsm[hidden]{display:none!important}
.rsm-s{width:100%;max-width:460px;max-height:calc(94vh - 20px);overflow:auto;background:#20264A;border:1px solid var(--line,#3A4175);border-radius:22px;padding:26px;box-shadow:0 30px 80px rgba(0,0,0,.5);color:var(--fg,#EEF1FF);text-align:left}
.rsm-x{float:right;width:34px;height:34px;border-radius:50%;border:1px solid var(--line,#3A4175);background:none;color:var(--mute,#A9B0D6);font-size:18px;cursor:pointer;margin:-6px -6px 0 0}
.rsm-h{padding-right:30px}.rsm-h h2{margin:0;font-size:22px;font-weight:500;letter-spacing:-.5px}
.rsm-sub{margin:6px 0 0;color:var(--mute,#A9B0D6);font-size:14px}
.rsm-lf{display:flex;gap:8px}
.rsm-lf input{flex:1;min-width:0;height:44px;border-radius:10px;border:1px solid var(--line,#3A4175);background:rgba(255,255,255,.04);color:var(--fg,#EEF1FF);padding:0 12px;font:inherit;font-size:14px}
.rsm-go{display:inline-flex;align-items:center;gap:7px;height:44px;padding:0 16px;border-radius:10px;border:0;background:#17C3C8;color:#0E1430;font:inherit;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap}
.rsm-go svg{width:17px;height:17px}
.rsm-o{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0 0}
.rsm-o a,.rsm-o button{display:flex;flex-direction:column;align-items:center;gap:8px;padding:14px 6px;border-radius:12px;border:1px solid var(--line,#3A4175);background:none;color:#C9CEEA;font:inherit;font-size:13px;text-decoration:none;cursor:pointer}
.rsm-o a:hover,.rsm-o button:hover{border-color:var(--mute,#A9B0D6);color:var(--fg,#EEF1FF)}
.rsm-o svg{width:22px;height:22px}
.rsm-f{margin:16px 0 0;color:var(--mute,#A9B0D6);font-size:13px;line-height:1.5}
@media (max-width:640px){.rsm{align-items:flex-end;padding:0}.rsm-s{max-width:none;border-radius:22px 22px 0 0;padding:22px 18px calc(22px + env(safe-area-inset-bottom,0px));max-height:92vh}}
</style>'''
JS='''<script id="tc-rshare-js">
(function(){var b=document.getElementById("rShare"),m=document.getElementById("rShM0");if(!b||!m)return;var last=null,built=false;
function rid(){var x=location.hash.match(/[#&]r=([^&]+)/);return x?x[1]:"free-will"}
function link(){return "timecapsule.app/c/"+rid()}
function T(k){return window.TCI18N&&TCI18N.t?TCI18N.t(k):k}
function open(){last=document.activeElement;var t=((document.getElementById("rTitle")||{}).textContent||"").trim(),tp=((document.getElementById("rcTop")||{}).textContent||"").trim(),n=Math.max(1,document.querySelectorAll("#rRounds button").length);
 document.getElementById("rsmSub").textContent=t;document.getElementById("rShL").value=link();
 document.getElementById("rShC").href="../help/live-pages/chats.html#compose&kind=conv&q="+encodeURIComponent(t)+"&th="+encodeURIComponent(tp)+"&host=Gregory&rounds="+n+"&r="+rid();
 document.getElementById("rShM").href="mailto:?subject="+encodeURIComponent(t)+"&body="+encodeURIComponent(t+"\\nhttps://"+link());
 if(!built&&window.tcIPK){tcIPK(document.getElementById("ipkw"));built=true}
 m.hidden=false;document.documentElement.style.overflow="hidden";var q=document.getElementById("ipkq");q&&q.focus()}
function close(){m.hidden=true;document.documentElement.style.overflow="";last&&last.focus&&last.focus()}
b.addEventListener("click",open);
m.addEventListener("click",function(e){if(e.target===m||e.target.closest("[data-close]")){close();return}
 var x=e.target.closest("[data-sh]");if(!x)return;var k=x.dataset.sh,u="https://"+link();
 if(k==="copy"){try{navigator.clipboard.writeText(u)}catch(_){}var s=x.querySelector("span");s.textContent=T("Copied ✓");setTimeout(function(){s.textContent=T("Copy link")},1600)}
 if(k==="more"){if(navigator.share){navigator.share({title:document.getElementById("rsmSub").textContent,url:u}).catch(function(){})}else{try{navigator.clipboard.writeText(u)}catch(_){}x.querySelector("span").textContent=T("Copied ✓")}}
});
document.addEventListener("keydown",function(e){if(e.key==="Escape"&&!m.hidden)close()});
})();
</script>'''
# share wording for the shared picker (the page has only this picker)
PK=picker.snippet().replace("Invite people you\\'ve met","Share with people you\\'ve met").replace("'Send invites':'Send invite'","'Send':'Send'").replace('<span>Invited</span>','<span>Sent to</span>')
assert "Share with people" in PK and "'Send':'Send'" in PK and 'Sent to' in PK
T={"Share this conversation":["Condividi questa conversazione","Compartir esta conversación","Κοινοποίησε αυτή τη συζήτηση"],
 "Share with people you've met":["Condividi con persone che hai conosciuto","Comparte con personas que conociste","Μοιράσου το με ανθρώπους που γνώρισες"],
 "Send":["Invia","Enviar","Αποστολή"],"Sent to":["Inviato a","Enviado a","Στάλθηκε σε"],
 "Anyone with the link can read this conversation.":["Chiunque abbia il link può leggere questa conversazione.","Cualquiera con el enlace puede leer esta conversación.","Όποιος έχει τον σύνδεσμο μπορεί να διαβάσει αυτή τη συζήτηση."],
 "Close":["Chiudi","Cerrar","Κλείσιμο"],"Link to this conversation":["Link a questa conversazione","Enlace a esta conversación","Σύνδεσμος σε αυτή τη συζήτηση"]}
T.update({k:v for k,v in picker.STRINGS.items() if k in("Type a name","Met at","Nobody by that name at your past tables. Send them the link instead.","They get it in their notifications.","Or send the link","Remove")})
def cut(s,tag,end):
    i=s.find(tag)
    while i>=0:
        j=s.find(end,i)+len(end); s=s[:i]+s[j:]; i=s.find(tag)
    return s
for f in FILES:
    s=open(f).read(); o=s
    if 'id="rShM0"' not in s:
        # remove v2 (inline panel between the boxes)
        i=s.find('<div class="rshwrap">')
        if i>=0:
            j=s.find('</div></div></div>',i)+len('</div></div></div>'); s=s[:i]+s[j:]
            s=s.replace('\n      \n      <!-- everyone -->','\n      <!-- everyone -->')
        for tag,end in (('<style id="tc-rshare">','</style>'),('<script id="tc-rshare-js">','</script>')): s=cut(s,tag,end)
        a='<aside aria-label="Pick it up again">\n      <!-- host -->'; assert a in s,f
        s=s.replace(a,'<aside aria-label="Pick it up again">\n      '+BTN+'\n      <!-- host -->',1)
        i=s.find('<section id="vrec">'); s=s[:i]+CSS+'\n'+s[i:]
        i=s.rfind('</body>'); add=MODAL+'\n'+('' if 'id="tc-ipk"' in s else PK)+JS+'\n'
        s=(s[:i]+add+s[i:]) if i>=0 else s+'\n'+add
        m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
        if m: s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k,ensure_ascii=False),json.dumps(v,ensure_ascii=False)) for k,v in T.items() if '"%s":['%k.replace('"','\\"') not in s and '%s:['%json.dumps(k) not in s)+s[m.end():]
    if s!=o: open(f,'w').write(s); print('patched',f)
    else: print('unchanged',f)
