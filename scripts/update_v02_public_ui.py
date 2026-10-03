from pathlib import Path
import re

p = Path('D:/헤르메스 작업/dino-bone-puzzle/index.html')
s = p.read_text(encoding='utf-8')

catalog = """const catalog=[
 ['티라노사우루스','Tyrannosaurus rex','퍼즐','','assets/source-images/packaged-v0.1/01-01-tyrannosaurus-rex.png','theropod'],
 ['트리케라톱스','Triceratops horridus','퍼즐','', 'assets/source-images/packaged-v0.1/02-02-triceratops.png','ceratopsian'],
 ['프로토케라톱스','Protoceratops andrewsi','퍼즐','','assets/source-images/packaged-v0.1/03-03-protoceratops-andrewsi.png','ceratopsian'],
 ['브라키오사우루스','Brachiosaurus altithorax','퍼즐','', 'assets/source-images/packaged-v0.1/04-04-brachiosaurus-altithorax.png','sauropod'],
 ['에드몬토사우루스','Edmontosaurus annectens','퍼즐','', 'assets/source-images/packaged-v0.1/05-05-edmontosaurus-annectens.png','hadrosaur'],
 ['프테라노돈','Pteranodon longiceps','퍼즐','','assets/source-images/packaged-v0.1/06-06-pteranodon.png','pterosaur'],
 ['타르키아','Tarchia tumanovae','퍼즐','', 'assets/source-images/packaged-v0.1/07-07-tarchia-tumanovae.png','tarchia'],
 ['스피노사우루스','Spinosaurus aegyptiacus','퍼즐','','assets/source-images/packaged-v0.1/08-08-spinosaurus-aegyptiacus.png','spinosaur'],
 ['이구아노돈','Iguanodon bernissartensis','퍼즐','','assets/source-images/packaged-v0.1/09-09-iguanodon-bernissartensis.png','dome'],
 ['디플로도쿠스','Diplodocus carnegii','퍼즐','','assets/source-images/packaged-v0.1/10-10-diplodocus-carnegii.png','sauropod-long'],
 ['알로사우루스','Allosaurus jimmadseni','퍼즐','','assets/source-images/packaged-v0.1/11-11-allosaurus-jimmadseni.png','theropod'],
 ['오비랍토르','Oviraptor philoceratops','퍼즐','','assets/source-images/packaged-v0.1/12-12-oviraptor-philoceratops.png','oviraptor'],
 ['파라사우롤로푸스','Parasaurolophus walkeri','퍼즐','','assets/source-images/packaged-v0.1/13-13-parasaurolophus.png','hadrosaur-crest'],
 ['디모르포돈','Dimorphodon macronyx','퍼즐','','assets/source-images/packaged-v0.1/14-14-dimorphodon.png','dimorphodon'],
 ['데이노니쿠스','Deinonychus antirrhopus','퍼즐','', 'assets/source-images/packaged-v0.1/15-15-deinonychus-antirrhopus.png','ostrich'],
 ['아파토사우루스','Apatosaurus louisae','퍼즐','','assets/source-images/packaged-v0.1/16-16-apatosaurus-louisae.png','hadrosaur-helmet']
];"""
s = re.sub(r"const catalog=\[.*?\];", catalog, s, count=1, flags=re.S)

