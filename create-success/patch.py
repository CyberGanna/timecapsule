"""'Your table is open!' screen, redesigned (Karim 2026-11-18). Idempotent, marker "tc-cok2".
Hero like a Tables card (blurred cover photo, or the topic glow), no link box: an "Invite people" button opens the picker,
date + time always shown, Go to my table for later tables too. Run after invite-picker/patch.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = '''<style id="tc-cok2">.cok{margin:6px auto 0!important;padding:0 28px 28px!important;overflow:hidden}
.cok .cktop{margin:0 -28px 22px;border-radius:21px 21px 0 0;padding:30px 0 26px}.cok .cktop .ring{width:176px;height:176px}
.cok h2{margin:0}.cok .ntinv{display:inline-flex;align-items:center;gap:8px;margin:20px auto 0;height:42px;padding:0 20px;border-radius:999px;border:1px solid var(--line);background:none;color:var(--text);font:inherit;font-size:14.5px;font-weight:500;cursor:pointer}
.cok .ntinv:hover{border-color:var(--mute)}.cok .ntinv[aria-expanded=true]{border-color:var(--teal,#17C3C8)}.cok .ntinv svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.cwrap>.back{margin-top:-6px}@media(max-width:640px){.cok{padding:0 18px 22px!important}.cok .cktop{margin:0 -18px 20px}.cok .cktop .ring{width:150px;height:150px}}</style>'''
STR = {"is private. Only people you invite can join. You host": ["è privato. Possono entrare solo le persone che inviti. Ospiti tu", "es privada. Solo pueden unirse las personas que invites. Eres el anfitrión", "είναι ιδιωτικό. Μπαίνουν μόνο όσοι καλέσεις. Φιλοξενείς εσύ"],
       "is on the Tables page. You host": ["è nella pagina Tavoli. Ospiti tu", "está en la página Mesas. Eres el anfitrión", "είναι στη σελίδα Τραπέζια. Φιλοξενείς εσύ"],
       ". Invite people who'd love this topic.": [". Invita chi amerebbe questo tema.", ". Invita a quien le encante este tema.", ". Κάλεσε όσους θα αγαπούσαν αυτό το θέμα."],
       "Back to tables": ["Torna ai tavoli", "Volver a las mesas", "Πίσω στα τραπέζια"]}

def rep(s, a, b):
    assert s.count(a) == 1, (s.count(a), a[:100]); return s.replace(a, b)

def run(rel):
    import json
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'id="tc-cok2"' in s: return
    s = s.replace('</title>', '</title>' + CSS, 1)
    add = ''.join('%s:%s,' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in STR.items())
    s = s.replace('window.TCI18N_DICT={', 'window.TCI18N_DICT={' + add, 1)
    # longWhen: always day, date and time (was "Wednesday, 18 Nov ·" within the hour)
    a = s[s.index('function longWhen(m){'):]; a = a[:a.index('\n}\n') + 3]
    s = rep(s, a, '''function longWhen(m){
  const d=new Date(Math.round((Date.now()+m*60000)/9e5)*9e5), dd=Math.round((new Date(d.toDateString())-new Date(new Date().toDateString()))/864e5);
  const day=dd===0?"Today":dd===1?"Tomorrow":FULLDAYS[d.getDay()];
  return `${day}, ${d.getDate()} ${MONTHS[d.getMonth()]} · ${String(d.getHours()).padStart(2,"0")}:${String(d.getMinutes()).padStart(2,"0")}`;
}
''')
    s = rep(s, '<div class="done-ring">${ring(t,true)}</div>',
            '<div class="ttop cktop" style="--c:${THEMES[t.theme]}">${t.img!=null?`<div class="tbg" style="background-image:url(\'${IMGS[t.img]}\')"></div>`:genBg(THEMES[t.theme])}${ring(t,true)}</div>')
    s = rep(s, "is on the Tables page. You host${me.mode",
            "${nt.vis===\"private\"?\"is private. Only people you invite can join. You host\":\"is on the Tables page. You host\"}${me.mode")
    a = s[s.index('<div class="share"><span>${link}</span><button id="ntshare"'):]; a = a[:a.index('</div>') + 6]
    s = rep(s, a, '<button class="ntinv" id="ntshare" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10" cy="8" r="4"/><path d="M3 20c0-3.9 3.1-6 7-6s7 2.1 7 6M19 8v6M16 11h6"/></svg>Invite people</button>')
    s = rep(s, '<div id="ntsopts" hidden style="max-width:400px;margin:16px auto 0">', '<div id="ntsopts" hidden style="max-width:420px;margin:16px auto 0">')
    s = rep(s, ':`<button class="cta go" data-close>Back to tables</button>`}</div>', ':`<button class="cta" data-close>Back to tables</button><button class="cta go" id="ntgo">Go to my table</button>`}</div>')
    s = rep(s, 'now:now?"1":"0"}).toString();', 'now:now?"1":"0",at:now?"0":String(Math.round((Date.now()+t.when*60000)/9e5)*9e5)}).toString();')
    open(p, 'w', encoding='utf8').write(s); print(rel, 'success screen')

for r in ['help/live-pages/create.html', 'help/live-pages/agenda.html', 'invite/pages/create.html', 'invite/pages/agenda.html']:
    run(r)
