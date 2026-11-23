#!/usr/bin/env python3
"""Tables page: the cycling "Smaller cards / Show as list / Bigger cards" link becomes a two-box
switch "Cards | List" (Karim 2026-11-22), boxes like the day filter (view switch rule).
Idempotent: re-run after rebuilding help/live-pages/agenda.html."""
import sys
P=sys.argv[1] if len(sys.argv)>1 else "help/live-pages/agenda.html"
s=open(P,encoding="utf-8").read()
a=s.index("function vlink(){");b=s.index("\nfunction render(){",a)
NEW='''function vlink(){ /* view-switch: one link that shows the other view */
  const L=S.view==="list", to=L?"cards":"list", t=L?"Cards":"List";
  return `<span class="vsw"><button class="vcyc" data-v="${to}" title="${t}" aria-label="${t}"><svg viewBox="0 0 16 16" aria-hidden="true">${VI[L?"grid":"list"]}</svg><span class="vt">${t}</span></button></span>`}'''
s=s[:a]+NEW+s[b:]
H='if(b.dataset&&b.dataset.v&&b.closest(".vsw")){S.view=b.dataset.v==="list"?"list":(MOB()?"land":"cards");try{localStorage.setItem("tc-agenda-view",S.view)}catch(e){}render();return}\n  '
if 'b.closest(".vsw")' not in s:
    s=s.replace('  if(b.id==="vcyc"){',"  "+H+'if(b.id==="vcyc"){',1)
CSS='''<style id="view-switch">.vsw{margin-left:auto;align-self:center;display:inline-flex}.vsw .vcyc{margin-left:0}</style>'''
import re
s=re.sub(r'<style id="view-switch">.*?</style>','',s,flags=re.S)
i=s.rfind("</body>");s=s[:i]+CSS+s[i:]
DS='<script id="view-switch-i18n">(function(){var D=window.TCI18N_DICT;if(!D)return;D["Cards"]=D["Cards"]||["Schede","Tarjetas","Κάρτες"];D["List"]=D["List"]||["Elenco","Lista","Λίστα"];D["View"]=D["View"]||["Vista","Vista","Προβολή"]})();</script>'
s=re.sub(r'<script id="view-switch-i18n">.*?</script>','',s,flags=re.S)
j=s.index('<script id="tc-i18n">');j=s.index('</script>',j)+9;s=s[:j]+DS+s[j:]
open(P,"w",encoding="utf-8").write(s);print("ok")
