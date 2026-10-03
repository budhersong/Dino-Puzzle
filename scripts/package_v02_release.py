from pathlib import Path
import base64, re, json, shutil, zipfile

base = Path('D:/헤르메스 작업/dino-bone-puzzle')
release = base / 'releases'
snap = release / 'v0.2-prototype'
standalone = release / 'dino-bone-puzzle-v0.2-standalone.html'
zip_path = release / 'dino-bone-puzzle-v0.2-prototype.zip'

s = (base / 'index.html').read_text(encoding='utf-8')
manifest = json.load(open(base / 'assets/pieces/artistic-difficulties-v1/manifest.json', encoding='utf-8'))
path_to_data = {}
for r in manifest['results']:
    rel = f"assets/source-images/packaged-v0.1/{int(r['number']):02d}-{r['slug']}.png"
    path_to_data[rel] = 'data:image/png;base64,' + base64.b64encode((base / rel).read_bytes()).decode('ascii')
first = manifest['results'][0]
first_rel = f"assets/source-images/packaged-v0.1/{int(first['number']):02d}-{first['slug']}.png"
s = re.sub(r"const IMAGE_URL='[^']+';", "const IMAGE_URL='" + path_to_data[first_rel] + "';", s)
for rel, data in path_to_data.items():
    s = s.replace("'" + rel + "'", "'" + data + "'")

snap.mkdir(parents=True, exist_ok=True)
(snap / 'index.html').write_text(s, encoding='utf-8')
standalone.write_text(s, encoding='utf-8')

for rel in ['assets/source-images/packaged-v0.1', 'assets/pieces/artistic-difficulties-v1']:
    src = base / rel
    dst = snap / rel
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

for f in [
    'PROTOTYPE-V0.2-LOCK.md', 'PROTOTYPE-V0.1-LOCK.md',
    'ARTISTIC-PUZZLE-CUT-STANDARD.md', 'FINAL-LINEUP-LOCK.md',
    'final-lineup-lock.json', 'artistic-difficulties-all-species-review.html',
    'apatosaurus-head-foot-final-check-2.png', 'deinonychus-final-no-marker-check.png'
]:
    p = base / f
    if p.exists():
        shutil.copy2(p, snap / p.name)

for f in [
    'scripts/make_artistic_all_difficulties_blobs.py',
    'scripts/build_artistic_difficulties_review.py',
    'scripts/clean_packaged_bottom_artifacts.py',
    'scripts/update_v02_public_ui.py',
    'scripts/link_v02_credits.py',
    'scripts/package_v02_release.py'
]:
    p = base / f
    if p.exists():
        dest = snap / f
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)

meta = {
    'version': 'v0.2-prototype',
    'saved_at': '2026-09-29 KST',
    'status': 'public-facing UI cleaned; Korean/scientific names shown; dino detail text/source/creator/responsive layout added',
    'package_mode': 'standalone HTML embeds 16 cleaned PNG images as base64',
    'difficulty_piece_counts': {'easy': 6, 'normal': 12, 'hard': 20},
    'public_ui': {
        'main_cards': 'Korean name + scientific name + short feature',
        'game_detail': 'controls preserved; feature/ecology/source/creator shown',
        'creator': '과학카페 쿠아(QUA) · Budher Song'
    },
    'validation': {'script_node_check': 'passed before packaging', 'stale_process_text': 'not found'}
}
(snap / 'VERSION.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in snap.rglob('*'):
        if p.is_file():
            z.write(p, p.relative_to(snap.parent))
    z.write(standalone, standalone.name)

bad = ['측면도만 남긴','로컬 확정','로컬 프로토타입','공개 배포 전','라이선스 원문','폐기','후보','puzzle image preview','oviraptor-whole','컨펌','사용자 제공 확정','하단 그림만']
result = {
    'standalone_size': standalone.stat().st_size,
    'zip_size': zip_path.stat().st_size,
    'snapshot_files': sum(1 for p in snap.rglob('*') if p.is_file()),
    'stale_terms': [x for x in bad if x in s],
    'creator_present': ('과학카페 쿠아(QUA)' in s and 'Budher Song' in s),
    'embedded_images': s.count('data:image/png;base64,')
}
print(json.dumps(result, ensure_ascii=False, indent=2))
