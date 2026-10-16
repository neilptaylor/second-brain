const { chromium } = require(process.env.PW);
const fs = require('fs');
const OUT = __dirname + '/a5/';
const fcss = fs.readFileSync(__dirname+'/fonts/s.css','utf8').replace(/url\((s?c?\d+\.ttf)\)/g,(m,f)=>'url(data:font/ttf;base64,'+fs.readFileSync(__dirname+'/fonts/'+f).toString('base64')+')');
const fonts = '<style>'+fcss+'</style>';
const css = (h) => `
*{margin:0;padding:0;box-sizing:border-box}
@page{size:1080px ${h}px;margin:0}
body{background:#f9f6f1}
.s{width:1080px;height:${h}px;background:#f9f6f1;position:relative;padding:120px;page-break-after:always;overflow:hidden;display:flex;flex-direction:column;justify-content:center;color:#1c1814}
.s.c{align-items:center;text-align:center}
.disp{font-family:"Marcellus","Cormorant Garamond",serif;font-weight:400;line-height:1.08}
.h1{font-size:84px}.h2{font-size:64px}
.q{font-family:"Cormorant Garamond","Marcellus",serif;font-style:italic;font-weight:300;font-size:92px;line-height:1.12}
.body{font-family:Inter,"Helvetica Neue",Arial,sans-serif;font-size:42px;line-height:1.5;color:#3a3228}
.lab{font-family:Inter,sans-serif;font-size:32px;color:#7a6e62;margin-top:40px;line-height:1.4}
.num{font-family:Marcellus,serif;font-size:140px;color:#b8674e;line-height:1;margin-bottom:36px}
.rule{width:80px;height:3px;background:#b8674e;margin:44px 0}
.s.c .rule{margin:44px auto}
.cta{font-family:Inter,sans-serif;font-weight:500;font-size:50px;color:#b8674e;margin-top:40px}
.pg{position:absolute;bottom:70px;right:120px;font-family:Inter,sans-serif;font-size:26px;color:#9e9185}
.mark{position:absolute;bottom:70px;left:0;right:0;text-align:center;font-family:Marcellus,serif;font-size:24px;color:#7a6e62}
.bg2{background:#f0ebe3}
`;
const page = (h, slides) => `<!doctype html><html><head><meta charset="utf-8">${fonts}<style>${css(h)}</style></head><body>${slides.join('')}</body></html>`;
const slide = (cls, inner, n, total, mark) => `<div class="s ${cls}">${inner}${n?`<div class="pg">${n} / ${total}</div>`:''}${mark?'<div class="mark">Me &amp; My Old Man</div>':''}</div>`;


const hand=(lines,sign)=>{const rots=[-1.2,0.6,-0.4,0.8];return `<div class="s hand">${lines.map((l,i)=>`<div class="hl" style="rotate:${rots[i%4]}deg">${l}</div>`).join('')}<div class="hs">&mdash; Neil</div></div>`;};
const handcss=`.s.hand{background:radial-gradient(ellipse at 50% 40%,#f3ecdd 0%,#e6dcc4 100%);justify-content:center;align-items:flex-start}
.hl{font-family:Caveat,cursive;font-weight:500;font-size:96px;line-height:1.25;color:#1e2a4a;text-shadow:0 0 1px rgba(30,42,74,.5),0 0 3px rgba(30,42,74,.25),0 0 6px rgba(30,42,74,.12)}
.hs{font-family:Caveat,cursive;font-size:64px;color:#3c4a6c;margin-top:50px;rotate:-1deg}`;
const T=(n,t,lab,total,i)=>slide('', `<div class="num" style="font-size:96px">${n}</div><div class="disp h2" style="font-size:60px">${t}</div>${lab?`<div class="lab">${lab}</div>`:''}`, i, total);
// Oct 15 why carousel
const whys=[
"If I&rsquo;m honest, there&rsquo;s so much about your life that I don&rsquo;t know. You may not have told me, I may not have asked, so this is a way to fix that.",
"I want to hear the stories of your life, in your own voice, not my memory of them, while I still can.",
"I think about my grandparents and realise I know almost nothing about them. I don&rsquo;t want that to happen with you too.",
"I want to know where I actually come from. The history, the &ldquo;why am I like this.&rdquo;",
"I want to say thank you properly, out loud, for everything you&rsquo;ve done for me.",
"I want my own kids, and whoever comes after them, to know you as fully as they can. Not just me.",
"I want us to feel closer. Not in a big dramatic way. Just closer.",
"I want you to look back at everything you&rsquo;ve done and feel proud of it.",
"I want something that lasts. Something my kids can put on in twenty years and hear you again."];
const TW=whys.length+2;
const why=[ slide('c', `<div class="disp h1">Why do you even want this?</div><div class="rule"></div><div class="disp h2" style="color:#3a3228">Nine ways to say it.</div>`,0,TW,true),
 ...whys.map((w,i)=>slide('', `<div class="num" style="font-size:96px">${i+1}</div><div class="disp" style="font-size:54px;line-height:1.2">${w}</div>`, i+2, TW)),
 slide('c bg2', `<div class="disp h2">Pick one.<br>That&rsquo;s your opening line.</div><div class="cta">Link in the comments</div>`,0,TW,true)];
