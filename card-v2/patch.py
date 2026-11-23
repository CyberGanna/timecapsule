#!/usr/bin/env python3
"""New table card for the Tables page (cards + Smaller cards views).
Serif question, latest spoken line, hour thread, faces, chairs free, button lower right.
Optional photo header when the table has an image. Idempotent: re-run after rebuilding agenda.html."""
import re,sys
P=sys.argv[1] if len(sys.argv)>1 else "help/live-pages/agenda.html"
s=open(P,encoding="utf-8").read()

FN=r'''function liveCard(t){ /* card-v2 */
  const c=THEMES[t.theme], mine=S.joined.has(t.id), k=t.people.length+(mine?1:0), left=t.seats-k, soon=!t.live;
  const ppl=[...t.people]; if(mine) ppl.push("You");
  const faces=ppl.map(p=>`<span${p!=="You"?` data-u="${p}" tabindex="0"`:""}>${av(p)}</span>`).join("")+Array.from({length:Math.max(0,left)},()=>`<em aria-hidden="true"></em>`).join("");
  /* photo header (Karim 2026-11-22): the host's photo; tables without one get a sample photo as a stand-in for the topic photo */
  const hd=`<div class="cc-hd"><img src="${(t.img!=null?IMGS[t.img]:CCPOOL[(CCIMG[t.id]??t.id)%CCPOOL.length])}" alt="" loading="lazy"></div>`;
  const q=false; /* quotes removed (Karim 2026-11-22) */
  let when, btn;
  if(soon){const m=Math.max(1,Math.round((t.at-NOW)/60000));
    when=`<span class="cc-when">${m<=60?`Starts <span class="cdn" data-at="${+t.at}">in ${m} min</span> · ${hhmm(t.at)}`:`${dayName(dayKey(t.at))} · ${hhmm(t.at)}`}</span>`;
    btn=t.mine?`<button class="jbtn on" data-hosting>You're hosting</button>`:mine?`<button class="jbtn on" data-id="${t.id}">Chair saved</button>`:left>0?`<button class="jbtn" data-id="${t.id}">Save chair</button>`:`<button class="jbtn ghost" data-id="${t.id}">Join waitlist</button>`;
  }else{
    when=`<span class="cc-live">LIVE<span>${t.live} of 60 min</span></span>`;
    btn=t.mine?`<button class="jbtn on" data-hosting>You're hosting</button>`:mine?`<button class="jbtn on back" data-id="${t.id}">Go back in</button>`:left>0?`<button class="jbtn" data-id="${t.id}">Join table</button>`:`<button class="jbtn ghost" data-id="${t.id}">Listen in</button>`;
  }
  return `<article class="tbl cc${soon?" soon":""}""" data-cp="1" style="--c:${c}">${hd}<div class="cc-in">${soon?"":`<div class="cc-hour"><i style="width:${Math.min(100,t.live/60*100)}%"></i></div>`}
    <div class="cc-top"><span class="cc-topic"><i></i>${t.theme}</span>${when}</div>
    <h3><a class="tdl" href="${tdUrl(t)}" target="_top">${esc(t.title)}</a></h3>
    <div class="cc-host">with <b>${t.host}</b> · ${t.country}</div>
    ${q?`<blockquote>“${q}”<cite>${t.talk}, just now</cite></blockquote>`:""}
    <div class="cc-foot"><div class="cc-seatrow"><span class="cc-faces">${faces}</span><span class="cc-seats">${left>0?`${left} ${left===1?"chair":"chairs"} free`:soon?"Full · waitlist open":"Table full"}</span></div>${btn}</div></div></article>`;
}
const CCIMG={1:5,3:0,16:6,18:8}; /* stand-ins: index into CCPOOL = sample photos + Profile backdrops, spread so neighbours differ */
const CCQ={
 "Is free will an illusion?":"If my brain decides before I notice, who is the “I” that is responsible?",
 "Who owns the past? Museums and stolen objects":"A museum label is also a way of saying who the object belongs to.",
 "Green technology versus nuclear: what should power our future?":"The cleanest kilowatt is the one we never need.",
 "Do we still need to own a home?":"Renting taught me that home is a habit, not a deed.",
 "Home batteries: are they worth it yet?":"Mine paid for itself the winter the grid went down.",
 "What makes a good question?":"A good question leaves the room bigger than it found it."};
'''
a=s.index("function liveCard(t){"); b=s.index("\nfunction chairs(t){",a)
s=s[:a]+FN.rstrip("\n")+s[b:]
# Profile backdrops mixed with the sample photos (Karim 2026-11-22)
import os
PROF=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','profile','timecapsule-profile-v2.html')
ps=open(PROF,encoding='utf-8').read()
BD={m.group(1):m.group(2) for m in re.finditer(r'\.bd-([a-z]+)\{background:url\((data:image/[^)]+)\)',ps)}
POOL='const CCPOOL=[...IMGS,'+','.join('"%s"'%BD[k] for k in ['galaxy','sunset','alps','eclipse'])+'];'
s=re.sub(r'const CCPOOL=\[\.\.\.IMGS,[^\]]*\];\n?','',s)
s=s.replace('const CCIMG=',POOL+'\nconst CCIMG=',1)

