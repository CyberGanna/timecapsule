"""Karim 2026-11-22: on the host's Table page, Invite people sits next to Start table,
same size, sharing the card width; Host tools keep Edit and Cancel. Idempotent, marker "tc-hinv".
Run after patch_mytables_link.py."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'table-detail/timecapsule-table.html')
s = open(P, encoding='utf8').read()
if 'tc-hinv' not in s:
    a = '<div class="acts2"><button class="btn go" data-act="start"${near?"":" disabled"}>Start table</button></div>'
    INV = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10" cy="8" r="4"/><path d="M3 20c0-3.9 3.1-6 7-6s7 2.1 7 6M19 8v6M16 11h6"/></svg>'
    b = ('<div class="acts2 hinv"><!--tc-hinv--><button class="btn" data-act="invite">' + INV +
         '<span>Invite people</span></button><button class="btn go" data-act="start"${near?"":" disabled"}>Start table</button></div>')
    old_tool = '<button type="button" data-act="invite">' + INV + '<span>Invite people</span></button>'
    for x in (a, old_tool):
        assert s.count(x) == 1, x[:60]
    s = s.replace(a, b).replace(old_tool, '')
    s = s.replace('</style>', '.acts2.hinv{display:grid;grid-template-columns:1fr 1fr;gap:12px}.acts2.hinv .btn{width:100%}.acts2.hinv svg{fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}</style>', 1)
    open(P, 'w', encoding='utf8').write(s); print('host invite moved')
