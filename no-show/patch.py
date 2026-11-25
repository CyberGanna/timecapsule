"""No-show rule (Gabriele approved 2026-11-22):
- Notifications page: the "Starting in 10 min" reminder gets a "Can't make it?" button that gives the chair back.
- FAQ: "What if I can't make it?" mentions the button and no penalty; new question "What if I don't show up?".
- Guides, Save a chair: a line on the 10-minute release.
EN/IT/ES/EL. Idempotent, marker "tc-noshow"."""
import os, json, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T = {
 "Can't make it?": ["Non riesci a esserci?", "¿No puedes ir?", "Δεν μπορείς να έρθεις;"],
 "Chair given back. Someone else can sit.": ["Posto liberato. Può sedersi qualcun altro.", "Sitio liberado. Puede sentarse otra persona.", "Η καρέκλα ελευθερώθηκε. Μπορεί να κάτσει κάποιος άλλος."],
 "You can also tap Can't make it? on the reminder. Giving a chair back before the table starts has no penalty.": [
   "Puoi anche toccare Non riesci a esserci? nel promemoria. Liberare un posto prima dell'inizio non ha nessuna penalità.",
   "También puedes tocar ¿No puedes ir? en el recordatorio. Liberar un sitio antes de que empiece la mesa no tiene ninguna penalización.",
   "Μπορείς επίσης να πατήσεις «Δεν μπορείς να έρθεις;» στην υπενθύμιση. Αν αφήσεις την καρέκλα πριν ξεκινήσει το τραπέζι, δεν υπάρχει καμία συνέπεια."],
 "What if I don't show up?": ["E se non mi presento?", "¿Y si no me presento?", "Κι αν δεν εμφανιστώ;"],
 "We keep your chair for the first 10 minutes. After that it goes to the first person on the waitlist, or opens to anyone. Missing one table is fine. After three missed tables in 30 days, you can only save a chair on the day of the table for two weeks. Only you see this, and it never touches your TimeCoins or your profile.": [
   "Teniamo il tuo posto per i primi 10 minuti. Dopo passa alla prima persona in lista d'attesa, oppure si libera per chiunque. Mancare a un tavolo va bene. Dopo tre tavoli mancati in 30 giorni, per due settimane puoi tenere un posto solo il giorno stesso del tavolo. Lo vedi solo tu, e non tocca mai i tuoi TimeCoins né il tuo profilo.",
   "Guardamos tu sitio durante los primeros 10 minutos. Después pasa a la primera persona en la lista de espera, o queda libre para cualquiera. Faltar a una mesa no pasa nada. Tras tres mesas perdidas en 30 días, durante dos semanas solo puedes guardar un sitio el mismo día de la mesa. Solo lo ves tú, y nunca afecta a tus TimeCoins ni a tu perfil.",
   "Κρατάμε την καρέκλα σου για τα πρώτα 10 λεπτά. Μετά πηγαίνει στο πρώτο άτομο στη λίστα αναμονής ή ανοίγει για όλους. Αν λείψεις από ένα τραπέζι, δεν πειράζει. Μετά από τρία τραπέζια που έχασες σε 30 ημέρες, για δύο εβδομάδες μπορείς να κρατάς καρέκλα μόνο την ίδια μέρα του τραπεζιού. Το βλέπεις μόνο εσύ και δεν επηρεάζει ποτέ τα TimeCoins ή το προφίλ σου."],
 "If you don't join within 10 minutes of the start, your chair goes to someone else. To give it back sooner, tap Can't make it? on the reminder.": [
   "Se non entri entro 10 minuti dall'inizio, il tuo posto passa a qualcun altro. Per liberarlo prima, tocca Non riesci a esserci? nel promemoria.",
   "Si no entras en los 10 minutos tras el inicio, tu sitio pasa a otra persona. Para liberarlo antes, toca ¿No puedes ir? en el recordatorio.",
   "Αν δεν μπεις μέσα σε 10 λεπτά από την έναρξη, η καρέκλα σου πηγαίνει σε κάποιον άλλο. Για να την αφήσεις νωρίτερα, πάτησε «Δεν μπορείς να έρθεις;» στην υπενθύμιση."],
}

