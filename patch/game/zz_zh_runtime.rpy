# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ZH runtime localization shim (shipped inside the RPA archive).
#
# Some text in SummertimeSaga does not go through Ren'Py's dialogue/string
# translation tables:
#   * HUD room name       -> Location.display_name
#   * HUD weekday         -> DayTimer.weekdays_long / dayOfWeek()
#   * inventory items     -> scripts/data/items.json ('name'/'description')
#   * achievements        -> A_* achievement objects
#   * prologue narration and other plain Text displayables
#
# Chinese strings come from scripts/data/zh_ui.json. Any English-only Text that
# is not covered is appended to <basedir>/zh_missing_text.log for later work.
# ---------------------------------------------------------------------------

init -100 python:

    import json as _zh_json
    import os as _zh_os

    _ZH_UI = {}
    try:
        _zh_file = renpy.file("scripts/data/zh_ui.json")
        _ZH_UI = _zh_json.loads(_zh_file.read().decode("utf-8"))
        _zh_file.close()
    except Exception:
        _ZH_UI = {}

    _ZH_STRINGS = _ZH_UI.get("strings", {})
    _ZH_ROOMS = _ZH_UI.get("rooms", {})
    _ZH_WEEK = _ZH_UI.get("weekdays", {})
    _ZH_ITEMS = _ZH_UI.get("items", {})
    _ZH_ACH = _ZH_UI.get("achievements", {})
    _ZH_MISSING = set()
    _ZH_LOG_PATH = _zh_os.path.join(renpy.config.basedir, "zh_missing_text.log")

    _ZH_CJK_RANGES = ((0x3400, 0x4dbf), (0x4e00, 0x9fff), (0xf900, 0xfaff))

    def _zh_has_cjk(text):
        for ch in text:
            code = ord(ch)
            for lo, hi in _ZH_CJK_RANGES:
                if lo <= code <= hi:
                    return True
        return False

    def _zh_strip_tags(text):
        out = []
        depth = 0
        for ch in text:
            if ch == u"{":
                depth += 1
            elif ch == u"}":
                if depth > 0:
                    depth -= 1
            elif depth == 0:
                out.append(ch)
        return u"".join(out).strip()

    def _zh_log_missing(text):
        try:
            if not isinstance(text, basestring) or not text:
                return
            if text in _ZH_STRINGS or text in _ZH_MISSING:
                return
            plain = _zh_strip_tags(text)
            if len(plain) < 2 or _zh_has_cjk(plain):
                return
            has_latin = False
            for ch in plain:
                if u"A" <= ch <= u"Z" or u"a" <= ch <= u"z":
                    has_latin = True
                    break
            if not has_latin:
                return
            _ZH_MISSING.add(text)
            handle = open(_ZH_LOG_PATH, "ab")
            try:
                handle.write((text + u"\n").encode("utf-8"))
            finally:
                handle.close()
        except Exception:
            pass

    def _zh_translate_text(value):
        if not isinstance(value, basestring):
            return value
        if value in _ZH_STRINGS:
            return _ZH_STRINGS[value]
        if value.startswith(u"{") and value.endswith(u"}"):
            left = value.find(u"}") + 1
            right = value.rfind(u"{")
            if 0 < left < right:
                head, inner, tail = value[:left], value[left:right], value[right:]
                if inner in _ZH_STRINGS:
                    return head + _ZH_STRINGS[inner] + tail
                if inner in _ZH_WEEK:
                    return head + _ZH_WEEK[inner] + tail
        return value

    # --- hook every Text created by the UI --------------------------------
    _zh_orig_text_init = renpy.text.text.Text.__init__

    def _zh_text_init(self, text, *args, **kwargs):
        try:
            if isinstance(text, basestring):
                new_text = _zh_translate_text(text)
                if new_text is text:
                    _zh_log_missing(text)
                text = new_text
        except Exception:
            pass
        return _zh_orig_text_init(self, text, *args, **kwargs)

    renpy.text.text.Text.__init__ = _zh_text_init


