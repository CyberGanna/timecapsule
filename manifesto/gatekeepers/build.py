"""One-page PDF: From gatekeepers to the table (Karim's positioning text, public version).
Run: python3 build.py && node render.js   -> ../From-Gatekeepers-to-the-Table.pdf
Reuses manifesto/src (base.css, fonts, cut-out logo)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, '..', 'src')
sys.path.insert(0, SRC)
from cutout import cut
SVG = '<svg viewBox="0 -6 110 82" aria-hidden="true"><defs><clipPath id="ID"><circle cx="35" cy="35" r="30"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z"/></clipPath></defs><circle cx="35" cy="35" r="30" fill="#7C5CFF"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z" fill="#7C5CFF"/><circle cx="75" cy="35" r="30" fill="#17C3C8"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#17C3C8"/><g clip-path="url(#ID)"><circle cx="75" cy="35" r="30" fill="#3B2A9E"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#3B2A9E"/></g><g fill="#fff"><circle cx="36" cy="35" r="4.6"/><circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g></svg>'
SVG = cut(SVG, 'IDm').replace('ID', 'h0')
WT = '<span class="wt"><b>time</b><i>capsule</i></span>'
css = open(os.path.join(SRC, 'base.css')).read().replace('url(fonts/', 'url(../src/fonts/')
css += """
.page{padding:0}
.body{position:absolute;left:21mm;right:21mm;top:24.5mm;bottom:22mm;display:flex;flex-direction:column}
.head{top:12mm;left:21mm;right:21mm}.pagefoot{left:21mm;right:21mm;bottom:11mm}
h1{font-size:26px;margin-bottom:1.2mm}
.sub{font-family:'Sora',sans-serif;font-weight:300;font-size:13.5px;color:var(--muted);margin-bottom:4mm}
p{font-size:10.2pt;line-height:1.42;margin-bottom:2mm}
p.lead{font-size:11pt;line-height:1.4;margin-bottom:3mm}
h2{font-family:'Sora',sans-serif;font-weight:600;font-size:8.2pt;letter-spacing:.2em;text-transform:uppercase;color:var(--violet);margin:3.6mm 0 1.8mm}
.ages{display:grid;grid-template-columns:.92fr .92fr 1.45fr;gap:5mm}
.age{border-top:1px solid var(--line);padding-top:2.4mm}
.age .n{font-family:'Sora',sans-serif;font-size:8pt;font-weight:600;letter-spacing:.12em;color:var(--violet);margin-bottom:1mm}
.age h3{font-family:'Sora',sans-serif;font-weight:600;font-size:10pt;color:var(--navy);margin-bottom:1.4mm}
.age p{font-size:9.6pt;line-height:1.4;margin-bottom:1.4mm}
.items{display:grid;grid-template-columns:1fr 1fr;column-gap:7mm}
.line{margin:4.2mm 0 1.4mm;padding:1.6mm 0 1.6mm 5mm;border-left:3px solid;border-image:linear-gradient(var(--violet),var(--teal)) 1}
.line p{font-size:11.4pt;line-height:1.38;color:var(--navy);margin:0}
.it{position:relative;padding-left:6.5mm;font-size:9.8pt;line-height:1.38;margin-bottom:1.5mm}
.it::before{content:"";position:absolute;left:0;top:.4em;width:8px;height:8px;border-radius:50%;border:2px solid var(--teal);background:#fff}
.it b{font-family:'Sora',sans-serif;font-weight:600;font-size:9pt;color:var(--navy)}
.principle{margin-top:auto;flex:none;background:var(--navy);color:#fff;border-radius:3mm;padding:4mm 5.5mm 3.8mm}
.principle h2{color:var(--teal);margin:0 0 2.2mm}
.principle p{font-size:11.2pt;line-height:1.38;color:#fff;margin-bottom:1.6mm}
.principle p.s{font-size:9.5pt;color:#B9BCD6;margin:0}
"""
age = lambda n, h, ps: '<div class="age"><div class="n">%02d</div><h3>%s</h3>%s</div>' % (n, h, ''.join('<p>%s</p>' % p for p in ps))
it = lambda a, b: '<div class="it"><b>%s</b> %s</div>' % (a, b)
body = ''.join([
 '<h1>From gatekeepers <b>to the table</b></h1><div class="sub">A different way for ideas to earn trust.</div>',
 '<p class="lead">For most of history, ideas reached the public through gatekeepers. Then social media removed the gates. TimeCapsule proposes a third way: anyone can bring an idea, but ideas are tested through conversation, questioned by peers and preserved with the reasoning and disagreements that emerge.</p>',
 '<h2>The argument</h2>',
 '<div class="ages">', age(1, 'The age of gatekeepers', ['Universities, churches, publishers and the press traditionally decided which ideas reached society. This provided mechanisms for scrutiny, but also restricted participation. Over time, trust in these institutions has eroded as their limitations, biases and failures have become increasingly visible.']),
 age(2, 'The age of the feed', ['Social media gave everyone a voice, and that was an important step forward. But it replaced many traditional filters with an attention economy. Ideas spread according to their ability to attract attention, provoke reactions or confirm existing beliefs. Reach became disconnected from scrutiny.']),
 age(3, 'The table', ['TimeCapsule keeps the open door but brings scrutiny back, without restoring the gatekeepers. Anyone can introduce an idea. Nobody is appointed to decide in advance which ideas deserve a hearing. Instead, ideas enter small conversations where participants can question assumptions, challenge conclusions, contribute experience and offer different perspectives.',
   'What emerges is not a final verdict, but a record of the conversation: the ideas, the reasoning, the disagreements and the questions still unanswered. Each new conversation can build on it, challenge it or change it.']), '</div>',
 '<div class="line"><p>Institutions filtered who could speak. Social media stopped filtering anything. TimeCapsule filters nothing at the door and lets ideas earn their weight in conversation.</p></div>',
 '<h2>Why this is already reflected in the product</h2>',
 '<div class="items">', it('Small tables:', 'You cannot simply broadcast. You have to participate and respond.'),
 it('No feed, followers or public counts:', 'Attention and popularity are not the currency of the platform.'),
 it('TimeCoins and Trusted:', 'Reputation develops through actual interactions and relationships with people who have sat at the table.'),
 it('Preserved conversations:', 'Ideas and disagreements remain accessible, allowing future participants to revisit and challenge what was previously discussed.'), '</div>',
 '<h2>Ideas tested in conversation</h2>',
 '<p>A table of like-minded people can become an echo chamber. Ideas are only tested when different perspectives meet, so TimeCapsule is designed to bring them to the same table.</p>',
 '<div class="principle"><h2>The principle</h2><p>We are not building a platform that decides what is true. We are building a platform where ideas have to meet other people before they become part of a shared record.</p>'
 '<p class="s">TimeCapsule doesn\'t determine what people should think.<br>It creates the conditions for people to think together.</p></div>',
])
html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>From gatekeepers to the table · TimeCapsule</title><style>%s</style></head><body>'
        '<section class="page"><div class="head"><div class="logo">%s%s</div></div><div class="body">%s</div>'
        '<div class="pagefoot"><span>From gatekeepers to the table</span><span>TimeCapsule</span></div></section></body></html>') % (css, SVG, WT, body)
open(os.path.join(HERE, 'gatekeepers.html'), 'w').write(html)
print('ok')
