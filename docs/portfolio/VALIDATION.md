# Validation status

Validated 11 October 2026 against the source-only visual revision, using Chromium 151.

- Static resource paths, fragment targets, unique IDs, image alt text, single h1, no external scripts, and JavaScript syntax pass.
- Combined portfolio/Pantograph validation passes **1,266 checks** at 1440, 768, 390 and 320 px: local resources, no horizontal overflow, skip navigation, seven screenshot dialogs, Escape/Close, Back/Forward, focus return and no-JavaScript reading.
- Pantograph keyboard tabs, successful and expected-rejection recordings, event inspection and JSON downloads pass. All six research pages pass phone/desktop contents navigation and overflow checks; bibliography links resolve.
- Desktop and mobile review images were inspected for the hero, book cards, Pantograph project card, three perspectives and view coverage. Original image pixels are unchanged; CSS preserves the full captures and cover art.
- All **22 distinct GitHub destinations** on the two landing pages returned HTTP 200. The previously approved LinkedIn and Practical Data Analysis Pages URLs remain independently unverified because the environment blocks those external hosts.
- The existing profile README, manuscript editions, backend code and shared CI workflows are unchanged. Eidetic's original approved native capture and its qualification limits remain intact.

The standalone portfolio harness is `tools/browser_check.py`. Review screenshots and its JSON report are written under ignored `review/`. A combined static-site harness additionally checks the assembled project subpaths and research documents. Local checks establish source behavior, not live deployment.

## Publication boundary

This visual revision, Chrema copy, book artwork and Eidetic addition have not been published. The existing Pages commit is recorded in `DEPLOYMENT.md`. Fresh Pantograph Graph/Scheduler/Network captures are pending in the app worker; Kenoma anatomy and Rheon updates are also pending. No replacement image is simulated.
