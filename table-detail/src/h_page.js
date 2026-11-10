/* ---------- links ---------- */
const URL_AGENDA="https://claude.ai/artifact/1HRtzD5kj8RFhEngLuAgU5";
const URL_LIVE="https://claude.ai/artifact/2CoEp7SXhBT2oP5hu3zNkk";
const URL_CHATS="https://claude.ai/artifact/PYd4f8xrcNkPc2TyPkE4ib";
const URL_SIGNIN="https://claude.ai/artifact/BFBabdFxq8LxqDChfvRn61";
const URL_ONB="https://claude.ai/artifact/Q7o5JaMGP7bHLXzJ6aw6TH";
const URL_GREG="https://claude.ai/artifact/TQ3edAr7Dje1uPbGk3yEQy";
const URL_MYT="https://claude.ai/artifact/GPnp3CiH7iGDpkbqvA4cLB";
const tt=s=>s;

/* ---------- data ---------- */
const TOPIC_C={Philosophy:"#F29BD0",Memoir:"#E8B577",Science:"#8BE38B",History:"#E8B577"};
const TICON={
 Philosophy:'<path d="M4 20h16M5 17h14M6 17V9m4 8V9m4 8V9m4 8V9M4 9h16L12 4z"/>',
 Memoir:'<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3zM5 17a3 3 0 0 1 3-3h11M9 8h6"/>'};
const PROF={
 Gregory:["Switzerland","Philosophy teacher. Hosts the free will table.",["Philosophy"],2023,true],
 Mia:["France","Writes letters she never sends. Hosts small circles.",["Philosophy","Memoir"],2024,false],
 Omar:["Morocco","Neuroscience PhD, part-time skeptic.",["Philosophy","Science"],2025,false],
 Priya:["India","Product manager, slow traveller.",["Philosophy"],2024,false],
 Lena:["Germany","Engineer. Asks the second question.",["Science"],2024,false],
 Tom:["Ireland","Retired electrician. Duct tape optimist.",["Science"],2025,false],
 Yuki:["Japan","Writes short stories about choices.",["Philosophy","Memoir"],2024,false],
 Elif:["Turkey","Musician. Thinks in rhythms.",["Philosophy"],2025,false],
 Ana:["Spain","Ceramicist. Learning to be patient.",["Memoir"],2024,false]
};
const TABLES={
 open:{title:"Is free will an illusion?",topic:"Philosophy",host:"Gregory",seats:8,lang:"English",transcript:true,
   people:["Gregory","Mia","Omar","Priya","Lena","Tom"],talk:"Omar",slug:"free-will-gregory",
   desc:"Neuroscience says the brain decides before we notice. Philosophy says we are still responsible. We start from Libet’s experiment and ask what freedom could mean if it holds. No reading needed, just curiosity and a willingness to change your mind."},
 inv:{title:"What would you tell your twenty-year-old self?",topic:"Memoir",host:"Mia",seats:6,lang:"English",transcript:false,
   people:["Mia","Yuki","Elif","Ana"],talk:"Yuki",slug:"i/8kq2-mia",
   desc:"A small, unhurried circle. Each of us brings one thing we learned the hard way, and one thing we are still not sure about. No host, we take turns.",
   note:"Gabriele, a small group, mostly people from the Camus table. I’d love to have your voice in it."}
};

