# 编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-142

错误描述

仅当兼容SDK版本为5.0.0(12)及以上版本时，useNormalizedOHMUrl才可以设置为true。

可能原因

当compatibleSdkVersion为5.0.0(12)以下版本时，设置useNormalizedOHMUrl为true导致。

解决措施

检查工程级build-profile.json5文件中的compatibleSdkVersion配置。如果compatibleSdkVersion为 4.1.0(11) 及之前版本，请将useNormalizedOHMUrl设置为false。


![](assets/编译报错“useNormalizedOHMUrl%20can%20be%20true%20only%20when%20Compatible%20SDK%20Version%20is%205.0.0%2012%20or%20later”/file-20260515130157143-0.png)
