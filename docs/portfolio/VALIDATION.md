# Validation status

The compact dark revision is source-only. It was checked locally in Chromium 151 at **1440, 768, 390 and 320 px** on 12 October 2026.

- Static paths, fragments, IDs, alt attributes, one h1, and JavaScript syntax pass. No external scripts are loaded.
- All four browser viewports have no horizontal overflow, broken images, blank links or JavaScript errors. Skip navigation works. All twelve screenshot dialogs open their original images, close with Escape, and restore focus at every width (48 dialog exercises). Reading and source links remain usable without JavaScript.
- **71 additional checks pass:** dark section backgrounds, separately stacked Tuldok/Eidetic sections, the four matching Pantograph multi-branch workbench views, both Kenoma views, screenshot hashes including the three Whip Docs captures and matching Pantograph receipt hashes.
- The Pantograph gallery uses the inspected 13-node run at `03d838b`; all four image hashes match its public receipt. Its visible caption identifies two untrained CPU embedding fixtures (8D/12D) and excludes text/image generation.
- Whip Docs’s three added images match the original `a5caed08` capture bytes retained on merged main `c5a8417`. The full visual section was inspected on desktop and mobile, including the uncropped portrait inspector and full-size dialogs.
- Desktop/mobile full-page and project-section previews were visually inspected. Existing screenshots and cover art retain their original pixels and aspect ratios.
- All **22 distinct GitHub destinations** on the current page returned HTTP 200. Four external destinations remain proxy-blocked: LinkedIn, the existing Practical Data Analysis Pages site, and two source-provided Creative Commons license links. These are recorded as unverified, not broken or successfully checked.
- The profile README is unchanged (`5d48d5df5f18548fc8706ee49fb6f13ca09eaa52`). Remote main remains `20ae4e6f08e753fc37f97abb6b651d60fd156ed5`; Pages remains `e0ddbf9811044cf2bbd25af4e6527032d2abd701`.

See [dark review and remaining blockers](DARK_REVIEW.md), [product icon inventory](ICON_AUDIT.md), [desktop/mobile previews](../portfolio-review/README.md), and [capture provenance](assets/capture-provenance.json). Pumas Library GUI evidence, the Cooking the Cat public source/cover, and the approved Rheon refinement are still outstanding.

The standalone browser harness is `tools/browser_check.py`; outputs under `review/` are ignored. Local source checks do not establish a live deployment. Earlier validation and release records follow for historical context.

## Publication boundary

The reviewed visual design from `b600137`, Chrema overview, original book artwork and preserved Eidetic section are published at `e0ddbf9811044cf2bbd25af4e6527032d2abd701`. Its isolated bundle passed 141 publication checks with seven screenshot dialogs across four viewport sizes. All 15 runtime files match the approved source, and desktop/mobile screenshot bytes match the exact reviewed previews. GitHub build/deploy succeeded; direct public HTTP verification remains proxy-blocked.

The dark revision and its Tuldok image-workspace, fresh Pantograph and Kenoma held anatomical-arm additions remain source-only. The dark source revision now includes fresh Pantograph captures; Rheon refinements remain pending. The separate Pantograph-site redesign was not published. See `DEPLOYMENT.md` for exact commits and verification limits.

## Tuldok image-workspace addition

The selected results JPEG matches the pinned public manifest SHA-256. Desktop/mobile card previews were visually inspected; the added image opens full-size and preserves the existing keyboard/history/focus behavior. All 1,276 paired-site checks pass after this addition. The new pinned gallery link returned HTTP 200. No application code, model-quality qualification or deployment is included in this addition.

## Kenoma arm apparatus addition

The selected 1440 × 1440 PNG matches its pinned public provenance hash. The separate poser PNG is unchanged. Desktop/mobile views were visually inspected, including full-image access, held-state scope and component attribution. The combined source now passes 1,286 checks with nine working screenshot dialogs. The new pinned caption/provenance GitHub destination returned HTTP 200; no application runtime qualification or deployment is included in this addition.
