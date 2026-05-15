# 编译报错“Duplicate 'Module-Abilities' object names detected.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-167

错误描述

Module-Abilities对象名称重复。

可能原因

依赖的HAR模块中module.json5的abilities数组中存在重复的ability对象名称。


![](assets/编译报错“Duplicate%20'Module-Abilities'%20object%20names%20detected.”/file-20260515130210167-0.png)


解决措施

检查依赖的HAR模块在module.json5文件中的abilities字段，确保每个ability的name唯一。
