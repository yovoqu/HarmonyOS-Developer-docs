#!/usr/bin/env python3
"""【示例脚本】Windows 版检查入口 — 仅供参照,非工作副本。

工作副本在: E:\\System\\Temp\\harmonyos-docs-pull-win\\check_updates_win.py
两处内容应保持一致,修改后需同步(或直接以 Temp 工作副本为准)。

复用本目录 check_updates.py(Linux 原版,不改)的全部逻辑,只做 Windows 适配:
- 强制 UTF-8 模式(-X utf8 重执行),否则 Windows 默认 GBK 打开 UTF-8 manifest 会崩
- 覆盖 REPO / OUTPUT_FILE / PROGRESS_FILE:中间产物(docs_to_update.json、进度)全落 Temp
- sys.dont_write_bytecode:不在仓库里生成 __pycache__

用法:
  E:/Dev/Env/venvs/harmonyos-docs/Scripts/python.exe <此文件副本或 Temp 工作副本> [--limit N] [--fast] [--resume]
"""
import sys

if not sys.flags.utf8_mode:
    import os
    os.execv(sys.executable, [sys.executable, "-X", "utf8"] + sys.argv)

sys.dont_write_bytecode = True  # 仓库脚本目录不留 __pycache__

from pathlib import Path

REPO = Path(r"E:\Dev\Doc\HarmonyOS-Developer-docs")   # 文档仓库根
SCRIPTS_DIR = REPO / "知识库" / "抓取脚本库"            # Linux 原版脚本所在
HERE = Path(__file__).resolve().parent                 # 中间产物落这里(示例默认本目录;Temp 工作副本落 Temp)

sys.path.insert(0, str(SCRIPTS_DIR))

import check_updates

check_updates.BASE = REPO
check_updates.OUTPUT_FILE = HERE / "docs_to_update.json"
check_updates.PROGRESS_FILE = HERE / ".check_progress.json"

if __name__ == "__main__":
    check_updates.main()