/* ---------- state ---------- */
const st={kind:"open",time:"later",auth:"in",saved:false,accepted:false,declined:false,startAt:0,liveSince:0};
(function(){const h=(location.hash||"").replace(/^#/,"").split(/[&,]/);
  if(h.includes("invite"))st.kind="inv"; if(h.includes("live"))st.time="live"; if(h.includes("out")||h.includes("signedout"))st.auth="out";})();
function setTimes(){const now=Date.now();
  st.startAt=Math.ceil((now+134*60000)/3e5)*3e5; /* about 2h 15m from now, on a 5-minute mark */
  st.liveSince=now-41*60000;}
setTimes();
const T=()=>TABLES[st.kind];
const isLive=()=>st.time==="live";
const isOut=()=>st.auth==="out";
const hasChair=()=>st.kind==="open"?st.saved:st.accepted;

/* ---------- helpers ---------- */
const hhmm=d=>`${String(d.getHours()).padStart(2,"0")}:${String(d.getMinutes()).padStart(2,"0")}`;
const DAYS=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],MON=["January","February","March","April","May","June","July","August","September","October","November","December"];
function dayLabel(d){const a=new Date(d);a.setHours(0,0,0,0);const b=new Date();b.setHours(0,0,0,0);const k=Math.round((a-b)/864e5);return k===0?"Today":k===1?"Tomorrow":DAYS[d.getDay()]}
function longDate(d){return `${DAYS[d.getDay()]}, ${d.getDate()} ${MON[d.getMonth()]}`}
const I={
 cal:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.7" stroke-linecap="round"><path d="M4 7H20V20H4ZM4 11H20M9 3V7M15 3V7"/></svg>',
 time:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.7" stroke-linecap="round"><path d="M12 7V12L15 14M21 12A9 9 0 1 1 3 12A9 9 0 0 1 21 12"/></svg>',
 fmt:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="3.5"/><circle cx="12" cy="3.8" r="1.6"/><circle cx="19.1" cy="16.1" r="1.6"/><circle cx="4.9" cy="16.1" r="1.6"/></svg>',
 lang:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.6"><path d="M3 12H21M12 3C15 6 15 18 12 21M12 3C9 6 9 18 12 21M21 12A9 9 0 1 1 3 12A9 9 0 0 1 21 12"/></svg>',
 seat:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.7"><path d="M12 21A9 9 0 1 0 12 3A9 9 0 0 0 12 21ZM12 15A3 3 0 1 0 12 9A3 3 0 0 0 12 15Z"/></svg>',
 doc:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h7l4 4v14H7zM14 3v4h4M10 12h5M10 16h5"/></svg>',
 lock:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/></svg>',
 share:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 15V3M7 8l5-5 5 5M5 13v7h14v-7"/></svg>',
 link:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1 1M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1-1"/></svg>',
 chat:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/></svg>',
 mail:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6l8.5 7 8.5-7"/></svg>',
 ok:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
 ear:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.7" stroke-linecap="round"><path d="M7 9a5 5 0 0 1 10 0c0 3-3 4-3 7a3 3 0 0 1-5.5 1.6M10 9.5a2 2 0 0 1 4 0"/></svg>',
 cam:'<svg viewBox="0 0 24 24" fill="none" stroke="#A9B0D6" stroke-width="1.7" stroke-linejoin="round"><path d="M3 7H15V17H3ZM15 10L21 7V17L15 14"/></svg>',
 coin:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5" fill="none" stroke="#F2C14E" stroke-width="1.7"/><circle cx="12" cy="12" r="4.5" fill="#F2C14E" opacity=".35"/></svg>'
};
const SHIELD='<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1.5l5 2v4c0 3.2-2.1 5.7-5 7-2.9-1.3-5-3.8-5-7v-4z" fill="#12304A"/><path d="M5.6 8.1l1.7 1.7 3.2-3.4" fill="none" stroke="#7FF0F2" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
let tst; function toast(s){const el=document.getElementById("toast");el.textContent=s;el.classList.add("on");clearTimeout(tst);tst=setTimeout(()=>el.classList.remove("on"),2600)}

/* ---------- render ---------- */
function people(){const t=T(),p=[...t.people];if(hasChair()&&!isOut())p.push("You");return p}
function ringHTML(){
  const t=T(),n=t.seats,ppl=people(),hide=isOut()||(st.kind==="inv"&&!st.accepted);
  let s="";
  for(let i=0;i<n;i++){
    const a=-Math.PI/2+i*2*Math.PI/n,x=50+44*Math.cos(a),y=50+44*Math.sin(a),p=ppl[i];
    if(!p){s+=`<span class="seat open" style="left:${x}%;top:${y}%" aria-hidden="true"></span>`;continue}
    if(hide){s+=`<span class="seat ghost" style="left:${x}%;top:${y}%" aria-hidden="true"></span>`;continue}
    s+=`<span class="seat${i===0?" host":""}${isLive()&&p===t.talk?" talk":""}" style="left:${x}%;top:${y}%"${p!=="You"?` data-u="${p}" tabindex="0"`:""}>${av(p)}</span>`;
  }
  return `<div class="ring"><div class="board"><svg class="ticon" viewBox="0 0 24 24" aria-hidden="true">${TICON[t.topic]}</svg></div>${s}</div>`;
}
function genBg(c){return `<div class="tbg" style="background:radial-gradient(45% 65% at 18% 30%,${c}99,transparent 70%),radial-gradient(50% 70% at 85% 75%,#7C5CFF80,transparent 70%),radial-gradient(40% 55% at 70% 12%,#17C3C855,transparent 70%),radial-gradient(45% 65% at 25% 95%,${c}5c,transparent 70%),#252B52"></div>`}

