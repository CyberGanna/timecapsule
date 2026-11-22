"""Build the three Profile simplification options (prototypes, not live).
Each option = the live Profile page + one CSS + one JS layer. Run: python3 profile-options/build.py"""
import os
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'..','profile','timecapsule-profile.html'),encoding='utf-8').read()
common=open(os.path.join(here,'common.css')).read()
names={'a6':'Option A6 · Map only, lists in the tabs','a5':'Option A5 · Map or List','a4':'Option A4 · Universe on the cover','a3':'Option A3 · One way in','a2':'Option A2 · Lists open in the page','a':'Option A · One calm column','b':'Option B · The universe is the cover','c':'Option C · Same layout, trimmed'}
for k,label in names.items():
    parts={'a2':['a','a2'],'a3':['a','a2','a3'],'a4':['a','a2','a3','a4'],'a5':['a','a2','a3','a5'],'a6':['a','a2','a3','a6']}.get(k,[k])
    css='\n'.join(open(os.path.join(here,p+'.css')).read() for p in parts); js='\n'.join(open(os.path.join(here,p+'.js')).read() for p in parts)
    bar=f'<div class="optbar">Draft, not live: {label}. <a href="index.html" style="color:#fff">All options</a> · <a href="../profile/timecapsule-profile.html" style="color:#fff">Current page</a></div>'
    page=src
    if k in ('a2','a3','a4','a5','a6'):
        # slower drift (about a third), full stop near the mouse, stop for 4 s after a touch
        for a,b in [('m.a+=m.w*dt*sp','m.a+=m.w*dt*sp*.35*((Date.now()-(window.__uniHold||0))<4000?0:1)'),
                    ('goal=Math.min(1,Math.max(.08,(d-8)/70))','goal=Math.min(1,Math.max(0,(d-8)/70))')]:
            assert page.count(a)==1,a
            page=page.replace(a,b)
    if k=='a6':
        # topics with more books sit on outer orbits (map only; lists keep their order)
        a='var R=[],O=[];T.forEach(function(th,i){var rx=44+i*21;'
        b='var R=[],O=[],RK=T.map(function(x,i){return i}).sort(function(p,q){return T[p].b.length-T[q].b.length||p-q});T.forEach(function(th,i){var rx=44+RK.indexOf(i)*21;'
        assert page.count(a)==1,a
        page=page.replace(a,b)
        # plain dot per book, no halo or ring around it
        a='el("circle",{r:6.5,fill:col,opacity:".12"},g);el("circle",{r:5,fill:"none",stroke:col,"stroke-width":"1.1"},g);el("circle",{"class":"core",r:2.6,fill:col},g);'
        b='el("circle",{"class":"core",r:3.4,fill:col},g);'
        assert page.count(a)==1,a
        page=page.replace(a,b)
    if k in ('a3','a4','a5','a6'):
        # expose the universe data so the topic rows can be built from it
        for a,b in [('var RT=T,MODE="read",LT=','var RT=window.__RT=T,MODE="read",LT=window.__LT='),
                    ('function YT(b){return MODE!="lib"&&MINE.indexOf(b[0])>=0}','function YT(b){return MODE!="lib"&&MINE.indexOf(b[0])>=0}window.__YT=function(b){return MINE.indexOf(b[0])>=0};')]:
            assert page.count(a)==1,a
            page=page.replace(a,b)
    out=page.replace('</head>',f'<style>{common}\n{css}</style></head>',1)
    i=out.find('<body>'); j=out.find('>',i)+1
    out=out[:j]+bar+out[j:]
    e=out.rfind('</body>')
    out=out[:e]+f'<script>window.addEventListener("load",function(){{{js}}});</script>'+out[e:]
    open(os.path.join(here,f'option-{k}.html'),'w',encoding='utf-8').write(out)
    print('wrote option-'+k)