CSS=r'''<style id="card-v2">
main .live article.tbl.cc{display:flex!important;flex-direction:column!important;height:auto!important;max-height:none!important;position:relative;padding:0!important;min-height:0!important;overflow:hidden;border:1px solid #323A6C!important;border-radius:20px!important;background:radial-gradient(120% 70% at 0% 0%,color-mix(in srgb,var(--c) 9%,transparent),transparent 60%),#20264A!important;box-shadow:0 1px 0 rgba(255,255,255,.04) inset,0 12px 30px rgba(5,8,25,.25)!important;transition:border-color .2s,transform .2s}
main .live article.tbl.cc:hover{border-color:color-mix(in srgb,var(--c) 45%,#323A6C)!important}
main .live .tbl.cc>.tbg{display:none!important}
/* border drawn on top so photos never bleed over it at the rounded corners */
main .live article.tbl.cc{border-color:transparent!important}
main .live article.tbl.cc::after{content:"";position:absolute;inset:0;border:1px solid #323A6C;border-radius:inherit;pointer-events:none;z-index:4}
main .live article.tbl.cc:hover::after{border-color:color-mix(in srgb,var(--c) 45%,#323A6C)}
.tbl.cc .cc-hd{border-radius:19px 19px 0 0}
.cc-hd{position:relative;flex:none;height:150px;overflow:hidden;background:#252B52}.cc-hd::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,25,54,0) 55%,rgba(32,38,74,.55))}
.cc-hd.plain{display:grid;place-items:center;background:linear-gradient(135deg,color-mix(in srgb,var(--c) 16%,#20264A),color-mix(in srgb,var(--c) 5%,#20264A))}
.cc-hd.plain svg{width:46px;height:46px;fill:none;stroke:color-mix(in srgb,var(--c) 70%,#EEF1FF);stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round;opacity:.75}
.cc-hd img{width:100%;height:100%;object-fit:cover;display:block}
.tbl.cc .cc-in{position:relative;display:flex;flex-direction:column;flex:1 1 auto;min-height:0;padding:22px 22px 20px}
.cc-hour{position:absolute;left:0;right:0;top:0;height:3px;background:rgba(238,241,255,.06)}
.cc-hour i{display:block;height:100%;background:#3DDC84;border-radius:0 3px 3px 0}
.cc-top{display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:13px;color:#C9CFF0}
.cc-topic{display:flex;align-items:center;gap:8px;min-width:0}.cc-topic i{width:8px;height:8px;border-radius:50%;background:var(--c);flex:none}
.cc-live{font-size:12px;font-weight:600;letter-spacing:.14em;color:#3DDC84;white-space:nowrap}
.cc-live span{color:#A9B0D6;font-weight:400;letter-spacing:0;margin-left:6px}
.cc-when{font-size:12.5px;color:#A9B0D6;white-space:nowrap}
main .live .tbl.cc .cc-hour{border-radius:20px 20px 0 0}main .live .tbl.cc h3{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;font-family:Literata,Georgia,serif!important;font-weight:500!important;font-size:23px!important;line-height:1.28!important;padding-bottom:.12em!important;margin:16px 0 4px!important;letter-spacing:-.005em;color:#EEF1FF}
.cc-host{font-size:13.5px;color:#A9B0D6}.cc-host b{color:#C9CFF0;font-weight:500}
.tbl.cc blockquote{display:block;margin:18px 0 0;padding:2px 0 2px 14px;border-left:2px solid var(--c);font-family:Literata,Georgia,serif;font-style:italic;font-size:15.5px;line-height:1.45;color:#C9CFF0}
.tbl.cc blockquote cite{display:block;margin-top:6px;font-family:Sora,sans-serif;font-style:normal;font-size:12px;color:#A9B0D6}
.cc-foot{margin-top:auto;padding-top:22px;display:flex;flex-direction:column;gap:14px}
.cc-seatrow{display:flex;flex-direction:column;align-items:stretch;gap:10px;min-width:0}
.cc-faces{display:flex;justify-content:space-between;gap:5px;width:100%;min-width:0;flex:none}.cc-faces>span,.cc-faces>em{flex:0 1 40px;min-width:0;aspect-ratio:1;border-radius:50%;overflow:hidden;display:block}
.cc-faces svg,.cc-faces img{width:100%;height:100%;display:block}
.cc-faces>em{box-sizing:border-box;border:1.5px dashed rgba(238,241,255,.28)}
.cc-seats{font-size:13px;color:#A9B0D6;white-space:nowrap;flex:none;text-align:center}
main .live .tbl.cc .cc-foot .jbtn{width:100%!important;margin:0!important;height:42px!important;padding:0 18px!important;border-radius:10px!important;justify-content:center}
main .live .tbl.cc .cc-foot .jbtn.back{background:transparent!important;color:#F2C14E!important;box-shadow:inset 0 0 0 1.5px #17C3C8!important;border:0!important}
/* List view: the question in the same serif as the cards (Karim 2026-11-22) */
.agenda .ev .et h3{font-family:Literata,Georgia,serif!important;font-weight:500!important;font-size:19px!important;line-height:1.25!important;letter-spacing:-.005em}
@media (max-width:640px){.agenda .ev .et h3{font-size:17px!important}}
@media (max-width:640px){.tbl.cc .cc-in{padding:18px 18px 16px}main .live .tbl.cc h3{font-size:20px!important;margin-top:12px!important}.tbl.cc blockquote{font-size:14.5px;margin-top:14px}.cc-foot{padding-top:18px}.cc-faces{gap:5px}.cc-hd{height:128px}}
</style>'''
s=re.sub(r'<style id="card-v2">.*?</style>','',s,flags=re.S)
i=s.rfind("</body>"); s=s[:i]+CSS+s[i:] if i>=0 else s+CSS
if "family=Literata" not in s:
    s=s.replace('family=Sora:wght@300;400;500;600&display=swap','family=Sora:wght@300;400;500;600&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap',1)
open(P,"w",encoding="utf-8").write(s)
print("ok",P)
