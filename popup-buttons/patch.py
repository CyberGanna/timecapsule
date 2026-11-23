"""Karim 2026-11-23: Chat and Follow on the person pop-up look the same as on the Profile page
(rounded rectangle radius 10, 34px, light fill, icon + word: violet chat icon "Chat", teal person icon "Follow").
Idempotent, marker "tc-popbtn". Re-run after rebuilding pages with the person pop-up."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = 'title="Chat">${TCP_CHAT}</a>'
NEW = 'title="Chat">${TCP_CHAT}<span>Chat</span></a>'
CSS = ('<style id="tc-popbtn">'
       '.tcp .tcpa button,.tcp .tcpa a.ic{height:34px!important;min-height:34px;border-radius:10px!important;border:1px solid var(--line,#3A4175)!important;'
       'background:rgba(255,255,255,.05)!important;color:#EEF1FF!important;padding:0 11px!important;width:auto!important;font-size:13px;font-weight:500;gap:6px}'
       '.tcp .tcpa{gap:6px!important}.tcp .tcpa a.pf{white-space:nowrap}'
       '.tcp .tcpa svg{width:15px!important;height:15px!important;stroke-width:1.9!important}'
       '.tcp .tcpa a.ic svg{color:#A48DFF}'
       '.tcp .tcpa a.ic:hover{border-color:#7C5CFF!important;background:rgba(124,92,255,.14)!important}'
       '.tcp .tcpa button.tcpf svg{color:#7FF0F2}'
       '.tcp .tcpa button.tcpf:hover{border-color:#17C3C8!important;background:rgba(23,195,200,.14)!important}'
       '.tcp .tcpa button.tcpf.on{border-color:rgba(23,195,200,.55)!important;background:rgba(23,195,200,.12)!important;color:#EEF1FF!important}'
       '</style>')
for d, _, fs in os.walk(ROOT):
    if '.git' in d: continue
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf8').read()
        if OLD not in s or 'tc-popbtn' in s: continue
        s = s.replace(OLD, NEW)
        k = s.rfind('</body>'); s = s[:k] + CSS + s[k:] if k >= 0 else s + CSS
        open(p, 'w', encoding='utf8').write(s); print(os.path.relpath(p, ROOT))
