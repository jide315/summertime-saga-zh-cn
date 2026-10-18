# -*- coding: utf-8 -*-
# ===========================================================================
#  中文字体覆盖
#
#  原理：
#    本游戏的全部文字最终都请求 DejaVuSans.ttf（Ren'Py 默认字体），
#    游戏自己用 config.font_replacement_map 把粗体/斜体映射到
#    fonts/dejavusans-*.ttf。这些字体都不含汉字，直接显示中文会变成方框。
#
#    Ren'Py 在真正加载字形前会查一次 config.font_replacement_map
#    （renpy/text/font.py: get_font -> get_face），所以只要把「游戏会用到的
#    每一个字体名」都映射到中文字体，就能在不改动任何界面样式的前提下
#    让全游戏切换为中文渲染。这比逐个改 style 更彻底，也不会漏掉
#    {font=...} 文本标签里写死的字体。
#
#  本文件位于 tl/chinese/ 下，因此只在中文模式下生效，
#  不会影响玩家切回英文时的显示。
# ===========================================================================

init 999 python:

    _ZH_FONT = "fonts/NotoSansSC-VF.ttf"

    def _zh_install_font():

        names = set()

        # 1) 加载器里能找到的所有字体文件（含 fonts.rpa 与 renpy/common）
        for _d, _fn in renpy.loader.listdirfiles():
            if _fn.lower().endswith((".ttf", ".otf", ".ttc")):
                names.add(_fn)

        # 2) 已经被游戏映射过的名字，以及它们映射到的目标名字
        for _k, _v in list(renpy.config.font_replacement_map.items()):
            try:
                names.add(_k[0])
                names.add(_v[0])
            except Exception:
                pass

        # 3) Ren'Py 默认字体（即使加载器没列出也要覆盖）
        names.update([
            "DejaVuSans.ttf",
            "DejaVuSans-Bold.ttf",
        ])

        # 覆盖游戏自带的那 3 条粗体/斜体映射：粗体交给 Ren'Py 合成，
        # 斜体对汉字没有意义，直接置 False，避免出现难看的机械倾斜。
        for _n in names:
            for _b in (False, True):
                for _i in (False, True):
                    renpy.config.font_replacement_map[_n, _b, _i] = (_ZH_FONT, _b, False)

        # 幂等：中文字体映射到自己，避免被其它规则二次改写
        renpy.config.font_replacement_map[_ZH_FONT, False, False] = (_ZH_FONT, False, False)
        renpy.config.font_replacement_map[_ZH_FONT, True, False] = (_ZH_FONT, True, False)

        return len(names)

    _zh_font_names = _zh_install_font()
