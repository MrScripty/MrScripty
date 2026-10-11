# Puma / Jeremy Bayley portfolio

A buildless portfolio for GitHub Pages. The validated static snapshot is on the separate `gh-pages` branch. GitHub reports its deployment succeeded; direct public-URL verification is blocked in the publication environment. The existing GitHub profile README and banner are unchanged.

## Preview

Open `index.html` in a browser, or run:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Then visit `http://127.0.0.1:8080` on that same computer. There is no dependency installation or build step. All images, styling, and scripts are local; third-party requests occur only if a visitor follows an external link.

## What is included

- A responsive portfolio with Pumas Library, Pantograph, Tuldok, Rheon, and Kenoma
- Source and architecture links, project status, and explicit research boundaries
- Dataset Production and Training Your Own Models presented as a paired collection of separate books, with distinct attribution and verified repository links
- Practical Data Analysis listed separately as an engineering-methods resource
- Public GitHub and LinkedIn contact links; no private contact details
- Genuine Pantograph editor/native-demo, Rheon native-comparison, and Kenoma WASM-editor captures with full-size enlargement and pinned provenance
- Two genuine Tuldok captures retained in `assets/` with provenance, currently omitted from the visible page pending its compact-UI update
- An accessible screenshot enlargement dialog with a direct-image fallback
- Dark / light sections, reduced-motion support, print styling, and a skip link

The Pumas panel currently shows a clearly labeled authored architecture summary, not an app screenshot. Pantograph shows genuine captures of its browser-rendered Svelte editor and separate native scheduler demo. Rheon and Kenoma show genuine running-application captures. Each project has concise capability copy; detailed scope and verification notes use closed disclosure sections.

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
