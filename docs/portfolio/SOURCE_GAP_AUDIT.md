# Public source gap recheck

Follow-up audit for the dark review at `af88d1b`, 11 October 2026. This is a source-discovery record, not evidence that an unpublished asset does not exist.

## Cooking the Cat

The exact title is present in the [public profile README at 20ae4e6](https://github.com/MrScripty/MrScripty/blob/20ae4e6f08e753fc37f97abb6b651d60fd156ed5/README.md). It is plain text, with no book URL, text or cover link.

Searches completed:

- Listed all 31 public owner repositories under `MrScripty`; none has a Cooking the Cat name or a corresponding book homepage.
- GitHub repository searches for the exact title and `"cooking-the-cat" in:name,description,readme`. The latter returned the profile and an unrelated pet-food repository. Neither supplied the book.
- GitHub code search for `"Cooking the Cat" user:MrScripty` returned zero indexed hits. This does not override the directly verified profile mention; code-search coverage is not an exhaustive authority.
- Checked complete, untruncated default-branch trees for `MrScripty`, `Coding-Standards`, `Creative-Writing-Experiments`, `Book-Be-Gone`, `Commonlight`, `Pantograph-Portfolio-Voice`, `practical-data-analysis`, and `dataset-production`, looking for Cooking/Cookbook title paths and book/cover artwork. No Cooking the Cat source or cover was found. The two established book covers belong to their named books and were not repurposed.
- Read the public profile and likely book-related READMEs. Creative Writing Experiments is Eidetic research; Book-Be-Gone is a digitization app. Their names do not establish a book source.
- Listed the seven public `bc-ai-ecosystem` repositories and read `training-your-own-models/README.md`. No Cooking the Cat project or link was found. Its linked `WalksWithASwagger/kk-kb` archive returned GitHub 404 and was not accessible as a public source.
- Public web searches for the exact title with Puma, Bayley and software-engineering terms found no attributable book source.

**Needed:** the owner's public book URL, plus the original cover source if a cover exists. The preview retains the owner-provided title and engineering-approach pairing as text only. No cover, URL, publication status, book contents or inference result is invented.

## Pumas Library GUI

**Partially resolved, 12 October:** the owner supplied the actual Library and Hugging Face search captures in [review-branch commit bdcb9b3](https://github.com/MrScripty/MrScripty/commit/bdcb9b38a696d757fa96e8eb0c70fb8fdea018b6). Both 805 × 1001 PNGs were inspected. Only HF search is displayed, unchanged. The Library image has two download-error states and is excluded at the owner’s request; its original file is retained pending a healthy replacement. No exact app source revision or inference result is established by these images.

Earlier source search:

- Enumerated 170 public repository branches; inspected 103 untruncated trees, including main `ad31e391`, the relevant desktop-review branches and playground `bd982b67`.
- Main and inspected desktop branches contain no suitable actual Library GUI capture. Product icons and backend logos are not screenshots.
- Four images exist in [the playground evidence folder at bd982b67](https://github.com/MrScripty/Pumas-Library/tree/bd982b67bb34e57088b5db466b3761809b6a03f6/tools/model-playground/evidence): `real-runtime-browser.png`, `real-untrained-onnx-browser.png`, `simulated-browser-desktop.png`, and `simulated-browser-mobile.png`. They are **playground evidence, not the actual Library GUI**. None was used for the portfolio's Library section.
- The actual Library screenshot referenced by the public README is GitHub attachment `be18cffc-b4fe-418b-a3b4-034ee0b35060`. Its download still fails at the environment proxy with HTTP 403; its pixels and provenance could not be verified here.
- No unpublished local catalog, app changes, or private model data were used.

The supplied HF search view replaces the authored architecture summary in the visible Pumas section. The Library replacement remains pending without a filler or placeholder. Exact original hashes and capture limits are recorded in [capture provenance](assets/capture-provenance.json).

## Icons

The original Pumas Library, Pantograph and Eidetic app icons are verified and used. Whip Docs contains a placeholder app image. Eidetic's owner published the previously local original as root `icon.png` at `cc80011`; its 512 × 512 pixels were inspected and the original bytes are now used. The old packaging placeholders are separate files. No usable standalone icon was found in the reviewed public sources for Tuldok, Rheon, Kenoma, Coding Standards or Passeur; Chrema has no verified public icon. See [the exact inventory and sources](ICON_AUDIT.md).
