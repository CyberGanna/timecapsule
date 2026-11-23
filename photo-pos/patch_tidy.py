"""Karim 2026-11-22 "a bit messy": picture row in Create a table tidied.
Thumbnail on the left; on the right one quiet line "Drag the picture to choose what shows" and a small Remove link.
Idempotent, marker "tc-cvtidy". Run after photo-pos/patch.py."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['help/live-pages/agenda.html', 'help/live-pages/create.html', 'invite/pages/agenda.html', 'invite/pages/create.html']
T = {"Drag the picture to choose what shows.": ["Trascina l'immagine per scegliere cosa si vede.", "Arrastra la imagen para elegir qué se ve.", "Σύρε την εικόνα για να διαλέξεις τι φαίνεται."]}
OLD = ('`<div class="cvwrap"><div class="cvimg"><img src="${IMGS[nt.img]}" alt="Cover picture" draggable="false"></div><small class="cvhint">Drag to move</small></div>'
       '<div class="cvact"><!--tc-nochange--><button data-cv="rm">Remove</button></div>`')
NEW = ('`<div class="cvimg"><img src="${IMGS[nt.img]}" alt="Cover picture" draggable="false"></div>'
       '<div class="cvside"><!--tc-cvtidy--><p>Drag the picture to choose what shows.</p><button class="cvrm" data-cv="rm">Remove</button></div>`')
CSS = ('<style id="tc-cvtidy">.cvside{display:flex;flex-direction:column;align-items:flex-start;gap:4px;min-width:0}'
       '.cvside p{margin:0;font-size:13px;line-height:1.4;color:var(--mute,#A9B0D6)}'
       '.cover .cvrm{border:0;background:none;padding:0;font:inherit;font-size:13px;color:var(--text,#EEF1FF);text-decoration:underline;text-underline-offset:3px;text-decoration-color:rgba(238,241,255,.35);cursor:pointer}'
       '.cover .cvrm:hover{text-decoration-color:currentColor}'
       '.cover .cvimg{width:160px;height:67px!important}</style>')
for rel in FILES:
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read()
    if 'tc-cvtidy' in s: continue
    assert s.count(OLD) == 1, rel
    s = s.replace(OLD, NEW)
    k = s.rindex('</body>'); s = s[:k] + CSS + s[k:]
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, flags=re.S)
    if m:
        d = json.loads(m.group(1)); d.update(T)
        s = s[:m.start(1)] + json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + s[m.end(1):]
    open(p, 'w', encoding='utf8').write(s); print(rel)
for f, line in (('help/dict-help.txt', "Drag the picture to choose what shows.|Trascina l'immagine per scegliere cosa si vede.|Arrastra la imagen para elegir qué se ve."), ('i18n/dict-el.txt', 'Drag the picture to choose what shows.|Σύρε την εικόνα για να διαλέξεις τι φαίνεται.')):
    q = os.path.join(ROOT, f); e = open(q, encoding='utf8').read()
    if '\n' + line.split('|')[0] + '|' not in '\n' + e: open(q, 'w', encoding='utf8').write(e.rstrip('\n') + '\n' + line + '\n')
