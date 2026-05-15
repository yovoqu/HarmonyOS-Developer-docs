# 编译报错“Unrecognized archive format in parameterFile”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-157

错误描述

parameterFile中包含无法识别的格式。

可能原因

使用parameterFile参数化配置的本地依赖既不是目录，也不是.har或.tgz文件。


![](assets/编译报错“Unrecognized%20archive%20format%20in%20parameterFile”/file-20260515130203530-0.png)


解决措施

将本地依赖修改为模块目录或模块编译后的har/tgz文件。
