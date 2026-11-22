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
 // the orbit as it is now (centre, radii, tilt) and each planet's angle on it, in map units
 function geom(key){var list=T()||[],i=list.findIndex(function(t){return t.n===key});if(i<0)return null;
  var M=metrics(),ur=box.getBoundingClientRect(),X0=(ur.left-M.r.left-M.ox)/M.s+4,X1=(ur.right-M.r.left-M.ox)/M.s-4;
  var el=svg.querySelectorAll('ellipse[stroke-dasharray]')[i];if(!el)return null;
  var cx=+el.getAttribute('cx'),cy=+el.getAttribute('cy'),rx=+el.getAttribute('rx'),ry=+el.getAttribute('ry');
  var sys=el.parentNode.parentNode,mt=/rotate\(\s*([-\d.]+)/.exec(sys.getAttribute('transform')||''),tilt=mt?+mt[1]:0;
  var col=list[i].c,els=[].filter.call(svg.querySelectorAll('ellipse'),function(x){return x.getAttribute('stroke')===col});
  var ts=[];svg.querySelectorAll('g.bk').forEach(function(g){var lab=g.getAttribute('aria-label')||'';if(lab.slice(lab.lastIndexOf(', ')+2)!==key)return;els.push(g);
   var m=/translate\(\s*([-\d.]+)[ ,]+([-\d.]+)/.exec(g.getAttribute('transform')||'');if(!m)return;ts.push(Math.atan2((+m[2]-cy)/ry,(+m[1]-cx)/rx))});
  return {key:key,col:col,els:els,ts:ts,X0:X0,X1:X1,a:{cx:cx,cy:cy,rx:rx,ry:ry,r:tilt},b:{cx:(X0+X1)/2,cy:LY,rx:(X1-X0)/2,ry:0,r:0}}}
 function vis(g,on){g.els.forEach(function(e){e.style.visibility=on?'':'hidden'})}
 function ease(x){return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}
 function overlay(){var m=metrics(),ur=box.getBoundingClientRect(),o=mk('svg',{viewBox:'0 0 340 250','class':'opt-morph'});
  o.style.left=(m.r.left-ur.left)+'px';o.style.top=(m.r.top-ur.top)+'px';o.style.width=m.r.width+'px';o.style.height=m.r.height+'px';o.style.overflow='visible';box.appendChild(o);return o}
 function at(g,k){var A=g.a,B=g.b,L=function(p,q){return p+(q-p)*k};return {cx:L(A.cx,B.cx),cy:L(A.cy,B.cy),rx:L(A.rx,B.rx),ry:Math.max(L(A.ry,B.ry),.01),r:L(A.r,B.r)}}
 function pos(e,t){var c=Math.cos(e.r*Math.PI/180),s=Math.sin(e.r*Math.PI/180),x=e.rx*Math.cos(t),y=e.ry*Math.sin(t);return [e.cx+x*c-y*s,e.cy+x*s+y*c]}
 // the orbit breaks at its left end and unrolls into the line; each point keeps its place along the orbit
 function pts(g,k){var out=[];for(var n=0;n<N;n++){var t=Math.PI+n/(N-1)*Math.PI*2,p=pos(g.a,t),q=[g.X0+(g.X1-g.X0)*n/(N-1),LY];out.push([p[0]+(q[0]-p[0])*k,p[1]+(q[1]-p[1])*k])}return out}
 function ux(g,t){var u=((t-Math.PI)%(2*Math.PI)+4*Math.PI)%(2*Math.PI)/(2*Math.PI);return g.X0+(g.X1-g.X0)*u}
 function run(g,dir,done){ // dir 1: orbit -> line at the top, -1: back
  var o=overlay(),pl=mk('polyline',{fill:'none',stroke:g.col,'stroke-opacity':'.8','stroke-width':'1.6','stroke-linecap':'round','stroke-dasharray':'0 5'},o);
  var cs=g.ts.map(function(){return mk('circle',{r:3.4,fill:g.col},o)});
  var t0=performance.now();
  function f(now){var e=DUR?Math.min(1,(now-t0)/DUR):1,k=ease(dir>0?e:1-e);
   pl.setAttribute('points',pts(g,k).map(function(p){return p[0].toFixed(2)+','+p[1].toFixed(2)}).join(' '));
   g.ts.forEach(function(t,j){var p=pos(g.a,t),x=ux(g,t);cs[j].setAttribute('cx',(p[0]+(x-p[0])*k).toFixed(2));cs[j].setAttribute('cy',(p[1]+(LY-p[1])*k).toFixed(2))});
   if(e<1)requestAnimationFrame(f);else{o.remove();done()}}
  requestAnimationFrame(f)}
 function strip(g,m){var s=mk('svg',{viewBox:g.X0.toFixed(2)+' 0 '+(g.X1-g.X0).toFixed(2)+' '+STRIP,'class':'opt-strip',role:'button',tabindex:'0','aria-label':'Back to the universe'});
  s.style.width=((g.X1-g.X0)*m.s)+'px';s.style.height=(STRIP*m.s)+'px';s.style.marginTop=m.oy+'px';
  mk('polyline',{points:pts(g,1).map(function(p){return p[0].toFixed(2)+','+p[1].toFixed(2)}).join(' '),fill:'none',stroke:g.col,'stroke-opacity':'.8','stroke-width':'1.6','stroke-linecap':'round','stroke-dasharray':'0 5'},s);
  g.ts.forEach(function(t){mk('circle',{cx:ux(g,t).toFixed(2),cy:LY,r:3.4,fill:g.col},s)});
  s.addEventListener('click',close);s.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();close()}});
  return s}
 function setRow(key){rows.querySelectorAll(':scope>.opt-g').forEach(function(x){var on=x.dataset.k===key;x.firstChild.setAttribute('aria-expanded',on);x.lastChild.hidden=!on})}
 var busy=false;
 function open(key){if(busy||st)return;var g=geom(key);if(!g)return;busy=true;window.__uniHold=1e15;
  var tip=document.getElementById('utip');if(tip)tip.hidden=true;
  vis(g,false);svg.classList.add('opt-fade');
  run(g,1,function(){var y=scrollY,m=metrics(),h0=box.offsetHeight;svg.style.display='none';g.strip=strip(g,m);svg.after(g.strip);var dy=(m.r.top+m.oy)-g.strip.getBoundingClientRect().top;g.strip.style.marginTop=(m.oy+dy)+'px';svg.classList.remove('opt-fade');
   document.body.classList.add('opt-lineopen');setRow(key);slide(h0);window.scrollTo(0,y);st=g;busy=false})}
 function close(){if(busy||!st)return;busy=true;var g=st,y=scrollY;
  var h0=box.offsetHeight;setRow(null);document.body.classList.remove('opt-lineopen');g.strip.remove();svg.style.display='';slide(h0);svg.classList.add('opt-fade');window.scrollTo(0,y);void svg.getBoundingClientRect();svg.classList.remove('opt-fade');
  run(g,-1,function(){vis(g,true);st=null;busy=false;window.__uniHold=Date.now()-3000})}
 function quick(){if(!st)return;vis(st,true);setRow(null);document.body.classList.remove('opt-lineopen');st.strip.remove();svg.style.display='';svg.classList.remove('opt-fade');st=null;busy=false;window.__uniHold=0}
 function slide(h0){if(reduce)return;var h1=box.offsetHeight;if(h0===h1)return;box.style.height=h0+'px';void box.offsetHeight;box.style.transition='height .45s cubic-bezier(.2,.8,.2,1)';box.style.height=h1+'px';
  setTimeout(function(){box.style.transition='';box.style.height=''},480)}
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
