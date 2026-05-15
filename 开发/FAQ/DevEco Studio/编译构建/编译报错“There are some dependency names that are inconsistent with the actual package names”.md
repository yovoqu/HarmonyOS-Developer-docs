# 编译报错“There are some dependency names that are inconsistent with the actual package names”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-144

错误描述

依赖名称与包名称不匹配。

可能原因

依赖名称与依赖包中oh-package.json5文件的name字段不一致。


![](assets/编译报错“There%20are%20some%20dependency%20names%20that%20are%20inconsistent%20with%20the%20actual%20package%20names”/file-20260515130158330-0.png)


解决措施

将依赖名修改为依赖包在oh-package.json5中定义的name。
