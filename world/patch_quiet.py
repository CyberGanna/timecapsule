# Speech boxes on the globe step aside while you use it (hover, drag, tap, scroll)
# and come back after 3.5 s without interaction. Gentle fade both ways.
import sys
FILES = sys.argv[1:] or ["world/timecapsule-world.html", "landing/world-base.html",
  "landing/timecapsule-landing.html", "landing/timecapsule-landing-artifact.html", "help/live-pages/world.html"]
A = "let captioned=new Set();"
A2 = A + "\nlet QT=-1e9,QA=1,QL=performance.now();const QUIET=3500;"
B = "  const FOCT=LIS.T;\n"
B2 = B + "  {const qd=Math.min(80,now-QL);QL=now;const qt=now-QT<QUIET?0:1;QA+=(qt-QA)*Math.min(1,qd/(qt?450:160));if(QA<.003)QA=0;if(QA>.997)QA=1}\n"
C = "    if(!box)continue;\n    shownNow.add(b.T);"
C2 = "    if(!box)continue;\n    if(!QA)continue;\n    shownNow.add(b.T);"
D = "    ctx.globalAlpha=a;\n"
D2 = "    ctx.globalAlpha=a*QA;\n"
E = 'cv.addEventListener("pointerleave",'
E2 = '["pointermove","pointerdown","wheel","touchstart","touchmove"].forEach(ev=>cv.addEventListener(ev,()=>{QT=performance.now()},{passive:true}));\n' + E
for f in FILES:
    s = open(f, encoding="utf8").read()
    if "const QUIET=" in s:
        print("already", f); continue
    for o, n in [(A, A2), (B, B2), (C, C2), (D, D2), (E, E2)]:
        assert s.count(o) == 1, (f, o)
        s = s.replace(o, n)
    open(f, "w", encoding="utf8").write(s)
    print("patched", f)
