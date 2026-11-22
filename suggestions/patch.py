"""Create a table form: the idea chips under "What do you want to discuss?"
are labelled "Suggestions" instead of "From your k▪universe" (Karim 2026-11-22).
Usage: python3 suggestions/patch.py <page.html> ...  (idempotent)"""
import sys
OLD='<span class="sl">From your <b class="kb">k▪universe</b></span>'
NEW='<span class="sl">Suggestions</span>'
KEY='"From your":["Dal tuo","De tu","Από το"]'
ADD=KEY+',"Suggestions":["Suggerimenti","Sugerencias","Προτάσεις"]'
for f in sys.argv[1:]:
    s=open(f,encoding="utf-8").read(); o=s
    s=s.replace(OLD,NEW)
    if '"Suggestions":[' not in s: s=s.replace(KEY,ADD,1)
    if s!=o: open(f,"w",encoding="utf-8").write(s); print("patched",f)
    else: print("unchanged",f)
