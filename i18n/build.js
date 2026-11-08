const fs=require('fs');const D={};
for(const f of ['dict1.txt','dict2.txt','dict3.txt','dict4.txt','dict5.txt','dict6.txt'])for(const ln of fs.readFileSync(f,'utf8').split('\n')){if(!ln.trim())continue;const [e,i,s]=ln.split('|');D[e]=[i,s]}
const js='window.TCI18N_DICT='+JSON.stringify(D)+';\n'+fs.readFileSync('i18n-core.js','utf8');
fs.writeFileSync('i18n.js',js);const tag='<script id="tc-i18n">'+js.replace(/<\//g,'<\\/')+'</script>';
fs.mkdirSync('out',{recursive:true});
for(const f of fs.readdirSync('src')){if(f==='home.html')continue;let h=fs.readFileSync('src/'+f,'utf8');
h=h.replace(/<script id="tc-i18n">[\s\S]*?<\/script>/,'');
{let i=h.indexOf('</title>');if(i<0)h=tag+h;else{i+=8;h=h.slice(0,i)+tag+h.slice(i)}
 h=h.replace(/(<template[^>]*>[\s\S]*?<\/title>)/g,m=>m+tag);}
h=require('./patch.js')(f,h);fs.writeFileSync('out/'+f,h)}
console.log(Object.keys(D).length,'entries',js.length,'bytes')
