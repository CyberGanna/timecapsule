#!/usr/bin/env python3
"""Tables page: the cycling "Smaller cards / Show as list / Bigger cards" link becomes a two-box
switch "Cards | List" (Karim 2026-11-22), boxes like the day filter (view switch rule).
Idempotent: re-run after rebuilding help/live-pages/agenda.html."""
import sys
P=sys.argv[1] if len(sys.argv)>1 else "help/live-pages/agenda.html"
s=open(P,encoding="utf-8").read()
a=s.index("function vlink(){");b=s.index("\nfunction render(){",a)
NEW='''function vlink(){ /* view-switch */
  const L=S.view==="list", ic=k=>`<svg viewBox="0 0 16 16" aria-hidden="true">${VI[k]}</svg>`;
  return `<div class="vsw" role="group" aria-label="View"><button class="vbox" data-v="cards" aria-pressed="${!L}">${ic("grid")}<span>Cards</span></button><button class="vbox" data-v="list" aria-pressed="${L}">${ic("list")}<span>List</span></button></div>`}'''
s=s[:a]+NEW+s[b:]
H='if(b.dataset&&b.dataset.v&&b.closest(".vsw")){S.view=b.dataset.v==="list"?"list":(MOB()?"land":"cards");try{localStorage.setItem("tc-agenda-view",S.view)}catch(e){}render();return}\n  '
if 'b.closest(".vsw")' not in s:
    s=s.replace('  if(b.id==="vcyc"){',"  "+H+'if(b.id==="vcyc"){',1)
CSS='''<style id="view-switch">
.vsw{margin-left:auto;align-self:center;display:inline-flex;align-items:center;gap:2px;flex:none}
.vbox{min-height:34px;padding:0 8px;border:0;background:none;color:var(--mute);font:inherit;font-size:14px;font-weight:500;display:inline-flex;align-items:center;gap:7px;cursor:pointer;white-space:nowrap}
.vbox+.vbox{border-left:1px solid var(--line);border-radius:0;min-height:16px;margin-left:2px;padding-left:10px}
.vbox svg{width:15px;height:15px;fill:currentColor}
.vbox[aria-pressed=true]{color:var(--fg);cursor:default}
@media (hover:hover){.vbox[aria-pressed=false]:hover{color:var(--fg)}}
.vbox:focus-visible{outline:2px solid var(--teal,#17C3C8);outline-offset:2px;border-radius:6px}
@media (max-width:640px){.sh:has(.vsw){flex-wrap:nowrap;align-items:center;gap:10px}.sh:has(.vsw) h2,.sh:has(.vsw)>span{white-space:nowrap}.sh:has(.vsw)>span{font-size:13px}.vbox span{display:none}.vbox{padding:0 7px;min-height:36px}.vbox+.vbox{min-height:16px;padding-left:9px}.vbox svg{width:17px;height:17px}.vsw{margin-right:-7px}}
@media (max-width:380px){.sh:has(.vsw){gap:6px}.sh:has(.vsw) h2{font-size:19px!important}.sh:has(.vsw)>span{font-size:12px}}
</style>'''
import re
s=re.sub(r'<style id="view-switch">.*?</style>','',s,flags=re.S)
i=s.rfind("</body>");s=s[:i]+CSS+s[i:]
DS='<script id="view-switch-i18n">(function(){var D=window.TCI18N_DICT;if(!D)return;D["Cards"]=D["Cards"]||["Schede","Tarjetas","Κάρτες"];D["List"]=D["List"]||["Elenco","Lista","Λίστα"];D["View"]=D["View"]||["Vista","Vista","Προβολή"]})();</script>'
s=re.sub(r'<script id="view-switch-i18n">.*?</script>','',s,flags=re.S)
j=s.index('<script id="tc-i18n">');j=s.index('</script>',j)+9;s=s[:j]+DS+s[j:]
open(P,"w",encoding="utf-8").write(s);print("ok")
