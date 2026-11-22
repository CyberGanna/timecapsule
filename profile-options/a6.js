(function(){
 var rows=document.querySelector('.opt-rows'),tabs=document.querySelector('.lbtabs .tabs'),lb=document.getElementById('t-lb'),view=document.getElementById('uniview');
 if(!rows||!tabs||!lb||!view)return;
 // make sure the map shows Readings
 var rb=document.querySelector('.unitog button[data-m="read"]');if(rb&&rb.getAttribute('aria-pressed')!=='true')rb.click();
 var panel=document.createElement('section');panel.id='p-rd';panel.className='panel';panel.hidden=true;panel.setAttribute('role','tabpanel');panel.setAttribute('aria-labelledby','t-rd');
 panel.appendChild(rows);
 var first=document.getElementById('p-lb');first.before(panel);
 var btn=document.createElement('button');btn.type='button';btn.setAttribute('role','tab');btn.id='t-rd';btn.setAttribute('aria-selected','false');btn.setAttribute('aria-controls','p-rd');btn.textContent='Readings';
 lb.before(btn);
 function show(){tabs.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-selected',x===btn?'true':'false')});document.querySelectorAll('.lbtabs .panel').forEach(function(p){p.hidden=p!==panel})}
 btn.addEventListener('click',show);
 tabs.querySelectorAll('button').forEach(function(x){if(x!==btn)x.addEventListener('click',function(){panel.hidden=true;btn.setAttribute('aria-selected','false')})});
 // a planet opens the Readings tab (A3 then opens and scrolls to its topic)
 ['click','keydown'].forEach(function(t){view.addEventListener(t,function(e){var g=e.target.closest&&e.target.closest('g.bk');if(g&&(t==='click'||e.key==='Enter'||e.key===' '))show()},true)});
 var cap=document.createElement('p');cap.className='opt-hint';cap.textContent='Tap a planet to see its books.';view.after(cap);
})();
