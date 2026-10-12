# Validation status

The compact dark revision is source-only. It was checked locally in Chromium 151 at **1440, 768, 390 and 320 px** on 12 October 2026.

- Static paths, fragments, IDs, alt attributes, one h1, and JavaScript syntax pass. No external scripts are loaded.
- All four browser viewports have no horizontal overflow, broken images, blank links or JavaScript errors. Skip navigation works. All twelve screenshot dialogs open their original images, close with Escape, and restore focus at every width (48 dialog exercises). Reading and source links remain usable without JavaScript.
- **The preceding layout revision passed 71 additional checks:** dark section backgrounds, separately stacked Tuldok/Eidetic sections, the four matching Pantograph multi-branch workbench views, both Kenoma views, screenshot hashes including the three Whip Docs captures and matching Pantograph receipt hashes.
- The Pantograph gallery uses the inspected 13-node run at `03d838b`; all four image hashes match its public receipt. Its visible caption identifies two untrained CPU embedding fixtures (8D/12D) and excludes text/image generation.
- Whip Docs’s two visible images match the original `a5caed08` capture bytes retained on merged main `c5a8417`. The repeated third, standalone inspector entry is removed; original screenshot files remain intact. The second view fills its row, and both visible images support full-size dialogs with correct Back/Forward navigation and focus restoration at all four widths.
- The Pumas gallery displays only the original owner-published 805 × 1001 HF search PNG from `bdcb9b3`, with its complete aspect ratio and a responsive width capped at 440 px. Back/Forward dialog navigation and focus restoration pass. The error-bearing Library image is absent from the HTML and browser requests; stale dialog history for the removed image is ignored. No placeholder is displayed. Both original PNGs remain byte-identical in source, and the replacement Library capture is pending.
- The header uses the owner-supplied `puma.jpg` from `a2ab18d`: 1176 × 1174 pixels, 185,254 bytes, SHA-256 `661bb77b05d56cf01ad0eba0bb108fee297d99f3c13009ebc8906467a04b5e19`. The original bytes remain unchanged. The centered circular display retains the existing 38 px desktop / 34 px phone dimensions, clear accessible text and navigation alignment.
- Eidetic now uses the owner’s original root `icon.png` from public source `cc80011`: 512 × 512 pixels, 122,910 bytes, SHA-256 `7b063a49f521c4d54fc69e8704cd58f06455b07437e9e9acc6419c376e9e0a86`. Pixels and provenance were inspected; the original bytes are unchanged.
- Desktop/mobile full-page and project-section previews were visually inspected. Existing screenshots and cover art retain their original pixels and aspect ratios.
- All **22 distinct GitHub destinations** on the current page returned HTTP 200. Four external destinations remain proxy-blocked: LinkedIn, the existing Practical Data Analysis Pages site, and two source-provided Creative Commons license links. These are recorded as unverified, not broken or successfully checked.
- The profile README is unchanged (`5d48d5df5f18548fc8706ee49fb6f13ca09eaa52`). Remote main remains `20ae4e6f08e753fc37f97abb6b651d60fd156ed5`; Pages remains `e0ddbf9811044cf2bbd25af4e6527032d2abd701`.

See [dark review and remaining blockers](DARK_REVIEW.md), [product icon inventory](ICON_AUDIT.md), [desktop/mobile previews](../portfolio-review/README.md), and [capture provenance](assets/capture-provenance.json). The Cooking the Cat public source/cover and the approved Rheon refinement are still outstanding. The HF search and profile-photo gaps are resolved using the owner’s public originals; a healthy Library replacement remains pending.

The Library-image exclusion was checked using an isolated copy of the intended commit: the separate uncommitted Cooking the Cat draft is excluded from the public previews and remains intact locally. The page has 22 images, 19 unique IDs and 79 local/external references; static validation reported no errors.

The standalone browser harness is `tools/browser_check.py`; outputs under `review/` are ignored. Local source checks do not establish a live deployment. Earlier validation and release records follow for historical context.

## Publication boundary

The reviewed visual design from `b600137`, Chrema overview, original book artwork and preserved Eidetic section are published at `e0ddbf9811044cf2bbd25af4e6527032d2abd701`. Its isolated bundle passed 141 publication checks with seven screenshot dialogs across four viewport sizes. All 15 runtime files match the approved source, and desktop/mobile screenshot bytes match the exact reviewed previews. GitHub build/deploy succeeded; direct public HTTP verification remains proxy-blocked.

The dark revision and its Tuldok image-workspace, fresh Pantograph and Kenoma held anatomical-arm additions remain source-only. The dark source revision now includes fresh Pantograph captures; Rheon refinements remain pending. The separate Pantograph-site redesign was not published. See `DEPLOYMENT.md` for exact commits and verification limits.

## Tuldok image-workspace addition

The selected results JPEG matches the pinned public manifest SHA-256. Desktop/mobile card previews were visually inspected; the added image opens full-size and preserves the existing keyboard/history/focus behavior. All 1,276 paired-site checks pass after this addition. The new pinned gallery link returned HTTP 200. No application code, model-quality qualification or deployment is included in this addition.

## Kenoma arm apparatus addition

The selected 1440 × 1440 PNG matches its pinned public provenance hash. The separate poser PNG is unchanged. Desktop/mobile views were visually inspected, including full-image access, held-state scope and component attribution. The combined source now passes 1,286 checks with nine working screenshot dialogs. The new pinned caption/provenance GitHub destination returned HTTP 200; no application runtime qualification or deployment is included in this addition.
