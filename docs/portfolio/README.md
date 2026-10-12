# Puma / Jeremy Bayley portfolio

Buildless, self-contained portfolio for the existing GitHub Pages project site. The approved source `83b67e99cb52c17af8eb42b8900ebadc81377569` is deployed as `fe30267e0c99c6cc19b9d5fd35208823cc93a678`. The newer presentation refinements in this branch are for review and are not deployed. See [deployment evidence](DEPLOYMENT.md).

## Preview and verify

Serve this directory with `python3 -m http.server 8080 --bind 127.0.0.1`, then open the local URL. All runtime assets are local; external requests occur only when following links.

```sh
python3 tools/verify.py
node --check script.js
python3 tools/browser_check.py
python3 tools/gallery_check.py
python3 tools/refinement_check.py
```

Browser checks require an existing Playwright installation and Chromium. Run them against the intended public source, excluding unrelated local drafts. [Validation](VALIDATION.md) records the four tested widths, keyboard/history behavior and real touch gestures.

## Current presentation

- Pumas Library, Pantograph and Chrema introduce models, workflows and agents.
- Memory and context groups Tuldok, Eidetic, Whip Docs and Coding Standards in separate rows.
- Rheon and Kenoma form the physics research section. Rheon's native interface and separate Surrogate Lab remain distinct; its approximate eightfold result describes the tested fixed-box CPU workload.
- The three existing books retain their original covers and attribution. Cooking the Cat retains only its approved short description. The genuine owner-supplied Lanternwake image appears below the books.
- Four manual galleries preserve complete image proportions and full-size viewing. Overlay arrows support hover, focus, touch, keyboard and swipes; no-JavaScript links remain usable.
- Eleven code projects have capability tags. Twelve separate language bars, including an independent Surrogate Lab bar, use GitHub byte proportions and GitHub Linguist colors. Hover, focus or tap exposes the percentages. [The data](assets/language-stats.json) records source URLs, timestamps, bytes, exact proportions and the pinned color source.
- The hero uses Local AI / Data provenance / Observability. Social links retain their destinations and accessible names, with standard GitHub and LinkedIn icons.
- Scope dropdowns and per-project status badges are removed. Required [image and icon credits](image-credits.html) remain available separately.

Edit `index.html`, `styles.css` and `script.js`; then regenerate content-versioned CSS/JS with `tools/version_assets.py` and verify. Keep `image-credits.html` on the same versioned stylesheet. Preserve original image bytes and provenance in `assets/`. Review-only documents, QA screenshots, unused assets and local logs do not belong in a deployment bundle.

The root profile README is maintained independently. This branch does not merge application code, add workflows, change account permissions or publish automatically.
