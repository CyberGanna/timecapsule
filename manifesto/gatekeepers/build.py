"""Two-page PDF (US Letter, portrait): From gatekeepers to the table (Gabriele's positioning text, public version).
Run: python3 build.py && node render.js   -> ../From-Gatekeepers-to-the-Table.pdf
Reuses manifesto/src (base.css, fonts, cut-out logo)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, '..', 'src')
sys.path.insert(0, SRC)
from cutout import cut
SVG = '<svg viewBox="0 -6 110 82" aria-hidden="true"><defs><clipPath id="ID"><circle cx="35" cy="35" r="30"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z"/></clipPath></defs><circle cx="35" cy="35" r="30" fill="#7C5CFF"/><path d="M13.8 56.2 L4 74 L29.8 64.5 Z" fill="#7C5CFF"/><circle cx="75" cy="35" r="30" fill="#17C3C8"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#17C3C8"/><g clip-path="url(#ID)"><circle cx="75" cy="35" r="30" fill="#3B2A9E"/><path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#3B2A9E"/></g><g fill="#fff"><circle cx="36" cy="35" r="4.6"/><circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g></svg>'
SVG = cut(SVG, 'IDm')
WT = '<span class="wt"><b>time</b><i>capsule</i></span>'
css = open(os.path.join(SRC, 'base.css')).read().replace('url(fonts/', 'url(../src/fonts/')
css += """
@page{size:letter;margin:0}
.page{width:8.5in;height:11in;padding:0}
.body{position:absolute;left:20mm;right:20mm;top:26mm;bottom:23mm;display:flex;flex-direction:column}
.head{top:13mm;left:20mm;right:20mm}.pagefoot{left:20mm;right:20mm;bottom:11.5mm}
h1{font-size:29px;margin-bottom:1.5mm}
.sub{font-family:'Sora',sans-serif;font-weight:300;font-size:16px;color:var(--muted);margin-bottom:4.5mm}
p{font-size:10.4pt;line-height:1.45;margin-bottom:2.2mm}
p.lead{font-size:11.6pt;line-height:1.44;margin-bottom:1mm}
h2{font-family:'Sora',sans-serif;font-weight:600;font-size:8.6pt;letter-spacing:.22em;text-transform:uppercase;color:var(--violet);margin:5.5mm 0 3mm}
h2:first-child{margin-top:0}
.age{display:grid;grid-template-columns:11mm 1fr;border-top:1px solid var(--line);padding-top:3mm;margin-bottom:1.4mm}
.age .n{font-family:'Sora',sans-serif;font-size:9pt;font-weight:600;letter-spacing:.12em;color:var(--violet);padding-top:.3em}
.age h3{font-family:'Sora',sans-serif;font-weight:600;font-size:11pt;color:var(--navy);margin-bottom:2mm}
.b1 p{font-size:10.2pt}.b1 p.lead{font-size:11.2pt}
.pair{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm}
.line{margin:0 0 1mm;padding:3mm 0 3mm 7mm;border-left:3px solid;border-image:linear-gradient(var(--violet),var(--teal)) 1}
.line p{font-size:14pt;line-height:1.4;color:var(--navy);margin:0}
.it{position:relative;padding-left:9mm;font-size:10.4pt;line-height:1.45;margin-bottom:2.4mm}
.it::before{content:"";position:absolute;left:0;top:.42em;width:10px;height:10px;border-radius:50%;border:2px solid var(--teal);background:#fff}
.it b{font-family:'Sora',sans-serif;font-weight:600;font-size:9.6pt;color:var(--navy)}
.principle{margin-top:auto;flex:none;background:var(--navy);color:#fff;border-radius:3mm;padding:6.5mm 7mm 6mm}
.b2 h2{margin-top:9mm}.b2 p,.b2 .it{font-size:11pt}.b2 .line p{font-size:15pt}.b2 h2:first-child{margin-top:0}.b2 .line{margin-bottom:2mm}
.principle h2{color:var(--teal);margin:0 0 3mm}
.principle p{font-size:12pt;line-height:1.4;color:#fff;margin-bottom:2.6mm}
.principle p.big{font-size:13.6pt;line-height:1.36;margin-bottom:3mm}
.principle p.s{font-size:10.2pt;color:#B9BCD6;margin:0}
"""
age = lambda n, h, ps: '<div class="age"><div class="n">%02d</div><div><h3>%s</h3>%s</div></div>' % (n, h, ''.join('<p>%s</p>' % p for p in ps))
it = lambda a, b: '<div class="it"><b>%s</b> %s</div>' % (a, b)
p1 = ''.join([
 '<h1>From gatekeepers <b>to the table</b></h1><div class="sub">A different way for ideas to earn trust.</div>',
 '<h2>The short version</h2>',
 '<p class="lead">For much of history, institutions controlled many of the channels through which ideas gained public recognition and legitimacy. Social media lowered the barriers to publishing, giving everyone a voice, but replaced traditional gatekeepers with algorithms and an economy driven by attention. TimeCapsule proposes a different approach: an open space where anyone can introduce an idea, but where ideas develop through conversation, questioning and disagreement. Rather than declaring what is true, it preserves the reasoning, perspectives and objections that allow ideas to be examined again.</p>',
 '<h2>The argument</h2>',
 '<div class="pair">', age(1, 'The age of gatekeepers', ['Universities, churches, publishers and the press traditionally controlled many of the major channels through which ideas gained public recognition and legitimacy. Ideas always circulated outside them too, through conversations, letters and communities, but rarely with the same reach. This provided mechanisms for scrutiny, but also restricted participation. Over time, trust in these institutions has eroded as their limitations, biases and failures have become increasingly visible.']),
 age(2, 'The age of the feed', ['Social media lowered the barriers to publishing and gave everyone a voice, and that was an important step forward. But it did not remove the gates. It replaced traditional gatekeepers with new ones: algorithms, platform owners and an attention economy. Ideas spread according to their ability to attract attention, provoke reactions or confirm existing beliefs. An idea can be open to everyone and still invisible to most. Reach became disconnected from scrutiny.']),
 '</div>',
 age(3, 'The table', ['TimeCapsule keeps the open door but brings scrutiny back, without restoring the gatekeepers. Anyone can introduce an idea. Nobody is appointed to decide in advance which ideas deserve a hearing. Instead, ideas enter small conversations where participants can question assumptions, challenge conclusions and offer different perspectives. Not everyone has equal expertise, and the table does not pretend otherwise: professional expertise, personal experience, research and critical reasoning are different forms of knowledge, and each can be brought to it.',
   'Conversation does not guarantee truth. A group can reinforce the same misconception. Its value is that it makes the reasoning, the disagreements and the competing perspectives visible.',
   'What emerges is not a final verdict, but a record of the conversation: the ideas, the reasoning, the objections, the questions still unanswered and the challenges that come later. Preservation is not certification. Each new conversation can build on it, challenge it or change it.']),
])
p2 = ''.join([
 '<h2>The central line</h2>',
 '<div class="line"><p>Institutions filtered who could be heard. Social media let algorithms and attention decide. TimeCapsule filters nothing at the door and lets ideas earn their weight in conversation.</p></div>',
 '<h2>Why this is already reflected in the product</h2>',
 it('Small tables:', 'You cannot simply broadcast. You have to participate and respond.'),
 it('No feed, followers or public counts:', 'Attention and popularity are not the currency of the platform.'),
 it('TimeCoins and Trusted:', 'Reputation develops through actual interactions and relationships with people who have sat at the table.'),
 it('Preserved conversations:', 'Ideas and disagreements remain accessible, allowing future participants to revisit and challenge what was previously discussed.'),
 '<h2>Ideas tested in conversation</h2>',
 '<p>A table of like-minded people can become an echo chamber. Ideas are only tested when different perspectives meet, so TimeCapsule is designed to bring them to the same table.</p>',
 '<h2>What makes TimeCapsule different</h2>',
 '<p>It isn\'t simply that people talk. It is that conversations become part of a continuing, revisitable record of how ideas are questioned, developed and understood.</p>',
 '<div class="principle"><h2>The principle</h2><p class="big">An idea doesn\'t become valuable because people agree with it. It becomes more valuable when people have had the opportunity to examine it.</p><p>We are not building a platform that decides what is true. We are building a platform where ideas have to meet other people before they become part of a shared record.</p>'
 '<p class="s">TimeCapsule doesn\'t determine what people should think.<br>It creates the conditions for people to think together.</p></div>',
])
def page(n, b):
    return ('<section class="page"><div class="head"><div class="logo">%s%s</div><div class="num">%d / 2</div></div><div class="body b%d">%s</div>'
            '<div class="pagefoot"><span>From gatekeepers to the table</span><span>TimeCapsule</span></div></section>') % (SVG.replace('ID', 'h%d' % n), WT, n, n, b)
html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>From gatekeepers to the table · TimeCapsule</title><style>%s</style></head><body>'
        '%s%s</body></html>') % (css, page(1, p1), page(2, p2))
open(os.path.join(HERE, 'gatekeepers.html'), 'w').write(html)
print('ok')
