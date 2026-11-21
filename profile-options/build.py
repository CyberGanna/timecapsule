"""Build the three Profile simplification options (prototypes, not live).
Each option = the live Profile page + one CSS + one JS layer. Run: python3 profile-options/build.py"""
import os
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'..','profile','timecapsule-profile.html'),encoding='utf-8').read()
common=open(os.path.join(here,'common.css')).read()
names={'a':'Option A · One calm column','b':'Option B · The universe is the cover','c':'Option C · Same layout, trimmed'}
for k,label in names.items():
    css=open(os.path.join(here,k+'.css')).read(); js=open(os.path.join(here,k+'.js')).read()
    bar=f'<div class="optbar">Draft, not live: {label}. <a href="index.html" style="color:#fff">All options</a> · <a href="../profile/timecapsule-profile.html" style="color:#fff">Current page</a></div>'
    out=src.replace('</head>',f'<style>{common}\n{css}</style></head>',1)
    i=out.find('<body>'); j=out.find('>',i)+1
    out=out[:j]+bar+out[j:]
    e=out.rfind('</body>')
    out=out[:e]+f'<script>window.addEventListener("load",function(){{{js}}});</script>'+out[e:]
    open(os.path.join(here,f'option-{k}.html'),'w',encoding='utf-8').write(out)
    print('wrote option-'+k)
