"""Conversation page: Share button next to the title with inline options (Gabriele 2026-11-19).
"Share" (not Invite) because a conversation is not a table. Idempotent; run on body.html and the built page."""
import re,json,sys
FILES=sys.argv[1:] or ["library/body.html","library/timecapsule-library.html"]
ICON='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 15V4M8 8l4-4 4 4M5 13v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
OLD_T='<div class="rtrow"><h1 id="rTitle" data-noi18n></h1><button type="button" class="rshare" id="rShare" aria-expanded="false" aria-controls="rShP">'+ICON+'<span>Share</span></button></div>'
BTN='<button type="button" class="rshare" id="rShare" aria-expanded="false" aria-controls="rShP">'+ICON+'<span>Share this conversation</span></button>'
PANEL='''<div class="rshp" id="rShP" hidden><span class="rshl" id="rShL" data-noi18n></span><div class="rsho"><button type="button" data-sh="copy">Copy link</button><a data-sh="chat" id="rShC" href="../help/live-pages/chats.html" target="_top">Send in a chat</a><a data-sh="mail" id="rShM" href="#" target="_top">Email</a><button type="button" data-sh="more">More</button></div></div>'''
CSS='''<style id="tc-rshare">
.rshwrap{margin:0 0 16px}
.rshare{display:flex;width:100%;justify-content:center;align-items:center;gap:8px;height:44px;padding:0 16px;border-radius:12px;border:1px solid var(--line,rgba(255,255,255,.14));background:transparent;color:var(--text,#EEF1FF);font:inherit;font-size:14px;font-weight:500;cursor:pointer}
.rshare svg{width:17px;height:17px}
.rshare:hover,.rshare[aria-expanded="true"]{border-color:#1BC3C7}
.rshp{margin:10px 0 0;padding:14px 16px;border:1px solid var(--line,rgba(255,255,255,.14));border-radius:14px;background:rgba(255,255,255,.03)}
.rshp[hidden]{display:none!important}
.rshl{display:block;font-size:13px;color:var(--mute,#9AA3C7);margin-bottom:10px;word-break:break-all}
.rsho{display:flex;flex-wrap:wrap;gap:8px}
.rsho>*{display:inline-flex;align-items:center;height:34px;padding:0 14px;border-radius:999px;border:1px solid var(--line,rgba(255,255,255,.14));background:transparent;color:var(--text,#EEF1FF);font:inherit;font-size:13px;text-decoration:none;cursor:pointer}
.rsho>*:hover{border-color:#1BC3C7}
</style>'''
JS='''<script id="tc-rshare-js">
(function(){var b=document.getElementById("rShare"),p=document.getElementById("rShP");if(!b||!p)return;
function rid(){var m=location.hash.match(/[#&]r=([^&]+)/);return m?m[1]:"free-will"}
function link(){return "timecapsule.app/c/"+rid()}
b.addEventListener("click",function(){var o=p.hidden;p.hidden=!o;b.setAttribute("aria-expanded",o);if(o){document.getElementById("rShL").textContent=link();var t=(document.getElementById("rTitle")||{}).textContent||"";var tp=(document.getElementById("rcTop")||{}).textContent||"",rn=[0,Math.max(1,document.querySelectorAll("#rRounds button").length)];document.getElementById("rShC").href="../help/live-pages/chats.html#compose&kind=conv&q="+encodeURIComponent(t)+"&th="+encodeURIComponent(tp.trim())+"&host=Gregory&rounds="+(rn?rn[1]:1)+"&r="+rid();document.getElementById("rShM").href="mailto:?subject="+encodeURIComponent(t)+"&body="+encodeURIComponent(t+"\\nhttps://"+link())}});
p.addEventListener("click",function(e){var x=e.target.closest("[data-sh]");if(!x)return;var k=x.dataset.sh,u="https://"+link();
 if(k==="copy"){e.preventDefault();try{navigator.clipboard.writeText(u)}catch(_){}x.textContent="Copied ✓";setTimeout(function(){x.textContent=(window.TCI18N&&TCI18N.t?TCI18N.t("Copy link"):"Copy link")},1600)}
 if(k==="more"){e.preventDefault();if(navigator.share){navigator.share({title:(document.getElementById("rTitle")||{}).textContent,url:u}).catch(function(){})}else{try{navigator.clipboard.writeText(u)}catch(_){}x.textContent="Copied ✓"}}
});})();
</script>'''
T={"Share this conversation":["Condividi questa conversazione","Compartir esta conversación","Κοινοποίησε αυτή τη συζήτηση"],"Copy link":["Copia link","Copiar enlace","Αντιγραφή συνδέσμου"],"Send in a chat":["Invia in una chat","Enviar en un chat","Αποστολή σε συνομιλία"],"Email":["Email","Correo","Email"],"More":["Altro","Más","Περισσότερα"],"Copied ✓":["Copiato ✓","Copiado ✓","Αντιγράφηκε ✓"]}
for f in FILES:
    s=open(f).read(); o=s
    # v1 (2026-11-19, PR #80) had the button next to the title: undo it
    if OLD_T in s:
        s=s.replace(OLD_T,'<h1 id="rTitle" data-noi18n></h1>',1); s=s.replace('\n  '+PANEL.replace(' id="rShC"',''),'',1)
        for tag,end in (('<style id="tc-rshare">','</style>'),('<script id="tc-rshare-js">','</script>')):
            i=s.find(tag); j=s.find(end,i)+len(end); s=s[:i]+s[j:]
    if 'id="rShare"' not in s:
        a='<!-- everyone -->'; assert a in s,f
        s=s.replace(a,'<div class="rshwrap">'+BTN+PANEL+'</div>\n      '+a,1)
        i=s.find('<section id="vrec">'); s=s[:i]+CSS+'\n'+s[i:]
        i=s.rfind('</body>')
        s=(s[:i]+JS+'\n'+s[i:]) if i>=0 else s+'\n'+JS+'\n'
        m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
        if m: s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k,ensure_ascii=False),json.dumps(v,ensure_ascii=False)) for k,v in T.items() if '"%s":['%k not in s and '"%s": ['%k not in s)+s[m.end():]
    if s!=o: open(f,'w').write(s); print('patched',f)
    else: print('unchanged',f)
