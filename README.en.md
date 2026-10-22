# Summertime Saga 0.20.16 Simplified Chinese Translation Patch

An unofficial **Simplified Chinese (zh-CN) translation patch for Summertime Saga / SummertimeSaga 0.20.16 on Windows PC**, known in Chinese as **夏日传说**. The installable patch is **`zh_cn.rpa`**. This repository, maintained by [jide315](https://github.com/jide315), includes translation sources and build tools; it does not distribute the base game.

[中文说明、下载与常见问题](README.md)

## Download

Patch release: **v1.0.0**. Target game: **0.20.16 (pre-tech update / old Stable)**.

- [GitHub release and release notes](https://github.com/jide315/summertime-saga-zh-cn/releases/tag/v1.0.0)
- [Download the patch ZIP](https://github.com/jide315/summertime-saga-zh-cn/releases/download/v1.0.0/summertime-saga-0.20.16-zh-cn-v1.0.0.zip), including installation instructions and licenses.
- [Lanzou mirror for users in China](https://wwbnq.lanzn.com/iEMWE4cfjjuf), password: **`e4zp`**. Mirror filename: `SummertimeSaga-0.20.16-zh_CN.zip` (about 24.63 MB). The ZIP packaging differs, but the enclosed `zh_cn.rpa` is identical.

## Installation

1. Obtain your own legitimate copy of **Summertime Saga 0.20.16 for Windows PC**.
2. Exit the game and back up your saves. Move previous Chinese patches, including `zh_cn_2.rpa` or an older `zh_cn.rpa`, out of the game directory. Use a clean game copy if loose translation files were previously installed.
3. Extract the ZIP and copy **`zh_cn.rpa` into the game's `game/` directory**, next to the original `scripts.rpa`. Keep the original archives.
4. Start the game; check language settings if needed. Retain the included copyright and license notices when redistributing the patch.

To uninstall, exit the game and remove only `game/zh_cn.rpa`; switch the language back to English if needed.

## Compatibility and limitations

This release targets **0.20.16, not v21 / Tech Update**. Android, macOS and Linux are unverified. File checks, source compilation and initialization have been performed, but a complete playthrough has **not** been performed. Translation and UI issues may remain; see [validation notes](docs/VALIDATION.md).

## Integrity

`zh_cn.rpa`: **33,438,630 bytes**; SHA-256:

```text
bd1763730d20eeee88a036bdbb322689e5e46c6aabc574df369217138653e08f
```

PowerShell: `Get-FileHash ./zh_cn.rpa -Algorithm SHA256`.

## Sources, feedback and licenses

Source translations and localization assets are in `patch/game/`. See the [build guide](docs/BUILD.md), [contribution guide](CONTRIBUTING.md) and [issue tracker](https://github.com/jide315/summertime-saga-zh-cn/issues).

Original translations and documentation: **CC BY-SA 4.0**. Original code: **MIT**. Noto Sans SC: **SIL OFL 1.1**. Original game text and game-derived artwork retain their respective owners' rights and are excluded from these grants. See [LICENSE](LICENSE) and [third-party notices](THIRD_PARTY_NOTICES.md).
