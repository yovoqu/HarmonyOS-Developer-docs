# 编译报错“The required attribute module-srcPath is missing”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-137

错误描述

缺少必需属性：module-srcPath。

可能原因

build-profile.json5文件中缺少模块的相对路径，具体表现为module-srcPath字段缺失。


![](assets/编译报错“The%20required%20attribute%20module-srcPath%20is%20missing”/file-20260515130154186-0.png)


解决措施

进入项目根目录下的build-profile.json5文件，确保module下srcPath字段存在且非空。
