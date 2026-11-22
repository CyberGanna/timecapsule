# Adds "My conversations" to the avatar menu after "My universe" on every page, and points
# old "My universe #discussions" links at the new My conversations page.
# Run after rebuilding any page with the avatar menu: python3 menu/patch_myconv.py
import re, json, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = ["Le mie conversazioni", "Mis conversaciones", "Οι συζητήσεις μου"]
SKIP = ('profile-options/', 'node_modules/')
changed = []
for f in glob.glob(os.path.join(ROOT, '**/*.html'), recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith(SKIP) or rel in ('help/live-pages/myuniverse.html', 'help/live-pages/myconversations.html'):
        continue
    s = open(f, encoding='utf8').read(); o = s
    def add(m):
        pre, attrs = m.group(1), m.group(2)
        nxt = s[m.end():m.end() + 200]
        if 'myconversations.html' in nxt[:120]:
            return m.group(0)
        return m.group(0) + '<a href="%smyconversations.html"%s>My conversations</a>' % (pre, attrs)
    s = re.sub(r'<a href="([^"]*?)myuniverse\.html"((?: target="_top")?)>My universe</a>', add, s)
    s = s.replace('myuniverse.html#discussions', 'myconversations.html')
    if s != o and '<script id="tc-i18n">window.TCI18N_DICT=' in s:
        m = re.search(r'<script id="tc-i18n">window\.TCI18N_DICT=(.*?);\n', s, re.S)
        if m:
            D = json.loads(m.group(1).replace('<\\/', '</'))
            if 'My conversations' not in D:
                D['My conversations'] = TR
                s = s[:m.start()] + '<script id="tc-i18n">window.TCI18N_DICT=' + json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n' + s[m.end():]
    if s != o:
        open(f, 'w', encoding='utf8').write(s); changed.append(rel)
print('\n'.join(sorted(changed)))
