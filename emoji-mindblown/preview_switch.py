# PREVIEW ONLY: adds "Emoji A | B | C" to the Live Table prototype bar so Karim can compare
# the three mind-blown options in place. Not for main once one is final.
import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
f = root / "live-table/timecapsule-live-table.html"
s = f.read_text()
if 'id="mbSeg"' in s: sys.exit("already")
def mini(p): return re.sub(r"\s*\n\s*", "", (root/"emoji-mindblown"/p).read_text()).replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg aria-hidden="true" ')
import json
opts = {"a": mini("a-burst.svg"), "b": mini("b-orbit.svg"), "c": mini("c-bubble.svg")}
seg = ('<label>Emoji <span class="seg" id="mbSeg"><button type="button" data-mb="a" aria-pressed="true">A Burst</button>'
       '<button type="button" data-mb="b" aria-pressed="false">B Orbit</button><button type="button" data-mb="c" aria-pressed="false">C Bubble</button></span></label>')
s = s.replace('<button type="button" class="pskip" id="skipEnd">', seg + '<button type="button" class="pskip" id="skipEnd">', 1)
js = ("<script>(function(){var O=" + json.dumps(opts) + ";var seg=document.getElementById('mbSeg');"
      "function set(k,pop){MB_SVG=O[k];document.querySelector('#myblown .mbico').innerHTML=O[k];"
      "seg.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.mb===k)});if(pop)mindBlown(ME)}"
      "seg.addEventListener('click',function(e){var b=e.target.closest('[data-mb]');if(b){set(b.dataset.mb,true);history.replaceState(null,'',location.pathname+location.search+'#emoji='+b.dataset.mb)}});"
      "var m=location.hash.match(/emoji=([abc])/);if(m)set(m[1],false)})();</script>")
s = s.replace("</body>", js + "</body>", 1) if "</body>" in s else s + js
f.write_text(s); print("ok")