function statusRow(){
  const t=T(),c=TOPIC_C[t.topic];let s="";
  if(isLive()) s+=`<span class="lpill"><i></i><span>LIVE</span> · <span class="lmin">${Math.round((Date.now()-st.liveSince)/60000)} min</span></span>`;
  else{const d=new Date(st.startAt);s+=`<span class="spill">${dayLabel(d)} · ${hhmm(d)}</span>`}
  s+=`<span class="topic" style="--c:${c}"><i></i>${t.topic}</span>`;
  if(st.kind==="inv") s+=`<span class="ppill">${I.lock}<span>Private</span></span>`;
  return `<div class="trow">${s}</div>`;
}
function hostRow(){
  const t=T(),p=PROF[t.host];
  return `<div class="host"><span class="hav" data-u="${t.host}" tabindex="0">${av(t.host)}</span><div>
    <div class="hn"><b data-u="${t.host}">${t.host}</b>${p[4]?`<span class="tchip" title="Trusted host">${SHIELD}<span>Trusted</span></span>`:""}</div>
    <small>Host · ${p[0]}</small></div></div>`;
}
function factsHTML(){
  const t=T(),start=isLive()?new Date(st.liveSince):new Date(st.startAt),end=new Date(+start+60*60000);
  const free=t.seats-people().length;
  const when=isLive()?`<dd>Started at <b style="font-weight:inherit">${hhmm(start)}</b><span>Ends around <b style="font-weight:inherit">${hhmm(end)}</b></span></dd>`
    :`<dd>${longDate(start)}<span>${hhmm(start)} – ${hhmm(end)} · ${tt("your time")}</span></dd>`;
  return `<dl class="facts2">
   <div>${I.cal}<div><dt>When</dt>${when}</div></div>
   <div>${I.seat}<div><dt>Chairs</dt><dd>${free===0?"Table full":free+" of "+t.seats+" chairs free"}<span>${"Small on purpose, so everyone is heard."}</span></dd></div></div>
   <div>${I.lang}<div><dt>Language</dt><dd>${t.lang}<span>${"60 minutes"}</span></dd></div></div>
   <div>${I.doc}<div><dt>Transcript</dt><dd>${t.transcript?"Kept":"Not kept"}<span>${t.transcript?"It goes public only if everyone at the table agrees.":"Nothing is recorded or written down."}</span></dd></div></div>
   ${st.kind==="inv"?`<div>${I.lock.replace('currentColor','#A9B0D6')}<div><dt>Who can join</dt><dd>Private<span>Only people with the invite link. It isn't on the Tables page.</span></dd></div></div>`
     :`<div>${I.coin}<div><dt>TimeCoins</dt><dd>8 to give<span>After the table, tip the people who inspired you.</span></dd></div></div>`}
  </dl>`;
}
function cdHTML(){
  if(isLive()) return `<div class="cd live" id="cd"><span class="lab">Talking for</span><span class="u"><b id="cdm">0</b><small>min</small></span></div>`;
  return `<div class="cd" id="cd"><span class="lab">Starts in</span><span class="u"><b id="cdh">0</b><small>h</small></span><span class="u"><b id="cdmn">00</b><small>min</small></span><span class="u"><b id="cds">00</b><small>sec</small></span></div>`;
}
function tick(){
  const now=Date.now();
  if(isLive()){const m=Math.round((now-st.liveSince)/60000);const a=document.getElementById("cdm");if(a)a.textContent=m;document.querySelectorAll(".lmin").forEach(x=>x.textContent=m+" min");return}
  let s=Math.max(0,Math.round((st.startAt-now)/1000));const h=Math.floor(s/3600),m=Math.floor(s%3600/60),sec=s%60;
  const a=document.getElementById("cdh");if(!a)return;a.textContent=h;document.getElementById("cdmn").textContent=String(m).padStart(2,"0");document.getElementById("cds").textContent=String(sec).padStart(2,"0");
}
setInterval(tick,1000);

function actionsHTML(){
  const t=T();
  if(isOut()){
    const inv=st.kind==="inv";
    return `<div class="gate"><h3>${inv?"Sign in to accept your invite":"Sign in to take a chair"}</h3>
      <p>${inv?"Your invite is kept. Once you're in, we bring you straight back to this table.":"It takes about a minute. We bring you straight back to this table."}</p>
      <div class="acts2"><a class="btn vi" href="${URL_ONB}" target="_top">Create your account</a><a class="btn" href="${URL_SIGNIN}" target="_top">Sign in</a></div>
      <p style="margin-top:14px;font-size:12.5px">We never sell or mine your data. You can join with a first name or an alias.</p></div>`;
  }
  const share=st.kind==="open"?`<button class="btn" data-act="share">${I.share}<span>Share</span></button>`:"";
  if(st.kind==="inv"&&!st.accepted){
    if(st.declined) return `<div class="acts2"><button class="btn go" data-act="accept">Accept invite</button></div><p class="hint">You told ${t.host} you can't make it. Changed your mind? You can still accept until the table starts.</p>`;
    return `<div class="acts2"><button class="btn go" data-act="accept">Accept invite</button><button class="lnk" data-act="decline">Not this time</button></div>
      <p class="hint">${isLive()?"The table has started. Accept to join the call.":"Accepting saves your chair. "+t.host+" sees that you're coming."}</p>`;
  }
  if(isLive()){
    return `<div class="acts2"><button class="btn go" data-act="join">Join table</button>${share}</div>
      <p class="hint"><span>${hasChair()?"Your chair is waiting.":"You check your camera and microphone first."}</span> <span>Listen first, then speak in turns.</span></p>`;
  }
  if(hasChair()){
    return `<div class="acts2"><button class="btn on" data-act="saved" aria-pressed="true">${I.ok}<span>Chair saved</span></button><a class="btn" data-act="ics" href="#" >${I.cal.replace('#A9B0D6','currentColor')}<span>Add to calendar</span></a>${share}</div>
      <p class="hint">We'll remind you 10 minutes before. <button class="lnk" data-act="giveup" style="padding:0">Give up my chair</button></p>`;
  }
  return `<div class="acts2"><button class="btn go" data-act="save">Save a chair</button>${share}</div>
    <p class="hint">Free. You can give your chair back anytime before the table starts.</p>`;
}
function inviteHTML(){
  if(st.kind!=="inv") return "";
  const t=T();
  let head,body;
  if(st.accepted){head=`You're coming to ${t.host}'s table`;body=`<p class="priv">${I.ok}<span>${"Your chair is saved. It's also in My tables."}</span></p>`}
  else if(st.declined){head=`You declined ${t.host}'s invite`;body=""}
  else{head=`${t.host} invited you to a table`;body=`<p class="note">${t.note}</p>`}
  return `<section class="inv${st.accepted?" done":""}${st.declined?" no":""}"><span class="iav" data-u="${t.host}" tabindex="0">${av(t.host)}</span><div class="it">
    <h2>${head}</h2>${body}
    <p class="priv">${I.lock}<span>${"Private table. It isn't on the Tables page, and only people with this link can see it."} ${"Please don't forward it: ask "+t.host+" if you'd like to bring someone."}</span></p></div></section>`;
}
function whoHTML(){
  const t=T(),ppl=people(),free=t.seats-ppl.length;
  if(isOut()||(st.kind==="inv"&&!st.accepted)){
    return `<h2>Who's coming <small>${ppl.length} / ${t.seats}</small></h2><div class="lock"><span class="dots">${ppl.slice(0,4).map(()=>"<i></i>").join("")}</span><span>${isOut()?"Sign in to see who's coming.":"You'll see who's coming once you accept."}</span></div>`;
  }
  const rows=ppl.map((p,i)=>{
    if(p==="You") return `<li class="me"><span class="pa">${av("You")}</span><div><b style="cursor:default">You</b><small>Gabriele</small></div></li>`;
    const pr=PROF[p]||["",""];const role=i===0?"Host":"";
    return `<li><span class="pa" data-u="${p}" tabindex="0">${av(p)}</span><div><b data-u="${p}">${p}</b><small>${role?`<i class="mt">${role}</i> · `:""}${pr[0]}</small></div></li>`}).join("");
  const frees=Array.from({length:Math.min(free,2)},()=>`<li class="free"><span class="pa"></span><div><b>Free chair</b></div></li>`).join("");
  return `<h2>${isLive()?"At the table":"Who's coming"} <small>${ppl.length} / ${t.seats}</small></h2><ul class="who2">${rows}${frees}</ul>`;
}
function goodHTML(){
  const t=T();
  return `<h2>Good to know</h2><ul class="gk">
   <li>${I.ear}<div><b>Listen first</b>Speak in turns and leave a little silence. Anyone can raise a hand.</div></li>
   <li>${I.cam}<div><b>Camera on, if you can</b>Faces make it a real table. You can join with an alias instead of your name.</div></li>
   <li>${I.time}<div><b>One hour</b>Arrive a minute early. Late arrivals wait for a pause to be let in.</div></li>
  </ul>`;
}
function render(){
  const t=T(),c=TOPIC_C[t.topic];
  document.body.classList.toggle("out",isOut());
  document.title=t.title+" · TimeCapsule";
  document.getElementById("page").innerHTML=`
   <a class="back" href="${URL_AGENDA}" target="_top">← Back to tables</a>
   ${inviteHTML()}
   <section class="td">
    <div class="stage${isLive()?" live":""}" style="--c:${c}">${genBg(c)}${ringHTML()}<p class="cap"><b>${people().length}</b> ${tt("at the table")} · ${t.seats-people().length} ${tt("free")}</p></div>
    <div class="info">
     ${statusRow()}
     <h1>${t.title}</h1>
     <p class="desc">${t.desc}</p>
     ${hostRow()}
     ${cdHTML()}
     ${actionsHTML()}
    </div>
   </section>
   ${factsHTML()}
   <section class="low"><div>${whoHTML()}</div><div>${goodHTML()}</div></section>`;
  tick();
  document.querySelectorAll(".proto [data-k]").forEach(b=>b.setAttribute("aria-pressed",st[b.dataset.k]===b.dataset.v));
}

