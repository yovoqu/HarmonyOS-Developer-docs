# 编译报错“Cannot resolved import statement”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-140

错误描述

在编译过程中，提示“Cannot resolved import statement”错误信息。

可能原因

导入文件时，大小写不一致会导致问题（导入到单个文件夹时，默认寻址小写 “index.ets”文件，但该文件夹下仅存在大写“index.ets”文件）。


![](assets/编译报错“Cannot%20resolved%20import%20statement”/file-20260515130155967-0.png)


解决措施

检查import文件的大小写。
