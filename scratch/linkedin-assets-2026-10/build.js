const { chromium } = require(process.env.PW);
const fs = require('fs');
const OUT = __dirname + '/a3/';
const fcss = fs.readFileSync(__dirname+'/fonts/s.css','utf8').replace(/url\((s\d+\.ttf)\)/g,(m,f)=>'url(data:font/ttf;base64,'+fs.readFileSync(__dirname+'/fonts/'+f).toString('base64')+')');
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

// PP3 carousel: Snippet to story
const pp3m = [
 ['Start with an object.','&ldquo;Tell me about this ring.&rdquo;'],
 ['Ask what they were<br>afraid of,','not just what happened.'],
 ['Leave the silence.','Don&rsquo;t rescue it.'],
 ['Ask &ldquo;and then<br>what?&rdquo;','three times before you let them move on.'],
 ['End with:','&ldquo;Who else was there? Who should I ask?&rdquo;'],
];
const T3 = 7;
const pp3 = [
 slide('c', `<div class="disp h1">You&rsquo;ve got fragments of your parents&rsquo; lives.</div><div class="rule"></div><div class="disp h2" style="color:#3a3228">Here&rsquo;s how to get the whole story.</div>`,0,T3,true),
 ...pp3m.map((m,i)=>slide('', `<div class="num">${i+1}</div><div class="disp h2">${m[0]}</div><div class="body" style="margin-top:36px">${m[1]}</div>`, i+2, T3)),
 slide('c bg2', `<div class="disp h2">The whole guide is the Conversation Playbook.</div><div class="cta">Comment PLAYBOOK</div>`,0,T3,true),
];
// PP1 carousel
const T1 = 5;
const pp1 = [
 slide('c', `<div class="disp h1">He&rsquo;d tell you forty stories.</div><div class="rule"></div><div class="disp h1" style="color:#3a3228">None of them were about him.</div>`,0,T1,true),
 slide('', `<div class="disp h2">&ldquo;You&rsquo;ve told me that story loads of times. Where were you standing when it happened? What were you thinking?&rdquo;</div><div class="lab">Keep the story he loves. Make it his.</div>`,2,T1),
 slide('', `<div class="disp h2">&ldquo;What were you like at the age I am now?&rdquo;</div><div class="lab">One he&rsquo;s been performing his way around for years.</div>`,3,T1),
 slide('', `<div class="disp h2">&ldquo;What&rsquo;s a decision you made that nobody else saw you make?&rdquo;</div><div class="lab">The one nobody&rsquo;s asked.</div>`,4,T1),
 slide('c bg2', `<div class="disp h2">The questions that get past the performance.</div><div class="cta">Comment PLAYBOOK</div>`,0,T1,true),
];
// Pull quote card
const pq = [ slide('', `<div class="q">&ldquo;That was the real him. We&rsquo;d never have got that from a solo interview.&rdquo;</div><div class="rule"></div><div class="lab" style="margin-top:0">A daughter, after her family&rsquo;s sessions</div>`,0,0,true) ];
// Reel covers 1080x1920
const rc1 = [ slide('c', `<div class="disp h1" style="font-size:96px">Someday is one of the most dangerous words in a family.</div>`,0,0,true) ];
const rc2 = [ slide('c', `<div class="disp h1" style="font-size:104px">What are you scared of?</div><div class="rule"></div><div class="disp h2" style="color:#3a3228">And what&rsquo;s the alternative?</div>`,0,0,true) ];

(async()=>{
  const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  const jobs = [
   ['MMOM_LI_bits-and-pieces_v1', 1350, pp3, 'pdf'],
   ['MMOM_LI_storyteller-never-tells-about-himself_v1', 1350, pp1, 'pdf'],
   ['MMOM_LI_more-of-his-real-character_v1', 1350, pq, 'png'],
   ['MMOM_LI_someday-is-dangerous_reel-cover_v1', 1920, rc1, 'png'],
   ['MMOM_LI_what-are-you-scared-of_reel-cover_v1', 1920, rc2, 'png'],
  ];
  for (const [name,h,slides,kind] of jobs){
    const p = await b.newPage({viewport:{width:1080,height:h}});
    await p.setContent(page(h,slides),{waitUntil:'networkidle'});
    await p.evaluate(()=>document.fonts.ready);
    if(kind==='pdf') await p.pdf({path:OUT+name+'.pdf',width:'1080px',height:h+'px',printBackground:true});
    else await p.screenshot({path:OUT+name+'.png',clip:{x:0,y:0,width:1080,height:h}});
    await p.close();
  }
  await b.close();
})();
