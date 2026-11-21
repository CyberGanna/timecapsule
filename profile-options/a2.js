(function(){var u=document.getElementById('ulay'),h=document.getElementById('uni-h');if(!u||!h)return;var was=false;
new MutationObserver(function(){var open=!u.hidden&&u.classList.contains('pg');if(open!==was){var t=h.getBoundingClientRect().top;if(t<0||(!open&&t<0))h.scrollIntoView({block:'start'});was=open}}).observe(u,{attributes:true,attributeFilter:['hidden','class']});})();
(function(){var u=document.getElementById('ulay');if(!u)return;
var f=function(){mo.disconnect();var pl=u.querySelector('.pl'),btn=u.querySelector('.opt-allbtn');
 var cm=u.querySelector('.cmb[aria-pressed=true]');u.classList.toggle('opt-mut',!!cm);var ttl=u.querySelector('.ph>b,.ph>h3,.ph>strong');if(ttl){if(cm){if(!ttl.dataset.optOrig)ttl.dataset.optOrig=ttl.textContent;ttl.textContent=pl.querySelectorAll(':scope>li .yt').length+' mutual reads'}else if(ttl.dataset.optOrig){ttl.textContent=ttl.dataset.optOrig;delete ttl.dataset.optOrig}}
 var n=pl?(cm?pl.querySelectorAll(':scope>li .yt').length:pl.querySelectorAll(':scope>li').length):0;
 var lim=matchMedia('(min-width:700px)').matches?18:9;if(pl&&n>lim&&!u.classList.contains('opt-all')){if(!btn){btn=document.createElement('button');btn.type='button';btn.className='opt-allbtn';btn.onclick=function(){u.classList.add('opt-all');btn.remove()};}btn.textContent='Show all '+n;pl.after(btn)}else if(btn)btn.remove();
 mo.observe(u,{childList:true,subtree:true,attributes:true,attributeFilter:['aria-pressed']})};
var mo=new MutationObserver(f);
new MutationObserver(function(){u.classList.remove('opt-all');f()}).observe(u,{attributes:true,attributeFilter:['hidden']});
mo.observe(u,{childList:true,subtree:true,attributes:true,attributeFilter:['aria-pressed']});})();
