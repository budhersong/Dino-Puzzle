from pathlib import Path
import re

p = Path('D:/헤르메스 작업/dino-bone-puzzle/index.html')
s = p.read_text(encoding='utf-8')

source_links = """const sourceLinks=[
 '',
 '',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Protoceratops_andrewsi_skeletal.png',
 '',
 '',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Pteranodon_skeletal.jpg',
 '',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Spinosaurus_aegyptiacus_skeletal.jpg',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Iguanodon_Skeletal.svg',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Diplodocus_carnegii_Skeletal.svg',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Allosaurus_jimmadseni_skeletal.png',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Oviraptor_Skeletal.png',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Parasaurolophus_reconstructed_skeleton.png',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Dimorphodon_skeleton.jpg',
 '',
 'https://commons.wikimedia.org/wiki/Special:Redirect/file/Apatosaurus_louisae_skeletal_by_Bricksmashtv.png'
];"""
if 'const sourceLinks=' in s:
    s = re.sub(r"const sourceLinks=\[.*?\];", source_links, s, count=1, flags=re.S)
else:
    s = s.replace('const dinoFacts=[', source_links + '\nconst dinoFacts=[')

# Static copyright footer link
s = s.replace('© 과학카페 쿠아(QUA) · Budher Song</footer>', '<a href="https://sciencecafekorea.com" target="_blank" rel="noopener">© 과학카페 쿠아(QUA) · Budher Song</a></footer>')

# CSS for links, once
css = ".site-credit a,.creator-line a,.source-line a{color:inherit;text-decoration:underline;text-decoration-color:rgba(255,224,160,.55);text-underline-offset:3px}.source-line a:hover,.site-credit a:hover,.creator-line a:hover{color:#ffe0a0}"
if '.site-credit a,.creator-line a,.source-line a' not in s:
    s = s.replace('\n@media(min-width:1280px)', css + '\n@media(min-width:1280px)')

old = "const box=$('#dinoInfo');if(box)box.innerHTML=`<div class=\"detail-box\"><div><b>특징</b>${info.feature||''}</div><div><b>먹이와 생활</b>${info.ecology||''}</div></div><div class=\"source-line\"><b>이미지 출처(CC)</b> ${info.source||'CC 계열 공개 이미지 자료'}</div><div class=\"creator-line\">제작: 과학카페 쿠아(QUA) · Budher Song</div>`}"
new = "const box=$('#dinoInfo');if(box){const srcText=info.source||'CC 계열 공개 이미지 자료',srcUrl=sourceLinks[currentIndex]||'';const srcHtml=srcUrl?`<a href=\"${srcUrl}\" target=\"_blank\" rel=\"noopener\">${srcText}</a>`:srcText;box.innerHTML=`<div class=\"detail-box\"><div><b>특징</b>${info.feature||''}</div><div><b>먹이와 생활</b>${info.ecology||''}</div></div><div class=\"source-line\"><b>이미지 출처(CC)</b> ${srcHtml}</div><div class=\"creator-line\">제작: <a href=\"https://sciencecafekorea.com\" target=\"_blank\" rel=\"noopener\">과학카페 쿠아(QUA) · Budher Song</a></div>`}}"
if old not in s:
    raise SystemExit('update source block target not found')
s = s.replace(old, new)

p.write_text(s, encoding='utf-8')
print('linked credits and available source URLs')
