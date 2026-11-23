"""Chair limits on the Tables page (Karim approved 2026-11-22):
1. No overlaps: saving a chair at a table that clashes with one you already saved shows
   "You're at another table then" with Keep my chair / Swap tables.
2. Up to 5 saved chairs at a time (upcoming tables you're a guest at; tables you host don't count).
Idempotent, marker "tc-climit". Run after seat-ok/patch.py."""
import os, json, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']

OLD = 'if(!on){t.live?openJoin(t):openSheet(t);return}'
NEW = 'if(!on){t.live?openJoin(t):(chairGuard(t)||openSheet(t));return}'

JS = r'''<script id="tc-climit">
/* tc-climit: no overlapping chairs, at most 5 saved chairs at a time */
const CHAIR_MAX=5;
function chairGuard(t){
  const mine=T.filter(x=>S.joined.has(x.id)&&!x.live&&!x.mine&&x.id!==t.id);
  const clash=mine.find(x=>Math.abs(x.when-t.when)<60);
  const sh=document.getElementById("sheet"), sc=document.getElementById("scrim");
  const show=html=>{cur=t;lastFocus=document.activeElement;sh.classList.remove("join");sh.innerHTML=`<button class="x" data-close aria-label="Close">×</button><div class="climit">${html}</div>`;sc.hidden=false;requestAnimationFrame(()=>sc.classList.add("on"));};
  if(clash){
    show(`<h2 id="sh-t">You're at another table then</h2>
      <p>You saved a chair at <b>${esc(clash.title)}</b>, ${longWhen(clash.when)}.</p><p class="cl2">You can sit at one table at a time.</p>
      <div class="acts"><button class="cta" data-close>Keep my chair</button><button class="cta go" id="swapT">Swap tables</button></div>`);
    document.getElementById("swapT").onclick=()=>{S.joined.delete(clash.id);render();openSheet(t);toast("Your chair at the other table is free again")};
    return true;
  }
  if(mine.length>=CHAIR_MAX){
    show(`<h2 id="sh-t">You have ${CHAIR_MAX} saved chairs</h2>
      <p>You can save up to ${CHAIR_MAX} chairs at a time, so others get a seat too. Give one back in My tables, or save this one after one of your tables ends.</p>
      <div class="acts"><a class="cta" href="mytables.html" target="_top">Open My tables</a><button class="cta go" data-close>OK</button></div>`);
    return true;
  }
  return false;
}
</script>'''
CSS = '''<style id="tc-climit-css">
.climit h2{font-size:22px;margin:4px 40px 10px 0}
.climit p{color:var(--mute,#A9B0D6);line-height:1.55;margin:0}
.climit .cl2{margin-top:8px}
.climit p b{color:var(--text,#EEF1FF);font-weight:500}
.climit .acts .cta{flex:1;display:flex;align-items:center;justify-content:center;text-decoration:none}
</style>'''
T = {
 "You're at another table then": ["Sei già a un altro tavolo a quell'ora", "Ya estás en otra mesa a esa hora", "Είσαι ήδη σε άλλο τραπέζι εκείνη την ώρα"],
 "You can sit at one table at a time.": ["Puoi sederti a un tavolo alla volta.", "Puedes sentarte en una mesa a la vez.", "Μπορείς να κάθεσαι σε ένα τραπέζι τη φορά."],
 "You saved a chair at": ["Hai tenuto un posto a", "Guardaste un sitio en", "Κράτησες καρέκλα στο"],
 "Keep my chair": ["Tengo il mio posto", "Mantener mi sitio", "Κρατάω την καρέκλα μου"],
 "Swap tables": ["Cambia tavolo", "Cambiar de mesa", "Άλλαξε τραπέζι"],
 "Your chair at the other table is free again": ["Il tuo posto all'altro tavolo è di nuovo libero", "Tu sitio en la otra mesa vuelve a estar libre", "Η καρέκλα σου στο άλλο τραπέζι είναι πάλι ελεύθερη"],
 "You have 5 saved chairs": ["Hai 5 posti tenuti", "Tienes 5 sitios guardados", "Έχεις 5 κρατημένες καρέκλες"],
 "You can save up to 5 chairs at a time, so others get a seat too. Give one back in My tables, or save this one after one of your tables ends.": [
   "Puoi tenere fino a 5 posti alla volta, così c'è posto anche per gli altri. Liberane uno in I miei tavoli, oppure tieni questo quando uno dei tuoi tavoli è finito.",
   "Puedes guardar hasta 5 sitios a la vez, para que otros también tengan sitio. Libera uno en Mis mesas, o guarda este cuando termine una de tus mesas.",
   "Μπορείς να κρατάς έως 5 καρέκλες τη φορά, για να βρίσκουν θέση και οι άλλοι. Άφησε μία στα Τραπέζια μου ή κράτα αυτή όταν τελειώσει ένα από τα τραπέζια σου."],
 "Open My tables": ["Apri I miei tavoli", "Abrir Mis mesas", "Άνοιξε τα Τραπέζια μου"],
}
def add_dict(s):
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, flags=re.S)
    if not m:
        return s
    d = json.loads(m.group(1)); d.update(T)
    return s[:m.start(1)] + json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + s[m.end(1):]

