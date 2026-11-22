# Onboarding universe in the same style as the profile universe (Profile Version 2):
# glowing photo at the centre, each chosen topic is a tilted dotted orbit, the book and the film are dots on them.
# Run: python3 onboarding/patch_orbits.py   (safe to run twice)
import os
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'timecapsule-onboarding.html')
s = open(F, encoding='utf8').read()
if 'ORBIT-STYLE' in s:
    print('already patched'); raise SystemExit
i = s.index(' neb.forEach((t,i)=>{const [ang,d]=SLOTS[i]')
j = s.index(' const u=$("#u");const prev=')
NEW = r''' /* ORBIT-STYLE: same look as the profile universe */
 const TILT=-14*Math.PI/180,ct=Math.cos(TILT),sn=Math.sin(TILT),K=.38;
 const orb=(n)=>70+n*28;
 const at=(rx,a)=>{const ex=Math.cos(a)*rx,ey=Math.sin(a)*rx*K;return [200+ex*ct-ey*sn,200+ex*sn+ey*ct]};
 const ring=(rx,col,n)=>`<g class="lay"><ellipse transform="rotate(-14 200 200)" cx="200" cy="200" rx="${rx}" ry="${(rx*K).toFixed(1)}" fill="none" stroke="${col}" stroke-opacity=".28" stroke-width=".6"/><ellipse transform="rotate(-14 200 200)" cx="200" cy="200" rx="${rx}" ry="${(rx*K).toFixed(1)}" fill="none" stroke="${col}" stroke-opacity=".7" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="0 ${(5.5+n*.4).toFixed(1)}"/></g>`;
 const rings=neb.length?neb.map(t=>TOPICS[t]):((S.book||S.film)?["#A9B0D6"]:[]);
 rings.forEach((c,n)=>{s+=ring(orb(n),c,n)});
 const hasMe=S.i>=1&&S.name.trim();
 if(!hasMe)s+=`<g class="here" fill="none" stroke="#EEF1FF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round" transform="translate(210,200) scale(0.0435) translate(-175,-690)"><path d="M700 250 L700 290 A400 400 0 0 1 300 690 L175 690"/><path d="M280 590 L175 690 L280 800"/></g><text x="233" y="174" text-anchor="middle" fill="#EEF1FF" font-size="11" font-style="italic">you're here</text>`;
 const star=(it,a,n,col,kind)=>{const [x,y]=at(orb(n),a),lbl=it.t.length>18?it.t.slice(0,17)+"…":it.t,right=x>200;
  return `<g class="lay"><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="5" fill="${col}"/><text x="${(x+(right?11:-11)).toFixed(1)}" y="${(y-7).toFixed(1)}" text-anchor="${right?"start":"end"}" fill="#EEF1FF" font-size="11.5" font-weight="500">${esc(lbl)}</text><text x="${(x+(right?11:-11)).toFixed(1)}" y="${(y+8).toFixed(1)}" text-anchor="${right?"start":"end"}" fill="#A9B0D6" font-size="9.5">${kind} · ${it.y}</text></g>`};
 if(S.book)s+=star(S.book,Math.PI,0,rings[0]||"#A9B0D6","Book");
 if(S.film)s+=star(S.film,0,rings.length>1?1:0,rings[rings.length>1?1:0]||"#A9B0D6","Film");
 if(hasMe){
  let rays="";for(let r=0;r<36;r++){const a=r/36*Math.PI*2,len=22+(r%3)*11;rays+=`<line x1="200" y1="200" x2="${(200+Math.cos(a)*len*1.6).toFixed(1)}" y2="${(200+Math.sin(a)*len*.75).toFixed(1)}" stroke="#F7C66B" stroke-opacity=".22" stroke-width=".6"/>`}
  s+=`<g class="lay"><defs><radialGradient id="sunG"><stop offset="0" stop-color="#FFF6D8"/><stop offset=".25" stop-color="#F7C66B" stop-opacity=".85"/><stop offset="1" stop-color="#F0A040" stop-opacity="0"/></radialGradient><radialGradient id="avG"><stop offset=".45" stop-color="#FFE7A8" stop-opacity=".9"/><stop offset="1" stop-color="#F0A040" stop-opacity="0"/></radialGradient></defs>${rays}<ellipse cx="200" cy="200" rx="40" ry="24" fill="url(#sunG)"/><circle cx="200" cy="200" r="33" fill="url(#avG)"/>${S.photo?`<circle cx="200" cy="200" r="17.5" fill="#1B2144"/><image href="${S.photo}" x="183" y="183" width="34" height="34" clip-path="url(#me)" preserveAspectRatio="xMidYMid slice"/>`:`<circle cx="200" cy="200" r="17" fill="#7C5CFF"/><text x="200" y="204.5" text-anchor="middle" fill="#fff" font-size="12" font-weight="500">${esc(initials())}</text>`}<circle cx="200" cy="200" r="17.5" fill="none" stroke="#FFE3A0" stroke-width="1.6"/></g>`;
 }else{
  s+=`<circle cx="200" cy="200" r="3.5" fill="#EEF1FF" opacity=".7"/>`;
 }
'''
s = s[:i] + NEW + s[j:]
for a, b in [('topics:["Your nebulae","Topics become the coloured clouds of your universe."]', 'topics:["Your orbits","Each topic becomes an orbit around you."]')]:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
open(F, 'w', encoding='utf8').write(s)
print('patched')
