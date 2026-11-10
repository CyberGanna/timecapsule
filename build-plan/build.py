"""Branded PDF of the TimeCapsule build plan.
Run: python3 build.py && node render.js  ->  TimeCapsule-Build-Plan.pdf
Content lives in content.md (same text as the Claude Doc). Fonts come from fonts.css (static woff, copyable text).
"""
import re, html

SVG = ('<svg viewBox="0 -6 110 82" aria-hidden="true"><defs><clipPath id="ID"><circle cx="35" cy="35" r="30"/>'
       '<path d="M13.8 56.2 L4 74 L29.8 64.5 Z"/></clipPath></defs><circle cx="35" cy="35" r="30" fill="#7C5CFF"/>'
       '<path d="M13.8 56.2 L4 74 L29.8 64.5 Z" fill="#7C5CFF"/><circle cx="75" cy="35" r="30" fill="#17C3C8"/>'
       '<path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#17C3C8"/><g clip-path="url(#ID)"><circle cx="75" cy="35" r="30" fill="#3B2A9E"/>'
       '<path d="M96.2 13.8 L106 -4 L80.2 5.5 Z" fill="#3B2A9E"/></g><g fill="#fff"><circle cx="36" cy="35" r="4.6"/>'
       '<circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g></svg>')
from cutout import cut
SVG = cut(SVG, 'IDm')  # PDFs and presentations use the cut-out logo (transparent link)
WT = '<span class="wt"><b>time</b><i>capsule</i></span>'

ROADMAP = """<div class="road">
<div class="lane">
 <div class="ph"><em>0</em><b>Setup</b><span>Weeks 1–2</span><p>Team, accounts, build list</p></div>
 <div class="ph"><em>1</em><b>Foundation</b><span>Weeks 3–8</span><p>Sign in, tables, invites, emails</p></div>
 <div class="ph"><em>2</em><b>Live Table</b><span>Weeks 9–14</span><p>Video, transcript, Rate and Tip</p></div>
 <div class="ph"><em>3</em><b>Closed beta</b><span>Weeks 15–20</span><p>Founding hosts, Admin, on-call</p></div>
 <div class="ph main"><em>4</em><b>Public launch</b><span>Weeks 21–26</span><p>Globe, Listen in, Trusted, orbits</p></div>
</div>
<div class="gates"><span>Tables can be created</span><span>A full table works</span><span>Beta lessons fixed</span><span>Live for everyone</span></div>
<div class="lane two"><div class="note">Can start alongside Phase 4, or earlier if a private group launches first</div>
 <div class="ph groups"><em>5</em><b>Private groups</b><span>6–8 weeks</span><p>Groups, recurring link, co-hosts</p></div></div>
</div>"""


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
    return t


def md(src):
    out, lines, i = [], src.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith('## '):
            out.append('<h2>%s</h2>' % inline(l[3:])); i += 1
        elif l.startswith('### '):
            out.append('<h3>%s</h3>' % inline(l[4:])); i += 1
        elif l.strip() == '[[ROADMAP]]':
            out.append(ROADMAP); i += 1
        elif l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            head, body = rows[0], rows[2:]
            h = '<table><thead><tr>%s</tr></thead><tbody>' % ''.join('<th>%s</th>' % inline(c) for c in head)
            for r in body:
                cls, lab = '', ''
                m = re.search(r'\s*\{(hi|pick):([^}]*)\}', r[0])
                if m:
                    r = [r[0].replace(m.group(0), '')] + r[1:]
                    cls = ' class="%s"' % m.group(1)
                    lab = '<span class="side">%s</span>' % html.escape(m.group(2))
                cells = ['<td>%s%s</td>' % (lab if k == 0 else '', inline(c)) for k, c in enumerate(r)]
                h += '<tr%s>%s</tr>' % (cls, ''.join(cells))
            if 'class="side"' in h: h = h.replace('<table>', '<table class="labelled">', 1)
            out.append(h + '</tbody></table>')
        elif re.match(r'- \[ \] ', l):
            items = []
            while i < len(lines) and lines[i].startswith('- [ ] '):
                items.append('<li>%s</li>' % inline(lines[i][6:])); i += 1
            out.append('<ul class="tasks">%s</ul>' % ''.join(items))
        elif l.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append('<li>%s</li>' % inline(lines[i][2:])); i += 1
            out.append('<ul>%s</ul>' % ''.join(items))
        elif re.match(r'\d+\. ', l):
            items = []
            while i < len(lines) and re.match(r'\d+\. ', lines[i]):
                items.append('<li>%s</li>' % inline(re.sub(r'^\d+\. ', '', lines[i]))); i += 1
            out.append('<ol>%s</ol>' % ''.join(items))
        else:
            out.append('<p>%s</p>' % inline(l)); i += 1
    return '\n'.join(out)


