# Builds journey.html (Ted's user journey) from the manifesto PDF's fonts and style.
# Run: python3 build.py [ted|fedor]  ->  journey.html / journey-fedor.html ; then node print.js [ted|fedor]
import sys
WHO = sys.argv[1] if len(sys.argv) > 1 else 'ted'
import re, base64, os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, '../manifesto/out.html')).read()
fonts = re.search(r'<style>@font-face.*?</style>', src, re.S).group(0)
logo = re.search(r'<svg viewBox="0 -6 110 82" aria-hidden="true">.*?</svg>', src, re.S).group(0)
def mark(i):
    from cutout import cut  # PDFs use the cut-out logo (transparent link)
    return cut(logo.replace('id="c0"', 'id="m%d"' % i).replace('url(#c0)', 'url(#m%d)' % i), 'k%d' % i)

def img(n):
    b = base64.b64encode(open(os.path.join(D, 'shots' if WHO == 'ted' else 'shots-fedor', n + '.jpg'), 'rb').read()).decode()
    return 'data:image/jpeg;base64,' + b

# (eyebrow, title, lead, [paragraphs], [(shot, caption)], footer)
STEPS = [
 ("Discover", "Ted <b>listens in</b>",
  "Ted wants to talk about the big questions with real people, not scroll another feed. He goes to TimeCapsule to see what it is.",
  ["The first thing he sees is a globe: <i>The world, talking</i>. Every dot is a table where people are talking right now. He clicks a dot in Lisbon and listens in for five free minutes, without signing in.",
   "He scrolls down and reads the rest in plain words: small tables, real conversations, hosted by the people who create them, and a record of what was said that can outlive the evening."],
  [("landing", "The landing page: “The world, talking”. Click a dot to listen in.")], "Discover"),
 ("Join", "Ted <b>pulls up a chair</b>",
  "Ted wants to take part, not just listen. He taps “Join TimeCapsule” to create his account.",
  ["Joining takes about a minute, one calm question per screen. He continues with Google, writes his first name (an alias would be fine too), picks two topics, Philosophy and History, then one book that stayed with him, <i>The Little Prince</i>, and one film, <i>Cinema Paradiso</i>. He could skip both.",
   "On the right his universe grows as he answers: topics become coloured nebulae, the book and the film become his first stars. These help TimeCapsule suggest tables and people with a similar taste, never ads."],
  [("onb-book", "Onboarding: one book that stayed with you."), ("onb-done", "“Welcome, Ted. Your universe has begun.”")], "Join"),
 ("Find", "Ted <b>finds a table</b>",
  "Ted wants a conversation he can join tonight. He opens the Tables page to see what is on.",
  ["“Pull up a chair.” No feeds, no algorithms, just people, live. He filters by Live now, Today, Tomorrow or This week, by topic and by language. Each card shows the question, the host, the faces around the table and how many chairs are still free.",
   "One title catches his eye: <i>Is free will an illusion?</i>, hosted by Gregory in Thessaloniki, Philosophy, six people at the table, two chairs free."],
  [("tables", "The Tables page: “Pull up a chair”.")], "Find a table"),
 ("Decide", "Ted <b>saves a chair</b>",
  "Ted wants to know who is hosting and what to expect. He opens the table page.",
  ["He reads Gregory’s question, sees the Trusted badge next to his name, who else is coming, when it starts, the language and whether a transcript of the discussion will be kept. A countdown shows how long until it begins.",
   "He taps “Save a chair”, chooses to show his name, and adds it to his calendar. One hour before, an email reminds him. If something comes up, he can give his chair back so someone else can sit."],
  [("table", "The table page, with “Save a chair” and Share.")], "Save a chair"),
 ("Arrive", "Ted <b>checks his camera</b>",
  "Ted wants to arrive ready, not fumbling with settings. When the table goes live he taps “Join”.",
  ["A short check opens first: his camera preview, the microphone, a background blur, and one choice, whether the table sees his name or an alias. A line reminds him of the spirit of the place: listen first and speak in turns.",
   "He taps “Join the table”."],
  [("camera", "Camera check: “Ready to join?”")], "Arrive"),
 ("Talk", "Ted <b>sits at the table</b>",
  "Ted wants to be heard, and to really listen. He joins the Live Table with seven other people.",
  ["Gregory opens with a question and guides the turns. Ted raises his hand, waits, and speaks. On the side a live transcript follows the conversation line by line. The Messages tab is for private notes to the host or a guest, People shows who is at the table.",
   "In his private Notes, which only he can see, Ted quotes a line Mia said and marks it Keep. Another note he flags Ask: it goes to Gregory, who brings it to the whole table. After an hour Gregory ends the table."],
  [("live", "The Live Table: video, live transcript, Messages, Notes and People.")], "The Live Table"),
 ("Thank", "Ted <b>rates and tips</b>",
  "Ted wants to thank the people who made him think. When the table ends, TimeCapsule asks how it was.",
  ["“How was the discussion?” Mind-blowing, Pleasant or Not so inspiring, with an optional note. Then he has 8 TimeCoins to award to the panelists. He gives some to Mia for the line he kept and some to Gregory for hosting well.",
   "Tips are a thank-you, not a payment. Coins he does not give expire in a few days. If he closes the window, an email the next day reminds him."],
  [("rate", "“How was the discussion?”"), ("rate-tip", "Award your favourite panelists with TimeCoins.")], "Rate and tip"),
 ("Keep", "Ted <b>keeps the record</b>",
  "Ted wants to remember what was said. He goes back to My tables the next morning.",
  ["Gregory had turned on “Keep a transcript of the discussion”, so it is saved with the names of who said what, together with the notes Ted marked Keep. It becomes public in the library only if everyone at the table agrees. Ideas keep their authorship and their context, so others can return to them, question them and build on them.",
   "My tables also lists what is coming: the tables he saved and, soon, the ones he will host."],
  [("mytables", "My tables: upcoming and past tables in one place.")], "Keep the record"),
 ("Belong", "Ted <b>fills his universe</b>",
  "Ted wants to meet people on his wavelength. He opens his profile.",
  ["His profile shows the topics he talks about, the tables he joined, the feedback and TimeCoins he received, and his universe: the books and films that shaped him.",
   "Where his orbits cross someone else’s, it is an opportunity for an exchange. On the People page he finds Elena, who also loved <i>Cinema Paradiso</i> and hosts History tables on Sundays. He follows her."],
  [("profile", "A profile, with the universe of books and films behind it.")], "Profile and universe"),
 ("Earn", "Ted <b>looks at his TimeCoins</b>",
  "Ted wants to know what his coins mean. He opens the TimeCoins page from his profile.",
  ["There are two numbers. <b>Received</b> is his reputation: it shows on his profile, it never drops and it counts towards Trusted. Reputation coins can never be bought. <b>To use</b> are coins he can spend on extras for the tables he hosts, such as two more chairs or thirty more minutes.",
   "There is no daily-login gift. Coins come from people, after a good discussion."],
  [("coins", "Your TimeCoins: Received and To use.")], "TimeCoins"),
 ("Host", "Ted <b>hosts his own table</b>",
  "Ted wants to ask his own question. He taps “Create a table”.",
  ["He picks History, writes “What do we owe strangers?”, chooses Thursday at 19:00, six chairs, English, an Open table, and keeps the transcript setting on. A preview shows how the card will look on the Tables page.",
   "Every table is hosted by the person who creates it. As host he opens the conversation, gives the turns and ends the table. After it, “Host again” fills in a new table for the same time next week."],
  [("create", "Create a table, with a live preview of the card.")], "Host a table"),
 ("Invite", "Ted <b>invites a friend</b>",
  "Ted wants his friend Sara at his next table. He opens “Invite friends to join TimeCapsule”.",
  ["He sends her his link. When Sara joins, they both receive 2 TimeCoins, and 5 more each when they sit at a table together, up to 10 a week. He can also invite her straight to a single table.",
   "On Thursday Sara takes one of Ted’s six chairs."],
  [("invite", "Invite friends to join TimeCapsule.")], "Invite friends"),
 ("Trust", "Ted <b>becomes Trusted</b>",
  "Ted wants people to know he is a good host. He keeps coming back, week after week.",
  ["Trust grows through repeated participation. His path goes from New to Member to Trusted and then Trusted host, measured by the tables he finishes, the people who thank him, the weeks he shows up and a clean record. It is earned, never bought.",
   "Three months in, the light-blue Trusted badge appears next to his name. <span class=\"note\">The exact rule is still a proposal.</span>"],
  [("trust", "Your path to Trusted.")], "Trusted"),
 ("Return", "Ted <b>is part of the world, talking</b>",
  "Ted wanted a conversation. He found a place he comes back to.",
  ["On a Thursday evening his table lights up on the globe. Somewhere, someone clicks the dot and listens in to Ted, Sara and four strangers talking about what we owe each other.",
   "What they say stays, with their names on it, for whoever comes next."],
  [("world", "The World page: every dot is a table, live.")], "Return"),
]

