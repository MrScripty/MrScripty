# Puma / Jeremy Bayley portfolio

Buildless, self-contained portfolio for the existing GitHub Pages project site. Tested source `faed6ec2ffe05a00d645e4d3e14a21cd7ae90d61` is published as `b9bb6841a2250b3be4e006d00609e3f9418d90e9` after independent review and four-width verification. See [deployment evidence and live-inspection limits](DEPLOYMENT.md).

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
- Memory and context groups Tuldok, Book-Be-Gone, Eidetic, Whip Docs and Coding Standards in separate rows.
- Rheon and Kenoma form the physics research section. Rheon's native interface and separate Surrogate Lab remain distinct; its approximate eightfold result describes the tested fixed-box CPU workload.
- The three existing books retain their original covers and attribution. Cooking the Cat retains only its approved short description. The genuine owner-supplied Lanternwake image appears below the books.
- Five manual galleries preserve complete image proportions and full-size viewing. Overlay arrows support hover, focus, touch, keyboard and swipes; no-JavaScript links remain usable.
- Twelve code projects have capability tags. Thirteen separate language bars, including an independent Surrogate Lab bar, use reproducible authored-source byte proportions and GitHub Linguist colors. All bars sit with their project text. Hover, focus or tap exposes the percentages. [The method](LANGUAGE_METHOD.md) and [data](assets/language-stats.json) record pinned commits, narrow hash-checked exclusions, byte totals, exact proportions and the pinned color source.
- The hero gives Model systems, Visual tools, Data provenance, Observability and Local AI equal headline typography. Social links retain their destinations and accessible names, with standard GitHub and LinkedIn icons.
- Image headers, labels and captions are removed throughout, including enlarged views. Meaningful image alt text, gallery counts/controls, full-size access and focus restoration remain. Whip Docs links only to its public source.
- Scope dropdowns and per-project status badges are removed. Required [image and icon credits](image-credits.html) remain available separately.

Edit `index.html`, `styles.css` and `script.js`; then regenerate content-versioned CSS/JS with `tools/version_assets.py` and verify. Keep `image-credits.html` on the same versioned stylesheet. Preserve original image bytes and provenance in `assets/`. Review-only documents, QA screenshots, unused assets and local logs do not belong in a deployment bundle.

The root profile README is maintained independently. This branch does not merge application code, add workflows, change account permissions or publish automatically.
