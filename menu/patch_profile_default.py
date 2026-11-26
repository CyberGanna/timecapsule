# Profile Version 2 is the default Profile (Gabriele, 2026-11-22): every link to profile/timecapsule-profile.html
# now points to profile/timecapsule-profile-v2.html. The old page stays reachable from index.html only.
# Skips the profile-options drafts and the old profile itself (it is the source for profile-options/build.py).
# Run again after rebuilding any page with the header or avatar menu. Safe to run twice.
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD, NEW = 'timecapsule-profile.html', 'timecapsule-profile-v2.html'
n = 0
for d, dirs, files in os.walk(R):
    dirs[:] = [x for x in dirs if not x.startswith('.') and x not in ('node_modules', 'profile-options')]
    for f in files:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); rel = os.path.relpath(p, R)
        if rel in ('profile/timecapsule-profile.html', 'index.html'): continue
        s = open(p, encoding='utf8').read()
        if OLD in s:
            open(p, 'w', encoding='utf8').write(s.replace(OLD, NEW)); n += 1; print('patched', rel)
# index: "Profile" opens V2, the old one is listed as "Profile (old version)"
p = os.path.join(R, 'index.html'); s = open(p, encoding='utf8').read()
a = '<a href="profile/timecapsule-profile.html">Profile</a>\n<a href="profile/timecapsule-profile-v2.html">Profile Version 2</a>'
b = '<a href="profile/timecapsule-profile-v2.html">Profile</a>\n<a href="profile/timecapsule-profile.html">Profile (old version)</a>'
if a in s:
    open(p, 'w', encoding='utf8').write(s.replace(a, b)); print('patched index.html')
print(n, 'pages')