CSS = r"""
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{--navy:#0E1230;--ink:#1C1F33;--muted:#6B6F86;--violet:#7C5CFF;--teal:#17C3C8;--paper:#FBFAF7;--line:#E6E3DC}
html,body{background:var(--paper)}
body{font-family:'Newsreader',Georgia,serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;padding:28mm 24mm 24mm}
.page:last-child{page-break-after:auto}
.logo{display:flex;align-items:center;gap:10px;font-family:'Sora',sans-serif}
.wt{font-size:22px;letter-spacing:-.01em}.wt b{font-weight:600}.wt i{font-style:normal;font-weight:300}
.cover{background:var(--navy);color:#fff;display:flex;flex-direction:column;padding:34mm 26mm}
.cover .logo svg{width:92px;height:68px}.cover .wt{font-size:44px}
.cover .big{margin-top:auto}
.cover .rule{width:56px;height:3px;border-radius:2px;background:linear-gradient(90deg,var(--violet),var(--teal));margin-bottom:26px}
.cover h1{color:#fff;font-size:46px;margin:22px 0 10px}
.cover .sub{font-family:'Sora',sans-serif;font-weight:300;font-size:15px;letter-spacing:.32em;color:#B9BCD6;text-transform:uppercase}
.cover .q{font-family:'Newsreader',serif;font-style:italic;font-size:17pt;line-height:1.45;color:#D9DBEE;margin-top:16mm;max-width:130mm}
.head{display:flex;justify-content:space-between;align-items:center;position:absolute;top:12mm;left:24mm;right:24mm}
.head svg{width:26px;height:19px}.head .wt{font-size:13px;color:var(--navy)}
.head .num{font-family:'Sora',sans-serif;font-size:9px;letter-spacing:.2em;color:var(--muted);text-transform:uppercase}
.eyebrow{font-family:'Sora',sans-serif;font-size:11px;letter-spacing:.28em;color:var(--violet);font-weight:600;margin-bottom:12px;display:flex;align-items:center;gap:12px;text-transform:uppercase}
.eyebrow::before{content:"";width:22px;height:2px;background:linear-gradient(90deg,var(--violet),var(--teal));border-radius:2px}
h1{font-family:'Sora',sans-serif;font-weight:300;font-size:32px;letter-spacing:-.02em;color:var(--navy);line-height:1.15;margin-bottom:7mm}
h1 b{font-weight:600}
p{font-size:12pt;line-height:1.55;margin-bottom:3.6mm}
p.lead{font-size:14pt;line-height:1.45;color:var(--navy);margin-bottom:5mm}
p b{font-family:'Sora',sans-serif;font-weight:600;font-size:10.5pt;color:var(--navy)}
.note{color:var(--muted);font-style:italic}
figure{margin-top:6mm}
figure img{display:block;width:100%;border-radius:10px;box-shadow:0 1px 0 var(--line),0 10px 28px rgba(14,18,48,.16)}
figcaption{font-family:'Sora',sans-serif;font-size:8.5pt;color:var(--muted);margin-top:3mm}
.two{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.two figure img{border-radius:7px}
.pagefoot{position:absolute;bottom:12mm;left:24mm;right:24mm;border-top:1px solid var(--line);padding-top:4mm;font-family:'Sora',sans-serif;font-size:8.5px;letter-spacing:.2em;color:var(--muted);text-transform:uppercase;display:flex;justify-content:space-between}
.toc{list-style:none;margin-top:4mm;columns:2;column-gap:10mm}
.toc li{break-inside:avoid;padding:3mm 0;border-top:1px solid var(--line);font-size:12pt;line-height:1.35}
.gaps{list-style:none;margin-top:2mm}.gaps li{position:relative;padding:0 0 0 8mm;margin-bottom:2.1mm;font-size:10pt;line-height:1.42}.gaps li::before{content:"";position:absolute;left:0;top:.45em;width:9px;height:9px;border-radius:50%;border:2px solid var(--teal)}.gaps li.no::before{border-color:var(--violet);background:var(--violet)}.gaps b{font-family:'Sora',sans-serif;font-weight:600;font-size:9pt;color:var(--navy)}.key{font-family:'Sora',sans-serif;font-size:8.5pt;color:var(--muted);margin:2mm 0 5mm;display:flex;gap:8mm}.key i{display:inline-block;width:8px;height:8px;border-radius:50%;border:2px solid var(--teal);margin-right:2mm}.key i.no{border-color:var(--violet);background:var(--violet)}
.toc li span{display:block;font-family:'Sora',sans-serif;font-size:8.5pt;letter-spacing:.2em;color:var(--violet);font-weight:600;margin-bottom:1mm;text-transform:uppercase}
"""

