"""Karim 2026-11-19: one globe page. Landing prototype bar gets "View as: Signed out | Signed in";
Signed in opens the World page (signed-in globe), whose "Signed out" switch comes back here. Idempotent."""
L=["landing/body.html","landing/timecapsule-landing.html"]
A="bar.querySelector('label').appendChild(lp);"
ADD=A+"if(!bar.querySelector('.lp-va')){var va=document.createElement('label');va.className='lp-va';va.innerHTML='View as <span class=\"tc-seg\"><button type=\"button\" aria-pressed=\"true\">Signed out</button><button type=\"button\" aria-pressed=\"false\" data-in>Signed in</button></span>';bar.appendChild(va);va.querySelector('[data-in]').addEventListener('click',function(){var u='../world/timecapsule-world.html';if(window.TCI18N&&TCI18N.u)u=TCI18N.u(u);var a=document.createElement('a');a.href=u;a.target='_top';document.body.appendChild(a);a.click();a.remove()})}"
for f in L:
    s=open(f).read()
    if 'lp-va' in s: print('unchanged',f); continue
    assert s.count(A)==1,f; s=s.replace(A,ADD)
    open(f,'w').write(s); print('patched',f)
W="world/timecapsule-world.html"
s=open(W).read()
JS='''<script id="tc-so-landing">/* Signed out = the landing page (Karim 2026-11-19) */
document.addEventListener('click',function(e){var b=e.target.closest('#lproto [data-so="1"]');if(!b)return;e.preventDefault();e.stopImmediatePropagation();var u='../landing/timecapsule-landing.html';if(window.TCI18N&&TCI18N.u)u=TCI18N.u(u);var a=document.createElement('a');a.href=u;a.target='_top';document.body.appendChild(a);a.click();a.remove()},true);
</script>'''
if 'tc-so-landing' not in s:
    i=s.rfind('</body>'); s=s[:i]+JS+'\n'+s[i:]; open(W,'w').write(s); print('patched',W)
# Karim 2026-11-19: hero button says "Join the conversation" (2026-11-22) and opens Onboarding (signed out)
f="landing/timecapsule-landing.html"; s=open(f).read()
o='<a class="cta" href="../onboarding/timecapsule-onboarding.html" target="_top">Join TimeCapsule <span aria-hidden="true">→</span></a>'
if o in s:
    s=s.replace(o,'<a class="cta" href="../onboarding/timecapsule-onboarding.html" target="_top">Join the conversation <span aria-hidden="true">→</span></a>',1); open(f,'w').write(s); print('button',f)
