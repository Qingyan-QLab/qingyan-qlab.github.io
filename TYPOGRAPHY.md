# Q-lab typography

The typography follows the site's concise, text-only format. Chinese and English share a font family lineage and layout, while their typesetting values are tuned separately.

## References

- [W3C Chinese Layout Requirements](https://www.w3.org/TR/clreq/): normal Han glyph spacing, punctuation placement, and Chinese line breaking. This is a Group Note Draft, not a mandatory website standard. It also permits tighter spacing in display typography; this site deliberately uses natural Chinese spacing.
- [U.S. Web Design System typography](https://designsystem.digital.gov/components/typography/): legible body size, alignment, line length, leading, and grouping through whitespace. Its Latin character-count guidance is not applied to Chinese as a Han-character quota.

## Site choices

| Element | Chinese | English |
| --- | --- | --- |
| Main headline, desktop | 56px, weight 500, 1.35 line height, normal tracking | 60px, weight 500, 1.12 line height, −0.018em tracking |
| Introduction | 20px / 1.8, at most 36em | 22px / 1.55, at most 62ch |
| Supporting paragraph | 18px / 1.8, at most 40em | 20px / 1.6, at most 68ch |
| Four principle titles | 22px / 1.5, weight 500 | 24px / 1.3, weight 500 |
| Four principle paragraphs | 17px / 1.8 | 18px / 1.6 |

These values are editorial choices for this page, not numbers prescribed by W3C. Sizes use rem units and fluid scaling so browser text sizing remains useful. Auxiliary text is smaller than prose, with sufficient contrast and comfortable interactive targets.

The short Chinese headline stays on one line when there is room. Its two clauses can flow onto separate lines on narrow screens without breaking a phrase unnecessarily. English keeps the two sentences as separate lines at desktop width. Neither language uses a fixed-height text container or clipped text.

The page uses a 960px maximum width, left alignment, and a two-column principles grid that becomes one column on phones. The fonts are [self-hosted OFL subsets](assets/fonts/README.md), totaling approximately 77 KiB. No external font request is needed. The current text coverage and byte sizes are recorded in `assets/fonts/manifest.json`.