/* ---------- person pop-up (shared .tcp card) ---------- */
const TCP_FOLLOW=new Set();
const TCP_CHAT='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>';
const TCP_ADD='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10" cy="8" r="4"/><path d="M3 20c0-3.9 3.1-6 7-6s7 2.1 7 6M19 8v6M16 11h6"/></svg>';
const TCP_OK='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>';
function tcpFollowBtn(n){const on=TCP_FOLLOW.has(n);return `<button type="button" class="tcpf${on?" on":""}" data-f="${n}" aria-pressed="${on}">${on?TCP_OK+"Following":TCP_ADD+"Follow"}</button>`}
function tcpHTML(u){
  const meta=[u.role,u.place,u.since?"Member since "+u.since:""].filter(Boolean).join(" · ");
  return `<div class="tcpbd" aria-hidden="true"></div>
  <div class="tcph"><span class="tcpav">${u.avatar||""}</span><div class="tcpw"><div class="tcpn"><b>${u.name}</b>${u.trusted?`<span class="tcpt" title="Trusted">${SHIELD}Trusted</span>`:""}</div>${meta?`<p class="tcpm">${meta}</p>`:""}</div></div>
  ${u.bio?`<p class="tcpb">${u.bio}</p>`:""}
  ${u.topics&&u.topics.length?`<div class="tcptg">${u.topics.map(([t,c])=>`<span style="--c:${c||"#A9B0D6"}"><i></i>${t}</span>`).join("")}</div>`:""}
  <dl><div><dd>${u.tables}</dd><dt>Tables</dt></div><div><dd>${u.feedbacks}</dd><dt>Feedbacks</dt></div><div><dd class="gold">${u.coins}</dd><dt>TimeCoins</dt></div></dl>
  <div class="tcpa">${u.profile?`<a class="pf" href="${u.profile}" target="_top">View profile</a>`:`<span style="margin-right:auto"></span>`}<a class="ic" href="${URL_CHATS}" target="_top" aria-label="Chat with ${u.name}" title="Chat">${TCP_CHAT}</a>${tcpFollowBtn(u.name)}</div>`;
}
document.addEventListener("click",e=>{const b=e.target.closest(".tcpf");if(!b)return;e.preventDefault();e.stopPropagation();const n=b.dataset.f;TCP_FOLLOW.has(n)?TCP_FOLLOW.delete(n):TCP_FOLLOW.add(n);b.outerHTML=tcpFollowBtn(n)},true);
const UC=document.createElement("div");UC.className="ucard tcp";UC.hidden=true;UC.setAttribute("role","dialog");document.body.appendChild(UC);
let ucFor=null,ucT;
function showU(el){
  const n=el.dataset.u,p=PROF[n]||["","",[],2025,false];ucFor=el;const h=[...n].reduce((a,c)=>a+c.charCodeAt(0),0);
  const host=n===T().host;
  UC.innerHTML=tcpHTML({name:n,avatar:av(n),trusted:p[4],role:host?"Host":"",place:p[0],since:p[3],bio:p[1],
    topics:p[2].map(x=>[x,TOPIC_C[x]]),tables:h%40+6,feedbacks:h%23+3,coins:p[4]?412:h%90+15,profile:n==="Gregory"?URL_GREG:""});
  UC.hidden=false;
  const r=el.getBoundingClientRect(),w=UC.offsetWidth,hh=UC.offsetHeight;
  let x=r.left+r.width/2-w/2;x=Math.max(12,Math.min(x,innerWidth-w-12));
  let y=r.bottom+8;if(y+hh>innerHeight-12)y=r.top-hh-8;
  UC.style.left=x+"px";UC.style.top=Math.max(12,y)+"px";
}
function hideU(){UC.hidden=true;ucFor=null}
const HOV=matchMedia("(hover:hover)").matches;
if(HOV){document.addEventListener("mouseover",e=>{const el=e.target.closest("[data-u]");if(el){clearTimeout(ucT);if(ucFor!==el)showU(el)}else if(!e.target.closest(".ucard")&&ucFor){clearTimeout(ucT);ucT=setTimeout(hideU,180)}})}
document.addEventListener("click",e=>{const el=e.target.closest("[data-u]");if(el){e.preventDefault();ucFor===el&&!HOV?hideU():showU(el);return}if(!e.target.closest(".ucard"))hideU()});
document.addEventListener("keydown",e=>{if(e.key==="Escape")hideU();if((e.key==="Enter"||e.key===" ")&&e.target.dataset&&e.target.dataset.u){e.preventDefault();showU(e.target)}});
addEventListener("scroll",()=>{if(!UC.hidden)hideU()},{passive:true});

