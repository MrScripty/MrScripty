# GitHub Pages publication

The approved destination is the existing public `MrScripty/MrScripty` repository. A static-only `gh-pages` branch can publish this portfolio independently of `main`, preserving the existing profile README and its workflow. It requires no application-code merge or new repository.

## Publishing source

In repository **Settings → Pages**, choose **Deploy from a branch**, branch **gh-pages**, folder **/(root)**, then **Save**.

The publication root contains only `index.html`, `styles.css`, `script.js`, `.nojekyll`, the favicon, and the five referenced approved screenshots. Review files, unused Tuldok captures, source notes and local QA logs are excluded.

The expected project URL is `https://mrscripty.github.io/MrScripty/`; it must not be described as live until the Pages build and returned URL are verified. This differs from a user-root site, which would require a separate `mrscripty.github.io` repository.

The supported REST equivalent is `POST /repos/MrScripty/MrScripty/pages` with `{"build_type":"legacy","source":{"branch":"gh-pages","path":"/"}}`. This operation requires the existing credential to have Pages write and Administration write permissions. A permission denial must be resolved by the repository owner; do not work around it with another account, credential, or hosting provider.

Before reporting launch, inspect the Pages deployment commit and actual public URL and verify all local assets. Add the separate Pantograph website link and canonical metadata only after the deployed URL is verified. Until then, existing source links remain authoritative.

Official references:

- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/rest/pages/pages#create-a-github-pages-site
