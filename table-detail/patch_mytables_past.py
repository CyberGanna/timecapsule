"""Karim 2026-11-18: every table in My tables opens the Table page, not the pop-up.
Adds past tables (ids 11-14) and the waitlist table (id 5) to the Table page (#t=N), on top of patch_mytables_link.py.

Idempotent, marker "tc-mt2". Run after patch_mytables_link.py:
  python3 table-detail/patch_mytables_link.py && python3 table-detail/patch_mytables_past.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TP = os.path.join(ROOT, 'table-detail/timecapsule-table.html')
MP = os.path.join(ROOT, 'help/live-pages/mytables.html')


def rep(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:80])
    return s.replace(a, b)


# same ids as My tables; "You" is the signed-in person (Gabriele)
MT2 = {
    5: dict(title='Who writes history?', topic='History', host='Omar', seats=6, lang='English', transcript=True,
            people=['Omar', 'Priya', 'Tom', 'Sofia', 'Kofi', 'Elif'], talk='Omar', slug='who-writes-history', inDays=3, hh=[17, 0],
            you='wait', waitPos=2,
            desc='Winners, archivists, grandmothers at the kitchen table. We ask whose stories get kept, whose get lost, and what we each would want remembered.'),
    11: dict(title='Where is home?', topic='Home', host='Yuki', lang='English', transcript=True, saved=True, rated=True, you='in',
             people=['Yuki', 'Lena', 'You', 'Omar', 'Ana', 'Jonas'], slug='where-is-home', past=-1, hh=[20, 0],
             notes=['Home might be a person, not a place. (Lena)', 'Ask Yuki for the name of the tea house in Kyoto.', "Keep: 'You can be homesick for a place you never lived.'"],
             desc='The house you grew up in, the city you chose, the people who make a place feel right. We share where home is for us now, and how it changed.'),
    12: dict(title='Is happiness a skill?', topic='Philosophy', host='You', lang='English', transcript=True, saved=True,
             people=['You', 'Mia', 'Kofi', 'Elif', 'Omar', 'Yuki', 'Amara', 'Gregory'], slug='happiness-skill', past=-2, hh=[19, 0], score=4.8, coins=9,
             notes=["Next time open with the 'two lists' exercise.", "Kofi's point about gratitude and envy: follow up."],
             desc='Can we practise being happy, the way we practise an instrument? We try a few small exercises and talk about what really changed for us.'),
    13: dict(title='Green technology versus nuclear', topic='Energy', host='Lena', lang='English', transcript=True, saved=True, rated=False, you='in',
             people=['Lena', 'Kofi', 'David', 'Ana', 'You'], slug='green-vs-nuclear', past=-5, hh=[18, 0],
             notes=['Look up the Finnish storage project David mentioned.'],
             desc='Solar, wind, storage or nuclear: what gets us to clean energy fastest? Bring one fact that surprised you.'),
    14: dict(title='Are we free to change who we are?', topic='Philosophy', host='You', lang='English', transcript=True, saved=False, left=6,
             people=['You', 'Mia', 'Kofi', 'Elif', 'Omar', 'Amara'], slug='free-to-change', past=-1, hh=[19, 30], score=4.7, coins=7, notes=[],
             desc='Habits, character, the stories others tell about us. We ask how much of who we are is ours to change, and what it takes.'),
}
STRINGS = {  # English: [it, es, el]
    'No transcript was kept at this table.': ['A questo tavolo non è stata tenuta nessuna trascrizione.', 'En esta mesa no se guardó transcripción.', 'Σε αυτό το τραπέζι δεν κρατήθηκε απομαγνητοφώνηση.'],
    'Ended': ['Concluso', 'Terminada', 'Ολοκληρώθηκε'],
    'Who was there': ["Chi c'era", 'Quién estuvo', 'Ποιοι ήταν εκεί'],
    'Your kept notes': ['Le tue note tenute', 'Tus notas guardadas', 'Οι σημειώσεις που κράτησες'],
    'Only you see these.': ['Le vedi solo tu.', 'Solo tú las ves.', 'Τις βλέπεις μόνο εσύ.'],
    'were at the table': ['erano al tavolo', 'estuvieron en la mesa', 'ήταν στο τραπέζι'],
    'Save to Conversations': ['Salva in Conversazioni', 'Guardar en Conversaciones', 'Αποθήκευση στις Συζητήσεις'],
    'Host again': ['Ospita di nuovo', 'Organizar de nuevo', 'Φιλοξένησε ξανά'],
    'Open in Conversations': ['Apri in Conversazioni', 'Abrir en Conversaciones', 'Άνοιγμα στις Συζητήσεις'],
    'Rate and tip': ['Valuta e premia', 'Valora y premia', 'Βαθμολόγησε και φιλοδώρησε'],
    'Not saved yet.': ['Non ancora salvato.', 'Aún sin guardar.', 'Δεν έχει αποθηκευτεί ακόμα.'],
    "6 days left to save it. We'll remind you the day before.": ['Hai ancora 6 giorni per salvarlo. Te lo ricordiamo il giorno prima.', 'Te quedan 6 días para guardarla. Te lo recordaremos el día antes.', 'Έχεις 6 μέρες για να το αποθηκεύσεις. Θα σου το θυμίσουμε την προηγούμενη μέρα.'],
    'Saved to your Conversations.': ['Salvato nelle tue Conversazioni.', 'Guardada en tus Conversaciones.', 'Αποθηκεύτηκε στις Συζητήσεις σου.'],
    'Your 8 TimeCoins expire in 2 days.': ['I tuoi 8 TimeCoins scadono tra 2 giorni.', 'Tus 8 TimeCoins caducan en 2 días.', 'Τα 8 TimeCoins σου λήγουν σε 2 μέρες.'],
    'You rated it. Thank you.': ["L'hai valutato. Grazie.", 'Ya la valoraste. Gracias.', 'Το βαθμολόγησες. Ευχαριστούμε.'],
    'Took place': ['Si è svolto', 'Se celebró', 'Πραγματοποιήθηκε'],
    'People': ['Persone', 'Personas', 'Άνθρωποι'],
    'Saved to Conversations': ['Salvato in Conversazioni', 'Guardada en Conversaciones', 'Αποθηκεύτηκε στις Συζητήσεις'],
    'Not saved yet': ['Non ancora salvato', 'Aún sin guardar', 'Δεν έχει αποθηκευτεί ακόμα'],
    'Nothing was recorded or written down.': ['Nulla è stato registrato o scritto.', 'No se grabó ni se escribió nada.', 'Τίποτα δεν καταγράφηκε.'],
    'Received': ['Ricevuti', 'Recibidos', 'Ελήφθησαν'],
    'from guests': ['dagli ospiti', 'de los invitados', 'από τους καλεσμένους'],
    'To give': ['Da dare', 'Para dar', 'Για να δώσεις'],
    'Given': ['Dati', 'Dados', 'Δόθηκαν'],
    'You tipped the people who inspired you.': ['Hai premiato chi ti ha ispirato.', 'Premiaste a quien te inspiró.', 'Φιλοδώρησες όσους σε ενέπνευσαν.'],
    'Tip the people who inspired you.': ['Premia chi ti ha ispirato.', 'Premia a quien te inspiró.', 'Φιλοδώρησε όσους σε ενέπνευσαν.'],
    "You're on the waitlist": ["Sei in lista d'attesa", 'Estás en la lista de espera', 'Είσαι στη λίστα αναμονής'],
    'Leave the waitlist': ["Lascia la lista d'attesa", 'Salir de la lista de espera', 'Φύγε από τη λίστα αναμονής'],
    'Join the waitlist': ["Mettiti in lista d'attesa", 'Apúntate a la lista de espera', 'Μπες στη λίστα αναμονής'],
    "2nd in line. We'll tell you as soon as a chair opens up.": ['Sei 2° in fila. Ti avvisiamo appena si libera una sedia.', 'Eres 2.º en la cola. Te avisamos en cuanto quede una silla libre.', 'Είσαι 2ος στη σειρά. Θα σε ειδοποιήσουμε μόλις αδειάσει μια θέση.'],
    'The table is full. Join the waitlist and we tell you when a chair opens up.': ["Il tavolo è pieno. Mettiti in lista d'attesa e ti avvisiamo quando si libera una sedia.", 'La mesa está llena. Apúntate a la lista de espera y te avisamos cuando quede una silla libre.', 'Το τραπέζι είναι γεμάτο. Μπες στη λίστα αναμονής και θα σε ειδοποιήσουμε όταν αδειάσει μια θέση.'],
    'Table full': ['Tavolo pieno', 'Mesa llena', 'Γεμάτο τραπέζι'],
}

CSS = '''<style id="tc-mt2-css">.epill{display:inline-flex;align-items:center;height:24px;padding:0 10px;border-radius:999px;font-size:12px;font-weight:600;color:#A9B0D6;background:rgba(169,176,214,.12)}
.btn.gold{background:#F2C14E;border-color:#F2C14E;color:#2A1F05;font-weight:600}.amb{color:#F2B25C}
.kn{list-style:none;margin:0;padding:0}.kn li{padding:12px 0;border-top:1px solid rgba(255,255,255,.08);font-size:15px;line-height:1.45;color:#EEF1FF}.kn li:first-child{border-top:0;padding-top:4px}
.knh{margin:-6px 0 10px;font-size:13px;color:#8E96C4}</style>'''


def patch_table():
    s = open(TP, encoding='utf8').read()
    if 'id="tc-mt2-css"' in s:
        print('table page already patched (past)'); return
    add = ''.join('%s:%s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in STRINGS.items())
    s = rep(s, 'window.TCI18N_DICT={', 'window.TCI18N_DICT={' + add)
    s = rep(s, '</title>', '</title>' + CSS)
    s = rep(s, 'function render(){\n  const t=T(),c=TOPIC_C[t.topic];', 'function render(){\n  Object.assign(TICON,{Home:\'<path d="M4 11l8-7 8 7M6 9.5V20h12V9.5M10 20v-5h4v5"/>\',Energy:\'<path d="M13 3L5 13h6l-1 8 8-10h-6l1-8z"/>\',History:\'<path d="M6 3h12M6 21h12M7 3c0 5 5 6 5 9s-5 4-5 9M17 3c0 5-5 6-5 9s5 4 5 9"/>\'});\n  const t=T(),c=TOPIC_C[t.topic];')
    s = rep(s, 'const TOPIC_C={Philosophy:"#F29BD0",', 'const TOPIC_C={Home:"#5FE0DE",Energy:"#6CB8FF",Philosophy:"#F29BD0",')
    # merge the extra tables into MT before the #t=N reader runs, and read past/waitlist
    s = rep(s, '(function(){const m=(location.hash||"").match(/[#&]t=(\\d+)/),d=m&&MT[m[1]];if(!d)return;st.mt=+m[1];',
            'Object.assign(MT,' + json.dumps(MT2) + ''');/* tc-mt2 */
(function(){const m=(location.hash||"").match(/[#&]t=(\\d+)/),d=m&&MT[m[1]];if(!d)return;
  if(d.past!==undefined){d.seats=d.people.length;if(d.host!=="You"){d.people=d.people.filter(p=>p!=="You")}st.past=d;const x=new Date();x.setDate(x.getDate()+d.past);x.setHours(d.hh[0],d.hh[1],0,0);st.pastAt=+x;st.rated=!!d.rated}
  if(d.you==="wait"){st.wait=d.waitPos||1}})();
(function(){const m=(location.hash||"").match(/[#&]t=(\\d+)/),d=m&&MT[m[1]];if(!d)return;st.mt=+m[1];''')
    # status pill, countdown, caption
    s = rep(s, '  if(isLive()) s+=`<span class="lpill"><i></i><span>LIVE</span>',
            '  if(st.past){const d=new Date(st.pastAt);s+=`<span class="epill">${tt("Ended")} · ${dayLabel(d)} · ${hhmm(d)}</span>`}\n  else if(isLive()) s+=`<span class="lpill"><i></i><span>LIVE</span>')
    s = rep(s, '  if(st.kind==="host") s+=st.cancelled?`<span class="cxl">Cancelled</span>`:`<span class="hpill">You host</span>`;',
            '  if(st.kind==="host") s+=st.cancelled?`<span class="cxl">Cancelled</span>`:`<span class="hpill">${st.past?"You hosted":"You host"}</span>`;\n  if(st.wait&&!st.past) s+=`<span class="hpill" style="color:#A9B0D6;background:rgba(169,176,214,.12)">${tt("Table full")}</span>`;')
    s = rep(s, 'function cdHTML(){\n', 'function cdHTML(){\n  if(st.past) return "";\n')
    s = rep(s, '<p class="cap"><b>${people().length}</b> ${tt("at the table")} · ${t.seats-people().length} ${tt("free")}</p>',
            '<p class="cap">${st.past?`<b>${people().length}</b> ${tt("were at the table")}`:`<b>${people().length}</b> ${tt("at the table")} · ${t.seats-people().length} ${tt("free")}`}</p>')
    # facts for a past table
    s = rep(s, 'function factsHTML(){\n', '''function factsHTML(){
  if(st.past){const t=T(),p=st.past,d=new Date(st.pastAt),e=new Date(+d+60*60000),host=st.kind==="host";
    const tr=!t.transcript?`<dd>${tt("Not kept")}<span>${tt("Nothing was recorded or written down.")}</span></dd>`:p.saved?`<dd>${tt("Saved to Conversations")}<span>${tt("Anyone at the table can leave their words out of it.")}</span></dd>`:`<dd class="amb">${tt("Not saved yet")}<span>${tt("6 days left to save it. We'll remind you the day before.")}</span></dd>`;
    const co=host?`<dd><b style="font-weight:inherit">${p.coins}</b> <b style="font-weight:inherit">${tt("Received")}</b><span>★ ${p.score} ${tt("from guests")}</span></dd>`:st.rated?`<dd><b style="font-weight:inherit">8</b> <b style="font-weight:inherit">${tt("Given")}</b><span>${tt("You tipped the people who inspired you.")}</span></dd>`:`<dd class="amb"><b style="font-weight:inherit">8</b> <b style="font-weight:inherit">${tt("To give")}</b><span>${tt("Your 8 TimeCoins expire in 2 days.")}</span></dd>`;
    return `<dl class="facts2">
   <div>${I.cal}<div><dt>${tt("Took place")}</dt><dd>${longDate(d)}<span>${hhmm(d)} – ${hhmm(e)}</span></dd></div></div>
   <div>${I.seat}<div><dt>${tt("People")}</dt><dd><b style="font-weight:inherit">${people().length}</b> <b style="font-weight:inherit">${tt("were at the table")}</b><span>${t.lang}</span></dd></div></div>
   <div>${I.doc}<div><dt>Transcript</dt>${tr}</div></div>
   <div>${I.coin}<div><dt>TimeCoins</dt>${co}</div></div>
  </dl>`}
''')
    # actions for past and waitlist
    s = rep(s, '  if(st.kind==="host"){\n    if(st.cancelled)', '''  if(st.past){const p=st.past,host=st.kind==="host",U=(window.TCI18N?TCI18N.u:(x=>x));
    const again=host?`<button class="btn" data-act="edit">${tt("Host again")}</button>`:"";
    if(host&&t.transcript&&!p.saved) return `<div class="acts2"><a class="btn go" href="${U("../library/timecapsule-library.html#save&as=host&q="+encodeURIComponent(t.title))}" target="_top">${tt("Save to Conversations")}</a>${again}</div><p class="hint"><span class="amb">${tt("Not saved yet.")}</span> <span>${tt("6 days left to save it. We'll remind you the day before.")}</span></p>`;
    const conv=t.transcript&&p.saved?`<a class="btn${!host&&!st.rated?"":" go"}" href="${U("../help/live-pages/myuniverse.html#discussions")}" target="_top">${tt("Open in Conversations")}</a>`:"";
    if(!host&&!st.rated) return `<div class="acts2"><a class="btn gold" href="${U("../help/live-pages/mytables.html#rate")}" target="_top">${tt("Rate and tip")}</a>${conv}</div><p class="hint">${tt("Your 8 TimeCoins expire in 2 days.")}${conv?"":` <span>${tt("No transcript was kept at this table.")}</span>`}</p>`;
    return `<div class="acts2">${conv}${again}</div><p class="hint">${host?(p.saved?tt("Saved to your Conversations."):""):tt("You rated it. Thank you.")}</p>`;
  }
  if(st.wait&&!isOut()){
    if(st.wait>0) return `<div class="acts2"><button class="btn on" aria-pressed="true" style="cursor:default">${I.ok}<span>${tt("You're on the waitlist")}</span></button><button class="lnk" data-act="leavewait">${tt("Leave the waitlist")}</button></div><p class="hint">${tt("2nd in line. We'll tell you as soon as a chair opens up.")}</p>`;
    return `<div class="acts2"><button class="btn go" data-act="joinwait">${tt("Join the waitlist")}</button></div><p class="hint">${tt("The table is full. Join the waitlist and we tell you when a chair opens up.")}</p>`;
  }
  if(st.kind==="host"){
    if(st.cancelled)''')
    s = rep(s, '  else if(a==="start"){', '''  else if(a==="leavewait"){st.wait=-1;render();toast(tt("You left the waitlist"))}
  else if(a==="joinwait"){st.wait=2;render();toast(tt("You're on the waitlist"))}
  else if(a==="start"){''')
    # who was there + kept notes instead of Good to know
    s = rep(s, '  return `<h2>${isLive()?"At the table":"Who\'s coming"} <small>${ppl.length} / ${t.seats}</small></h2><ul class="who2">${rows}${frees}</ul>`;',
            '  if(st.past) return `<h2>${tt("Who was there")} <small>${ppl.length}</small></h2><ul class="who2">${rows}</ul>`;\n  return `<h2>${isLive()?"At the table":"Who\'s coming"} <small>${ppl.length} / ${t.seats}</small></h2><ul class="who2">${rows}${frees}</ul>`;')
    s = rep(s, 'function goodHTML(){\n  const t=T();\n', '''function goodHTML(){
  const t=T();
  if(st.past){const n=st.past.notes||[];return n.length?`<h2>${tt("Your kept notes")} <small>${n.length}</small></h2><p class="knh">${tt("Only you see these.")}</p><ul class="kn">${n.map(x=>`<li data-noi18n>${x.replace(/</g,"&lt;")}</li>`).join("")}</ul>`:""}
''')
    s = rep(s, '<div><b style="cursor:default">You</b><small>${st.kind==="host"?`<i class="mt">Host</i> · `:""}Gabriele</small>',
            '<div><b style="cursor:default">You</b><small>${st.kind==="host"?`<i class="mt">Host</i> · `:""}Gabriele</small>')
    # the base page predates the rename "Discussions" -> "Conversations" (Karim 2026-11-18)
    s = re.sub(r'(?<![/#|(\w-])([Dd])iscussion(s?)\b(?!\.html)(?![\w-])', lambda m: ('C' if m.group(1) == 'D' else 'c') + 'onversation' + m.group(2), s)
    s = re.sub(r'(?<!in )([Dd])iscussion([ei])\b', lambda m: ('C' if m.group(1) == 'D' else 'c') + 'onversazion' + m.group(2), s)
    s = re.sub(r'in Discussion([ei])\b', r'in Conversazion\1', s)
    open(TP, 'w', encoding='utf8').write(s)
    print('table page patched (past)')


def patch_mytables():
    s = open(MP, encoding='utf8').read()
    if 'tc-mt2' in s:
        print('my tables already patched (past)'); return
    s = rep(s, 'const TPAGE=id=>[1,2,3,4].includes(id)&&byId(id)&&!byId(id).past&&!byId(id).cancelled;',
            'const TPAGE=id=>[1,2,3,4,5,11,12,13,14].includes(id)&&byId(id)&&!byId(id).cancelled; /* tc-mt2: past and waitlist tables too */')
    open(MP, 'w', encoding='utf8').write(s)
    print('my tables patched (past)')


if __name__ == '__main__':
    patch_table()
    patch_mytables()
