# GitHub Pages publication

The approved destination is the existing public `MrScripty/MrScripty` repository. A static-only `gh-pages` branch can publish this portfolio independently of `main`, preserving the existing profile README and its workflow. It requires no application-code merge or new repository.

## Confirmed deployment and remaining verification

GitHub reports a successful Pages deployment of `5c5be2f53129f91fe89843caf0e53559f88655c7` from `gh-pages`:

- Deployment: https://github.com/MrScripty/MrScripty/actions/runs/38175626680
- GitHub-reported public URL: https://mrscripty.github.io/MrScripty/
- Source: `gh-pages`, `/(root)`; public; HTTPS enforced.

The publication environment's outbound proxy rejects `mrscripty.github.io`, including an approved escalated fetch. The web fetch tool also could not access it. Therefore public HTTP content and assets have not been independently verified. Local Chromium QA passed against the exact publication bundle. The current refresh uses approved capture revision `7fc3584`, with original image hashes verified and 1,220 combined portfolio/presentation checks passing. Open the returned URL in an authorized browser, check the desktop and mobile layouts and screenshot dialogs, and verify assets before describing it as publicly browser-verified.

## Publishing source

The settings below describe the existing route, not a request to reconfigure it. Do not republish this new visual revision until appearance review and approval are clear.

In repository **Settings → Pages**, choose **Deploy from a branch**, branch **gh-pages**, folder **/(root)**, then **Save**.

The publication root contains only `index.html`, `styles.css`, `script.js`, `.nojekyll`, the favicon, and the five referenced approved screenshots. Review files, unused Tuldok captures, source notes and local QA logs are excluded.

The project URL reported by Pages is `https://mrscripty.github.io/MrScripty/`. This differs from a user-root site, which would require a separate `mrscripty.github.io` repository.

The supported REST equivalent is `POST /repos/MrScripty/MrScripty/pages` with `{"build_type":"legacy","source":{"branch":"gh-pages","path":"/"}}`. This operation requires the existing credential to have Pages write and Administration write permissions. A permission denial must be resolved by the repository owner; do not work around it with another account, credential, or hosting provider.

Before reporting launch, inspect the Pages deployment commit and actual public URL and verify all local assets. Add the separate Pantograph website link and canonical metadata only after the deployed URL is verified. Until then, existing source links remain authoritative.

Official references:

- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/rest/pages/pages#create-a-github-pages-site

## Prepared source revision

The redesigned portfolio, Chrema overview, original book covers, retained-output lead image, and Eidetic native screenplay/timeline capture are prepared in the source branch only. They are not included in deployed commit `5c5be2f53129f91fe89843caf0e53559f88655c7`. The `gh-pages` branch has not been updated for this visual revision. No merge, new permission, account grant or hosting change is required to review these source changes.
