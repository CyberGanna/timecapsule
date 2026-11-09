# Content for "Fedor's journey": an A.A. member whose weekly Zoom meeting moves to TimeCapsule.
# Built by: python3 build.py fedor ; node print.js fedor
# Revised 2026-11-09 after Karim's corrections (order of steps, standing table, open the room, real details allowed, etc.)
META = dict(name='Fedor’s journey', file='journey-fedor.html',
    cover_q='Fedor’s A.A. group has met on Zoom every Tuesday for years. Now it moves to TimeCapsule. This is how the meeting works there, and what the group needs from the place.',
    meet='Meet Fedor', meet_h1='A weekly meeting, <b>a new room</b>',
    meet_lead='Fedor is a member of Alcoholics Anonymous. For four years his home group has met on Zoom every Tuesday at 19:00. Anna, the group’s secretary, is moving it to TimeCapsule.',
    meet_p='For Fedor, nothing about the meeting should change except the room. TimeCapsule has to be a secure environment that keeps his privacy and the anonymity of the group, while leaving him free to be himself. This story follows the meeting step by step. Some screens are real pages of the prototype; the steps marked “to build” describe what the group needs and does not exist yet.')

NOTE = '<span class="note">%s</span>'
STEPS = [
 ("Set up", "Anna <b>sets up the group’s table</b>",
  "Anna wants a room that is always there. Before anyone can receive a link, she sets up the group’s table, once and for all.",
  ["She creates a Private table: it stays off the Tables page, and only people with the link can see it. She sets it to repeat every Tuesday at 19:00, with the same link and a password, so the group never has to ask for a new one. She turns off “Keep a transcript of the discussion” and leaves the camera optional. She can change any of these settings at any time.",
   "In the table format she also sets how shares work at this meeting: whether people share in turn or only when they want to. " + NOTE % "To build: a standing table with one fixed link and password, repeating daily or weekly, and the share-format field. Today a table is created one date at a time, with at most ten chairs."],
  [("f-create", "Create a table: Private, transcript off. The repeat, password and share-format options are not in the prototype yet.")], "Set up"),
 ("Link", "Fedor <b>receives the link</b>",
  "Fedor wants to keep going to his Tuesday meeting. Anna sends the group the link to the new room.",
  ["The link opens a private invite: “Fedor, it’s Anna. Same Tuesday group, same time, new room.” The page says that this is a private table, that it isn’t on the Tables page, and that only people with the link can see it. Then one line matters more than the rest: <b>Don’t share this link with anyone outside the A.A. community.</b>",
   "He cannot see who else is coming until he accepts. Nobody outside the group can find the table, search for it, or see that he has a chair. " + NOTE % "To build: the A.A. line as part of the invite text the secretary can set."],
  [("f-invite", "A private invite: off the Tables page, link only. Example content on a prototype screen.")], "The link"),
 ("Join", "Fedor <b>joins TimeCapsule</b>",
  "Fedor wants to be himself in a room that protects him. He creates his account in a minute.",
  ["TimeCapsule asks what people should call him at the table. He is free to give his real name and a photo if he wants; many members do. He can also give only a first name, or an alias. Whatever he chooses, the environment keeps it inside the group: nothing from a private table shows on his profile or anywhere else.",
   "He skips the topics, the book and the film, which are all optional."],
  [("f-name", "“What should we call you at the table?” Real name, first name or alias: his choice.")], "Join"),
 ("Privacy", "Fedor <b>closes the doors</b>",
  "Fedor wants to be sure no one stumbles on him. He opens Settings, Privacy.",
  ["He turns off “Let people find me”, so he is not listed on the People page. The page promises that tables he only joined, private tables and when he was last seen are never shown to anyone. He sets “Who can chat with me” to people he has sat with.",
   "If anyone ever bothers him, Blocked people and Report are one tap away."],
  [("f-settings", "Settings, Privacy: Let people find me, Show when I’m live, Who can chat with me.")], "Privacy"),
 ("Open", "Anna <b>opens the room</b>",
  "Anna wants the meeting to start the way it always has. At 18:55 she opens the room and makes the announcement.",
  ["Until the secretary opens the room, nobody can enter it: the link shows “The room opens at 19:00” and nothing more. When Anna opens it, members come in and she makes the opening announcement, as on Zoom.",
   "Fedor is reminded before the meeting the way he prefers: an email, a notification from the TimeCapsule app, or a message on WhatsApp or by SMS. " + NOTE % "To build: the room that stays closed until the host opens it, and reminders by app notification, WhatsApp or SMS. Today there is only an email one hour before."],
  [("f-mytables", "My tables: the Tuesday meeting at the top. “Join now” appears once the room is open.")], "Open the room"),
 ("Enter", "Fedor <b>joins the meeting</b>",
  "Fedor wants to be in his seat when the first share begins. He taps “Join now”.",
  ["A short check opens: camera, microphone and background blur. Under “Show me at the table as” he keeps the name he chose. He can leave the camera off and still take part. He enters the password Anna gave the group, and he is in.",
   NOTE % "To build: the table password."],
  [("f-camera", "“Ready to join?” Name or alias, camera optional.")], "Join the meeting"),
 ("Listen", "Fedor <b>listens to the shares</b>",
  "Fedor wants to hear the others first. He sits with the group as on any Tuesday.",
  ["Anna gives the turns. The screen shows the person who is speaking large, and the rest of the participants in a row beside it, so Fedor sees both the speaker and the group. The host can mute anyone, so no one is interrupted. People shows who is at the table, and Messages lets him write privately to Anna.",
   "Nothing is kept. No transcript is saved, no recording is made, and his Notes, if he writes any, are visible only to him. " + NOTE % "To build: a speaker view with the group beside it (today the Live Table shows equal tiles), and a switch that turns the live transcript off completely for such tables."],
  [("f-live", "The Live Table, People tab. Example names on a prototype screen.")], "The meeting"),
 ("Share", "Fedor <b>shares</b>",
  "Fedor wants to speak when it is his turn. He raises his hand, or waits to be called.",
  ["Whether shares are in turn or voluntary was set by Anna in the table format, and she says it in the announcement, so everyone knows the rule before the first share. When it is his turn, Fedor shares. Nobody writes it down.",
   "After the last share, Anna closes the meeting."],
  [], "Share"),
 ("Leave", "Fedor <b>can leave quietly, anytime</b>",
  "Fedor wants to be free to go. He can leave the meeting at any moment, without a word.",
  ["“Leave table” takes him out quietly. There is no “How was the discussion?”, no TimeCoins to award, no rating: for this table the group has turned all of that off. " + NOTE % "To build: turning off Rate and tip and TimeCoins per table. Today Fedor would tap Skip.",
   "Next Tuesday the same link, the same password, the same faces, the same time."],
  [], "Leave"),
 ("Group", "The group <b>has a home</b>",
  "Fedor wants to reach a member between meetings. The group has its own page, open only to its members.",
  ["Like a group on a social network, the table has an entity of its own: who the members are, when it meets, the announcement text, and the contacts of the members who are willing to help others, shared only inside the group. Fedor finds a number he can call on a hard evening.",
   NOTE % "To build: a group page for a standing table, visible only to participants, with an opt-in member contact list."],
  [], "The group"),
]

