"""Karim 2026-11-22 "tidy this section": Topic / What do you want to discuss / picture in Create a table.
- Topic: an even grid of round pills (4 per row on desktop, 2 on phones), each with its colour dot.
- Suggestions move out of the text box to a wrapping row under it (no cut-off chips).
- Picture gets its own label "Picture (optional)" and a dashed drop box the size of the thumbnail.
Idempotent, marker "tc-ctidy". Run after photo-pos/patch_tidy.py."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
T = {"Picture": ["Immagine", "Imagen", "Εικόνα"]}
REPS = [
 ('<button class="fch" data-nth="${k}" aria-pressed="${nt.theme===k}">${k}</button>',
  '<button class="fch" data-nth="${k}" aria-pressed="${nt.theme===k}" style="--c:${THEMES[k]}"><i></i>${k}</button>'),
 ('<span id="ntcount"></span>\n          <div class="sparks">', '<span id="ntcount"></span></div>\n          <div class="sparks"><!--tc-ctidy-->'),
 ('<button data-spark="${q}" data-sth="${th}">${q}</button>`).join("")}</div></div></div>',
  '<button data-spark="${q}" data-sth="${th}">${q}</button>`).join("")}</div></div>'),
 ('<div class="opt" style="margin-top:12px"><div class="cover" id="ntcover">',
  '<div class="opt"><label class="l">Picture <span class="optl">optional</span></label><div class="cover" id="ntcover">'),
 ('Add a picture <span class="optl">optional</span></button>', 'Add a picture</button>'),
]
CSS = '''<style id="tc-ctidy-css">
#cpage .ntchips{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;flex-wrap:nowrap}
#cpage .ntchips .fch{display:flex;align-items:center;justify-content:center;gap:7px;height:38px;padding:0 10px;border-radius:999px;font-size:14px;width:100%;min-width:0;white-space:nowrap}
#cpage .ntchips .fch i{width:7px;height:7px;border-radius:50%;background:var(--c);flex:none}
#cpage .qwrap{padding-bottom:12px}
#cpage .sparks{position:static!important;display:flex!important;flex-wrap:wrap!important;overflow:visible!important;gap:6px 6px;margin:10px 0 0!important;padding:0!important;align-items:center;mask-image:none!important;-webkit-mask-image:none!important}
#cpage .sparks .sl{flex:none;font-size:12.5px;color:var(--mute);margin-right:2px}
#cpage .sparks button{height:30px;font-size:13px;padding:0 12px;white-space:nowrap;flex:none}
#cpage .cover .cvdrop{display:flex!important;align-items:center;justify-content:center;gap:10px;width:100%!important;height:67px;border:1.5px dashed var(--line)!important;border-radius:12px;background:none!important;color:var(--mute)!important}
#cpage .cover .cvdrop:hover,#cpage .cover.over .cvdrop{border-color:var(--teal)!important;color:var(--text)!important}
#cpage .cover .cvdrop svg{width:22px;height:22px}
@media (max-width:640px){#cpage .ntchips{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>'''
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-ctidy' in s: continue
    for a, b in REPS:
        assert s.count(a) == 1, (rel, a[:50], s.count(a)); s = s.replace(a, b)
    k = s.rindex('</body>'); s = s[:k] + CSS + s[k:]
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, flags=re.S)
    if m:
        d = json.loads(m.group(1)); d.update(T)
        s = s[:m.start(1)] + json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + s[m.end(1):]
    open(p, 'w', encoding='utf8').write(s); print(rel)
for f, line in (('help/dict-help.txt', 'Picture|Immagine|Imagen'), ('i18n/dict-el.txt', 'Picture|Εικόνα')):
    q = os.path.join(ROOT, f); e = open(q, encoding='utf8').read()
    if '\nPicture|' not in '\n' + e: open(q, 'w', encoding='utf8').write(e.rstrip('\n') + '\n' + line + '\n')
