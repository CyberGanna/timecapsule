"""Rating window = 7 days after the table ends (Karim 2026-11-19). Updates the old 3-day / "few days" /
"24 hours after" wording in every page, dict and source, with IT/ES/EL. Idempotent."""
import os,sys
R=[
("Any you don't award within 3 days expire.","Any you don't award within 7 days expire."),
("Any you don&#x27;t award within 3 days expire.","Any you don&#x27;t award within 7 days expire."),
("Quelli non assegnati entro 3 giorni scadono.","Quelli non assegnati entro 7 giorni scadono."),
("Los que no des en 3 días caducan.","Los que no des en 7 días caducan."),
("Όσα δεν δώσεις μέσα σε 3 ημέρες λήγουν.","Όσα δεν δώσεις μέσα σε 7 ημέρες λήγουν."),
("Unawarded coins expire after 3 days.","Unawarded coins expire after 7 days."),
("scadono dopo 3 giorni.","scadono dopo 7 giorni."),
("caducan a los 3 días.","caducan a los 7 días."),
("λήγουν μετά από 3 ημέρες.","λήγουν μετά από 7 ημέρες."),
(" · expire in 3 days"," · expire in 7 days"),
("24 hours after a table ends, if you haven't rated it yet, with when your TimeCoins expire.","The day before rating closes, if you haven't rated the table yet, with when your TimeCoins expire."),
("24 hours after a table ends, if you haven&#x27;t rated it yet, with when your TimeCoins expire.","The day before rating closes, if you haven&#x27;t rated the table yet, with when your TimeCoins expire."),
("24 ore dopo la fine di un tavolo, se non l'hai ancora votato, con la scadenza dei tuoi TimeCoins.","Il giorno prima che le valutazioni si chiudano, se non hai ancora votato il tavolo, con la scadenza dei tuoi TimeCoins."),
("24 horas después de que termine una mesa, si aún no la has valorado, con cuándo caducan tus TimeCoins.","El día antes de que se cierren las valoraciones, si aún no has valorado la mesa, con cuándo caducan tus TimeCoins."),
("24 ώρες μετά το τέλος ενός τραπεζιού, αν δεν το έχεις βαθμολογήσει ακόμα, με το πότε λήγουν τα TimeCoins σου.","Την παραμονή του κλεισίματος της βαθμολόγησης, αν δεν έχεις βαθμολογήσει ακόμα το τραπέζι, με το πότε λήγουν τα TimeCoins σου."),
("The 8 coins you get to award after a table expire after a few days if you don't award them.","The 8 coins you get to award after a table expire 7 days after it ends if you don't award them."),
("The 8 coins you get to award after a table expire after a few days if you don&#x27;t award them.","The 8 coins you get to award after a table expire 7 days after it ends if you don&#x27;t award them."),
("Le 8 monete da assegnare dopo un tavolo scadono dopo qualche giorno se non le assegni.","Le 8 monete da assegnare dopo un tavolo scadono 7 giorni dopo la fine se non le assegni."),
("Las 8 monedas para dar después de una mesa caducan a los pocos días si no las das.","Las 8 monedas para dar después de una mesa caducan 7 días después de que termine si no las das."),
("Τα 8 νομίσματα που παίρνεις για να δώσεις μετά από ένα τραπέζι λήγουν μετά από λίγες ημέρες αν δεν τα δώσεις.","Τα 8 νομίσματα που παίρνεις για να δώσεις μετά από ένα τραπέζι λήγουν 7 ημέρες μετά το τέλος του αν δεν τα δώσεις."),
("If you leave in a hurry, the bell reminds you the next day.","If you sat for at least 10 minutes, you can rate even if you left early. You have 7 days, and the bell reminds you the day before rating closes."),
("Se esci di fretta, la campanella te lo ricorda il giorno dopo.","Se sei rimasto almeno 10 minuti, puoi votare anche se sei uscito prima. Hai 7 giorni, e la campanella te lo ricorda il giorno prima della chiusura."),
("Si sales con prisa, la campana te lo recuerda al día siguiente.","Si estuviste al menos 10 minutos, puedes valorar aunque te hayas ido antes. Tienes 7 días, y la campana te lo recuerda el día antes del cierre."),
("Αν φύγεις βιαστικά, το κουδουνάκι σού το θυμίζει την επόμενη μέρα.","Αν έμεινες τουλάχιστον 10 λεπτά, μπορείς να βαθμολογήσεις ακόμα κι αν έφυγες νωρίτερα. Έχεις 7 ημέρες, και το κουδουνάκι σού το θυμίζει την παραμονή του κλεισίματος."),
("Your 8 TimeCoins expire in 2 days.","Last day to rate. Your 8 TimeCoins expire tomorrow."),
("I tuoi 8 TimeCoins scadono tra 2 giorni.","Ultimo giorno per votare. I tuoi 8 TimeCoins scadono domani."),
("Tus 8 TimeCoins caducan en 2 días.","Último día para valorar. Tus 8 TimeCoins caducan mañana."),
("Τα 8 TimeCoins σου λήγουν σε 2 ημέρες.","Τελευταία μέρα για βαθμολόγηση. Τα 8 TimeCoins σου λήγουν αύριο."),
]
n=0
for root,ds,fs in os.walk('.'):
    if '.git' in root or 'node_modules' in root: continue
    for f in fs:
        if not f.endswith(('.html','.txt','.py','.json','.md','.js')) or f=='replace_text.py': continue
        p=os.path.join(root,f)
        try: s=open(p,encoding='utf8').read()
        except Exception: continue
        o=s
        for a,b in R: s=s.replace(a,b)
        if s!=o: open(p,'w',encoding='utf8').write(s); n+=1; print(p)
print(n,"files")
