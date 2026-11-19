"""Karim 2026-11-19: "TimeCoins received" label is too long -> "Tips" (gold number = TimeCoins received). Run after patch.py. Idempotent."""
import re,json,subprocess
FILES=subprocess.run("grep -rlF '<dt>TimeCoins received</dt>' --include=*.html --include=*.js .",shell=True,capture_output=True,text=True).stdout.split()
T={"Tips":["Mance","Propinas","Φιλοδωρήματα"]}
for f in FILES:
    s=open(f).read()
    s=s.replace('<dt>TimeCoins received</dt>','<dt title="TimeCoins received">Tips</dt>')
    m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
    if m and '"Tips":[' not in s: s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k),json.dumps(v,ensure_ascii=False)) for k,v in T.items())+s[m.end():]
    open(f,'w').write(s);print('tips',f)
