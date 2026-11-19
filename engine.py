import json,os,sys,urllib.request as R,urllib.error as E
U=os.environ.get("MAKEFUN_ENV_URL","")
def P(p,b):
 if not U:sys.exit("no env")
 q=R.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with R.urlopen(q) as s:return json.load(s)
 except E.HTTPError as x:sys.exit(f"{p}:{x.code}")
V=[0,100,320,330,500,900,0]
ND=[-33,-31,-18,-14,14,18,31,33]
KD=[-17,-16,-15,-1,1,15,16,17]
BD=[-17,-15,15,17]
RD=[-16,-1,1,16]
B=[0]*128;SD=1;CA=0;EP=-1;KW=4;KB=116;ST=[];KL=[[0,0] for _ in range(128)];PV=0;NN=0;NB=120000
class X(Exception):pass
def uc(m):
 f=m&127;t=m>>7&127;q=m>>14
 return "abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1)+("nbrq"[q-2] if q else "")
def parse(f):
 global B,SD,CA,EP,KW,KB
 B=[0]*128;ST.clear();p=f.split();r=7;d=0
 for c in p[0]:
  if c=="/":r-=1;d=0
  elif c.isdigit():d+=int(c)
  else:
   v="PNBRQK".index(c.upper())+1;z=r*16+d
   B[z]=v if c.isupper() else -v
   if v==6:KW,KB=(z,KB) if c.isupper() else (KW,z)
   d+=1
 SD=1 if p[1]=="w" else -1
 g=p[2] if len(p)>2 else "-"
 CA=(1 if "K" in g else 0)|(2 if "Q" in g else 0)|(4 if "k" in g else 0)|(8 if "q" in g else 0)
 h=p[3] if len(p)>3 else "-"
 EP=-1 if h=="-" else (int(h[1])-1)*16+ord(h[0])-97
def atk(s,a):
 for o in (s-16*a-1,s-16*a+1):
  if not o&136 and B[o]==a:return 1
 for d in ND:
  o=s+d
  if not o&136 and B[o]==2*a:return 1
 for d in KD:
  o=s+d
  if not o&136 and B[o]==6*a:return 1
 for d in BD:
  o=s+d
  while not o&136:
   q=B[o]
   if q:
    if q==3*a or q==5*a:return 1
    break
   o+=d
 for d in RD:
  o=s+d
  while not o&136:
   q=B[o]
   if q:
    if q==4*a or q==5*a:return 1
    break
   o+=d
 return 0
def gen():
 ms=[]
 def pm(f,t):
  if (f>>4)+SD in (0,7):
   for q in (5,4,3,2):ms.append(f|t<<7|q<<14)
  else:ms.append(f|t<<7)
 for i,p in enumerate(B):
  if i&136 or p*SD<=0:continue
  t=abs(p);r=i>>4
  if t==1:
   d=16*SD;o=i+d
   if not o&136 and not B[o]:
    pm(i,o)
    if r==(1 if SD>0 else 6) and not B[i+2*d]:ms.append(i|(i+2*d)<<7)
   for df in (-1,1):
    o=i+d+df
    if o&136:continue
    if B[o]*SD<0:pm(i,o)
    elif o==EP:ms.append(i|o<<7)
  elif t==2 or t==6:
   for d in ND if t==2 else KD:
    o=i+d
    if not o&136 and B[o]*SD<=0:ms.append(i|o<<7)
  else:
   for d in BD+RD if t==5 else BD if t==3 else RD:
    o=i+d
    while not o&136:
     q=B[o]
     if q:
      if q*SD<0:ms.append(i|o<<7)
      break
     ms.append(i|o<<7);o+=d
 for K,R,T,C,E,A in ((4,7,6,1,(5,6),(4,5,6)),(4,0,2,2,(3,2,1),(4,3,2)),(116,119,118,4,(117,118),(116,117,118)),(116,112,114,8,(115,114,113),(116,115,114))):
  if CA&C and B[K]==6*SD and B[R]==4*SD and all(not B[e] for e in E) and all(not atk(a,-SD) for a in A):ms.append(K|T<<7)
 return ms
def make(m):
 global SD,CA,EP,KW,KB
 f=m&127;t=m>>7&127;q=m>>14
 p=B[f];c=B[t];u=0
 if abs(p)==1 and t==EP and not c:
  u=t-16*SD;c=B[u];B[u]=0
 ST.append((m,c,CA,EP,KW,KB,u))
 B[f]=0;B[t]=q*SD if q else p
 if abs(p)==6:
  if SD>0:KW=t
  else:KB=t
  if t-f==2:B[t-1]=B[t+1];B[t+1]=0
  elif f-t==2:B[t+1]=B[t-2];B[t-2]=0
  CA&=-4 if SD>0 else -13
 if f==0 or t==0:CA&=~2
 if f==7 or t==7:CA&=~1
 if f==112 or t==112:CA&=~8
 if f==119 or t==119:CA&=~4
 EP=f+16*SD if abs(p)==1 and abs(t-f)==32 else -1
 SD=-SD
