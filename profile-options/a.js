(function(){
 var tags=document.getElementById('herotags'),meta=document.querySelector('.lbmeta'),nm=document.querySelector('.lbname'),bio=document.getElementById('bio');
 if(meta&&nm)nm.after(meta);
 if(tags&&bio)bio.after(tags);
 // ratings as tappable chips; each one filters the list you are looking at (Received or Given)
 var hb=[...document.querySelectorAll('.hist button')];
 var P=document.getElementById('p-fb'),sw=P&&P.querySelector('.fbsw'),gl=P&&P.querySelector('.list.given');
 if(sw&&hb.length){
  var box=document.createElement('div');box.className='opt-rchips';box.setAttribute('role','group');box.setAttribute('aria-label','Filter by rating');
  var gcur=null,giv=function(){return P.classList.contains('giv')};
  var gapply=function(){if(!gl)return;gl.querySelectorAll('li.fb').forEach(function(li){li.hidden=!!gcur&&li.dataset.v!==gcur})};
  var paint=function(){var g=giv(),f=false;
   hb.forEach(function(b,i){var c=box.children[i],v=b.dataset.h,on,dim,n;
    if(g){n=gl?gl.querySelectorAll('li.fb[data-v="'+v+'"]').length:0;on=gcur===v;dim=!!gcur&&!on}
    else{n=b.querySelector('b').textContent;on=b.classList.contains('on');dim=b.classList.contains('dim')}
    c.querySelector('b').textContent=n;c.classList.toggle('on',on);c.classList.toggle('dim',dim);c.setAttribute('aria-pressed',on);if(on)f=true});
   if(!g){if(!f&&document.body.classList.contains('opt-filt'))document.body.classList.add('opt-more');document.body.classList.toggle('opt-filt',f)}};
  hb.forEach(function(b){var c=document.createElement('button');c.type='button';
   c.innerHTML='<i></i><b></b> '+b.querySelector('span').textContent;
   c.addEventListener('click',function(){if(giv()){gcur=gcur===b.dataset.h?null:b.dataset.h;gapply();paint();return}
    var y=scrollY;b.click();requestAnimationFrame(function(){scrollTo({top:y})})});
   box.appendChild(c)});
  sw.after(box);
  hb.forEach(function(b){new MutationObserver(paint).observe(b,{attributes:true,attributeFilter:['class']})});
  // switching Received/Given clears the Given filter and shows that list's own numbers
  new MutationObserver(function(){gcur=null;gapply();paint()}).observe(P,{attributes:true,attributeFilter:['class']});
  paint();
 }
 document.querySelectorAll('.lbtabs .tabs b').forEach(b=>b.remove());
 // ? next to the Universe title; card split into Readings and Conversations (text from My universe)
 var h=document.getElementById('uni-h'),kq=document.getElementById('kq'),kb=document.getElementById('kbox'),reads=document.querySelector('.lbreads .reads');
 if(h&&kq&&kb&&reads){
  var old=kq.parentElement;h.appendChild(kq);if(old&&old.tagName=='SPAN'&&!old.textContent.trim()&&!old.children.length)old.remove();
  kq.setAttribute('aria-label','What is in the universe?');
  h.after(kb);
  var kx=document.getElementById('kx');[...kb.children].forEach(function(n){if(n!==kx)n.remove()});
  kb.insertAdjacentHTML('beforeend','<b class="opt-kh">Readings</b><p>The books and films that shaped how you think, sorted by topic. Add one and it joins the map on your profile.</p><b class="opt-kh">Conversations</b><p>What your tables left behind, saved and sorted by topic. Read one again, or pick it up for a new round.</p>');
  kb.setAttribute('aria-label','About the universe');
  new MutationObserver(function(){if(kq.getAttribute('aria-label')!='What is in the universe?')kq.setAttribute('aria-label','What is in the universe?');if(kb.getAttribute('aria-label')!='About the universe')kb.setAttribute('aria-label','About the universe')}).observe(kq,{attributes:true});
 }
})();
(function(){var t=document.getElementById('t-fb');if(!t)return;var fix=function(){if(t.textContent.trim()!=='Feedbacks'){mo.disconnect();t.textContent='Feedbacks';mo.observe(t,{childList:true,subtree:true,characterData:true})}};var mo=new MutationObserver(fix);mo.observe(t,{childList:true,subtree:true,characterData:true});fix()})();
(function(){var m=document.querySelector('#p-fb .more');if(!m)return;m.addEventListener('click',function(e){if(!document.body.classList.contains('opt-more')){document.body.classList.add('opt-more');e.stopImmediatePropagation();e.preventDefault()}},true)})();
