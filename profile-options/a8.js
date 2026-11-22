(function(){
 // A8: tapping a planet opens its orbit as a flat, still circle with the titles next to the dots
 var view=document.getElementById('uniview'),svg=document.getElementById('uni'),rows=document.querySelector('.opt-rows'),hint=document.querySelector('.opt-hint');
 if(!view||!svg||!rows)return;
 var NS='http://www.w3.org/2000/svg',box=svg.parentNode;
 var o=document.createElementNS(NS,'svg');o.setAttribute('viewBox','0 0 340 250');o.setAttribute('class','opt-orb');o.setAttribute('role','img');o.setAttribute('hidden','');svg.after(o);
 var bk=document.createElement('button');bk.type='button';bk.className='opt-orbback';bk.textContent='‹ Universe';bk.hidden=true;box.appendChild(bk);
  function el(n,a,p){var e=document.createElementNS(NS,n);for(var k in a)e.setAttribute(k,a[k]);(p||o).appendChild(e);return e}
 function mode(){var b=document.querySelector('.unitog button[aria-pressed=true]');return b?b.dataset.m:'read'}
 var want=null;
 function mutual(){var m=[];(window.__RT||[]).forEach(function(t){t.b.forEach(function(b){if(window.__YT&&window.__YT(b))m.push(b)})});return {n:'Books you both read',c:'#17C3C8',b:m}}
 function draw(key){var lib=mode()==='lib',T=lib?window.__LT:window.__RT,th=key==='__mut'?mutual():(T||[]).find(function(t){return t.n===key});if(!th||!th.b.length)return false;
  o.innerHTML='';var n=th.b.length,radial=n>10,cx=170,cy=radial?136:130,R=radial?40:60,col=th.c,mut=key==='__mut';
  var g=el('radialGradient',{id:'optneb'},el('defs',{}));el('stop',{offset:'0','stop-color':col,'stop-opacity':'.35'},g);el('stop',{offset:'1','stop-color':col,'stop-opacity':'0'},g);
  el('circle',{cx:cx,cy:cy,r:R-14,fill:'url(#optneb)'});
  el('circle',{cx:cx,cy:cy,r:R,fill:'none',stroke:col,'stroke-opacity':'.55','stroke-width':'.8','stroke-dasharray':'2 4'});
  var c=el('g',{'class':'opt-orbc',tabindex:'0',role:'button','aria-label':'Back to the universe'});
  el('circle',{cx:cx,cy:cy,r:30,fill:'transparent'},c);
  var t=el('text',{x:cx,y:cy+1,'text-anchor':'middle','class':'opt-orbn',fill:col,'font-size':R<50?'7':'10'},c);t.textContent=mut?'YOU BOTH READ':th.n.toUpperCase();
  var u=el('text',{x:cx,y:cy+13,'text-anchor':'middle','class':'opt-orbu'},c);u.textContent=n+' '+(lib?(n==1?'conversation':'conversations'):(n==1?'book':'books'));
  c.addEventListener('click',close);c.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();close()}});
  var step=Math.PI*2/n,max=radial?13:22;
  th.b.forEach(function(b,j){var a=-Math.PI/2+step*(j+.5),x=cx+Math.cos(a)*R,y=cy+Math.sin(a)*R,yt=!mut&&!lib&&window.__YT&&window.__YT(b);
   el('circle',{cx:x.toFixed(1),cy:y.toFixed(1),r:3.4,fill:col});
   var s=b[0].length>max?b[0].slice(0,max-1).trim()+'…':b[0],lab;
   if(radial){var deg=a*180/Math.PI,right=Math.cos(a)>=0,lx=cx+Math.cos(a)*(R+7),ly=cy+Math.sin(a)*(R+7);
    lab=el('text',{x:lx.toFixed(1),y:ly.toFixed(1),'text-anchor':right?'start':'end','dominant-baseline':'middle',transform:'rotate('+(right?deg:deg+180).toFixed(1)+' '+lx.toFixed(1)+' '+ly.toFixed(1)+')','class':'opt-orbl'+(yt?' yt':'')})}
   else{var ca=Math.cos(a),side=ca>.3?'start':ca<-.3?'end':'middle',lx=cx+Math.cos(a)*(R+8),ly=cy+Math.sin(a)*(R+8)+(side==='middle'?(Math.sin(a)<0?-4:10):3);
    lab=el('text',{x:lx.toFixed(1),y:ly.toFixed(1),'text-anchor':side,'class':'opt-orbl big'+(yt?' yt':'')})}
   lab.textContent=s;var ti=el('title',{},lab);ti.textContent=b[0]+' · '+b[1];
   if(lib&&b[2]){lab.classList.add('lnk');lab.setAttribute('tabindex','0');lab.setAttribute('role','link');var go=function(){var a=document.createElement('a');a.href='../library/timecapsule-library.html#r='+encodeURIComponent(b[2])+'&as='+(document.body.classList.contains('visitor')?'visitor':'host');a.target='_top';document.body.appendChild(a);a.click();a.remove()};lab.addEventListener('click',go);lab.addEventListener('keydown',function(e){if(e.key==='Enter')go()})}});
  o.setAttribute('aria-label',th.n+' orbit: '+th.b.map(function(b){return b[0]}).join(', '));
  return true}
 var shownAt=0;
 function show(key){var hh=svg.getBoundingClientRect().height;if(!draw(key))return;want=key;shownAt=Date.now();if(hh)o.style.height=hh+'px';svg.setAttribute('hidden','');o.removeAttribute('hidden');var tp=document.getElementById('utip');if(tp)tp.hidden=true;bk.hidden=false;document.body.classList.add('opt-orbopen')}
 function hide(){want=null;o.setAttribute('hidden','');svg.removeAttribute('hidden');bk.hidden=true;document.body.classList.remove('opt-orbopen')}
 function close(){hide()}
 bk.addEventListener('click',close);
 // a tap on a planet also sends a click to whatever replaces it: ignore that one
 o.addEventListener('click',function(e){if(Date.now()-shownAt<500){e.stopImmediatePropagation();e.preventDefault()}},true);
 // a planet tap turns the map into that orbit, in place: no list below, no scrolling
 function keyOf(g){var lab=g.getAttribute('aria-label')||'';return lab.slice(lab.lastIndexOf(', ')+2)}
 view.addEventListener('click',function(e){var g=e.target.closest&&e.target.closest('#uni g.bk');if(!g)return;e.stopImmediatePropagation();e.preventDefault();show(keyOf(g))},true);
 view.addEventListener('keydown',function(e){var g=e.target.closest&&e.target.closest('#uni g.bk');if(!g||!(e.key==='Enter'||e.key===' '))return;e.stopImmediatePropagation();e.preventDefault();show(keyOf(g))},true);
 // the mutual link opens the shared books as an orbit too
 var mb=hint&&hint.querySelector('button');if(mb)mb.addEventListener('click',function(e){e.stopImmediatePropagation();e.preventDefault();var r=rows.querySelector('.opt-row[aria-expanded=true]');if(r){r.setAttribute('aria-expanded','false');r.nextSibling.hidden=true}show('__mut')},true);
 // the photo (all topics list) and the switch go back to the universe
 new MutationObserver(function(){if(document.body.classList.contains('opt-allrows'))hide()}).observe(document.body,{attributes:true,attributeFilter:['class']});
 document.querySelectorAll('.unitog button').forEach(function(b){b.addEventListener('click',hide)});
})();
