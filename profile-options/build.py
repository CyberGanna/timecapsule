"""Build the three Profile simplification options (prototypes, not live).
Each option = the live Profile page + one CSS + one JS layer. Run: python3 profile-options/build.py"""
import os
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'..','profile','timecapsule-profile.html'),encoding='utf-8').read()
common=open(os.path.join(here,'common.css')).read()
names={'a9':'Option A9 · The orbit becomes a line','a8':'Option A8 · A planet opens its orbit','a7':'Option A7 · Map, tap the photo for the list','a6':'Option A6 · Map only, lists in the tabs','a5':'Option A5 · Map or List','a4':'Option A4 · Universe on the cover','a3':'Option A3 · One way in','a2':'Option A2 · Lists open in the page','a':'Option A · One calm column','b':'Option B · The universe is the cover','c':'Option C · Same layout, trimmed'}
for k,label in names.items():
    parts={'a2':['a','a2'],'a3':['a','a2','a3'],'a4':['a','a2','a3','a4'],'a5':['a','a2','a3','a5'],'a6':['a','a2','a3','a6'],'a7':['a','a2','a3','a7'],'a8':['a','a2','a3','a7','a8'],'a9':['a','a2','a3','a7','a9']}.get(k,[k])
    css='\n'.join(open(os.path.join(here,p+'.css')).read() for p in parts); js='\n'.join(open(os.path.join(here,p+'.js')).read() for p in parts)
    bar=f'<div class="optbar">Draft, not live: {label}. <a href="index.html" style="color:#fff">All options</a> · <a href="../profile/timecapsule-profile.html" style="color:#fff">Current page</a></div>'
    page=src
    if k in ('a2','a3','a4','a5','a6','a7','a8','a9'):
        # slower drift (about a third), full stop near the mouse, stop for 4 s after a touch
        for a,b in [('m.a+=m.w*dt*sp','m.a+=m.w*dt*sp*.35*((Date.now()-(window.__uniHold||0))<4000?0:1)'),
                    ('goal=Math.min(1,Math.max(.08,(d-8)/70))','goal=Math.min(1,Math.max(0,(d-8)/70))')]:
            assert page.count(a)==1,a
            page=page.replace(a,b)
    if k in ('a6','a7','a8','a9'):
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
    if k in ('a3','a4','a5','a6','a7','a8','a9'):
        # expose the universe data so the topic rows can be built from it
        for a,b in [('var RT=T,MODE="read",LT=','var RT=window.__RT=T,MODE="read",LT=window.__LT='),
                    ('function YT(b){return MODE!="lib"&&MINE.indexOf(b[0])>=0}','function YT(b){return MODE!="lib"&&MINE.indexOf(b[0])>=0}window.__YT=function(b){return MINE.indexOf(b[0])>=0};')]:
            assert page.count(a)==1,a
            page=page.replace(a,b)
    if k=='a9':
        # Version 2: films join the Readings universe (sample films, Gabriele-style demo data)
        films='{"Philosophy":[["The Seventh Seal","Bergman"],["My Dinner with Andre","Malle"],["Waking Life","Linklater"]],"Religion":[["Of Gods and Men","Beauvois"]],"Home":[["Tokyo Story","Ozu"]],"Travel":[["Paris, Texas","Wenders"],["The Motorcycle Diaries","Salles"]],"Energy":[["Koyaanisqatsi","Reggio"]],"Craft":[["Jiro Dreams of Sushi","Gelb"]]}'
        page=page.replace('"On the Road"]','"On the Road", "Paris, Texas", "Tokyo Story", "The Seventh Seal"]',1)
        # Version 2: a bigger universe. Orbits spaced out (44+21k -> 40+25k); the photo keeps its on-screen size
        for x,y in [('var rx=44+RK.indexOf(i)*21;','var rx=40+RK.indexOf(i)*25;'),
                    ('function sunAv(sys,before,cx,cy){','function sunAv(sys,before,cx,cy){var Z=1,uw=document.getElementById("uni").getBoundingClientRect().width;if(uw)Z=Math.min(1,1.52/(uw/340));'),
                    ('el("circle",{cx:cx,cy:cy,r:15},cp);','el("circle",{cx:cx,cy:cy,r:15*Z},cp);'),
                    ('el("circle",{"class":"avglow",cx:cx,cy:cy,r:28,','el("circle",{"class":"avglow",cx:cx,cy:cy,r:28*Z,'),
                    ('el("circle",{cx:cx,cy:cy,r:15.5,fill:"#1B2144"},g);','el("circle",{cx:cx,cy:cy,r:15.5*Z,fill:"#1B2144"},g);'),
                    ('el("image",{x:cx-15,y:cy-15,width:30,height:30,','el("image",{x:cx-15*Z,y:cy-15*Z,width:30*Z,height:30*Z,'),
                    ('el("circle",{"class":"avring",cx:cx,cy:cy,r:15.5,','el("circle",{"class":"avring",cx:cx,cy:cy,r:15.5*Z,'),
                    ('el("circle",{cx:cx,cy:cy,r:22,fill:"transparent"},g);','el("circle",{cx:cx,cy:cy,r:22*Z,fill:"transparent"},g);')]:
            assert page.count(x)==1,x
            page=page.replace(x,y)
        a='var RT=window.__RT=T,'
        assert page.count(a)==1,a
        page=page.replace(a,'(function(F){T.forEach(function(t){(F[t.n]||[]).forEach(function(f){t.b.push([f[0],f[1],"","film"])})})})('+films+');'+a)
    out=page.replace('</head>',f'<style>{common}\n{css}</style></head>',1)
    i=out.find('<body>'); j=out.find('>',i)+1
    out=out[:j]+bar+out[j:]
    e=out.rfind('</body>')
    out=out[:e]+f'<script>window.addEventListener("load",function(){{{js}}});</script>'+out[e:]
    open(os.path.join(here,f'option-{k}.html'),'w',encoding='utf-8').write(out)
    print('wrote option-'+k)
    if k=='a9':
        # Profile Version 2 (Karim, 2026-11-22): option A9 as its own page next to the current Profile, no draft bar
        v2=out.replace(bar,'',1).replace('<title>Gregory Profile Letterbox','<title>Profile Version 2',1)
        open(os.path.join(here,'..','profile','timecapsule-profile-v2.html'),'w',encoding='utf-8').write(v2)
        print('wrote profile/timecapsule-profile-v2.html')
