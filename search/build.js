const fs=require('fs');const I='/mnt/project-files/i18n/';const D={};
for(const f of ['dict1.txt','dict2.txt','dict3.txt','dict4.txt','dict5.txt'].map(x=>I+x).concat(['dict6.txt']))for(const ln of fs.readFileSync(f,'utf8').split('\n')){if(!ln.trim())continue;const [e,i,s]=ln.split('|');D[e]=[i,s]}
const js='window.TCI18N_DICT='+JSON.stringify(D)+';\n'+fs.readFileSync(I+'i18n-core.js','utf8');
const tag='<script id="tc-i18n">'+js.replace(/<\//g,'<\\/')+'</script>';
const P=fs.readFileSync(process.argv[2],'utf8').split('\n');
let head=P.slice(158,421).join('\n'); // fonts .. header script (lines 159-421)
const rep=(a,b)=>{if(!head.includes(a))throw new Error('missing '+a);head=head.split(a).join(b)};
rep('<a href="#" aria-current="page">People</a>','<a href="https://claude.ai/artifact/MTbRjvLFV7pPhBjpvAzXaq" target="_top">People</a>');
rep('<a class="ph" href="#">People</a>','<a class="ph" href="https://claude.ai/artifact/MTbRjvLFV7pPhBjpvAzXaq" target="_top">People</a>');
rep('<input id="q" type="search"','<input id="hq" type="search"');
const av=P.slice(567,570).join('\n');
let body=fs.readFileSync('body.html','utf8').replace('__AVATARS__',av);
const html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<title>TimeCapsule Search</title>'+tag+'\n'+head+'\n'+body+'\n</body></html>\n';
fs.writeFileSync('timecapsule-search.html',html);console.log(Object.keys(D).length,'entries',html.length,'bytes');
