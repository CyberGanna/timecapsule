"""More table topics (Gabriele 2026-11-23, thread "Sort Clubhouse topics list").
Adds Society, Wellbeing, Books & Films, Work, Languages, Art and Music as table topics:
colour (THEMES), icon (TICON), IT/ES/EL names in every page's embedded i18n dict, the i18n
source dicts, and one sample table per new topic on the Tables page. Idempotent.
Re-run after rebuilding any page with THEMES/TICON, then table-detail/patch_topics_all.py."""
import os, re, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BF = "Books & Films"
WT = "Work & Tech"
NEW = [  # name, colour, icon, it, es, el
 ("Society", "#FFD166", '<circle cx="9" cy="8" r="3"/><path d="M3.5 20c0-3.3 2.4-5.5 5.5-5.5s5.5 2.2 5.5 5.5"/><circle cx="16.5" cy="9" r="2.4"/><path d="M16 14.6c2.8.1 4.5 2.1 4.5 5"/>', "Società", "Sociedad", "Κοινωνία"),
 ("Wellbeing", "#9BE7C4", '<path d="M5 19.5C5 11 10 5 20 4.5c-.3 9.8-6 15-14.5 15"/><path d="M5 19.5c3-4.3 6.3-7.3 10-9.5"/>', "Benessere", "Bienestar", "Ευεξία"),
 (BF, "#FFA8A8", '<path d="M3.5 5.5c2.8-1 5.8-.9 8.5.8 2.7-1.7 5.7-1.8 8.5-.8V19c-2.8-1-5.8-.9-8.5.8-2.7-1.7-5.7-1.8-8.5-.8z"/><path d="M12 6.3v13.5"/>', "Libri e film", "Libros y películas", "Βιβλία και ταινίες"),
 (WT, "#A9B8D9", '<rect x="3.5" y="7.5" width="17" height="12" rx="2"/><path d="M9 7.5v-2A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5v2M3.5 12.5h17"/>', "Lavoro e tecnologia", "Trabajo y tecnología", "Εργασία και τεχνολογία"),
 ("Languages", "#E8E4D8", '<path d="M3.5 4.5h10v7.5H8.5l-3 2.5V12h-2z"/><path d="M15.5 8.5h5v8h-1.5V19l-3-2.5H11V14"/>', "Lingue", "Idiomas", "Γλώσσες"),
 ("Art", "#FF6F91", '<path d="M12 3.5a8.5 8.5 0 1 0 0 17c1.2 0 1.8-.8 1.8-1.7 0-1.3-1.2-1.6-1.2-2.8 0-1 .8-1.6 1.9-1.6h2.2c2.3 0 3.8-1.7 3.8-3.8 0-4-3.8-7.1-8.5-7.1z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7.5" r="1"/><circle cx="14.5" cy="7.5" r="1"/>', "Arte", "Arte", "Τέχνη"),
 ("Music", "#9FA8FF", '<path d="M9 18V5.5l11-2V16"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>', "Musica", "Música", "Μουσική"),
]
def key(n): return n if n.isidentifier() else f'"{n}"'
HIST_ICON = '''History:'<path d="M7 5.5A2.5 2.5 0 0 1 9.5 3H19a2 2 0 0 1 0 4h-2.5v11.5A2.5 2.5 0 0 1 14 21H5a2 2 0 0 1 0-4h2z"/><path d="M5 17h9.5a2 2 0 0 1-.5 4M10.5 8.5h3M10.5 12h3"/>\''''
ICONS = "".join(f",{key(n)}:'{ic}'" for n, c, ic, *_ in NEW)
COL8 = "".join(f',{key(n)}:"{c}"' for n, c, *_ in NEW)
COL5 = "".join(f',{key(n)}:"{c}"' for n, c, *_ in NEW if n not in ("Art", "Music"))
DICT = "".join(f',"{n}":["{it}","{es}","{el}"]' for n, c, ic, it, es, el in NEW)
D_HIST = '"History":["Storia","Historia","Ιστορία"]'
TABLES = [
 ("Can we still disagree without hating each other?", "Society", "Lena", "Germany", "at(1,20,0)", 8, ["Lena", "Omar", "Priya"]),
 ("Rest is not laziness", "Wellbeing", "Yuki", "Japan", "at(2,9,0)", 6, ["Yuki", "Mia"]),
 ("The book that changed your mind", BF, "Sofia", "Italy", "at(2,19,30)", 8, ["Sofia", "David", "Elif", "Tom"]),
 ("Will AI change what work means?", WT, "Jonas", "United States", "at(3,18,30)", 8, ["Jonas", "Kofi"]),
 ("Slow Italian for beginners", "Languages", "Marco", "Italy", "at(3,10,0)", 6, ["Marco", "Ana", "Yuki"]),
 ("Why do we keep making art?", "Art", "Mia", "France", "at(4,19,0)", 8, ["Mia", "Gabriele"]),
 ("Songs that carry a place", "Music", "Kofi", "Ghana", "at(5,20,0)", 8, ["Kofi", "Sofia", "Omar"]),
]
def patch_html(s, rel):
    if "Wellbeing" in s: return s
    s = s.replace('Science:"#8BE38B",History:"#E8B577"}', 'Science:"#8BE38B",History:"#E8B577"' + COL8 + '}')
    s = s.replace('History:"#E8B577",Climate:', 'History:"#E8B577"' + COL5 + ',Climate:')
    s = s.replace(HIST_ICON, HIST_ICON + ICONS)
    s = s.replace(D_HIST, D_HIST + DICT)
    if rel == "help/live-pages/agenda.html":
        m = re.search(r'\{id:13,[^}]*\}', s)
        rows = "".join(',{id:%d,title:"%s",theme:"%s",host:"%s",country:"%s",lang:"English",at:%s,seats:%d,people:[%s]}'
                       % (30 + i, t, th, h, c, at, n, ",".join(f'"{x}"' for x in p)) for i, (t, th, h, c, at, n, p) in enumerate(TABLES))
        s = s[:m.end()] + rows + s[m.end():]
    return s
files = subprocess.run(['grep', '-rlE', '#8BE38B', '--include=*.html', '.'], cwd=ROOT, capture_output=True, text=True).stdout.split()
for rel in sorted(files):
    rel = rel[2:]
    if rel.startswith(("profile-options/", "topics-more/")): continue
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read(); n = patch_html(s, rel)
    if n != s: open(p, 'w', encoding='utf8').write(n); print(rel)
def add_lines(path, lines):
    p = os.path.join(ROOT, path); s = open(p, encoding='utf8').read()
    add = [l for l in lines if not re.search(r'^' + re.escape(l.split("|")[0]) + r'\|', s, re.M)]
    if add: open(p, 'a', encoding='utf8').write(("" if s.endswith("\n") else "\n") + "\n".join(add) + "\n"); print(path, len(add))
add_lines("i18n/dict1.txt", [f"{n}|{it}|{es}" for n, c, ic, it, es, el in NEW])
add_lines("i18n/dict-el.txt", [f"{n}|{el}" for n, c, ic, it, es, el in NEW])
