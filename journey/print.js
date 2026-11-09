// node print.js  ->  TimeCapsule-Teds-Journey.pdf
const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.join(__dirname,'journey.html'),{waitUntil:'networkidle'});
await p.pdf({path:path.join(__dirname,'TimeCapsule-Teds-Journey.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close()})();
