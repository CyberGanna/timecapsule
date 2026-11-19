# Public conversations hosted by other people (sample content stays English).
# Used by the public Conversations page and the saved-discussion page, never by Gregory's profile or My universe.
PUB_COL = {"Home":"#7FF0F2","Energy":"#7CC8FF","Philosophy":"#F4A6D7","Science":"#8BE38B","History":"#E8B577","Music":"#9FA8FF","Climate":"#4FD1A5","Art":"#FF6F91","Design":"#FFB35C"}
# id, host, topic, subtopic, title, rounds [(date, people)], voices left out (last round), "trusted" host
PUB = [
 ("listening","Amara","Music","Listening","Why do sad songs make us feel better?",[("Tue 27 Oct",5),("Mon 16 Nov",6)],0,True),
 ("octopus","Yuki","Science","Minds","Does an octopus have a self?",[("Sun 15 Nov",5)],0,True),
 ("grandparents","Kofi","History","Memory","What our grandparents never told us",[("Thu 12 Nov",7)],1,True),
 ("heat","Lena","Climate","Cities","Living with hotter summers",[("Wed 11 Nov",6)],0,False),
 ("museums","Mia","Art","Museums","Should museums give things back?",[("Mon 2 Nov",5),("Mon 9 Nov",6)],0,True),
 ("silence","Omar","Music","Silence","Is silence a kind of music?",[("Sat 7 Nov",4)],0,False),
 ("chairs","Sofia","Design","Objects","The chair you'd save from a fire",[("Thu 5 Nov",5)],0,False),
 ("stars","Nikos","Science","Space","Would you go to Mars and not come back?",[("Tue 3 Nov",6)],0,True),
 ("letters","Mia","History","Letters","Letters we would write by hand again",[("Fri 30 Oct",4)],0,True),
 ("forest","Kofi","Climate","Forests","What a forest knows that we don't",[("Wed 28 Oct",5)],0,True),
 # past tables from My tables (Gabriele was there), Karim 2026-11-18
 ("where-home","Yuki","Home","Belonging","Where is home?",[("Tue 17 Nov",6)],0,True),
 ("happiness-skill","Gabriele","Philosophy","Happiness","Is happiness a skill?",[("Mon 16 Nov",8)],0,False),
 ("green-nuclear","Lena","Energy","Nuclear","Green technology versus nuclear",[("Sat 14 Nov",5)],0,False),
]

