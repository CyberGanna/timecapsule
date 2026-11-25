#!/usr/bin/env python3
"""Every person pop-up shows "View profile" (Gabriele 2026-11-22: some had it, some not).
Before, only Gregory (and hosts with a profile link) got it. The prototype has one sample
Profile page, so every person links to it. Also removes the gold (host) and violet (you)
rings from the face stacks in the Tables page list view (Gabriele: rings are a distraction).
Idempotent. python3 popup-profile/patch.py"""
import re,os,glob
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
FILES=['table-detail/timecapsule-table.html','table-detail/src/h_page.js','world/timecapsule-world.html','landing/world-base.html',
'landing/timecapsule-landing-artifact.html','landing/timecapsule-landing.html','help/live-pages/agenda.html','help/live-pages/table.html',
'help/live-pages/world.html','help/live-pages/create.html','invite/pages/agenda.html']
P=re.compile(r'profile:n==="Gregory"\?("[^"]*"|URL_GREG):(?:u\.prof|"")')
RING='<style id="no-rings">.lf .fc span:first-child,.lf .fc .you{box-shadow:none!important}</style>'
for f in FILES:
    p=os.path.join(R,f);s=open(p,encoding='utf-8').read();n=len(P.findall(s))
    s=P.sub(r'profile:\1',s)
    if f.endswith('agenda.html') and 'id="no-rings"' not in s:
        i=s.rfind('</body>');s=s[:i]+RING+s[i:]
    open(p,'w',encoding='utf-8').write(s);print(f,n)
