# Puma / Jeremy Bayley portfolio

A buildless portfolio for GitHub Pages. This source branch contains a new visual revision awaiting review; it has not been published. The existing layout with the separately approved Eidetic addition is on the `gh-pages` branch. GitHub reports its deployment succeeded; direct public-URL verification is blocked in the publication environment. The existing GitHub profile README and banner are unchanged.

## Preview

Open `index.html` in a browser, or run:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Then visit `http://127.0.0.1:8080` on that same computer. There is no dependency installation or build step. All images, styling, and scripts are local; third-party requests occur only if a visitor follows an external link.

## What is included

- A responsive portfolio with Pumas Library, Pantograph, Chrema, Tuldok, Eidetic, Rheon, and Kenoma
- A clear project landscape and separate related-tool links, without claiming a complete end-to-end integration
- Chrema described only through the existing public profile summary; no private source or operational data
- Source and architecture links, project status, and explicit research boundaries
- Dataset Production and Training Your Own Models presented as a paired collection of separate books, with distinct attribution and verified repository links
- Practical Data Analysis listed separately as an engineering-methods resource
- Three original public book covers with pinned byte-level provenance in `assets/books/provenance.json`
- Public GitHub and LinkedIn contact links; no private contact details
- Genuine Tuldok image-workflow results, Pantograph editor/native-demo, Eidetic native screenplay/timeline, Rheon native-comparison, and Kenoma posing/anatomical-arm captures with full-size enlargement and pinned provenance
- Two earlier Tuldok captures retained in `assets/` with provenance; the visible card now uses the approved image-workspace milestone
- An accessible screenshot enlargement dialog with a direct-image fallback
- Dark / light sections, reduced-motion support, print styling, and a skip link

Tuldok shows a completed scratch CPU image-classification run on 12 authored CC0 drawings, with frozen inputs, metrics and retained artifacts. It makes no useful-model-quality, audio-training or 3D-training claim. The Pumas panel currently shows a clearly labeled authored architecture summary, not an app screenshot. Pantograph shows approved genuine captures from PR #71 revision `7fc3584`: the I/O Inspector reading retained outputs, the earlier browser-rendered Svelte Graph connected to a live loopback Rust host, plus successful and deliberately rejected deterministic scheduler runs. The workbench reads retained output; native Tauri execution and model inference are not claimed. Eidetic shows the native Linux screenplay/timeline workflow with authored demo fiction and explicit renderer/inference limits. Rheon and Kenoma show genuine running-application captures. Kenoma pairs the schematic poser with the separate anatomical arm viewer at a held reference state; no new motion solve or full-body validation is claimed. Each project has concise capability copy; detailed scope and verification notes use closed disclosure sections.

## Checks

```sh
python3 tools/verify.py
node --check script.js
```

Both pass. The static checker covers local resource paths, fragment targets, duplicate IDs, alt attributes, a single primary heading, external scripts, and the Pages marker.

`tools/browser_check.py` is the responsive and dialog QA harness for an environment with Playwright and Chromium. Publication QA passed at 1440, 768, 390 and 320 px, including lazy images, keyboard navigation, Escape/Close, history traversal, focus return, overflow and the no-JavaScript baseline. See `VALIDATION.md` for evidence and external-link verification limits.

## Publication status

See `DEPLOYMENT.md` for the exact deployment commit, GitHub-reported URL, and remaining external verification. This source package adds no deployment workflow to the profile branch.

## Editing

- `index.html`: copy and page structure
- `styles.css`: layout, responsive rules, and appearance
- `script.js`: progressive screenshot dialog
- `assets/`: local image files and provenance
- `SOURCES.md`: claim-to-source notes for review

Relative asset paths work on a user site or project site. Add a canonical URL and social-preview metadata only after the actual deployment URL is verified. Link the separate Pantograph site only once its published address is verified; the current portfolio links verified repository documentation.

The visual redesign, Chrema, original book covers and new Tuldok image-workspace card remain source-only. The approved Eidetic section was published separately onto the existing layout; see `DEPLOYMENT.md`.
