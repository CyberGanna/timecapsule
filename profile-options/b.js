(function(){
 var side=document.querySelector('.lbside');
 var secs=[...side.querySelectorAll(':scope>section.lbsec')].filter(s=>!s.classList.contains('lbreads'));
 var tabs=document.querySelector('.lbtabs .tabs');
 var panel=document.createElement('section');panel.id='p-about';panel.className='panel';panel.hidden=true;panel.setAttribute('role','tabpanel');
 secs.forEach(s=>{var c=s.cloneNode(true);c.removeAttribute('style');c.style.display='grid';panel.appendChild(c)});
 var first=document.querySelector('.lbtabs .panel');first.before(panel);
 var btn=document.createElement('button');btn.type='button';btn.setAttribute('role','tab');btn.id='t-about';btn.textContent='About';btn.setAttribute('aria-selected','false');
 tabs.prepend(btn);
 document.querySelectorAll('.lbtabs .tabs b').forEach(b=>b.remove());
 btn.addEventListener('click',function(){tabs.querySelectorAll('button').forEach(x=>x.setAttribute('aria-selected',x===btn?'true':'false'));document.querySelectorAll('.lbtabs .panel').forEach(p=>p.hidden=p!==panel)});
 tabs.querySelectorAll('button:not(#t-about)').forEach(x=>x.addEventListener('click',function(){panel.hidden=true;btn.setAttribute('aria-selected','false')}));
 btn.click();
})();
