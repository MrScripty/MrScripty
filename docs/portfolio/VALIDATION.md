# Validation status

Validated 11 October 2026 using Chromium 151. The source checks below include later image additions; the separately published reviewed design is qualified in the publication section.

- Static resource paths, fragment targets, unique IDs, image alt text, single h1, no external scripts, and JavaScript syntax pass.
- Combined portfolio/Pantograph validation passes **1,286 checks** at 1440, 768, 390 and 320 px: local resources, no horizontal overflow, skip navigation, nine screenshot dialogs, Escape/Close, Back/Forward, focus return and no-JavaScript reading.
- Pantograph keyboard tabs, successful and expected-rejection recordings, event inspection and JSON downloads pass. All six research pages pass phone/desktop contents navigation and overflow checks; bibliography links resolve.
- Desktop and mobile review images were inspected for the hero, book cards, Pantograph project card, three perspectives and view coverage. Original image pixels are unchanged; CSS preserves the full captures and cover art.
- All **24 distinct GitHub destinations** on the two landing pages returned HTTP 200. The previously approved LinkedIn and Practical Data Analysis Pages URLs remain independently unverified because the environment blocks those external hosts. The two Creative Commons license URLs from Kenoma's pinned attribution record are also blocked by the proxy; their exact source-provided links are preserved.
- The existing profile README, manuscript editions, backend code and shared CI workflows are unchanged. Eidetic's original approved native capture and its qualification limits remain intact.

The standalone portfolio harness is `tools/browser_check.py`. Review screenshots and its JSON report are written under ignored `review/`. A combined static-site harness additionally checks the assembled project subpaths and research documents. Local checks establish source behavior, not live deployment.

## Publication boundary

The reviewed visual design from `b600137`, Chrema overview, original book artwork and preserved Eidetic section are published at `e0ddbf9811044cf2bbd25af4e6527032d2abd701`. Its isolated bundle passed 141 publication checks with seven screenshot dialogs across four viewport sizes. All 15 runtime files match the approved source, and desktop/mobile screenshot bytes match the exact reviewed previews. GitHub build/deploy succeeded; direct public HTTP verification remains proxy-blocked.

The newer Tuldok image-workspace and Kenoma held anatomical-arm additions remain source-only. Fresh Pantograph captures and Rheon refinements remain pending. The separate Pantograph-site redesign was not published. See `DEPLOYMENT.md` for exact commits and verification limits.

## Tuldok image-workspace addition

The selected results JPEG matches the pinned public manifest SHA-256. Desktop/mobile card previews were visually inspected; the added image opens full-size and preserves the existing keyboard/history/focus behavior. All 1,276 paired-site checks pass after this addition. The new pinned gallery link returned HTTP 200. No application code, model-quality qualification or deployment is included in this addition.

## Kenoma arm apparatus addition

The selected 1440 × 1440 PNG matches its pinned public provenance hash. The separate poser PNG is unchanged. Desktop/mobile views were visually inspected, including full-image access, held-state scope and component attribution. The combined source now passes 1,286 checks with nine working screenshot dialogs. The new pinned caption/provenance GitHub destination returned HTTP 200; no application runtime qualification or deployment is included in this addition.
