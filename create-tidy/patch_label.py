"""Karim 2026-11-22: Create a table question label "What would you like to talk about?" (was "What do you want to discuss?").
Idempotent."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
OLD, NEW = 'for="ntq">What do you want to discuss?</label>', 'for="ntq">What would you like to talk about?</label>'
T = {"What would you like to talk about?": ["Di cosa ti piacerebbe parlare?", "¿De qué te gustaría hablar?", "Για τι θα ήθελες να μιλήσεις;"]}
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if OLD not in s: continue
    s = s.replace(OLD, NEW)
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, flags=re.S)
    if m:
        d = json.loads(m.group(1)); d.update(T)
        s = s[:m.start(1)] + json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + s[m.end(1):]
    open(p, 'w', encoding='utf8').write(s); print(rel)
for f, line in (('help/dict-help.txt', 'What would you like to talk about?|Di cosa ti piacerebbe parlare?|¿De qué te gustaría hablar?'), ('i18n/dict-el.txt', 'What would you like to talk about?|Για τι θα ήθελες να μιλήσεις;')):
    q = os.path.join(ROOT, f); e = open(q, encoding='utf8').read()
    if '\nWhat would you like to talk about?|' not in '\n' + e: open(q, 'w', encoding='utf8').write(e.rstrip('\n') + '\n' + line + '\n')
