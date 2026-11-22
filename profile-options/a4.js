(function(){
 var view=document.getElementById('uniview'),hero=document.querySelector('.lbh'),rows=document.querySelector('.opt-rows'),tog=document.querySelector('.unitog');
 if(!view||!hero||!rows)return;
 if(tog){var w=document.createElement('div');w.className='opt-tog';w.appendChild(tog);rows.before(w)}
 var back=document.getElementById('lbback');(back?back.after(view):hero.prepend(view));
})();
(function(){
 // centre the orbits on the profile photo, so the photo is the sun
 var view=document.getElementById('uniview'),img=document.querySelector('.lbh img.big, .lbh .big'),hero=document.querySelector('.lbh'),svg=document.getElementById('uni');
 if(!view||!img||!hero||!svg)return;
 function place(){document.body.classList.add('opt-sun');
  var hr=hero.getBoundingClientRect(),ir=img.getBoundingClientRect(),sr=svg.getBoundingClientRect(),vr=view.getBoundingClientRect();
  // the sun sits at x 170/340, y 125/250 of the map; with preserveAspectRatio meet, map is centred in the box
  var sc=Math.min(sr.width/340,sr.height/250),oy=(sr.height-250*sc)/2,sunY=sr.top+oy+125*sc;
  var dy=(ir.top+ir.height/2)-sunY;view.style.top=(parseFloat(getComputedStyle(view).top)+dy)+'px';
  // start the name just below the outer orbit
  var who=hero.querySelector('.lbwho');if(who){who.style.marginTop='0px';var bot=0;svg.querySelectorAll('ellipse').forEach(function(e){if(e.getAttribute('fill')&&e.getAttribute('fill').indexOf('url(')==0)return;var m=e.getScreenCTM(),L=e.getTotalLength(),pt=svg.createSVGPoint();if(!m||!L)return;for(var k=0;k<72;k++){var q=e.getPointAtLength(L*k/72);pt.x=q.x;pt.y=q.y;var t=pt.matrixTransform(m);bot=Math.max(bot,t.y)}});var gap=bot-who.getBoundingClientRect().top+16;who.style.marginTop=Math.max(0,gap)+'px'}}
 place();addEventListener('resize',place);setTimeout(place,600);
})();
