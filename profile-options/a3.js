(function(){
 var view=document.getElementById('uniview'),svg=document.getElementById('uni');if(!view||!svg||!window.__RT)return;
 var ul=document.createElement('div');ul.className='opt-rows';view.after(ul);
 var esc=function(x){return String(x).replace(/&/g,'&amp;').replace(/</g,'&lt;')};
 var mode=function(){var b=document.querySelector('.unitog button[aria-pressed=true]');return b?b.dataset.m:'read'};
 var CH='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>';
 function item(b,m){
  if(m==='lib'){var as=document.body.classList.contains('visitor')?'visitor':'host';
   return '<div><a href="../library/timecapsule-library.html#r='+encodeURIComponent(b[2])+'&as='+as+'" target="_top">'+esc(b[0])+'</a><small>'+esc(b[1])+'</small></div>'}
  return '<div><span>'+esc(b[0])+(window.__YT(b)?'<em>You too</em>':'')+'</span><small>'+esc(b[1])+'</small></div>'}
 function row(key,label,color,books,m,cls){
  var li=document.createElement('div');li.className='opt-g';li.dataset.k=key;
  var n=books.length,unit=m==='lib'?(n==1?'conversation':'conversations'):(n==1?'book':'books');
  li.innerHTML='<button type="button" class="opt-row'+(cls?' '+cls:'')+'" aria-expanded="false" style="--c:'+color+'"><i></i><span>'+esc(label)+'</span><small>'+n+' '+unit+'</small>'+CH+'</button><div class="opt-items'+(n>18?' opt-big':'')+'" hidden>'+books.map(function(b,i){var h=item(b,m);return i>=9?h.replace('<div>','<div class="opt-x'+(i<18?' opt-d':'')+'">'):h}).join('')+(n>9?'<div class="opt-all"><button type="button">Show all '+n+'</button></div>':'')+'</div>';
  li.firstChild.addEventListener('click',function(){toggle(li)});var sa=li.querySelector('.opt-all button');if(sa)sa.addEventListener('click',function(){li.lastChild.classList.add('all')});return li}
 function toggle(li,force){var btn=li.firstChild,list=li.lastChild,open=force!=null?force:btn.getAttribute('aria-expanded')!=='true';
  ul.querySelectorAll(':scope>.opt-g').forEach(function(o){if(o!==li){o.firstChild.setAttribute('aria-expanded','false');o.lastChild.hidden=true}});
  btn.setAttribute('aria-expanded',open);list.hidden=!open;return open}
 var last=null;
 function render(){var m=mode();if(m===last&&ul.children.length)return;last=m;ul.innerHTML='';
  var T=m==='lib'?window.__LT:window.__RT;
  if(m!=='lib'){var mine=[];T.forEach(function(t){t.b.forEach(function(b){if(window.__YT(b))mine.push(b)})});
   if(mine.length)ul.appendChild(row('__mut','Books you both read','#17C3C8',mine,m,'mut'))}
  T.forEach(function(t){ul.appendChild(row(t.n,t.n,t.c,t.b,m))})}
 render();
 document.querySelectorAll('.unitog button').forEach(function(b){new MutationObserver(render).observe(b,{attributes:true,attributeFilter:['aria-pressed']})});
 // tapping a planet opens its topic row instead of a list inside the map
 function openFrom(g){var lab=g.getAttribute('aria-label')||'',topic=lab.slice(lab.lastIndexOf(', ')+2);
  var li=[...ul.children].find(function(x){return x.dataset.k===topic});if(!li)return;
  toggle(li,true);li.scrollIntoView({block:'nearest',behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'});
  li.firstChild.classList.remove('opt-flash');void li.offsetWidth;li.firstChild.classList.add('opt-flash')}
 svg.addEventListener('click',function(e){var g=e.target.closest&&e.target.closest('g.bk');if(g){e.stopImmediatePropagation();e.preventDefault();openFrom(g)}},true);
 svg.addEventListener('keydown',function(e){var g=e.target.closest&&e.target.closest('g.bk');if(g&&(e.key==='Enter'||e.key===' ')){e.stopImmediatePropagation();e.preventDefault();openFrom(g)}},true);
})();
