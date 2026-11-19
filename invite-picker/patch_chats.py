"""Send in a chat opens a new message with the table's invite card attached; you pick who gets it (Karim 2026-11-18).
Chats: #compose&q=<title>&th=<topic>&when=<label>&free=N. Idempotent, marker "tc-compose". Run after invite-picker/patch.py and create-success/patch_back.py."""
import os, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from picker import PEOPLE

def rep(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:100]); return s.replace(a, b)

CSS = '''<style id="tc-compose-css">.to{max-width:520px;width:100%;margin:6px auto 0;position:relative}.to label{display:block;margin:0 0 8px;font-size:11.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--mute,#8E96C4)}
.to input{box-sizing:border-box;width:100%;height:46px;padding:0 14px;border-radius:12px;border:1px solid var(--line,#3A4175);background:rgba(255,255,255,.03);color:inherit;font:inherit;font-size:15px;outline:none}.to input:focus{border-color:#17C3C8}
.to ul{list-style:none;margin:6px 0 0;padding:4px;border-radius:12px;border:1px solid var(--line,#3A4175);background:#20264A}.to li{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:8px;cursor:pointer;font-size:14px}
.to li .a{width:32px;height:32px;border-radius:50%;overflow:hidden;flex:none}.to li .a svg{width:100%;height:100%;display:block}.to li small{display:block;color:var(--mute,#8E96C4);font-size:12px}
.to li[aria-selected=true],.to li:hover{background:rgba(255,255,255,.06)}.to li.none{cursor:default;color:var(--mute,#8E96C4);font-size:13px}.to li.none:hover{background:none}
.to .hint{margin:14px 0 0;color:var(--mute,#8E96C4);font-size:13px;line-height:1.5}.to .pv{margin:16px 0 0;padding:12px 14px;border-radius:14px;background:#2C3366;font-size:14px;line-height:1.5;word-break:break-word}
.to.warn input{border-color:#F2C14E}.to .pvw{margin:22px 0 0}.to .pvw .go,.att .go{display:none}.to .pvl{display:block;margin:0 0 8px;font-size:11.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--mute,#8E96C4)}
.draft{align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;gap:10px;margin:14px 0 4px;max-width:100%}.draft .dl{font-size:11.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#F2C14E}
.draft .inv{border:1.5px dashed rgba(124,92,255,.7)}.draft .go{display:none}.draft .dacts{display:flex;gap:8px;align-items:center}
.draft .dsend{all:unset;box-sizing:border-box;cursor:pointer;height:40px;padding:0 18px;border-radius:10px;background:#17C3C8;color:#0E1430;font-size:14px;font-weight:600}.draft .dsend:focus-visible{outline:2px solid #EEF1FF;outline-offset:2px}
.draft .dx{all:unset;cursor:pointer;height:40px;padding:0 12px;border-radius:10px;color:var(--mute,#8E96C4);font-size:14px}.draft .dx:hover{color:#EEF1FF}</style>'''

