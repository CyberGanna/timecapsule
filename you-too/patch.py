"""Hide the "You too" marks (books and films the visitor also has) on the owner's own Profile.
They stay for a visitor. Idempotent. Run after rebuilding profile/timecapsule-profile-v2.html:
    python3 you-too/patch.py"""
import os
here=os.path.dirname(os.path.abspath(__file__))
f=os.path.join(here,'..','profile','timecapsule-profile-v2.html')
s=open(f,encoding='utf-8').read()
css='<style id="youtoo-owner">body:not(.visitor) em.yt,body:not(.visitor) .opt-items>div em{display:none!important}</style>'
if 'id="youtoo-owner"' in s:
    print('already patched')
else:
    s=s.replace('</head>',css+'</head>',1)
    open(f,'w',encoding='utf-8').write(s)
    print('patched',f)
