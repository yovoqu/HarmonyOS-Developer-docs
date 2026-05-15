# DevEco Studio上使用ArcList组件时编辑器提示“The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-18

问题现象

使用ArcList组件时，编辑器报错，错误信息如下：


![](assets/DevEco%20Studio上使用ArcList组件时编辑器提示“The%20default%20system%20capabilities%20of%20devices%20wearable%20do%20not%20include%20SystemCapability.ArkUI.ArkUI.Circle”/file-20260515130030767-0.png)


解决措施

1. 请前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至6.0.1 Release及以上版本。
2. 若仍需使用当前版本，可在src/main目录下添加syscap.json配置文件。可参考[SysCap开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap#syscap开发指导)。


![](assets/DevEco%20Studio上使用ArcList组件时编辑器提示“The%20default%20system%20capabilities%20of%20devices%20wearable%20do%20not%20include%20SystemCapability.ArkUI.ArkUI.Circle”/file-20260515130030767-1.png)
