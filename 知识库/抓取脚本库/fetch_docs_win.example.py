#!/usr/bin/env python3
"""【示例脚本】Windows 版拉取入口 — 仅供参照,非工作副本。

工作副本在: E:\\System\\Temp\\harmonyos-docs-pull-win\\fetch_docs_win.py
两处内容应保持一致,修改后需同步(或直接以 Temp 工作副本为准)。

复用本目录 fetch_docs.py(Linux 原版,不改)的全部逻辑,只做 Windows 适配:
- 强制 UTF-8 模式(-X utf8 重执行)
- 覆盖 REPO;docs_to_update.json 从 Temp 目录读(原版 main() 硬编码读仓库根,
  这里包一层:临时拷到仓库根 → 跑完删除,仓库根不残留)
- 补丁 build_image_map:str(Path) 反斜杠换回 /,否则图片链接坏
- sys.dont_write_bytecode:不在仓库里生成 __pycache__

用法:
  E:/Dev/Env/venvs/harmonyos-docs/Scripts/python.exe <此文件副本或 Temp 工作副本>
"""
import sys

if not sys.flags.utf8_mode:
    import os
    os.execv(sys.executable, [sys.executable, "-X", "utf8"] + sys.argv)

sys.dont_write_bytecode = True  # 仓库脚本目录不留 __pycache__

import shutil
from pathlib import Path

REPO = Path(r"E:\Dev\Doc\HarmonyOS-Developer-docs")   # 文档仓库根
SCRIPTS_DIR = REPO / "知识库" / "抓取脚本库"            # Linux 原版脚本所在
HERE = Path(__file__).resolve().parent                 # 中间产物落这里(示例默认本目录;Temp 工作副本落 Temp)

sys.path.insert(0, str(SCRIPTS_DIR))

import fetch_docs

fetch_docs.BASE = REPO

# Windows 补丁:原版 build_image_map 用 str(Path) 拼资产路径,
# Windows 上产出反斜杠(assets\xx\a.png),会破坏 Markdown 图片链接。
_orig_build_image_map = fetch_docs.build_image_map

def build_image_map(html, doc_file_path):
    m = _orig_build_image_map(html, doc_file_path)
    return {url: path.replace("\\", "/") for url, path in m.items()}

fetch_docs.build_image_map = build_image_map

# 原版 main() 硬编码从 仓库根/docs_to_update.json 读。
# 检查版已把该文件写到 Temp 目录,这里临时拷回、跑完删掉,仓库根不残留。
_orig_main = fetch_docs.main

def main():
    src = HERE / "docs_to_update.json"
    dst = REPO / "docs_to_update.json"
    if not src.exists():
        print(f"未找到 {src},请先运行 check_updates_win.py")
        return
    shutil.copyfile(src, dst)
    try:
        _orig_main()
    finally:
        dst.unlink(missing_ok=True)

fetch_docs.main = main

if __name__ == "__main__":
    fetch_docs.main()
