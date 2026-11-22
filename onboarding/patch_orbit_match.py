# Book and film sit on the orbit of their own topic. If none of the chosen topics fits,
# a new orbit is added for the item's topic. Run after patch_orbits.py (safe to run twice).
import os
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'timecapsule-onboarding.html')
s = open(F, encoding='utf8').read()
if 'ORBIT-MATCH' in s:
    print('already patched'); raise SystemExit
R = [
 (' const orb=(n)=>70+n*28;\n', ''),
 (' const rings=neb.length?neb.map(t=>TOPICS[t]):((S.book||S.film)?["#A9B0D6"]:[]);\n rings.forEach((c,n)=>{s+=ring(orb(n),c,n)});\n',
  ''' /* ORBIT-MATCH: each pick sits on its own topic's orbit; a missing topic gets a new orbit */
 const rt=neb.slice();
 const place=it=>{if(!it)return -1;const tp=it.tp||[];let k=rt.findIndex(t=>tp.includes(t));if(k<0&&tp.length&&TOPICS[tp[0]]){rt.push(tp[0]);k=rt.length-1}if(k<0){if(!rt.length)rt.push("");k=0}return k};
 const bo=place(S.book),fo=place(S.film);
 const rings=rt.map(t=>TOPICS[t]||"#A9B0D6");
 const stp=rings.length>4?Math.floor(100/(rings.length-1)):28;
 const orb=(n)=>70+n*stp;
 rings.forEach((c,n)=>{s+=ring(orb(n),c,n)});
'''),
 (' if(S.book)s+=star(S.book,Math.PI,0,rings[0]||"#A9B0D6","Book");\n if(S.film)s+=star(S.film,0,rings.length>1?1:0,rings[rings.length>1?1:0]||"#A9B0D6","Film");\n',
  ' if(S.book)s+=star(S.book,Math.PI,bo,rings[bo],"Book");\n if(S.film)s+=star(S.film,0,fo,rings[fo],"Film");\n'),
]
R.append(('lbl=it.t.length>18?it.t.slice(0,17)+"…":it.t,right=x>200;','lbl=it.t.length>18?it.t.slice(0,17)+"…":it.t,right=x>200?x<300:x<100;'))
for a, b in R:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
open(F, 'w', encoding='utf8').write(s)
print('patched')
