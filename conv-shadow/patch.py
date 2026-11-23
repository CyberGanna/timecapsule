"""Karim 2026-11-23: Conversations page cards get the same shadow as the Tables page cards. Idempotent, marker "tc-convshadow"."""
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS='<style id="tc-convshadow">.dp .card{box-shadow:0 1px 0 rgba(255,255,255,.04) inset,0 14px 34px rgba(4,6,20,.55),0 2px 6px rgba(4,6,20,.35)}.dp .card:hover{box-shadow:0 1px 0 rgba(255,255,255,.06) inset,0 18px 40px rgba(4,6,20,.62),0 2px 6px rgba(4,6,20,.35)}</style>'
for rel in ['help/live-pages/discussions.html','library/disc-body.html']:
    p=os.path.join(ROOT,rel);s=open(p,encoding='utf8').read()
    if 'tc-convshadow' in s:continue
    k=s.rfind('</body>');s=s[:k]+CSS+s[k:] if k>=0 else s+CSS
    open(p,'w',encoding='utf8').write(s);print(rel)
