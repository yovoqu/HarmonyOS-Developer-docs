# 执行python.exe -m pip install --upgrade pip命令更新pip库时报错ValueError: Unable to find resource t64.exe in package pip._vendor.distlib

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-3

输入python -m pip uninstall pip setuptools卸载setuptools，输入pip install --upgrade setuptools重新安装 setuptools，然后重新执行python -m pip install --upgrade pip更新pip库。
