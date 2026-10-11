# Validation status

## Passed locally

- `python3 tools/verify.py`: no errors; one h1, valid local resource paths and anchor targets, required image alt attributes, and no external scripts.
- `node --check script.js`: JavaScript syntax passed.
- Original Tuldok JPEG files opened, decoded, and visually inspected at 1600 × 1100.
- Original Pantograph, Rheon, and Kenoma PNG captures decoded and visually inspected; screenshot pixels are unedited.
- SHA-256 image provenance recorded.
- Manual source review: no fabricated metrics, testimonials, customers, inference quality, anatomical accuracy, or production fluid-simulation claims; no private project disclosures.
- Basic palette contrast spot checks prompted darker light-background label colors. This is not a full automated accessibility audit.

## Browser QA baseline and pending rerun

The source at commit `e5e743e536330ebee40be62cdc0416b09cc73ff5` was rendered in a separate authorized saved environment: 39 checks passed across desktop and phone, 320–1440 px widths, overflow, anchors, disclosures, keyboard navigation, and the skip link. Two issues were reported: missing-glyph external-link arrows and small phone attribution/diagram labels.

This follow-up replaces arrows with inline SVG and adds a readable mobile project map and larger labels. It also adds five visible app captures and browser-history-aware image dialogs. These new changes still need a browser rerun, including Close, Escape, Back/Forward, and repeated opening. The earlier baseline had no visible captures, so it did not validate the dialog.

The original local rendering limitation below remains specific to this preparation workspace.

The installed Chromium process failed before navigation with:

```
FATAL:chrome/browser/process_singleton_posix.cc:297
Check failed: . socket() failed: Operation not permitted (1)
```

The execution escalation ran but returned the same Chromium runtime failure. This was not a reviewer denial. A subsequent supported cloud-browser attempt to the local preview URL returned `net::ERR_CONNECTION_REFUSED`; that browser could not reach the workspace's loopback service. The temporary preview server was stopped.

The included `tools/browser_check.py` is a test harness, not evidence of passed checks. Run it on an authorized environment with working Playwright and Chromium, or perform equivalent browser QA manually. It checks 1440, 768, 390, and 320 px widths; resource loads; overflow; skip navigation; screenshot dialog open/Escape/focus return; and a no-JavaScript baseline.

Additional final QA should check the close button, repeated open/close, anchor navigation, screenshots at full size, source links, and reduced-motion presentation. The result is a source-only review package, not a launch-ready certification.
