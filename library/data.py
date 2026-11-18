# Sample library of Gregory's tables (sample content stays English).
TOPIC_COL = {"Philosophy":"#F4A6D7","Religion":"#C9A7FF","Energy":"#7CC8FF","Travel":"#E9F27A","Home":"#7FF0F2","Craft":"#FF9E8A"}
# id, topic, subtopic, title, rounds [(date, people)], private, voices left out (last round)
R = [
 ("free-will","Philosophy","Free will","Is free will an illusion?",[("Tue 22 Sep",5),("Tue 3 Nov",6),("Tue 17 Nov",6)],False,1),
 ("phenomenology","Philosophy","Phenomenology","Phenomenology vs. God",[("Tue 13 Oct",4),("Tue 27 Oct",4)],False,0),
 ("repair-ethics","Philosophy","Ethics","The ethics of repair",[("Tue 8 Sep",5)],False,0),
 ("faith","Religion","Faith","Is faith a choice?",[("Tue 22 Sep",6)],False,1),
 ("candles","Religion","Ritual","Why we still light candles",[("Tue 1 Sep",4)],True,0),
 ("wind","Energy","Wind","Wind and the future of energy",[("Tue 20 Oct",6)],False,0),
 ("nuclear","Energy","Nuclear","Is nuclear the bridge?",[("Tue 25 Aug",5)],False,0),
 ("road-trips","Travel","Road trips","Road trips that changed us",[("Tue 6 Oct",7)],False,0),
 ("trains","Travel","Slow travel","Trains instead of planes",[("Tue 18 Aug",4)],False,0),
 ("homes","Home","Belonging","Homes that hold us",[("Tue 15 Sep",5)],False,0),
 ("room-home","Home","Belonging","What makes a room feel like home",[("Tue 29 Sep",4)],False,0),
 ("fix-it","Craft","Repair","Fix it yourself",[("Tue 13 Oct",5)],False,0),
]

