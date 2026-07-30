# 文件隔离后被隔离文件能否通过系统文管或系统UI查看和操作

更新时间：2026-07-24 01:16:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-privacy-and-security-1

#### 问题现象

通过[文件隔离](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-isolate)API隔离文件后，除了通过[文件隔离恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-restore)和[文件隔离查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-query)API之外，能否通过系统文管或其他途径查看被隔离的文件？能否通过系统UI来操作被隔离的文件（如隔离删除或恢复）？
 
 

#### 解决方案

不能通过系统文管或其他途径查看被隔离的文件，只能通过文件隔离相关API处理。从HarmonyOS 7.0开始，可以通过[hidumper](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper)查看处置记录。无法通过系统UI来操作被隔离的文件（如隔离删除或恢复）。
