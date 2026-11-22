"""Remove the k▪universe name from the product UI (Karim 2026-11-22: "change all.
Knowledge orbits say my universe"). Idempotent.
Usage: python3 no-kuniverse/patch.py <file.html> ..."""
import sys
R=[
 ('<span class="wmt" aria-hidden="true">powered by k▪universe</span>',''),
 ('<span aria-hidden="true">powered by k▪universe</span>',''),
 ('aria-label="What is k-universe?"','aria-label="What is my universe?"'),
 ('aria-label="About k-universe"','aria-label="About my universe"'),
 ('<b class="kb-r">k▪universe</b>','<b class="kb-r">My universe</b>'),
 ('<b>k▪universe</b><p>Turns','<b>My universe</b><p>Turns'),
 ('<a href="https://k-universe.com/" target="_blank" rel="noopener">Learn more →</a>',''),
 ('  <span class="wm">k▪universe</span>\n',''),
 ('\n    <small class="pw">Knowledge orbits are powered by k▪universe.</small>',''),
 ('<small class="pw">Knowledge orbits are powered by k▪universe.</small>',''),
 ('<p class="ey">Knowledge orbits</p>','<p class="ey">My universe</p>'),
 ('Adding it to my k-universe now 📚','Adding it to my universe now 📚'),
 ("books in the user's k-universe","books in the user's universe"),
 ('"About k-universe");','"About my universe");'),
 ('"What is k-universe?");','"What is my universe?");'),
]
KEY='"My universe":["Il mio universo","Mi universo","Το σύμπαν μου"]'
ADD=(',"What is my universe?":["Cos\'è il mio universo?","¿Qué es mi universo?","Τι είναι το σύμπαν μου;"]'
     ',"About my universe":["Il mio universo","Sobre mi universo","Σχετικά με το σύμπαν μου"]')
for f in sys.argv[1:]:
    s=open(f,encoding="utf-8").read(); o=s
    for a,b in R: s=s.replace(a,b)
    if 'is my universe?"' in s and '"What is my universe?":[' not in s and KEY in s:
        s=s.replace(KEY,KEY+ADD,1)
    if s!=o: open(f,"w",encoding="utf-8").write(s); print("patched",f)
