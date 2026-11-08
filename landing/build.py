# Builds the public, signed-out landing page (globe hero + about + long read).
# Base: world-base.html = a fresh read of the live World globe artifact (WXKBrXY78yuhpghQCpK3RU).
# Usage: python3 build.py   ->  timecapsule-landing.html
import re, json
SIGNIN = 'https://claude.ai/artifact/BFBabdFxq8LxqDChfvRn61'
ONB = 'https://claude.ai/artifact/Q7o5JaMGP7bHLXzJ6aw6TH'
AGENDA = 'https://claude.ai/artifact/1HRtzD5kj8RFhEngLuAgU5'
GUIDES = 'https://claude.ai/artifact/WHk7qYCmXBgugxJW1kqevd'
FAQ = 'https://claude.ai/artifact/LTQdD5XzBLaDbCRrhHttMK'

src = open('world-base.html', encoding='utf8').read()
i = src.find('<!doctype html>\n<html lang="en">'); assert i >= 0
src = src[i:]
j = src.find('</html>'); src = src[:j + 7] + '\n'

def rep(h, a, b, n=1):
    assert a in h, a[:90]
    return h.replace(a, b, n)

s = src
s = rep(s, '<title>TimeCapsule Orbit</title>', '<title>TimeCapsule</title>')
s = rep(s, 'family=Sora:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap',
        'family=Sora:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap')
# header nav: in-page sections
nav = re.search(r'<nav class="tch-nav" aria-label="Main">.*?</nav>', s, re.S).group(0)
s = s.replace(nav, '<nav class="tch-nav" aria-label="Main"><a href="#about">About</a><a href="#how">How it works</a><a href="#deeper">Manifesto</a><a href="' + AGENDA + '" target="_top">Tables</a></nav>', 1)
# hero copy
hud = re.search(r'<div class="hud">.*?</div>', s, re.S).group(0)
s = s.replace(hud, '''<div class="hud">
  <h1 class="lp-h"><span>The table is digital.</span><span>The people are real.</span></h1>
  <p>Small tables, real people, every corner of the world. Talk, listen and think together.</p>
  <div class="lp-acts"><a class="cta" href="''' + ONB + '''" target="_top">Join TimeCapsule <span aria-hidden="true">→</span></a><a class="ghost" href="#read=believe" data-go="believe">Read the manifesto</a></div>
</div>''', 1)
# pause drawing while the globe is scrolled away or the long read is open
s = rep(s, 'try{draw(now)}catch(e){console.error(e)}', 'if(!window.__lpPause)try{draw(now)}catch(e){console.error(e)}')
# always signed out
s = rep(s, 'if(/[#&]out\\b/.test(location.hash))proto.querySelector(\'[data-so="1"]\').click();', 'proto.querySelector(\'[data-so="1"]\').click();')
# footer
foot = open('../help/footer.html', encoding='utf8').read()
foot = foot.replace('GUIDES_URL', GUIDES).replace('FAQ_URL', FAQ)
foot = rep(foot, '<a href="https://claude.ai/artifact/3erX1TAL2xoYjAmfvqkWtp" target="_top">Invite friends</a><a href="https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy" target="_top">Settings</a>',
           '<a href="' + SIGNIN + '" target="_top">Sign in</a>')
foot = rep(foot, 'href="' + AGENDA + '" target="_top" aria-label="TimeCapsule home"', 'href="#" aria-label="TimeCapsule home"')
body = open('body.html', encoding='utf8').read().replace('<!--FOOTER-->', foot)
s = rep(s, '<div id="lbar" hidden', body + '\n<div id="lbar" hidden')
# dictionary
m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, re.S)
D = json.loads(m.group(1))
n = 0
for ln in open('dict-landing.txt', encoding='utf8'):
    if ln.strip():
        e, it, es = ln.rstrip('\n').split('|'); D[e] = [it, es]; n += 1
js = json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
s = s[:m.start(1)] + js + s[m.end(1):]
open('timecapsule-landing.html', 'w', encoding='utf8').write(s)
print(len(s), 'bytes,', n, 'landing strings')
