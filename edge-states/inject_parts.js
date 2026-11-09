
/*AVATARS*/
P.Sofia=["#D9F8FA","#7C5CFF","#F1C9A5","#3A2A20","long"];
const $=s=>document.querySelector(s);
const U={agenda:'https://claude.ai/artifact/1HRtzD5kj8RFhEngLuAgU5',create:'https://claude.ai/artifact/MFBQwEDcUA8ctJbo2BWShj',people:'https://claude.ai/artifact/MTbRjvLFV7pPhBjpvAzXaq',invite:'https://claude.ai/artifact/3erX1TAL2xoYjAmfvqkWtp',settings:'https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy',search:'https://claude.ai/artifact/NdgohZznzHtQ8p2PmohNhE',mytables:'https://claude.ai/artifact/GPnp3CiH7iGDpkbqvA4cLB',guides:'https://claude.ai/artifact/WHk7qYCmXBgugxJW1kqevd',table:'https://claude.ai/artifact/AQKmmAgq8JPDsrRACWEy6i'};
const go=u=>{top.location.href=(window.TCI18N&&TCI18N.u)?TCI18N.u(u):u};
const T={Philosophy:'#F29BD0',Society:'#5FE0DE',Science:'#8BE38B',Books:'#E8B577',Psychology:'#B99BFF'};
const I={
 back:'<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M13 8H3M7 4L3 8l4 4"/></svg>',
 cols:'<svg viewBox="0 0 48 48"><path d="M8 18L24 9l16 9M10 18h28M13 22v13M20 22v13M28 22v13M35 22v13M9 39h30"/></svg>',
 bell:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></svg>',
 check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
 off:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="8.5"/><path d="M6 6l12 12"/></svg>',
 door:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4H6v16h8M10 12h10M17 9l3 3-3 3"/></svg>',
 note:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3.5h7l4 4V20.5H7z"/><path d="M14 3.5v4h4M10 12h5M10 16h5"/></svg>',
 shield:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5.5c0 4.5-3 7.7-7 9.5-4-1.8-7-5-7-9.5V6z"/><path d="M9 12l2 2 4-4"/></svg>',
 search:'<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
 seat:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="3.5" r="1.6"/><circle cx="12" cy="20.5" r="1.6"/><circle cx="3.5" cy="12" r="1.6"/><circle cx="20.5" cy="12" r="1.6"/></svg>',
 plus:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
 tshield:'<svg viewBox="0 0 12 12"><path d="M6 1l4 1.6v3c0 2.4-1.7 4.1-4 5.1-2.3-1-4-2.7-4-5.1v-3z" fill="#12304A"/><path d="M4.2 6l1.3 1.3L8 4.8" fill="none" stroke="#7FF0F2" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
};
const seatsAt=(n,r)=>Array.from({length:n},(_,i)=>{const a=-Math.PI/2+i*2*Math.PI/n;return[50+r*Math.cos(a),50+r*Math.sin(a)]});
function stage(people,off,cap){
 const pos=seatsAt(8,45);
 return `<div class="e-stage${off?' e-off':''}"><div class="e-tbg"></div><div class="e-ring"><div class="e-board">${I.cols}</div>${pos.map((p,i)=>{const n=people[i];return `<span class="e-seat${n?'':' e-ghost'}${i===0&&n?' e-host':''}" style="left:${p[0]}%;top:${p[1]}%">${n?av(n):''}</span>`}).join('')}</div><div class="e-cap">${cap}</div></div>`}
const host=`<div class="e-who"><span class="e-av">${av('Gregory')}</span><div><b>Gregory <span class="e-trust">${I.tshield}Trusted</span></b><small>Host · Switzerland</small></div></div>`;
const topic=t=>`<span class="e-tag"><i style="background:${T[t]}"></i>${t}</span>`;
const backL=`<a class="e-back" href="${U.agenda}" target="_top">${I.back}Back to tables</a>`;