JS = '''
/* tc-compose: Send in a chat from a table opens a new message with the link written; you pick who gets it */
(function(){
  const h=new URLSearchParams((location.hash||"").slice(1)); if(!h.has("compose")) return false;
  const PP=%s, TT={id:"new",title:h.get("q")||"Your table",theme:h.get("th")||"Philosophy",when:h.get("when")||"",host:ME,free:+h.get("free")||0};
  if(!THEMES[TT.theme])TT.theme="Philosophy"; MYTABLES.push(TT);
  const people=PP.map(p=>({name:p[0],met:p[2]}));
  C.filter(c=>c.kind==="person").forEach(c=>{if(!people.some(p=>p.name===c.name))people.push({name:c.name,met:(c.ctx||"").replace(/<[^>]+>/g,"").replace(/^You met at /,"")})});
  let list=[],act=-1;
  S.cur=null; document.getElementById("app").classList.add("open"); renderList();
  document.getElementById("ch").innerHTML='<button class="back" type="button" id="back" aria-label="Back to conversations">←</button><div class="t"><div class="nm">New message</div><div class="sub">Pick who gets it</div></div>';
  document.getElementById("stream").innerHTML='<div class="to" id="to"><label for="tonm">To</label><input id="tonm" placeholder="Type a name" autocomplete="off" role="combobox" aria-expanded="false" aria-controls="tosug"><ul id="tosug" role="listbox" hidden></ul><p class="hint">Only people you met at a table.</p><div class="pvw"><span class="pvl">Invite card</span>'+invCard("new",true)+'</div></div>';
  document.getElementById("invbtn").style.display="none";
  const q=document.getElementById("tonm"),ul=document.getElementById("tosug"),txt=document.getElementById("txt");
  const ph=txt.placeholder; txt.placeholder="Add a note (optional)";
  function tray(name){const st=document.getElementById("stream");if(document.getElementById("att"))return;
    st.insertAdjacentHTML("beforeend",'<div class="draft" id="att"><span class="dl">Not sent yet</span>'+invCard("new",true)+'<div class="dacts"><button type="button" class="dx" id="attx">Remove</button><button type="button" class="dsend" id="atts"><span>Send invite to</span> <span data-noi18n>'+esc(name)+'</span></button></div></div>');
    st.scrollTop=st.scrollHeight;
    document.getElementById("attx").onclick=()=>{document.getElementById("att").remove();txt.placeholder=ph};
    document.getElementById("atts").onclick=()=>sendDraft()}
  function sendDraft(){const at=document.getElementById("att");if(!at)return;const t=txt.value.trim();txt.value="";at.remove();txt.placeholder=ph;
    push({from:ME,inv:"new",at:now()});if(t)push(["You",t,now()]);reply(S.cur)}
  function sug(){const v=q.value.trim().toLowerCase();document.getElementById("to").classList.remove("warn");
    if(!v){ul.hidden=true;q.setAttribute("aria-expanded","false");return}
    list=people.filter(p=>p.name.toLowerCase().includes(v)).sort((a,b)=>a.name.toLowerCase().indexOf(v)-b.name.toLowerCase().indexOf(v)).slice(0,5);act=list.length?0:-1;
    ul.innerHTML=list.length?list.map((p,i)=>'<li role="option" data-i="'+i+'" aria-selected="'+(i===act)+'"><span class="a">'+av(p.name)+'</span><span><span data-noi18n>'+esc(p.name)+'</span>'+(p.met?'<small><span>Met at</span> <span data-noi18n>'+esc(p.met)+'</span></small>':'')+'</span></li>').join(""):'<li class="none">Nobody by that name at your past tables.</li>';
    ul.hidden=false;q.setAttribute("aria-expanded","true")}
  function pick(i){const p=list[i];if(!p)return;let c=C.find(x=>x.kind==="person"&&x.name===p.name);
    if(!c){c={id:"new-"+p.name.toLowerCase(),kind:"person",name:p.name,online:false,seen:"",unread:0,ctx:"You met at <b>"+esc(p.met)+"</b>",m:[]};C.unshift(c)}
    try{history.replaceState(history.state,"",location.pathname+location.search)}catch(e){}
    open(c.id);tray(p.name);txt.focus()}
  q.addEventListener("input",sug);
  q.addEventListener("keydown",e=>{if(e.key==="ArrowDown"&&list.length){e.preventDefault();act=(act+1)%%list.length;ul.querySelectorAll("li[data-i]").forEach(li=>li.setAttribute("aria-selected",String(+li.dataset.i===act)))}
    else if(e.key==="ArrowUp"&&list.length){e.preventDefault();act=(act-1+list.length)%%list.length;ul.querySelectorAll("li[data-i]").forEach(li=>li.setAttribute("aria-selected",String(+li.dataset.i===act)))}
    else if(e.key==="Enter"&&act>=0&&!ul.hidden){e.preventDefault();pick(act)}});
  ul.addEventListener("mousedown",e=>{const li=e.target.closest("li[data-i]");if(li){e.preventDefault();pick(+li.dataset.i)}});
  document.getElementById("composer").addEventListener("submit",e=>{
    if(!S.cur){e.preventDefault();e.stopImmediatePropagation();document.getElementById("to").classList.add("warn");q.focus();return}
    if(!document.getElementById("att"))return;
    e.preventDefault();e.stopImmediatePropagation();sendDraft()},true);
  document.addEventListener("click",e=>{if(e.target.closest("#back")){const at=document.getElementById("att");if(at)at.remove();txt.placeholder=ph}});
  q.focus();
  return true;
})()||'''

