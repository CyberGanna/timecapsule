"""Karim 2026-11-19: Tables and Conversations numbers are links. Pop-up (people with a profile, i.e. Gregory):
Tables -> Gregory's tables page, Conversations -> his conversations. Profile header: open the full pages (same as the tabs' See all links; Karim 2026-11-19).
Rate and tip host preview: same pages as the pop-up. Idempotent; run after patch.py and patch_tips.py."""
import subprocess,re
def files(pat): return subprocess.run("grep -rlF '"+pat+"' --include=*.html --include=*.js .",shell=True,capture_output=True,text=True).stdout.split()
BASE='(location.pathname.indexOf("/live-pages/")>=0?"":location.pathname.indexOf("/invite/pages/")>=0?"../../help/live-pages/":"../help/live-pages/")'
LU='((p)=>{let x='+BASE+'+p;return window.TCI18N&&TCI18N.u?TCI18N.u(x):x})'
CSS='.tcp dl a.tcpn{display:grid;justify-items:center;gap:2px;color:inherit;text-decoration:none;border-radius:8px}.tcp dl a.tcpn:hover dd,.tcp dl a.tcpn:hover dt{color:#17C3C8}'
for f in files('<dt>Conversations</dt></div><div><dd class="gold">'):
    s=open(f).read();o=s
    for v in ('${fmt(u.tables)}','${u.tables}'):
        a='<dl><div><dd>'+v+'</dd><dt>Tables</dt></div>'
        if a in s:
            s=s.replace(a,'<dl><div>${u.profile?`<a class="tcpn" href="${'+LU+'("hosttables.html")}" target="_top">`:""}<dd>'+v+'</dd><dt>Tables</dt>${u.profile?"</a>":""}</div>')
    s=re.sub(r'<div><dd>(\$\{(?:fmt\()?u\.convs[^<]*\})</dd><dt>Conversations</dt></div>',lambda m:'<div>${u.profile?`<a class="tcpn" href="${'+LU+'("discussions.html#h="+encodeURIComponent(u.name||"Gregory"))}" target="_top">`:""}<dd>'+m.group(1)+'</dd><dt>Conversations</dt>${u.profile?"</a>":""}</div>',s)
    if s!=o and '.tcp dl a.tcpn' not in s and '.tcp dl div+div{' in s:
        s=s.replace('.tcp dl div+div{',CSS+'\n.tcp dl div+div{',1)
    if s!=o: open(f,'w').write(s);print('popup',f)
# Rate and tip host preview (Gregory)
f='rate-tip/timecapsule-rate-tip.html';s=open(f).read()
o='<dl class="lbpst"><div><dd>12</dd><dt>Tables</dt></div><div><dd>11</dd><dt>Conversations</dt></div>'
if o in s:
    s=s.replace(o,'<dl class="lbpst"><div><a class="lbpn" href="../help/live-pages/hosttables.html" target="_top"><dd>12</dd><dt>Tables</dt></a></div><div><a class="lbpn" href="../help/live-pages/discussions.html#h=Gregory" target="_top"><dd>11</dd><dt>Conversations</dt></a></div>')
    s=s.replace('</head>','<style>.lbpst a.lbpn{display:grid;justify-items:center;color:inherit;text-decoration:none}.lbpst a.lbpn:hover dd,.lbpst a.lbpn:hover dt{color:#17C3C8}</style></head>',1)
    open(f,'w').write(s);print('rate',f)
# Profile header: numbers open the tabs
JS='''<script id="tc-statlinks">(function(){var m={0:"p-tb",1:"p-lb"};document.querySelectorAll(".lbstats>div").forEach(function(d,i){if(!m[i])return;var p=document.getElementById(m[i]);if(!p)return;d.classList.add("lbsl");d.setAttribute("role","link");d.tabIndex=0;var go=function(){var a=p.querySelector(".seeall a."+(document.body.classList.contains("visitor")?"lbv":"lbo"));if(a)a.click()};d.addEventListener("click",go);d.addEventListener("keydown",function(e){if(e.key==="Enter")go()})})})();</script>
<style>.lbstats .lbsl{cursor:pointer}.lbstats .lbsl:hover dd,.lbstats .lbsl:hover dt{color:#17C3C8}</style>'''
for f in files('<dl class="lbstats">'):
    s=open(f).read()
    if 'tc-statlinks' in s: continue
    i=s.rfind('</body>'); s=s[:i]+JS+'\n'+s[i:]; open(f,'w').write(s);print('profile',f)
