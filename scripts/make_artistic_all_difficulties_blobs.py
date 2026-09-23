from pathlib import Path
from PIL import Image, ImageChops, ImageFilter
from urllib.request import urlopen, Request
from io import BytesIO
import json, re, math, sys
base=Path('D:/헤르메스 작업/dino-bone-puzzle')
lock=json.load(open(base/'final-lineup-lock.json',encoding='utf-8'))['lineup']
root=base/'assets/pieces/artistic-difficulties-v1'; root.mkdir(parents=True,exist_ok=True)
cache=base/'assets/cache/locked-images'; cache.mkdir(parents=True,exist_ok=True)
DIFFS={'easy':6,'normal':12,'hard':20}
COLORS=[(255,92,92,255),(255,170,70,255),(255,232,80,255),(93,220,130,255),(80,190,255,255),(190,135,255,255),(255,120,190,255),(120,240,220,255),(210,190,90,255),(160,220,90,255),(120,150,255,255),(255,140,90,255),(170,110,255,255),(90,230,180,255),(230,230,230,255),(255,210,130,255),(130,255,160,255),(120,210,255,255),(220,140,255,255),(255,110,110,255)]
def slugify(s): return re.sub(r'[^a-z0-9가-힣]+','-',s.lower()).strip('-')[:60] or 'item'
def load(src,num):
    if src.startswith('http'):
        fetch=src+('?width=2000' if src.lower().endswith('.svg') else '')
        data=urlopen(Request(fetch,headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read(); (cache/f'{num:02d}-blob-raw').write_bytes(data)
        im=Image.open(BytesIO(data)).convert('RGBA')
    else: im=Image.open(base/src).convert('RGBA')
    bg=Image.new('RGBA',im.size,(255,255,255,255)); bg.alpha_composite(im); im=bg
    pix=im.load(); xs=[]; ys=[]; w,h=im.size
    for y in range(h):
        for x in range(w):
            r,g,b,a=pix[x,y]
            if a>20 and not (r>245 and g>245 and b>245): xs.append(x); ys.append(y)
    if xs:
        pad=24; im=im.crop((max(0,min(xs)-pad),max(0,min(ys)-pad),min(w,max(xs)+pad),min(h,max(ys)+pad)))
    if im.width>2200:
        nh=int(im.height*2200/im.width); im=im.resize((2200,nh),Image.Resampling.LANCZOS)
    return im
def visible_cells(im,cell):
    w,h=im.size; pix=im.load(); cells=[]; xs=[]; ys=[]
    for y in range(0,h,cell):
        for x in range(0,w,cell):
            pts=[]
            for yy in range(y,min(h,y+cell)):
                for xx in range(x,min(w,x+cell)):
                    r,g,b,a=pix[xx,yy]
                    if a>20 and not (r>245 and g>245 and b>245): pts.append((xx,yy))
            if pts:
                cx=x+cell/2; cy=y+cell/2; cells.append({'x':x,'y':y,'cx':cx,'cy':cy,'pts':pts}); xs.append(cx); ys.append(cy)
    return cells,(min(xs),min(ys),max(xs),max(ys)) if cells else (0,0,1,1)
def make_groups(cells,bbox,n,level,num):
    minx,miny,maxx,maxy=bbox; W=max(1,maxx-minx); H=max(1,maxy-miny)
    def norm(p): return ((p['cx']-minx)/W,(p['cy']-miny)/H)
    byx=sorted(cells,key=lambda p:p['cx'])
    seeds=[byx[int(len(byx)*.08)]]
    while len(seeds)<n:
        best=None; bd=-1
        for p in cells:
            px,py=norm(p); d=min((px-norm(s)[0])**2+(py-norm(s)[1])**2*2.2 for s in seeds)
            if d>bd: bd=d; best=p
        seeds.append(best)
    seeds=[{'x':s['cx'],'y':s['cy'],'i':i} for i,s in enumerate(seeds)]
    groups=[[] for _ in range(n)]
    for _ in range(12):
        groups=[[] for _ in range(n)]
        for p in cells:
            px=(p['cx']-minx)/W; py=(p['cy']-miny)/H; best=0; bd=1e9
            for i,s in enumerate(seeds):
                sx=(s['x']-minx)/W; sy=(s['y']-miny)/H
                wob=0 if level=='easy' else .012*math.sin((px+i*.31)*21)+.010*math.cos((py-i*.17)*17)
                d=(px-sx)**2+(py-sy)**2*2.05+wob
                if d<bd: bd=d; best=i
            groups[best].append(p)
        for guard in range(30):
            empty=[i for i,g in enumerate(groups) if not g]
            if not empty: break
            bi=max(range(n),key=lambda i:len(groups[i])); g=sorted(groups[bi],key=lambda p:p['cx']+p['cy']*.35); cut=len(g)//2
            groups[bi]=g[:cut]; groups[empty[0]]=g[cut:] or groups[bi][-1:]
        seeds=[]
        for i,g in enumerate(groups):
            if not g: seeds.append({'x':cells[0]['cx'],'y':cells[0]['cy'],'i':i})
            else: seeds.append({'x':sum(p['cx'] for p in g)/len(g),'y':sum(p['cy'] for p in g)/len(g),'i':i})
    mincells=max(4,int(len(cells)/n*.16))
    for _ in range(40):
        small=[i for i,g in enumerate(groups) if 0<len(g)<mincells]
        if not small: break
        si=small[0]; bi=max(range(n),key=lambda i:len(groups[i]))
        if len(groups[bi])<=mincells*2: break
        groups[bi]=sorted(groups[bi],key=lambda p:p['cx']+p['cy']*.45); take=groups[bi][int(len(groups[bi])*.62):]; groups[bi]=groups[bi][:int(len(groups[bi])*.62)]; groups[si]+=take
    return groups
def make(im,level,n,od,num):
    od.mkdir(parents=True,exist_ok=True); im.save(od/'source-normalized.png')
    cell=6 if level=='easy' else 5 if level=='normal' else 4
    cells,bbox=visible_cells(im,cell)
    if len(cells)<n: raise RuntimeError(f'not enough visible cells {len(cells)} for {n}')
    groups=make_groups(cells,bbox,n,level,num)
    w,h=im.size; pix=im.load(); piece_imgs=[Image.new('RGBA',(w,h),(0,0,0,0)) for _ in range(n)]; over=Image.new('RGBA',(w,h),(255,255,255,255)); counts=[0]*n
    for i,g in enumerate(groups):
        col=COLORS[i%len(COLORS)]
        for cellobj in g:
            for x,y in cellobj['pts']:
                piece_imgs[i].putpixel((x,y),pix[x,y]); counts[i]+=1
                sr,sg,sb,sa=pix[x,y]; cr,cg,cb,ca=col; over.putpixel((x,y),(int(cr*.72+sr*.28),int(cg*.72+sg*.28),int(cb*.72+sb*.28),255))
    if any(c<=0 for c in counts): raise RuntimeError(f'empty counts {counts}')
    over.save(od/f'artistic-{n}-colored-overview.png')
    meta=[]
    for i,pim in enumerate(piece_imgs):
        bb=pim.getchannel('A').getbbox(); pad=22
        if not bb: raise RuntimeError(f'empty piece {i+1}')
        l,t,r,b=bb; crop=(max(0,l-pad),max(0,t-pad),min(w,r+pad),min(h,b+pad)); cropped=pim.crop(crop)
        fname=f'{i+1:02d}-piece-{i+1}.png'; cropped.save(od/fname)
        meta.append({'piece':i+1,'label':f'조각 {i+1}','en':f'Puzzle piece {i+1}','file':str((od/fname).relative_to(base)).replace('\\','/'),'bbox':crop,'ink_pixels':counts[i]})
    edge=over.copy()
    for i,p in enumerate(meta):
        img=Image.open(base/p['file']).convert('RGBA'); l,t,r,b=p['bbox']; full=Image.new('L',(w,h),0); full.paste(img.getchannel('A'),(l,t))
        e=ImageChops.subtract(full.filter(ImageFilter.MaxFilter(7)),full.filter(ImageFilter.MinFilter(3))); ep=e.load(); op=edge.load(); col=COLORS[i%len(COLORS)]
        for y in range(h):
            for x in range(w):
                if ep[x,y]>0: op[x,y]=col
    edge.save(od/f'artistic-{n}-pixel-edge-overview.png')
    (od/'pieces.json').write_text(json.dumps({'piece_count':n,'method':'compact visible-pixel blob clustering; no stripes/dots; generic labels only','pieces':meta},ensure_ascii=False,indent=2),encoding='utf-8')
    return {'piece_count':n,'assigned_ink_pixels':sum(counts),'min_piece_pixels':min(counts),'pieces':meta}
results=[]; errors=[]
for item in lock:
    try:
        num=item['number']; slug=f'{num:02d}-{slugify(item["name"])}'; im=load(item['image'],num); sdir=root/slug; diffmeta={}
        for level,n in DIFFS.items(): diffmeta[level]=make(im,level,n,sdir/level,num)
        (sdir/'species.json').write_text(json.dumps({'number':num,'ko':item['ko'],'name':item['name'],'source':item['image'],'difficulties':diffmeta},ensure_ascii=False,indent=2),encoding='utf-8')
        results.append({'number':num,'ko':item['ko'],'name':item['name'],'slug':slug,'outdir':str(sdir.relative_to(base)).replace('\\','/'),'status':'generated-blob-clusters-v3'}); print('OK',num,item['name'])
    except Exception as e:
        errors.append({'number':item.get('number'),'name':item.get('name'),'error':str(e)}); print('ERROR',item.get('number'),item.get('name'),e)
(root/'manifest.json').write_text(json.dumps({'difficulties':DIFFS,'results':results,'errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
print('DONE',len(results),'ok',len(errors),'errors')
if errors: sys.exit(2)
