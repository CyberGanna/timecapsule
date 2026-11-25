"""Gabriele 2026-11-22: a new table with a topic the Table page didn't know (Religion, Craft, Travel, Science)
showed a navy header with a dark Philosophy icon. Give the Table page every topic's colour and icon,
copied from the Tables page (THEMES + TICON). Idempotent, marker "tc-alltopics". Re-run after topic-icons/apply.py."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'table-detail/timecapsule-table.html')
A = open(os.path.join(ROOT, 'help/live-pages/agenda.html'), encoding='utf8').read()
themes = re.search(r'THEMES=(\{[^}]*\})', A).group(1)
i = A.index('TICON={'); j = A.index('};', i)
ticon = A[i + 6:j + 1]
s = open(P, encoding='utf8').read()
s = re.sub(r'/\*tc-alltopics\*/.*?/\*end\*/', '', s, flags=re.S)
JS = ('/*tc-alltopics*/'
      f'Object.assign(TOPIC_C,{themes},{{Memoir:"#E8B577"}});'
      f'(function(){{const A={ticon};for(const k in A)TICON[k]=A[k]}})();/*end*/\n')
# inside the same script, right after both TOPIC_C and TICON are declared (before the first render)
k = s.index('const TICON={'); e = s.index('};\n', k) + 3
s = s[:e] + JS + s[e:]
open(P, 'w', encoding='utf8').write(s); print('topics ok')