def add_dict(s):
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, flags=re.S)
    if not m:
        return s
    d = json.loads(m.group(1)); d.update(T)
    js = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return s[:m.start(1)] + js + s[m.end(1):]

def esc(x):
    return x.replace("'", "&#39;") if False else x

FAQ_A = "<p>Give up your chair in My tables so someone else can sit. At a live table you can leave at any time with Leave table.</p></details>"
FAQ_B = ("<p>Give up your chair in My tables so someone else can sit. At a live table you can leave at any time with Leave table.</p>"
         "<p><!--tc-noshow-->You can also tap Can't make it? on the reminder. Giving a chair back before the table starts has no penalty.</p></details>\n"
         " <details><summary><span>What if I don't show up?</span><svg><use href=\"#i-plus\"/></svg></summary>"
         "<p>We keep your chair for the first 10 minutes. After that it goes to the first person on the waitlist, or opens to anyone. Missing one table is fine. After three missed tables in 30 days, you can only save a chair on the day of the table for two weeks. Only you see this, and it never touches your TimeCoins or your profile.</p></details>")
GD_A = "If plans change, give up your chair in My tables so someone else can sit.</p>"
GD_B = GD_A + "<p><!--tc-noshow-->If you don't join within 10 minutes of the start, your chair goes to someone else. To give it back sooner, tap Can't make it? on the reminder.</p>"

N_ACT_A = "acts:[{l:'Join now',c:'pri',go:'live'}]},"
N_ACT_B = "acts:[{l:'Join now',c:'pri',go:'live'},{l:\"Can't make it?\",c:'',free:1}]},"
N_ST_A = " if(n.state==='rated')"
N_ST_B = " if(n.state==='freed')return `<span class=\"btn done\" style=\"color:var(--mute)\"><span>Chair given back. Someone else can sit.</span></span>`;/*tc-noshow*/\n if(n.state==='rated')"
N_H_A = "  if(act.inv){"
N_H_B = "  if(act.free){e.preventDefault();n.state='freed';render();toast('Chair given back. Someone else can sit.',()=>{delete n.state;render()});return}\n  if(act.inv){"

JOBS = {
 'help/timecapsule-faq.html': [(FAQ_A, FAQ_B)],
 'help/faq-body.html': [(FAQ_A, FAQ_B)],
 'help/timecapsule-guides.html': [(GD_A, GD_B)],
 'help/guides-body.html': [(GD_A, GD_B)],
 'notifications/notifications.html': [(N_ACT_A, N_ACT_B), (N_ST_A, N_ST_B), (N_H_A, N_H_B)],
 'help/live-pages/notifications.html': [(N_ACT_A, N_ACT_B), (N_ST_A, N_ST_B), (N_H_A, N_H_B)],
}
for rel, reps in JOBS.items():
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        continue
    s = open(p, encoding='utf8').read()
    if 'tc-noshow' in s:
        continue
    for a, b in reps:
        assert s.count(a) == 1, (rel, a[:50], s.count(a))
        s = s.replace(a, b)
    s = add_dict(s)
    open(p, 'w', encoding='utf8').write(s); print(rel, 'no-show')

# source dictionaries for rebuilds
dh = os.path.join(ROOT, 'help/dict-help.txt'); de = os.path.join(ROOT, 'i18n/dict-el.txt')
h = open(dh, encoding='utf8').read(); e = open(de, encoding='utf8').read()
for k, (it, es, el) in T.items():
    if '\n' + k + '|' not in '\n' + h:
        h = h.rstrip('\n') + '\n' + f'{k}|{it}|{es}\n'
    if '\n' + k + '|' not in '\n' + e:
        e = e.rstrip('\n') + '\n' + f'{k}|{el}\n'
open(dh, 'w', encoding='utf8').write(h); open(de, 'w', encoding='utf8').write(e)
