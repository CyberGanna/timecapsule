"""Conversations page intro copy (Karim 2026-11-19). Idempotent text swap in page, body and dicts."""
R=[("Conversations saved at the end of their tables, sorted by topic. Read what was said, then ask the host to join the next round.",
    "Conversations are what a table leaves behind, saved when it ends and sorted by topic. Read what was said, then ask the host for a chair at the next round, and help write what comes next."),
   ("Conversazioni salvate alla fine dei loro tavoli, divise per argomento. Leggi cosa si è detto, poi chiedi all'host di unirti al prossimo giro.",
    "Le conversazioni sono ciò che un tavolo lascia dietro di sé, salvate alla fine e divise per argomento. Leggi cosa si è detto, poi chiedi all'host una sedia al prossimo giro, e aiuta a scrivere ciò che viene dopo."),
   ("Conversaciones guardadas al final de sus mesas, ordenadas por tema. Lee lo que se dijo y pide al anfitrión unirte a la próxima ronda.",
    "Las conversaciones son lo que una mesa deja tras de sí, guardadas al terminar y ordenadas por tema. Lee lo que se dijo, pide al anfitrión una silla en la próxima ronda y ayuda a escribir lo que viene."),
   ("Συζητήσεις που αποθηκεύτηκαν στο τέλος των τραπεζιών τους, ανά θέμα. Διάβασε τι ειπώθηκε και ζήτα από τον οικοδεσπότη να μπεις στον επόμενο γύρο.",
    "Οι συζητήσεις είναι ό,τι αφήνει πίσω του ένα τραπέζι, αποθηκευμένες όταν τελειώνει και ταξινομημένες ανά θέμα. Διάβασε τι ειπώθηκε, ζήτα από τον οικοδεσπότη μια καρέκλα στον επόμενο γύρο και βοήθησε να γραφτεί η συνέχεια.")]
for f in ["library/dict-disc-el.txt","library/dict-disc.txt","library/disc-body.html","help/live-pages/discussions.html","i18n/dict-el.txt"]:
    s=open(f).read(); o=s
    for a,b in R: s=s.replace(a,b)
    if s!=o: open(f,'w').write(s); print('patched',f)