dino_details = """const dinoDetails=[
 {feature:'강력한 턱과 큰 두개골을 가진 백악기 후기의 대형 육식공룡입니다.',ecology:'북아메리카의 강가와 범람원 주변에서 살았으며, 대형 초식공룡을 사냥하거나 사체를 먹었을 가능성이 큽니다.',source:'Wikimedia Commons 계열 골격도 · CC BY-SA 계열 자료 기반'},
 {feature:'세 개의 뿔과 넓은 프릴이 특징인 대표적인 각룡류입니다.',ecology:'낮은 초목과 질긴 식물을 먹던 초식공룡으로, 무리 생활을 했을 가능성이 자주 논의됩니다.',source:'과학카페 쿠아(QUA) 제공 골격 이미지 · CC 표기'},
 {feature:'작은 몸집의 각룡류로, 트리케라톱스와 가까운 계통의 공룡입니다.',ecology:'건조한 환경의 낮은 식물을 먹었고, 튼튼한 부리로 식물을 잘라 먹었을 것으로 봅니다.',source:'Wikimedia Commons Protoceratops 골격도 · CC BY-SA 계열'},
 {feature:'앞다리가 길고 어깨가 높아 목을 높이 든 실루엣이 두드러지는 용각류입니다.',ecology:'높은 나무의 잎과 식물을 먹었을 것으로 추정되는 거대한 초식공룡입니다.',source:'과학카페 쿠아(QUA) 제공 골격 이미지 · CC 표기'},
 {feature:'납작하고 넓은 부리를 가진 하드로사우루스류 공룡입니다.',ecology:'습지와 강가 주변에서 다양한 식물을 먹었고, 많은 화석 자료로 성장과 생활상이 연구됩니다.',source:'Wikimedia Commons 계열 Edmontosaurus 골격도 · CC BY-SA 계열'},
 {feature:'긴 날개와 뒤로 뻗은 볏을 가진 백악기의 대표 익룡입니다.',ecology:'바닷가와 내륙 수역 주변에서 물고기 같은 먹이를 잡아먹었을 가능성이 큽니다.',source:'Wikimedia Commons Pteranodon 골격도 · CC BY-SA 계열'},
 {feature:'두꺼운 갑옷과 꼬리 곤봉을 지닌 안킬로사우루스류 공룡입니다.',ecology:'낮은 식물을 먹는 초식공룡으로, 단단한 몸 장갑이 포식자로부터 몸을 지켰습니다.',source:'Wikimedia Commons / 공개 학술 도판 기반 · CC BY-SA 계열'},
 {feature:'긴 주둥이와 등에 솟은 돛 모양 구조가 특징인 대형 수각류입니다.',ecology:'물가 환경과 관련이 깊으며, 물고기와 육상 먹이를 함께 이용했을 가능성이 논의됩니다.',source:'Wikimedia Commons 및 공개 학술 골격 복원도 · CC BY 계열'},
 {feature:'엄지 가시와 튼튼한 뒷다리로 유명한 고전적인 조각류 공룡입니다.',ecology:'초식성으로, 낮은 식물과 나뭇잎을 먹었고 네 발 또는 두 발 자세를 모두 활용했을 수 있습니다.',source:'Wikimedia Commons Iguanodon 골격도 · CC BY-SA 계열'},
 {feature:'매우 긴 목과 꼬리를 가진 길쭉한 체형의 용각류입니다.',ecology:'넓은 지역을 이동하며 낮거나 중간 높이의 식물을 먹던 대형 초식공룡으로 해석됩니다.',source:'Wikimedia Commons Diplodocus 골격도 · CC BY-SA 계열'},
 {feature:'쥐라기 후기의 날렵한 대형 육식공룡입니다.',ecology:'초식공룡을 사냥하거나 사체를 먹었고, 여러 개체가 같은 지역에서 발견되어 생태 연구가 활발합니다.',source:'Wikimedia Commons Allosaurus 골격도 · CC BY-SA 계열'},
 {feature:'짧은 부리와 가벼운 몸, 긴 뒷다리를 가진 오비랍토르류 공룡입니다.',ecology:'작은 동물, 알, 식물성 먹이 등 다양한 먹이를 이용했을 가능성이 있는 잡식성 공룡입니다.',source:'Wikimedia Commons Oviraptor 골격도 · CC BY-SA 계열'},
 {feature:'뒤로 길게 뻗은 관 모양 볏이 특징인 하드로사우루스류입니다.',ecology:'무리 생활을 했을 가능성이 높고, 볏은 소리 전달이나 시각 신호에 쓰였을 것으로 봅니다.',source:'Wikimedia Commons Parasaurolophus 골격도 · CC BY-SA 계열'},
 {feature:'큰 머리와 긴 꼬리를 가진 초기 익룡입니다.',ecology:'해안과 숲 가장자리 환경에서 작은 척추동물이나 곤충을 먹었을 가능성이 있습니다.',source:'Wikimedia Commons Dimorphodon 골격도 · CC BY-SA 계열'},
 {feature:'낫처럼 휘어진 둘째 발톱과 민첩한 몸으로 유명한 수각류입니다.',ecology:'작고 빠른 먹이를 사냥했을 가능성이 있으며, 깃털을 가진 근연 공룡들과 함께 조류 진화 연구에 중요합니다.',source:'공개 학술 골격도 및 CC 계열 이미지 자료 기반'},
 {feature:'긴 목과 긴 꼬리, 거대한 몸집을 가진 대표적인 용각류입니다.',ecology:'넓은 평원과 숲 가장자리에서 대량의 식물을 먹었고, 긴 목으로 다양한 높이의 식생을 이용했을 것입니다.',source:'Wikimedia Commons Apatosaurus 골격도 · CC BY-SA 계열'}
];"""
# insert after catalog if not present, replace if present
if 'const dinoDetails=' in s:
    s = re.sub(r"const dinoDetails=\[.*?\];", dino_details, s, count=1, flags=re.S)
else:
    s = s.replace(catalog + "\nconst dinoFacts=", catalog + "\n" + dino_details + "\nconst dinoFacts=")

