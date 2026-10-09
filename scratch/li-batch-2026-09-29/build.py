import re, pathlib
T = pathlib.Path("../../skills/mmom-carousel/assets/template.html").read_text()
head = T.split("<body>")[0] + "<body>\n"
tail = "\n<script>" + T.split("<script>")[1]
extra = """<style>
 .q { font: italic 500 70px/1.2 "Lora", serif; max-width: 880px; }
 .q.small { font-size: 60px; }
 .by { font: 500 28px/1.4 "DM Sans", sans-serif; color: var(--body); margin-top: 48px; letter-spacing: .02em; }
 .slide.peach .by { color: var(--cream); }
 .slide.dark .by { color: var(--peach); }
 .slide.dark .q { color: var(--cream); }
 .slide.peach .foot .left { color: var(--cream); }
</style>
"""
head = head.replace("</head>", extra + "</head>")
M = '<div class="mark">Me &amp; My Old Man</div>'
def carousel(slides):
    n = len(slides); out = []
    for i,(cls,inner,left) in enumerate(slides,1):
        foot = f'<div class="foot">{"<span class=left>"+left+"</span>" if left else ""}<span class="page">{i:02d} / {n:02d}</span></div>'
        out.append(f'<section class="slide {cls}">\n  {M}\n  {inner}\n  {foot}\n</section>')
    return head + "\n".join(out) + tail
def card(cls, quote, by, small=False):
    inner = f'<div class="q{" small" if small else ""}">{quote}</div>\n  <div class="by">{by}</div>'
    return head + f'<section class="slide {cls}">\n  {M}\n  {inner}\n  <div class="foot"><span class="left">meandmyoldman.co.uk</span></div>\n</section>' + tail

files = {}
files["tell-her"] = carousel([
 ("", "<h1>He&rsquo;d already decided. He just didn&rsquo;t know how to tell her.</h1><p>Every practical question asked. Ready to book.</p>", "Here&rsquo;s what I told him &rarr;"),
 ("", "<h2>&ldquo;I just don&rsquo;t know how I&rsquo;m going to tell her.&rdquo;</h2><p>Not because he thought she&rsquo;d say no.</p>", ""),
 ("", "<h2>He was already rehearsing it going wrong.</h2>", ""),
 ("peach", "<h2>It&rsquo;s not about persuading them.</h2><p>It&rsquo;s about telling them the truth of why you want it.</p>", ""),
 ("", "<div class=num>&times;</div><h2>&ldquo;I&rsquo;ve booked something.&rdquo;</h2><p>A plan, with no reason attached.</p>", ""),
 ("", "<h2>&ldquo;I want to hear you tell it, in your own words, while I still can.&rdquo;</h2><div class=accent>The why.</div>", ""),
 ("dark", "<h2>The real reasons, and what to say back to the six things parents usually say.</h2><p>Link&rsquo;s in the comments.</p>", "meandmyoldman.co.uk"),
])
files["one-question"] = carousel([
 ("", "<h1>The two questions I wish I&rsquo;d asked my dad.</h1><p>Asked live on a podcast. No time to think.</p>", "Here they are &rarr;"),
 ("", "<div class=num>1</div><h2>&ldquo;Am I doing okay?&rdquo;</h2><p>The small one.</p>", ""),
 ("", "<div class=num>2</div><h2>&ldquo;What do you believe are the ingredients to a good life?&rdquo;</h2><p>The bigger one.</p>", ""),
 ("peach", "<h2>I&rsquo;ll never get an answer to either.</h2>", ""),
 ("", "<h2>If your parent&rsquo;s still here, you still can.</h2><div class=accent>This week.</div><p>Pick one. Ask it.</p>", ""),
 ("dark", "<h2>Comment STORIES and I&rsquo;ll send you the other 105.</h2><p>107 questions, organised by life stage.</p>", "meandmyoldman.co.uk"),
])
files["ventriloquist"] = card("", "Neither fact had come up at a family dinner in thirty years.", "A ventriloquist granddad. A cellist dad.")
files["mates-text"] = card("dark", "&ldquo;Mate, this really is something so special.&rdquo;", "A mate, texting on a Tuesday")
files["pringle-pots"] = card("", "We&rsquo;ve mostly seen the version built for us. Not the cellar version.", "The Pringle pots")
files["waiting"] = card("peach", "&ldquo;There is no scenario where waiting is a better option.&rdquo;", "Neil Taylor")
def nb(m):
    t=m.group(2); t=re.sub(r' (\S+)$', r'&nbsp;\1', t.strip()); return m.group(1)+t+m.group(3)
for k in files:
    files[k]=re.sub(r'(<(?:h1|h2)>|<div class="q[^"]*">)(.*?)(</(?:h1|h2|div)>)', nb, files[k])
for k,v in files.items():
    pathlib.Path(f"{k}.html").write_text(v)
print("ok")
