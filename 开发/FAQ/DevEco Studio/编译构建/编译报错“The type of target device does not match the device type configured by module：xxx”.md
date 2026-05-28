# 编译报错“The type of target device does not match the device type configured by module：xxx”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-141

**错误描述**
 
指定target设备的类型与模块配置的设备类型不匹配。
 
**可能原因**
 
指定target设备的类型与模块配置的设备类型不匹配。
 

![](assets/编译报错“The%20type%20of%20target%20device%20does%20not%20match%20the%20device%20type%20configured%20by%20module：xxx”/file-20260515130156536-0.png)

 
**解决措施**
 1. 确保module目录的build-profile.json5文件中targets下指定的设备类型包含所需的设备类型。
2. 确保module目录下src/main/module.json5中配置的deviceTypes字段包含所需的类型。
3. 检查hvigorfile.ts或[Hvigor脚本文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-life-cycle#section810245135914)是否包含任何可能更改模块deviceTypes设置的代码。