/* ---------- alias (same as Tables) ---------- */
const ACOL=["#7C5CFF","#17C3C8","#F4A6D7","#FF9E8A","#7CC8FF","#E9F27A"];
const TAKEN=new Set(Object.keys(P).map(x=>x.toLowerCase()).concat(["blue comet","admin","host"]));
const me={mode:"name",alias:"",col:ACOL[0]};
const KBOOKS=[["Zarathustra","Thus Spoke Zarathustra","Nietzsche"],["Happy Sisyphus","The Myth of Sisyphus","Camus"],["Owl of Minerva","Phenomenology of Spirit","Hegel"],["Knight of Faith","Fear and Trembling","Kierkegaard"],["Dasein","Being and Time","Heidegger"],["Golden Mean","Nicomachean Ethics","Aristotle"],["Cave Dweller","The Republic","Plato"],["Inner Citadel","Meditations","Marcus Aurelius"]];
const KB=Object.fromEntries(KBOOKS.map(k=>[k[0],k]));
function rndAlias(){const f=KBOOKS.filter(k=>!TAKEN.has(k[0].toLowerCase()));return f[Math.random()*f.length|0][0]}
function mono(name,col,size){const ini=(name.trim().split(/\s+/).map(w=>w[0]||"").join("").slice(0,2)||"?").toUpperCase();
  return `<svg class="mono" viewBox="0 0 64 64" role="img" aria-label="${name}" style="width:${size}px;height:${size}px;border-radius:50%;display:block"><rect width="64" height="64" fill="${col}"/><text x="32" y="40" text-anchor="middle" font-family="Sora,sans-serif" font-size="22" font-weight="500" fill="#121633">${ini}</text></svg>`}