# Transcripts: (time, speaker or None for left-out, text or duration)
TX = {
"free-will": [
 dict(names=["Gregory","Lena","Tom","Ana","Nikos"], notes=["We agreed to start from experience, not from physics.","Lena: the feeling of choosing is real even if the choice is not."], open=["Can you be responsible for a choice you didn't make freely?"], tx=[
  ("0:02","Gregory","Let's start from the inside. When did you last feel you really chose something?"),
  ("0:05","Lena","Leaving my job. It felt like jumping, not like calculating."),
  ("0:09","Tom","But the jump had causes. Ten years of being tired of it."),
  ("0:14","Nikos","Causes aren't chains, though. They're more like weather."),
  ("0:21","Gregory","Let's keep that image for next time: weather, not chains.")]),
 dict(names=["Gregory","Lena","Tom","Ana","Maya","Jonas"], notes=["Weather, not chains: everyone kept coming back to it.","Maya brought Frankfurt's cases; worth reading before round 3."], open=["Is luck the enemy of free will, or its condition?"], tx=[
  ("0:01","Gregory","Last time we ended with weather, not chains. Did anyone change their mind?"),
  ("0:04","Maya","I read Frankfurt. You can be responsible even if you couldn't have done otherwise."),
  ("0:10","Ana","That scares me a bit. It means excuses don't work."),
  ("0:16","Jonas","Or it means we stop looking for excuses and start owning things."),
  ("0:23","Tom","Then where does luck go? I was lucky to have parents who read.")]),
 dict(names=["Gregory","Gabriele","Lena","Tom","Ana"], out=1, notes=["Freedom may be less about choosing and more about owning what we chose.","Nobody defended full determinism once we spoke about our own children."], open=["Is luck the enemy of free will, or its condition?","Would we raise children differently if we were sure free will is an illusion?"], my=["Look up Frankfurt's cases before next round.","Gregory's point about owning a choice: ask him for the source."], tx=[
  ("0:01","Gregory","Two rounds in, and luck is still on the table. Tom, you raised it."),
  ("0:03","Tom","My parents read to me every night. I didn't choose that, and it shaped every choice after."),
  ("0:07","Gabriele","Maybe freedom isn't the starting point. Maybe it's something you grow into, like a language."),
  ("0:10",None,"1 min"),
  ("0:12","Lena","I like that. Nobody is born speaking, but at some point you say things nobody taught you."),
  ("0:17","Ana","When I think about my daughter, I can't believe she isn't free. Even if the theory says so."),
  ("0:22","Gregory","Then maybe freedom is less about choosing and more about owning what we chose."),
  ("0:26","Gabriele","Owning it, and letting other people hold you to it. That's why we talk about it here.")]),
],
"phenomenology": [
 dict(names=["Gregory","Sofia","Marco","Ines"], notes=["Husserl's 'back to the things themselves' as a way into prayer."], open=["Is the experience of the sacred a perception or an interpretation?"], tx=[
  ("0:02","Gregory","Phenomenology asks us to describe before we explain. Can we do that with faith?"),
  ("0:06","Sofia","When I pray I don't feel anyone listening. I feel myself listening."),
  ("0:11","Marco","That's already a description. No God in it, but no absence either.")]),
 dict(names=["Gregory","Sofia","Marco","Ana"], notes=["Marion: the gift that gives itself without a giver."], open=["Can a gift exist without a giver?"], tx=[
  ("0:01","Gregory","Last time Sofia said she feels herself listening. Let's start there."),
  ("0:05","Ana","For me it's like music. I don't need to know who wrote it to be moved."),
  ("0:09","Gabriele","But you'd want to thank someone, wouldn't you?"),
  ("0:12","Sofia","Thanking might be the most honest prayer there is.")]),
],
"repair-ethics": [dict(names=["Gregory","Elena","Tom","Nikos","Lea"], notes=["Repair as care for things, and for the people who made them."], open=["Do we owe anything to objects?"], tx=[
  ("0:02","Gregory","Is repairing a moral act, or just a thrifty one?"),
  ("0:06","Elena","My grandmother darned socks. It was love, not money."),
  ("0:10","Nikos","Throwing away is easy because we don't see where things go."),
  ("0:14","Gabriele","Repair makes you look at the thing long enough to respect it.")])],
"faith": [dict(names=["Gregory","Marco","Sofia","Ines","Jonas"], out=1, notes=["Faith as a practice rather than a belief."], open=["Can you decide to believe?"], tx=[
  ("0:01","Gregory","Pascal said act as if you believe and belief will come. Does it work?"),
  ("0:05","Marco","It worked for running. I hated it until I didn't."),
  ("0:09",None,"2 min"),
  ("0:12","Ines","Maybe faith is less a choice than a habit of attention."),
  ("0:16","Gabriele","Then we choose where to look, and the rest follows.")])],
"candles": [dict(names=["Gregory","Ana","Elena","Maya"], notes=["Ritual marks time when nothing else does."], open=["What rituals have we lost without noticing?"], tx=[
  ("0:02","Gregory","Why do we still light candles, even without believing?"),
  ("0:06","Elena","Because the dark is still there."),
  ("0:09","Gabriele","And lighting one is a way of saying: I'm still here too.")])],
"wind": [dict(names=["Gregory","Lea","Tom","Jonas","Nikos","Maya"], notes=["Turbines look different when the village owns them."], open=["Who should own the wind?"], tx=[
  ("0:02","Gregory","Wind is free, turbines are not. Who should own them?"),
  ("0:06","Lea","In my village the cooperative owns two. Nobody complains about the view any more."),
  ("0:11","Jonas","Ownership changes how things look. Literally."),
  ("0:15","Gabriele","Then the energy question is really a question about belonging.")])],
"nuclear": [dict(names=["Gregory","Tom","Ines","Marco","Sofia"], notes=["Fear and numbers rarely meet in the same room."], open=["How do we decide about risks we can't feel?"], tx=[
  ("0:01","Gregory","Is nuclear a bridge or a trap?"),
  ("0:05","Tom","The numbers say bridge. My stomach says trap."),
  ("0:09","Gabriele","Maybe the stomach is answering a different question: who do we trust?")])],
"road-trips": [dict(names=["Gregory","Ines","Tom","Lena","Maya","Jonas","Elena"], notes=["The best trips had no plan for the second half."], open=["Can you travel like that at home?"], tx=[
  ("0:02","Gregory","Tell us about a road trip that changed you."),
  ("0:05","Ines","Lisbon to Seville with a broken radio. We had to talk."),
  ("0:09","Tom","Mine was a wrong turn in Scotland. Best day of the year."),
  ("0:13","Gabriele","Wrong turns are the only time we really look around.")])],
"trains": [dict(names=["Gregory","Lea","Marco","Sofia"], notes=["Slow travel gives the journey back its middle."], open=["Is slowness a privilege?"], tx=[
  ("0:02","Gregory","Trains instead of planes: sacrifice or gift?"),
  ("0:06","Lea","Gift. Twelve hours to Vienna and I finished a book."),
  ("0:10","Gabriele","On a plane you arrive. On a train you travel.")])],
"homes": [dict(names=["Gregory","Elena","Ana","Ines","Jonas"], notes=["Home is where your habits are known."], open=["Can a city be a home?"], tx=[
  ("0:02","Gregory","What makes a place hold you?"),
  ("0:06","Elena","The baker knows my order. That's home."),
  ("0:10","Gabriele","Being known without having to explain yourself.")])],
"room-home": [dict(names=["Gregory","Maya","Tom","Ana"], notes=["Light and one old object: everyone said the same two things."], open=["Why do new things feel like a hotel?"], tx=[
  ("0:02","Gregory","What makes a room feel like home?"),
  ("0:05","Maya","One thing that's older than me."),
  ("0:09","Gabriele","And light from the side, never from above.")])],
"fix-it": [dict(names=["Gregory","Nikos","Lea","Marco","Elena"], notes=["Swap list: Nikos fixes radios, Lea sews, Marco does bikes."], open=["Should we start a repair table every month?"], tx=[
  ("0:02","Gregory","What's the last thing you fixed yourself?"),
  ("0:05","Nikos","A radio from 1974. It still smells warm when it's on."),
  ("0:09","Gabriele","I fixed a chair badly. I still sit on it, proudly.")])],
}

