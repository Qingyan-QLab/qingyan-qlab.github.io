# Q-lab web fonts

The site uses self-hosted subsets of Adobe's **Source Han Serif CN (思源宋体)** for the main content (headlines and prose), **Source Han Sans CN (思源黑体)** for Chinese interface text, and **Source Sans 3** for Latin interface text. All are licensed under SIL OFL 1.1; the unmodified upstream licenses are included in this directory.

These are modified, reduced-character-set fonts. Their internal family names are **QLab Serif**, **QLab Sans CN**, and **QLab Sans Latin** to respect the upstream Reserved Font Name. This does not imply that Q-lab designed the original typefaces. Copyright and license metadata remain in each font.

- Main-content source: [Adobe Source Han Serif](https://github.com/adobe-fonts/source-han-serif), release commit `7889f11bf31170b5d092a083b357c8c8130f89e0`. Its built-in Latin is derived from Source Serif and adjusted for CJK use, as documented in the [official ReadMe](https://github.com/adobe-fonts/source-han-serif/blob/release/SourceHanSerifReadMe.pdf). The main-content subset covers the full bilingual site text and weights 400–650. It is preloaded to prioritize its first render.
- Chinese interface source: [Adobe Source Han Sans](https://github.com/adobe-fonts/source-han-sans), release commit `a4f7cf94edfb9d7ffbdfc4841de276358bd7e0f2`.
- Latin interface source: [Adobe Source Sans](https://github.com/adobe-fonts/source-sans), release commit `87b37a2daaed80fcb8e8ccb0085c4d72ddade12e`.
- The interface subsets keep upright weights 400–600 and the site's current Han characters. Latin includes basic Western characters and the site's punctuation. New Han characters fall back to local fonts until the subset is regenerated.
- `manifest.json` records the exact upstream URLs, source and output SHA-256 hashes, sizes, and character counts.

## Updating copy

After changing the HTML text, regenerate the fonts:

```sh
python3 -m venv .artifacts/font-env
.artifacts/font-env/bin/python -m pip install 'fonttools[woff]==4.61.1'
.artifacts/font-env/bin/python scripts/subset-fonts.py
```

The script caches pinned upstream inputs in ignored `.artifacts/font-sources`, updates the font cache keys in `style.css`, and refreshes the stylesheet cache key in `index.html`. Run from a checked-out repository. This is an authoring step only; the deployed website has no build or runtime dependency.
