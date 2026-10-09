import html
H="font-family:'Marcellus', serif; color:#A85639; font-weight:normal;"
B="font-family:'Merriweather', serif; font-size:11pt; line-height:1.5; color:#2B2420;"
def h2(t): return f'<h2 style="{H} font-size:18pt; margin-top:22pt;">{t}</h2>'
def p(t,extra=""): return f'<p style="{B}{extra}">{t}</p>'
def hr(): return '<hr style="border:none; border-top:1px solid #D8CFC2;">'
def q(n,question,note):
    return (f'<p style="{B} margin-bottom:2pt;"><b>{n}. {question}</b></p>'
            f'<p style="font-family:\'Merriweather\', serif; font-size:10.5pt; line-height:1.5; font-style:italic; color:#5A5048; padding-left:16pt; border-left:2px solid #1F7A85; margin-top:0;">{note}</p>')
qs=[
("The warm-up",[
 ("What did you want for Christmas when you were eight, and did you get it?","Why this works: it has a date on it, a toy, and a parent. Listen for the shop, the wrapping, who was in the room."),
 ("When did you stop believing in Father Christmas? Who told you, or did you work it out yourself?","Why this works: everyone has an answer, and it's usually funny. It gets the table laughing before the deeper ones."),
 ("What did Christmas dinner look like at your house growing up? Who cooked, and where did everyone sit?","What to listen for: the small logistics. A table pushed against a wall, a fold-up chair, the aunt who took over the kitchen."),
]),
("The middle",[
 ("What was Christmas like for you when you were the one making it happen?","Why this works: we only ever see Christmas from our side of the front door. This shows us theirs. The first answer is usually the practical one."),
 ("What's the best present you remember, given or received?","What to listen for: the story behind it. The present is rarely the point."),
 ("Was there a Christmas that went wrong? What did you end up laughing about afterwards?","Why this works: disasters become the stories a family repeats for forty years. Someone will finish their sentence for them."),
 ("Who was always at the table when you were young, and what were they like?","What to listen for: names you don't know. Ask about one of them before you move on."),
 ("Which Christmas tradition would you most like us to keep going, and where did it start?","Why this works: traditions usually began with one person and one odd decision. This finds out who, and it hands the family a job."),
]),
("The door to the room you've never walked into",[
 ("What did your parents do at Christmas that you swore you'd never do? Or always would?","Why this works: it's a question about them as a child and as a parent at once. Go gently, and let them answer at their own speed."),
 ("Which Christmas would you relive, if you could?","What to listen for: whether they pick a big one or a small one. It's usually a small one."),
]),
("The close",[
 ("What's a Christmas memory that still makes you laugh?","Why this works: it ends the conversation somewhere warm, and the best stories tend to arrive here, once everyone's relaxed."),
 ("When we look back on these Christmases in twenty years, what do you hope we remember?","What to listen for: the answer is often about how they want to be remembered as a person. Just listen. You don't have to say anything back."),
]),
]
out=['<html><head><meta charset="utf-8"></head><body style="font-family:\'Merriweather\', serif; color:#2B2420;">']
out.append(f'<h1 style="{H} font-size:28pt; margin-bottom:4pt;">After the Pudding</h1>')
out.append(p("12 questions for the Christmas table","font-style:italic; color:#5A5048; font-size:12pt;"))
out.append(p('Neil Taylor<br>Founder | Me &amp; My Old Man<br><a href="https://www.meandmyoldman.co.uk" style="color:#1F7A85;">www.meandmyoldman.co.uk</a>'))
out.append(hr())
out.append(p("Christmas is the one week the whole family ends up in the same room, with time on its hands and a parent who's a bit more relaxed than usual. It's also loud, and there's a lot of washing up."))
out.append(p("These are 12 questions you can actually ask in the middle of that. Short enough to say out loud. Warm enough that nobody feels interviewed."))
out.append(p("You don't need all twelve. One is plenty."))
out.append(h2("How to use them"))
out.append('<ul style="font-family:\'Merriweather\', serif; font-size:11pt; line-height:1.6; color:#2B2420;">'
 '<li><b>Pick one, then stop talking.</b> Count to ten if you have to.</li>'
 '<li><b>Wait for the second answer.</b> The first is usually the practical one. The second one is the real one.</li>'
 '<li><b>Ask side by side.</b> Washing up, a walk, a lift home. It\'s easier than face to face.</li>'
 '<li><b>Press record before you ask.</b> Put your phone on the table. Ask permission first, and most people say yes.</li>'
 '</ul>')
out.append(hr())
n=1
for title,items in qs:
    out.append(h2(title))
    for question,note in items:
        out.append(q(n,question,note)); n+=1
out.append(hr())
out.append(h2("Before you go"))
out.append(p("These aren't an interview. They're invitations. The point isn't to get through the list, it's to find out one thing about someone you love that you didn't know before."))
out.append(p("If something comes up, hit reply and tell me what they said. I read every one."))
out.append(p("And if you'd like more questions like these, I send one story and one thing to try every Friday. You're on the list now."))
out.append(hr())
out.append(h2("About Me &amp; My Old Man"))
out.append(p("I'm Neil. I record parents' life stories and turn them into audio documentaries, in their own voice, after first sitting down with their children to find out what everyone wants to know. I've spent 390+ hours in conversations like these, with 38 families across 11 countries. The best stories are almost never the ones people expected to tell."))
out.append('</body></html>')
open('christmas-questions-after-the-pudding_v1.html','w').write("\n".join(out))
