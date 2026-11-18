# Adds the library to the Profile: the glowing photo in the centre of the k-universe map
# opens "My library" (discussions as stars, topics as orbits), plus a Library tab.
# Idempotent: if the profile is already patched it starts again from the pre-library version in git.
import os, re, json, subprocess, html
BASE_COMMIT = 'f26a9a8'

def rep(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:80]); return s.replace(a, b)

def lib_tab(recs):
    order = []; by = {}
    for r in recs.values():
        by.setdefault(r['topic'], {}).setdefault(r['sub'], []).append(r)
        if r['topic'] not in order: order.append(r['topic'])
    h = ['<section class="panel" id="p-lb" role="tabpanel" aria-labelledby="t-lb" hidden>',
         '<p class="lbintro"><span class="lbo">Transcripts and notes saved after your tables, by topic. Each one can be picked up again.</span><span class="lbv">Transcripts and notes from Gregory\'s tables, by topic. Ask to join the next round of any of them.</span></p>']
    for t in order:
        n = sum(len(v) for v in by[t].values()); col = next(iter(by[t].values()))[0]['col']
        npub = sum(1 for v in by[t].values() for r in v if not r['private'])
        h.append('<div class="lbt%s"><h3><i style="--c:%s"></i>%s<span>%d</span></h3>' % (' lbprivonly' if npub == 0 else '', col, t, n))
        for sub, rs in by[t].items():
            allpriv = all(r['private'] for r in rs)
            h.append('<h4%s>%s</h4><ul class="lbl">' % (' class="lbpriv"' if allpriv else '', html.escape(sub)))
            for r in rs:
                last = r['rounds'][-1]; k = len(r['rounds'])
                meta = ('<span>%d</span> <span>rounds</span> · ' % k if k > 1 else '') + '%s · %d <span>people</span>' % (last['date'], last['people'])
                lock = '<span class="lblock"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6 10V8a6 6 0 0112 0v2h1v11H5V10zm2 0h8V8a4 4 0 00-8 0z"/></svg>Only the people at the table</span>' if r['private'] else ''
                h.append('<li class="lbr%s"><a href="../library/timecapsule-library.html#r=%s" target="_top" data-r="%s"><b data-noi18n>%s</b><small>%s</small>%s</a></li>'
                         % (' lbpriv' if r['private'] else '', r['id'], r['id'], html.escape(r['title']), meta, lock))
            h.append('</ul>')
        h.append('</div>')
    h.append('</section>')
    return '\n'.join(h)

CSS = r'''<style id="lib-css">
.sunav{cursor:default;outline:none}
.lbreads.libmode .wmt,.lbreads.libmode .kb-r,.lbreads:not(.libmode) .kb-l{display:none}
.lbreads .uni{background:#0F1A30;border:1px solid #6CB8FF}
.lbreads.libmode .uni{border-color:#F0C858}
.sunav .avglow{transform-box:fill-box;transform-origin:center;animation:avp 3.6s ease-in-out infinite}
@keyframes avp{50%{opacity:.55;transform:scale(1.18)}}
@media (prefers-reduced-motion:reduce){.sunav .avglow{animation:none}}
.sunav .avring{transition:stroke-width .15s}
.ulay .udot{cursor:pointer}
.uh-sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.unitog{position:absolute;top:10px;left:14px;z-index:3;display:flex;gap:14px}
.unitog button{min-height:30px;padding:0;border:0;border-bottom:1.5px solid transparent;border-radius:0;background:none;color:rgba(238,241,255,.55);font:inherit;font-size:13px;cursor:pointer;white-space:nowrap}
.unitog button span{display:none}
.unitog button:hover{color:#EEF1FF}
.unitog button[aria-pressed=true]{color:#EEF1FF;border-bottom-color:var(--teal)}
.unitog button:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.wmt{display:none!important}
.lbreads .uni{padding-top:44px}
.lbreads .ulay{top:44px}
.lbreads:not(.fsx) #uni{margin-top:-10px;margin-bottom:10px}
.lbreads .ulay:not(.pg){top:34px;bottom:10px}
.lbreads #uni{transition:margin .45s ease}
.lbreads .uni:has(#ulink:not([hidden])) #uni{margin-top:0;margin-bottom:0}
.lbreads .uni:has(#ulink:not([hidden])) .ulay:not(.pg){top:44px;bottom:0}
.lbreads .ulink{top:50px;left:6px}
.uni.fs .ua.uend{min-width:44px;height:40px;line-height:40px;padding:0 12px;font-size:24px}
.uni:has(#ulink:not([hidden])) #pgb{visibility:hidden}
#uni-h{margin-bottom:4px}
body.visitor .unitog .lbc-o,body:not(.visitor) .unitog .lbc-v{display:none}
.ulay .pl li[data-r]{cursor:pointer}.ulay .pl li[data-r]:hover span{text-decoration:underline;text-underline-offset:3px}
.lbintro{margin:4px 0 18px;color:var(--mute);font-size:13.5px;line-height:1.5}
body.visitor .lbo,body:not(.visitor) .lbv{display:none}
body.visitor .lbpriv,body.visitor .lbprivonly{display:none!important}
body.visitor #t-lb .lbc-o,body:not(.visitor) #t-lb .lbc-v{display:none}
.lbt{margin:0 0 26px}
.lbt h3{display:flex;align-items:center;gap:8px;margin:0 0 4px;font-size:16px;font-weight:500}
.lbt h3 i{width:9px;height:9px;border-radius:50%;background:var(--c)}
.lbt h3 span{color:var(--mute);font-size:13px;font-weight:400}
.lbt h4{margin:14px 0 2px 17px;font-size:11px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--mute)}
.lbl{list-style:none;margin:0;padding:0 0 0 17px}
.lbr{display:flex;align-items:center;gap:12px;padding:7px 0}
.lbr a{flex:1;min-width:0;display:grid;gap:3px;color:inherit;text-decoration:none}
.lbr a b{font-weight:500;font-size:15px}
.lbr a:hover b{text-decoration:underline;text-underline-offset:3px}
.lbr small{color:var(--mute);font-size:12.5px}
.lblock{display:inline-flex;align-items:center;gap:5px;color:var(--mute);font-size:12px}.lblock svg{width:11px;height:11px}
.lbk{flex:none;color:var(--mute);font-size:12px}
@media (max-width:640px){.lbk{display:none}.lbt h4,.lbl{margin-left:0;padding-left:0}}
</style>'''