def head(i):
    m = mark(i).replace(' aria-hidden="true"', '')
    return '<div class="head"><div class="logo">%s<span class="wt"><b>time</b><i>capsule</i></span></div><span class="num">%s</span></div>' % (m, NAME)

def figs(shots):
    f = ''.join('<figure><img src="%s" alt=""><figcaption>%s</figcaption></figure>' % (img(n), c) for n, c in shots)
    return '<div class="two">%s</div>' % f if len(shots) > 1 else f


if WHO == 'fedor':
    from fedor import STEPS, META, EXTRA
else:
    META = dict(name='Ted’s journey', file='journey.html',
        cover_q='Ted wants to talk about the big questions with real people. This is what happens when he goes to TimeCapsule.',
        meet='Meet Ted', meet_h1='One person, <b>fourteen steps</b>',
        meet_lead='Ted is 34 and lives in Lisbon. He reads a lot, argues with podcasts in his head, and misses the long conversations he used to have at university.',
        meet_p='This is his first months on TimeCapsule, told as a story, from the first time he listens in to the day he becomes a Trusted host. Every screen in it is a real page of the current prototype.')
    EXTRA = []
NAME = META['name']

pages = []
pages.append('''<section class="page cover">
  <div class="logo">%s</div>
  <div class="big">
    <div class="rule"></div>
    <div class="logo"><span class="wt"><b>time</b><i>capsule</i></span></div>
    <h1>%s</h1>
    <div class="sub">The TimeCapsule experience, step by step</div>
    <p class="q">%s</p>
  </div>
</section>''' % (mark(999), NAME, META['cover_q']))

