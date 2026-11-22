"""Build the three Profile simplification options (prototypes, not live).
Each option = the live Profile page + one CSS + one JS layer. Run: python3 profile-options/build.py"""
import os
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'..','profile','timecapsule-profile.html'),encoding='utf-8').read()
common=open(os.path.join(here,'common.css')).read()
names={'a2':'Option A2 · Lists open in the page','a':'Option A · One calm column','b':'Option B · The universe is the cover','c':'Option C · Same layout, trimmed'}
for k,label in names.items():
    parts=['a',k] if k=='a2' else [k]
    css='\n'.join(open(os.path.join(here,p+'.css')).read() for p in parts); js='\n'.join(open(os.path.join(here,p+'.js')).read() for p in parts)
    bar=f'<div class="optbar">Draft, not live: {label}. <a href="index.html" style="color:#fff">All options</a> · <a href="../profile/timecapsule-profile.html" style="color:#fff">Current page</a></div>'
    page=src
    if k=='a2':
        # slower drift (about a third), full stop near the mouse, stop for 4 s after a touch
        for a,b in [('m.a+=m.w*dt*sp','m.a+=m.w*dt*sp*.35*((Date.now()-(window.__uniHold||0))<4000?0:1)'),
                    ('goal=Math.min(1,Math.max(.08,(d-8)/70))','goal=Math.min(1,Math.max(0,(d-8)/70))')]:
            assert page.count(a)==1,a
            page=page.replace(a,b)
    out=page.replace('</head>',f'<style>{common}\n{css}</style></head>',1)
    i=out.find('<body>'); j=out.find('>',i)+1
    out=out[:j]+bar+out[j:]
    e=out.rfind('</body>')
    out=out[:e]+f'<script>window.addEventListener("load",function(){{{js}}});</script>'+out[e:]
    open(os.path.join(here,f'option-{k}.html'),'w',encoding='utf-8').write(out)
    print('wrote option-'+k)
