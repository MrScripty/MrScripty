# Source and claim review

Reviewed 2026-10-11. These are repository descriptions and contracts, not an independent qualification of every application feature.

## Profile and biography

- Public profile: https://github.com/MrScripty
- Profile README: https://github.com/MrScripty/MrScripty/blob/main/README.md
- Profile README blob at review: `5d48d5df5f18548fc8706ee49fb6f13ca09eaa52`
- LinkedIn: https://www.linkedin.com/in/jeremybayley
- The name Jeremy Bayley and professional VFX background are based on Jeremy's LinkedIn profile. Public copy stays at that brief level and is for editorial review before publication.
- The description of independent reusable projects and applications informing research follows the current public GitHub profile. No employment, client, usage, performance, or production-readiness metrics are invented.

## Pumas Library

- https://github.com/MrScripty/Pumas-Library/blob/main/README.md
- README blob: `ea97563e96d7209bb715bb7bd13c68166b9c341b`
- https://github.com/MrScripty/Pumas-Library/blob/main/docs/ARCHITECTURE.md
- Architecture blob: `911dffffbc6cdc52b21bec6a45c2eb59220300d2`
- Supports: reusable Rust backend, optional GUI, SQLite model index, resumable downloads, import/repair, typed artifact/runtime requirements, loopback RPC, Linux-primary runtime target.
- Boundary: no representation that unpublished local fixes are released; integrations and language bindings have separate verification limits.

## Pantograph

- https://github.com/MrScripty/Pantograph/blob/main/README.md
- README blob: `c80628b5a01c181e2a57aae5db80bc9f83b98b50`
- https://github.com/MrScripty/Pantograph/blob/main/ARCHITECTURE.md
- Architecture blob: `ab1d2c22bfcf33ec335f52948ba87b0d3d7e8a31`
- Supports: local-first Rust workflow platform, optional Svelte/Tauri host, node contracts, resource-aware scheduling, artifacts/diagnostics/provenance modules.
- Boundary: active transition to durable scheduler-owned task execution; no single green repository-wide compliance command. No qualified distributed execution or inference-quality claim.
- The dedicated Pantograph website is a separate project. This portfolio does not duplicate it or invent its URL.

## Tuldok

- https://github.com/MrScripty/Tuldok/blob/main/README.md
- README blob: `456b214ea170ebac301dde00692639bd4c3fb5d4`
- Supports: local Python/browser dataset tool, capture/import, corner labeling, provenance/review/export workflows.
- Screenshot provenance: https://github.com/MrScripty/Tuldok/blob/83b2df92d16acb80a03d1a5d19370489b464501a/docs/images/README.md
- Source application: `1bb2c3ae9d08432c53ddf9d4bf77fa5f62ad318c`.
- Capture commit: `83b2df92d16acb80a03d1a5d19370489b464501a` in draft PR #32 (not merged at capture review). These provisional captures are retained as source evidence but omitted from the visible page in favor of the newer image-workspace milestone described below.
- Captured in Chromium 151.0.7922.173, 1600 × 1100, device scale 1, direct JPEG85. Files were downloaded from those pinned public URLs and their pixels inspected. No image modification is applied.
- Image screenshot uses the built-in `rectangles-v1` offline recipe, seed 42, count 3. Text screenshot uses an authored SAMPLE workshop request and a manually saved draft label. Neither image contains personal records or demonstrates model-quality qualification.
- SHA-256 values and dimensions are recorded in `assets/capture-provenance.json`.

## Rheon

- https://github.com/MrScripty/Rheon/blob/main/README.md
- README blob: `d0829ea21cc21af523229ef5366357f10740c1c8`
- https://github.com/MrScripty/Rheon/blob/main/docs/COMPARISON.md
- Supports: Rust fixed-box pressure implementations, native comparison UI/headless CLI, conservative represented liquid-volume transport.
- Boundary: an initial comparison lab, with free-surface pressure and other coupling still open. No general physical-accuracy, production-simulation, or real-time claim.

## Kenoma

