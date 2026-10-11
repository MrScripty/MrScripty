# Validation status

Validated 11 October 2026 in Chromium 151 on the isolated publication checkout.

- Static resource, fragment, duplicate-ID, alt-text, single-h1 and no-external-script checks pass.
- JavaScript syntax checks pass.
- Browser checks pass at 1440, 768, 390 and 320 px: no horizontal overflow, successful local resources, working skip navigation, and readable responsive layouts.
- All six screenshot dialogs load their original images. Escape and Close dismiss them; focus returns to the initiating link after history traversal. Back closes and Forward reopens the dialog.
- The page remains readable and source links work with JavaScript disabled.
- The harness waits for lazy image loading and asynchronous history/focus changes before asserting outcomes.
- Original image bytes and the approved paired-book attribution are preserved. No inference-quality, production simulation, or anatomical-accuracy claim was added.

Publication validation also traverses every local link and fragment in the paired Pantograph site, tests recording selection and event inspection, and checks all six research reading pages on phone and desktop.

The landing pages contain 16 distinct external links. Fourteen GitHub targets returned HTTP 200. The environment cannot verify the public LinkedIn profile or Practical Data Analysis Pages URL: its outbound proxy rejects those hosts, and the web fetch tool could not retrieve them. Their previously approved source URLs remain unchanged. This is an external-access limitation, not evidence that those links are broken.

The earlier preparation environment's browser-startup failure is superseded by these checks. Local QA does not establish that either public site has deployed; see `DEPLOYMENT.md`.

## Eidetic source addition

The added native Linux screenplay/timeline PNG matches the SHA-256 in the pinned public provenance at `0f3481cd93e28673a566c77a2f0c7ca48469aab5`. Original image bytes and authored demo content are preserved. The source card retains explicit inference, renderer-restart and multiwindow limits. This addition has not been deployed to Pages.
