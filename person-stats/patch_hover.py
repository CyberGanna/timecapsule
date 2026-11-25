"""Gabriele 2026-11-19: one hover for every stat link: a soft box, label turns white (was teal text on two, gold box on Tips). Idempotent."""
import subprocess
def files(p): return subprocess.run("grep -rlF '"+p+"' --include=*.html --include=*.js .",shell=True,capture_output=True,text=True).stdout.split()
R=[('.lbstats .lbsl{cursor:pointer}.lbstats .lbsl:hover dd,.lbstats .lbsl:hover dt{color:#17C3C8}','.lbstats .lbsl{cursor:pointer;position:relative}.lbstats .lbsl,.lbstats .coinstat{border-radius:0!important;background:none!important}.lbstats .lbsl::before,.lbstats .coinstat::before{content:"";position:absolute;inset:-4px 6px;border-radius:8px;pointer-events:none}.lbstats .lbsl:hover::before,.lbstats .coinstat:hover::before{background:rgba(255,255,255,.06)}.lbstats .lbsl:hover dt,.coinstat:hover dt{color:#EEF1FF!important}'),
   ('.tcp dl a.tcpn:hover dd,.tcp dl a.tcpn:hover dt{color:#17C3C8}','.tcp dl a.tcpn{padding:4px 0;margin:-4px 2px}.tcp dl a.tcpn:hover{background:rgba(255,255,255,.06)}.tcp dl a.tcpn:hover dt{color:#EEF1FF}'),
   ('.lbpst a.lbpn:hover dd,.lbpst a.lbpn:hover dt{color:#17C3C8}','.lbpst a.lbpn{border-radius:8px;padding:4px 0;margin:-4px 2px}.lbpst a.lbpn:hover{background:rgba(255,255,255,.06)}.lbpst a.lbpn:hover dt{color:#EEF1FF}')]
for a,b in R:
    for f in files(a):
        s=open(f).read().replace(a,b);open(f,'w').write(s);print(f)
for f in ['person-stats/patch_links.py']:
    s=open(f).read()
    for a,b in R: s=s.replace(a,b)
    open(f,'w').write(s)