# Static HTML replacements
s = s.replace('<title>Dino-Bone Puzzle · Bone Alpha Outline Edition</title>', '<title>Dino-Bone Puzzle · 공룡 골격 퍼즐</title>')
s = s.replace('</section><section id="grid" class="grid"></section></main>', '</section><section id="grid" class="grid"></section><footer class="site-credit">© 과학카페 쿠아(QUA) · Budher Song</footer></main>')
s = s.replace('<div class="note">현재는 로컬 프로토타입입니다. 공개 배포 전 각 이미지의 라이선스와 출처 표기를 최종 확인해야 합니다.</div>', '<div class="note" id="dinoInfo"></div><footer class="site-credit game-credit">© 과학카페 쿠아(QUA) · Budher Song</footer>')

# CSS additions before </style>
css_add = """
.site-credit{font-size:11px;color:rgba(248,241,223,.72);text-align:center;padding:4px 0 1px}.game-credit{padding-top:5px}.card .sci{font-style:italic;color:#d7ded2;font-size:12px;line-height:1.25}.card .quick{margin-top:4px;color:#aebbad;font-size:11px;line-height:1.32}.detail-box{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:6px}.detail-box div{padding:7px 8px;border-radius:12px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.08)}.detail-box b{display:block;color:#ffe0a0;margin-bottom:2px}.source-line{margin-top:6px;color:#cfd8ca}.source-line b{color:#ffe0a0}.creator-line{margin-top:3px;color:rgba(248,241,223,.75)}
@media(min-width:1280px){.app{max-width:min(1720px,96vw)}.grid{grid-template-columns:repeat(auto-fill,minmax(236px,1fr));gap:12px}.card{min-height:232px}.thumb{height:126px}.game{grid-template-rows:auto minmax(360px,1fr) auto}.tray{max-height:34vh}}
@media(max-width:920px) and (orientation:landscape){.app{max-width:100vw;padding:6px;gap:6px}.top{padding:7px 9px}.logo{width:38px;height:38px}.game{grid-template-rows:auto 1fr auto}.hud{padding:6px}.board-wrap{min-height:0}.tray{min-height:108px;max-height:32vh;overflow:auto}.detail-box{grid-template-columns:1fr 1fr}.intro{padding:10px}.thumb{height:104px}}
@media(max-width:760px){body{overflow:hidden}.grid{grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}.card{min-height:214px}.detail-box{grid-template-columns:1fr}.tray{overflow:auto}.site-credit{text-align:left;padding-left:4px}.game-credit{text-align:center}.card .quick{display:none}}
"""
if '.site-credit{' not in s:
    s = s.replace('\n</style>', css_add + '\n</style>')

# Render/logic replacements
old = "function renderThumb(el){if(!sourceReady)return;const c=document.createElement('canvas');c.width=360;c.height=100;const t=c.getContext('2d');t.fillStyle='#fff';t.fillRect(0,0,c.width,c.height);t.drawImage(sourceCanvas,0,0,955,310,5,6,350,88);t.fillStyle='rgba(181,135,36,.9)';t.font='700 10px system-ui';t.fillText('puzzle image preview',10,94);el.innerHTML='';el.appendChild(c)}"
new = "function renderThumb(el){if(!sourceReady)return;const c=document.createElement('canvas');c.width=360;c.height=100;const t=c.getContext('2d');t.fillStyle='#fff';t.fillRect(0,0,c.width,c.height);t.drawImage(sourceCanvas,0,0,955,310,5,6,350,88);el.innerHTML='';el.appendChild(c)}"
s = s.replace(old, new)

old = "function renderDex(){$('#clearCount').textContent=`도감 ${solvedSet.size}/16`;$('#grid').innerHTML=catalog.map((d,i)=>`<button type=\"button\" class=\"card\" data-i=\"${i}\" id=\"card-${i}\"><span class=\"badge\">${solvedSet.has(i)?'완성':d[2]}</span><div class=\"thumb\" id=\"thumb-${i}\">${dexThumb(d,i)}</div><h3>${d[0]}</h3><p>${d[1]} · ${d[3]}</p></button>`).join('');document.querySelectorAll('.card').forEach(c=>c.onclick=()=>start(+c.dataset.i));if(sourceReady)renderThumb($(`#thumb-${currentIndex}`))}"
new = "function renderDex(){$('#clearCount').textContent=`도감 ${solvedSet.size}/16`;$('#grid').innerHTML=catalog.map((d,i)=>{const info=dinoDetails[i]||{};return `<button type=\"button\" class=\"card\" data-i=\"${i}\" id=\"card-${i}\"><span class=\"badge\">${solvedSet.has(i)?'완성':'퍼즐'}</span><div class=\"thumb\" id=\"thumb-${i}\">${dexThumb(d,i)}</div><h3>${d[0]}</h3><p class=\"sci\">${d[1]}</p><p class=\"quick\">${info.feature||''}</p></button>`}).join('');document.querySelectorAll('.card').forEach(c=>c.onclick=()=>start(+c.dataset.i));if(sourceReady)renderThumb($(`#thumb-${currentIndex}`))}"
s = s.replace(old, new)

