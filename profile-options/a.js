(function(){
 var tags=document.getElementById('herotags'),meta=document.querySelector('.lbmeta');
 if(tags&&meta)meta.after(tags);
 // one quiet line instead of the Ratings block
 var h=[...document.querySelectorAll('.hist button')].map(b=>'<b>'+b.querySelector('b').textContent+'</b> '+b.querySelector('span').textContent);
 var sw=document.querySelector('#p-fb .fbsw');
 if(sw&&h.length){var p=document.createElement('p');p.className='opt-rline';p.innerHTML=h.join(' · ');sw.after(p)}
 document.querySelectorAll('.lbtabs .tabs b').forEach(b=>b.remove());
})();
