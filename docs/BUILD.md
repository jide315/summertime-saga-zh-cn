# 从源码构建

需要 Python 3.10 或更新版本、Windows，以及自行取得的 Summertime Saga **0.20.16 Windows PC** 完整副本（含 `lib/windows-i686/python.exe` 和 `SummertimeSaga.py`）。不需要额外 pip 依赖。

在仓库根目录执行，将路径替换为本地游戏目录：

```powershell
python tools/build.py --game-dir 'D:/Games/SummertimeSaga-0-20-16-pc'
python tools/verify.py dist
```

生成 `dist/zh_cn.rpa` 与 `dist/SHA256SUMS.txt`。工具在仓库 `.build/` 中创建临时工程，只链接原版归档、复制补丁源码，再调用游戏自带 Ren'Py 编译器。编译产物和字体、图片、UI JSON 被打入 RPA-3.0；工具不会将补丁安装到输入游戏目录。

`patch/game/` 是源码维护入口；修改前请保留变量、格式标签、翻译块 ID 和文件编码。不要把游戏完整脚本或资源目录复制到仓库。

根目录 `zh_cn.rpa` 是原始发布包的改名副本。构建时会重新编译源码并添加字体许可文件，因此新归档不保证与原始归档逐字节相同。构建成功仅表示编译和打包成功，仍需安装到干净游戏副本测试相关场景。

分发时将补丁、校验文件、README、安装说明、LICENSE、LICENSES 和 THIRD_PARTY_NOTICES.md 一并打包。新发布应更新版本、CHANGELOG 和校验值；不要沿用初始归档的校验和。
