// node shot.js plan.json outdir   — plan: [{name,url,js?,wait?,full?}]
const {chromium}=require('playwright');const fs=require('fs');
const plan=JSON.parse(fs.readFileSync(process.argv[2]));const out=process.argv[3];
(async()=>{const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1600/1440});
for(const s of plan){const p=await ctx.newPage();p.on('pageerror',e=>console.log(s.name,'ERR',e.message));
 await p.goto('http://127.0.0.1:8765/'+s.url,{waitUntil:'networkidle'});await p.waitForTimeout(s.wait||1200);
 if(s.js){for(const step of [].concat(s.js)){try{const r=await p.evaluate(step);if(r!==undefined)console.log(s.name,'->',JSON.stringify(r).slice(0,300))}catch(e){console.log(s.name,'JSERR',e.message)}await p.waitForTimeout(s.stepwait||700);}}
 await p.screenshot({path:out+'/'+s.name+'.png'});await p.close();console.log('ok',s.name)}
await b.close()})();
