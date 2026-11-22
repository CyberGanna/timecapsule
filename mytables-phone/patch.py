"""My tables on phones: a calmer, shorter row (Karim 2026-11-22, "Way too busy on mobile. Let's simplify.").
Phones only (max-width 640px); desktop and tablet unchanged.
- Date and time on one small line at the top, with the ... menu at its right.
- No coloured topic icon tile; the title uses the full width.
- Topic and role stay on one small line under the title.
- No avatar stack; only the short people line (e.g. "5 guests · Not saved").
- Main button at the top right, beside the date, with ... after it, so every action sits
  in the same spot on the right edge like the desktop column (Karim 2026-11-22, option A).
- The prototype switch at the bottom drops its PROTOTYPE label and gets smaller.
Idempotent: re-run after any rebuild of My tables (after my-tabs/patch.py).  python3 mytables-phone/patch.py
"""
import os, re
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'help', 'live-pages', 'mytables.html')
CSS = """<style id="tc-mtphone">@media (max-width:640px){
body .row{grid-template-columns:minmax(0,1fr) auto;grid-template-areas:"t a" "i i" "p p";gap:0;padding:16px 0 18px;align-items:start}
body .row .tm{grid-area:t;display:flex;align-items:baseline;gap:6px;flex-wrap:wrap;align-self:center;font-size:13px;color:var(--mute);min-height:0}
body .row .tm b{font-size:13px;font-weight:500;color:var(--soft)}
body .row .tm.lv b{color:var(--green,#4ADE80)}
body .row .tm span{font-size:13px}
body .row .tm span::before{content:"·";margin-right:6px}
body .row .ei{gap:0;margin-top:10px}
body .row .ei .th{display:none}
body .row .et h3{font-size:17px;line-height:1.3;margin:0 0 6px}
body .row .meta{font-size:12.5px;gap:4px 10px}
body .row .role{font-size:11px}
body .row .ppl{margin-top:8px;gap:0}
body .row .ppl .fc{display:none}
body .row .ppl small{font-size:13px}
body .row .act{display:flex;grid-area:a;align-items:center;gap:2px;justify-self:end;margin:0}
body .row .act .btn{margin:0;height:34px;padding:0 12px;font-size:13px}
body .row .act .more{width:30px;height:30px;margin:0 -6px 0 0}
.e-chip{transform:scale(.86);transform-origin:left bottom}
.e-chip>:not(.e-seg){display:none}
}</style>"""
s = open(P, encoding='utf-8').read()
s = re.sub(r'<style id="tc-mtphone">.*?</style>', '', s, flags=re.S)
i = s.rfind('</body>'); assert i > 0
open(P, 'w', encoding='utf-8').write(s[:i] + CSS + s[i:]); print('patched mytables.html')
