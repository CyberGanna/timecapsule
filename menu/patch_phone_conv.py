# Adds "Conversations" to the phone-only links of the avatar menu (class "ph"), right after
# "Tables", the same order as the desktop nav. Re-runnable: skips pages that already have it.
# Run after rebuilding any page with the header: python3 menu/patch_phone_conv.py
import re, json, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = ["Conversazioni", "Conversaciones", "Συζητήσεις"]
SKIP = ('profile-options/', 'node_modules/')
PAT = re.compile(r'<a class="ph" href="((?:[^"]*/)?)agenda\.html" target="_top">Tables</a>')
changed = []
for f in glob.glob(os.path.join(ROOT, '**/*.html'), recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith(SKIP):
        continue
    s = open(f, encoding='utf8').read(); o = s
    def add(m):
        if s[m.end():m.end() + 80].find('discussions.html') != -1:
            return m.group(0)
        return m.group(0) + '<a class="ph" href="%sdiscussions.html" target="_top">Conversations</a>' % m.group(1)
    s = PAT.sub(add, s)
    if s != o and '<script id="tc-i18n">window.TCI18N_DICT=' in s:
        m = re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n', s, re.S)
        if m:
            D = json.loads(m.group(1).replace('<\\/', '</'))
            if 'Conversations' not in D:
                D['Conversations'] = TR
                s = s[:m.start()] + '<script id="tc-i18n">window.TCI18N_DICT=' + json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n' + s[m.end():]
    if s != o:
        open(f, 'w', encoding='utf8').write(s); changed.append(rel)
print(len(changed)); print('\n'.join(sorted(changed)))
