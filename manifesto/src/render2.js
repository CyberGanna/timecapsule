const {chromium}=require('playwright');
(async()=>{
const b=await chromium.launch();
for(const name of process.argv.slice(2)){
  const p=await b.newPage(); p.on('console',m=>console.log(name,m.text()));
  await p.setViewportSize({width:794,height:1123});
  await p.goto('file://'+process.cwd()+'/'+name+'.html',{waitUntil:'load'});
  await p.evaluate(async()=>{await Promise.all(['300 10px Sora','400 10px Sora','600 10px Sora','400 10px Newsreader','500 10px Newsreader','italic 400 10px Newsreader'].map(f=>document.fonts.load(f)));window.paginate();});
  // re-run after fonts ready is not needed: fonts are local and loaded before script? ensure by reload
  const pages=await p.evaluate(()=>window.PAGES);
  console.log(name,'pages',pages);
  await p.pdf({path:name+'.pdf',preferCSSPageSize:true,printBackground:true});
  const n=await p.$$('.page');for(let i=0;i<n.length;i++){await n[i].screenshot({path:'shots/'+name+'-'+i+'.png'})}
  await p.close();
}
await b.close()})();