TXP = {
"listening": [
 dict(names=["Amara","Omar","Lena","Jonas","Maya"], notes=["Sad songs give a shape to feelings we can't name."], open=["Is it the song or the company that comforts?"], tx=[
  ("0:02","Amara","Think of the saddest song you love. Why do you go back to it?"),
  ("0:06","Omar","Because it already knows how I feel. I don't have to explain."),
  ("0:11","Lena","It's like being sad next to someone, not alone."),
  ("0:15","Jonas","A sad song is a room where sadness is allowed.")]),
 dict(names=["Amara","Omar","Lena","Jonas","Maya","Ines"], notes=["Ines brought fado: saudade as a feeling you can share.","Everyone named one song; the playlist is in the notes."], open=["Why do we listen alone to songs about other people?"], tx=[
  ("0:01","Amara","Last time Jonas called a sad song a room. Who wants to go in first?"),
  ("0:04","Ines","In Lisbon we have fado. You don't listen to it, you sit inside it."),
  ("0:09","Maya","Maybe we don't want to be cheered up. We want to be accompanied."),
  ("0:14","Omar","That's the difference between advice and music.")])],
"octopus": [dict(names=["Yuki","Nikos","Tom","Maya","Elena"], notes=["Two thirds of an octopus's neurons are in its arms."], open=["Can a self be spread out instead of in one place?"], tx=[
  ("0:02","Yuki","Each arm of an octopus can taste and decide on its own. So who is in charge?"),
  ("0:06","Tom","Maybe nobody. Maybe 'in charge' is our human idea."),
  ("0:11","Elena","My hands sometimes know a piano piece my head forgot."),
  ("0:15","Nikos","Then we're a bit octopus too.")])],
"grandparents": [dict(names=["Kofi","Ana","Marco","Ines","Lea","Jonas","Sofia"], out=1, notes=["Silence was often protection, not secrecy."], open=["Do we owe our children the stories we were never told?"], tx=[
  ("0:02","Kofi","My grandfather never spoke about the war. I learned everything from a box of letters."),
  ("0:07","Ana","Mine spoke about it every Sunday. Maybe that was his way of staying quiet."),
  ("0:11",None,"2 min"),
  ("0:14","Marco","Not telling can be a gift. They wanted us to start clean."),
  ("0:19","Lea","But then we inherit the silence instead of the story.")])],
"heat": [dict(names=["Lena","Tom","Ines","Marco","Elena","Lea"], notes=["Shade, water and old stone: the old towns knew."], open=["Who gets shade in a city, and who decides?"], tx=[
  ("0:02","Lena","Last August my flat hit 34 degrees at night. How are you all coping?"),
  ("0:06","Ines","In Seville we close everything at noon and live at night. It's not lazy, it's clever."),
  ("0:11","Tom","Trees are the cheapest air conditioning ever invented."),
  ("0:15","Elena","And the only one that makes the street nicer too.")])],
"museums": [
 dict(names=["Mia","Kofi","Sofia","Marco","Ana"], notes=["Context changes what an object means."], open=["Who does an object belong to after two hundred years?"], tx=[
  ("0:02","Mia","If something was taken, does time make it yours?"),
  ("0:06","Kofi","Time makes it familiar. That's not the same as yours."),
  ("0:10","Sofia","Some objects are safer where they are. Is that an argument or an excuse?")]),
 dict(names=["Mia","Kofi","Sofia","Marco","Ana","Yuki"], notes=["Yuki: in Japan some objects are kept by families and shown once a year."], open=["Could museums borrow instead of own?"], tx=[
  ("0:01","Mia","Round two. Kofi, you said familiar isn't the same as yours."),
  ("0:05","Yuki","What if a museum were a guest of the object, not its owner?"),
  ("0:10","Marco","Then the label would tell you whose home it misses."),
  ("0:14","Kofi","That label would change everything.")])],
"silence": [dict(names=["Omar","Amara","Elena","Jonas"], notes=["Cage's 4'33\": the room becomes the music."], open=["Is a pause part of a song or a break from it?"], tx=[
  ("0:02","Omar","In Cage's piece the pianist plays nothing for four minutes. Is that music?"),
  ("0:06","Elena","It's the audience who plays. Coughs, chairs, rain."),
  ("0:10","Amara","The best musicians I know are the ones who leave space."),
  ("0:14","Jonas","Like the best people at a table.")])],
"chairs": [dict(names=["Sofia","Lea","Tom","Maya","Nikos"], notes=["Nobody picked the most expensive thing they own."], open=["Why do worn things feel more ours?"], tx=[
  ("0:02","Sofia","Your house is on fire and you can save one object. Which one?"),
  ("0:06","Maya","My grandmother's chair. The seat has her shape in it."),
  ("0:10","Nikos","A cheap radio. It was on every night of my childhood."),
  ("0:14","Lea","Things become precious by being used, not by being bought.")])],
"stars": [dict(names=["Nikos","Yuki","Tom","Ana","Jonas","Maya"], notes=["Most said no, then changed their mind when we spoke about the view."], open=["What would you miss first?"], tx=[
  ("0:02","Nikos","One-way ticket to Mars. Who goes?"),
  ("0:05","Tom","Not me. I'd miss rain."),
  ("0:09","Yuki","I'd go. Someone has to be the first person to look back at Earth from there."),
  ("0:14","Ana","Maybe we'd finally see how small our arguments are.")])],
"letters": [dict(names=["Mia","Elena","Sofia","Marco"], notes=["Handwriting is slower, and the slowness is the message."], open=["Who would you write to this week?"], tx=[
  ("0:02","Mia","When did you last write a letter by hand?"),
  ("0:06","Elena","To my son when he left home. I couldn't say it out loud."),
  ("0:11","Marco","A letter can't be edited. That's why we trust it."),
  ("0:15","Sofia","And you can keep it in a drawer for fifty years.")])],
"forest": [dict(names=["Kofi","Lena","Lea","Tom","Ines"], notes=["Trees share sugar through fungi with weaker neighbours."], open=["Could a city work like a forest?"], tx=[
  ("0:02","Kofi","Old trees feed young ones through their roots. What does that teach us?"),
  ("0:07","Lea","That strength is something you pass on, not something you keep."),
  ("0:11","Tom","A forest has no CEO and it's been fine for millions of years."),
  ("0:16","Lena","It's slow. Maybe that's the secret.")])],
"where-home": [dict(names=["Yuki","Lena","Gabriele","Omar","Ana","Jonas"], notes=["Home can be a person, a smell, a kitchen."], open=["Can you be homesick for a place you never lived?"], my=["Home might be a person, not a place. (Lena)","Ask Yuki for the name of the tea house in Kyoto.","Keep: 'You can be homesick for a place you never lived.'"], tx=[
  ("0:02","Yuki","Where is home for you tonight? Not the address, the feeling."),
  ("0:06","Lena","For me home might be a person, not a place."),
  ("0:10","Omar","I grew up in three cities. I feel at home in the kitchen of each one."),
  ("0:14","Gabriele","You can be homesick for a place you never lived."),
  ("0:18","Ana","That is exactly how I feel about my grandmother's village.")])],
"happiness-skill": [dict(names=["Gabriele","Mia","Kofi","Elif","Omar","Yuki","Amara","Gregory"], notes=["Gratitude helps, until it turns into comparing."], open=["Is noticing the real skill, more than being happy?"], my=["Next time open with the 'two lists' exercise.","Kofi's point about gratitude and envy: follow up."], tx=[
  ("0:01","Gabriele","Tonight's question: is happiness a skill we can practise?"),
  ("0:05","Mia","I think it is more like a garden than a skill."),
  ("0:09","Kofi","Gratitude helps, but it can turn into comparing. Then envy comes back."),
  ("0:13","Elif","Maybe the skill is noticing, not being happy."),
  ("0:17","Gregory","We don't practise happiness. We practise attention, and happiness visits.")])],
"green-nuclear": [dict(names=["Lena","Kofi","David","Ana","Gabriele"], notes=["Storage is the bottleneck, not generation."], open=["Is nuclear a bridge or a detour?"], my=["Look up the Finnish storage project David mentioned."], tx=[
  ("0:02","Lena","Bring one fact that surprised you. Who starts?"),
  ("0:06","David","Finland stores energy in sand. Hot sand, for months."),
  ("0:10","Kofi","In Ghana the sun is free, but the batteries are not."),
  ("0:14","Gabriele","So the real question is storage, not solar versus nuclear."),
  ("0:18","Ana","And who pays for it while we wait.")])]
}
