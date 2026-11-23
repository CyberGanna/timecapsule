"""Topic icons (Karim 2026-11-22): History = scroll (option C), Religion = prayer beads (option B).
Craft keeps the hammer. Replaces the TICON paths in every page and patch file. Idempotent."""
import os, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = {
 '<path d="M6 3h12M6 21h12M7 3c0 5 5 6 5 9s-5 4-5 9M17 3c0 5-5 6-5 9s5 4 5 9"/>':
 '<path d="M7 5.5A2.5 2.5 0 0 1 9.5 3H19a2 2 0 0 1 0 4h-2.5v11.5A2.5 2.5 0 0 1 14 21H5a2 2 0 0 1 0-4h2z"/><path d="M5 17h9.5a2 2 0 0 1-.5 4M10.5 8.5h3M10.5 12h3"/>',
 '<path d="M12 8.5v12M12 8.5C10 7.3 7 7 3.5 7.5v11.5c3.5-.5 6.5-.2 8.5 1M12 8.5c2-1.2 5-1.5 8.5-1v11.5c-3.5-.5-6.5-.2-8.5 1M12 2.5v2.5M8 3.5l1 1.8M16 3.5l-1 1.8"/>':
 '<circle cx="12" cy="9.5" r="6.5" style="stroke-dasharray:0 3.4;stroke-width:2.6;stroke-linecap:round"/><path d="M12 16v3.2M10.3 21l1.7-1.8 1.7 1.8"/>',
}
files = subprocess.run(['grep', '-rlF', '-e', list(REP)[0], '-e', list(REP)[1], '--include=*.html', '--include=*.py', '--include=*.js', '.'],
                       cwd=ROOT, capture_output=True, text=True).stdout.split()
for rel in files:
    if rel.endswith('topic-icons/apply.py'): continue
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf8').read(); n = s
    for a, b in REP.items(): n = n.replace(a, b)
    if n != s: open(p, 'w', encoding='utf8').write(n); print(rel)