/* art for centered states */
const tbl=(o={})=>{const n=o.n||6,cx=90,cy=78,R=56;let s='';for(let i=0;i<n;i++){const a=-Math.PI/2+i*2*Math.PI/n,x=cx+R*Math.cos(a),y=cy+R*Math.sin(a)*.78;const hi=o.hi===i;s+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="11" fill="${hi?'rgba(23,195,200,.18)':'#252B52'}" stroke="${hi?'#17C3C8':'#3A4175'}" stroke-width="2" ${hi?'':'stroke-dasharray="3 3"'}/>`}
 return `<svg viewBox="0 0 180 150" aria-hidden="true"><ellipse cx="90" cy="140" rx="70" ry="6" fill="rgba(0,0,0,.18)"/>${s}<ellipse cx="${cx}" cy="${cy}" rx="38" ry="30" fill="#20264A" stroke="#3A4175" stroke-width="2"/>${o.mid||''}</svg>`};
const ART={
 removed:`<svg viewBox="0 0 180 150" aria-hidden="true"><defs><linearGradient id="dl" x1="0" x2="1"><stop offset="0" stop-color="#17C3C8" stop-opacity=".35"/><stop offset="1" stop-color="#17C3C8" stop-opacity="0"/></linearGradient></defs><ellipse cx="90" cy="140" rx="64" ry="6" fill="rgba(0,0,0,.18)"/><path d="M62 26h48v104H62z" fill="url(#dl)" stroke="#3A4175" stroke-width="2" stroke-linejoin="round"/><path d="M62 26l-22 10v100l22-6z" fill="#252B52" stroke="#3A4175" stroke-width="2" stroke-linejoin="round"/><circle cx="48" cy="84" r="3" fill="#A9B0D6"/><path d="M110 130l34 6" stroke="rgba(23,195,200,.25)" stroke-width="10" stroke-linecap="round"/></svg>`,
 lost:tbl({n:6,mid:`<g transform="translate(70 52)"><circle cx="20" cy="22" r="20" fill="#7C5CFF"/><path d="M5 37l-5 10 13-5z" fill="#7C5CFF"/><text x="20" y="30" text-anchor="middle" font-size="24" font-weight="600" fill="#fff" font-family="Sora,sans-serif">?</text></g>`}),
 chair:tbl({n:6,hi:3}),
 day:tbl({n:6,mid:`<g transform="translate(76 64)" stroke="#17C3C8" stroke-width="3" stroke-linecap="round"><path d="M14 2v24M2 14h24"/></g>`}),
 follow:`<svg viewBox="0 0 180 150" aria-hidden="true"><ellipse cx="90" cy="140" rx="60" ry="6" fill="rgba(0,0,0,.18)"/><circle cx="66" cy="80" r="30" fill="#252B52" stroke="#3A4175" stroke-width="2" stroke-dasharray="4 4"/><circle cx="114" cy="80" r="30" fill="#252B52" stroke="#3A4175" stroke-width="2" stroke-dasharray="4 4"/><g transform="translate(118 18)"><circle cx="18" cy="18" r="18" fill="rgba(23,195,200,.16)"/><g transform="translate(6 6)" fill="none" stroke="#17C3C8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></g></g></svg>`,
 bell:`<svg viewBox="0 0 180 150" aria-hidden="true"><ellipse cx="90" cy="140" rx="50" ry="6" fill="rgba(0,0,0,.18)"/><circle cx="90" cy="72" r="56" fill="#20264A" stroke="#3A4175" stroke-width="2"/><g transform="translate(60 42) scale(2.5)" fill="none" stroke="#A9B0D6" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></g><text x="136" y="40" font-size="13" fill="#A9B0D6" font-family="Sora,sans-serif" opacity=".7">z</text><text x="146" y="28" font-size="10" fill="#A9B0D6" font-family="Sora,sans-serif" opacity=".5">z</text></svg>`,
 chats:`<svg viewBox="0 0 180 150" aria-hidden="true"><ellipse cx="90" cy="140" rx="60" ry="6" fill="rgba(0,0,0,.18)"/><g fill="none" stroke-width="2.5"><circle cx="70" cy="72" r="34" stroke="#7C5CFF"/><path d="M46 96l-12 22 26-10" stroke="#7C5CFF" stroke-linejoin="round"/><circle cx="114" cy="72" r="34" stroke="#17C3C8"/><path d="M138 48l12-22-26 10" stroke="#17C3C8" stroke-linejoin="round"/></g><g fill="#A9B0D6" opacity=".7"><circle cx="80" cy="72" r="3.5"/><circle cx="92" cy="72" r="3.5"/><circle cx="104" cy="72" r="3.5"/></g></svg>`
};
function solo(o){return `<section class="e-solo">${o.art?`<div class="e-art">${o.art}</div>`:''}<h1 class="e-h1">${o.h}</h1>${(o.p||[]).map(x=>`<p>${x}</p>`).join('')}${o.extra||''}<div class="e-acts">${o.acts}</div>${o.after||''}</section>`}
const A=(u,l,c)=>`<a class="${c||'e-btn e-pri'}" href="${u}" target="_top">${l}</a>`;

const SIM=[
 {t:'Today',h:'21:00',q:'What makes a life meaningful?',tp:'Philosophy',host:'Kofi',free:'3 of 8 chairs free'},
 {t:'Tomorrow',h:'18:30',q:'Can we disagree kindly?',tp:'Society',host:'Ruth',free:'2 of 6 chairs free'},
 {t:'Thu',h:'20:00',q:'Do we choose what we believe?',tp:'Philosophy',host:'Omar',free:'5 of 8 chairs free'}];
const simRows=()=>`<section class="e-more"><h2>Tables with free chairs</h2><p>Close to this one, by topic and time.</p><ul class="e-rows">${SIM.map((r,i)=>`<li class="e-rw"><div class="e-tm"><b>${r.h}</b><small>${r.t}</small></div><div class="e-tt"><b>${r.q}</b><div class="e-meta"><span>${topic(r.tp)}</span><span>${r.host} hosts</span><span>${r.free}</span></div></div><button class="e-btn e-sm e-go" type="button" data-save="${i}">Save a chair</button></li>`).join('')}</ul></section>`;

const S={
 full(){return `<div class="e-wrap">${backL}<div class="e-td">${stage(['Gregory','Lena','Omar','Mia','Priya','Kofi','Noah','Ruth'],0,'<b>8</b> at the table · no free chairs')}<div class="e-info"><div class="e-trow"><span class="e-when">Tomorrow · 19:00</span>${topic('Philosophy')}</div><h1 class="e-h1">Is free will an illusion?</h1>${host}
 <div class="e-note"><h2><span class="e-ni e-t">${I.seat}</span>This table is full</h2><p>All 8 chairs are taken. People sometimes give their chair back before it starts, so one may still open up.</p>
 <div class="e-acts" id="e-wl"><button class="e-btn e-pri" type="button" data-wl>${I.bell}Join the waitlist</button>${A(U.agenda,'See other tables','e-lnk')}</div>
 <p class="e-hint" id="e-wlh">${I.bell}If a chair opens, we ring your bell. The first person to take it gets the chair.</p></div></div></div>${simRows()}</div>`},
 cancelled(){return `<div class="e-wrap">${backL}<div class="e-td">${stage([],1,'Cancelled by the host')}<div class="e-info"><div class="e-trow"><span class="e-when e-x">Cancelled</span>${topic('Philosophy')}</div><h1 class="e-dim">Is free will an illusion?</h1>${host}
 <div class="e-note"><h2><span class="e-ni e-r">${I.off}</span>Gregory cancelled this table</h2><p class="e-say">Sorry everyone, I'm unwell tonight. Same question next Thursday, and I'll invite you first.<span class="e-by">Gregory, 2 hours ago</span></p><p>Your chair is free again. There's nothing you need to do.</p>
 <div class="e-acts">${A(U.agenda,'Find another table')}<button class="e-lnk" type="button" data-fol>Follow Gregory</button></div><p class="e-hint" id="e-folh" hidden>${I.bell}We'll tell you when Gregory hosts next.</p></div></div></div>${simRows()}</div>`},
 removed(){return `<div class="e-wrap">${solo({art:ART.removed,h:"You're no longer at this table",p:['The host removed you from “Is free will an illusion?”. You can’t rejoin this table.','Everything else stays as it was: your profile, your TimeCoins and your other tables.'],
 extra:`<div class="e-card"><span class="e-ni e-t">${I.note}</span><div><b>Your notes are safe</b><span>Anything you kept from this table is in My tables, and only you can see it.</span></div></div>`,
 acts:A(U.agenda,'See other tables')+`<button class="e-lnk" type="button" data-tell>Think it was a mistake? Tell us</button>`})}</div>`},
 '404'(){return `<div class="e-wrap">${solo({art:ART.lost,h:"We can't find this page",p:['The link may be old or mistyped, or the table may now be private.'],
 acts:A(U.agenda,'Back to tables'),
 after:`<form class="e-sform" id="e-sf" role="search"><label>${I.search}<input type="search" placeholder="Or search tables, people, topics" aria-label="Search"></label><button class="e-btn" type="submit">Search</button></form><span class="e-code">Error 404</span>`})}</div>`},
 'new-agenda'(){const D=['Today','Tomorrow','Thu','Fri','Sat','Sun','Mon'];return `<div class="e-wrap"><div class="e-hero"><h1 class="e-h1">Pull up a chair</h1><p>Small tables, real conversations. Pick a day.</p></div><div class="e-tabs e-days" id="e-days">${D.map(d=>`<button class="e-tb" type="button" aria-pressed="${d==='Sun'}">${d}</button>`).join('')}</div><hr class="e-rule"><div class="e-page-es">${solo({art:ART.day,h:'No tables on Sunday yet',p:['Be the first. Open a table, and people looking for Sunday will find it here.'],acts:A(U.create,I.plus+'Create a table')+`<button class="e-lnk" type="button" data-day="Today">See today's tables</button>`})}</div></div>`},
 'new-mytables'(){return `<div class="e-wrap"><div class="e-hero"><h1 class="e-h1">My tables</h1><p>The tables you host and the chairs you saved, with everything you need to run them.</p></div><div class="e-tabs" id="e-mtt"><button class="e-tb" type="button" aria-pressed="true" data-mt="up">Upcoming <small>0</small></button><button class="e-tb" type="button" aria-pressed="false" data-mt="past">Past <small>0</small></button></div><hr class="e-rule"><div class="e-page-es" id="e-mtb"></div></div>`},
 'new-following'(){return `<div class="e-wrap"><div class="e-hero"><h1 class="e-h1">Find your people</h1><p>Hosts and guests worth sitting with.</p></div><div class="e-tabs"><a class="e-tb" href="${U.people}" target="_top" style="text-decoration:none" aria-pressed="false">Discover</a><button class="e-tb" type="button" aria-pressed="true">Following <small>0</small></button></div><hr class="e-rule"><div class="e-page-es">${solo({art:ART.follow,h:"You're not following anyone yet",p:['Follow the people you enjoy talking with, and we’ll tell you when they host their next table.'],acts:A(U.people,'Discover people')+A(U.invite,'Invite a friend','e-lnk')})}</div></div>`},
 'new-notifications'(){return `<div class="e-wrap"><div class="e-hero"><h1 class="e-h1">Notifications</h1></div><div class="e-page-es">${solo({art:ART.bell,h:'All quiet for now',p:['When a table you saved is about to start, someone tips you, or a person you follow hosts, you’ll see it here.'],acts:A(U.agenda,'Find your first table')+A(U.settings+'#notifications','Choose what rings the bell','e-lnk')})}</div></div>`},
 'new-chats'(){return `<div class="e-wrap"><div class="e-hero"><h1 class="e-h1">Chats</h1></div><div class="e-page-es">${solo({art:ART.chats,h:'No chats yet',p:['Conversations often carry on after a table. You can message the people you sat with, or anyone from their profile.'],acts:A(U.agenda,'Find a table')})}</div></div>`},
 'new-profile'(){return `<div class="e-wrap"><section class="e-pf"><div class="e-bd"><button type="button" data-toast="Edit profile opens here">Change backdrop</button></div><div class="e-top"><span class="e-pav">${av('Sofia')}</span><div class="e-nm"><h1 class="e-h1">Sofia Marino</h1><small><span class="e-pill">New member</span>&nbsp; Milan, Italy · Joined today</small></div><div class="e-ed"><button class="e-btn e-sm" type="button" data-toast="Edit profile opens here">Edit profile</button></div></div>
 <div class="e-stats"><div><b>0</b><span>Tables</span></div><div><b>0</b><span>TimeCoins</span></div><div><b>0</b><span>Following</span></div></div>
 <div class="e-welcome"><div class="e-tx"><b>Your profile fills in as you talk</b><span>Tables, feedback and TimeCoins appear here after your first table.</span></div>${A(U.agenda,'Find your first table')}</div>
 <div class="e-pcols"><div><div class="e-ps"><h3>Talks about</h3><div class="e-chips"><span><i style="background:${T.Philosophy}"></i>Philosophy</span><span><i style="background:${T.Books}"></i>Books</span><span><i style="background:${T.Psychology}"></i>Psychology</span></div></div><div class="e-ps"><h3>My readings</h3><p class="e-em">The Overstory, Richard Powers</p></div><div class="e-ps"><h3>Ratings</h3><p class="e-em">No ratings yet. They come from the people you sit with.</p></div></div>
 <div><div class="e-ps"><h3>Tables</h3><p class="e-em">No tables yet. <a href="${U.agenda}" target="_top">Save your first chair</a> or <a href="${U.create}" target="_top">host one</a>.</p></div><div class="e-ps"><h3>Feedbacks</h3><p class="e-em">Kind words people leave after a table will show here.</p></div><div class="e-ps"><h3>Following</h3><p class="e-em">Nobody yet. <a href="${U.people}" target="_top">Find your people</a>.</p></div></div></div></section></div>`}
};
const MT={up:{art:ART.chair,h:'No tables yet',p:['Save a chair at any table on the Tables page, or host your own. They’ll wait for you here.'],acts:A(U.agenda,'Find a table')+A(U.create,'Create a table','e-lnk')},
 past:{art:tbl({n:6}),h:'Nothing here yet',p:['After your first table, you’ll find it here with its transcript and the notes you kept.'],acts:A(U.agenda,'Find a table')}};

function mt(k){$('#e-mtb').innerHTML=solo(MT[k]);document.querySelectorAll('[data-mt]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.mt===k))}
let tt;function toast(m){const t=$('#e-toast');t.textContent=m;t.classList.add('e-on');clearTimeout(tt);tt=setTimeout(()=>t.classList.remove('e-on'),2600)}
function onClick(e){
 const w=e.target.closest('[data-wl]');
 if(w){const on=w.classList.toggle('e-ok');w.classList.toggle('e-pri',!on);w.innerHTML=on?I.check+"You're on the waitlist":I.bell+'Join the waitlist';toast(on?"You're on the waitlist":'You left the waitlist');return}
 const f=e.target.closest('[data-fol]');
 if(f){const on=f.dataset.on!=='1';f.dataset.on=on?'1':'0';f.textContent=on?'Following Gregory':'Follow Gregory';$('#e-folh').hidden=!on;return}
 const sv=e.target.closest('[data-save]');
 if(sv){const on=!sv.classList.contains('e-ok');sv.classList.toggle('e-ok',on);sv.innerHTML=on?I.check+'Chair saved':'Save a chair';if(on)toast('Chair saved. See you there.');return}
 if(e.target.closest('[data-tell]')){$('#e-scrim').hidden=false;setTimeout(()=>$('#e-sh-x').focus(),30);return}
 const d=e.target.closest('[data-day]');
 if(d){document.querySelectorAll('#e-days .e-tb').forEach(b=>b.setAttribute('aria-pressed',TCI18N.src(b).trim()===d.dataset.day));toast('On the real Tables page, today’s tables show here');return}
 const dd=e.target.closest('#e-days .e-tb');
 if(dd){document.querySelectorAll('#e-days .e-tb').forEach(b=>b.setAttribute('aria-pressed',b===dd));return}
 const m=e.target.closest('[data-mt]');if(m){mt(m.dataset.mt);return}
 const ts=e.target.closest('[data-toast]');if(ts){toast(ts.dataset.toast);return}
}
function onSubmit(e){if(e.target.id!=='e-sf')return;e.preventDefault();const q=e.target.querySelector('input').value.trim();go(U.search+(q?'#q='+encodeURIComponent(q):''))}
const closeS=()=>{$('#e-scrim').hidden=true};
$('#e-sh-c').onclick=closeS;$('#e-scrim').addEventListener('click',e=>{if(e.target.id==='e-scrim')closeS()});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('#e-scrim').hidden)closeS()});
$('#e-sh-s').onclick=()=>{closeS();$('#e-sh-x').value='';toast('Thanks. We’ll read it and get back to you by email.')};
