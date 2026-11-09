# Content for "Fedor's journey": an A.A. member whose weekly Zoom meeting moves to TimeCapsule.
# Built by: python3 build.py fedor ; node print.js fedor
META = dict(name='Fedor’s journey', file='journey-fedor.html',
    cover_q='Fedor’s A.A. group has met on Zoom every Tuesday for years. Now it moves to TimeCapsule. This is his first evening there, and what the group needs from the place.',
    meet='Meet Fedor', meet_h1='A weekly meeting, <b>a new room</b>',
    meet_lead='Fedor is a member of Alcoholics Anonymous. For four years his home group has met on Zoom every Tuesday at 19:00. Anna, the group’s secretary, is moving it to TimeCapsule.',
    meet_p='For Fedor, nothing about the meeting should change except the room. Anonymity comes first: first names only, nothing recorded, nothing visible from outside. This story follows his first Tuesday, step by step, on the real pages of the prototype, and ends with what TimeCapsule still needs for groups like his.')

STEPS = [
 ("Invite", "Fedor <b>gets the link</b>",
  "Fedor wants to keep going to his Tuesday meeting. Anna sends the group a link to the new room.",
  ["The link opens a private invite: “Fedor, it’s Anna. Same Tuesday group, same time, new room.” The page says it plainly: this is a private table, it isn’t on the Tables page, and only people with the link can see it. Please don’t forward it.",
   "He can’t see who else is coming until he accepts. Nobody outside the group can find the table, search for it or see that he has a chair."],
  [("f-invite", "A private invite: off the Tables page, link only. Example content on a prototype screen.")], "Private invite"),
 ("Join", "Fedor <b>joins with his first name</b>",
  "Fedor wants an account that says nothing about him. He creates one in a minute.",
  ["He writes “Fedor” and nothing else: no surname, no photo. The screen says it is the only name people see. He skips the topics, the book and the film, which are all optional.",
   "He could also use an alias. At a table, only the host would know it was him."],
  [("f-name", "“What should we call you at the table?” First name or alias.")], "Join"),
 ("Privacy", "Fedor <b>closes the doors</b>",
  "Fedor wants to be sure no one stumbles on him. He opens Settings, Privacy.",
  ["He turns off “Let people find me”, so he is not listed on the People page. The page promises that tables he only joined, private tables and when he was last seen are never shown to anyone. He sets “Who can chat with me” to people he has sat with.",
   "If anyone ever bothers him, Blocked people and Report are one tap away."],
  [("f-settings", "Settings, Privacy: Let people find me, Show when I’m live, Who can chat with me.")], "Privacy"),
 ("Set up", "Anna <b>sets up the room</b>",
  "Anna wants the meeting to be private and leave no trace. She creates the table once.",
  ["She chooses Private (only people invited with the link can join, and it stays off the Tables page), Tuesday at 19:00, English, and turns off “Keep a transcript of the discussion”. She hosts under her own first name.",
   "Each week, “Host again” prepares next Tuesday’s table for her. <span class=\"note\">Today a table has at most ten chairs, fewer than many meetings need.</span>"],
  [("f-create", "Create a table: Private, transcript off.")], "Set up"),
 ("Arrive", "Fedor <b>arrives on time</b>",
  "Fedor wants to be there when the meeting opens. An email reminds him an hour before.",
  ["At 18:55 he opens My tables. The Tuesday meeting is at the top with “Join now”. The tables he joins are listed here for him alone, never on his profile.",
   "A short check opens: camera, microphone and background blur. Under “Show me at the table as” he keeps “Fedor”. He can leave his camera off and still take part."],
  [("f-mytables", "My tables: the Tuesday meeting, Join now."), ("f-camera", "“Ready to join?” Name or alias, camera optional.")], "Arrive"),
 ("Share", "Fedor <b>shares</b>",
  "Fedor wants to listen, and to speak when he is ready. He sits with the group as on any Tuesday.",
  ["Anna opens the meeting and gives the turns, as she did on Zoom. Fedor raises his hand when he wants to share and waits for his turn. The host can mute anyone, so no one is interrupted. People shows who is at the table, and Messages lets him write privately to Anna.",
   "Nothing is kept. No transcript is saved, no recording is made, and his Notes, if he writes any, are visible only to him. <span class=\"note\">For groups like this the live transcript panel should be off too (see the last page).</span>"],
  [("f-live", "The Live Table, People tab. Example names on a prototype screen.")], "The meeting"),
 ("After", "Fedor <b>leaves quietly</b>",
  "Fedor wants the evening to end the way it always has. Anna closes the meeting and ends the table.",
  ["On other tables, a “How was the discussion?” window and TimeCoins to award would appear now. Fedor taps Skip. For a recovery meeting there should be nothing to rate and no coins to give: the group can turn this off.",
   "Next Tuesday the same link, the same faces, the same time. Over the weeks, the room stops feeling new."],
  [], "After the meeting"),
]

G_HAVE = [
 ("Private tables", "off the Tables page, link only, “don’t forward it”, guests’ faces hidden until you accept."),
 ("First name or alias", "no surname, no photo needed; with an alias only the host knows who you are."),
 ("Privacy settings", "Let people find me off; tables you joined and private tables never shown to anyone."),
 ("Transcript off", "“Keep a transcript of the discussion” can be turned off for each table."),
 ("Calm tools", "camera optional, background blur, host can mute anyone, Block and Report."),
]
G_NEED = [
 ("Never on the globe", "private tables must never appear on the World globe or be open to Listen in. Today every table on the globe can be listened to."),
 ("No live transcript", "a table setting that switches off speech-to-text and AI tools completely, not only the saved transcript."),
 ("No rating, no tips", "turn off Rate and tip and TimeCoins for a table."),
 ("A standing weekly table", "one fixed link that stays the same every week, instead of “Host again” by hand."),
 ("More chairs", "many meetings have 15 to 40 people; today the limit is ten chairs."),
 ("Co-hosts", "so the meeting runs when the secretary is away, and someone can admit people from a waiting room."),
 ("A “sensitive table” mark", "aliases and camera off by default, as in the aliases proposal."),
 ("Privacy review", "attending such a meeting reveals health information, a special category of data under GDPR and the Swiss data protection law. It needs its own legal check before a pilot."),
]
def _li(xs, cls=''):
    return ''.join('<li%s><b>%s.</b> %s</li>' % (cls, a, b) for a, b in xs)
EXTRA = [
 ("What groups like Fedor’s need", "What A.A. groups <b>need from TimeCapsule</b>",
  '<p class="lead">Fedor’s first Tuesday works with what TimeCapsule already has. To be a safe home for anonymous groups week after week, a few things are missing.</p>'
  '<div class="key"><span><i></i>Already in the prototype</span><span><i class="no"></i>Still needed, to decide</span></div>'
  '<ul class="gaps">' + _li(G_HAVE) + _li(G_NEED, ' class="no"') + '</ul>',
  "What groups need"),
]