STR = {'New message': ['Nuovo messaggio', 'Nuevo mensaje', 'Νέο μήνυμα'], 'Pick who gets it': ['Scegli a chi mandarlo', 'Elige a quién enviarlo', 'Διάλεξε σε ποιον θα πάει'],
       'To': ['A', 'Para', 'Προς'], 'Only people you met at a table.': ['Solo persone conosciute a un tavolo.', 'Solo personas que conociste en una mesa.', 'Μόνο άνθρωποι που γνώρισες σε τραπέζι.'], 'Invite card': ['Invito al tavolo', 'Invitación a la mesa', 'Πρόσκληση στο τραπέζι'], 'Not sent yet': ['Non ancora inviato', 'Aún sin enviar', 'Δεν στάλθηκε ακόμα'], 'Send invite to': ['Invia invito a', 'Enviar invitación a', 'Στείλε πρόσκληση στον/στην'], 'Remove': ['Togli', 'Quitar', 'Αφαίρεση'], 'Add a note (optional)': ['Aggiungi una nota (facoltativa)', 'Añade una nota (opcional)', 'Πρόσθεσε ένα σημείωμα (προαιρετικό)'],
       'Nobody by that name at your past tables.': ['Nessuno con questo nome ai tuoi tavoli passati.', 'Nadie con ese nombre en tus mesas pasadas.', 'Κανείς με αυτό το όνομα στα περασμένα τραπέζια σου.'],
       'Type a name': ['Scrivi un nome', 'Escribe un nombre', 'Γράψε ένα όνομα'], 'Met at': ['Conosciuto a', 'Os conocisteis en', 'Γνωριστήκατε στο']}
MSG = 'Pull up a chair with me: '

def chats(rel):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-compose' in s: return
    s = s.replace('</title>', '</title>' + CSS, 1)
    s = s.replace('<input id="q" placeholder="Search people and tables">', '<input id="q" placeholder="Search people and tables" autocomplete="off">')
    add = ''.join('%s:%s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in STR.items())
    s = rep(s, 'window.TCI18N_DICT={', 'window.TCI18N_DICT={' + add)
    s = rep(s, 'if(matchMedia("(min-width:821px)").matches)open("gregory");', (JS % json.dumps([list(x) for x in PEOPLE])).strip() + '\n(matchMedia("(min-width:821px)").matches&&open("gregory"));')
    open(p, 'w', encoding='utf8').write(s); print(rel, 'compose')

def create(rel):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    a = '<a href="chats.html" target="_top">Send in a chat</a>'
    if a not in s: return
    s = rep(s, a, '<a href="chats.html#compose&q=${encodeURIComponent(t.title)}&th=${encodeURIComponent(nt.theme)}&when=${encodeURIComponent(now?"Live now":longWhen(t.when))}&free=${nt.seats-1}" target="_top">Send in a chat</a>')
    open(p, 'w', encoding='utf8').write(s); print(rel, 'send in a chat link')

def table():
    p = os.path.join(ROOT, 'table-detail/timecapsule-table.html'); s = open(p, encoding='utf8').read()
    a = '<a href="${URL_CHATS}" target="_top">${I.chat}<span>Send in a chat'
    if a not in s: return
    s = rep(s, a, '<a href="${URL_CHATS}#compose&q=${encodeURIComponent(t.title)}&th=${encodeURIComponent(t.topic)}&when=${encodeURIComponent(isLive()?"Live now":new Date(st.startAt).toLocaleString("en-GB",{weekday:"short",day:"numeric",month:"short",hour:"2-digit",minute:"2-digit"}).replace(",","").replace(/ (\\d\\d:)/," · $1"))}&free=${Math.max(0,t.seats-t.people.length)}" target="_top">${I.chat}<span>Send in a chat')
    open(p, 'w', encoding='utf8').write(s); print('table page send in a chat link')

for r in ['help/live-pages/chats.html', 'invite/pages/chats.html']: chats(r)
for r in ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']: create(r)
table()
