"""Tables page: a "My tables" chip at the end of the day filters (Karim 2026-11-18). Idempotent, marker "tc-mine".
Shows only upcoming tables you host or saved a chair at, in the same cards. Sample: you saved chairs at
"Is free will an illusion?" (1) and "Stoicism for hard times" (8), as in My tables."""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = '<style id="tc-mine">.day.mine{margin-left:14px;position:relative}.day.mine::before{content:"";position:absolute;left:-10px;top:22%;bottom:22%;width:1px;background:var(--line,#3A4175)}.mfoot{margin:6px 0 0;font-size:14px;color:var(--mute)}.mfoot a{color:var(--teal,#17C3C8);text-decoration:none;font-weight:500}.mfoot a:hover{text-decoration:underline}</style>'
STR = {"open table": ["tavolo aperto", "mesa abierta", "ανοιχτό τραπέζι"], "My tables": ["I miei tavoli", "Mis mesas", "Τα τραπέζια μου"],
       "Nothing coming up yet. Save a chair at a table, or open your own.": ["Ancora niente in programma. Tieni un posto a un tavolo, o aprine uno tuo.", "Aún no tienes nada previsto. Reserva un sitio en una mesa o abre la tuya.", "Τίποτα προγραμματισμένο ακόμα. Κράτα μια καρέκλα σε ένα τραπέζι ή άνοιξε το δικό σου."],
       "Past tables, notes and transcripts are in": ["Tavoli passati, note e trascrizioni sono in", "Las mesas pasadas, notas y transcripciones están en", "Τα περασμένα τραπέζια, οι σημειώσεις και τα πρακτικά είναι στο"]}

def rep(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:100]); return s.replace(a, b)

def run(rel):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'id="tc-mine"' in s: return
    s = s.replace('</title>', '</title>' + CSS, 1)
    add = ''.join('%s:%s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in STR.items())
    s = rep(s, 'window.TCI18N_DICT={', 'window.TCI18N_DICT={' + add)
    s = rep(s, 'q:"",joined:new Set()};', 'q:"",joined:new Set([1,8])}; /* tc-mine: chairs you saved, as in My tables */')
    s = rep(s, '["week","This week"]];', '["week","This week"],["mine","My tables"]];')
    s = rep(s, '`<button class="day${k==="live"?" now":""}"', '`<button class="day${k==="live"?" now":""}${k==="mine"?" mine":""}"')
    s = rep(s, '  const vis=T.filter(match);\n', '  const D0=S.day, mineOnly=D0==="mine"; if(mineOnly) S.day="all";\n  const vis=T.filter(match).filter(t=>!mineOnly||t.mine||S.joined.has(t.id));\n')
    a = '  if(!h) h=`<div class="empty">No tables match these filters yet.<br><button id="reset">Show all tables</button></div>`;\n'
    s = rep(s, a, '''  S.day=D0;
  if(mineOnly){if(!h) h=`<div class="empty">Nothing coming up yet. Save a chair at a table, or open your own.<br><button id="reset">Show all tables</button></div>`;
    h+=`<p class="mfoot"><span>Past tables, notes and transcripts are in</span> <a href="mytables.html#past" target="_top">My tables ›</a></p>`}
''' + a)
    s = rep(s, '${live.length} open tables</span>', '${live.length} ${live.length===1?"open table":"open tables"}</span>')
    open(p, 'w', encoding='utf8').write(s); print(rel, 'My tables chip')

for r in ['help/live-pages/agenda.html', 'invite/pages/agenda.html']:
    run(r)