function checkAlias(v){v=v.trim();if(v.length<2)return[false,"At least 2 characters."];if(v.length>20)return[false,"20 characters at most."];
  if(!/^[\p{L}\p{N} ._-]+$/u.test(v))return[false,"Letters, numbers, spaces, dots and dashes only."];if(TAKEN.has(v.toLowerCase()))return[false,`“${v}” is taken. Try another.`];return[true,"Nice, it's free."]}
function aliasHTML(){return `<div class="opt"><label class="l">Show me at the table as</label>
  <div class="seg" role="group"><button aria-pressed="${me.mode==="name"}" data-as="name">Gabriele</button><button aria-pressed="${me.mode==="alias"}" data-as="alias">An alias</button></div>
  <div class="alias" id="alias" ${me.mode==="alias"?"":"hidden"}>
    <div class="prev"><span id="apv"></span><div><small>Others will see you as</small><b id="apn"></b></div></div>
    <div class="ain"><label for="ain" style="position:absolute;left:-9999px">Alias</label><input id="ain" maxlength="24" autocomplete="off" placeholder="Type an alias"><button id="adice" title="Suggest one" aria-label="Suggest an alias">⚄</button></div>
    <div class="amsg" id="amsg"></div><div class="sugg" id="sugg"></div>
    <div class="cols" role="group" aria-label="Colour">Colour ${ACOL.map(c=>`<button data-col="${c}" style="background:${c}" aria-pressed="${me.col===c}" aria-label="Colour"></button>`).join("")}</div>
    <p class="anote">Only the host can see it's you. Your alias is kept for your next tables, and you can change it anytime.</p>
  </div></div>`}
function wireAlias(){if(!me.alias)me.alias=rndAlias();document.getElementById("ain").value=me.alias;fillSugg();updAlias();document.getElementById("ain").addEventListener("input",updAlias)}
function fillSugg(){const s=new Set();while(s.size<4)s.add(rndAlias());
  document.getElementById("sugg").innerHTML=`<span class="kfrom">Ideas from your <b>k▪universe</b></span>`+[...s].map(a=>`<button data-sugg="${a}" title="${KB[a][1]} · ${KB[a][2]}">${a}<small>${KB[a][1]}</small></button>`).join("")}
function updAlias(){const inp=document.getElementById("ain");if(!inp)return;const v=inp.value,[ok,msg]=checkAlias(v),m=document.getElementById("amsg");
  m.textContent=msg;m.className="amsg "+(ok?"good":"bad");inp.classList.toggle("bad",!ok);
  document.getElementById("apv").innerHTML=mono(v||"?",me.col,44);document.getElementById("apn").textContent=v.trim()||"…";if(ok)me.alias=v.trim();
  const c=document.getElementById("confirm")||document.getElementById("enter");if(c){const dis=me.mode==="alias"&&!ok;c.toggleAttribute("aria-disabled",dis);c.style.opacity=dis?.45:1;c.style.pointerEvents=dis?"none":""}
  paintCam()}

