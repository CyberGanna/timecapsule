const {chromium}=require('playwright');
(async()=>{
const b=await chromium.launch(); const p=await b.newPage();
await p.setViewportSize({width:794,height:1123});
await p.goto('file://'+__dirname+'/gatekeepers.html',{waitUntil:'load'});
await p.evaluate(async()=>{await Promise.all(['300 10px Sora','400 10px Sora','600 10px Sora','400 10px Newsreader','500 10px Newsreader'].map(f=>document.fonts.load(f)));});
const r=await p.evaluate(()=>{const b=document.querySelector('.body');const k=[...b.children];const last=k[k.length-2];return {over:b.scrollHeight-b.clientHeight, gap:b.querySelector('.principle').getBoundingClientRect().top-last.getBoundingClientRect().bottom}});
console.log('overflow px',r.over,'gap above principle px',Math.round(r.gap));
await p.pdf({path:__dirname+'/../From-Gatekeepers-to-the-Table.pdf',preferCSSPageSize:true,printBackground:true});
await p.screenshot({path:__dirname+'/preview.png'});
await b.close()})();
