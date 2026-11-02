# Product icon inventory

Public-source audit for the dark appearance review, 11–12 October 2026. Existing app branding is reused where verified. No replacement icons, generic framework logos, or generated covers were made.

| Project | Result | Public source inspected |
| --- | --- | --- |
| Pumas Library | **Used:** shipped 512 × 512 custom app icon | [Pumas-Library_05.png at ad31e391](https://github.com/MrScripty/Pumas-Library/blob/ad31e391dcd94c204b3fcd748cc98d27b3281e65/electron/build/icons/Pumas-Library_05.png) |
| Pantograph | **Used:** shipped 512 × 512 custom app icon | [icon.png at 256b6b94](https://github.com/MrScripty/Pantograph/blob/256b6b94ece4dbbaa1fb236bc4092ad08aa63525/src-tauri/icons/icon.png) |
| Tuldok | No standalone icon found; the app has a textual `t.` mark | Main 1bb2c3a and capture branch 6d93935 |
| Eidetic | **Used:** original 512 × 512 silver E / film-reel logo, visually inspected | [Root icon.png at cc80011](https://github.com/MrScripty/Eidetic/blob/cc80011cbf631f7c4774c576ba879dfec1211c6a/icon.png) |
| Rheon | No standalone icon found | Main 34235d3 and capture branch 515212d |
| Kenoma | No standalone icon found | Main e2ea6ac and capture branch 8510719 |
| Coding Standards | No standalone icon found | Main 188beda1 |
| Passeur | No standalone icon found | Main 725c45c |
| Whip Docs | App PNG is a placeholder; language/platform logos are not app branding | Main 3e299d6 |
| Chrema | No public icon verified | Existing public profile overview only; private source was not accessed |

The three currently copied icons retain their original bytes. SHA-256:

- `assets/icons/pumas-icon.png`: `3e9f4267db33be64bf3552bb1a92677c060a3f6dd87eeafb8cc3956697403638`
- `assets/icons/pantograph-icon.png`: `c7ce58f4acbda8c9af51ee663e65d8b3e5275a691f1c53b65c1fa598a013df62`
- `assets/icons/eidetic-icon.png`: `7b063a49f521c4d54fc69e8704cd58f06455b07437e9e9acc6419c376e9e0a86`

“No icon found” describes the reviewed public source, not proof that no icon exists elsewhere. The text names remain on the page until original product artwork is supplied.

## Eidetic correction

The earlier findings described committed packaging placeholders; they did not establish whether original artwork existed outside the repository. The owner confirmed that the actual icon had not yet been pushed, then published it as repository-root `icon.png` in commit `cc80011cbf631f7c4774c576ba879dfec1211c6a` ("chore(assets): add Eidetic logo"). That original is now copied unchanged into the portfolio and displayed beside the Eidetic section title.

The verified asset is a 122,910-byte, 512 × 512 PNG, visually inspected as a silver E mark over a film reel on a dark rounded square. The old 1 × 1 files under `src-tauri/icons/` are separate packaging placeholders and were not selected. No replacement artwork was created. Exact provenance is retained in [eidetic-provenance.json](assets/icons/eidetic-provenance.json).
