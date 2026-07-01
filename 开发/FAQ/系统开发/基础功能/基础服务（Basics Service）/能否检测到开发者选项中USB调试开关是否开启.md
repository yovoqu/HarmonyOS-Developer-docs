# 能否检测到开发者选项中USB调试开关是否开启

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-68

#### 问题现象

希望应用内能够检测手机是否开启了USB调试功能，并在检测到该功能开启时，向用户提示可能存在的安全风险。
 
 

#### 解决方案

可以使用[getValueSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-settings#settingsgetvaluesync11)获取，API19开始支持，传入name参数为字符串格式（备注：与[general](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-settings#general)中的settings.general.HDC_STATUS不是同一个值）：'HDC_STATUS'，defValue参数为字符串格式：'NONE'，domainName参数为字符串格式：settings.domainName.DEVICE_SHARED。
