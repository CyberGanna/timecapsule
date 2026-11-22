(function(){
 var view=document.getElementById('uniview'),rows=document.querySelector('.opt-rows');if(!view||!rows)return;
 var rb=document.querySelector('.unitog button[data-m="read"]');if(rb&&rb.getAttribute('aria-pressed')!=='true')rb.click();
 var X='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
 function fix(){rows.querySelectorAll('.opt-row').forEach(function(b){var s=b.querySelector('svg');if(s&&!s.dataset.x){s.outerHTML=X;b.querySelector('svg').dataset.x=1;b.setAttribute('aria-label',b.textContent.trim()+', close')}})}
 fix();new MutationObserver(fix).observe(rows,{childList:true});
 var hint=document.createElement('p');hint.className='opt-hint';hint.textContent='Tap an orbit to open it. Tap the photo to see all.';rows.before(hint);
 var mut=rows.querySelector('.opt-g[data-k="__mut"]');
 if(mut){var n=mut.lastChild.querySelectorAll(':scope>div:not(.opt-all)').length,b=document.createElement('button');b.type='button';b.textContent='· '+n+' you both read';
  b.addEventListener('click',function(){mut.firstChild.click()});hint.appendChild(b)}

 // tapping the photo shows every topic (each opens in place)
 var head=document.createElement('div');head.className='opt-allhead';head.innerHTML='<span>All topics</span><button type="button">Back to the map</button>';rows.prepend(head);
 function all(on){document.body.classList.toggle('opt-allrows',on);if(!on)rows.querySelectorAll('.opt-row[aria-expanded=true]').forEach(function(b){b.click()})}
 head.querySelector('button').addEventListener('click',function(){all(false)});
 var sun=document.querySelector('#uni .sunav');
 if(sun){sun.setAttribute('tabindex','0');sun.setAttribute('role','button');sun.setAttribute('aria-label','See all topics as a list');
  var go=function(e){e.stopImmediatePropagation();e.preventDefault();rows.querySelectorAll('.opt-row[aria-expanded=true]').forEach(function(b){b.setAttribute('aria-expanded','false');b.nextSibling.hidden=true});all(true);var h=document.getElementById('uni-h');if(h&&h.getBoundingClientRect().top<0)h.scrollIntoView({block:'start'})};
  var onSun=function(e){if(e.target.closest&&e.target.closest('.sunav'))return true;if(e.clientX==null)return false;var r=sun.getBoundingClientRect();return e.clientX>=r.left&&e.clientX<=r.right&&e.clientY>=r.top&&e.clientY<=r.bottom};
  view.addEventListener('click',function(e){if(!document.body.classList.contains('opt-allrows')&&onSun(e))go(e)},true);
  sun.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' ')go(e)},true)}
 var host=view.closest('.uni')||document.body;
 new MutationObserver(function(){document.body.classList.toggle('uni-a7open',!!rows.querySelector('.opt-row[aria-expanded=true]'))}).observe(rows,{subtree:true,attributes:true,attributeFilter:['aria-expanded']});
})();
