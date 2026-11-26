"""Slides: Keeping the record (does saving conversations help or hurt TimeCapsule?).
Run from this folder: python3 build.py && node render.js  ->  TimeCapsule-Keeping-the-Record.pdf
Fonts come from ../../build-plan/fonts.css (static woff, copyable text). Logo is the cut-out version (Gabriele's rule for PDFs and presentations).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cutout import cut

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(HERE, '..', '..', 'build-plan', 'fonts.css')).read()

SVG = ('<svg viewBox="0 -6 110 82" aria-hidden="true"><defs><clipPath id="ID"><circle cx="35" cy="35" r="30"/>'
       '<path d="M13.8 56.2 L4 74 L29.8 64.5 Z"/></clipPath></defs><circle cx="35" cy="35" r="30" fill="#7C5CFF"/>'
       '<path d="M13.8 56.2 L4 74 L29.8 64.5 Z" fill="#7C5CFF"/><circle cx="75" cy="35" r="30" fill="#17C3C8"/>'
       '<path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#17C3C8"/><g clip-path="url(#ID)"><circle cx="75" cy="35" r="30" fill="#3B2A9E"/>'
       '<path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#3B2A9E"/></g><g fill="#fff"><circle cx="36" cy="35" r="4.6"/>'
       '<circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g></svg>')
WT = '<span class="wt"><b>time</b><i>capsule</i></span>'
_n = [0]


def logo():
    _n[0] += 1
    return '<div class="logo">%s%s</div>' % (cut(SVG.replace('ID', 'c%d' % _n[0]), 'm%d' % _n[0]), WT)


CSS = FONTS + """
:root{--navy:#0E1230;--ink:#1C1F33;--muted:#6B6F86;--violet:#7C5CFF;--teal:#17C3C8;--deep:#3B2A9E;--gold:#E3B34A;--paper:#FBFAF7;--line:#E6E3DC}
@page{size:1280px 720px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#fff}
body{font-family:'Sora',sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.s{width:1280px;height:720px;position:relative;overflow:hidden;background:var(--paper);padding:84px 104px 0;break-after:page;page-break-after:always}
.s:last-child{break-after:auto;page-break-after:auto}
.s.dark{background:var(--navy);color:#fff}
.logo{display:flex;align-items:center;gap:10px}
.logo svg{width:30px;height:22px}
.wt{font-size:15px;letter-spacing:-.01em;color:var(--navy)}.wt b{font-weight:600}.wt i{font-style:normal;font-weight:300}
.dark .wt{color:#fff}
.foot{position:absolute;left:104px;right:104px;bottom:40px;display:flex;justify-content:space-between;align-items:center;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
.dark .foot{color:#8C90AE}
.foot .wt{text-transform:none;letter-spacing:-.01em;font-size:14px}
.kick{font-size:13px;font-weight:600;letter-spacing:.24em;text-transform:uppercase;color:var(--violet);margin-bottom:22px;padding-top:16px;background:linear-gradient(90deg,var(--violet),var(--teal)) no-repeat 0 0/28px 3px}
.dark .kick{color:var(--teal)}
h1{font-weight:300;font-size:50px;line-height:1.14;letter-spacing:-.02em;color:var(--navy);max-width:960px}
h1 b{font-weight:600}
.dark h1{color:#fff}
.lead{font-family:'Newsreader',Georgia,serif;font-size:24px;line-height:1.45;color:#3A3D55;max-width:880px;margin-top:22px}
.dark .lead{color:#C9CCE4}
/* cover */
.cover{padding:84px 104px}
.cover .logo svg{width:84px;height:62px}.cover .logo .wt{font-size:38px}
.cover .big{position:absolute;left:104px;right:104px;bottom:96px}
.cover h1{font-size:64px;margin:0 0 18px}
.cover .lead{margin-top:0;max-width:820px}
.cover .ed{font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--teal);margin-top:34px}
.rule{width:64px;height:3px;border-radius:2px;background:linear-gradient(90deg,var(--violet),var(--teal));margin-bottom:30px}
/* two columns */
.two{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:44px}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:30px 34px}
.card h3{font-size:14px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;margin-bottom:16px}
.card.v h3{color:var(--violet)}.card.t h3{color:#0E9BA0}
.card p{font-family:'Newsreader',Georgia,serif;font-size:21px;line-height:1.45;color:var(--ink);margin-bottom:8px}
/* three */
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:46px}
.three .card{padding:30px 30px 32px}
.three em{display:block;font-style:normal;font-size:13px;font-weight:600;letter-spacing:.2em;color:var(--violet);margin-bottom:12px}
.three b{display:block;font-size:26px;font-weight:600;color:var(--navy);margin-bottom:12px}
.three p{font-family:'Newsreader',Georgia,serif;font-size:20px;line-height:1.42;color:#3A3D55}
/* list */
.list{list-style:none;margin-top:40px;max-width:1000px}
.list li{position:relative;padding:0 0 0 40px;margin-bottom:22px;font-family:'Newsreader',Georgia,serif;font-size:23px;line-height:1.4;color:var(--ink)}
.list li b{font-family:'Sora',sans-serif;font-weight:600;font-size:20px;color:var(--navy);margin-right:6px}
.list li::before{content:"";position:absolute;left:0;top:.42em;width:12px;height:12px;border-radius:50%;border:3px solid var(--teal);background:#fff}
.dark .list li{color:#E4E6F4}.dark .list li b{color:#fff}.dark .list li::before{background:var(--navy)}
.quote{position:absolute;left:104px;right:104px;bottom:96px;font-family:'Newsreader',Georgia,serif;font-style:italic;font-size:26px;color:var(--deep)}
/* rules table */
table{width:100%;border-collapse:collapse;margin-top:28px}
.wide h1{max-width:none}
th{font-size:12px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;text-align:left;color:var(--muted);padding:0 18px 12px 0;border-bottom:2px solid var(--navy)}
td{padding:12px 18px 12px 0;border-bottom:1px solid var(--line);vertical-align:top;font-family:'Newsreader',Georgia,serif;font-size:19px;line-height:1.36;color:var(--ink)}
td:first-child{font-family:'Sora',sans-serif;font-size:18px;font-weight:600;color:var(--navy);width:170px}
td:last-child{width:150px;padding-right:0}
.tag{display:inline-block;font-family:'Sora',sans-serif;font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:6px 11px;border-radius:999px;white-space:nowrap}
.tag.on{background:rgba(23,195,200,.16);color:#0B7F83}
.tag.prop{background:rgba(124,92,255,.10);color:var(--violet)}
.tag.open{background:rgba(227,179,74,.18);color:#94690F}
/* question */
.q{display:flex;flex-direction:column;justify-content:center;padding-top:0}
.q h1{font-size:56px;line-height:1.18;max-width:1040px}
.q h1 b{color:var(--teal);font-weight:400}
.q .lead{margin-top:34px}
/* pilot */
.grid2{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;margin-top:40px}
.grid2 .list{margin-top:0}
.ask{background:var(--navy);color:#fff;border-radius:16px;padding:34px 36px}
.ask h3{font-size:13px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);margin-bottom:16px}
.ask p{font-family:'Newsreader',Georgia,serif;font-size:24px;line-height:1.4;font-style:italic}
.ask small{display:block;margin-top:20px;font-family:'Sora',sans-serif;font-size:14px;line-height:1.5;color:#B9BCD6;font-style:normal}
.note{position:absolute;left:104px;bottom:84px;font-size:14px;color:var(--muted)}
"""

TOTAL = 11


def slide(n, body, dark=False, cls=''):
    foot = '<div class="foot">%s<span>Keeping the record &nbsp;·&nbsp; %d / %d</span></div>' % (logo(), n, TOTAL)
    return '<section class="s%s%s">%s%s</section>' % (' dark' if dark else '', ' ' + cls if cls else '', body, foot)


S = []

# 1 cover
S.append('<section class="s dark cover">%s<div class="big"><div class="rule"></div>'
         '<h1><b>Keeping the record</b></h1>'
         '<div class="lead">Does saving conversations help TimeCapsule, or does it stop people opening up and signing up?</div>'
         '<div class="ed">20 November 2026 &nbsp;·&nbsp; for discussion</div></div></section>' % logo().replace('<div class="logo">', '<div class="logo">', 1))

# 2 tension
S.append(slide(2, '<div class="kick">The tension</div>'
               '<h1>The record is our <b>greatest value</b>, and our <b>greatest obstacle</b>.</h1>'
               '<div class="two">'
               '<div class="card v"><h3>Why we keep it</h3><p>Knowledge that outlives the call.</p><p>Authorship: your words, with your name.</p><p>Something future generations can build on.</p></div>'
               '<div class="card t"><h3>Why it can hold people back</h3><p>People speak less freely when they know it is kept.</p><p>Some will not sign up if saving audio and transcripts feels permanent and public.</p></div>'
               '</div>'))

# 3 two problems, three questions
S.append(slide(3, '<div class="kick">Reframing</div>'
               '<h1>Preserving a conversation and feeling safe in it are <b>two different design problems</b>.</h1>'
               '<div class="three">'
               '<div class="card"><em>01</em><b>Philosophy</b><p>Why should a conversation be preserved at all?</p></div>'
               '<div class="card"><em>02</em><b>Experience</b><p>How can people feel safe speaking freely?</p></div>'
               '<div class="card"><em>03</em><b>Rules</b><p>Who controls what is recorded, kept and shared?</p></div>'
               '</div>'))

# 4 philosophy
S.append(slide(4, '<div class="kick">01 &nbsp;Philosophy</div>'
               '<h1>Why preserve a conversation?</h1>'
               '<ul class="list">'
               '<li><b>Knowledge.</b> It grows out of experience and dialogue, not only out of information.</li>'
               '<li><b>Authorship.</b> What you said stays yours, with your name on it.</li>'
               '<li><b>Inheritance.</b> A lasting human record that others can question and build on.</li>'
               '<li><b>Better talk.</b> People think before they speak, and tables become worth keeping.</li>'
               '</ul>'
               '<div class="quote">A conversation can become an enduring contribution: something to revisit, build on and pass forward.</div>'))

# 5 continuity
S.append(slide(5, '<div class="kick">01 &nbsp;Philosophy</div>'
               '<h1>Understanding develops <b>between people</b> and <b>across generations</b>.</h1>'
               '<div class="three">'
               '<div class="card"><b>An archive</b><p>keeps what happened.</p></div>'
               '<div class="card"><b>A knowledge base</b><p>keeps what was learned.</p></div>'
               '<div class="card"><b>TimeCapsule</b><p>keeps how understanding grew: the questions, the disagreements and the experiences behind it.</p></div>'
               '</div>'
               '<div class="quote">Never frozen. What one conversation leaves open can start the next.</div>'))

# 5 the risk
S.append(slide(6, '<div class="kick">The risk, honestly</div>'
               '<h1>Where saving can scare people away</h1>'
               '<ul class="list">'
               '<li><b>Self-censorship.</b> Work, family, health, or an opinion you might regret later.</li>'
               '<li><b>Sign-up doubt.</b> &ldquo;Everything is saved forever&rdquo; is the wrong first impression.</li>'
               '<li><b>A cultural shift.</b> Live audio apps built trust on talk that disappears. Keeping it asks for a new kind of trust.</li>'
               '<li><b>Feeling watched.</b> It comes from not knowing who holds the record, and who will see it.</li>'
               '</ul>'))

# 6 experience
S.append(slide(7, '<div class="kick">02 &nbsp;Experience</div>'
               '<h1>How people can feel safe speaking freely</h1>'
               '<ul class="list">'
               '<li><b>Clear before you sit down.</b> Recording is set in the table settings, so everyone knows the conditions before joining.</li>'
               '<li><b>Visible while you talk.</b> A calm marker on the Live Table, never hidden.</li>'
               '<li><b>Off the record.</b> One tap for &ldquo;don&rsquo;t keep this part&rdquo;, so people can go deeper.</li>'
               '<li><b>Words, not faces.</b> Keep the transcript and notes, never video or audio, and say so plainly.</li>'
               '</ul>'))

# 8 autonomy
S.append(slide(8, '<div class="kick">03 &nbsp;Rules</div>'
               '<h1>Taking part never means <b>giving up ownership</b> of what you said.</h1>'
               '<div class="two">'
               '<div class="card v"><h3>Three separate choices</h3><p>Recording a conversation.</p><p>Keeping it.</p><p>Sharing it beyond the table.</p></div>'
               '<div class="card t"><h3>Yours to change</h3><p>Take part under your name, anonymously, or not recorded.</p><p>Change your mind before, during or after.</p></div>'
               '</div>'
               '<div class="quote">Participation is a contribution, not a resource the platform acquires.</div>'))

# 7 rules
rows = [
    ('Recorded', 'Set in advance in the table settings. Everyone sees it before joining.', 'prop', 'To build'),
    ('Kept', 'Separate from recording. Anyone can leave their words out of what is kept.', 'open', 'Partly built'),
    ('Named', 'Under your name, anonymously, or not recorded at all.', 'prop', 'To build'),
    ('Reconsidered', 'Before, during or after: change how you are named, or withdraw your words.', 'open', 'Partly built'),
    ('Shared', 'Kept within the community by default. Sharing wider needs a separate agreement.', 'prop', 'To build'),
    ('Used', 'Conversations are never used to train AI.', 'on', 'Decided'),
]
tr = ''.join('<tr><td>%s</td><td>%s</td><td><span class="tag %s">%s</span></td></tr>' % r for r in rows)
S.append(slide(9, '<div class="kick">03 &nbsp;Rules</div>'
               '<h1>Who controls what is recorded, kept and shared</h1>'
               '<table><thead><tr><th>What</th><th>Rule</th><th>Status</th></tr></thead><tbody>%s</tbody></table>' % tr, cls='wide'))

# 8 central question
S.append(slide(10, '<div class="kick">The question</div>'
               '<h1>Can we create a culture in which people <b>want</b> their conversations to be preserved, without feeling that they are <b>being watched</b>?</h1>'
               '<div class="lead">Being watched is when someone else keeps a record of you. Preserving is when you choose to give it. The difference is control.</div>',
               dark=True, cls='q'))

# 9 next step
S.append(slide(11, '<div class="kick">Next step</div>'
               '<h1>Test it with a small pilot before we decide</h1>'
               '<div class="grid2"><ul class="list">'
               '<li><b>Two or three founding hosts.</b> A mix of Open and Private tables.</li>'
               '<li><b>Some saved, some not.</b> Same hosts, same topics.</li>'
               '<li><b>Watch the numbers.</b> How many leave their words out, use off the record, come back, or stop at the consent step.</li>'
               '</ul>'
               '<div class="ask"><h3>Ask after every table</h3><p>&ldquo;Did knowing it was saved change what you said?&rdquo;</p>'
               '<small>Everything in these slides is judgement, not data. Nothing has been tested with users yet.</small></div></div>'))

page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>TimeCapsule: Keeping the record</title><style>%s</style></head><body>%s</body></html>') % (CSS, '\n'.join(S))
open(os.path.join(HERE, 'slides.html'), 'w').write(page)
print('ok', len(S), 'slides')
