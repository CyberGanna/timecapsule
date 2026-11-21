(function(){
 var tags=document.getElementById('herotags'),meta=document.querySelector('.lbmeta');
 if(tags&&meta)meta.after(tags);
 var hist=document.querySelector('.lbside .hist'),sw=document.querySelector('#p-fb .fbsw');
 if(hist&&sw)sw.after(hist);
})();
