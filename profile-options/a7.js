(function(){
 window.__optNoScroll=1;
 var view=document.getElementById('uniview'),rows=document.querySelector('.opt-rows');if(!view||!rows)return;
 var X='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
 var hint=document.createElement('p');hint.className='opt-hint';hint.innerHTML='<span>Tap to open topic. Tap photo to see all.</span>';rows.before(hint);
 var mb=document.createElement('button');mb.type='button';hint.appendChild(mb);
 var head=document.createElement('div');head.className='opt-allhead';head.innerHTML='<span>All topics</span><button type="button">Back to the map</button>';
 head.querySelector('button').addEventListener('click',function(){all(false)});
 function mut(){return rows.querySelector('.opt-g[data-k="__mut"]')}
 mb.addEventListener('click',function(){var m=mut();if(!m)return;var y=scrollY;rows.querySelectorAll(':scope>.opt-g').forEach(function(o){var on=o===m;o.firstChild.setAttribute('aria-expanded',on);o.lastChild.hidden=!on});window.scrollTo(0,y)});
 // after every render (Readings or Conversations): close icons, the All topics header, the mutual link
 var busy=false;
 function fix(){if(busy)return;busy=true;
  rows.querySelectorAll('.opt-row').forEach(function(b){var s=b.querySelector('svg');if(s&&!s.dataset.x){s.outerHTML=X;b.querySelector('svg').dataset.x=1;b.setAttribute('aria-label',b.textContent.trim()+', close')}});
  if(rows.firstChild!==head)rows.prepend(head);
  var m=mut();mb.hidden=!m;if(m)mb.textContent='· '+m.lastChild.querySelectorAll(':scope>div:not(.opt-all)').length+' you both read';
  busy=false}
 fix();new MutationObserver(fix).observe(rows,{childList:true});
 function all(on){document.body.classList.toggle('opt-allrows',on);rows.querySelectorAll('.opt-row[aria-expanded=true]').forEach(function(b){b.setAttribute('aria-expanded','false');b.nextSibling.hidden=true})}
 // switching Readings / Conversations goes back to the map
 document.querySelectorAll('.unitog button').forEach(function(b){b.addEventListener('click',function(){all(false)})});
 // tapping the photo swaps the map for the list of all topics
 function sun(){return document.querySelector('#uni .sunav')}
 function go(e){e.stopImmediatePropagation();e.preventDefault();all(true);var h=document.getElementById('uni-h');if(h&&h.getBoundingClientRect().top<0)h.scrollIntoView({block:'start'})}
 function onSun(e){var s=sun();if(!s)return false;if(e.target.closest&&e.target.closest('.sunav'))return true;if(!e.clientX&&!e.clientY)return false;var r=s.getBoundingClientRect();return e.clientX>=r.left&&e.clientX<=r.right&&e.clientY>=r.top&&e.clientY<=r.bottom}
 view.addEventListener('click',function(e){if(!document.body.classList.contains('opt-allrows')&&onSun(e))go(e)},true);
 view.addEventListener('keydown',function(e){if((e.key==='Enter'||e.key===' ')&&e.target.closest&&e.target.closest('.sunav'))go(e)},true);
 function tagSun(){var s=sun();if(s&&!s.hasAttribute('tabindex')){s.setAttribute('tabindex','0');s.setAttribute('role','button');s.setAttribute('aria-label','See all topics as a list')}}
 tagSun();new MutationObserver(tagSun).observe(document.getElementById('uni'),{childList:true});
})();
