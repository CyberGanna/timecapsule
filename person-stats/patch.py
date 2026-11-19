"""Karim 2026-11-19: person stats everywhere (pop-up preview, profile header, Rate and tip host preview)
= Tables · Conversations · TimeCoins received (was Tables · Feedbacks · TimeCoins). Idempotent; run on built pages and sources."""
import re,sys,json,subprocess
FILES=sys.argv[1:] or subprocess.run("grep -rlE 'dt>Feedbacks</dt' --include=*.html --include=*.js .",shell=True,capture_output=True,text=True).stdout.split()
PAT=re.compile(r'<dd>(\$\{(?:fmt\()?u\.feedbacks\)?\}|[\d,]+)</dd><dt>Feedbacks</dt>(</div>\s*<div[^>]*><dd class="gold"[^>]*>.*?</dd>)<dt>TimeCoins</dt>',re.S)
def conv(v):
    if v.startswith('${'):
        f='fmt(' in v
        return '${'+('fmt(' if f else '')+'u.convs!=null?u.convs:Math.round((u.tables||0)*.6)'+(')' if f else '')+'}'
    return ('<b class="lbc-o">12</b><b class="lbc-v">11</b>' if PROFILE else '11') if v=='48' else str(round(int(v.replace(',',''))*.6))
T={"Conversations":["Conversazioni","Conversaciones","Συζητήσεις"],"TimeCoins received":["TimeCoins ricevuti","TimeCoins recibidos","TimeCoins που έλαβε"]}
for f in FILES:
    s=open(f).read();o=s;PROFILE='lbstats' in s
    s=PAT.sub(lambda m:'<dd>'+conv(m.group(1))+'</dd><dt>Conversations</dt>'+m.group(2)+'<dt>TimeCoins received</dt>',s)
    s=s.replace('title="Your TimeCoins">','title="TimeCoins received">')
    if s!=o:
        m=re.search(r'window\.TCI18N_DICT\s*=\s*\{',s)
        if m: s=s[:m.end()]+''.join('%s:%s,'%(json.dumps(k),json.dumps(v,ensure_ascii=False)) for k,v in T.items() if '"%s":['%k not in s)+s[m.end():]
        if PROFILE and 'lbstats dd b' not in s: s=s.replace('.lbstats .gold{','body:not(.visitor) .lbstats .lbc-v,body.visitor .lbstats .lbc-o{display:none}.lbstats dd b{font-weight:inherit}.lbstats .gold{',1)
        open(f,'w').write(s);print('patched',f,len(PAT.findall(o)))
# pop-up: longer labels need tighter tracking and a centred wrap
R='.tcp dt{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#A9B0D6}'
for f in subprocess.run("grep -rlF '"+R+"' --include=*.html --include=*.js .",shell=True,capture_output=True,text=True).stdout.split():
    s=open(f).read()
    if '.tcp dt{letter-spacing:.06em' in s: continue
    s=s.replace(R,R+'\n.tcp dt{letter-spacing:.06em;text-align:center;line-height:1.3;padding:0 4px}');open(f,'w').write(s);print('css',f)