G_HAVE = [
 ("Private tables", "off the Tables page, link only, “don’t forward it”, guests’ faces hidden until you accept."),
 ("Your name, your choice", "real name and photo, first name only, or an alias; with an alias only the host knows who you are."),
 ("Privacy settings", "Let people find me off; tables you joined and private tables never shown to anyone."),
 ("Transcript off", "“Keep a transcript of the discussion” can be turned off for each table."),
 ("Calm tools", "camera optional, background blur, host can mute anyone, Block and Report, Leave table."),
]
G_NEED = [
 ("A standing table", "set up once and for all: repeats every day or week, same link and password, settings changeable anytime. Today a table is one date at a time."),
 ("The room opens by the host", "nobody can enter before the secretary opens it; then the announcement."),
 ("Share format", "a field in the table format: shares in turn or voluntary."),
 ("Speaker view", "video with the speaker large and the participants beside it."),
 ("A group page", "an entity like a social-network group, visible only to participants, with the opt-in contacts of members willing to help."),
 ("Reminders", "by TimeCapsule app notification, WhatsApp or SMS, not only email."),
 ("Never on the globe", "private tables must never appear on the World globe or be open to Listen in. Today every table on the globe can be listened to."),
 ("No live transcript", "a switch that turns off speech-to-text and AI tools completely, not only the saved transcript."),
 ("No rating, no tips", "turn off Rate and tip and TimeCoins for a table."),
 ("More chairs", "many meetings have 15 to 40 people; today the limit is ten chairs."),
 ("Co-hosts", "so the meeting runs when the secretary is away."),
 ("Privacy review", "attending such a meeting reveals health information, a special category of data under GDPR and Swiss law. It needs its own legal check before a pilot."),
]
def _li(xs, cls=''):
    return ''.join('<li%s><b>%s.</b> %s</li>' % (cls, a, b) for a, b in xs)
EXTRA = [
 ("What groups like Fedor’s need", "What A.A. groups <b>need from TimeCapsule</b>",
  '<p class="lead">Part of Fedor’s Tuesday already works with what TimeCapsule has. To be a safe home for a group week after week, the rest has to be built.</p>'
  '<div class="key"><span><i></i>Already in the prototype</span><span><i class="no"></i>To build</span></div>'
  '<ul class="gaps">' + _li(G_HAVE) + _li(G_NEED, ' class="no"') + '</ul>',
  "What groups need"),
]
