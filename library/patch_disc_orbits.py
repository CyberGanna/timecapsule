import sys
NEW = r'''G.forEach((t,i)=>{
  const r=Math.floor(i/cols),c=i%cols,cw=W/cols;
  let cx=Math.max(mob?62:96,Math.min(W-(mob?62:96),cw*c+cw/2+(mob?0:(r%2?cw*.14:-cw*.14)))),cy=top0+rowH*r+(mob?40:62)+((c%2)?(mob?8:14):0);
  // same look as the profile universe: a tilted dotted orbit in the topic colour, conversations as plain dots on it
  const R=rnd(i*97+13+(inT?7:0)),shown=t.d.slice().sort((a,b)=>b.score-a.score).slice(0,MAXST),k=shown.length,size=t.d.length,gl=.62+.38*Math.sqrt(size/big),
   rx=(mob?46:62)*gl,ry=rx*.38,th=-14*Math.PI/180,ct=Math.cos(th),sn=Math.sin(th),a0=R()*Math.PI*2,pts=[];
  for(let j=0;j<k;j++){const a=a0+(j/k)*Math.PI*2+(R()-.5)*.5,ex=Math.cos(a)*rx,ey=Math.sin(a)*ry;pts.push([cx+ex*ct-ey*sn,cy+ex*sn+ey*ct])}
  const rot='rotate(-14 '+cx+' '+cy+')';
  g+='<g class="cl" data-t="'+esc(t.n)+'" tabindex="0" role="button" aria-label="'+esc(t.n)+', '+size+'">'+
   '<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+(rx+16).toFixed(1)+'" ry="'+(ry+16).toFixed(1)+'" fill="transparent"/>'+
   '<circle cx="'+cx+'" cy="'+cy+'" r="'+(mob?9:12)+'" fill="url(#ng'+i+')"/><circle cx="'+cx+'" cy="'+cy+'" r="'+(mob?2.6:3.2)+'" fill="'+t.c+'" opacity=".9"/>'+
   '<ellipse transform="'+rot+'" cx="'+cx+'" cy="'+cy+'" rx="'+rx.toFixed(1)+'" ry="'+ry.toFixed(1)+'" fill="none" stroke="'+t.c+'" stroke-opacity=".28" stroke-width=".6"/>'+
   '<ellipse transform="'+rot+'" cx="'+cx+'" cy="'+cy+'" rx="'+rx.toFixed(1)+'" ry="'+ry.toFixed(1)+'" fill="none" stroke="'+t.c+'" stroke-opacity=".7" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="0 '+(mob?4.5:5.5)+'"/>'+
   shown.map((d,j)=>{const[x,y]=pts[j];return '<circle class="st" data-id="'+d.id+'" cx="'+x.toFixed(1)+'" cy="'+y.toFixed(1)+'" r="'+(mob?3:3.6)+'" fill="'+t.c+'"/>'}).join("")+
   '<text x="'+cx+'" y="'+(cy+ry+(mob?24:32)).toFixed(1)+'"><tspan>'+esc(t.n)+'</tspan><tspan class="n" dx="6">'+fmt(size)+'</tspan></text></g>';
 });'''
for f in sys.argv[1:]:
    s=open(f,encoding='utf8').read()
    i=s.index("G.forEach((t,i)=>{\n  const r=Math.floor(i/cols)")
    j=s.index("\n svg.innerHTML=defs+g;render();",i)
    s=s[:i]+NEW+s[j:]
    open(f,'w',encoding='utf8').write(s)
    print('patched',f)
