# 参与贡献

在 Issues 中提供版本、复现步骤及相关界面，提交修改前请确认没有重复报告。

1. 从 main 创建分支。
2. 修改 `patch/game/tl/chinese/` 译文，保留 translate 标识、说话人、变量占位符和格式标签。
3. 运行时 UI 映射位于 `patch/game/scripts/data/zh_ui.json`；图片位于 `patch/game/images/`，保持尺寸并说明来源。
4. 按 `docs/BUILD.md` 构建，在干净的 0.20.16 游戏副本中验证相关场景。
5. 提交 Pull Request，说明原因、复现及实际验证范围，不提交生成的 `.rpyc`、构建目录或游戏本体。

贡献者应有权提交相应内容，并同意原创贡献按 LICENSE 中对应许可发布；第三方材料保留原许可和署名。不要提交令牌、存档、私人日志或无关原版素材。
