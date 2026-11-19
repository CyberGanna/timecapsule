"""Rate and tip pop-up: calmer top (Karim 2026-11-19, "this part is a mess").
Header = "Table ended" + close only (no truncated "Thanks for joining", language switch moved to the
page corner, hidden inside My tables); table block centred without the gradient box. Idempotent."""
import sys
FILES=sys.argv[1:] or ["rate-tip/timecapsule-rate-tip.html","help/live-pages/mytables.html","invite/pages/mytables.html"]
CSS='''<style id="tc-rt-clean">
.rtpop .ph{border-bottom:0!important;padding-bottom:0!important;background:transparent!important}
.rtpop .ph .pt{display:none!important}
.rtpop .ph .ended{margin-right:auto}
@media (min-width:601px){.rtpop .ph .tc-lp{position:fixed;top:14px;right:16px;z-index:200;margin:0!important}}
@media (max-width:600px){.rtpop .ph .tc-lp{margin:0 4px 0 0!important}}
.embed .rtpop .ph .tc-lp{display:none!important}
.rtpop .card.tbl{background:transparent!important;border:0!important;border-bottom:1px solid var(--line)!important;border-radius:0!important;box-shadow:none!important;padding:2px 0 14px!important}
.rtpop .card.tbl .ttl{flex-direction:column!important;text-align:center!important;gap:10px!important}
.rtpop .card.tbl .topic{width:56px!important;height:56px!important}
.rtpop .card.tbl h1{font-size:22px!important;line-height:1.25!important;letter-spacing:-.4px!important}
.rtpop .card.tbl .sub{display:block!important;margin-top:4px!important;font-size:13px!important;color:var(--mute)!important}
.rtpop .card.tbl .sep{display:inline!important}
.rtpop .card.tbl .mod{border-top:0!important;margin-top:6px!important;padding-top:0!important}
.rtpop .card.tbl .mod summary{justify-content:center!important;color:var(--mute)!important;min-height:32px!important}
.rtpop .card.tbl .mod summary>span:not(.mini):not(.caret){flex:none!important}
.rtpop .card.tbl .mod summary .caret{margin-left:6px!important;transform-origin:center}
.rtpop .card.tbl .mod summary b{color:var(--text)}
.rtpop .card.tbl .caret{border-color:var(--mute)!important}
</style>'''
for f in FILES:
    s=open(f).read()
    if 'id="tc-rt-clean"' in s: print('unchanged',f); continue
    a='<header class="ph">'; assert a in s,f
    s=s.replace(a,CSS+a,1); open(f,'w').write(s); print('patched',f)
