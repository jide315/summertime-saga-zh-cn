# Summertime Saga 简体中文汉化

适用于 **Summertime Saga 0.20.16 / Windows PC** 的非官方简体中文补丁。包含翻译源码、界面补丁及构建工具，不包含游戏本体、原版脚本归档、音乐或完整美术资源。

**补丁版本：v1.0.0；目标游戏版本：0.20.16。** 其他版本及平台未经验证，请勿直接用于 21.x / Tech Update。

## 下载与安装

| 下载入口 | 压缩包 | 提取密码 |
|---|---|---|
| [蓝奏云（国内下载）](https://wwbnq.lanzn.com/iEMWE4cfjjuf) | `SummertimeSaga-0.20.16-zh_CN.zip`（约 24.63 MB） | `e4zp` |
| [GitHub Releases](https://github.com/jide315/summertime-saga-zh-cn/releases/latest) | `summertime-saga-0.20.16-zh-cn-v1.0.0.zip` | 无 |

两个入口均提供 v1.0.0 补丁及配套许可；压缩包的文件名与附带文档有所不同，`zh_cn.rpa` 内容相同。国内用户可优先使用蓝奏云。

1. 从上述任一入口下载 ZIP，解压后找到 **`zh_cn.rpa`**。保留随包的许可及版权说明，转载时一并附带。
2. 退出游戏并备份存档。将旧汉化包移到游戏目录外，包括旧 `zh_cn_2.rpa` 和其他版本的 `zh_cn.rpa`。安装过散装汉化时建议使用干净游戏副本。
3. 把 `zh_cn.rpa` 放入游戏的 **`game/`** 文件夹，与 `scripts.rpa` 等原版归档同级，保留原版文件。
4. 启动游戏。如未显示中文，请检查路径、残留补丁及设置中的语言选项。

```text
SummertimeSaga-0-20-16-pc/
├── SummertimeSaga.exe
└── game/
    ├── scripts.rpa
    └── zh_cn.rpa
```

卸载：退出游戏，只移除本补丁 `game/zh_cn.rpa`，必要时在设置中切回英文。补丁不会主动转换存档；不保证与其他修改兼容。

安装路径参考 [官方翻译说明](https://summertimesaga.com/translations) 和 [PC 安装说明](https://wiki.summertimesaga.com/Translations/Installation/PC)。官方页面上的旧社区包与本项目是独立项目。

## 校验

文件大小：33,438,630 字节；SHA-256：

```text
bd1763730d20eeee88a036bdbb322689e5e46c6aabc574df369217138653e08f
```

PowerShell：`Get-FileHash ./zh_cn.rpa -Algorithm SHA256`；Linux：`sha256sum -c SHA256SUMS.txt`。

## 汉化范围与限制

- 剧情、界面翻译、运行时界面文字映射、42 张中文按钮图片、1 段菜单动画及 Noto Sans SC 字体。
- 部分技术字符串、专有名词和语言梗可能保留英文或采用近似翻译。
- 本次整理未完成全流程通关，不能承诺全部场景均无问题；实际检查结果见 [验证记录](docs/VALIDATION.md)。

## 开发与贡献

详见 [构建说明](docs/BUILD.md) 和 [贡献指南](CONTRIBUTING.md)。构建需要自行准备合法获取的 0.20.16 Windows 游戏副本；游戏及引擎不随仓库分发。

```text
patch/game/       翻译源文件、界面补丁和字体
tools/           构建与发布校验工具
docs/            构建说明与验证记录
LICENSES/        完整许可文本
zh_cn.rpa        可直接安装的初始补丁
SHA256SUMS.txt   补丁校验和
```

## 许可与署名

- 原创翻译文本及文档：**CC BY-SA 4.0**，允许商用，须署名、注明修改并以相同许可共享。署名建议：`jide315 / summertime-saga-zh-cn contributors`，并附仓库链接。
- 原创工具与补丁代码：**MIT**。
- Noto Sans SC：**SIL OFL 1.1**。
- 游戏原文、人物、商标及游戏衍生 UI 图片等第三方内容保留原权利人的权利，不因本仓库公开而获得额外开放授权。本项目与 Kompas Productions 无官方关联。

完整范围见 [LICENSE](LICENSE) 与 [第三方声明](THIRD_PARTY_NOTICES.md)。整个混合素材补丁不具有统一 MIT 或 CC 授权。

## 反馈

在 [Issues](https://github.com/jide315/summertime-saga-zh-cn/issues) 提供游戏版本、补丁版本、系统、复现步骤及相关截图。可附清理过的 `zh_missing_text.log` 片段；该日志只是诊断线索，不代表完整漏译列表。不要上传游戏本体、存档、凭证或个人信息。
