#!/usr/bin/env python3
"""One topic per table (Karim, 2026-11-22).
A table, and the conversation it leaves behind, has exactly one topic. The Profile
Tables tab showed two topic tags per row; cut every row to its main topic (the
same topic the table has on the Tables page, Conversations and My tables).
Idempotent. Re-run after rebuilding any Profile page.
Usage: python3 one-topic/patch.py [files...]   (defaults below)"""
import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["profile/timecapsule-profile.html", "profile/timecapsule-profile-v2.html",
         "help/live-pages/profile.html", "invite/pages/profile.html"]
MAIN = {  # title -> main topic, as on every other page
    "Is free will an illusion?": "Philosophy", "Stoics at the kitchen table": "Philosophy",
    "Phenomenology vs. God": "Philosophy", "Wind and the future of energy": "Energy",
    "Fix it yourself": "Craft", "Road trips that changed us": "Travel",
    "What makes a room feel like home": "Home", "Is faith a choice?": "Religion",
    "Slow travel": "Travel", "The ethics of repair": "Philosophy", "Homes that hold us": "Home",
    "Solar on every roof?": "Energy", "Kierkegaard on anxiety": "Philosophy",
    "Walking as thinking": "Travel"}

def fix(s):
    n = 0
    # static rows: <b>Title</b><small>..</small><span class="ttags"><i>A</i><i>B</i></span>
    def st(m):
        nonlocal n
        tags = re.findall(r"<i>([^<]*)</i>", m.group(3))
        if len(tags) < 2: return m.group(0)
        n += 1
        return m.group(1) + '<span class="ttags"><i>' + MAIN.get(m.group(2), tags[0]) + "</i></span>"
    s = re.sub(r'(<b>([^<]*)</b><small>[^<]*</small>)<span class="ttags">((?:<i>[^<]*</i>)+)</span>', st, s)
    # data arrays: ["Title","when",["A","B"],...
    def ar(m):
        nonlocal n
        tags = re.findall(r'"([^"]*)"', m.group(3))
        if len(tags) < 2: return m.group(0)
        n += 1
        return m.group(1) + '["' + MAIN.get(m.group(2), tags[0]) + '"]'
    s = re.sub(r'(\["([^"]*)","[^"]*",)(\["[^"\]]*"(?:,"[^"\]]*")+\])', ar, s)
    # renderers: one tag only
    for v in ("r", "c"):
        old = '.innerHTML="<i>"+%s[2][0]+"</i><i>"+%s[2][1]+"</i>"' % (v, v)
        if old in s:
            s = s.replace(old, '.innerHTML="<i>"+%s[2][0]+"</i>"' % v); n += 1
    return s, n

for f in sys.argv[1:] or FILES:
    p = f if os.path.isabs(f) else os.path.join(ROOT, f)
    if not os.path.exists(p): print("skip", f); continue
    s = open(p, encoding="utf-8").read()
    s2, n = fix(s)
    if s2 != s: open(p, "w", encoding="utf-8").write(s2)
    print(f, n, "changes")
