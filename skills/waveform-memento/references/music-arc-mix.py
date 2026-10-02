import numpy as np, subprocess
SR=48000; D=5.8; TOTAL=104.4
def load(p):
    r=subprocess.run(["ffmpeg","-v","error","-i",p,"-ar",str(SR),"-ac","2","-f","f32le","-"],capture_output=True).stdout
    return np.frombuffer(r,dtype=np.float32).reshape(-1,2)
vo=load("assets/audio/vo.wav"); st=load("assets/audio/sting.wav")
N=int(TOTAL*SR); t=np.arange(N)/SR
def sm(x): x=np.clip(x,0,1); return x*x*(3-2*x)   # smoothstep
def ramp(t,a,b,v0,v1): return v0+(v1-v0)*sm((t-a)/(b-a))
# VO
voch=np.zeros((N,2),np.float32); o=int(D*SR); voch[o:o+len(vo)]=vo[:N-o]
vog=np.clip((t-D)/0.4,0,1)[:,None]
# Music
def place(off):
    m=np.zeros((N,2),np.float32); o=int(off*SR); seg=st[:N-o]; m[o:o+len(seg)]=seg; return m
# intro: sting from its start at t=0 ; outro: sting restarted at 87.0
intro=place(0.0); outro=place(87.0)
gi=ramp(t,0.8,4.4,0,0.75)*(1-sm((t-4.9)/1.4))                 # slow fade in 3-5s, out as title leaves
go=np.where(t<87.0,0.0,0.0)
# outro envelope: gentle build under VO, never competes; crescendo 1s after last word; hold; fade with end card
VO_END=D+91.6
go=ramp(t,87.0,VO_END,0.0,0.10)
go=np.where(t>VO_END, 0.10+0.0, go)
go=np.where(t>VO_END+1.0, 0.10+(0.80-0.10)*sm((t-(VO_END+1.0))/2.4), go)
go=go*(1-sm((t-102.4)/2.0))
go=np.where(t<87.0,0,go)
music=intro*gi[:,None]+outro*go[:,None]
mix=voch*vog+music
print("peak",np.abs(mix).max())
mix=mix/max(1.0,np.abs(mix).max()*1.02)
import wave
w=wave.open("assets/audio/mix.wav","wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix*32767).astype("<i2").tobytes()); w.close()
