# Q-lab official website

Official static website for the [Qingyan-QLab](https://github.com/Qingyan-QLab) organization, intended for **https://qlab-ai.org/**.

The site introduces six user-confirmed research directions: geometry, the physical world, embodied intelligence, continual learning, mental models, and robots that integrate seamlessly into human society. Research descriptions express interests and aspirations, rather than claims of completed results.

## Local preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/. No framework, package installation, or build step is required. Chinese is the default language; `?lang=en` opens English. The language button saves the visitor's preference locally.

## Edit

- `index.html`: content, semantic markup, and both languages in `data-zh` / `data-en` attributes.
- `style.css`: responsive layout and visual design.
- `main.js`: language selection and accessible research tabs.
- `assets/manifold.svg`: original mathematical illustration, regenerated with `python3 scripts/generate-art.py`.

## Publishing

Host with GitHub Pages, from the `main` branch and repository root. A push updates the site. GitHub Pages is available free for public organization repositories. All public site assets are self-contained; there are no external fonts, analytics, trackers, forms, or runtime dependencies.

The domain stays registered and managed at GoDaddy. DNS records and current deployment state are documented in `DEPLOYMENT.md` once configured. Set the custom domain in GitHub Pages before pointing DNS to GitHub. HTTPS enforcement becomes available after DNS validation and certificate issuance.

## Content provenance

- Research scope and domain: supplied by the site owner on 2026-10-29.
- Organization account and mission: verified against https://github.com/Qingyan-QLab on 2026-10-29.
- Remaining site copy and mathematical artwork: created for this website.

No private repositories, internal company documents, unpublished results, or personal details are included in the site.
