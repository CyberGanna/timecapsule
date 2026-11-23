# The shared dictionary translates "Time" as a clock time (Ora / Hora / Ώρα), which is right on
# forms (My tables edit, Create) but wrong for the Philosophy subtopic "Time".
# On pages where "Time" only appears as that subtopic, use Tempo / Tiempo / Χρόνος.
# Re-run after rebuilding any of these pages. Safe to run twice.
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD, NEW = '"Time":["Ora","Hora","Ώρα"]', '"Time":["Tempo","Tiempo","Χρόνος"]'
PAGES = ('help/live-pages/discussions.html', 'library/timecapsule-library.html',
         'help/live-pages/myconversations.html', 'help/live-pages/myuniverse.html',
         'help/live-pages/profile.html', 'profile/timecapsule-profile.html',
         'profile/timecapsule-profile-v2.html')
for rel in PAGES:
    F = os.path.join(R, rel); s = open(F, encoding='utf8').read()
    if NEW in s: print(rel, 'already'); continue
    assert s.count(OLD) == 1, rel
    open(F, 'w', encoding='utf8').write(s.replace(OLD, NEW)); print(rel, 'patched')
