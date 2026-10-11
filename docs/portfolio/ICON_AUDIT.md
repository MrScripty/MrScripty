# Product icon inventory

Public-source audit for the dark appearance review, 11 October 2026. Existing app branding is reused where verified. No replacement icons, generic framework logos, or generated covers were made.

| Project | Result | Public source inspected |
| --- | --- | --- |
| Pumas Library | **Used:** shipped 512 × 512 custom app icon | [Pumas-Library_05.png at ad31e391](https://github.com/MrScripty/Pumas-Library/blob/ad31e391dcd94c204b3fcd748cc98d27b3281e65/electron/build/icons/Pumas-Library_05.png) |
| Pantograph | **Used:** shipped 512 × 512 custom app icon | [icon.png at 256b6b94](https://github.com/MrScripty/Pantograph/blob/256b6b94ece4dbbaa1fb236bc4092ad08aa63525/src-tauri/icons/icon.png) |
| Tuldok | No standalone icon found; the app has a textual `t.` mark | Main 1bb2c3a and capture branch 6d93935 |
| Eidetic | **Original artwork pending location.** The owner confirms it exists. Reviewed PNG/ICO files are 1 × 1 placeholders and are not used. | Main 7e963d5; native capture 0f3481c; coordinated follow-up across 125 branch heads, icon history, packaging configuration and local generated assets |
| Rheon | No standalone icon found | Main 34235d3 and capture branch 515212d |
| Kenoma | No standalone icon found | Main e2ea6ac and capture branch 8510719 |
| Coding Standards | No standalone icon found | Main 188beda1 |
| Passeur | No standalone icon found | Main 725c45c |
| Whip Docs | App PNG is a placeholder; language/platform logos are not app branding | Main 3e299d6 |
| Chrema | No public icon verified | Existing public profile overview only; private source was not accessed |

The two currently copied icons retain their original bytes. SHA-256:

- `assets/icons/pumas-icon.png`: `3e9f4267db33be64bf3552bb1a92677c060a3f6dd87eeafb8cc3956697403638`
- `assets/icons/pantograph-icon.png`: `c7ce58f4acbda8c9af51ee663e65d8b3e5275a691f1c53b65c1fa598a013df62`

“No icon found” describes the reviewed public source, not proof that no icon exists elsewhere. The text names remain on the page until original product artwork is supplied.

## Eidetic correction

The initial audit established only that `src-tauri/icons/icon.png` was a placeholder. That was insufficient to describe the original icon as unavailable or ask for new artwork. The owner confirms an existing icon. The follow-up checked PNG, ICO, SVG/ICNS candidates, Tauri configuration, icon history, frontend branding and the relevant current branches; the coordinated Eidetic worker checked 125 fetched branch heads and local generated assets. The committed PNG is a 70-byte 1 × 1 black pixel, the 92-byte ICO embeds that same pixel, and the packaging README labels the files placeholders. The real artwork was not located in those reviewed sources. Its location or attachment has been requested; **do not recreate it**. The portfolio keeps the icon slot pending until the original can be inspected and copied.