def run(ROOT, recs, LIBD, add_dict):
    P = os.path.join(ROOT, 'profile/timecapsule-profile.html')
    s = open(P, encoding='utf8').read()
    if 'id="t-lb"' in s:
        s = subprocess.run(['git', '-C', ROOT, 'show', BASE_COMMIT + ':profile/timecapsule-profile.html'], capture_output=True, text=True, check=True).stdout
    s = add_dict(s, LIBD)
    npub = sum(1 for r in recs.values() if not r['private'])
    # tab + panel
    s = rep(s, '<button type="button" role="tab" id="t-fw" aria-selected="false" aria-controls="p-fw"><b>6</b> Following</button>',
            '<button type="button" role="tab" id="t-lb" aria-selected="false" aria-controls="p-lb"><b class="lbc-o">%d</b><b class="lbc-v">%d</b> Discussions</button>\n    <button type="button" role="tab" id="t-fw" aria-selected="false" aria-controls="p-fw"><b>6</b> Following</button>' % (len(recs), npub))
    s = rep(s, '  <section class="panel" id="p-fw" role="tabpanel"', lib_tab(recs) + '\n\n  <section class="panel" id="p-fw" role="tabpanel"')
    s = rep(s, '<h2 id="uni-h">My readings <span>36</span></h2>',
            '<h2 id="uni-h">My universe</h2>')
    s = rep(s, '<div class="uni"><button type="button" class="ulink"', '<div class="uni"><div class="unitog" role="group" aria-label="Which universe"><button type="button" data-m="read" aria-pressed="true">Readings <span>36</span></button><button type="button" data-m="lib" aria-pressed="false">Discussions <span class="lbc-o">%d</span><span class="lbc-v">%d</span></button></div><button type="button" class="ulink"' % (len(recs), npub))
    # library data for the map: one orbit per topic, one star per discussion
    order = []; by = {}
    for r in recs.values():
        by.setdefault(r['topic'], []).append(r)
        if r['topic'] not in order: order.append(r['topic'])
    LT = [dict(n=t, c=by[t][0]['col'], b=[[r['title'], r['sub'] + (' · %d rounds' % len(r['rounds']) if len(r['rounds']) > 1 else ''), r['id'], 1 if r['private'] else 0] for r in sorted(by[t], key=lambda r: r['sub'])]) for t in order]
    # universe code
    s = rep(s, '\nvar BOOKS=[];T.forEach', '\nvar RT=T,MODE="read",LT=' + json.dumps(LT, ensure_ascii=False) + ';\nvar BOOKS=[];T.forEach')
    s = rep(s, '<b>k▪universe</b><p>Turns your reading list into a living map. Every book finds its orbit in a theme, so you can see at a glance what shapes your thinking.</p><a href="https://k-universe.com/" target="_blank" rel="noopener">Learn more →</a>',
            '<b class="kb-r">k▪universe</b><p class="kb-r">Turns your reading list into a living map. Every book finds its orbit in a theme, so you can see at a glance what shapes your thinking.</p>'
            '<b class="kb-l">Discussions</b><p class="kb-l">Every table leaves a trace. The discussions you save find their orbit here, by topic, so you can see the ideas you have explored with other people.</p><p class="kb-l">Tap a planet to read it again, or pick it up for another round.</p>')
    s = rep(s, '<span aria-hidden="true">powered by k▪universe</span>', '<span class="wmt" aria-hidden="true">powered by k▪universe</span>')
    s = rep(s, ' el("circle",{cx:cx,cy:cy,r:4.2,fill:"#FFFDF2"},sunG);', ' var avg=sunAv(sys,orbs,cx,cy);')
    s = rep(s, 'sunG.style.opacity=(1-e).toFixed(3);', 'sunG.style.opacity=(1-e).toFixed(3);avg.setAttribute("transform","rotate("+(-TILT*(1-e)).toFixed(2)+" "+cx+" "+cy+")");avg.style.opacity=(1-e).toFixed(3);avg.style.pointerEvents=e>.5?"none":"";')
    s = rep(s, '"aria-label":bk[0]+" by "+bk[1]+", "+th.n},front);', '"aria-label":bk[0]+BY()+bk[1]+", "+th.n},front);')
    s = rep(s, "aria-label=\"'+esc(b[0])+' by '+esc(b[1])+'\"></button>'", "aria-label=\"'+esc(b[0])+BY()+esc(b[1])+'\"></button>'")
    s = rep(s, "' '+th.n+' books\">'", "' '+th.n+' '+(MODE==\"lib\"?\"discussions\":\"books\")+'\">'")
    s = rep(s, 's.onclick=null;s.onpointerdown=function(ev){if(U.list', 's.onclick=null;s.onpointerdown=function(ev){if(ev.target.closest&&ev.target.closest(".sunav"))return;if(U.list')
    s = rep(s, "'<li style=\"--c:'+th.c+'\"'+(k===sel?' class=\"sel\"':'')+'>", "'<li style=\"--c:'+th.c+'\"'+RA(b)+(k===sel?' class=\"sel\"':'')+'>")
    s = rep(s, "'<li style=\"--c:'+th.c+'\"><span>'+esc(b[0])+'</span><small>'+esc(b[1])+' · <i", "'<li style=\"--c:'+th.c+'\"'+RA(b)+'><span>'+esc(b[0])+'</span><small>'+esc(b[1])+' · <i")
    s = rep(s, '<b>All books</b>', "<b>'+(MODE==\"lib\"?\"All discussions\":\"All books\")+'</b>")
    s = rep(s, "function capU(){var nb=T.reduce(function(a,x){return a+x.b.length},0);return '<button type=\"button\" class=\"caplink\" data-act=\"all\">'+nb+' books</button>. <button type=\"button\" class=\"caplink\" data-act=\"themes\">'+T.length+' themes</button>. Hover/tap to learn more.'}",
            "function capU(){var nb=T.reduce(function(a,x){return a+x.b.length},0);if(MODE==\"lib\")return '<button type=\"button\" class=\"caplink\" data-act=\"themes\"><span>'+T.length+'</span> topics</button>. <button type=\"button\" class=\"caplink\" data-act=\"all\"><span>'+nb+'</span> discussions</button>. <span>Tap a planet to open it.</span>';return '<button type=\"button\" class=\"caplink\" data-act=\"themes\"><span>'+T.length+'</span> topics</button>. <button type=\"button\" class=\"caplink\" data-act=\"all\"><span>'+nb+'</span> books</button>. <span>Tap a planet to open it.</span>'}")
    HELP = r'''function BY(){return MODE=="lib"?", ":" by "}
function RA(b){return b&&b[2]?' data-r="'+b[2]+'" tabindex="0" role="link"':''}
function goRec(id){var a=document.createElement("a");a.href="../library/timecapsule-library.html#r="+id+(document.body.classList.contains("visitor")?"&as=visitor":"");a.target="_top";document.body.appendChild(a);a.click();a.remove()}
ulay.addEventListener("click",function(e){var li=e.target.closest("li[data-r]");if(li)goRec(li.dataset.r)});
ulay.addEventListener("keydown",function(e){var li=e.target.closest("li[data-r]");if(li&&(e.key=="Enter"||e.key==" ")){e.preventDefault();goRec(li.dataset.r)}});
function sunAv(sys,before,cx,cy){
 var src=(document.querySelector(".lbh img.big")||{}).src||"";
 var cp=el("clipPath",{id:"avclip"},d);el("circle",{cx:cx,cy:cy,r:15},cp);
 var gl=el("radialGradient",{id:"avg"},d);el("stop",{offset:".45","stop-color":"#FFE7A8","stop-opacity":".9"},gl);el("stop",{offset:"1","stop-color":"#F0A040","stop-opacity":"0"},gl);
 var g=el("g",{"class":"sunav","aria-hidden":"true"},sys);sys.insertBefore(g,before);
 el("circle",{"class":"avglow",cx:cx,cy:cy,r:28,fill:"url(#avg)"},g);
 el("circle",{cx:cx,cy:cy,r:15.5,fill:"#1B2144"},g);
 if(src){var im=el("image",{x:cx-15,y:cy-15,width:30,height:30,"clip-path":"url(#avclip)",preserveAspectRatio:"xMidYMid slice"},g);im.setAttribute("href",src)}
 el("circle",{"class":"avring",cx:cx,cy:cy,r:15.5,fill:"none",stroke:MODE=="lib"?"#7FF0F2":"#FFE3A0","stroke-width":"1.6"},g);
 el("circle",{cx:cx,cy:cy,r:22,fill:"transparent"},g);
 return g}
document.querySelectorAll(".unitog button").forEach(function(b){b.addEventListener("click",function(){if(b.dataset.m!=MODE||!ulink.hidden||!ulay.hidden)setMode(b.dataset.m)})});
function setMode(m){MODE=m;T=m=="lib"?LT:RT;utip.hidden=true;U.list=false;U.page=-1;U.allPg=false;U.uniPg=false;ulay.hidden=true;ulay.className="ulay";ulink.hidden=true;ulink.textContent="☰ List";s.classList.remove("dim");s.parentNode.classList.remove("pgm");if(typeof back!="undefined"&&back)back.hidden=true;document.querySelectorAll(".unitog button").forEach(function(b){b.setAttribute("aria-pressed",b.dataset.m==m)});var r=document.querySelector(".lbreads");if(r)r.classList.toggle("libmode",m=="lib");var kq=document.getElementById("kq");if(kq)kq.setAttribute("aria-label",m=="lib"?"What are Discussions?":"What is k-universe?");var kb=document.getElementById("kbox");if(kb)kb.setAttribute("aria-label",m=="lib"?"About Discussions":"About k-universe");universe()}
window.KUlib=function(){if(MODE!="lib")setMode("lib")};
'''
    s = rep(s, '\nuniverse();\nwindow.KU={T:T,render:universe};', '\n' + HELP + 'universe();\nwindow.KU={T:RT,render:function(){if(MODE!="read"){MODE="read";T=RT;var r=document.querySelector(".lbreads");if(r)r.classList.remove("libmode");document.querySelectorAll(".unitog button").forEach(function(b){b.setAttribute("aria-pressed",b.dataset.m=="read")})}universe()}};')
    s = rep(s, 'd.onclick=function(e){e.stopPropagation();show(d)}', 'd.onclick=function(e){e.stopPropagation();if(MODE=="lib"){goRec(T[d.dataset.i].b[d.dataset.j][2]);return}show(d)}')
    # deep link #lib opens the Library tab and the library map
    TAIL = CSS + '''<script>(function(){if(!/(^#|&)lib\\b/.test(location.hash))return;var t=document.getElementById("t-lb");if(t)t.click();if(window.KUlib)KUlib()})();</script>\n'''
    i = s.rindex('</body></html>')
    s = s[:i] + TAIL + s[i:]
    s = s.replace('◎ Universe', '‹ Back')
    s = rep(s, '\nfunction allBooks(){', '\nvar _ulb=ulink.onclick;ulink.onclick=function(){utip.hidden=true;if(U.list&&!U.uniPg&&(U.page>=0||U.allPg)){rows();return}_ulb()};\nfunction allBooks(){')
    s = rep(s, 'var cx=170,cy=125,TILT=-14,', 'var cx=170,cy=125,TILT=MODE=="lib"?14:-14,')
    open(P, 'w', encoding='utf8').write(s)
    subprocess.run(['python3', os.path.join(ROOT, 'i18n/add-greek.py'), P], check=True)
    print('profile patched', len(s))
