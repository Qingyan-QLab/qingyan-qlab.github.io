# Q-lab official website

Official static website for the [Qingyan-QLab](https://github.com/Qingyan-QLab) organization, intended for **https://qlab-ai.org/**.

The site connects four research pillars: **world modeling, embodied learning, understanding minds, and reliable coexistence**. These preserve the original scope of geometry, physics, embodiment, continual learning, mental models, and robots in human society. Verifiability is integrated into each pillar and the whole system. Reliability is a necessary condition for the vision of robots integrating into every aspect of human society. The site describes verifiable, measurable, highly reliable physical AI systems; specific metrics will be defined in technical research for particular tasks, operating environments, and failure types. Research descriptions express interests and aspirations, rather than claims of completed results.

## Local preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/. No framework, package installation, or build step is required. Chinese is the default language; `?lang=en` opens English. The language button saves the visitor's preference locally.

## Edit

- `index.html`: the complete single-page site: physical AI introduction, vision, and four principles, with Chinese and English text in `data-zh` / `data-en` attributes.
- `style.css`: responsive layout and visual design.
- `main.js`: language selection and localized metadata.
- `assets/manifold.svg`: original mathematical illustration, regenerated with `python3 scripts/generate-art.py`.

## Publishing

Host with GitHub Pages, from the `main` branch and repository root. A push updates the site. GitHub Pages is available free for public organization repositories. All public site assets are self-contained; there are no external fonts, analytics, trackers, forms, or runtime dependencies.

The domain stays registered and managed at GoDaddy. DNS records and current deployment state are documented in `DEPLOYMENT.md` once configured. Set the custom domain in GitHub Pages before pointing DNS to GitHub. HTTPS enforcement becomes available after DNS validation and certificate issuance.

## Content provenance

- Research scope and domain: supplied by the site owner on 2026-10-29.
- Organization account and mission: verified against https://github.com/Qingyan-QLab on 2026-10-29.
- A concise single page, an explanation directly following the headline, four principles, and removal of an undefined reliability percentage: requested by the site owner on 2026-10-30. Earlier separate pages and their navigation links have been removed.
- Editorial reference: https://amilabs.xyz/ (clear goals and concrete explanations; no organization-specific claims or copy reused).
- Remaining site copy and mathematical artwork: created for this website.

No private repositories, internal company documents, unpublished results, or personal details are included in the site.
