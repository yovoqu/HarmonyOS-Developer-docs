# DevEco Studio上使用使用api或组件时编辑器提示各种报错与告警

更新时间：2026-07-15 01:45:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-18

#### 场景1

使用ArcList组件时编辑器提示"The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle"。
 
**问题现象**
 
使用ArcList组件时，编辑器报错，错误信息如下：
 

![](assets/DevEco%20Studio上使用ArcList组件时编辑器提示“The%20default%20system%20capabilities%20of%20devices%20wearable%20do%20not%20include%20SystemCapability.ArkUI.ArkUI.Circle”/file-20260515130030767-0.png)

 
**解决措施**
 
请前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至6.0.1 Release及以上版本。
 
 

#### 场景2

使用被@test标注的api或组件属性时编辑报错："This API can only be used for unit test code"。
 
**问题现象**
 
使用被@test标注的api或组件属性时，例如通用组件属性key时，编辑器会报错，错误信息如下：
 

![](assets/DevEco%20Studio上使用ArcList组件时编辑器提示“The%20default%20system%20capabilities%20of%20devices%20wearable%20do%20not%20include%20SystemCapability.ArkUI.ArkUI.Circle”/file-20260515130030767-1.png)

 
**原因说明**
 
HarmonyOS目前采用jsdoc系统来标记各个api与组件属性能力与限制，被@test标注的api或组件属性表示该api或组件属性应当在测试目录下使用，因此编辑器在检查到被@test标注的api或组件属性在非测试代码中使用时会进行报错提示。
 
**解决措施**
 
请前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至26.0.0 Beta2及以上版本。
