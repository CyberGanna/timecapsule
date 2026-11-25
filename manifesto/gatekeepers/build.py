"""Two-page PDF (US Letter, portrait): From gatekeepers to the table (Karim's positioning text, public version).
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
.body{position:absolute;left:24mm;right:24mm;top:28mm;bottom:24mm;display:flex;flex-direction:column}
.head{top:14mm;left:24mm;right:24mm}.pagefoot{left:24mm;right:24mm;bottom:12mm}
h1{font-size:32px;margin-bottom:2mm}
.sub{font-family:'Sora',sans-serif;font-weight:300;font-size:16px;color:var(--muted);margin-bottom:7mm}
p{font-size:11.2pt;line-height:1.48;margin-bottom:2.6mm}
p.lead{font-size:12.8pt;line-height:1.46;margin-bottom:2mm}
h2{font-family:'Sora',sans-serif;font-weight:600;font-size:8.6pt;letter-spacing:.22em;text-transform:uppercase;color:var(--violet);margin:6.5mm 0 3.5mm}
h2:first-child{margin-top:0}
.age{display:grid;grid-template-columns:11mm 1fr;border-top:1px solid var(--line);padding-top:3.6mm;margin-bottom:2mm}
.age .n{font-family:'Sora',sans-serif;font-size:9pt;font-weight:600;letter-spacing:.12em;color:var(--violet);padding-top:.3em}
.age h3{font-family:'Sora',sans-serif;font-weight:600;font-size:12pt;color:var(--navy);margin-bottom:2mm}
.line{margin:0 0 1mm;padding:3mm 0 3mm 7mm;border-left:3px solid;border-image:linear-gradient(var(--violet),var(--teal)) 1}
.line p{font-size:16pt;line-height:1.4;color:var(--navy);margin:0}
.it{position:relative;padding-left:9mm;font-size:11.4pt;line-height:1.5;margin-bottom:3.2mm}
.it::before{content:"";position:absolute;left:0;top:.42em;width:10px;height:10px;border-radius:50%;border:2px solid var(--teal);background:#fff}
.it b{font-family:'Sora',sans-serif;font-weight:600;font-size:10.4pt;color:var(--navy)}
.principle{margin-top:auto;flex:none;background:var(--navy);color:#fff;border-radius:3mm;padding:8mm 8mm 7.5mm}
.b2 h2{margin-top:11mm}.b2 h2:first-child{margin-top:0}.b2 .line{margin-bottom:2mm}
.principle h2{color:var(--teal);margin:0 0 4mm}
.principle p{font-size:14pt;line-height:1.42;color:#fff;margin-bottom:3.5mm}
.principle p.s{font-size:11.2pt;color:#B9BCD6;margin:0}
"""
age = lambda n, h, ps: '<div class="age"><div class="n">%02d</div><div><h3>%s</h3>%s</div></div>' % (n, h, ''.join('<p>%s</p>' % p for p in ps))
it = lambda a, b: '<div class="it"><b>%s</b> %s</div>' % (a, b)
p1 = ''.join([
 '<h1>From gatekeepers <b>to the table</b></h1><div class="sub">A different way for ideas to earn trust.</div>',
 '<h2>The short version</h2>',
 '<p class="lead">For most of history, ideas reached the public through gatekeepers. Then social media removed the gates. TimeCapsule proposes a third way: anyone can bring an idea, but ideas are tested through conversation, questioned by peers and preserved with the reasoning and disagreements that emerge.</p>',
 '<h2>The argument</h2>',
 age(1, 'The age of gatekeepers', ['Universities, churches, publishers and the press traditionally decided which ideas reached society. This provided mechanisms for scrutiny, but also restricted participation. Over time, trust in these institutions has eroded as their limitations, biases and failures have become increasingly visible.']),
 age(2, 'The age of the feed', ['Social media gave everyone a voice, and that was an important step forward. But it replaced many traditional filters with an attention economy. Ideas spread according to their ability to attract attention, provoke reactions or confirm existing beliefs. Reach became disconnected from scrutiny.']),
 age(3, 'The table', ['TimeCapsule keeps the open door but brings scrutiny back, without restoring the gatekeepers.',
   'Anyone can introduce an idea. Nobody is appointed to decide in advance which ideas deserve a hearing. Instead, ideas enter small conversations where participants can question assumptions, challenge conclusions, contribute experience and offer different perspectives.',
   'What emerges is not a final verdict, but a record of the conversation: the ideas, the reasoning, the disagreements and the questions still unanswered.',
   'Each new conversation can build on it, challenge it or change it.']),
])
p2 = ''.join([
 '<h2>The central line</h2>',
 '<div class="line"><p>Institutions filtered who could speak. Social media stopped filtering anything. TimeCapsule filters nothing at the door and lets ideas earn their weight in conversation.</p></div>',
 '<h2>Why this is already reflected in the product</h2>',
 it('Small tables:', 'You cannot simply broadcast. You have to participate and respond.'),
 it('No feed, followers or public counts:', 'Attention and popularity are not the currency of the platform.'),
 it('TimeCoins and Trusted:', 'Reputation develops through actual interactions and relationships with people who have sat at the table.'),
 it('Preserved conversations:', 'Ideas and disagreements remain accessible, allowing future participants to revisit and challenge what was previously discussed.'),
 '<h2>Ideas tested in conversation</h2>',
 '<p>A table of like-minded people can become an echo chamber. Ideas are only tested when different perspectives meet, so TimeCapsule is designed to bring them to the same table.</p>',
 '<div class="principle"><h2>The principle</h2><p>We are not building a platform that decides what is true. We are building a platform where ideas have to meet other people before they become part of a shared record.</p>'
 '<p class="s">TimeCapsule doesn\'t determine what people should think.<br>It creates the conditions for people to think together.</p></div>',
])
def page(n, b):
    return ('<section class="page"><div class="head"><div class="logo">%s%s</div><div class="num">%d / 2</div></div><div class="body b%d">%s</div>'
            '<div class="pagefoot"><span>From gatekeepers to the table</span><span>TimeCapsule</span></div></section>') % (SVG.replace('ID', 'h%d' % n), WT, n, n, b)
html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>From gatekeepers to the table · TimeCapsule</title><style>%s</style></head><body>'
        '%s%s</body></html>') % (css, page(1, p1), page(2, p2))
open(os.path.join(HERE, 'gatekeepers.html'), 'w').write(html)
print('ok')
