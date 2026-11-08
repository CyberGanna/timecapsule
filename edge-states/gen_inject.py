import re
s=open('body.html').read()
css=s[s.index('<style>')+7:s.index('</style>')]
js=s[s.index('<script>')+8:s.rindex('</script>')]
KEEP={'tch-d','tch-n','tch-nav'}
# ---- CSS
css=re.sub(r'^\.proto.*\n','',css,flags=re.M)
css=re.sub(r'^body\.newu.*\n','',css,flags=re.M)
css=css.replace(' .proto .wrap{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none}.proto .wrap::-webkit-scrollbar{display:none}.proto .gl,.proto .pg{flex-wrap:nowrap;flex:none}','')
css=re.sub(r'\.([a-zA-Z][\w-]*)',lambda m:m.group(0) if m.group(1) in KEEP else '.e-'+m.group(1),css)
css=re.sub(r'#(toast|scrim|sh-[a-z])\b',r'#e-\1',css)
css=re.sub(r'\bh1\b','.e-h1',css)  # page h1 rules leak; use class
css=re.sub(r'var\(--([\w-]+)\)',r'var(--e-\1)',css)
css=css.replace('.e-wrap{max-width:1040px;margin:0 auto;','.e-wrap{max-width:1040px;margin:0 auto;box-sizing:border-box;')
VARS='--e-bg:#1B2144;--e-surface:#20264A;--e-raise:#252B52;--e-line:#3A4175;--e-fg:#EEF1FF;--e-mute:#A9B0D6;--e-soft:#C9CFF0;--e-lamp:#17C3C8;--e-lamp-ink:#0E1430;--e-violet:#7C5CFF;--e-gold:#F2C14E;--e-live:#3DDC84'
base='#tce,#e-scrim,#e-toast{%s;font-family:"Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--e-fg);line-height:1.4}\n:where(#tce,#e-scrim) *{box-sizing:border-box}\n#tce{background:var(--e-bg);padding-bottom:20px;min-height:calc(100vh - 64px)}\n:where(#tce) .e-h1{font-weight:400;font-size:clamp(32px,4.6vw,46px);line-height:1.05;letter-spacing:-.04em;margin:0;color:var(--e-fg)}\n:where(#tce) a{color:inherit}\n:where(#tce) .e-lnk,:where(#tce) .e-ps .e-em a{color:var(--e-lamp)}\n:where(#tce) button{font-family:inherit}\nbody.tce-newu .tch-n,body.tce-newu .tch-d{display:none!important}\n'%VARS
chip='''.e-chip{position:fixed;left:14px;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:70;display:flex;align-items:center;gap:8px;padding:5px 5px 5px 12px;border-radius:12px;background:#171C3B;border:1px solid #3A4175;box-shadow:0 8px 24px rgba(0,0,0,.35);font:12.5px "Sora",ui-sans-serif,system-ui,sans-serif;color:#A9B0D6}
.e-chip b{font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:10px;opacity:.85}
.e-chip .e-seg{display:inline-flex;gap:2px;padding:2px;border-radius:9px;background:#20264A;border:1px solid #3A4175}
.e-chip button{border:0;background:none;color:#A9B0D6;font:inherit;font-size:12.5px;padding:5px 10px;border-radius:7px;cursor:pointer;white-space:nowrap}
.e-chip button[aria-pressed=true]{background:#EEF1FF;color:#121633;font-weight:500}
'''
css=base+chip+css
# ---- JS
def cls(m):
  toks=m.group(1)
  out=re.sub(r'(?<![\w$-])([a-zA-Z][\w-]*)',lambda t:t.group(1) if t.group(1) in KEEP else 'e-'+t.group(1),toks)
  return 'class="'+out+'"'
# protect ${...} inside class attrs by handling simple class attrs only
js=re.sub(r'class="([a-zA-Z][\w -]*)"',cls,js)
js=re.sub(r'class="([a-zA-Z][\w-]*)\$\{',lambda m:'class="e-'+m.group(1)+'${',js)
for a,b in [("' ghost'","' e-ghost'"),("' host'","' e-host'"),("' off'","' e-off'"),("class=\"${c||'btn pri'}\"","class=\"${c||'e-btn e-pri'}\""),
 ("A(U.agenda,'See other tables','lnk')","A(U.agenda,'See other tables','e-lnk')"),("A(U.invite,'Invite a friend','lnk')","A(U.invite,'Invite a friend','e-lnk')"),
 ("A(U.settings+'#notifications','Choose what rings the bell','lnk')","A(U.settings+'#notifications','Choose what rings the bell','e-lnk')"),
 ("A(U.create,'Create a table','lnk')","A(U.create,'Create a table','e-lnk')"),
 ("classList.toggle('ok')","classList.toggle('e-ok')"),("classList.toggle('pri',","classList.toggle('e-pri',"),("classList.contains('ok')","classList.contains('e-ok')"),("classList.toggle('ok',on)","classList.toggle('e-ok',on)"),
 ("<h1>","<h1 class=\"e-h1\">"),('<h1 class="dim">','<h1 class="e-h1 e-dim">'),
 ("'#days .tb'","'#e-days .e-tb'"),("closest('#days .tb')","closest('#e-days .e-tb')"),
 ]:
  js=js.replace(a,b)
js=re.sub(r'id="(wl|wlh|folh|mtb|mtt|days|sf)"',r'id="e-\1"',js)
js=re.sub(r"\$\('#(folh|mtb|toast|scrim|sh-[a-z])'\)",r"$('#e-\1')",js)
js=js.replace("e.target.id!=='sf'","e.target.id!=='e-sf'").replace("e.target.id==='scrim'","e.target.id==='e-scrim'")
js=js.replace("'.e-proto [data-s]'","'.proto [data-s]'")
# cut off original state machine (from 'const NAV' onward) and keep render parts
cut=js.index('const NAV=')
render=js[:cut]
rest=js[cut:]
# keep handlers block: from "let tt;" to before "show((location"
h0=rest.index('let tt;');h1=rest.index('show((location')
handlers=rest[h0:h1]
handlers=handlers.replace("document.querySelector('.proto').addEventListener('click',e=>{const b=e.target.closest('[data-s]');if(b)show(b.dataset.s)});\n","")
handlers=handlers.replace("$('#page')","$('#tce')")
render=render.replace("const $=s=>document.querySelector(s);","const $=s=>document.querySelector(s);")
mt="function mt(k){$('#e-mtb').innerHTML=solo(MT[k]);document.querySelectorAll('[data-mt]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.mt===k))}\n"
open('inject_parts.js','w').write(render+'\n'+mt+handlers)
open('inject.css','w').write(css)
print(len(render),len(handlers))
