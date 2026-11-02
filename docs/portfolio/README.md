# Puma / Jeremy Bayley portfolio

Buildless, self-contained portfolio for the existing GitHub Pages project site. The previous design (source `faed6ec`) is published as `b9bb684`/`edd3f0d`. This redesign is not yet published. See [deployment evidence and live-inspection limits](DEPLOYMENT.md).

## Preview and verify

Serve this directory with `python3 -m http.server 8080 --bind 127.0.0.1`, then open the local URL. All runtime assets are local; external requests occur only when following links.

```sh
python3 tools/verify.py
node --check script.js
python3 tools/browser_check.py
python3 tools/gallery_check.py
python3 tools/refinement_check.py
```

Browser checks require an existing Playwright installation and Chromium; set `PORTFOLIO_CHROMIUM` to use a browser other than `/usr/bin/chromium`. Run them against the intended public source, excluding unrelated local drafts. [Validation](VALIDATION.md) records the four tested widths, keyboard/history behavior and real touch gestures.

## Current presentation

Redesigned on 2 November 2026 for AI labs and AI-engineering hiring: what each project does, and how complete it is, should be clear at a glance. Depth lives in each project's own source or site.

- **Concept: node canvas.** The hero draws the projects as a node graph in category backdrops, a nod to the owner's VFX background and Pantograph's graph UI. Wires show real connections: Rheon generates training data for the Surrogate Lab, which keeps its training recipes and runs in Tuldok. The Pumas → Pantograph → Chrema wires show the design, and the note under the graph says those integrations are still in development. Each wire takes the color of the project it comes from.
- **Groups and color.** Model infrastructure (amber), Model development (violet), Memory systems (sky: Eidetic, Coding Standards and Phased Memory as related reference designs), Agent tooling (mint), Physics simulation (rose), Applications (neutral), then Books and About.
- **Projects are panels.** Each one has a title bar tinted in its category color, with a status: a three-step maturity meter (early prototype → in development → usable) and a short label set by the owner.
- **Languages are explained once**, in About, with single-color icons (Devicon, MIT; Lean ∀ from the Lean 4 VS Code extension, Apache-2.0) and no percentages. The measured data in `assets/language-stats.json` and `language-audit/` stays as provenance but is not shown.
- **Background.** A coarse real-time 2D fluid simulation (stable fluids with vorticity confinement) moves a faint dot grid. The pointer stirs it, slow ambient stirrers keep it alive, it runs at 30 fps and pauses in hidden tabs. Under reduced motion it draws the grid once and stays still.
- **Hero verb.** The headline cycles inspect → trace → audit → compose → understand, with a trace line sweeping under each new word. Screen readers get the full sentence once; reduced motion stays on "inspect".
- **Type.** Archivo (self-hosted variable font, `assets/fonts/`, SIL OFL). Its width axis carries the hierarchy: expanded for display, normal for body, condensed for labels.
- **Unchanged.** Original image bytes, the no-caption galleries with full-size view, in-development disclosures, and the image credits page.

Edit `index.html`, `styles.css` and `script.js`; then regenerate content-versioned CSS/JS with `tools/version_assets.py` and verify. Keep `image-credits.html` on the same versioned stylesheet. Preserve original image bytes and provenance in `assets/`. Review-only documents, QA screenshots, unused assets and local logs do not belong in a deployment bundle.

The root profile README is maintained independently. This branch does not merge application code, add workflows, change account permissions or publish automatically.