CSS = open('fonts.css').read() + """
:root{--navy:#0E1230;--ink:#1C1F33;--muted:#6B6F86;--violet:#7C5CFF;--teal:#17C3C8;--deep:#3B2A9E;--paper:#FBFAF7;--line:#E6E3DC}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#fff}
body{font-family:'Newsreader',Georgia,serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:10.6pt;line-height:1.48}
.logo{display:flex;align-items:center;gap:10px;font-family:'Sora',sans-serif}
.wt{letter-spacing:-.01em}.wt b{font-weight:600}.wt i{font-style:normal;font-weight:300}
/* cover */
body.cover{width:210mm;height:297mm;overflow:hidden}
.cv{background:var(--navy);color:#fff;width:210mm;height:297mm;display:flex;flex-direction:column;padding:34mm 26mm}
.cv .logo svg{width:92px;height:68px}.cv .logo .wt{font-size:44px}
.cv .big{margin-top:auto}
.cv .rule{width:56px;height:3px;border-radius:2px;background:linear-gradient(90deg,var(--violet),var(--teal));margin-bottom:26px}
.cv h1{font-family:'Sora',sans-serif;font-weight:300;font-size:46px;letter-spacing:-.02em;line-height:1.1;margin:18px 0 10px}
.cv h1 b{font-weight:600}
.cv .sub{font-family:'Sora',sans-serif;font-weight:300;font-size:16px;color:#C9CCE4;line-height:1.5;max-width:135mm}
.cv .edition{font-family:'Sora',sans-serif;font-weight:300;font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--teal);margin-top:22px}
.cv .toc{list-style:none;margin-top:16mm;padding-top:8mm;border-top:1px solid rgba(255,255,255,.12);font-family:'Sora',sans-serif;font-weight:300;font-size:11.5px;letter-spacing:.04em;color:#B9BCD6;columns:2;column-gap:12mm}
.cv .toc li{margin:0 0 7px}.cv .toc b{color:var(--teal);font-weight:600;margin-right:10px}
/* body pages */
@page{size:A4;margin:26mm 22mm 22mm}
.head .logo svg{width:26px;height:19px}.head .wt{font-size:13px;color:var(--navy)}
.head .tag{font-family:'Sora',sans-serif;font-size:8.5px;letter-spacing:.22em;color:var(--muted);text-transform:uppercase}
h2{font-family:'Sora',sans-serif;font-weight:300;font-size:25px;letter-spacing:-.015em;color:var(--navy);line-height:1.2;margin:10mm 0 5mm;break-after:avoid;page-break-after:avoid}
h2{padding-top:12px;background:linear-gradient(90deg,var(--violet),var(--teal)) no-repeat 0 0/22px 2px}
h2.first{margin-top:0}
h2.newpage{break-before:page;page-break-before:always;margin-top:0}
h3{font-family:'Sora',sans-serif;font-weight:600;font-size:13px;color:var(--navy);margin:7mm 0 2.5mm;break-after:avoid}
p{margin-bottom:3.2mm}
p i{color:var(--deep)}
ul,ol{margin:0 0 4mm;padding:0;list-style:none}
li{position:relative;padding-left:7mm;margin-bottom:2.4mm;break-inside:avoid}
ul>li::before{content:"";position:absolute;left:0;top:.45em;width:8px;height:8px;border-radius:50%;border:2px solid var(--teal);background:#fff}
ol{counter-reset:n}
ol>li{counter-increment:n;padding-left:9mm}
ol>li::before{content:counter(n,decimal-leading-zero);position:absolute;left:0;top:.2em;font-family:'Sora',sans-serif;font-size:8.5pt;font-weight:600;letter-spacing:.1em;color:var(--violet)}
li b,td b{font-family:'Sora',sans-serif;font-weight:600;font-size:.9em;color:var(--navy)}
ul.tasks li::before{border-radius:3px;border-color:var(--violet);width:9px;height:9px}
table{width:100%;border-collapse:collapse;margin:2mm 0 5mm;font-size:9pt;line-height:1.38;break-inside:auto}
thead{display:table-header-group}
tr{break-inside:avoid}
th{font-family:'Sora',sans-serif;font-weight:600;font-size:7.6pt;letter-spacing:.06em;text-transform:uppercase;text-align:left;color:#fff;background:var(--navy);padding:2.4mm 2.6mm;vertical-align:bottom}
th:first-child{border-radius:6px 0 0 0}th:last-child{border-radius:0 6px 0 0}
td{padding:2.2mm 2.6mm;border-bottom:1px solid var(--line);vertical-align:top}
td:first-child{font-family:'Sora',sans-serif;font-size:8.2pt;font-weight:400;color:var(--navy)}
tr.hi td{background:rgba(124,92,255,.07)}
tr.pick td{background:rgba(23,195,200,.16);border-bottom-color:rgba(23,195,200,.5)}
tr.pick td:first-child{box-shadow:inset 3px 0 0 #17C3C8}
tr.hi td:first-child{box-shadow:inset 3px 0 0 #7C5CFF}
tr.hi td,tr.pick td{height:24mm}
td{position:relative}
table.labelled{width:calc(100% - 7mm);margin-left:7mm}
.side{position:absolute;right:calc(100% + 2mm);top:50%;transform:translateY(-50%) rotate(180deg);writing-mode:vertical-rl;white-space:nowrap;font-family:'Sora',sans-serif;font-size:5pt;font-weight:600;letter-spacing:.05em;text-transform:uppercase}
tr.hi .side{color:#7C5CFF}tr.pick .side{color:#0E9BA0}
tbody tr:last-child.hi td{background:rgba(23,195,200,.10)}
/* roadmap */
.road{margin:4mm 0 7mm;font-family:'Sora',sans-serif;break-inside:avoid}
.lane{display:grid;grid-template-columns:repeat(5,1fr);gap:2.2mm}
.ph{border:1px solid #D9D6EA;border-radius:8px;padding:3mm 2.8mm;background:#fff;min-height:29mm}
.ph em{font-style:normal;font-size:7.5pt;font-weight:600;letter-spacing:.14em;color:var(--violet);display:block}
.ph b{display:block;font-size:9.6pt;font-weight:600;color:var(--navy);margin:1mm 0 .6mm;line-height:1.2}
.ph span{display:block;font-size:7.6pt;color:var(--muted);font-weight:300;margin-bottom:1.6mm}
.ph p{font-size:8pt;line-height:1.35;margin:0;color:var(--ink);font-family:'Sora',sans-serif;font-weight:300}
.ph.main{background:var(--navy);border-color:var(--navy)}
.ph.main b,.ph.main p{color:#fff}.ph.main span{color:#B9BCD6}.ph.main em{color:var(--teal)}
.gates{display:grid;grid-template-columns:repeat(4,1fr);margin:2.4mm 0 0 calc(20% - 1mm);font-size:7.2pt;color:var(--muted);font-weight:300}
.gates span{position:relative;padding-left:4mm}
.gates span::before{content:"";position:absolute;left:0;top:.35em;width:6px;height:6px;transform:rotate(45deg);background:var(--teal)}
.lane.two{margin-top:4mm;grid-template-columns:4fr 1fr;align-items:center}
.note{text-align:right;font-size:7.8pt;color:var(--muted);font-weight:300;padding-right:4mm}
.ph.groups{border-style:dashed;border-color:var(--violet);background:rgba(124,92,255,.05)}
"""

