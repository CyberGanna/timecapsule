"""Karim 2026-11-18: an upcoming table in My tables opens the full Table page instead of the "Manage table" pop-up.

Patches (idempotent, marker "tc-mt"):
  table-detail/timecapsule-table.html  #t=N shows one of your tables from My tables; host view with a host bar
  help/live-pages/mytables.html        rows 1-4 open ../../table-detail/timecapsule-table.html#t=N
Run: python3 table-detail/patch_mytables_link.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TP = os.path.join(ROOT, 'table-detail/timecapsule-table.html')
MP = os.path.join(ROOT, 'help/live-pages/mytables.html')


def rep(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:80])
    return s.replace(a, b)


# the same tables as My tables (ids match); "You" is the signed-in person (Gabriele)
MT = {
    1: dict(you='in', live=True),
    2: dict(title='What do we owe strangers?', topic='Philosophy', host='You', seats=8, lang='English', transcript=True,
            people=['You', 'Amara', 'Yuki', 'Kofi', 'Sofia', 'David'], talk='Amara', slug='owe-strangers', inMin=25, invites=1,
            desc='Neighbours, newcomers, the person next to you on the train. We ask how far kindness should reach when nobody is watching, and what a stranger can fairly expect from us.'),
    3: dict(title='Stoicism for hard times', topic='Philosophy', host='Marco', seats=10, lang='English', transcript=True,
            people=['Marco', 'Gregory', 'Mia', 'David', 'Yuki', 'Priya', 'Jonas', 'Elif'], talk='Marco', slug='stoicism-marco', inDays=1, hh=[18, 30], you='in',
            desc='Seneca, Epictetus and Marcus Aurelius wrote for difficult days. Bring one moment that tested you, and we look at what the Stoics would have done with it.'),
    4: dict(title='Stoics at the kitchen table', topic='Philosophy', host='You', seats=6, lang='English', transcript=False,
            people=['You', 'Tom', 'Ana'], talk='Tom', slug='stoics-kitchen', inDays=2, hh=[19, 0], invites=2,
            desc='An open circle about everyday Stoicism: cooking, chores and the small irritations of home. We take turns, no reading needed.'),
}
PROF_ADD = {
    'You': ['Switzerland', 'That is you.', ['Philosophy'], 2024, False],
    'Amara': ['Nigeria', 'Nurse. Collects proverbs.', ['Philosophy'], 2024, False],
    'Kofi': ['Ghana', 'Teacher. Loves a good counter-argument.', ['Philosophy'], 2024, True],
    'Sofia': ['Italy', 'Architect. Draws while she listens.', ['Philosophy'], 2025, False],
    'David': ['Israel', 'Software developer, amateur historian.', ['Philosophy', 'History'], 2024, False],
    'Marco': ['Italy', 'Hosts the Stoicism tables.', ['Philosophy'], 2023, True],
    'Jonas': ['Sweden', 'Carpenter. Asks why twice.', ['Philosophy'], 2025, False],
}
STRINGS = {  # English: [it, es, el]
    '← My tables': ['← I miei tavoli', '← Mis mesas', '← Τα τραπέζια μου'],
    'You host': ['Ospiti tu', 'Eres anfitrión', 'Φιλοξενείς'],
    'Start table': ['Avvia il tavolo', 'Iniciar la mesa', 'Ξεκίνα το τραπέζι'],
    'Edit table': ['Modifica il tavolo', 'Editar la mesa', 'Επεξεργασία τραπεζιού'],
    'Invite people': ['Invita persone', 'Invitar personas', 'Κάλεσε ανθρώπους'],
    'Copy link': ['Copia il link', 'Copiar enlace', 'Αντιγραφή συνδέσμου'],
    'Message guests': ['Scrivi agli ospiti', 'Escribir a los invitados', 'Μήνυμα στους καλεσμένους'],
    'Cancel table': ['Annulla il tavolo', 'Cancelar la mesa', 'Ακύρωση τραπεζιού'],
    'Keep it': ['Lo tengo', 'Mantenerla', 'Κράτα το'],
    'Host tools': ["Strumenti dell'host", 'Herramientas del anfitrión', 'Εργαλεία οικοδεσπότη'],
    'Open the room when you are ready. Guests can come in after you.': ['Apri la stanza quando sei pronto. Gli ospiti entrano dopo di te.', 'Abre la sala cuando estés listo. Los invitados entran después de ti.', 'Άνοιξε το δωμάτιο όταν είσαι έτοιμος. Οι καλεσμένοι μπαίνουν μετά από σένα.'],
    'You can open the room 30 minutes before it starts. Nobody can come in before you.': ['Puoi aprire la stanza 30 minuti prima. Nessuno entra prima di te.', 'Puedes abrir la sala 30 minutos antes. Nadie entra antes que tú.', 'Μπορείς να ανοίξεις το δωμάτιο 30 λεπτά πριν. Κανείς δεν μπαίνει πριν από σένα.'],
    'invite not answered yet': ['invito senza risposta', 'invitación sin respuesta', 'πρόσκληση χωρίς απάντηση'],
    'invites not answered yet': ['inviti senza risposta', 'invitaciones sin respuesta', 'προσκλήσεις χωρίς απάντηση'],
    'Cancel this table? Your guests get a message right away.': ['Annullare questo tavolo? I tuoi ospiti ricevono subito un messaggio.', '¿Cancelar esta mesa? Tus invitados reciben un mensaje al momento.', 'Ακύρωση του τραπεζιού; Οι καλεσμένοι σου ενημερώνονται αμέσως.'],
    'Table cancelled. Your guests were told.': ['Tavolo annullato. I tuoi ospiti sono stati avvisati.', 'Mesa cancelada. Tus invitados han sido avisados.', 'Το τραπέζι ακυρώθηκε. Οι καλεσμένοι σου ενημερώθηκαν.'],
    'Cancelled': ['Annullato', 'Cancelada', 'Ακυρώθηκε'],
    'Link copied': ['Link copiato', 'Enlace copiado', 'Ο σύνδεσμος αντιγράφηκε'],
}

CSS = '''<style id="tc-mt-css">.hpill{display:inline-flex;align-items:center;height:24px;padding:0 10px;border-radius:999px;font-size:12px;font-weight:600;letter-spacing:.04em;color:#F2C14E;background:rgba(242,193,78,.12)}
.htools{margin-top:18px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08)}.htools h4{margin:0 0 10px;font-size:11.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#8E96C4}
.htools .hb{display:flex;flex-wrap:wrap;gap:8px}.htools .hb button{all:unset;cursor:pointer;display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 14px;border-radius:10px;border:1px solid #3A4175;font-size:13.5px;color:#EEF1FF}
.htools .hb button:hover{border-color:#8E96C4}.htools .hb button:focus-visible{outline:2px solid #17C3C8;outline-offset:2px}.htools .hb svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;color:#A9B0D6}
.htools .hb .dz{color:#FF8A8A}.htools .hb .dz svg{color:#FF8A8A}.htools .cc{margin-top:12px;padding:14px;border-radius:12px;background:rgba(255,138,138,.08)}.htools .cc p{margin:0 0 10px;font-size:13.5px;color:#EEF1FF}
.htools .cc .hb .dzf{background:#FF8A8A;border-color:#FF8A8A;color:#2A0F14;font-weight:600}.cxl{display:inline-flex;align-items:center;height:24px;padding:0 10px;border-radius:999px;font-size:12px;font-weight:600;color:#FF8A8A;background:rgba(255,138,138,.12)}
.btn[disabled]{opacity:.45;cursor:default}.who2 li.me{width:auto;height:auto;border-radius:0;overflow:visible}</style>'''

ICON = {
    'edit': '<path d="M4 20h4L19 9l-4-4L4 16z"/>',
    'inv': '<circle cx="10" cy="8" r="4"/><path d="M3 20c0-3.9 3.1-6 7-6s7 2.1 7 6M19 8v6M16 11h6"/>',
    'link': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    'msg': '<path d="M4 5h16v11H9l-5 4z"/>',
    'x': '<circle cx="12" cy="12" r="8.5"/><path d="M9 9l6 6M15 9l-6 6"/>',
}


def patch_table():
    s = open(TP, encoding='utf8').read()
    if 'id="tc-mt-css"' in s:
        print('table page already patched'); return
    # strings for the translator (prepended to the page dictionary)
    add = ''.join('%s:%s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in STRINGS.items())
    s = rep(s, 'window.TCI18N_DICT={', 'window.TCI18N_DICT={' + add)
    s = rep(s, '</title>', '</title>' + CSS)
    # people the new tables need
    s = rep(s, 'const TABLES={', 'Object.assign(PROF,' + json.dumps(PROF_ADD) + ');\nconst TABLES={')
    # #t=N: one of your tables from My tables
    s = rep(s, 'setTimes();\nconst T=()=>TABLES[st.kind];',
            'setTimes();\n/* tc-mt: #t=N opens one of your tables from My tables (Karim 2026-11-18) */\nconst MT=' + json.dumps(MT) + ''';
(function(){const m=(location.hash||"").match(/[#&]t=(\\d+)/),d=m&&MT[m[1]];if(!d)return;st.mt=+m[1];
  if(d.host==="You"){st.kind="host";TABLES.host=d}else{if(d.title)TABLES.open=Object.assign({},TABLES.open,d);st.saved=d.you==="in"}
  if(d.live)st.time="live";
  if(d.inMin)st.startAt=Math.ceil((Date.now()+d.inMin*60000)/3e5)*3e5;
  if(d.inDays){const x=new Date();x.setDate(x.getDate()+d.inDays);x.setHours(d.hh[0],d.hh[1],0,0);st.startAt=+x}})();
addEventListener("hashchange",()=>{if(/[#&]t=\\d+/.test(location.hash))location.reload()});
const T=()=>TABLES[st.kind];''')
    s = rep(s, '<a class="back" href="${URL_AGENDA}" target="_top">← Back to tables</a>',
            '<a class="back" href="${st.mt?"../help/live-pages/mytables.html":URL_AGENDA}" target="_top">${st.mt?"← My tables":"← Back to tables"}</a>')
    s = rep(s, '  if(st.kind==="inv") s+=`<span class="ppill">${I.lock}<span>Private</span></span>`;\n',
            '  if(st.kind==="inv") s+=`<span class="ppill">${I.lock}<span>Private</span></span>`;\n  if(st.kind==="host") s+=st.cancelled?`<span class="cxl">Cancelled</span>`:`<span class="hpill">You host</span>`;\n')
    s = rep(s, '<b data-u="${t.host}">${t.host}</b>', '${t.host==="You"?"<b>Gabriele</b>":`<b data-u="${t.host}">${t.host}</b>`}')
    s = rep(s, '<span class="hav" data-u="${t.host}" tabindex="0">', '<span class="hav"${t.host==="You"?"":` data-u="${t.host}" tabindex="0"`}>')
    s = rep(s, '<small>Gabriele</small></div></li>`;', '<small>${st.kind==="host"?`<i class="mt">Host</i> · `:""}Gabriele</small></div></li>`;')
    # host bar
    ic = lambda k: '<svg viewBox="0 0 24 24" aria-hidden="true">' + ICON[k] + '</svg>'
    host = ('''  if(st.kind==="host"){
    if(st.cancelled) return `<p class="hint" style="margin-top:6px">Table cancelled. Your guests were told.</p>`;
    const near=isLive()||st.startAt-Date.now()<=30*60000,inv=t.invites||0;
    return `<div class="acts2"><button class="btn go" data-act="start"${near?"":" disabled"}>Start table</button></div>
      <p class="hint">${near?"Open the room when you are ready. Guests can come in after you.":"You can open the room 30 minutes before it starts. Nobody can come in before you."}${inv?` <span>${inv} ${inv===1?"invite not answered yet":"invites not answered yet"}</span>.`:""}</p>
      <div class="htools"><h4>Host tools</h4><div class="hb"><button type="button" data-act="edit">''' + ic('edit') + '''<span>Edit table</span></button><button type="button" data-act="invite">''' + ic('inv') + '''<span>Invite people</span></button><button type="button" data-act="copy">''' + ic('link') + '''<span>Copy link</span></button><button type="button" data-act="msg">''' + ic('msg') + '''<span>Message guests</span></button><button type="button" class="dz" data-act="cancel">''' + ic('x') + '''<span>Cancel table</span></button></div>
      ${st.confirmCancel?`<div class="cc"><p>Cancel this table? Your guests get a message right away.</p><div class="hb"><button type="button" class="dzf" data-act="cancelyes">Cancel table</button><button type="button" data-act="cancelno">Keep it</button></div></div>`:""}</div>`;
  }
''')
    s = rep(s, '  const share=st.kind==="open"?`<button class="btn" data-act="share">', host + '  const share=st.kind==="open"?`<button class="btn" data-act="share">')
    # actions
    s = rep(s, '  else if(a==="ics")toast(tt("Added to your calendar"));\n',
            '''  else if(a==="ics")toast(tt("Added to your calendar"));
  else if(a==="start"){if(!b.disabled)openJoin()}
  else if(a==="edit"){const t=T();top.location.href=TCI18N.u("../help/live-pages/create.html#again=1&th="+encodeURIComponent(t.topic)+"&q="+encodeURIComponent(t.title))}
  else if(a==="invite")openShare();
  else if(a==="copy"){try{navigator.clipboard.writeText(shareURL())}catch(x){}toast(tt("Link copied"))}
  else if(a==="msg")top.location.href=TCI18N.u(URL_CHATS);
  else if(a==="cancel"){st.confirmCancel=true;render()}
  else if(a==="cancelno"){st.confirmCancel=false;render()}
  else if(a==="cancelyes"){st.confirmCancel=false;st.cancelled=true;render()}
''')
    # the host opens the room as host
    s = rep(s, 'id="enter" href="${URL_LIVE}"', 'id="enter" href="${URL_LIVE}${st.kind==="host"?"#as=host":""}"')
    open(TP, 'w', encoding='utf8').write(s)
    print('table page patched')


def patch_mytables():
    s = open(MP, encoding='utf8').read()
    if 'tc-mt:' in s:
        print('my tables already patched'); return
    go = 'const TPAGE=id=>[1,2,3,4].includes(id)&&byId(id)&&!byId(id).past&&!byId(id).cancelled; /* tc-mt: these open the Table page (Karim 2026-11-18) */\nconst goTable=id=>{top.location.href=(window.TCI18N?TCI18N.u:(x=>x))("../../table-detail/timecapsule-table.html#t="+id)};\n'
    s = rep(s, 'function fromHash(){', go + 'function fromHash(){')
    s = rep(s, 'function fromHash(){const m=/^#t-(\\d+)$/.exec(location.hash);const t=m&&byId(+m[1]);if(t&&!t.cancelled){',
            'function fromHash(){const m=/^#t-(\\d+)$/.exec(location.hash);const t=m&&byId(+m[1]);if(t&&TPAGE(t.id)){goTable(t.id);return}if(t&&!t.cancelled){')
    s = rep(s, 'const op=e.target.closest("[data-open]"); if(op){closeMenu();sheetManage(byId(+op.dataset.open));return}',
            'const op=e.target.closest("[data-open]"); if(op){closeMenu();if(TPAGE(+op.dataset.open)){goTable(+op.dataset.open);return}sheetManage(byId(+op.dataset.open));return}')
    s = rep(s, 'if(op&&(e.key==="Enter"||e.key===" ")){e.preventDefault();sheetManage(byId(+op.dataset.open));return}',
            'if(op&&(e.key==="Enter"||e.key===" ")){e.preventDefault();if(TPAGE(+op.dataset.open)){goTable(+op.dataset.open);return}sheetManage(byId(+op.dataset.open));return}')
    open(MP, 'w', encoding='utf8').write(s)
    print('my tables patched')


if __name__ == '__main__':
    patch_table()
    patch_mytables()
