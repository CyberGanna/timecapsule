// page-specific patches applied after injection
module.exports=function(f,h){
 const cnt0=(h.match(/TCI18N\.u\(/g)||[]).length;
 h=h.replace(/location\.href\s*=\s*(["'])(https:\/\/claude\.ai\/artifact\/[A-Za-z0-9]+(?:#[^"']*)?)\1/g,(m,q,u)=>'location.href=TCI18N.u('+q+u+q+')');
 const rep=(a,b)=>{if(!h.includes(a))throw new Error(f+': missing '+a.slice(0,60));h=h.split(a).join(b)};
 if(f==='settings.html'){
  rep('<select class="lang" aria-label="App language"><option>English</option><option>Deutsch</option><option>Français</option><option>Italiano</option><option>Español</option><option>Português</option><option>日本語</option></select>',
      '<select class="lang" id="applang" aria-label="App language" data-noi18n><option value="en">English</option><option value="it">Italiano</option><option value="es">Español</option><option value="el">Ελληνικά</option></select>');
  rep('<b>App language</b></div>','<b>App language</b><span>Applies to every TimeCapsule page you open from here.</span></div>');
  rep("if(a.textContent.trim()==='Sign out')","if(TCI18N.src(a).trim()==='Sign out')");
  rep("document.querySelectorAll('.lang').forEach(s=>s.addEventListener('change',()=>toast('Saved')));",
      "document.querySelectorAll('.lang').forEach(s=>s.addEventListener('change',()=>{if(s.id==='applang')TCI18N.set(s.value);toast('Saved')}));(function(){var s=document.getElementById('applang');if(s)s.value=TCI18N.lang})();");
 }
 if(f==='profile.html'){
  rep('function(s){return s.textContent}','function(s){return TCI18N.src(s)}');
  rep('tint(x,x.textContent.trim())','tint(x,TCI18N.src(x).trim())');
  rep('var c=C[i.textContent.trim()]','var c=C[TCI18N.src(i).trim()]');
 }
 return h};
