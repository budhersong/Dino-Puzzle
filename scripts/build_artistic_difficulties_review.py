from pathlib import Path
import json
base=Path('D:/헤르메스 작업/dino-bone-puzzle')
root=base/'assets/pieces/artistic-difficulties-v1'
manifest=json.load(open(root/'manifest.json',encoding='utf-8'))
results=manifest['results']
diffs=[('easy','쉬움',6),('normal','보통',12),('hard','어려움',20)]
html=['''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dino-Bone Puzzle · 난이도별 예쁜 퍼즐 컷</title><style>*{box-sizing:border-box}body{margin:0;background:#070b09;color:#f6f0df;font-family:'Malgun Gothic',system-ui,sans-serif;padding:22px}h1{margin:0 0 8px}.lead{color:#c8d3cb;line-height:1.6}.box{border:1px solid #314339;border-radius:16px;background:#101912;padding:14px;margin:14px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:16px}.card{border:1px solid #314339;border-radius:18px;background:#111b16;overflow:hidden}.body{padding:12px}.num{font-weight:900;color:#ffe09b}.ko{font-size:18px;font-weight:900}.en{color:#b9c4bb;font-size:13px}.small{font-size:12px;color:#b9c4bb;line-height:1.55}.diffs{display:grid;grid-template-columns:1fr;gap:10px;margin-top:12px}.diff{border:1px solid #2b3a31;border-radius:12px;background:#0d1511;padding:8px}.diff h4{margin:0 0 6px;color:#ffe09b}.stage{height:210px;background:#fff;display:flex;align-items:center;justify-content:center;padding:6px;overflow:hidden;border-radius:10px}.stage img{max-width:100%;max-height:100%;object-fit:contain}code{background:#1e2b23;border-radius:5px;padding:1px 4px;color:#fff}</style></head><body><h1>Dino-Bone Puzzle · 난이도별 예쁜 퍼즐 컷 v1</h1><p class="lead">전략 확정: 골격 부위 명칭을 더 이상 사용하지 않습니다. 모든 조각은 <b>조각 1, 조각 2...</b> 형태의 단순 퍼즐 조각입니다.</p><div class="box"><b>조각 수:</b> 쉬움 6조각 / 보통 12조각 / 어려움 20조각<br><b>커팅:</b> 직선 박스가 아닌 물결형 퍼즐 컷. 종명/이미지는 최종 LOCK 그대로 유지.</div><div class="grid">''']
for r in results:
    od=r['outdir']
    html.append(f'''<article class="card"><div class="body"><div class="num">{r['number']}</div><div class="ko">{r['ko']}</div><div class="en">{r['name']}</div><div class="diffs">''')
    for key,ko,n in diffs:
        img=f'{od}/{key}/artistic-{n}-pixel-edge-overview.png'
        html.append(f'''<section class="diff"><h4>{ko} · {n}조각</h4><div class="stage"><img src="{img}"></div><p class="small">라벨: 조각 1~{n}</p></section>''')
    html.append('</div></div></article>')
html.append('''</div><div class="box"><b>출력 위치:</b> <code>assets/pieces/artistic-difficulties-v1/</code><br><b>manifest:</b> <code>assets/pieces/artistic-difficulties-v1/manifest.json</code></div></body></html>''')
(base/'artistic-difficulties-all-species-review.html').write_text('\n'.join(html),encoding='utf-8')
print('wrote', base/'artistic-difficulties-all-species-review.html', len(results))