init 900 python:

    _ZH_WEEK_LONG = (u"星期一", u"星期二", u"星期三", u"星期四",
                     u"星期五", u"星期六", u"星期日")

    # --- rooms -------------------------------------------------------------
    try:
        _zh_seen = []
        _zh_seen_ids = set()

        def _zh_walk(loc, depth=0):
            if depth > 40 or id(loc) in _zh_seen_ids:
                return
            _zh_seen_ids.add(id(loc))
            _zh_seen.append(loc)
            for child in loc.children:
                _zh_walk(child, depth + 1)

        for root_loc in store.Location.roots:
            _zh_walk(root_loc)
        rooms_done = 0
        for loc in _zh_seen:
            zh_name = _ZH_ROOMS.get(loc.name)
            if zh_name:
                loc._display_name = zh_name
                rooms_done += 1
        print("[zh] room names patched: %d / %d" % (rooms_done, len(_zh_seen)))
    except Exception, e:
        print("[zh] room patch error: %s" % e)

    # --- weekday display tuples on the timer class -------------------------
    try:
        dow_owners = 0
        for name, value in list(store.__dict__.items()):
            try:
                if isinstance(value, (basestring, dict, list, tuple, int, float)):
                    continue
                if hasattr(value, "weekdays_long"):
                    value.weekdays_long = _ZH_WEEK_LONG
                    dow_owners += 1
            except Exception:
                pass
        print("[zh] weekday tuple owners patched: %d" % dow_owners)
    except Exception, e:
        print("[zh] weekday tuple patch error: %s" % e)

    # --- inventory items ---------------------------------------------------
    try:
        items_done = 0
        for item_id, item in store.items.items():
            entry = _ZH_ITEMS.get(item_id)
            if not entry:
                continue
            try:
                if entry.get("name"):
                    item["name"] = entry["name"]
                if entry.get("description"):
                    item["description"] = entry["description"]
            except (TypeError, AttributeError):
                if entry.get("name"):
                    item.name = entry["name"]
                if entry.get("description"):
                    item.description = entry["description"]
            items_done += 1
        print("[zh] items patched: %d / %d" % (items_done, len(store.items)))
    except Exception, e:
        import traceback
        traceback.print_exc()
        print("[zh] item patch error: %s" % e)

    # --- achievements ------------------------------------------------------
    try:
        ach_done = 0
        for attr in dir(store):
            if not attr.startswith("A_"):
                continue
            obj = getattr(store, attr, None)
            nameid = getattr(obj, "nameid", None)
            if not nameid:
                continue
            entry = _ZH_ACH.get(nameid)
            if not entry:
                continue
            if entry.get("name"):
                obj.name = entry["name"]
            if entry.get("description"):
                obj.description = entry["description"]
            ach_done += 1
        print("[zh] achievements patched: %d" % ach_done)
    except Exception, e:
        print("[zh] achievement patch error: %s" % e)

    # --- runtime fallback: wrap dayOfWeek on the live timer object ---------
    _zh_timer_state = {"done": False}

    def _zh_patch_timer():
        if _zh_timer_state["done"]:
            return
        timer = None
        try:
            timer = store.game.timer
        except Exception:
            timer = None
        if timer is None:
            for value in store.__dict__.values():
                try:
                    if hasattr(value, "dayOfWeek") and hasattr(value, "weekdays_long"):
                        timer = value
                        break
                except Exception:
                    pass
        if timer is None:
            return
        try:
            timer.weekdays_long = _ZH_WEEK_LONG
            original = timer.dayOfWeek

            def _zh_day_of_week(*args, **kwargs):
                result = original(*args, **kwargs)
                if isinstance(result, basestring):
                    return _ZH_WEEK.get(result, result)
                return result

            timer.dayOfWeek = _zh_day_of_week
            _zh_timer_state["done"] = True
            print("[zh] timer.dayOfWeek patched")
        except Exception, e:
            _zh_timer_state["done"] = True
            print("[zh] timer patch error: %s" % e)

    renpy.config.periodic_callbacks.append(_zh_patch_timer)
