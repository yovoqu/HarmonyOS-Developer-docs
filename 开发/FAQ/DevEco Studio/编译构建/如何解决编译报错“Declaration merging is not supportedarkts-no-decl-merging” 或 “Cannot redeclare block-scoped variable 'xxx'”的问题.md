# 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-127

问题现象

在不同的文件中声明相同变量、interface、enum等类型，DevEco Studio不报错，但编译时会报错。


![](assets/如何解决编译报错“Declaration%20merging%20is%20not%20supportedarkts-no-decl-merging”%20或%20“Cannot%20redeclare%20block-scoped%20variable%20'xxx'”的问题/file-20260515130147492-0.png)


解决方案

如果文件中不包含export关键字，该文件将视为全局命名空间的一部分。
