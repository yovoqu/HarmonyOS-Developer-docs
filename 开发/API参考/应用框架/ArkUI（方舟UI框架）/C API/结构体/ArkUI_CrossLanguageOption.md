# ArkUI_CrossLanguageOption

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-crosslanguageoption
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_CrossLanguageOption ArkUI_CrossLanguageOption
```
  

##### 概述

定义跨语言配置项。
 
**起始版本：** 15
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_ArkUI_NodeUtils_SetCrossLanguageOption | 设置目标节点跨语言设置属性的能力。 |
| OH_ArkUI_NodeUtils_GetCrossLanguageOption | 获取目标节点跨语言设置属性的配置项。 |
| OH_ArkUI_CrossLanguageOption_Create | 创建跨语言配置项实例。 |
| OH_ArkUI_CrossLanguageOption_Destroy | 销毁跨语言配置项实例。 |
| OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus | 设置配置项中是否允许跨语言修改属性。 |
| OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus | 获取配置项中是否允许跨语言修改属性。 |
