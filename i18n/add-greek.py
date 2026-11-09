# Adds Greek (EL) to built TimeCapsule pages that carry the shared tc-i18n script.
# Usage: python3 add-greek.py page1.html [page2.html ...]   (edits the files in place, safe to run twice)
# What it does, per page:
#  - every TCI18N_DICT entry [it, es] becomes [it, es, el] using dict-el.txt (English|Greek)
#  - patches the i18n core: el accepted in #lang=, Greek dates, Greek count/name patterns,
#    EN/IT/ES/EL switcher, Greek glyphs for Sora and Newsreader (Manrope / Literata Greek subsets)
#  - Settings "App language" select gets Ελληνικά; FAQ language answer mentions Greek
import re, json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
EL = {}
for ln in open(os.path.join(HERE, 'dict-el.txt'), encoding='utf8'):
    ln = ln.rstrip('\n')
    if ln.strip():
        e, g = ln.split('|', 1); EL[e] = g
FAQ_OLD = 'The app itself is in English, Italian and Spanish:'
FAQ_NEW = 'The app itself is in English, Italian, Spanish and Greek:'
FAQ_KEY = 'Each table shows its language before you sit down. The app itself is in English, Italian, Spanish and Greek: switch it in the menu under your photo or in Settings.'
FAQ_ITES = ["Ogni tavolo mostra la sua lingua prima che ti sieda. L'app è in inglese, italiano, spagnolo e greco: cambiala dal menu sotto la tua foto o in Impostazioni.",
            "Cada mesa muestra su idioma antes de que te sientes. La app está en inglés, italiano, español y griego: cámbiala en el menú de tu foto o en Ajustes."]

GREEK_JS = r'''
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
'''.strip('\n')

GR_RANGE = "U+0370-0377,U+037A-037F,U+0384-038A,U+038C,U+038E-03A1,U+03A3-03FF,U+1F00-1FFF"
GR_SRC = {
    ('Sora', 'normal'): "https://fonts.gstatic.com/s/manrope/v23/xn7gYHE41ni1AdIRggSxSuXd.woff2",
    ('Newsreader', 'normal'): "https://fonts.gstatic.com/s/literata/v40/or3PQ6P12-iJxAIgLa78DkTtAoDhk0oVpaK3YLanFLHpPf2TbLi4J_LWTFCW.woff2",
    ('Newsreader', 'italic'): "https://fonts.gstatic.com/s/literata/v40/or3yQ6P12-iJxAIgLYT1PLs1a-t7PU0AbeE9KK5X5ClqOw.woff2",
}
DEFAULT_W = {('Sora', 'normal'): ['100 800'], ('Newsreader', 'normal'): ['200 800'], ('Newsreader', 'italic'): ['200 800']}

def page_weights(html):
    """Greek faces must use the SAME weight descriptors the page loads from Google Fonts.
    A wider range (100 800) wins font matching at weights the Latin face lacks and
    knocks Latin text off Sora/Newsreader."""
    out = {}
    for url in re.findall(r'fonts\.googleapis\.com/css2\?([^"\')\s]*)', html):
        for fam in re.findall(r'family=([^&]*)', url):
            name, _, spec = fam.partition(':')
            name = name.replace('+', ' ')
            if name not in ('Sora', 'Newsreader') or '@' not in spec:
                continue
            axes, vals = spec.split('@', 1)
            axes = axes.split(',')
            for tup in vals.split(';'):
                v = dict(zip(axes, tup.split(',')))
                st = 'italic' if v.get('ital') == '1' else 'normal'
                w = v.get('wght', '400').replace('..', ' ')
                out.setdefault((name, st), [])
                if w not in out[(name, st)]:
                    out[(name, st)].append(w)
    return out

def font_css(html):
    pw = page_weights(html)
    r = ''
    for key, src in GR_SRC.items():
        for w in pw.get(key) or (DEFAULT_W[key] if key[0] not in {k[0] for k in pw} else []):
            r += ("@font-face{font-family:'%s';font-style:%s;font-weight:%s;font-display:swap;"
                  "src:url(%s) format('woff2');unicode-range:%s}" % (key[0], key[1], w, src, GR_RANGE))
    return r


# Greek text has no Latin letters: the core used to skip such nodes, so they could never be restored to English.
RESTORE_FIX = [
    ('function doText(n){var v=n.nodeValue;if(!v||!/[A-Za-z]/.test(v))return;var rec=TN.get(n),base=v;',
     'function doText(n){var v=n.nodeValue,rec=TN.get(n);if(!v||!(/[A-Za-z]/.test(v)||(rec&&v===rec.t)))return;var base=v;'),
    ('function doAttr(e,a){var v=e.getAttribute(a);if(v==null||!/[A-Za-z]/.test(v))return;var m=AT.get(e);if(!m){m={};AT.set(e,m)}',
     'function doAttr(e,a){var v=e.getAttribute(a);if(v==null)return;var m=AT.get(e);if(!/[A-Za-z]/.test(v)&&!(m&&m[a]&&m[a].t===v))return;if(!m){m={};AT.set(e,m)}'),
]
def fix_restore(t):
    for a, b in RESTORE_FIX:
        t = t.replace(a, b)
    return t

FONT_MARK = "/*tc-el-fonts*/"

