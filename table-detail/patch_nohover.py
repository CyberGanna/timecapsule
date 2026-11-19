"""Table page: person pop-up opens on click only, no hover (Karim 2026-11-19). Idempotent."""
import sys
for f in sys.argv[1:] or ["table-detail/timecapsule-table.html","help/live-pages/table.html","invite/pages/table.html"]:
    s=open(f).read(); a='const HOV=matchMedia("(hover:hover)").matches;'
    if a in s: s=s.replace(a,'const HOV=false; /* click only (Karim 2026-11-19) */',1); open(f,'w').write(s); print('patched',f)
    else: print('unchanged',f)