for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-climit' in s:
        continue
    assert s.count(OLD) == 1, rel
    s = s.replace(OLD, NEW)
    i = s.rindex('</body>'); s = s[:i] + JS + CSS + s[i:]
    s = add_dict(s)
    open(p, 'w', encoding='utf8').write(s); print(rel, 'chair limits')

# FAQ + Guides (marker "tc-climit-help")
T2 = {
 "How many chairs can I save?": ["Quanti posti posso tenere?", "¿Cuántos sitios puedo guardar?", "Πόσες καρέκλες μπορώ να κρατήσω;"],
 "One chair per table, at up to 5 upcoming tables at a time, and never at two tables that overlap. Tables you host don't count.": [
   "Un posto per tavolo, fino a 5 tavoli in arrivo alla volta, e mai a due tavoli che si sovrappongono. I tavoli che ospiti non contano.",
   "Un sitio por mesa, en hasta 5 mesas próximas a la vez, y nunca en dos mesas que se solapen. Las mesas que organizas no cuentan.",
   "Μία καρέκλα ανά τραπέζι, σε έως 5 επερχόμενα τραπέζια τη φορά, και ποτέ σε δύο τραπέζια που συμπίπτουν. Τα τραπέζια που φιλοξενείς δεν μετράνε."],
 "You can save chairs at up to 5 tables at a time, as long as they don't overlap.": [
   "Puoi tenere posti fino a 5 tavoli alla volta, purché non si sovrappongano.",
   "Puedes guardar sitios en hasta 5 mesas a la vez, siempre que no se solapen.",
   "Μπορείς να κρατάς καρέκλες σε έως 5 τραπέζια τη φορά, αρκεί να μη συμπίπτουν."],
}
T.update(T2)
FQ_A = "<details><summary><span>What if I can't make it?</span>"
FQ_B = ("<details><summary><span>How many chairs can I save?</span><svg><use href=\"#i-plus\"/></svg></summary>"
        "<p><!--tc-climit-help-->One chair per table, at up to 5 upcoming tables at a time, and never at two tables that overlap. Tables you host don't count.</p></details>\n " + FQ_A)
GD_A = "<p><!--tc-noshow-->"
GD_B = "<p><!--tc-climit-help-->You can save chairs at up to 5 tables at a time, as long as they don't overlap.</p>" + GD_A
for rel, (a, b) in {'help/timecapsule-faq.html': (FQ_A, FQ_B), 'help/faq-body.html': (FQ_A, FQ_B),
                    'help/timecapsule-guides.html': (GD_A, GD_B), 'help/guides-body.html': (GD_A, GD_B)}.items():
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-climit-help' in s:
        continue
    assert s.count(a) == 1, (rel, s.count(a))
    s = add_dict(s.replace(a, b))
    open(p, 'w', encoding='utf8').write(s); print(rel, 'help')
dh = os.path.join(ROOT, 'help/dict-help.txt'); de = os.path.join(ROOT, 'i18n/dict-el.txt')
h = open(dh, encoding='utf8').read(); e = open(de, encoding='utf8').read()
for k, (it, es, el) in T.items():
    if '\n' + k + '|' not in '\n' + h: h = h.rstrip('\n') + '\n' + f'{k}|{it}|{es}\n'
    if '\n' + k + '|' not in '\n' + e: e = e.rstrip('\n') + '\n' + f'{k}|{el}\n'
open(dh, 'w', encoding='utf8').write(h); open(de, 'w', encoding='utf8').write(e)
