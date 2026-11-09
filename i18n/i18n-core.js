(function(){
var W=window;if(W.TCI18N)return;
var KEY="tc-lang",OK={en:1,it:1,es:1,el:1},L="en";
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
try{var h=location.hash,m=h.match(/[#&]lang=(en|it|es|el)\b/);if(m){L=m[1];ls(KEY,L);var nh=h.replace(/&?lang=(en|it|es|el)\b/,"").replace(/^#&/,"#");if(nh==="#")nh="";try{history.replaceState(history.state,"",location.pathname+location.search+nh)}catch(e){}}else{var s=ls(KEY);if(s&&OK[s])L=s}}catch(e){}
try{if(W.parent!==W&&W.parent.TCI18N)L=W.parent.TCI18N.lang}catch(e){}
var D=W.TCI18N_DICT||{},I={it:0,es:1,el:2};
var MS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],MF=["January","February","March","April","May","June","July","August","September","October","November","December"];
var M={it:["gen","feb","mar","apr","mag","giu","lug","ago","set","ott","nov","dic"],es:["ene","feb","mar","abr","may","jun","jul","ago","sept","oct","nov","dic"]};
var MFL={it:["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"],es:["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]};
var DS=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],DF=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
var DY={it:["Lun","Mar","Mer","Gio","Ven","Sab","Dom"],es:["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"]};
var DFL={it:["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"],es:["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]};
function dt(s,l){if(l==="el")return dtEl(s);var r=s.replace(/\b(January|February|March|April|May|June|July|August|September|October|November|December)\b( (\d{4}))?/g,function(_,m,y,yy){return MFL[l][MF.indexOf(m)]+(yy?(l==="es"?" de ":" ")+yy:"")});
r=r.replace(/\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/g,function(m){return DFL[l][DF.indexOf(m)]});
r=r.replace(/\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b/g,function(m){return DY[l][DS.indexOf(m)]});
r=r.replace(/\b(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b/g,function(_,d,m){return d+" "+M[l][MS.indexOf(m)]});
r=r.replace(/^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4})$/,function(_,m,y){return M[l][MS.indexOf(m)]+" "+y});
r=r.replace(/^(Today|Tomorrow|Yesterday|today|tomorrow)\b/,function(m){var w={Today:["Oggi","Hoy"],Tomorrow:["Domani","Mañana"],Yesterday:["Ieri","Ayer"],today:["oggi","hoy"],tomorrow:["domani","mañana"]}[m];return w[I[l]]});
return r}
var ISDATE=/^(((Mon|Tue|Wed|Thu|Fri|Sat|Sun|Today|Tomorrow|Yesterday|today|tomorrow|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b,? ?)?((\d{1,2} )?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\b( \d{4})?)?,? ?(at )?(\d{1,2}:\d\d( ?[AP]M)?)?)$/;
var NM="([A-Z][A-Za-zÀ-ÿ'’.-]*(?: [A-Z][A-Za-zÀ-ÿ'’.-]*)?)";
function pl(n,a,b){return +n===1?a:b}
function W2(w,l){var t=D[w];return t?t[I[l]]:w}
var P=[
[/^(\d+) (?:chairs?|seats?) free$/,function(m){return [m[1]+pl(m[1]," posto libero"," posti liberi"),m[1]+pl(m[1]," sitio libre"," sitios libres")]}],
[/^(\d+) of (\d+) (?:chairs|seats) free$/,function(m){return [m[1]+" di "+m[2]+" posti liberi",m[1]+" de "+m[2]+" sitios libres"]}],
[/^(\d+) of (\d+) (?:chairs|seats)$/,function(m){return [m[1]+" di "+m[2]+" posti",m[1]+" de "+m[2]+" plazas"]}],
[/^(\d+) of (\d+) free$/,function(m){return [m[1]+" di "+m[2]+" liberi",m[1]+" de "+m[2]+" libres"]}],
[/^(\d+) free$/,function(m){return [m[1]+pl(m[1]," libero"," liberi"),m[1]+pl(m[1]," libre"," libres")]}],
[/^(\d+) invited$/,function(m){return [m[1]+pl(m[1]," invitato"," invitati"),m[1]+pl(m[1]," invitado"," invitados")]}],
[/^(\d+) (people|persons?)$/,function(m){return [m[1]+pl(m[1]," persona"," persone"),m[1]+pl(m[1]," persona"," personas")]}],
[/^(\d+) tables?$/,function(m){return [m[1]+pl(m[1]," tavolo"," tavoli"),m[1]+pl(m[1]," mesa"," mesas")]}],
[/^(\d+) open tables?$/,function(m){return [m[1]+pl(m[1]," tavolo aperto"," tavoli aperti"),m[1]+pl(m[1]," mesa abierta"," mesas abiertas")]}],
[/^(\d+) guests?$/,function(m){return [m[1]+pl(m[1]," ospite"," ospiti"),m[1]+pl(m[1]," invitado"," invitados")]}],
[/^(\d+) coming$/,function(m){return [m[1]+" in arrivo",m[1]+pl(m[1]," viene"," vienen")]}],
[/^(\d+) at the table$/,function(m){return [m[1]+" al tavolo",m[1]+" en la mesa"]}],
[/^(\d+) (books|themes|notes?)$/,function(m){var w={books:["libri","libros"],themes:["temi","temas"],note:["nota","nota"],notes:["note","notas"]}[m[2]];return [m[1]+" "+w[0],m[1]+" "+w[1]]}],
[/^(\d+) min in$/,function(m){return ["da "+m[1]+" min","desde hace "+m[1]+" min"]}],
[/^(In|in) (\d+) min$/,function(m){return [(m[1]==="In"?"Tra ":"tra ")+m[2]+" min",(m[1]==="In"?"En ":"en ")+m[2]+" min"]}],
[/^(In|in) (\d+) ?h(?: (\d+) ?m(?:in)?)?$/,function(m){var x=m[2]+" h"+(m[3]?" "+m[3]+" min":"");return [(m[1]==="In"?"Tra ":"tra ")+x,(m[1]==="In"?"En ":"en ")+x]}],
[/^(Today|Tomorrow), in (\d+) (h|min)$/,function(m){return [(m[1]==="Today"?"Oggi":"Domani")+", tra "+m[2]+" "+m[3],(m[1]==="Today"?"Hoy":"Mañana")+", en "+m[2]+" "+m[3]]}],
[/^Starting in (\d+) min$/,function(m){return ["Inizia tra "+m[1]+" min","Empieza en "+m[1]+" min"]}],
[/^Starts in (\d+) min$/,function(m){return ["Inizia tra "+m[1]+" min","Empieza en "+m[1]+" min"]}],
[/^Step (\d+) of (\d+)$/,function(m){return ["Passo "+m[1]+" di "+m[2],"Paso "+m[1]+" de "+m[2]]}],
[/^You tipped (\d+)$/,function(m){return ["Hai dato "+m[1],"Diste "+m[1]]}],
[/^\+(\d+) this week$/,function(m){return ["+"+m[1]+" questa settimana","+"+m[1]+" esta semana"]}],
[/^Show (.+) only, (\d+)$/,function(m,l){return null}],
[/^(?:M|m)ember since (.+)$/,function(m){return ["Membro da "+dt(m[1],"it"),"Miembro desde "+dt(m[1],"es")]}],
[/^Following since (.+)$/,function(m){return ["Segui da "+dt(m[1],"it"),"Siguiendo desde "+dt(m[1],"es")]}],
[/^Blocked (\d.+)$/,function(m){return ["Bloccato il "+dt(m[1],"it"),"Bloqueado el "+dt(m[1],"es")]}],
[/^Met at “(.+)”$/,function(m){return ["Al tavolo “"+m[1]+"”","En la mesa “"+m[1]+"”"]}],
[/^Hosts (.+)$/,function(m){return ISDATE.test(m[1])?["Ospita "+dt(m[1],"it").replace(/^Oggi/,"oggi").replace(/^Domani/,"domani"),"Organiza "+dt(m[1],"es").replace(/^Hoy/,"hoy").replace(/^Mañana/,"mañana")]:null}],
[/^Active (\d+)(h|m|d) ago$/,function(m){return ["Attivo "+m[1]+" "+m[2]+" fa","Activo hace "+m[1]+" "+m[2]]}],
[/^Welcome, (.+)\. Your universe has begun\.$/,function(m){return ["Ciao "+m[1]+", il tuo universo è nato.","Hola, "+m[1]+". Tu universo ha comenzado."]}],
[/^Add “(.+)”$/,function(m){return ["Aggiungi “"+m[1]+"”","Añadir “"+m[1]+"”"]}],
[/^Loved by people who talk about (.+)$/,function(m){return ["Amato da chi parla di "+m[1],"Favorito de quienes hablan de "+m[1]]}],
[/^Exported (\d+) kept notes?$/,function(m){return ["Esportate "+m[1]+" note tenute","Exportadas "+m[1]+" notas guardadas"]}],
[/^Sent to (\d+) guests$/,function(m){return ["Inviato a "+m[1]+" ospiti","Enviado a "+m[1]+" invitados"]}],
[/^Saved\. (\d+) guests will be told\.$/,function(m){return ["Salvato. "+m[1]+" ospiti verranno avvisati.","Guardado. Se avisará a "+m[1]+" invitados."]}],
[/^Saved (.+\..+)$/,function(m){return ["Salvato "+m[1],"Guardado "+m[1]]}],
[/^Sent to (.+)$/,function(m){return ["Inviato a "+m[1],"Enviado a "+m[1]]}],
[new RegExp("^"+NM+" tipped you (\\d+) TimeCoins?$"),function(m){return [m[1]+" ti ha dato "+m[2]+" TimeCoins",m[1]+" te ha dado "+m[2]+" TimeCoins"]}],
[new RegExp("^"+NM+" was removed from the table$"),function(m){return [m[1]+" è stato rimosso dal tavolo","Se ha quitado a "+m[1]+" de la mesa"]}],
[new RegExp("^Open "+NM+"['’]s profile$"),function(m){return ["Apri il profilo di "+m[1],"Abrir el perfil de "+m[1]]}],
[new RegExp("^"+NM+"['’]s camera$"),function(m){return ["Videocamera di "+m[1],"Cámara de "+m[1]]}],
[new RegExp("^"+NM+" only$"),function(m){return ["Solo "+m[1],"Solo "+m[1]]}],
[new RegExp("^Remove "+NM+" from the table$"),function(m){return ["Rimuovi "+m[1]+" dal tavolo","Quitar a "+m[1]+" de la mesa"]}],
[new RegExp("^(Mute|Unmute|Message|Remove|Unfollow|Ask|Block|Report|Chat with|Follow) "+NM+"(\\??)$"),function(m){var v={Mute:["Silenzia ","Silenciar a "],Unmute:["Riattiva ","Activar audio a "],Message:["Scrivi a ","Escribir a "],Remove:["Rimuovi ","Quitar a "],Unfollow:["Non seguire più ","Dejar de seguir a "],Ask:["Chiedi a ","Preguntar a "],Block:["Blocca ","Bloquear a "],Report:["Segnala ","Denunciar a "],"Chat with":["Chatta con ","Chatear con "],Follow:["Segui ","Seguir a "]}[m[1]];return m[3]?[v[0]+m[2]+"?","¿"+v[1]+m[2]+"?"]:[v[0]+m[2],v[1]+m[2]]}],
[new RegExp("^One TimeCoin (more|less) for "+NM+"$"),function(m){return m[1]==="more"?["Un TimeCoin in più per "+m[2],"Un TimeCoin más para "+m[2]]:["Un TimeCoin in meno per "+m[2],"Un TimeCoin menos para "+m[2]]}],
[/^You muted (.+)$/,function(m){return ["Hai silenziato "+m[1],"Has silenciado a "+m[1]]}],
[/^(.+) can speak again$/,function(m){return [m[1]+" può parlare di nuovo",m[1]+" puede volver a hablar"]}],
[/^(.+) was muted by the host$/,function(m){return [m[1]+" è stato silenziato dall'host","El anfitrión ha silenciado a "+m[1]]}],
[/^Asked the table at (.+)\.$/,function(m){return ["Chiesto al tavolo alle "+m[1]+".","Preguntado a la mesa a las "+m[1]+"."]}],
[/^Only (.+) sees it\.$/,function(m){return ["La vede solo "+m[1]+".","Solo la ve "+m[1]+"."]}],
[/^(.+) put it to the table\.$/,function(m){return [m[1]+" l'ha proposta al tavolo.",m[1]+" la planteó a la mesa."]}],
[/^Question from (you|.+)$/,function(m){return m[1]==="you"?["Domanda tua","Pregunta tuya"]:["Domanda da "+m[1],"Pregunta de "+m[1]]}],
[/^asked by (you|.+)$/,function(m){return m[1]==="you"?["chiesta da te","hecha por ti"]:["chiesta da "+m[1],"hecha por "+m[1]]}],
[/^Added to the transcript, under (.+)'s line$/,function(m){return ["Aggiunta alla trascrizione, sotto la frase di "+m[1],"Añadida a la transcripción, bajo la frase de "+m[1]]}],
[/^You asked a question from (.+)$/,function(m){return ["Hai posto una domanda di "+m[1],"Has planteado una pregunta de "+m[1]]}],
[/^hosted by (.+)$/,function(m){return ["ospitato da "+m[1],"organizada por "+m[1]]}],
[/^Hosted by (.+)$/,function(m){return ["Ospitato da "+m[1],"Organizada por "+m[1]]}],
[/^Nothing matches "(.+)"$/,function(m){return ["Nessun risultato per \""+m[1]+"\"","Nada coincide con \""+m[1]+"\""]}],
[/^Goes to the (\d+) people coming to "(.+)"\.$/,function(m){return ["Va alle "+m[1]+" persone che vengono a \""+m[2]+"\".","Llega a las "+m[1]+" personas que vienen a \""+m[2]+"\"."]}],
[/^On the waitlist, (\d+)(?:nd|th|rd|st) in line$/,function(m){return ["In lista d'attesa, "+m[1]+"° in fila","En la lista de espera, "+m[1]+".º en la cola"]}],
[/^You joined$/,function(m){return ["Hai partecipato","Participaste"]}],
[/^Your chair is saved$/,function(m){return ["Il tuo posto è tenuto","Tu sitio está reservado"]}],
[/^Hosts tables on TimeCapsule from (.+)\.$/,function(m){return ["Ospita tavoli su TimeCapsule da "+m[1]+".","Organiza mesas en TimeCapsule desde "+m[1]+"."]}],
[/^You stopped following (.+)$/,function(m){return ["Non segui più "+m[1],"Has dejado de seguir a "+m[1]]}],
[/^We'll tell you when (.+) hosts next$/,function(m){return ["Ti avviseremo quando "+m[1]+" ospiterà di nuovo","Te avisaremos cuando "+m[1]+" organice otra mesa"]}],
[/^Showing the (\d+) (.+) feedbacks$/,function(m){var a=D[m[2]]||D[m[2].charAt(0).toUpperCase()+m[2].slice(1)];var w=a?[a[0].toLowerCase(),a[1].toLowerCase()]:[m[2],m[2]];return ["Mostro i "+m[1]+" feedback \""+w[0]+"\"","Mostrando las "+m[1]+" opiniones \""+w[1]+"\""]}],
[/^We sent a link to (.+)\. Your email changes once you open it\.$/,function(m){return ["Abbiamo inviato un link a "+m[1]+". L'email cambia quando lo apri.","Hemos enviado un enlace a "+m[1]+". Tu correo cambiará cuando lo abras."]}],
[/^For "(.+)"$/,function(m){return ["Per \""+m[1]+"\"","Para \""+m[1]+"\""]}],
[/^(.+) at (\d{1,2}:\d\d)$/,function(m){if(!ISDATE.test(m[1]))return null;return [dt(m[1],"it")+" alle "+m[2],dt(m[1],"es")+" a las "+m[2]]}],
[/^with (.+)$/,function(m){return ["con "+m[1],"con "+m[1]]}],
[/^More for (.+)$/,function(m){return ["Altro per "+m[1],"Más opciones para "+m[1]]}],
[/^Open (.+)$/,function(m){return ["Apri "+m[1],"Abrir "+m[1]]}],
[/^Thanks for joining, (.+)$/,function(m){return ["Grazie di esserci, "+m[1],"Gracias por unirte, "+m[1]]}],
[/^Now viewing as (.+), (?:the host|a guest)$/,function(m,s){return null}]
];
var MGS=["Ιαν","Φεβ","Μαρ","Απρ","Μαΐ","Ιουν","Ιουλ","Αυγ","Σεπ","Οκτ","Νοε","Δεκ"],MGG=["Ιανουαρίου","Φεβρουαρίου","Μαρτίου","Απριλίου","Μαΐου","Ιουνίου","Ιουλίου","Αυγούστου","Σεπτεμβρίου","Οκτωβρίου","Νοεμβρίου","Δεκεμβρίου"],MGN=["Ιανουάριος","Φεβρουάριος","Μάρτιος","Απρίλιος","Μάιος","Ιούνιος","Ιούλιος","Αύγουστος","Σεπτέμβριος","Οκτώβριος","Νοέμβριος","Δεκέμβριος"];
var DGS=["Δευ","Τρί","Τετ","Πέμ","Παρ","Σάβ","Κυρ"],DGF=["Δευτέρα","Τρίτη","Τετάρτη","Πέμπτη","Παρασκευή","Σάββατο","Κυριακή"];
function dtEl(s){var MFR="(January|February|March|April|May|June|July|August|September|October|November|December)";
var r=s.replace(new RegExp("\\b(\\d{1,2}) "+MFR+"\\b","g"),function(_,d,m){return d+" "+MGG[MF.indexOf(m)]});
r=r.replace(new RegExp("\\b"+MFR+"\\b","g"),function(m){return MGN[MF.indexOf(m)]});
r=r.replace(/\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/g,function(m){return DGF[DF.indexOf(m)]});
r=r.replace(/\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b/g,function(m){return DGS[DS.indexOf(m)]});
r=r.replace(/\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b/g,function(m){return MGS[MS.indexOf(m)]});
r=r.replace(/\bat (\d{1,2}:\d\d)/,"στις $1");
r=r.replace(/^(Today|Tomorrow|Yesterday|today|tomorrow)\b/,function(m){return {Today:"Σήμερα",Tomorrow:"Αύριο",Yesterday:"Χθες",today:"σήμερα",tomorrow:"αύριο"}[m]});
return r}
function accEl(s){return s.replace(/(Ιανουάρι|Φεβρουάρι|Μάρτι|Απρίλι|Μάι|Ιούνι|Ιούλι|Αύγουστ|Σεπτέμβρι|Οκτώβρι|Νοέμβρι|Δεκέμβρι)ος/g,"$1ο")}
function artEl(x){return /^\d/.test(x)?"τις ":/^(January|February|March|April|May|June|July|August|September|October|November|December)\b/.test(x)?"τον ":""}
function lc1(s){return s.replace(/^Σήμερα/,"σήμερα").replace(/^Αύριο/,"αύριο")}
var PE=[
[/^(\d+) (?:chairs?|seats?) free$/,function(m){return m[1]+pl(m[1]," ελεύθερη καρέκλα"," ελεύθερες καρέκλες")}],
[/^(\d+) of (\d+) (?:chairs|seats) free$/,function(m){return m[1]+" από "+m[2]+" καρέκλες ελεύθερες"}],
[/^(\d+) of (\d+) (?:chairs|seats)$/,function(m){return m[1]+" από "+m[2]+" καρέκλες"}],
[/^(\d+) of (\d+) free$/,function(m){return m[1]+" από "+m[2]+" ελεύθερες"}],
[/^(\d+) free$/,function(m){return m[1]+pl(m[1]," ελεύθερη"," ελεύθερες")}],
[/^(\d+) invited$/,function(m){return m[1]+pl(m[1]," προσκεκλημένος"," προσκεκλημένοι")}],
[/^(\d+) (people|persons?)$/,function(m){return m[1]+pl(m[1]," άτομο"," άτομα")}],
[/^(\d+) tables?$/,function(m){return m[1]+pl(m[1]," τραπέζι"," τραπέζια")}],
[/^(\d+) open tables?$/,function(m){return m[1]+pl(m[1]," ανοιχτό τραπέζι"," ανοιχτά τραπέζια")}],
[/^(\d+) guests?$/,function(m){return m[1]+pl(m[1]," καλεσμένος"," καλεσμένοι")}],
[/^(\d+) coming$/,function(m){return m[1]+pl(m[1]," έρχεται"," έρχονται")}],
[/^(\d+) at the table$/,function(m){return m[1]+" στο τραπέζι"}],
[/^(\d+) (books|themes|notes?)$/,function(m){return m[1]+" "+{books:"βιβλία",themes:"θέματα",note:"σημείωση",notes:"σημειώσεις"}[m[2]]}],
[/^(\d+) min in$/,function(m){return "εδώ και "+m[1]+" λεπ."}],
[/^(In|in) (\d+) min$/,function(m){return (m[1]==="In"?"Σε ":"σε ")+m[2]+" λεπ."}],
[/^(In|in) (\d+) ?h(?: (\d+) ?m(?:in)?)?$/,function(m){return (m[1]==="In"?"Σε ":"σε ")+m[2]+" ώρ."+(m[3]?" "+m[3]+" λεπ.":"")}],
[/^(Today|Tomorrow), in (\d+) (h|min)$/,function(m){return (m[1]==="Today"?"Σήμερα":"Αύριο")+", σε "+m[2]+(m[3]==="h"?" ώρ.":" λεπ.")}],
[/^Starting in (\d+) min$/,function(m){return "Ξεκινά σε "+m[1]+" λεπ."}],
[/^Starts in (\d+) min$/,function(m){return "Ξεκινά σε "+m[1]+" λεπ."}],
[/^Step (\d+) of (\d+)$/,function(m){return "Βήμα "+m[1]+" από "+m[2]}],
[/^You tipped (\d+)$/,function(m){return "Έδωσες "+m[1]}],
[/^\+(\d+) this week$/,function(m){return "+"+m[1]+" αυτή την εβδομάδα"}],
[/^Show (.+) only, (\d+)$/,function(m){return null}],
[/^(?:M|m)ember since (.+)$/,function(m){return "Μέλος από "+artEl(m[1])+accEl(dtEl(m[1]))}],
[/^Following since (.+)$/,function(m){return "Ακολουθείς από "+artEl(m[1])+accEl(dtEl(m[1]))}],
[/^Blocked (\d.+)$/,function(m){return "Αποκλείστηκε στις "+dtEl(m[1])}],
[/^Met at “(.+)”$/,function(m){return "Στο τραπέζι «"+m[1]+"»"}],
[/^Hosts (.+)$/,function(m){return ISDATE.test(m[1])?"Φιλοξενεί "+lc1(dtEl(m[1])):null}],
[/^Active (\d+)(h|m|d) ago$/,function(m){return "Ενεργός πριν από "+m[1]+" "+{h:"ώρ.",m:"λεπ.",d:"ημ."}[m[2]]}],
[/^Welcome, (.+)\. Your universe has begun\.$/,function(m){return "Καλώς ήρθες, "+m[1]+". Το σύμπαν σου ξεκίνησε."}],
[/^Add “(.+)”$/,function(m){return "Προσθήκη «"+m[1]+"»"}],
[/^Loved by people who talk about (.+)$/,function(m){return "Αγαπημένο όσων μιλούν για "+m[1]}],
[/^Exported (\d+) kept notes?$/,function(m){return "Εξήχθησαν "+m[1]+pl(m[1]," σημείωση"," σημειώσεις")}],
[/^Sent to (\d+) guests$/,function(m){return "Στάλθηκε σε "+m[1]+" καλεσμένους"}],
[/^Saved\. (\d+) guests will be told\.$/,function(m){return "Αποθηκεύτηκε. Θα ενημερωθούν "+m[1]+" καλεσμένοι."}],
[/^Saved (.+\..+)$/,function(m){return "Αποθηκεύτηκε: "+m[1]}],
[/^Sent to (.+)$/,function(m){return "Στάλθηκε σε: "+m[1]}],
[new RegExp("^"+NM+" tipped you (\\d+) TimeCoins?$"),function(m){return m[1]+" σου έδωσε "+m[2]+" TimeCoins"}],
[new RegExp("^"+NM+" was removed from the table$"),function(m){return m[1]+": αφαιρέθηκε από το τραπέζι"}],
[new RegExp("^Open "+NM+"['’]s profile$"),function(m){return "Άνοιξε το προφίλ: "+m[1]}],
[new RegExp("^"+NM+"['’]s camera$"),function(m){return "Κάμερα: "+m[1]}],
[new RegExp("^"+NM+" only$"),function(m){return "Μόνο "+m[1]}],
[new RegExp("^Remove "+NM+" from the table$"),function(m){return "Αφαίρεση από το τραπέζι: "+m[1]}],
[new RegExp("^(Mute|Unmute|Message|Remove|Unfollow|Ask|Block|Report|Chat with|Follow) "+NM+"(\\??)$"),function(m){var v={Mute:"Σίγαση: ",Unmute:"Άρση σίγασης: ",Message:"Μήνυμα: ",Remove:"Αφαίρεση: ",Unfollow:"Διακοπή ακολούθησης: ",Ask:"Ερώτηση: ",Block:"Αποκλεισμός: ",Report:"Αναφορά: ","Chat with":"Συζήτηση με ",Follow:"Ακολούθησε: "}[m[1]];return v+m[2]+(m[3]?";":"")}],
[new RegExp("^One TimeCoin (more|less) for "+NM+"$"),function(m){return "Ένα TimeCoin "+(m[1]==="more"?"παραπάνω":"λιγότερο")+" για "+m[2]}],
[/^You muted (.+)$/,function(m){return "Σίγαση από εσένα: "+m[1]}],
[/^(.+) can speak again$/,function(m){return m[1]+": μπορεί να μιλήσει ξανά"}],
[/^(.+) was muted by the host$/,function(m){return "Ο οικοδεσπότης έβαλε σε σίγαση: "+m[1]}],
[/^Asked the table at (.+)\.$/,function(m){return "Ρώτησες το τραπέζι στις "+m[1]+"."}],
[/^Only (.+) sees it\.$/,function(m){return "Τη βλέπει μόνο: "+m[1]+"."}],
[/^(.+) put it to the table\.$/,function(m){return m[1]+": την έθεσε στο τραπέζι."}],
[/^Question from (you|.+)$/,function(m){return m[1]==="you"?"Δική σου ερώτηση":"Ερώτηση από "+m[1]}],
[/^asked by (you|.+)$/,function(m){return m[1]==="you"?"από εσένα":"από "+m[1]}],
[/^Added to the transcript, under (.+)'s line$/,function(m){return "Προστέθηκε στην απομαγνητοφώνηση, κάτω από τη φράση: "+m[1]}],
[/^You asked a question from (.+)$/,function(m){return "Έθεσες μια ερώτηση από "+m[1]}],
[/^hosted by (.+)$/,function(m){return "οικοδεσπότης: "+m[1]}],
[/^Hosted by (.+)$/,function(m){return "Οικοδεσπότης: "+m[1]}],
[/^Nothing matches "(.+)"$/,function(m){return "Κανένα αποτέλεσμα για \""+m[1]+"\""}],
[/^Goes to the (\d+) people coming to "(.+)"\.$/,function(m){return "Πηγαίνει στα "+m[1]+" άτομα που έρχονται στο \""+m[2]+"\"."}],
[/^On the waitlist, (\d+)(?:nd|th|rd|st) in line$/,function(m){return "Στη λίστα αναμονής, "+m[1]+"ος στη σειρά"}],
[/^You joined$/,function(m){return "Μπήκες"}],
[/^Your chair is saved$/,function(m){return "Η καρέκλα σου κρατήθηκε"}],
[/^Hosts tables on TimeCapsule from (.+)\.$/,function(m){return "Φιλοξενεί τραπέζια στο TimeCapsule από "+m[1]+"."}],
[/^You stopped following (.+)$/,function(m){return "Δεν ακολουθείς πια: "+m[1]}],
[/^We'll tell you when (.+) hosts next$/,function(m){return "Θα σου πούμε όταν φιλοξενήσει ξανά: "+m[1]}],
[/^Showing the (\d+) (.+) feedbacks$/,function(m){var a=D[m[2]]||D[m[2].charAt(0).toUpperCase()+m[2].slice(1)];var w=a&&a[2]?a[2].toLowerCase():m[2];return "Εμφανίζονται τα "+m[1]+" σχόλια «"+w+"»"}],
[/^We sent a link to (.+)\. Your email changes once you open it\.$/,function(m){return "Στείλαμε έναν σύνδεσμο στο "+m[1]+". Το email σου αλλάζει μόλις τον ανοίξεις."}],
[/^For "(.+)"$/,function(m){return "Για \""+m[1]+"\""}],
[/^(.+) at (\d{1,2}:\d\d)$/,function(m){if(!ISDATE.test(m[1]))return null;return dtEl(m[1])+" στις "+m[2]}],
[/^with (.+)$/,function(m){return "με "+m[1]}],
[/^More for (.+)$/,function(m){return "Περισσότερα για "+m[1]}],
[/^Open (.+)$/,function(m){return "Άνοιξε "+m[1]}],
[/^Thanks for joining, (.+)$/,function(m){return "Ευχαριστούμε που ήρθες, "+m[1]}],
[/^Now viewing as (.+), (?:the host|a guest)$/,function(m,s){return null}]
];
function pre(s,l){var m=s.match(/^(.+?) \(?(\d+)\)?$/);if(m&&D[m[1]]){var x=D[m[1]][I[l]];if(x==null)return null;return x+s.slice(m[1].length)}return null}
function one(s,l){var t=D[s];if(t&&t[I[l]]!=null)return t[I[l]];if(l==="el"){for(var i=0;i<PE.length;i++){var m=s.match(PE[i][0]);if(m){var r=PE[i][1](m);if(r!=null)return r}}}else for(var i=0;i<P.length;i++){var m=s.match(P[i][0]);if(m){var r=P[i][1](m);if(r)return r[I[l]]}}
var x=pre(s,l);if(x)return x;if(ISDATE.test(s)&&/[A-Za-z]/.test(s)){var d=dt(s,l);if(d!==s)return d}
var sm=s.match(/^Show (.+) only, (\d+)$/);if(sm){var a=D[sm[1]];if(a)return({it:"Mostra solo ",es:"Mostrar solo ",el:"Μόνο "}[l])+a[I[l]]+", "+sm[2]}
return null}
var C={};
function tr(s,l){if(l==="en")return null;var k=l+"\u0001"+s;if(k in C)return C[k];var r=one(s,l);
if(r===null&&s.indexOf("·")>=0){var parts=s.split(/(\s*·\s*)/),ch=false;for(var i=0;i<parts.length;i+=2){var p=parts[i];if(!p)continue;var q=one(p,l);if(q!==null){parts[i]=q;ch=true}}if(ch)r=parts.join("")}
if(r===null&&/[,:]\s/.test(s)){var m2=s.match(/^(.+?)([,:]\s)(.+)$/);if(m2){var a=one(m2[1],l);if(a!==null){var b=one(m2[3],l);r=a+m2[2]+(b===null?m2[3]:b)}}}
C[k]=r;return r}
var TN=new WeakMap(),AT=new WeakMap(),ATTRS=["placeholder","aria-label","title","data-tip"];
var SKIP={SCRIPT:1,STYLE:1,TEXTAREA:1,NOSCRIPT:1,CODE:1,PRE:1};
function skipEl(e){for(;e&&e.nodeType===1;e=e.parentNode){if(SKIP[e.nodeName])return true;if(e.hasAttribute&&e.hasAttribute("data-noi18n"))return true;if(e.isContentEditable)return true}return false}
var busy=false;
function doText(n){var v=n.nodeValue,rec=TN.get(n);if(!v||!(/[A-Za-z]/.test(v)||(rec&&v===rec.t)))return;var base=v;if(rec&&v===rec.t)base=rec.o;
var tm=base.trim();if(!tm)return;var out;
if(L==="en"){out=base}else{var t=null,pb=n.parentNode&&n.parentNode.closest&&n.parentNode.closest("[aria-pressed]");if(pb&&D[tm+"@btn"])t=D[tm+"@btn"][I[L]];if(t===null)t=tr(tm,L);if(t===null){out=base}else{var i=base.indexOf(tm);out=base.slice(0,i)+t+base.slice(i+tm.length)}}
if(out!==v){if(skipEl(n.parentNode))return;n.nodeValue=out}
if(out!==base)TN.set(n,{o:base,t:out});else if(rec)TN.delete(n)}
function doAttr(e,a){var v=e.getAttribute(a);if(v==null)return;var m=AT.get(e);if(!/[A-Za-z]/.test(v)&&!(m&&m[a]&&m[a].t===v))return;if(!m){m={};AT.set(e,m)}var rec=m[a],base=v;if(rec&&v===rec.t)base=rec.o;
var out=L==="en"?base:(tr(base.trim(),L)||base);if(out!==v)e.setAttribute(a,out);if(out!==base)m[a]={o:base,t:out};else delete m[a]}
function walk(root){if(root.nodeType===3){doText(root);return}if(root.nodeType!==1&&root.nodeType!==9&&root.nodeType!==11)return;if(root.nodeType===1&&SKIP[root.nodeName])return;
var w=document.createTreeWalker(root,5,null),n=root.nodeType===1?root:w.nextNode();
for(;n;n=w.nextNode()){if(n.nodeType===3){var p=n.parentNode;if(p&&SKIP[p.nodeName])continue;doText(n)}else{if(SKIP[n.nodeName])continue;for(var i=0;i<ATTRS.length;i++)if(n.hasAttribute(ATTRS[i]))doAttr(n,ATTRS[i])}}}
function src(el){if(!el)return"";if(el.nodeType===3){var r=TN.get(el);return r&&el.nodeValue===r.t?r.o:el.nodeValue}var s="",w=document.createTreeWalker(el,4,null),n;while(n=w.nextNode())s+=src(n);return s}
function u(url){if(!url||!/claude\.ai\/(code\/)?artifact\//.test(url))return url;url=url.replace(/([#&])lang=(en|it|es|el)\b/,"$1").replace(/[#&]$/,"").replace("#&","#");return url+(url.indexOf("#")>=0?"&":"#")+"lang="+L}
var mo=new MutationObserver(function(rs){if(busy)return;busy=true;try{for(var i=0;i<rs.length;i++){var r=rs[i];if(r.type==="childList"){for(var j=0;j<r.addedNodes.length;j++)walk(r.addedNodes[j])}else if(r.type==="characterData"){doText(r.target)}else if(r.type==="attributes"){doAttr(r.target,r.attributeName)}}}finally{mo.takeRecords();busy=false}});
function start(){mo.observe(document.documentElement,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:ATTRS})}
function all(){busy=true;try{walk(document.body||document.documentElement)}finally{mo.takeRecords();busy=false}}
function setLang(l){if(!OK[l])l="en";L=l;ls(KEY,l);document.documentElement.lang=l;all();try{W.dispatchEvent(new CustomEvent("tc-lang",{detail:l}))}catch(e){}}
document.addEventListener("click",function(e){var t=e.target;if(!t||!t.closest)return;var a=t.closest("a[href],[data-href],[onclick]");if(!a)return;
if(a.hasAttribute("href")){var h=a.getAttribute("href");var nh=u(h);if(nh!==h)a.setAttribute("href",nh)}
if(a.hasAttribute("data-href")){var d=a.getAttribute("data-href"),nd=u(d);if(nd!==d)a.setAttribute("data-href",nd)}
if(a.hasAttribute("onclick")){var o=a.getAttribute("onclick"),no=o.replace(/https:\/\/claude\.ai\/(?:code\/)?artifact\/[A-Za-z0-9-]+(?:#[^'"]*)?/g,function(x){return u(x)});if(no!==o)a.setAttribute("onclick",no)}},true);
W.TCI18N={get lang(){return L},set:setLang,t:function(s){return L==="en"?s:(tr(s,L)||s)},src:src,u:u,refresh:all,isT:function(n){var r=TN.get(n);return !!(r&&n.nodeValue===r.t)}};
document.documentElement.lang=L;start();
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",all);else all();
/* language picker: avatar menu, or the page header when there is no menu */
var LBL={en:"Language",it:"Lingua",es:"Idioma",el:"Γλώσσα"};
function syncLP(){var bs=document.querySelectorAll(".tc-lp button");for(var i=0;i<bs.length;i++)bs[i].setAttribute("aria-pressed",bs[i].getAttribute("data-l")===L);var ls2=document.querySelectorAll(".tc-lp .tc-lpl");for(var j=0;j<ls2.length;j++)ls2[j].textContent=LBL[L];var s=document.getElementById("applang");if(s)s.value=L}
function mkLP(cls){var d=document.createElement("div");d.className="tc-lp "+cls;d.setAttribute("data-noi18n","");d.setAttribute("role","group");d.setAttribute("aria-label","Language");
d.innerHTML=(cls==="m"?'<span class="tc-lpl"></span>':'')+'<span class="tc-seg"><button type="button" data-l="en" title="English">EN</button><button type="button" data-l="it" title="Italiano">IT</button><button type="button" data-l="es" title="Español">ES</button><button type="button" data-l="el" title="Ελληνικά">EL</button></span>';
d.addEventListener("click",function(e){var b=e.target.closest("button[data-l]");if(!b)return;e.preventDefault();e.stopPropagation();setLang(b.getAttribute("data-l"))});return d}
function addLP(){if(document.querySelector(".tc-lp")||/^about:/.test(location.href))return;
var st=document.createElement("style");st.textContent="/*tc-el-fonts*/"+'.tc-lp{display:flex;align-items:center;gap:10px;font-family:inherit}.tc-lp.m{justify-content:space-between;min-height:40px;padding:0 6px 0 10px;font-size:14px;color:#EEF1FF}.tc-lp.h{margin-left:auto;flex:none}.tc-seg{display:inline-flex;padding:2px;border-radius:9px;border:1px solid #3A4175;background:rgba(255,255,255,.03)}.tc-seg button{border:0;background:none;color:#A9B0D6!important;font:inherit;font-size:12px!important;font-weight:600!important;letter-spacing:.04em;height:26px;min-width:32px;padding:0 6px;border-radius:7px;cursor:pointer}.tc-seg button:hover{color:#EEF1FF!important}.tc-seg button[aria-pressed=true]{background:#EEF1FF!important;color:#1B2144!important}';
document.head.appendChild(st);
var menu=document.querySelector(".tch-menu");
if(menu){var hr=menu.querySelector("hr");menu.insertBefore(mkLP("m"),hr||null)}
else{var hs=document.querySelectorAll("header"),h=null;for(var i=0;i<hs.length;i++){if(!hs[i].closest(".rtpop")&&!hs[i].closest("template")){h=hs[i];break}}
if(!h)h=document.querySelector("header");if(h){var lp=mkLP("h"),tt=h.querySelector(".ttl"),end=h.querySelector(".rtx");if(tt)tt.appendChild(lp);else if(end){lp.style.marginLeft="0";h.insertBefore(lp,end)}else h.appendChild(lp)}}
syncLP()}
W.addEventListener("tc-lang",syncLP);
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",addLP);else addLP();
})();
