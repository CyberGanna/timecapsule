# Builds the public, signed-out landing page (globe hero + about + long read).
# Base: world-base.html = a fresh read of the live World globe artifact (WXKBrXY78yuhpghQCpK3RU).
# Usage: python3 build.py   ->  timecapsule-landing.html
import re, json, os, sys
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
  <h1 class="lp-h">The world, talking</h1>
  <p>Small tables, real people, every corner of the world. Talk, listen and think together.</p>
  <div class="lp-acts"><a class="cta" href="''' + ONB + '''" target="_top">Join TimeCapsule <span aria-hidden="true">→</span></a></div>
</div>''', 1)
# pause drawing while the globe is scrolled away or the long read is open
s = rep(s, 'try{draw(now)}catch(e){console.error(e)}', 'if(!window.__lpPause)try{draw(now)}catch(e){console.error(e)}')
# every table on the globe is open to listeners (Karim: no grey dots), simple hint
s = re.sub(r'TABLES\.forEach\(\(T,k\)=>T\.lis=[^;]*\);', 'TABLES.forEach(T=>T.lis=true);', s, count=1)
s = rep(s, '<span class="dk">Click a teal dot to listen in</span><span class="mb">Tap a teal dot to listen in</span>', '<span class="dk">Click a dot to listen in</span><span class="mb">Tap a dot to listen in</span>')
# table card: no coordinates / live-since block (Karim: too many modals)
s = re.sub(r'\n\s*<div class="coord">Host at .*?</div>', '', s, count=1)
# always signed out
s = rep(s, 'if(/[#&]out\\b/.test(location.hash))proto.querySelector(\'[data-so="1"]\').click();', 'proto.querySelector(\'[data-so="1"]\').click();')
# footer
foot = open('../help/footer.html', encoding='utf8').read()
foot = foot.replace('GUIDES_URL', GUIDES).replace('FAQ_URL', FAQ)
# footer links (Karim 2026-11-09): only Help (to Guides), Terms and Privacy
LEGAL = 'https://claude.ai/artifact/5dZ8VXcg7f29xHcecFWd72'
foot = re.sub(r'<nav aria-label="Help and more">.*?</nav>', '<nav aria-label="Help and more"><a href="' + GUIDES + '" target="_top">Help</a><a href="' + LEGAL + '#terms" target="_top">Terms</a><a href="' + LEGAL + '#privacy" target="_top">Privacy</a></nav>', foot, count=1, flags=re.S)
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
# 1) artifact version (claude.ai links), for publishing as an Artifact
open('timecapsule-landing-artifact.html', 'w', encoding='utf8').write(s)
# 2) site version (relative links inside the GitHub / Cloudflare site, #lang kept by tc-i18n)
SITE = {'1HRtzD5kj8RFhEngLuAgU5': 'help/live-pages/agenda.html', 'WXKBrXY78yuhpghQCpK3RU': 'world/timecapsule-world.html',
 'AQKmmAgq8JPDsrRACWEy6i': 'table-detail/timecapsule-table.html', 'MFBQwEDcUA8ctJbo2BWShj': 'help/live-pages/create.html',
 'GPnp3CiH7iGDpkbqvA4cLB': 'help/live-pages/mytables.html', 'TQ3edAr7Dje1uPbGk3yEQy': 'profile/timecapsule-profile.html',
 'MTbRjvLFV7pPhBjpvAzXaq': 'help/live-pages/people.html', 'PYd4f8xrcNkPc2TyPkE4ib': 'help/live-pages/chats.html',
 'SggBcVnWacDjzBsZeke1D1': 'notifications/notifications.html', 'NdgohZznzHtQ8p2PmohNhE': 'search/timecapsule-search.html',
 'PAUksqiFCEtbuDeWsoXjWy': 'help/live-pages/settings.html', 'BFBabdFxq8LxqDChfvRn61': 'auth/timecapsule-signin.html',
 'Q7o5JaMGP7bHLXzJ6aw6TH': 'onboarding/timecapsule-onboarding.html', '3erX1TAL2xoYjAmfvqkWtp': 'invite/timecapsule-invite.html',
 'VRtXrcZBGsWhfQkPMZuKpK': 'timecoins/timecapsule-timecoins.html', '9vjFardtQTDB9NgmX9g9em': 'trust/timecapsule-trust-meter.html',
 'WHk7qYCmXBgugxJW1kqevd': 'help/timecapsule-guides.html', 'LTQdD5XzBLaDbCRrhHttMK': 'help/timecapsule-faq.html',
 'GcdFnhR5eggq6hB7fm1Njw': 'admin/timecapsule-admin.html'}
t = s
for k, v in SITE.items():
    t = t.replace('https://claude.ai/artifact/' + k, '../' + v)
t = rep(t, 'if(!url||!/claude\\.ai\\/(code\\/)?artifact\\//.test(url))return url;', 'if(!url||!/claude\\.ai\\/(code\\/)?artifact\\/|\\.html(#|$)/.test(url))return url;')
t = t.replace(LEGAL, '../legal/timecapsule-legal.html')
open('timecapsule-landing.html', 'w', encoding='utf8').write(t)
left = sorted(set(re.findall(r'claude\.ai/artifact/[A-Za-z0-9]+', t)))
print(len(s), 'bytes,', n, 'landing strings; claude.ai links left in site version:', left)
# 3) Greek (EL): post-process both outputs (script owned by the "Add Greek to the languages" thread)
import subprocess
GR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'i18n', 'add-greek.py')
if os.path.exists(GR):
    subprocess.run([sys.executable, GR, 'timecapsule-landing-artifact.html', 'timecapsule-landing.html'], check=True)
