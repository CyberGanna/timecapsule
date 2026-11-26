# Live Table, host view: "Later" on a guest's question now KEEPS it (decided 2026-11-23).
# It moves into a "Saved for later" list at the TOP of the Chat tab (under new questions,
# above messages), where the host can still "Ask the table" or remove it.
# Re-run after rebuilding the Live Table. Idempotent.
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
f = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "live-table/timecapsule-live-table.html"
s = f.read_text()
if "qlater" in s: print("already patched"); sys.exit()
def rep(a, b):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b, 1)
rep('window.TCI18N_DICT={', 'window.TCI18N_DICT={"Later":["Più tardi","Más tarde","Αργότερα"],"Saved for later":["Salvate per dopo","Guardadas para después","Αποθηκευμένες για αργότερα"],', )
rep("</style>", """
/* saved-for-later questions (host) */
.qlater{border:1px solid var(--line);border-radius:14px;background:var(--surface)}
.qlater>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:8px;padding:9px 12px;font-size:12.5px;font-weight:600;color:var(--soft)}
.qlater>summary::-webkit-details-marker{display:none}
.qlater>summary b{min-width:18px;height:18px;padding:0 5px;border-radius:9px;background:var(--raise);color:var(--fg);font-size:11px;display:inline-grid;place-items:center}
.qlater>summary::after{content:"";margin-left:auto;width:7px;height:7px;border-right:1.6px solid var(--mute);border-bottom:1.6px solid var(--mute);transform:rotate(45deg) translateY(-2px);transition:transform .15s}
.qlater[open]>summary::after{transform:rotate(-135deg) translateY(-1px)}
.qlater .ql{border-top:1px solid var(--line);padding:9px 12px;font-size:13.5px;line-height:1.45}
.qlater .ql small{display:block;font-size:11px;color:var(--mute);margin-bottom:2px}
.qlater .row{display:flex;gap:8px;margin-top:8px}
.qlater .row button{flex:1;height:30px;border-radius:9px;font-size:12px;font-weight:500}
</style>""")
rep('const S={role:"guest",', 'const S={later:[],laterOpen:true,role:"guest",')
# render the later list after the new questions
rep('''    <div class="row"><button type="button" class="ghost" data-qi="${i}" data-qa="done">Later</button><button type="button" class="gold" data-qi="${i}" data-qa="ask">Ask the table</button></div></div>`).join("");''',
    '''    <div class="row"><button type="button" class="ghost" data-qi="${i}" data-qa="done">Later</button><button type="button" class="gold" data-qi="${i}" data-qa="ask">Ask the table</button></div></div>`).join("")
    +(S.role==="mod"&&S.later.length?`<details class="qlater"${S.laterOpen?" open":""}><summary><span>Saved for later</span><b>${S.later.length}</b></summary>${S.later.map((x,i)=>`<div class="ql"><small>${x.from} · ${x.at}</small>${esc(x.t)}
    <div class="row"><button type="button" class="ghost" data-li="${i}" data-la="rm">Remove</button><button type="button" class="gold" data-li="${i}" data-la="ask">Ask the table</button></div></div>`).join("")}</details>`:"");''')
rep('''  if(q.length)document.querySelector("#msgs .empty")?.remove();''',
    '''  if(q.length||(S.role==="mod"&&S.later.length))document.querySelector("#msgs .empty")?.remove();
  const d=box.querySelector(".qlater"); if(d)d.addEventListener("toggle",()=>S.laterOpen=d.open);''')
rep('''  const b=e.target.closest("[data-qa]"); if(!b)return;
  const x=S.questions.splice(+b.dataset.qi,1)[0];
  if(b.dataset.qa==="ask"){showBanner(x.from,x.t,ME); sys(`You asked a question from ${x.from}`);}''',
    '''  const l=e.target.closest("[data-la]");
  if(l){const x=S.later.splice(+l.dataset.li,1)[0]; if(l.dataset.la==="ask"){showBanner(x.from,x.t,ME); sys(`You asked a question from ${x.from}`);} renderQin(); return;}
  const b=e.target.closest("[data-qa]"); if(!b)return;
  const x=S.questions.splice(+b.dataset.qi,1)[0];
  if(b.dataset.qa==="ask"){showBanner(x.from,x.t,ME); sys(`You asked a question from ${x.from}`);}
  if(b.dataset.qa==="done"){S.later.unshift(x); S.laterOpen=true;}''')
f.write_text(s); print("patched", f)