def patch_core(c):
    if 'el:2' in c:
        return c
    def rep(a, b, cnt=1):
        nonlocal c
        n = c.count(a)
        assert n >= 1, 'core: missing ' + a[:70]
        if cnt == 1: assert n == 1, 'core: ambiguous ' + a[:70]
        c = c.replace(a, b)
    rep('OK={en:1,it:1,es:1}', 'OK={en:1,it:1,es:1,el:1}')
    rep('(en|it|es)', '(en|it|es|el)', cnt=0)
    rep('I={it:0,es:1}', 'I={it:0,es:1,el:2}')
    # Greek dates and patterns
    rep('function dt(s,l){', 'function dt(s,l){if(l==="el")return dtEl(s);')
    rep('function pre(s,l){', GREEK_JS + '\nfunction pre(s,l){')
    # use the Greek table for el
    rep('function one(s,l){var t=D[s];if(t)return t[I[l]];for(var i=0;i<P.length;i++){var m=s.match(P[i][0]);if(m){var r=P[i][1](m);if(r)return r[I[l]]}}',
        'function one(s,l){var t=D[s];if(t&&t[I[l]]!=null)return t[I[l]];if(l==="el"){for(var i=0;i<PE.length;i++){var m=s.match(PE[i][0]);if(m){var r=PE[i][1](m);if(r!=null)return r}}}else for(var i=0;i<P.length;i++){var m=s.match(P[i][0]);if(m){var r=P[i][1](m);if(r)return r[I[l]]}}')
    rep('return D[m[1]][I[l]]+s.slice(m[1].length)', 'var x=D[m[1]][I[l]];if(x==null)return null;return x+s.slice(m[1].length)')
    rep('return(l==="it"?"Mostra solo ":"Mostrar solo ")+a[I[l]]+", "+sm[2]',
        'return({it:"Mostra solo ",es:"Mostrar solo ",el:"Μόνο "}[l])+a[I[l]]+", "+sm[2]')
    # switcher
    rep('LBL={en:"Language",it:"Lingua",es:"Idioma"}', 'LBL={en:"Language",it:"Lingua",es:"Idioma",el:"Γλώσσα"}')
    rep('<button type="button" data-l="es" title="Español">ES</button>',
        '<button type="button" data-l="es" title="Español">ES</button><button type="button" data-l="el" title="Ελληνικά">EL</button>')
    rep("st.textContent='.tc-lp{", "st.textContent=\"" + FONT_MARK + "\"+'.tc-lp{")
    return c

def add_dict(dj, miss):
    D = json.loads(dj.replace('<\\/', '</'))
    for k, v in D.items():
        g = EL.get(k)
        if g is None:
            miss.add(k); g = k
        D[k] = [v[0], v[1], g]
    return json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

def run(path):
    s = open(path, encoding='utf8').read()
    s0 = s
    # FAQ answer: the app now speaks Greek too
    if FAQ_OLD in s:
        s = s.replace(FAQ_OLD, FAQ_NEW)
    miss = set()
    def fix(m):
        dj, core = m.group(1), m.group(2)
        D = json.loads(dj.replace('<\\/', '</'))
        if FAQ_NEW in s and FAQ_KEY not in D:
            D[FAQ_KEY] = FAQ_ITES[:]
        dj = json.dumps(D, ensure_ascii=False, separators=(',', ':'))
        return '<script id="tc-i18n">window.TCI18N_DICT=' + add_dict(dj, miss) + ';\n' + patch_core(core.replace('<\\/', '</')).replace('</', '<\\/') + '</script>'
    # extra dictionaries merged at runtime (World / landing listen-in strings): X={...};for(var k in X)if(!D[k])D[k]=X[k]
    def fixx(m):
        X = json.loads(m.group(2))
        for k, v in X.items():
            g = EL.get(k)
            if g is None: miss.add(k); g = k
            X[k] = [v[0], v[1], g]
        return m.group(1) + json.dumps(X, ensure_ascii=False) + m.group(3)
    s = re.sub(r'(var D=window\.TCI18N_DICT\|\|\{\},X=)(\{.*?\})(;for\(var k in X\))', fixx, s, flags=re.S)
    s, n = re.subn(r'<script id="tc-i18n">window\.TCI18N_DICT=(\{.*?\});\n(.*?)</script>', fix, s, flags=re.S)
    s = fix_restore(s)
    # Greek font faces, matched to this page's Google Fonts weights (replaces older versions)
    fc = FONT_MARK + font_css(s)
    s = re.sub(r'st\.textContent="(?:/\*tc-el-fonts\*/)?(?:@font-face\{[^}]*\})*"\+\'\.tc-lp\{', lambda m: 'st.textContent="' + fc + '"+\'.tc-lp{', s)
    # Settings language select
    s = s.replace('<option value="es">Español</option></select>', '<option value="es">Español</option><option value="el">Ελληνικά</option></select>')
    if s != s0:
        open(path, 'w', encoding='utf8').write(s)
    print(f'{path}: {n} i18n block(s), {len(miss)} strings without Greek' + (': ' + ' | '.join(sorted(miss))[:300] if miss else ''))

if __name__ == '__main__':
    for p in sys.argv[1:]:
        run(p)
