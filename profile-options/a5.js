(function(){
 var h=document.getElementById('uni-h'),view=document.getElementById('uniview'),rows=document.querySelector('.opt-rows'),tog=document.querySelector('.unitog');
 if(!h||!view||!rows)return;
 if(tog){var w=document.createElement('div');w.className='opt-tog';w.appendChild(tog);view.before(w)}
 var ml=document.createElement('span');ml.className='opt-ml';ml.setAttribute('role','group');ml.setAttribute('aria-label','Show as');
 ml.innerHTML='<button type="button" data-v="map" aria-pressed="true">Map</button><button type="button" data-v="list" aria-pressed="false">List</button>';
 h.appendChild(ml);
 function set(v){document.body.classList.toggle('opt-list',v==='list');ml.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.v===v)})}
 ml.addEventListener('click',function(e){var b=e.target.closest('button');if(b)set(b.dataset.v)});
 // tapping a planet switches to the list with its topic open (A3 opens the row; switch first)
 var svg=document.getElementById('uni');
 ['click','keydown'].forEach(function(t){view.addEventListener(t,function(e){var g=e.target.closest&&e.target.closest('g.bk');if(g&&(t==='click'||e.key==='Enter'||e.key===' '))set('list')},true)});
})();
