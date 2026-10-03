from pathlib import Path
from PIL import Image, ImageDraw

base = Path('D:/헤르메스 작업/dino-bone-puzzle')
items = {
    '09-09-iguanodon-bernissartensis.png': 'iguanodon',
    '10-10-diplodocus-carnegii.png': 'diplodocus',
    '15-15-deinonychus-antirrhopus.png': 'deinonychus',
}
root = base / 'assets/source-images/packaged-v0.1'
backup = base / 'assets/source-images/packaged-v0.1-before-bottom-clean'
backup.mkdir(parents=True, exist_ok=True)

for fname, kind in items.items():
    p = root / fname
    if not p.exists():
        raise FileNotFoundError(p)
    b = backup / fname
    if not b.exists():
        b.write_bytes(p.read_bytes())
    im = Image.open(p).convert('RGBA')
    w, h = im.size
    px = im.load()
    # 1) Remove full-width gray bars in lower area.
    for y in range(int(h * 0.58), h):
        gray_count = 0
        for x in range(w):
            r, g, b_, a = px[x, y]
            if a > 20 and abs(r - g) < 4 and abs(g - b_) < 4 and 165 <= r <= 225:
                gray_count += 1
        # full horizontal gray ruler/bar artifact
        if gray_count > w * 0.45:
            for yy in range(max(0, y - 2), min(h, y + 3)):
                for x in range(w):
                    r, g, b_, a = px[x, yy]
                    if a > 20 and abs(r - g) < 6 and abs(g - b_) < 6 and 150 <= r <= 235:
                        px[x, yy] = (255, 255, 255, 255)
    draw = ImageDraw.Draw(im)
    if kind == 'diplodocus':
        # Remove black scale bar / tiny line remnants and right-side legend, below the actual body line.
        # Coordinates are after normalized packaged crop (2200x575).
        draw.rectangle((0, int(h * 0.80), w, h), fill=(255, 255, 255, 255))  # gray bottom bar area
        draw.rectangle((360, int(h * 0.50), 880, int(h * 0.62)), fill=(255, 255, 255, 255))  # scale bar
        draw.rectangle((0, int(h * 0.48), 180, int(h * 0.62)), fill=(255, 255, 255, 255))  # small left slash
        draw.rectangle((1640, int(h * 0.46), 1900, int(h * 0.66)), fill=(255, 255, 255, 255))  # legend text/squares
    elif kind == 'deinonychus':
        # Remove lower horizontal baseline and thick vertical black marker, preserve legs above.
        # Baseline is at the very bottom area; vertical marker is right of the feet.
        draw.rectangle((0, int(h * 0.90), w, h), fill=(255, 255, 255, 255))
        draw.rectangle((1780, int(h * 0.70), 1845, h), fill=(255, 255, 255, 255))
    elif kind == 'iguanodon':
        # Remove bottom gray bar only, below feet.
        draw.rectangle((0, int(h * 0.84), w, h), fill=(255, 255, 255, 255))
    im.save(p)
    print('cleaned', p, im.size)
