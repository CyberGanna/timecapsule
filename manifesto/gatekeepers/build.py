"""Internal text: TimeCapsule: From Gatekeepers to the Table (US Letter, portrait, flows over as many pages as needed).
Run: python3 build.py && node render.js   -> ../From-Gatekeepers-to-the-Table.pdf
Also builds the public one-pager (public.html -> ../TimeCapsule-Think-Together.pdf).
Reuses manifesto/src (base.css, fonts, cut-out logo)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, '..', 'src')
sys.path.insert(0, SRC)
from cutout import cut
SVG = '<svg viewBox="0 -6 110 82" aria-hidden="true"><defs><clipPath id="ID"><circle cx="35" cy="35" r="30"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z"/></clipPath></defs><circle cx="35" cy="35" r="30" fill="#7C5CFF"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z" fill="#7C5CFF"/><circle cx="75" cy="35" r="30" fill="#17C3C8"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#17C3C8"/><g clip-path="url(#ID)"><circle cx="75" cy="35" r="30" fill="#3B2A9E"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#3B2A9E"/></g><g fill="#fff"><circle cx="36" cy="35" r="4.6"/><circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g></svg>'
SVG = cut(SVG, 'IDm')
WT = '<span class="wt"><b>time</b><i>capsule</i></span>'
css = open(os.path.join(SRC, 'base.css')).read().replace('url(fonts/', 'url(../src/fonts/')
css += """
@page{size:letter;margin:0}
:root{--bg:#1B2144;--surface:#20264A;--raise:#252B52;--fg:#EEF1FF;--soft:#C9CFF0;--mute:#A9B0D6;--ln:#3A4175;--gold:#F2C14E}
html,body{background:var(--bg)}
body{font-family:'Sora',sans-serif;color:var(--fg)}
.page{width:8.5in;height:11in;padding:0;background:var(--bg)}
.body{position:absolute;left:21mm;right:21mm;top:24.5mm;bottom:21.5mm;overflow:hidden}
.head{top:12.5mm;left:21mm;right:21mm}.pagefoot{left:21mm;right:21mm;bottom:11.5mm;border-top-color:var(--ln);color:var(--mute)}
.head .wt{color:var(--fg)}.head .num{color:var(--mute)}
.tag{display:inline-block;font-size:8pt;font-weight:400;color:var(--soft);border:1px solid var(--ln);border-radius:99px;padding:1.2mm 3.4mm;margin-bottom:4mm}
h1{font-family:'Sora',sans-serif;font-weight:400;font-size:32px;letter-spacing:-.02em;color:var(--fg);line-height:1.15;margin-bottom:7mm}
h1 b{font-weight:400}
p{font-family:'Sora',sans-serif;font-weight:300;font-size:9.5pt;line-height:1.58;color:var(--soft);margin-bottom:2.4mm}
p.lead{font-weight:400;font-size:10.8pt;line-height:1.55;color:var(--fg)}
p b{font-weight:600;color:var(--fg)}
h2{font-family:'Sora',sans-serif;font-weight:400;font-size:9.4pt;color:var(--fg);margin:6mm 0 2.8mm;display:flex;align-items:center;gap:2.4mm}
h2::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--violet)}
h3{font-family:'Sora',sans-serif;font-weight:600;font-size:12.5pt;color:var(--fg);margin:4.4mm 0 2.2mm;padding-top:3mm;border-top:1px solid var(--ln)}
h3 span{color:var(--teal);font-weight:400;font-size:9pt;margin-right:3mm}
.body>:first-child{margin-top:0}
.it{position:relative;padding-left:6mm;font-weight:300;font-size:9.4pt;line-height:1.52;color:var(--soft);margin-bottom:1.6mm}
.it::before{content:"";position:absolute;left:.5mm;top:.62em;width:5px;height:5px;border-radius:50%;background:var(--teal)}
.it b{font-weight:600;color:var(--fg)}
.it.last{margin-bottom:3.4mm}
.line{margin:1mm 0 2mm;background:var(--surface);border:1px solid var(--ln);border-radius:4mm;padding:5.5mm 6.5mm}
.line p{font-family:'Newsreader',Georgia,serif;font-style:italic;font-weight:400;font-size:15pt;line-height:1.42;color:var(--fg);margin:0}
"""

def P(t): return '<p>%s</p>' % t
def H2(t): return '<h2 data-keep="1">%s</h2>' % t
def H3(n, t): return '<h3 data-keep="1"><span>%02d</span>%s</h3>' % (n, t)
def UL(items):
    out = []
    for i, x in enumerate(items):
        cls = 'it last' if i == len(items) - 1 else 'it'
        if isinstance(x, tuple): x = '<b>%s</b> %s' % x
        out.append('<div class="%s">%s</div>' % (cls, x))
    return out

B = [
 '<div class="tag" data-keep="1">Internal</div>',
 '<h1 data-keep="1">From gatekeepers <b>to the table</b></h1>',
 H2('The short version'),
 '<p class="lead">Institutions once controlled who could be heard, and above all what words like &ldquo;knowledge,&rdquo; &ldquo;reason&rdquo; and &ldquo;serious&rdquo; were allowed to mean. Social media opened the door but replaced them with algorithms and attention. TimeCapsule starts from a different premise: every space for ideas has gates, so the question is whether they are hidden or visible. It is an open space where anyone can introduce an idea, and where the idea develops through conversation, questioning and disagreement. Nobody rules on what is true, but the rules of the conversation are public. What is preserved is the reasoning, the objections and the open questions, so they can be examined again.</p>',
 H2('The argument'),
 H3(1, 'The age of gatekeepers'),
 P('Universities, churches, publishers and the press controlled many of the channels through which ideas gained recognition. But their deeper power was over language. They defined what counted as knowledge, evidence and a serious argument, and whoever did not speak that language was heard as noise. This provided scrutiny, but also restricted participation, and trust in these institutions has eroded as their biases and failures have become visible.'),
 H3(2, 'The age of the feed'),
 P('Social media lowered the barriers to publishing, and that was a real step forward. But it replaced the old gatekeepers with new ones: algorithms, platform owners and an attention economy. Ideas spread by their power to provoke, not by how well they hold up. Reach became disconnected from scrutiny. Anyone could speak, but only inside moderation systems and a vocabulary that someone else had set.'),
 P('TimeCapsule has no feed, so it does not have this problem. It has the problem the feed was hiding: how people find each other and who gets seated at which table. That is a gate too, and it is designed openly. Tables form through invitation and shared questions, never through ranking by popularity.'),
 H3(3, 'The table'),
 P('Anyone can introduce an idea. Nobody is appointed to decide in advance which ideas deserve a hearing. Ideas enter small conversations where participants question assumptions, challenge conclusions and offer different perspectives. Professional expertise, lived experience, research and critical reasoning are different kinds of knowledge, and each can be brought to the table.'),
 P('<b>Language belongs to the table.</b> No one has to speak in an academic register to be heard. A story, an example and a simple question all count as contributions. Tables run in the participants&rsquo; own language, with translation available. When a disagreement is really about what a word means, the table marks it as a dispute over meaning, not over facts. The platform&rsquo;s own terms are open to challenge in the same way.'),
 P('<b>No verdict on truth, but a discipline of reasoning.</b> Conversation does not guarantee truth, and a group can reinforce the same mistake. So TimeCapsule separates verdicts from procedure. It never declares a claim true or false. It keeps the rules of criticism visible:'),
] + UL([
 'Claims are marked by kind (factual, interpretive, value-based), because each needs a different kind of support.',
 'Sources are disclosed, and a claim with none is marked as unsupported.',
 'A fallacy can be named openly by any participant, and the name stays attached to the argument.',
 'An unanswered objection stays attached to the claim it challenges.',
 'The record shows the status of a claim (&ldquo;contested,&rdquo; &ldquo;unanswered&rdquo;), not a ruling.',
]) + [
 P('Rules need enforcement, and enforcement is a form of gatekeeping. We do not hide that. Moderation applies to the conduct and the rules of the conversation, never to opinions. It is public, it states its reasons, and it can be appealed.'),
 P('<b>Guarding against indoctrination.</b> Indoctrination works through repetition, closed groups and imbalance. So a table of like-minded people is not enough. Tables are built to include different perspectives, a place for dissent is built into every table, and how a table was assembled is visible to everyone. Ideas are only truly tested when different perspectives meet.'),
 H3(4, 'Private first, public by choice'),
 P('A permanent record is valuable, but a record alone makes thinking difficult. Ideas need a space where people can be tentative, be wrong and change their minds unobserved. So TimeCapsule has two spaces:'),
] + UL([
 'Direct, private conversation is never recorded unless every participant agrees.',
 'The record holds only what participants have chosen to place there.',
 'Participants can annotate or retract a position and mark that they have changed their mind. Revising is treated as honesty, not as defeat.',
]) + [
 P('A capsule is sealed first and opened later. The record works the same way.'),
 H3(5, 'Weight without a scoreboard'),
 P('Conversation does not mean counting agreement. An idea&rsquo;s weight comes from how well it stands up: which objections it has answered, and which remain open. Agreement can be manufactured and is no proof of truth. Reputation can be gamed too, and no system can prevent that completely. TimeCapsule makes it costly and visible:'),
] + UL([
 'Agreement and trust from people who disagree with you count more than from allies.',
 'Reputation is tied to a domain and fades over time.',
 'There is no single public score, and trust cannot be transferred or traded.',
 'Anyone can reply to and appeal against damage to their reputation, and the reply is kept beside the claim.',
 'Patterns such as mutual vouching, coordinated groups and duplicate accounts are detected and shown openly.',
]) + [
 H2('The central line'),
 '<div class="line"><p>Institutions controlled who could be heard and what words meant. Social media handed visibility to algorithms and attention. TimeCapsule opens the door to everyone, keeps its own gates visible and open to challenge, and lets ideas earn their weight through conversation.</p></div>',
 H2('Why this is already reflected in the product'),
] + UL([
 ('Small tables:', 'You cannot simply broadcast. You have to participate and respond.'),
 ('No feed, followers or public counts:', 'Attention and popularity are not the currency of the platform.'),
 ('Private space and the chosen record:', 'What is said in private stays private. Only what participants choose enters the record.'),
 ('TimeCoins and Trusted:', 'Reputation develops through real interactions with people who have sat at the table, and is tied to a domain and fades over time.'),
 ('Preserved conversations:', 'Ideas, objections and open questions remain accessible, so future participants can revisit and challenge them.'),
]) + [
 H2('What makes TimeCapsule different'),
 P('It isn&rsquo;t simply that people talk. It is the combination of three things:'),
] + UL([
 ('Conversation with a procedure.', 'Open participation, with public rules of criticism instead of a ruling on truth.'),
 ('A record that people control.', 'Private by default, public by consent, and revisable.'),
 ('Trust spread across many people.', 'Weight that comes from answered objections and varied relationships, never from a ranking.'),
])

def doc(css_extra, blocks, foot, title, js=True):
    head = '<div class="head"><div class="logo">%s%s</div><div class="num"></div></div>' % (SVG, WT)
    script = """