/* ---------- sheets ---------- */
let cur=null,lastFocus=null;
const cam={video:true,mic:true,blur:false,stream:null};
function sumHTML(){const t=T();return `<div class="thumb"><div style="width:100%;height:100%;background:radial-gradient(circle at 35% 30%,${TOPIC_C[t.topic]},#20264A)"></div></div><div class="si"><b>${t.title}</b><small>${t.topic}</small></div>`}
function openScrim(cls,html,focusSel){
  lastFocus=document.activeElement;cur=T();
  const sh=document.getElementById("sheet");sh.className="sheet "+cls;sh.style.setProperty("--c",TOPIC_C[T().topic]);sh.innerHTML=html;
  const sc=document.getElementById("scrim");sc.hidden=false;requestAnimationFrame(()=>sc.classList.add("on"));
  const f=focusSel&&document.querySelector(focusSel);if(f)f.focus({preventScroll:true});
}
function openJoin(){
  const t=T();
  openScrim("join",`<button class="x" data-close aria-label="Close">×</button>
    <div class="jg"><div class="jl">
    <div class="pv" id="pv"><video id="vid" autoplay playsinline muted></video><div class="fake" id="fake"></div><div class="off" id="off"></div><div class="tagme" id="tagme"></div><div class="lvl" id="lvl" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div></div>
    <div class="ctl">
      <button class="cb on" data-cam="mic" aria-pressed="true" aria-label="Microphone"><svg viewBox="0 0 24 24"><path d="M12 3A3 3 0 0 0 9 6V12A3 3 0 0 0 15 12V6A3 3 0 0 0 12 3ZM5 11A7 7 0 0 0 19 11M12 18V21" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path class="sl" d="M4 4L20 20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>Mic</span></button>
      <button class="cb on" data-cam="video" aria-pressed="true" aria-label="Camera"><svg viewBox="0 0 24 24"><path d="M3 7H15V17H3ZM15 10L21 7V17L15 14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path class="sl" d="M4 4L20 20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>Camera</span></button>
      <button class="cb" data-cam="blur" aria-pressed="false" aria-label="Blur background"><svg viewBox="0 0 24 24"><circle cx="12" cy="9" r="3.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 20C6 15.5 9 14 12 14C15 14 18 15.5 19 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="4" cy="5" r="1" fill="currentColor"/><circle cx="20" cy="5" r="1" fill="currentColor"/><circle cx="3" cy="11" r="1" fill="currentColor"/><circle cx="21" cy="11" r="1" fill="currentColor"/></svg><span>Blur</span></button>
    </div></div><div class="jr">
    <div class="shd"><span class="badge live" style="margin-bottom:12px"><span class="blink"></span>LIVE · <b class="lmin" style="font-weight:inherit">${Math.round((Date.now()-st.liveSince)/60000)} min</b></span><h2 id="sh-t">Ready to join?</h2></div>
    <div class="sum">${sumHTML()}</div>
    <div class="who" style="margin-top:16px"><span class="ppl">${t.people.slice(1,7).map(p=>`<span>${av(p)}</span>`).join("")}</span><span>${t.people.length-1} people talking with ${t.host}</span></div>
    ${aliasHTML()}
    <p class="anote" style="margin-top:16px">Listen first and speak in turns. The host can mute anyone to keep the table calm.</p>
    <div class="acts"><button class="cta" data-close>Not now</button><a class="cta go" id="enter" href="${URL_LIVE}" target="_top">Join the table</a></div></div></div>`,"#enter");
  wireAlias();paintCam();startCam();
}
async function startCam(){try{if(!navigator.mediaDevices?.getUserMedia)throw 0;cam.stream=await navigator.mediaDevices.getUserMedia({video:true,audio:true});if(!cur){stopCam();return}
  const v=document.getElementById("vid");v.srcObject=cam.stream;document.getElementById("pv").classList.add("real")}catch(e){}}
function stopCam(){if(cam.stream){cam.stream.getTracks().forEach(x=>x.stop());cam.stream=null}}
function paintCam(){const pv=document.getElementById("pv");if(!pv)return;
  const name=me.mode==="alias"?(me.alias||"Alias"):"Gabriele";const face=me.mode==="alias"?mono(name,me.col,96):av("You");
  document.getElementById("fake").innerHTML=`<div class="room"></div><div class="selfie">${face}</div>`;
  document.getElementById("off").innerHTML=`<div class="offav">${me.mode==="alias"?mono(name,me.col,84):av("You")}</div><span>Camera is off</span>`;
  document.getElementById("tagme").innerHTML=`${cam.mic?"":'<b class="mut">🔇</b>'}${name}`;
  pv.classList.toggle("vidoff",!cam.video);pv.classList.toggle("blur",cam.blur);pv.classList.toggle("micoff",!cam.mic);
  document.querySelectorAll(".cb").forEach(b=>{const k=b.dataset.cam,on=cam[k];b.classList.toggle("on",on);b.setAttribute("aria-pressed",on)});
  if(cam.stream){cam.stream.getVideoTracks().forEach(x=>x.enabled=cam.video);cam.stream.getAudioTracks().forEach(x=>x.enabled=cam.mic)}}