def unmake():
 global SD,CA,EP,KW,KB
 m,c,CA,EP,KW,KB,u=ST.pop()
 f=m&127;t=m>>7&127;q=m>>14
 SD=-SD;p=B[t]
 if abs(p)==6 and abs(t-f)==2:
  if t>f:B[t+1]=B[t-1];B[t-1]=0
  else:B[t-2]=B[t+1];B[t+1]=0
 B[f]=SD if q else p;B[t]=0
 if u:B[u]=c
 else:B[t]=c
def ev():
 s=0;n=0;w=0;b=0
 for i,p in enumerate(B):
  if i&136 or not p or abs(p)==6:continue
  t=abs(p);v=V[t];r=i>>4;f=i&7;c=14-abs(2*f-7)-abs(2*r-7)
  if t==1:v+=(r if p>0 else 7-r)*7
  elif t==2:v+=c*4
  elif t==3:
   v+=c*2
   if p>0:w+=1
   else:b+=1
  if t>1:n+=V[t]
  s+=v if p>0 else -v
 for k,g in ((KW,1),(KB,-1)):
  r=k>>4;f=k&7;c=14-abs(2*f-7)-abs(2*r-7)
  s+=(c*4 if n<2600 else ((2-r) if g>0 else (r-5))*8)*g
 return s+25*(w==2)-25*(b==2)
def sc(m,pl):
 f=m&127;t=m>>7&127;q=m>>14;v=0;c=B[t]
 if c:v=10*V[abs(c)]-V[abs(B[f])]//10
 elif abs(B[f])==1 and t==EP:v=1000
 if q:v+=900
 if m==KL[pl][0]:v+=6000
 elif m==KL[pl][1]:v+=5000
 if m==PV:v+=100000
 return -v
def qs(a,b,pl):
 global NN
 NN+=1
 if NN>NB:raise X
 s=ev()*SD
 if s>=b:return b
 if s>a:a=s
 k=KW if SD>0 else KB;ch=atk(k,-SD)
 ms=gen() if ch else [m for m in gen() if B[(m>>7)&127] or (m>>14) or (abs(B[m&127])==1 and ((m>>7)&127)==EP)]
 ms.sort(key=lambda m:sc(m,pl))
 lg=0
 for m in ms:
  make(m)
  if atk(KW if SD<0 else KB,SD):unmake();continue
  lg+=1
  s=-qs(-b,-a,pl+1)
  unmake()
  if s>a:a=s
  if a>=b:break
 if ch and not lg:return -100000+pl
 return a
def sr(a,b,d,pl):
 global NN
 NN+=1
 if NN>NB:raise X
 if d<=0 or pl>40:return qs(a,b,pl)
 k=KW if SD>0 else KB
 if atk(k,-SD):d+=1
 ms=gen();ms.sort(key=lambda m:sc(m,pl))
 be=-999999;lg=0
 for m in ms:
  make(m)
  if atk(KW if SD<0 else KB,SD):unmake();continue
  lg+=1
  s=-sr(-b,-a,d-1,pl+1)
  unmake()
  if s>be:be=s
  if be>a:a=be
  if a>=b:
   if not B[(m>>7)&127] and not (m>>14) and not (abs(B[m&127])==1 and ((m>>7)&127)==EP):
    if m!=KL[pl][0]:KL[pl][1]=KL[pl][0];KL[pl][0]=m
   break
 if not lg:return -100000+pl if atk(k,-SD) else 0
 return be
def best(fen,legal):
 parse(fen)
 global NN,PV
 NN=0;PV=0;bm=0
 ls=set(legal)
 for d in range(1,13):
  try:
   ms=[m for m in gen() if uc(m) in ls]
   ms.sort(key=lambda m:sc(m,0))
   a=-10**9;cur=0
   for m in ms:
    make(m)
    if atk(KW if SD<0 else KB,SD):unmake();continue
    s=-sr(-10**9,-a,d-1,1)
    unmake()
    if s>a:a=s;cur=m
   if cur:bm=cur;PV=cur
  except X:break
 parse(fen)
 return uc(bm) if bm else legal[0]
if __name__=="__main__":
 while 1:
  g=P("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   g=P("/move",{"game":g["game"],"move":best(g["fen"],g["legal_moves"])})
  print(g["game"],g["outcome"],g["reason"],file=sys.stderr)
 print("done",g.get("wins"),g.get("draws"),g.get("losses"),file=sys.stderr)