- https://github.com/MrScripty/Kenoma/blob/main/README.md
- README blob: `1fc4691d9f73743e5f540e463ba9b6bcc18f6998`
- https://github.com/MrScripty/Kenoma/blob/main/browser/simple-graph/README.md
- Supports: embeddable static WebGL/WASM posing page, multiple characters, gizmos, two-bone IK, undo/redo, separate headless graph/persistence/surface/rig tools.
- Boundary: schematic posing, no anatomical accuracy or physical simulation; biomechanics is a separate research track.

## Books

Dataset Production and Training Your Own Models are presented as a paired collection, not as one book. Their repository ownership and attribution remain separate.

- **Dataset Production**: https://github.com/MrScripty/dataset-production . This remains MrScripty’s fieldbook and interactive dataset-production workbench. README blob at review: `00d2d1f3333586feb5a68b0b5bba07283c5721d2`. Manuscript title and companion relationship verified in `docs/book/manuscript.md`, blob `8f10a4bc9adc5325974fa0e3cdba1a97127d3fdf`.
- **Training Your Own Models on One 24 GB GPU**: https://github.com/bc-ai-ecosystem/training-your-own-models . Exact credit: “Vibe Authored by Dr.Puma.” The project was transferred to BC+AI. The repository is archived as of the metadata check on 2026-10-11; the portfolio uses this verified repository link rather than claiming its current site was live-verified. README blob: `b7ee10d5c4ee437c7bc1dd547905f498e78ed8d4`.
- The training README references a copied archive in WalksWithASwagger/kk-kb and an unspecified improved edition elsewhere. The copied archive is not described or linked here as an improved edition.
- **Practical Data Analysis for Engineering Decisions** remains a separate resource: https://mrscripty.github.io/practical-data-analysis/ . This title and URL are published in the GitHub profile README.

## Artwork

The hero landscape is authored semantic HTML with inline SVG arrow icons. The Pumas architecture panel is an authored diagram, not a screenshot. Pantograph, Rheon, and Kenoma use unedited running-application captures; no generated or reconstructed application interface is used.

## Additional running-application captures

All source pixels were inspected before integration. Original PNG bytes are preserved; CSS scales images without cropping. File hashes, dimensions, source URLs, exact capture commits, and scope are in `assets/capture-provenance.json`.

- **Pantograph**: approved captures pinned to `7fc3584cca8bef647b60ebf303c4b5d6b37d98bd` in PR #71. The real Svelte workbench connects to a persistent Rust workflow service over loopback HTTP. Diagnostics query that running service and the I/O Inspector reads retained scalar artifact bytes. The model catalog is a real isolated empty Pumas library. Success and deliberate missing-path rejection captures preserve actual native results. At that capture revision, Graph editor mutation/submission was outside the demo host; native Tauri and model inference remain unqualified. Source PNG bytes are unchanged. Guide: https://github.com/MrScripty/Pantograph/blob/7fc3584cca8bef647b60ebf303c4b5d6b37d98bd/examples/scheduler-demo/README.md
- **Rheon**: source capture commit `a2ebb8f11bcb65df0c70c45bfb8234d08b293a0a`, running app commit `34235d33c886aa05b5bdf95d920b863d1fb2ad6f`. Native Linux software-rendered solver comparison, 1650 × 900. The unequal accepted-time warning is visible. This is exploratory fixed-box solver evidence, not physical validation or a qualified speed comparison. Source: https://github.com/MrScripty/Rheon/blob/a2ebb8f11bcb65df0c70c45bfb8234d08b293a0a/README.md
- **Kenoma**: source capture commit `9739080116b658e6248816f4e4239c4fde95ca94`, running app commit `e2ea6acc5db44794ae8b49beb877f5a8bccea056`. Chromium151, 1600 × 1000, actual Rust/WASM editor. Schematic posing and joint creasing are retained. Source: https://github.com/MrScripty/Kenoma/blob/9739080116b658e6248816f4e4239c4fde95ca94/README.md

## Eidetic native workflow capture

