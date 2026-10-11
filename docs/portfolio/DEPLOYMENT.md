# Optional GitHub Pages deployment

Committing this source does not enable website hosting. The site is not deployed. Obtain approval for the hosting destination and publication before taking these steps.

## Recommended destination

A GitHub user site uses a repository named `mrscripty.github.io`, giving the root address `https://mrscripty.github.io/`. This is a proposed destination, not a verified live website. A project repository is also possible; all local paths in this source are relative.

## Once publication is approved

1. Create or choose the approved repository, preserving any existing files.
2. Put `index.html`, `styles.css`, `script.js`, `.nojekyll`, and the required `assets/` files at the publishing root.
3. In repository Settings → Pages, select “Deploy from a branch,” the approved branch, and “/(root).”
4. Save the publishing source. Inspect the Pages workflow and confirm its deployment uses the intended commit.
5. Open the exact URL returned by Pages and verify the site and local assets. Only then describe that address as live.

Do not publish the `review/` directory. It is ignored. Keep source/provenance documents in the repository if desired, but review them as public content. No private project data, credentials, contact address, or internal coordination material belongs in the deployed bundle.

## Before launch

- Review the biography, project copy, and public contact links.
- Complete browser QA; see `VALIDATION.md`.
- Replace architecture panels only with verified running-app captures and accurate captions.
- Confirm status of screenshot source PRs and any newer application changes.
- Link the separate Pantograph website only after its URL is verified.
- Add a canonical URL and social-preview image for the actual destination.

Official references, checked 2026-10-11:

- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
