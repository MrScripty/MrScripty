# Authored-source language composition

The portfolio measures source bytes at 13 pinned public repository commits. It does not estimate effort, author identity, runtime importance, or commit ownership. Maintained mixed-origin files count in full; generated outputs and unchanged dependencies do not. There are no hand-set percentages, language weights, whole-directory exclusions or line-based authorship guesses.

## Reproduce

Requires Python 3, Git and Docker. From `docs/portfolio`:

```sh
python3 tools/measure_languages.py --cache-root /tmp/portfolio-language-sources
```

The runner checks out only public repositories at the exact commits in [language-sources.json](tools/language-sources.json). Existing clones must have the specified HEAD and a clean working tree. Project code is never executed. Classification uses the official GitHub Linguist container, pinned by digest, mounted read-only with networking disabled:

- Version actually measured: **9.3.0**.
- Image: `ghcr.io/github-linguist/linguist@sha256:cfe77ac6fe1d7d46c2e705922f53ddb8260f2bbe37ccceb8d9ef13ddce151fb6`.
- Command: `github-linguist --json --breakdown`.
- Normal Linguist language classification and generated/vendor/documentation/binary filtering apply. The policy adds exact file exclusions only where provenance or an explicit generator supports them.
- Colors use the official Linguist palette pinned at `5fbdfcb8133be2bed88bf3ce62b2335f50474525`; its URL and hash are in [linguist-colors.json](tools/linguist-colors.json).

Each exclusion identifies the complete path, original SHA-256, category, reason and supporting evidence paths/hashes. The runner verifies those records, protected maintained files, all counted byte totals and classifier version before writing any output. It retains normal authored tests, fixtures, generators and historical source. Changes to a pinned source or evidence file fail closed and require review, not silently widened exclusions. Files already omitted by Linguist are recorded without subtracting their bytes twice.

[language-stats.json](assets/language-stats.json) contains the measured totals and exact proportions used by all 13 bars. [The per-repository audit](language-audit/) records every classified file and its count/exclusion decision. Two complete classifier passes produced byte-identical snapshots. The browser checks compare every rendered proportion and source commit with the snapshot.

## Exclusion evidence

- **Whip Docs:** exclude the three generated Tree-sitter parser C outputs, upstream scanner C files and Tree-sitter runtime headers. Upstream grammar originals, queries and unchanged Rust wrappers match the repository's pinned source-provenance manifests. Retain the three maintained grammar.js files, the modified C grammar Rust build.rs, handwritten Python, and all seven authored C/H fixtures (1,033 bytes). This removes 30,286,412 generated/upstream C/header bytes while retaining real C; all language exclusions together remove 30,389,634 bytes. The C share becomes about 0.095%, rather than the former 96.1% repository bar. Rust is 40.72% and TypeScript 38.67%. The 12,506 Python bytes remain included.
- **Pumas Library:** six generated desktop-contract projections are identified by their generated headers and generator/source contract. The authored generator, Rust contract and build hook remain counted.
- **Coding Standards:** its 612,362-byte disposable `_generated_contract.py` projection is identified by the contract documentation and projection writer. The generator and tests remain counted.
- **Kenoma:** three downloaded BodyParts3D documentation files, one Pandoc preview and four generated negative-test HTML pages are excluded. Maintained interactive-lab HTML, templates, generators and historical authored JavaScript remain counted. Existing vendor filtering already removes unchanged Three.js/sql.js dependencies.
- **Lanternwake:** 42 unchanged MeltySynth files match the upstream hash manifest. Linguist already omits them, so they cause no additional subtraction.
- **Book-Be-Gone:** three committed Vite distribution outputs are documented by the build configuration. Linguist already omits them. Authored Python, JavaScript and Svelte remain counted.
- **Pantograph, Chrema, Tuldok, Eidetic, Rheon, Rheon Surrogate Lab and Passeur:** the inspected pinned source needs no extra exclusions beyond Linguist's existing rules.

There are 93 exact exclusion records. Some identify files already filtered by Linguist. This is a reviewed source-byte metric, not a claim that every retained byte was typed by one person.

## Before and after

The previous display was a timestamped GitHub `/languages` API snapshot without a recorded commit. It is preserved verbatim in [repository-api-before.json](language-audit/repository-api-before.json). The comparison also records a fresh Linguist baseline at each new exact commit, so source evolution is not mistaken for an exclusion effect. The last column measures only extra exclusions against that same-commit baseline. The table shows the three largest languages; the JSON contains every language.

| Project | Pinned commit | Previous API display | Authored source | Extra excluded bytes |
| --- | --- | --- | --- | ---: |
| Pumas-Library | `ef9eead` | Rust 60.61%, JavaScript 19.73%, TypeScript 12.14% | Rust 73.59%, TypeScript 14.17%, Python 8.75% | 3,673,382 |
| Pantograph | `07b23d4` | Rust 83.01%, TypeScript 8.60%, Svelte 5.17% | Rust 83.01%, TypeScript 8.60%, Svelte 5.17% | 0 |
| Chrema | `75fba33` | JavaScript 90.90%, PLpgSQL 9.10% | JavaScript 91.00%, PLpgSQL 9.00% | 0 |
| Tuldok | `c522bf6` | Python 50.66%, JavaScript 46.78%, HTML 1.84% | Python 50.66%, JavaScript 46.78%, HTML 1.84% | 0 |
| Eidetic | `cc80011` | Rust 69.26%, TypeScript 19.12%, Svelte 6.49% | Rust 69.26%, TypeScript 19.12%, Svelte 6.49% | 0 |
| whip-docs | `c5a8417` | C 96.11%, Rust 1.44%, TypeScript 1.34% | Rust 40.72%, TypeScript 38.67%, JavaScript 14.19% | 30,389,634 |
| Rheon | `2209012` | Rust 51.31%, Python 43.50%, Lean 4.90% | Rust 51.31%, Python 43.50%, Lean 4.90% | 0 |
| rheon-surrogate-lab | `e8a90bf` | Python 60.27%, Rust 33.75%, JavaScript 4.39% | Python 60.27%, Rust 33.75%, JavaScript 4.39% | 0 |
| Kenoma | `e2ea6ac` | JavaScript 57.09%, Python 25.31%, HTML 6.92% | JavaScript 60.30%, Python 26.74%, Lean 6.83% | 169,513 |
| Coding-Standards | `188beda` | Python 99.46%, HTML 0.54%, TypeScript 0.00% | Python 99.36%, HTML 0.64%, TypeScript 0.00% | 612,362 |
| Lanternwake | `76b8428` | C# 67.66%, Python 29.94%, GDScript 1.91% | C# 67.66%, Python 29.94%, GDScript 1.91% | 0 |
| Passeur | `725c45c` | JavaScript 57.40%, TypeScript 42.02%, Shell 0.12% | JavaScript 58.03%, TypeScript 41.40%, Shell 0.12% | 0 |
| Book-Be-Gone | `ea6a3fa` | New project | Python 64.82%, JavaScript 19.63%, Svelte 15.28% | 0 |
