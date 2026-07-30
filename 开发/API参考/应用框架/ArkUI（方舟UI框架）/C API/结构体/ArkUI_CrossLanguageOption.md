# ArkUI_CrossLanguageOption

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-crosslanguageoption
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_CrossLanguageOption ArkUI_CrossLanguageOption
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义跨语言配置项，用于配置目标节点的跨语言访问能力，例如是否允许跨语言修改属性；从API version 26.0.0开始，还可配置节点树跨语言操作状态。
 
**起始版本：** 15
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_ArkUI_NodeUtils_SetCrossLanguageOption | 设置目标节点的跨语言配置项。 |
| OH_ArkUI_NodeUtils_GetCrossLanguageOption | 获取目标节点的跨语言配置项。 |
| OH_ArkUI_CrossLanguageOption_Create | 创建跨语言配置项实例。使用完毕后，需调用OH_ArkUI_CrossLanguageOption_Destroy销毁实例。 |
| OH_ArkUI_CrossLanguageOption_Destroy | 销毁跨语言配置项实例。 |
| OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus | 设置配置项中是否允许跨语言修改属性。 |
| OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus | 获取配置项中是否允许跨语言修改属性。 |
| OH_ArkUI_CrossLanguageOption_SetTreeOperatingStatus | 设置跨语言配置项的节点树操作状态。 |
| OH_ArkUI_CrossLanguageOption_GetTreeOperatingStatus | 获取跨语言配置项的节点树操作状态。 |
