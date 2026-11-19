"""Invite people you've met (Karim 2026-11-18): one shared picker for the Invite panels.

tcIPK(el, {title}) renders a search box; typing suggests people from your past tables
("Met at ..."), you pick a few as chips, then Send invites. Self-contained CSS + JS.
"""
PEOPLE = [  # name, colour, last table you shared
    ('Yuki', '#E07A5F', 'Where is home?'), ('Lena', '#17C3C8', 'Where is home?'), ('Omar', '#F2C14E', 'Where is home?'),
    ('Ana', '#7C5CFF', 'Where is home?'), ('Jonas', '#5FA8E0', 'Where is home?'), ('Mia', '#E05FA8', 'Is happiness a skill?'),
    ('Kofi', '#3DBE8B', 'Is happiness a skill?'), ('Elif', '#C9A0FF', 'Is happiness a skill?'), ('Amara', '#FF8A5C', 'Is happiness a skill?'),
    ('Gregory', '#8E7CFF', 'Is happiness a skill?'), ('David', '#4FC3F7', 'Green technology versus nuclear'),
    ('Tom', '#F28C8C', 'Stoics at the kitchen table'), ('Priya', '#FFB74D', 'Is free will an illusion?'),
    ('Marco', '#81C784', 'Stoicism for hard times'), ('Sofia', '#BA68C8', 'Stoicism for hard times'), ('Elena', '#4DB6AC', 'Is free will an illusion?'),
]
STRINGS = {  # English: [it, es, el]
    'Invite people': ['Invita persone', 'Invitar personas', 'Κάλεσε ανθρώπους'],
    'Invite': ['Invita', 'Invitar', 'Πρόσκληση'],
    "Invite people you've met": ['Invita persone che hai conosciuto', 'Invita a personas que conociste', 'Κάλεσε ανθρώπους που γνώρισες'],
    'Type a name': ['Scrivi un nome', 'Escribe un nombre', 'Γράψε ένα όνομα'],
    'Met at': ['Conosciuto a', 'Os conocisteis en', 'Γνωριστήκατε στο'],
    'Send invites': ['Invia gli inviti', 'Enviar invitaciones', 'Στείλε τις προσκλήσεις'],
    'Send invite': ["Invia l'invito", 'Enviar invitación', 'Στείλε την πρόσκληση'],
    'Nobody by that name at your past tables. Send them the link instead.': ['Nessuno con questo nome ai tuoi tavoli passati. Mandagli il link.', 'Nadie con ese nombre en tus mesas pasadas. Envíale el enlace.', 'Κανείς με αυτό το όνομα στα περασμένα τραπέζια σου. Στείλε του τον σύνδεσμο.'],
    'Invited': ['Invitati', 'Invitados', 'Προσκλήθηκαν'],
    'They get it in their notifications.': ['Lo ricevono nelle notifiche.', 'Lo reciben en sus notificaciones.', 'Το βλέπουν στις ειδοποιήσεις τους.'],
    'Or send the link': ['Oppure manda il link', 'O envía el enlace', 'Ή στείλε τον σύνδεσμο'],
    'Remove': ['Togli', 'Quitar', 'Αφαίρεση'],
    'Your table is open!': ['Il tuo tavolo è aperto!', '¡Tu mesa está abierta!', 'Το τραπέζι σου άνοιξε!'],
    'Later': ['Più tardi', 'Más tarde', 'Αργότερα'],
    'Go to my table': ['Vai al mio tavolo', 'Ir a mi mesa', 'Πήγαινε στο τραπέζι μου'],
    "is on the Tables page. You host. Invite people who'd love this topic.": ['è nella pagina Tavoli. Ospiti tu. Invita chi amerebbe questo tema.', 'está en la página Mesas. Eres el anfitrión. Invita a quien le encante este tema.', 'είναι στη σελίδα Τραπέζια. Φιλοξενείς εσύ. Κάλεσε όσους θα αγαπούσαν αυτό το θέμα.'],
}
CSS = '''<style id="tc-ipk-css">.ipk{text-align:left;margin:0}#ipkw{margin-top:18px}.ipk .ipl{display:block;margin:0 0 8px;font-size:11.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#8E96C4}
.ipk .ipb{display:flex;flex-wrap:wrap;align-items:center;gap:6px;min-height:44px;padding:5px 8px;border-radius:12px;border:1px solid #3A4175;background:rgba(255,255,255,.03);cursor:text}
.ipk .ipb:focus-within{border-color:#17C3C8}.ipk input{flex:1;min-width:120px;border:0;background:none;outline:none;color:#EEF1FF;font:inherit;font-size:14px;padding:6px 4px}
.ipk input::placeholder{color:#8E96C4}.ipk .chip{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 4px 0 3px;border-radius:999px;background:#2C3366;color:#EEF1FF;font-size:13px}
.ipk .chip button{all:unset;cursor:pointer;width:20px;height:20px;border-radius:50%;display:grid;place-items:center;color:#8E96C4;font-size:15px;line-height:1}.ipk .chip button:hover{color:#EEF1FF;background:rgba(255,255,255,.08)}
.ipk .ia{flex:none;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-size:11.5px;font-weight:600;color:#121633;background:var(--a)}
.ipk ul{list-style:none;margin:6px 0 0;padding:4px;border-radius:12px;border:1px solid #3A4175;background:#20264A}.ipk li{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:8px;cursor:pointer;color:#EEF1FF;font-size:14px}
.ipk li .ia{width:30px;height:30px;font-size:13px}.ipk li small{display:block;color:#8E96C4;font-size:12px}.ipk li[aria-selected=true],.ipk li:hover{background:rgba(255,255,255,.06)}.ipk li.none{cursor:default;color:#8E96C4;font-size:13px}.ipk li.none:hover{background:none}
.ipk .ips{all:unset;box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;margin-top:10px;height:40px;padding:0 18px;border-radius:10px;background:#17C3C8;color:#0E1430;font-size:14px;font-weight:600}
.ipk .ips:focus-visible{outline:2px solid #EEF1FF;outline-offset:2px}.ipk .ipd{margin:10px 0 0;font-size:13.5px;color:#EEF1FF}.ipk .ipd i{font-style:normal;color:#3DDC97;margin-right:6px}.ipk .ipd small{color:#8E96C4;font-size:13px}
.iporl{margin:18px 0 8px!important;font-size:11.5px!important;line-height:1.4!important;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#8E96C4;text-align:left}</style>'''
JS = '''<script id="tc-ipk">
window.tcIPK=function(root){
  var PP=%s, sel=[], act=-1, list=[];
  var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})};
  var ia=function(p){return '<span class="ia" style="--a:'+p[1]+'" aria-hidden="true">'+p[0][0]+'</span>'};
  root.innerHTML='<div class="ipk"><label class="ipl" for="ipkq">Invite people you\\'ve met</label><div class="ipb"><span class="ipc"></span><input id="ipkq" autocomplete="off" placeholder="Type a name" role="combobox" aria-expanded="false" aria-controls="ipkl"></div><ul id="ipkl" role="listbox" hidden></ul><div class="ipf"></div></div>';
  var q=root.querySelector("input"),ul=root.querySelector("ul"),chips=root.querySelector(".ipc"),foot=root.querySelector(".ipf");
  function draw(){
    chips.innerHTML=sel.map(function(p){return '<span class="chip">'+ia(p)+'<span data-noi18n>'+esc(p[0])+'</span><button type="button" data-rm="'+esc(p[0])+'" aria-label="Remove">×</button></span>'}).join("");
    foot.innerHTML=sel.length?'<button type="button" class="ips">'+(sel.length>1?'Send invites':'Send invite')+'</button>':"";
    q.placeholder=sel.length?"":"Type a name";
  }
  function sug(){
    var v=q.value.trim().toLowerCase();
    if(!v){ul.hidden=true;q.setAttribute("aria-expanded","false");return}
    list=PP.filter(function(p){return sel.indexOf(p)<0&&p[0].toLowerCase().indexOf(v)>=0}).sort(function(a,b){return a[0].toLowerCase().indexOf(v)-b[0].toLowerCase().indexOf(v)}).slice(0,5);
    act=list.length?0:-1;
    ul.innerHTML=list.length?list.map(function(p,i){return '<li role="option" data-i="'+i+'" aria-selected="'+(i==act)+'">'+ia(p)+'<span><span data-noi18n>'+esc(p[0])+'</span><small><span>Met at</span> <span data-noi18n>'+esc(p[2])+'</span></small></span></li>'}).join(""):'<li class="none">Nobody by that name at your past tables. Send them the link instead.</li>';
    ul.hidden=false;q.setAttribute("aria-expanded","true");
  }
  function pick(i){var p=list[i];if(!p)return;sel.push(p);q.value="";ul.hidden=true;foot.querySelector(".ipd")&&(foot.innerHTML="");draw();q.focus()}
  function hi(){ul.querySelectorAll("li[data-i]").forEach(function(li){li.setAttribute("aria-selected",String(+li.dataset.i==act))})}
  q.addEventListener("input",sug);
  q.addEventListener("keydown",function(e){
    if(e.key=="ArrowDown"&&list.length){e.preventDefault();act=(act+1)%%list.length;hi()}
    else if(e.key=="ArrowUp"&&list.length){e.preventDefault();act=(act-1+list.length)%%list.length;hi()}
    else if(e.key=="Enter"&&!ul.hidden&&act>=0){e.preventDefault();pick(act)}
    else if(e.key=="Backspace"&&!q.value&&sel.length){sel.pop();draw()}
    else if(e.key=="Escape"&&!ul.hidden){e.stopPropagation();ul.hidden=true}
  });
  ul.addEventListener("mousedown",function(e){var li=e.target.closest("li[data-i]");if(li){e.preventDefault();pick(+li.dataset.i)}});
  root.querySelector(".ipb").addEventListener("click",function(e){var b=e.target.closest("[data-rm]");if(b){e.stopPropagation();sel=sel.filter(function(p){return p[0]!=b.dataset.rm});draw();q.focus();return}q.focus()});
  foot.addEventListener("click",function(e){if(!e.target.closest(".ips"))return;var n=sel.map(function(p){return p[0]});
    foot.innerHTML='<p class="ipd"><i>✓</i><span>Invited</span> <span data-noi18n>'+esc(n.join(", "))+'</span>. <small>They get it in their notifications.</small></p>';sel=[];chips.innerHTML="";q.placeholder="Type a name"});
  draw();
};
</script>'''


def snippet():
    import json
    return CSS + JS % json.dumps([list(p) for p in PEOPLE])


def add_strings(s):
    import json
    add = ''.join('%s:%s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in STRINGS.items())
    assert 'window.TCI18N_DICT={' in s
    return s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={' + add, 1)