function openSave(){
  const t=T(),d=new Date(st.startAt),left=t.seats-people().length;
  openScrim("",`<button class="x" data-close aria-label="Close">×</button>
    <div class="shd"><h2 id="sh-t">Save a chair</h2><p class="sub">${left+" of "+t.seats+" chairs free"}</p></div>
    <div class="sum">${sumHTML()}</div>
    <p class="sub" style="margin-top:10px">${longDate(d)} · ${hhmm(d)}</p>
    ${aliasHTML()}
    <label class="tog">Remind me 10 minutes before<input type="checkbox" id="rem" checked></label>
    <label class="tog">Add to my calendar<input type="checkbox" id="cal"></label>
    <div class="coinnote"><i></i>After the table you get 8 TimeCoins to award the people who inspired you.</div>
    <div class="acts"><button class="cta" data-close>Cancel</button><button class="cta go" id="confirm">Save my chair</button></div>`,"#confirm");
  wireAlias();
}
function shareURL(){return "https://timecapsule.app/t/"+T().slug}
function openShare(){
  const t=T();
  openScrim("sh2",`<button class="x" data-close aria-label="Close">×</button>
    <div class="shd"><h2 id="sh-t">Share this table</h2><p class="sub">${t.title}</p></div>
    <div class="lf"><input id="surl" readonly value="${shareURL()}" aria-label="Link to this table"><button class="btn go" id="scopy">${I.link}<span>Copy link</span></button></div>
    <div class="sopts">
      <a href="${URL_CHATS}" target="_top">${I.chat}<span>Send in a chat</span></a>
      <a href="mailto:?subject=${encodeURIComponent(t.title)}&body=${encodeURIComponent("Pull up a chair with me: "+shareURL())}" target="_top">${I.mail}<span>Email</span></a>
      <button type="button" id="snative">${I.share}<span>More</span></button>
    </div>
    <p class="fine">Anyone with the link can see this table. They need a TimeCapsule account to take a chair.</p>`,"#scopy");
}
function openDecline(){
  const t=T();
  openScrim("sh2",`<button class="x" data-close aria-label="Close">×</button>
    <div class="shd"><h2 id="sh-t">Decline the invite?</h2><p class="sub">${t.host+" will see you can't make it this time. You can still change your mind until the table starts."}</p></div>
    <div class="acts two"><button class="cta" data-close>Keep the invite</button><button class="cta go" id="dodecline">Decline</button></div>`,"#dodecline");
}
function openGiveUp(){
  openScrim("sh2",`<button class="x" data-close aria-label="Close">×</button>
    <div class="shd"><h2 id="sh-t">Give up your chair?</h2><p class="sub">Your chair is free for someone else.</p></div>
    <div class="acts two"><button class="cta" data-close>Keep it</button><button class="cta go" id="dogiveup">Give up chair</button></div>`,"#dogiveup");
}
function closeSheet(){stopCam();const sc=document.getElementById("scrim");sc.classList.remove("on");setTimeout(()=>{sc.hidden=true},220);cur=null;if(lastFocus&&document.contains(lastFocus))lastFocus.focus()}
function copy(){const v=shareURL();let ok=false;try{const i=document.getElementById("surl");i.select();ok=document.execCommand("copy")}catch(e){}
  if(navigator.clipboard&&!ok){navigator.clipboard.writeText(v).then(()=>toast(tt("Link copied")),()=>toast(tt("Link copied")))}else toast(tt("Link copied"))}
document.getElementById("scrim").addEventListener("click",e=>{
  if(e.target.id==="scrim"){closeSheet();return}
  const b=e.target.closest("button,a");if(!b)return;
  if(b.id==="enter"){/* plain link to the Live Table; let it navigate */return}
  if(b.tagName==="A")return;
  e.stopPropagation();
  if(b.id==="confirm"){st.saved=true;const as=me.mode==="alias"?me.alias:"Gabriele";closeSheet();render();toast(tt("Your chair is saved"));return}
  if(b.id==="scopy"){copy();return}
  if(b.id==="snative"){if(navigator.share){navigator.share({title:T().title,url:shareURL()}).catch(()=>{})}else copy();return}
  if(b.id==="dodecline"){st.declined=true;closeSheet();render();toast(tt("We let "+T().host+" know"));return}
  if(b.id==="dogiveup"){st.saved=false;closeSheet();render();toast(tt("Your chair is free for someone else."));return}
  if(b.dataset.cam){cam[b.dataset.cam]=!cam[b.dataset.cam];paintCam();return}
  if(b.dataset.as){me.mode=b.dataset.as;b.parentNode.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",x===b));document.getElementById("alias").hidden=me.mode!=="alias";updAlias();if(me.mode==="alias")document.getElementById("ain").focus();return}
  if(b.id==="adice"){document.getElementById("ain").value=rndAlias();fillSugg();updAlias();return}
  if(b.dataset.sugg){document.getElementById("ain").value=b.dataset.sugg;updAlias();return}
  if(b.dataset.col){me.col=b.dataset.col;b.parentNode.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",x===b));updAlias();return}
  if(b.hasAttribute("data-close"))closeSheet();
});
document.addEventListener("keydown",e=>{if(e.key==="Escape"&&cur)closeSheet()});

/* ---------- page actions ---------- */
document.getElementById("page").addEventListener("click",e=>{
  const b=e.target.closest("[data-act]");if(!b)return;e.preventDefault();
  const a=b.dataset.act;
  if(a==="join")openJoin();
  else if(a==="save")openSave();
  else if(a==="share")openShare();
  else if(a==="accept"){st.accepted=true;st.declined=false;render();toast(tt(isLive()?"You're in. Join when you're ready.":"Your chair is saved"))}
  else if(a==="decline")openDecline();
  else if(a==="giveup")openGiveUp();
  else if(a==="saved")toast(tt("Your chair is saved"));
  else if(a==="ics")toast(tt("Added to your calendar"));
});
document.querySelector(".proto").addEventListener("click",e=>{
  const b=e.target.closest("[data-k]");if(!b)return;st[b.dataset.k]=b.dataset.v;
  if(b.dataset.k==="kind"){st.saved=false;st.accepted=false;st.declined=false}
  setTimes();render();
});
/* header search: go to the Tables page */
(function(){const ins=document.querySelectorAll("#tch input[type=search]");ins.forEach(i=>i.addEventListener("keydown",e=>{if(e.key==="Enter"){top.location.href=TCI18N.u(URL_AGENDA)}}))})();
render();
addEventListener("tc-lang",()=>render());
