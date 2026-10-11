# Validation status

## Passed locally

- `python3 tools/verify.py`: no errors; 26 unique IDs, one h1, valid local resource paths and anchor targets, required image alt attributes, and no external scripts.
- `node --check script.js`: JavaScript syntax passed.
- Original Tuldok JPEG files opened, decoded, and visually inspected at 1600 × 1100.
- SHA-256 image provenance recorded.
- Manual source review: no fabricated metrics, testimonials, customers, inference quality, anatomical accuracy, or production fluid-simulation claims; no private project disclosures.
- Basic palette contrast spot checks prompted darker light-background label colors. This is not a full automated accessibility audit.

## Not completed

The website has not yet been rendered successfully in a browser in this workspace. No website screenshots are supplied or claimed.

The installed Chromium process failed before navigation with:

```
FATAL:chrome/browser/process_singleton_posix.cc:297
Check failed: . socket() failed: Operation not permitted (1)
```

The execution escalation ran but returned the same Chromium runtime failure. This was not a reviewer denial. A subsequent supported cloud-browser attempt to the local preview URL returned `net::ERR_CONNECTION_REFUSED`; that browser could not reach the workspace's loopback service. The temporary preview server was stopped.

The included `tools/browser_check.py` is a test harness, not evidence of passed checks. Run it on an authorized environment with working Playwright and Chromium, or perform equivalent browser QA manually. It checks 1440, 768, 390, and 320 px widths; resource loads; overflow; skip navigation; screenshot dialog open/Escape/focus return; and a no-JavaScript baseline.

Additional final QA should check the close button, repeated open/close, anchor navigation, screenshots at full size, source links, and reduced-motion presentation. The result is a source-only review package, not a launch-ready certification.