toc = ''.join('<li><span>%02d · %s</span>%s</li>' % (i + 1, s[0], re.sub('<[^>]+>', '', s[1])) for i, s in enumerate(STEPS))
toc += ''.join('<li><span>%s</span>%s</li>' % (e[0], re.sub('<[^>]+>', '', e[1])) for e in EXTRA)
pages.append('''<section class="page">%s
  <div class="eyebrow">%s</div>
  <h1>%s</h1>
  <p class="lead">%s</p>
  <p>%s</p>
  <ul class="toc">%s</ul>
  <div class="pagefoot"><span>%s</span><span>2</span></div>
</section>''' % (head(1), META['meet'], META['meet_h1'], META['meet_lead'], META['meet_p'], toc, META['meet']))

for i, (eb, h, lead, ps, shots, foot) in enumerate(STEPS):
    n = i + 3
    body = '<p class="lead">%s</p>%s%s' % (lead, ''.join('<p>%s</p>' % p for p in ps), figs(shots))
    pages.append('<section class="page">%s\n<div class="eyebrow">Step %02d · %s</div>\n<h1>%s</h1>\n%s\n<div class="pagefoot"><span>%s</span><span>%d</span></div>\n</section>' % (head(n), i + 1, eb, h, body, foot, n))
for j, (eb, h, body, foot) in enumerate(EXTRA):
    n = len(STEPS) + 3 + j
    pages.append('<section class="page">%s\n<div class="eyebrow">%s</div>\n<h1>%s</h1>\n%s\n<div class="pagefoot"><span>%s</span><span>%d</span></div>\n</section>' % (head(n), eb, h, body, foot, n))

html = '<!doctype html>\n<html><head><meta charset="utf-8"><title>TimeCapsule · %s</title>\n%s\n<style>%s</style></head><body>\n%s\n</body></html>' % (NAME, fonts, CSS, '\n'.join(pages))
html = html.replace('Time Capsule', 'TimeCapsule')
assert 'Agenda' not in html
open(os.path.join(D, META['file']), 'w').write(html)
print(len(pages), 'pages')
