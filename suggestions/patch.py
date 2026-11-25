"""Create a table form: the idea chips under "What do you want to discuss?"
and the alias picker chips are labelled "Suggestions" instead of
"From your k▪universe" / "Ideas from your k▪universe" (Gabriele 2026-11-22).
Usage: python3 suggestions/patch.py <page.html> ...  (idempotent)"""
import sys
OLD='<span class="sl">From your <b class="kb">k▪universe</b></span>'
NEW='<span class="sl">Suggestions</span>'
KEY='"From your":["Dal tuo","De tu","Από το"]'
ADD=KEY+',"Suggestions":["Suggerimenti","Sugerencias","Προτάσεις"]'
# Alias picker (join/rejoin a table): same label (Gabriele 2026-11-22)
OLD2='<span class="kfrom">Ideas from your <b>k▪universe</b></span>'
NEW2='<span class="kfrom">Suggestions</span>'
KEY2='"Ideas from your":["Idee dal tuo","Ideas de tu","Ιδέες από το"]'
for f in sys.argv[1:]:
    s=open(f,encoding="utf-8").read(); o=s
    s=s.replace(OLD,NEW).replace(OLD2,NEW2)
    if '"Suggestions":[' not in s and s!=o:
        s=s.replace(KEY,ADD,1) if KEY in s else s.replace(KEY2,KEY2+ADD[len(KEY):],1)
    if s!=o: open(f,"w",encoding="utf-8").write(s); print("patched",f)
    else: print("unchanged",f)
