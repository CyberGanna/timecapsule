(function(){
 // A9: tapping a planet straightens its orbit into a line at the top; the topic's books open below the line
 var view=document.getElementById('uniview'),svg=document.getElementById('uni'),rows=document.querySelector('.opt-rows');
 if(!view||!svg||!rows)return;
 var NS='http://www.w3.org/2000/svg',box=svg.parentNode,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
 var LY=16,X0=22,X1=318,STRIP=34,N=140,DUR=reduce?0:650;
 var st=null; // {key,col,pts:[[from],[to]],dots,strip}
 function mode(){var b=document.querySelector('.unitog button[aria-pressed=true]');return b?b.dataset.m:'read'}
 function T(){return mode()==='lib'?window.__LT:window.__RT}
 function mk(n,a,p){var e=document.createElementNS(NS,n);for(var k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e}
 function tp(m,x,y){return [m.a*x+m.c*y+m.e,m.b*x+m.d*y+m.f]}
 function metrics(){var r=svg.getBoundingClientRect(),s=Math.min(r.width/340,r.height/250);return {r:r,s:s,ox:(r.width-340*s)/2,oy:(r.height-250*s)/2}}
 // where the orbit and its planets are right now, in map units
 function geom(key){var list=T()||[],i=list.findIndex(function(t){return t.n===key});if(i<0)return null;
  var el=svg.querySelectorAll('ellipse[stroke-dasharray]')[i];if(!el)return null;
  var m=el.getCTM(),cx=+el.getAttribute('cx'),cy=+el.getAttribute('cy'),rx=+el.getAttribute('rx'),ry=+el.getAttribute('ry'),inv=m.inverse();
  var ring=[],line=[];for(var k=0;k<N;k++){var t=Math.PI+k/(N-1)*Math.PI*2;ring.push(tp(m,cx+rx*Math.cos(t),cy+ry*Math.sin(t)));line.push([X0+(X1-X0)*k/(N-1),LY])}
  var dots=[];svg.querySelectorAll('g.bk').forEach(function(g){var lab=g.getAttribute('aria-label')||'';if(lab.slice(lab.lastIndexOf(', ')+2)!==key)return;
   var p=tp(g.getCTM(),0,0),l=tp(inv,p[0],p[1]),t=Math.atan2((l[1]-cy)/ry,(l[0]-cx)/rx),u=((t-Math.PI)%(2*Math.PI)+4*Math.PI)%(2*Math.PI)/(2*Math.PI);
   dots.push({a:p,b:[X0+(X1-X0)*u,LY]})});
  return {key:key,col:list[i].c,ring:ring,line:line,dots:dots}}
 function ease(x){return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}
 function overlay(){var m=metrics(),ur=box.getBoundingClientRect(),o=mk('svg',{viewBox:'0 0 340 250','class':'opt-morph'});
  o.style.left=(m.r.left-ur.left)+'px';o.style.top=(m.r.top-ur.top)+'px';o.style.width=m.r.width+'px';o.style.height=m.r.height+'px';box.appendChild(o);return o}
 function run(g,dir,done){ // dir 1: ring -> line, -1: line -> ring
  var o=overlay(),pl=mk('polyline',{fill:'none',stroke:g.col,'stroke-opacity':'.8','stroke-width':'1.6','stroke-linecap':'round','stroke-dasharray':'0 5'},o);
  var cs=g.dots.map(function(){return mk('circle',{r:3.4,fill:g.col},o)});
  var t0=performance.now();
  function f(now){var e=DUR?Math.min(1,(now-t0)/DUR):1,k=ease(dir>0?e:1-e);
   pl.setAttribute('points',g.ring.map(function(p,j){var q=g.line[j];return (p[0]+(q[0]-p[0])*k).toFixed(1)+','+(p[1]+(q[1]-p[1])*k).toFixed(1)}).join(' '));
   g.dots.forEach(function(d,j){cs[j].setAttribute('cx',(d.a[0]+(d.b[0]-d.a[0])*k).toFixed(1));cs[j].setAttribute('cy',(d.a[1]+(d.b[1]-d.a[1])*k).toFixed(1))});
   if(e<1)requestAnimationFrame(f);else{o.remove();done()}}
  requestAnimationFrame(f)}
 function strip(g,m){var s=mk('svg',{viewBox:'0 0 340 '+STRIP,'class':'opt-strip',role:'button',tabindex:'0','aria-label':'Back to the universe'});
  s.style.width=(340*m.s)+'px';s.style.height=(STRIP*m.s)+'px';s.style.marginTop=m.oy+'px';
  mk('line',{x1:X0,y1:LY,x2:X1,y2:LY,stroke:g.col,'stroke-opacity':'.8','stroke-width':'1.6','stroke-linecap':'round','stroke-dasharray':'0 5'},s);
  g.dots.forEach(function(d){mk('circle',{cx:d.b[0].toFixed(1),cy:LY,r:3.4,fill:g.col},s)});
  s.addEventListener('click',close);s.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();close()}});
  return s}
 function setRow(key){rows.querySelectorAll(':scope>.opt-g').forEach(function(x){var on=x.dataset.k===key;x.firstChild.setAttribute('aria-expanded',on);x.lastChild.hidden=!on})}
 var busy=false;
 function open(key){if(busy||st)return;var g=geom(key);if(!g)return;busy=true;window.__uniHold=1e15;
  var tip=document.getElementById('utip');if(tip)tip.hidden=true;
  svg.classList.add('opt-fade');
  run(g,1,function(){var y=scrollY,m=metrics();svg.style.display='none';g.strip=strip(g,m);svg.after(g.strip);svg.classList.remove('opt-fade');
   document.body.classList.add('opt-lineopen');setRow(key);window.scrollTo(0,y);st=g;busy=false})}
 function close(){if(busy||!st)return;busy=true;var g=st,y=scrollY;
  setRow(null);document.body.classList.remove('opt-lineopen');g.strip.remove();svg.style.display='';svg.classList.add('opt-fade');window.scrollTo(0,y);
  run(g,-1,function(){svg.classList.remove('opt-fade');st=null;busy=false;window.__uniHold=Date.now()-3000})}
 function quick(){if(!st)return;setRow(null);document.body.classList.remove('opt-lineopen');st.strip.remove();svg.style.display='';svg.classList.remove('opt-fade');st=null;busy=false;window.__uniHold=0}
 function keyOf(g){var lab=g.getAttribute('aria-label')||'';return lab.slice(lab.lastIndexOf(', ')+2)}
 view.addEventListener('click',function(e){var g=e.target.closest&&e.target.closest('#uni g.bk');if(!g)return;e.stopImmediatePropagation();e.preventDefault();open(keyOf(g))},true);
 view.addEventListener('keydown',function(e){var g=e.target.closest&&e.target.closest('#uni g.bk');if(!g||!(e.key==='Enter'||e.key===' '))return;e.stopImmediatePropagation();e.preventDefault();open(keyOf(g))},true);
 // the × on the topic closes it the same way, backwards
 rows.parentNode.addEventListener('click',function(e){if(!st)return;var b=e.target.closest&&e.target.closest('.opt-row');if(!b||!rows.contains(b))return;e.stopImmediatePropagation();e.preventDefault();close()},true);
 // switch, photo list and mutual link: go back to the map at once
 document.querySelectorAll('.unitog button').forEach(function(b){b.addEventListener('click',quick,true)});
 var mb=document.querySelector('.opt-hint button');if(mb)mb.addEventListener('click',quick,true);
 new MutationObserver(function(){if(document.body.classList.contains('opt-allrows'))quick()}).observe(document.body,{attributes:true,attributeFilter:['class']});
})();