// Oct 22 photo box
const TP=7;
const photo=[ slide('c', `<div class="disp h1">One person in your family can still name everyone in that box.</div>`,0,TP,true),
 slide('', `<div class="disp h2">&ldquo;Who is this?&rdquo;</div><div class="body" style="margin-top:36px">Full name, and what you called them.</div>`,2,TP),
 slide('', `<div class="disp h2">&ldquo;Where was this taken?&rdquo;</div><div class="body" style="margin-top:36px">Whose house, whose garden?</div>`,3,TP),
 slide('', `<div class="disp h2">&ldquo;What happened right after this was taken?&rdquo;</div><div class="body" style="margin-top:36px">And right before?</div>`,4,TP),
 slide('', `<div class="disp h2">&ldquo;Who took it?&rdquo;</div><div class="body" style="margin-top:36px">Why that day?</div>`,5,TP),
 slide('', `<div class="disp h2">Tip the box out on the table. Phone on record. One at a time.</div>`,6,TP),
 slide('c bg2', `<div class="disp h2">Do the box before it&rsquo;s just faces.</div><div class="cta">Comment PHOTOS</div>`,0,TP,true)];
// Nov 5 choice not chronology
const TC=5;
const choice=[ slide('c', `<div class="disp h1">Stop asking your parents for a timeline.</div>`,0,TC,true),
 slide('', `<div class="disp h2">&ldquo;What&rsquo;s the hardest decision you ever made that nobody saw you make?&rdquo;</div>`,2,TC),
 slide('', `<div class="disp" style="font-size:52px;line-height:1.3">Then follow the thread, gently, three times:</div><div class="body" style="margin-top:44px">What would have happened if you&rsquo;d gone the other way?<br><br>Who did you talk to about it, or did you carry it on your own?<br><br>Do you still think you got it right?</div>`,3,TC),
 slide('', `<div class="disp h2">Chronology tells you what your parent did.</div><div class="rule"></div><div class="disp h2" style="color:#b8674e">Choice tells you who they are, and what it cost them.</div>`,4,TC),
 slide('c bg2', `<div class="disp h2">The full guide this question comes from.</div><div class="cta">Comment PLAYBOOK</div>`,0,TC,true)];
const pqc=(t)=>[slide('', `<div class="q">${t}</div><div class="rule"></div>`,0,0,true)];
const reel=[slide('c', `<div class="disp h1" style="font-size:96px">Sorry. Back up.<br>There was a SALT FARM?</div>`,0,0,true)];
(async()=>{
  const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  const jobs=[
   ['MMOM_LI_why-do-you-even-want-this_v1',1350,why,'pdf'],
   ['MMOM_LI_photo-box_v1',1350,photo,'pdf'],
   ['MMOM_LI_choice-not-chronology_v1',1350,choice,'pdf'],
   ['MMOM_LI_dont-price-it-like-a-present_v1',1350,pqc('I get why. But it&rsquo;s the wrong shelf.'),'png'],
   ['MMOM_LI_my-life-isnt-that-interesting_v1',1350,pqc('The ordinary is only ordinary from the inside.'),'png'],
   ['MMOM_LI_does-this-happen_v1',1350,[hand(['Does this happen','when we&rsquo;re not there?'])],'png'],
   ['MMOM_LI_how-big-a-shag-is-it_v1',1350,[hand(['Not grief.','Not awkwardness.','Admin.'])],'png'],
   ['MMOM_LI_diary-test_v1',1350,[hand(['The important stuff','doesn&rsquo;t shout.'])],'png'],
   ['MMOM_LI_we-parked-it_v1',1350,[hand(['Not through','carelessness.','Through timing that&rsquo;s','never quite right.'])],'png'],
   ['MMOM_LI_almost-none-of-his-voice_v1',1350,[hand(['The voice is the thing','that goes first.'])],'png'],
   ['MMOM_LI_salt-farm_reel-cover_v1',1920,reel,'png'],
  ];
  for (const [name,h,slides,kind] of jobs){
    const p = await b.newPage({viewport:{width:1080,height:h}});
    await p.setContent(page(h,slides).replace('</style>',handcss+'</style>'),{waitUntil:'networkidle'});
    await p.evaluate(()=>document.fonts.ready);
    if(kind==='pdf') await p.pdf({path:OUT+name+'.pdf',width:'1080px',height:h+'px',printBackground:true});
    else await p.screenshot({path:OUT+name+'.png',clip:{x:0,y:0,width:1080,height:h}});
    await p.close();
  }
  await b.close();
})();
