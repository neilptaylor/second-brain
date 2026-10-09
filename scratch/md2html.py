import re,sys,html
src,dst,title=sys.argv[1:4]
H="font-family:'Marcellus', serif; color:#A85639; font-weight:normal;"
B="font-family:'Merriweather', serif; font-size:11pt; line-height:1.5; color:#2B2420;"
M="font-family:'Merriweather', serif; font-size:9.5pt; line-height:1.4; color:#5A5048; font-style:italic;"
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'(https?://[^\s<]+)',lambda m:f'<a href="{m.group(1)}" style="color:#1F7A85;">Book a 20-minute chat</a>' if 'calendly' in m.group(1) else m.group(1),t)
    return t
o=['<html><head><meta charset="utf-8"></head><body style="font-family:\'Merriweather\', serif; color:#2B2420;">']
meta=re.compile(r'^(Job:|Source:|Check:|Swap:|Alt hook|Segment:|Offer:|Call ask:|Links to confirm:|Sources at)')
for line in open(src).read().split('\n'):
    s=line.rstrip()
    if not s: continue
    if s=='---': o.append('<hr style="border:none; border-top:1px solid #D8CFC2;">'); continue
    if s.startswith('# '): o.append(f'<h1 style="{H} font-size:24pt;">{inline(s[2:])}</h1>'); continue
    if s.startswith('## '): o.append(f'<h2 style="{H} font-size:16pt; margin-top:18pt;">{inline(s[3:])}</h2>'); continue
    if s.startswith('- '): o.append(f'<p style="{M}">{inline(s)}</p>'); continue
    if s.startswith(('Subject:','Preview:')):
        k,v=s.split(':',1); o.append(f'<p style="{B}"><b>{k}:</b>{inline(v)}</p>'); continue
    if meta.match(s): o.append(f'<p style="{M}">{inline(s)}</p>'); continue
    o.append(f'<p style="{B}">{inline(s)}</p>')
o.append('</body></html>')
open(dst,'w').write('\n'.join(o))
