(function(){
 var view=document.getElementById('uniview'),rows=document.querySelector('.opt-rows');if(!view||!rows)return;
 var rb=document.querySelector('.unitog button[data-m="read"]');if(rb&&rb.getAttribute('aria-pressed')!=='true')rb.click();
 var X='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
 function fix(){rows.querySelectorAll('.opt-row').forEach(function(b){var s=b.querySelector('svg');if(s&&!s.dataset.x){s.outerHTML=X;b.querySelector('svg').dataset.x=1;b.setAttribute('aria-label',b.textContent.trim()+', close')}})}
 fix();new MutationObserver(fix).observe(rows,{childList:true});
 var hint=document.createElement('p');hint.className='opt-hint';hint.textContent='Tap a planet to see its books.';rows.before(hint);
 var mut=rows.querySelector('.opt-g[data-k="__mut"]');
 if(mut){var n=mut.lastChild.querySelectorAll(':scope>div:not(.opt-all)').length,b=document.createElement('button');b.type='button';b.textContent=n+' you both read';
  b.addEventListener('click',function(){mut.firstChild.click()});hint.appendChild(b)}
 var host=view.closest('.uni')||document.body;
 new MutationObserver(function(){document.body.classList.toggle('uni-a7open',!!rows.querySelector('.opt-row[aria-expanded=true]'))}).observe(rows,{subtree:true,attributes:true,attributeFilter:['aria-expanded']});
})();
