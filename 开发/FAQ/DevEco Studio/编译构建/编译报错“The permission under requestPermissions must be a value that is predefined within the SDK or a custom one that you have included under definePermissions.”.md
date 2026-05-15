# 编译报错“The permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-163

错误描述

requestPermissions下的权限必须是SDK中预定义的值，或在definePermissions中定义的自定义值。

可能原因

在module.json5文件的requestPermissions中配置name时，使用了不存在的权限名称或者使用了当前版本不支持的权限。


![](assets/编译报错“The%20permission%20under%20requestPermissions%20must%20be%20a%20value%20that%20is%20predefined%20within%20the%20SDK%20or%20a%20custom%20one%20that%20you%20have%20included%20under%20definePermissions.”/file-20260515130207455-0.png)


解决措施

在module.json5文件的requestPermissions中配置name字段时，必须使用SDK中预定义的权限或在definePermissions下自定义的权限。如果使用了当前版本不支持的权限，建议升级API版本。

例如，若在DevEco Studio 6.0.0 Release版本使用了ohos.permission.START_WINDOW_BELOW_LOCK_SCREEN权限，但该权限从API 21开始支持，建议开发者前往下载中心将DevEco Studio更新至DevEco Studio 6.0.1 Release及以上版本。
