# Universe panel background closer to the profile universe (navy instead of near black). Safe to run twice.
import os
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'timecapsule-onboarding.html')
s = open(F, encoding='utf8').read()
a = 'background:radial-gradient(120% 100% at 50% 45%,#141933 0%,var(--space) 70%,#070912 100%);border:1px solid rgba(238,241,255,.08)}'
b = 'background:radial-gradient(120% 100% at 50% 45%,#262D5C 0%,#1E2450 55%,#161B3C 100%);border:1px solid rgba(238,241,255,.08)}'
if b in s: print('already'); raise SystemExit
assert s.count(a) == 1
s = s.replace(a, b)
a2 = 'background:linear-gradient(to top,rgba(7,9,18,.92) 40%,transparent)}'
b2 = 'background:linear-gradient(to top,rgba(22,27,60,.94) 40%,transparent)}'
if a2 in s: s = s.replace(a2, b2)
open(F, 'w', encoding='utf8').write(s); print('patched')
