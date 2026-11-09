// node print.js [ted|fedor]
const {chromium}=require('playwright');const path=require('path');
const who=process.argv[2]||'ted';
const src=who==='ted'?'journey.html':'journey-fedor.html';
const out=who==='ted'?'TimeCapsule-Teds-Journey.pdf':'TimeCapsule-Fedors-Journey.pdf';
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.join(__dirname,src),{waitUntil:'networkidle'});
await p.pdf({path:path.join(__dirname,out),format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close()})();