const DATA=%s, HEAD=%s, FOOT=%s;
window.paginate=function(){
let cid=0;
function newPage(){const s=document.createElement('section');s.className='page';
 s.innerHTML=HEAD.replace(/ID/g,'h'+(cid++))+'<div class="body"></div><div class="pagefoot"><span>'+FOOT+'</span><span>TimeCapsule</span></div>';
 document.body.appendChild(s);return s.querySelector('.body');}
const over=b=>b.scrollHeight>b.clientHeight+1;
let body=newPage();
for(const h of DATA){const t=document.createElement('div');t.innerHTML=h;const el=t.firstChild;body.appendChild(el);
 if(over(body)){body.removeChild(el);const moved=[];
  while(body.lastElementChild&&body.lastElementChild.dataset.keep){moved.unshift(body.lastElementChild);body.removeChild(body.lastElementChild);}
  body=newPage();moved.forEach(m=>body.appendChild(m));body.appendChild(el);if(over(body))console.log('OVERFLOW');}}
const ps=document.querySelectorAll('.page');if(ps.length>1)ps.forEach((p,i)=>p.querySelector('.num').textContent=(i+1)+' / '+ps.length);
window.PAGES=ps.length;};
""" % (json.dumps(blocks), json.dumps(head), json.dumps(foot))
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body><script>%s</script></body></html>') % (title, css + css_extra, script)

open(os.path.join(HERE, 'gatekeepers.html'), 'w').write(doc('', B, 'From gatekeepers to the table · Internal', 'From gatekeepers to the table · TimeCapsule'))

# ---------- Public one-pager (the four elements, from Gabriele's draft opening) ----------
PUB_CSS = """
.pub h1{font-size:34px;line-height:1.2;margin-bottom:8mm}
.pub h1 b{color:var(--mute)}
.pub p.lead{font-size:12.4pt;line-height:1.6;margin-bottom:4mm}
.pub p{font-size:10.6pt;line-height:1.65;margin-bottom:3.4mm}
.four{display:grid;grid-template-columns:1fr 1fr;gap:4.5mm;margin:5mm 0 5mm}
.four>div{background:var(--surface);border:1px solid var(--ln);border-radius:4mm;padding:4.6mm 5mm}
.four .k{font-size:8.6pt;color:var(--fg);margin-bottom:2.4mm;display:flex;align-items:center;gap:2.2mm}
.four .k::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--c,var(--violet))}
.four>div:nth-child(2){--c:var(--teal)}.four>div:nth-child(3){--c:var(--gold)}.four>div:nth-child(4){--c:#FF8FB1}
.four p{font-size:10.2pt;line-height:1.55;margin:0}
.close{background:var(--surface);border:1px solid var(--ln);border-radius:4mm;padding:7mm 8mm;margin-top:6mm}
.close p{font-family:'Newsreader',Georgia,serif;font-style:italic;font-weight:400;color:var(--fg);font-size:17pt;line-height:1.4;margin:0}
"""
PUB = [
 '<div class="pub">'
 '<h1>We have more ways to communicate than ever, <b>but fewer opportunities to really think together.</b></h1>'
 '<p class="lead">Most online spaces are built around sharing, reacting and attracting attention. But some conversations deserve more time. They deserve different perspectives, thoughtful questions and the freedom to explore an idea without having to reduce it to a post or a quick reaction.</p>'
 '<p>We are creating a place where people can come together around subjects they care about, exchange ideas and learn from different perspectives.</p>'
 '<div class="four">'
 '<div><div class="k">The problem</div><p>Online communication is abundant, but meaningful conversation is harder to find.</p></div>'
 '<div><div class="k">The experience</div><p>People meet around subjects, exchange ideas and explore different perspectives.</p></div>'
 '<div><div class="k">The difference</div><p>Conversations have room to develop, rather than being lost in an endless feed.</p></div>'
 '<div><div class="k">The value</div><p>What emerges from a conversation can be preserved and revisited.</p></div>'
 '</div>'
 '<p>Conversations don&rsquo;t simply disappear. They can become something people return to, explore further and build upon.</p>'
 '<div class="close"><p>Not just another place to share what you think. A place to discover what we can think together.</p></div>'
 '</div>'
]
open(os.path.join(HERE, 'public.html'), 'w').write(doc(PUB_CSS, PUB, 'Think together', 'TimeCapsule · Think together'))
print('ok')