# AI summary written after each round (editable by the host). Max ~6-7 lines.
SUM = {
"free-will": [
 "Gregory opened with experience rather than theory: when did you last feel you really chose something? Lena described leaving her job as a jump, not a calculation; Tom answered that the jump had ten years of causes. Nikos offered the image the table kept: causes are like weather, not chains.",
 "The table came back to weather, not chains. Maya brought Frankfurt's cases: you can be responsible even when you couldn't have done otherwise. Ana found that unsettling because excuses stop working; Jonas saw it as a reason to own our choices. Tom closed by asking where luck fits, which became the question for round 3.",
 "Round 3 took up luck. Tom said the most important things that shaped him, like his parents reading to him, were never chosen. Gabriele suggested freedom is something we grow into, like a language; Lena agreed that we end up saying things nobody taught us. Ana couldn't believe her daughter isn't free, whatever the theory says. Gregory summed up: freedom may be less about choosing and more about owning what we chose, and letting others hold us to it.",
],
"phenomenology": [
 "Gregory proposed describing faith before explaining it. Sofia said that when she prays she doesn't feel anyone listening, she feels herself listening. Marco noted that this description has no God in it, but no absence either. The table left open whether the sacred is perceived or interpreted.",
 "Starting from Sofia's 'listening', Ana compared faith to music that moves you without knowing who wrote it. Gabriele asked whether we wouldn't still want to thank someone, and Sofia answered that thanking might be the most honest prayer there is. Marion's idea of a gift without a giver stayed open.",
],
}