- Public repository: https://github.com/MrScripty/Eidetic
- Approved capture commit: `0f3481cd93e28673a566c77a2f0c7ca48469aab5`, draft PR #30.
- Native application source at capture: `18d6c5e0c51c2c6b75f161939ce4b32f0bfb6338`; native Linux Tauri/WebKit window with the production frontend.
- Pinned acceptance report: https://github.com/MrScripty/Eidetic/blob/0f3481cd93e28673a566c77a2f0c7ca48469aab5/docs/reports/native-workflow-acceptance/README.md
- The displayed `screenplay-timeline.png` is copied byte-for-byte. Its SHA-256 is `d8f85a18ac887ad5821e944eade2efa7f987bcff72ec9c7e767d87580812db16`; dimensions are 1440 × 960. The public provenance manifest confirms those values.
- All displayed story material is the original authored Signal at Low Tide demo, not private story content or generated output.
- Verified scope: native project open; screenplay and story-bible editing, save/reopen, cancelled screenplay edits, timeline-title changes, and renderer controls.
- Limits: no real Pumas inference; native graph/timeline renderers remain minimal; renderer-type switching needs an application restart; unified multiwindow rendering is unfinished. No Windows/macOS native UI acceptance is claimed.
- Exact-head CI run: https://github.com/MrScripty/Eidetic/actions/runs/38175127015 . CI is separate from the visible native Linux workflow evidence.

## Source-only visual revision

- **Chrema / Composable Agents:** copy comes only from the public profile README, in “Models, workflows & agent-first development.” It describes private workflow-composition and auditable-ledger research. No Chrema private repository, source, credentials or ledger records were accessed or published. “Composable Agents” is the requested presentation label, not a new integration qualification.
- **Related tools:** Passeur (cross-provider delegation), Coding Standards (shared agent-oriented standards), and Whip Docs (code architecture navigation) are described at the level of their existing public profile entries. These relationships communicate shared concerns, not a verified end-to-end stack.
- **Book art:** original public cover files are copied without pixel changes. Exact repository commits, raw URLs and SHA-256 hashes are in `assets/books/provenance.json`. Dataset Production and Training Your Own Models retain separate ownership and attribution.
- **Pantograph lead image:** the actual I/O Inspector at approved capture revision `7fc3584` shows retained text. The earlier Graph image is retained and labeled. App follow-up `679622e9d8b17e87a278b81b60194d31ee4f4981` adds saved-workflow submission and a Network adapter, but no new screenshot was delivered; presentation copy distinguishes source changes from old visual evidence.
- **Pending captures:** Kenoma anatomy and improved Rheon simulation/layout await actual approved images from their application workers. Current genuine captures and their limits remain in place.
- **Audit:** `IMAGE_AUDIT.md` records displayed image states, source revisions and deployed-branch comparisons. Content-derived asset query strings are cache hygiene, not evidence that caching caused the reported errors.

## Tuldok image-workspace milestone

- Gallery documentation commit: `6d939359d3cef2464c2aff990dd58d50c4f8d791` on `feature/workspace-image-runs-20261011`.
- The gallery manifest pins the actual capture to clean application source `f725bd1806bfe5e27635eb817a403b602a14591a`, Chromium 151.0.7922.173, 1440 × 900, original JPEG quality 85. The capture's source is distinguished from the later qualification/documentation heads.
- Displayed image: `results-real-1440.jpg`, copied unchanged as `assets/tuldok-workspace-results.jpg`. SHA-256: `34fdf853af386eec516d6e026930d98fd80256ec0545b6c9b299e4f4d7e20487`.
- Approved authored data: 12 independent CC0 drawings; 6 training, 3 validation and 3 test examples. The screenshot displays a completed CPU run, 33.3% validation accuracy on 3 examples, macro F1 0.250, frozen graph/release identities, completed stages and verified artifacts. Test access is visibly locked at capture time. This demonstrates the workflow, not useful model quality.
- Manifest checks cover image import/labels/review, immutable release, actual editable graph and trainer parameters, real CPU training, artifact verification, correction/new release and application restart with retained run/input/prediction identities. The portfolio describes image classification only; it does not claim audio/3D training.
- Gallery: https://github.com/MrScripty/Tuldok/blob/6d939359d3cef2464c2aff990dd58d50c4f8d791/docs/images/workspaces-m2/README.md
- Provenance: https://github.com/MrScripty/Tuldok/blob/6d939359d3cef2464c2aff990dd58d50c4f8d791/docs/images/workspaces-m2/manifest.json
- The app worker reported 98 passing CI steps and 507 Python tests at qualified successor `acac0d3`; this portfolio change does not rerun or extend application qualification. It does not claim the later documentation head has completed CI.
