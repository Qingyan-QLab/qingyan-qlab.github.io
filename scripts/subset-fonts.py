#!/usr/bin/env python3
"""Regenerate self-hosted OFL font subsets after editing the site's copy.
Requires fonttools[woff]==4.61.1. Sources are pinned to upstream commits.
"""
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.request import urlretrieve
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.artifacts/font-sources'
OUT = ROOT / 'assets/fonts'
SOURCES = {
    'cn': ('source-han-sans-cn.woff2', 'https://raw.githubusercontent.com/adobe-fonts/source-han-sans/a4f7cf94edfb9d7ffbdfc4841de276358bd7e0f2/Variable/WOFF2/TTF/Subset/SourceHanSansCN-VF.ttf.woff2'),
    'latin': ('source-sans-3.woff2', 'https://raw.githubusercontent.com/adobe-fonts/source-sans/87b37a2daaed80fcb8e8ccb0085c4d72ddade12e/WOFF2/VF/SourceSans3VF-Upright.ttf.woff2'),
}

class Copy(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)
    def handle_starttag(self, tag, attrs):
        self.parts.extend(value for key, value in attrs if value and (key.startswith('data-') or key in ('aria-label', 'alt', 'content')))

copy = Copy()
copy.feed((ROOT / 'index.html').read_text())
# Include the language switch's dynamically assigned aria-label.
codepoints = {ord(char) for char in ''.join(copy.parts) + '切换至中文Switch to English'}
CACHE.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)
css = (ROOT / 'style.css').read_text()
manifest = {}
for kind, (filename, url) in SOURCES.items():
    path = CACHE / filename
    if not path.exists():
        urlretrieve(url, path)
    font = TTFont(path, recalcTimestamp=False)
    cmap = font.getBestCmap()
    # Keep normal Latin, numbers, and punctuation; Han is limited to site copy.
    wanted = (set(range(0x20, 0x100)) | {cp for cp in codepoints if cp < 0x3000}) if kind == 'latin' else {cp for cp in codepoints if cp >= 0x3000}
    available = wanted & set(cmap)
    missing = wanted - set(cmap)
    if kind == 'cn' and missing:
        raise ValueError(f'Missing Han glyphs: {sorted(missing)}')
    options = subset.Options()
    options.layout_features = ['*']
    options.name_IDs = ['*']
    options.name_languages = ['*']
    options.recalc_timestamp = False
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=available)
    subsetter.subset(font)
    font = instantiateVariableFont(font, {'wght': (400, 600)}, inplace=True)
    family = 'QLab Sans CN' if kind == 'cn' else 'QLab Sans Latin'
    psname = family.replace(' ', '')
    # OFL reserved-name compliance: rename modified subsets, preserve copyright/license.
    replacements = {1: family, 3: f'{psname}-Subset-1.0', 4: family, 6: psname, 16: family, 21: family, 25: psname}
    for record in font['name'].names:
        if record.nameID in replacements:
            record.string = replacements[record.nameID].encode(record.getEncoding())
    for record in font['fvar'].instances:
        if record.postscriptNameID != 0xffff:
            for name in font['name'].names:
                if name.nameID == record.postscriptNameID:
                    name.string = f'{psname}-{int(record.coordinates["wght"])}'.encode(name.getEncoding())
    font.flavor = 'woff2'
    target = OUT / f'qlab-sans-{kind}.woff2'
    font.save(target)
    digest = sha256(target.read_bytes()).hexdigest()
    css = re.sub(rf'assets/fonts/qlab-sans-{kind}\.woff2(?:\?v=[a-f0-9]+)?', f'assets/fonts/qlab-sans-{kind}.woff2?v={digest[:12]}', css)
    manifest[kind] = {'source': url, 'source_sha256': sha256(path.read_bytes()).hexdigest(), 'subset_sha256': digest, 'bytes': target.stat().st_size, 'glyphs': len(available)}
    print(f'{target.name}: {target.stat().st_size:,} bytes; {len(available)} codepoints')
(ROOT / 'style.css').write_text(css)
# Refresh CSS URL for browsers that have cached a previous edition.
html = (ROOT / 'index.html').read_text()
html = re.sub(r'style\.css\?v=[a-f0-9]+', f'style.css?v={sha256(css.encode()).hexdigest()[:12]}', html)
(ROOT / 'index.html').write_text(html)
import json
(OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
