# Puma / Jeremy Bayley portfolio

A reviewable, buildless portfolio for GitHub Pages. This source is prepared for review in a separate branch. Website hosting has not been enabled and the site is not deployed. The existing GitHub profile README and banner are unchanged.

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
- Two genuine Tuldok captures retained in `assets/` with provenance, currently omitted from the visible page pending its compact-UI update
- An accessible screenshot enlargement dialog with a direct-image fallback
- Dark / light sections, reduced-motion support, print styling, and a skip link

The Pumas and Pantograph visual panels currently show clearly labeled authored architecture summaries. They are not app screenshots. Their markup has `SCREENSHOT_SLOT` comment markers for verified captures when available. Rheon and Kenoma are presented through supported source descriptions without invented imagery. Each project has concise capability copy; detailed scope and verification notes use closed disclosure sections.

## Checks

```sh
python3 tools/verify.py
node --check script.js
```

Both pass. The static checker covers local resource paths, fragment targets, duplicate IDs, alt attributes, a single primary heading, external scripts, and the Pages marker.

`tools/browser_check.py` contains a local responsive and dialog QA harness for an environment that already has Playwright and Chromium. In the preparation environment, browser startup failed before page rendering because Chromium could not create its process-singleton socket. A retry with elevated execution returned the same runtime failure. The supported cloud browser could not reach this workspace's loopback server. Consequently, no visual/browser QA pass or website preview screenshot is claimed. See `VALIDATION.md`.

Before publishing: render desktop, tablet, and phone sizes; check anchors, keyboard navigation, dialog close/Escape/focus return, overflow, and actual screenshot readability. Confirm the final copy and capture selection.

## Deploying later

See `DEPLOYMENT.md`. Publishing remains a separate approved step. This package has no automatic deploy workflow and no live URL.

## Editing

- `index.html`: copy and page structure
- `styles.css`: layout, responsive rules, and appearance
- `script.js`: progressive screenshot dialog
- `assets/`: local image files and provenance
- `SOURCES.md`: claim-to-source notes for review

Relative asset paths work on a user site or project site. Add a canonical URL and social-preview metadata only after the actual deployment URL is verified. Link the separate Pantograph site only once its published address is verified; the current portfolio links verified repository documentation.
