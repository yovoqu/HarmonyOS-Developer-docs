# 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-166

错误描述

当useNormalizedOHMUrl配置为false时，不支持编译字节码HAR。

可能原因

当HAR模块的build-profile.json5文件中的byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段未配置为true。


![](assets/编译报错“byteCodeHar%20not%20supported%20when%20useNormalizedOHMUrl%20is%20not%20true.”/file-20260515130209253-0.png)


解决措施

当HAR模块的build-profile.json5文件中byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段也必须配置为true。


![](assets/编译报错“byteCodeHar%20not%20supported%20when%20useNormalizedOHMUrl%20is%20not%20true.”/file-20260515130209253-1.png)


参考链接

strictMode
