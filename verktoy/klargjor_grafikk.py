"""Prepare Tuktuk graphics: key out magenta, split sheets, crop, scale, save PNG/JPG into grafikk/spill/."""
import sys, os, json
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = sys.argv[1]
OUT = os.path.join(SRC, 'spill')
os.makedirs(OUT, exist_ok=True)

def load(name):
    return Image.open(os.path.join(SRC, name)).convert('RGB')

def key(img):
    a = np.asarray(img).astype(np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = np.minimum(r, b) - g
    bg = (r > 160) & (b > 160) & (g < 130) & (m > 100)
    edge = (~bg) & (r > 120) & (b > 120) & (m > 50)
    alpha = np.where(bg, 0, 255).astype(np.uint8)
    alpha[edge] = 110
    # despill purple fringe
    sp = np.clip(m - 20, 0, None) * 0.8
    sp = np.where(bg, 0, sp)
    r2 = np.clip(r - sp, 0, 255); b2 = np.clip(b - sp, 0, 255)
    # remove isolated speckles in the background
    solid = ndimage.binary_opening(alpha > 128, iterations=2)
    alpha = np.where(solid | edge, alpha, 0).astype(np.uint8)
    out = np.dstack([r2, g, b2, alpha]).astype(np.uint8)
    return Image.fromarray(out, 'RGBA')

def parts(rgba, min_frac=0.01, merge=18):
    al = np.asarray(rgba)[..., 3] > 128
    lab, n = ndimage.label(ndimage.binary_dilation(al, iterations=merge))
    boxes = []
    for sl in ndimage.find_objects(lab):
        h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
        if (al[sl].sum()) > min_frac * al.size:
            boxes.append((sl[1].start, sl[0].start, sl[1].stop, sl[0].stop))
    return boxes

def crop(rgba, box=None):
    if box is None:
        al = np.asarray(rgba)[..., 3] > 128
        ys, xs = np.where(al)
        box = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
    return rgba.crop(box)

def fit(im, maxdim):
    s = maxdim / max(im.size)
    if s < 1:
        im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    if im.mode == 'RGBA':
        a = np.asarray(im).copy()
        a[..., 3] = np.where(a[..., 3] > 100, 255, 0)
        im = Image.fromarray(a, 'RGBA')
    return im

info = {}
def save(im, name):
    p = os.path.join(OUT, name)
    if name.endswith('.jpg'):
        im.convert('RGB').save(p, quality=86, optimize=True)
    else:
        im.save(p, optimize=True)
    info[name] = list(im.size)

def largest(rgba):
    """Keep only the biggest blob (drops exhaust puffs and neighbours' edges)."""
    a = np.asarray(rgba).copy()
    al = a[..., 3] > 128
    lab, n = ndimage.label(ndimage.binary_dilation(al, iterations=6))
    if n > 1:
        sizes = ndimage.sum(al, lab, range(1, n + 1))
        keep = lab == (int(np.argmax(sizes)) + 1)
        a[..., 3] = np.where(keep, a[..., 3], 0)
    return Image.fromarray(a, 'RGBA')

# single sprites
singles = {
    'arve-sittende-telefon.jpg': ('arve-sitter.png', 300),
    'andre-sittende.jpg': ('andre-sitter.png', 300),
    'arve-staaende.jpg': ('arve-staar.png', 260),
    'andre-staaende.jpg': ('andre-staar.png', 260),
    'somchai-staaende.jpg': ('somchai-staar.png', 260),
    'tempel.jpg': ('tempel.png', 330),
    'stolpe.jpg': ('stolpe.png', 300),
    'gatekjokken.jpg': ('gatekjokken.png', 240),
    'minimarked.jpg': ('minimarked.png', 300),
    'paalehus.jpg': ('paalehus.png', 260),
    'aandehus.jpg': ('aandehus.png', 160),
    'veiskilt.jpg': ('veiskilt.png', 256),
    'port.jpg': ('port.png', 420),
    'elefant.jpg': ('elefant.png', 240),
    'munker.jpg': ('munker.png', 200),
    'hund.jpg': ('hund.png', 140),
}
for src, (dst, md) in singles.items():
    k = key(load(src))
    if dst in ('stolpe.png',): k = largest(k)
    save(fit(crop(k), md), dst)

# sheets
def sheet(src, prefix, md, cols, rows=1):
    k = key(load(src))
    cw, ch = k.width / cols, k.height / rows
    names = []
    for r in range(rows):
        for c in range(cols):
            cell = k.crop((round(c * cw), round(r * ch), round((c + 1) * cw), round((r + 1) * ch)))
            n = f'{prefix}-{r * cols + c + 1}.png'
            save(fit(crop(largest(cell)), md), n)
            names.append(n)
    return names

sheets = {
    'tuktuk': sheet('tuktuk-bak-ark.jpg', 'tuktuk-bak', 288, 2),
    'andre_tuk': sheet('tuktuk-annen-ark.jpg', 'tuktuk-annen', 200, 2, 2),
    'scooter': sheet('scooter-ark.jpg', 'scooter', 120, 3),
    'butikkhus': sheet('butikkhus-ark.jpg', 'butikkhus', 260, 3),
}

# backgrounds (16:10 crops)
def bg16x10(src, dst, w=960):
    im = load(src)
    tw = im.height * 16 / 10
    if tw <= im.width:
        x0 = (im.width - tw) / 2
        im = im.crop((round(x0), 0, round(x0 + tw), im.height))
    else:
        th = im.width * 10 / 16
        y0 = (im.height - th) / 2
        im = im.crop((0, round(y0), im.width, round(y0 + th)))
    save(im.resize((w, w * 10 // 16), Image.LANCZOS), dst)

bg16x10('verksted-kaffe-2-hund.jpg', 'bg-verksted.jpg')
bg16x10('bg-gate.jpg', 'bg-gate.jpg')
# skyline: drop the hazy ground below the buildings, mirror to make it seamless
sk = load('skyline.jpg'); sk = sk.crop((0, 0, sk.width, round(sk.height * .86)))
sk = sk.resize((480, round(sk.height * 480 / sk.width)), Image.LANCZOS)
wide = Image.new('RGB', (960, sk.height)); wide.paste(sk, (0, 0)); wide.paste(sk.transpose(Image.FLIP_LEFT_RIGHT), (480, 0))
save(wide, 'skyline.jpg')
# title poster (portrait, shown full screen on the phone)
tp = load('bg-tittel.jpg'); save(tp.resize((720, round(tp.height * 720 / tp.width)), Image.LANCZOS), 'tittel.jpg')

print(json.dumps({'sheets': sheets, 'sizes': info}, indent=1))