body = md(open('content.md').read())
heads = re.findall(r'<h2>(.*?)</h2>', body)
# section breaks: start these sections on a new page
for k, t in enumerate(heads):
    cls = 'first' if k == 0 else ('newpage' if t in ('Phases',) else '')
    body = body.replace('<h2>%s</h2>' % t, '<h2 class="%s">%s</h2>' % (cls, t), 1)

toc = ''.join('<li><b>%02d</b>%s</li>' % (k + 1, re.sub('<.*?>', '', t).replace(', and when each one blocks the build', '')) for k, t in enumerate(heads))
cover = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>TimeCapsule build plan</title><style>%s @page{size:A4;margin:0}</style></head>'
         '<body class="cover"><div class="cv"><div class="logo">%s%s</div><div class="big"><div class="rule"></div>'
         '<h1><b>Build plan</b><br>from prototype to launch</h1><div class="sub">Recommended stack, phases, team options and rough costs for taking TimeCapsule live.</div>'
         '<div class="edition">10 November 2026 · draft for discussion</div></div><ul class="toc">%s</ul></div></body></html>') % (
    CSS, SVG.replace('ID', 'cv'), WT, toc)
page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>TimeCapsule build plan</title><style>%s</style></head>'
        '<body>%s</body></html>') % (CSS, body)
hdr = ('<style>%s .h{width:100%%;padding:0 22mm;margin-top:9mm;display:flex;justify-content:space-between;align-items:center;-webkit-print-color-adjust:exact} .h svg{width:22px;height:16px} .h .wt{font-family:Sora;font-size:11px;color:#0E1230} .h .wt b{font-weight:600}.h .wt i{font-style:normal;font-weight:300} .h .tag{font-family:Sora;font-weight:300;font-size:7px;letter-spacing:2px;color:#6B6F86}</style><div class="h"><div style="display:flex;align-items:center;gap:7px">%s%s</div><div class="tag">BUILD PLAN</div></div>') % (open('fonts.css').read(), SVG.replace('ID','hd'), WT)
open('header.html','w').write(hdr)
open('cover.html', 'w').write(cover)
open('plan.html', 'w').write(page)
print('ok', len(heads), 'sections')
