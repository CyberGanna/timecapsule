const {chromium}=require('playwright');
(async()=>{
const b=await chromium.launch(); const p=await b.newPage();
await p.setViewportSize({width:816,height:1056});
await p.goto('file://'+__dirname+'/gatekeepers.html',{waitUntil:'load'});
await p.evaluate(async()=>{await Promise.all(['300 10px Sora','400 10px Sora','600 10px Sora','400 10px Newsreader','500 10px Newsreader'].map(f=>document.fonts.load(f)));});
const r=await p.evaluate(()=>[...document.querySelectorAll('.body')].map(b=>{const k=[...b.children];const last=k[k.length-1];return {over:b.scrollHeight-b.clientHeight, free:Math.round(b.getBoundingClientRect().bottom-last.getBoundingClientRect().bottom)}}));
console.log(JSON.stringify(r));
await p.pdf({path:__dirname+'/../From-Gatekeepers-to-the-Table.pdf',preferCSSPageSize:true,printBackground:true});
const s=await p.$$('.page');for(let i=0;i<s.length;i++)await s[i].screenshot({path:__dirname+'/preview-'+(i+1)+'.png'});
await b.close()})();
