# Hosting and domain

Configured on 2026-10-29 for the Q-lab organization.

- Provider: GitHub Pages, free hosting for a public organization repository.
- Repository: https://github.com/Qingyan-QLab/qingyan-qlab.github.io
- Canonical domain: https://qlab-ai.org/
- Alternative domain: https://www.qlab-ai.org/ redirects to the canonical domain.
- Publishing source: `main`, repository root (`/`), no build dependencies.
- Domain registration and DNS provider: GoDaddy.
- Nameservers: `ns23.domaincontrol.com`, `ns24.domaincontrol.com`.

## DNS records

| Type | Name | Value | TTL |
| --- | --- | --- | --- |
| A | @ | 185.199.108.153 | 600 seconds |
| A | @ | 185.199.109.153 | 600 seconds |
| A | @ | 185.199.110.153 | 600 seconds |
| A | @ | 185.199.111.153 | 600 seconds |
| CNAME | www | qingyan-qlab.github.io | 1 hour |

The GoDaddy parking A record was replaced. Existing nameservers, SOA, `_domainconnect`, and `_dmarc` records were preserved. No email service was configured by this deployment.

## Publish an update

Edit the static files, preview them locally, and push to `main`. GitHub Pages automatically builds and publishes the updated repository. Keep the root `CNAME` file set to `qlab-ai.org`.

Check publication and certificate state:

```sh
gh api repos/Qingyan-QLab/qingyan-qlab.github.io/pages
gh api repos/Qingyan-QLab/qingyan-qlab.github.io/pages/builds/latest
curl -I https://qlab-ai.org/
```

## Verification

- Desktop layout and Chinese/English switching checked in a browser.
- Mobile layouts checked at 390 px and 320 px; no horizontal overflow.
- Research tabs checked by click and keyboard; research details expand/collapse.
- Internal links, local assets, unique IDs, SVG/XML validity, and JavaScript syntax checked.
- Public DNS answers checked against the four GitHub Pages A records and the `www` CNAME.
- The custom domain serves the website, including the explicitly labeled 99.9999% reliability research goal.
- HTTPS certificate approved for `qlab-ai.org` and `www.qlab-ai.org`; certificate verification succeeds.
- HTTPS enforcement enabled; HTTP redirects to HTTPS, and HTTPS `www` redirects to the canonical domain.
- Deployed HTML, CSS, JavaScript, illustration, favicon, and CNAME checked against local source bytes.

Reference: [GitHub Pages custom-domain configuration](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
