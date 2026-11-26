const {chromium}=require('playwright');
const JOBS=[['gatekeepers','From-Gatekeepers-to-the-Table'],['public','TimeCapsule-Think-Together']];
(async()=>{
const b=await chromium.launch();
for(const [src,out] of JOBS){
 const p=await b.newPage(); p.on('console',m=>console.log(src,m.text()));
 await p.setViewportSize({width:816,height:1056});
 await p.goto('file://'+__dirname+'/'+src+'.html',{waitUntil:'load'});
 await p.evaluate(async()=>{await Promise.all(['300 10px Sora','400 10px Sora','600 10px Sora','400 10px Newsreader','500 10px Newsreader'].map(f=>document.fonts.load(f)));window.paginate();});
 console.log(src,'pages',await p.evaluate(()=>window.PAGES),'free last page px',await p.evaluate(()=>{const bs=document.querySelectorAll('.body');const b=bs[bs.length-1];return Math.round(b.getBoundingClientRect().bottom-b.lastElementChild.getBoundingClientRect().bottom)}));
 await p.pdf({path:__dirname+'/../'+out+'.pdf',preferCSSPageSize:true,printBackground:true});
 const s=await p.$$('.page');for(let i=0;i<s.length;i++)await s[i].screenshot({path:__dirname+'/'+src+'-'+(i+1)+'.png'});
 await p.close();
}
await b.close()})();
