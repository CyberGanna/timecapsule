import json,base64,os
H=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(H,"preview-src.html"),encoding="utf-8").read()
b=lambda f:"data:image/png;base64,"+base64.b64encode(open(os.path.join(H,f),"rb").read()).decode()
d=json.dumps(json.load(open(os.path.join(H,"preview-data.json"),encoding="utf-8")),ensure_ascii=False).replace("</","<\\/")
out=src.replace("/*DATA*/null",d).replace("/*LOGO*/",b("timecapsule-logo-email.png")).replace("/*COIN*/",b("timecoin.png"))
open(os.path.join(H,"timecapsule-emails.html"),"w",encoding="utf-8").write(out)
