(function(){
 var tags=document.getElementById('herotags'),meta=document.querySelector('.lbmeta');
 if(tags&&meta)meta.after(tags);
 // ratings as tappable chips; each one filters the feedbacks (uses the page's own Ratings buttons)
 var hb=[...document.querySelectorAll('.hist button')];
 var sw=document.querySelector('#p-fb .fbsw');
 if(sw&&hb.length){
  var box=document.createElement('div');box.className='opt-rchips';box.setAttribute('role','group');box.setAttribute('aria-label','Filter by rating');
  hb.forEach(function(b){var c=document.createElement('button');c.type='button';
   c.innerHTML='<i></i><b>'+b.querySelector('b').textContent+'</b> '+b.querySelector('span').textContent;
   c.addEventListener('click',function(){var y=scrollY;b.click();requestAnimationFrame(function(){scrollTo({top:y})})});
   box.appendChild(c)});
  sw.after(box);
  var sync=function(){document.body.classList.toggle('opt-filt',hb.some(function(b){return b.classList.contains('on')}));hb.forEach(function(b,i){var c=box.children[i];c.classList.toggle('on',b.classList.contains('on'));c.classList.toggle('dim',b.classList.contains('dim'));c.setAttribute('aria-pressed',b.classList.contains('on'))})};
  hb.forEach(function(b){new MutationObserver(sync).observe(b,{attributes:true,attributeFilter:['class']})});sync();
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