old = "function update(){const done=pieces.filter(p=>p.locked).length,total=pieces.length||1,pct=Math.round(done/total*100),d=catalog[currentIndex];$('#stageTitle').textContent=`${d[0]} · ${levels[selectedLevel].label} · ${total}조각 · ${selected?.name||''}`;$('#progressText').textContent=pct+'%';$('#progressBar').style.width=pct+'%';$('#pieceCount').textContent=`${done}/${total}개`}"
new = "function update(){const done=pieces.filter(p=>p.locked).length,total=pieces.length||1,pct=Math.round(done/total*100),d=catalog[currentIndex],info=dinoDetails[currentIndex]||{};$('#stageTitle').textContent=`${d[0]} · ${d[1]} · ${levels[selectedLevel].label} · ${total}조각 · ${selected?.name||''}`;$('#progressText').textContent=pct+'%';$('#progressBar').style.width=pct+'%';$('#pieceCount').textContent=`${done}/${total}개`;const box=$('#dinoInfo');if(box)box.innerHTML=`<div class=\"detail-box\"><div><b>특징</b>${info.feature||''}</div><div><b>먹이와 생활</b>${info.ecology||''}</div></div><div class=\"source-line\"><b>이미지 출처(CC)</b> ${info.source||'CC 계열 공개 이미지 자료'}</div><div class=\"creator-line\">제작: 과학카페 쿠아(QUA) · Budher Song</div>`}"
s = s.replace(old, new)

old = "function clear(){solvedSet.add(currentIndex);localStorage.setItem('dinoOutlineSolved',JSON.stringify([...solvedSet]));const d=catalog[currentIndex],info=dinoFacts[currentIndex]||{fact:'멋진 고생물 퍼즐을 완성했습니다.',praise:'끝까지 집중해서 완성했어요!'};$('#modal h3').textContent=`${d[0]} · ${d[1]}`;$('#dinoFact').textContent=info.fact;$('#praiseText').textContent=info.praise;$('#clearMessage').textContent=`${d[0]} 퍼즐을 완성했습니다.`;$('#clearOverlay').classList.remove('hidden');confetti();fanfare();renderDex()}"
new = "function clear(){solvedSet.add(currentIndex);localStorage.setItem('dinoOutlineSolved',JSON.stringify([...solvedSet]));const d=catalog[currentIndex],info=dinoFacts[currentIndex]||{fact:'멋진 고생물 퍼즐을 완성했습니다.',praise:'끝까지 집중해서 완성했어요!'};$('#modal h3').textContent=`${d[0]} · ${d[1]}`;$('#dinoFact').textContent=info.fact;$('#praiseText').textContent=info.praise;$('#clearMessage').textContent=`${d[0]} 퍼즐을 완성했습니다.`;$('#clearOverlay').classList.remove('hidden');confetti();fanfare();renderDex()}"
s = s.replace(old, new)

# Remove visible debug labels from special source drawing helpers.
s = s.replace("if(currentIndex===11){drawWholeOnly(s,'oviraptor-whole-skeleton')}", "if(currentIndex===11){drawWholeOnly(s,'')}")
s = s.replace("s.fillStyle='rgba(140,80,0,.72)';s.font='700 10px system-ui';s.fillText(label,8,302);", "if(label){s.fillStyle='rgba(140,80,0,.72)';s.font='700 10px system-ui';s.fillText(label,8,302);}")

# Ensure no stale user-facing process terms remain in cards/notes.
for bad in ['측면도만 남긴 로컬 확정 파일','사용자 제공 확정 이미지','사우로르니톨레스테스 폐기','하단 그림만 남긴 로컬 확정 파일','Commons/논문 CC 후보','드라코렉스 폐기 · 정확 종명 대체','컨펌된 측면 골격도','온전한 전체 골격 사용','동종 후보 · 라이선스 원문 확인 필요','코리토사우루스 대체 추천','현재는 로컬 프로토타입입니다. 공개 배포 전 각 이미지의 라이선스와 출처 표기를 최종 확인해야 합니다.','puzzle image preview','oviraptor-whole-skeleton']:
    if bad in s:
        raise SystemExit(f'stale term remained: {bad}')

p.write_text(s, encoding='utf-8')
print('updated public UI', p, 'bytes', len(s.encode('utf-8')))
