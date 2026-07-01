# OH_AbilityRuntime_AllModularObjectExtensionInfos*

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AbilityRuntime_AllModularObjectExtensionInfos* OH_AbilityRuntime_AllModObjExtensionInfosHandle
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示当前应用内所有ModularObjectExtensionAbility信息的集合句柄。该句柄指向一个包含多个[OH_AbilityRuntime_ModObjExtensionInfoHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h) 的集合，可通过[OH_AbilityRuntime_GetCountFromAllModObjExtensionInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-manager-h#oh_abilityruntime_getcountfromallmodobjextensioninfos) 获取集合中元素的数量，并通过[OH_AbilityRuntime_GetModObjExtensionInfoByIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-manager-h#oh_abilityruntime_getmodobjextensioninfobyindex) 按索引遍历获取单个ModularObjectExtensionAbility信息。使用完毕后需通过[OH_AbilityRuntime_ReleaseAllExtensionInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-manager-h#oh_abilityruntime_releaseallextensioninfos) 释放该集合。
 
**起始版本：** 26.0.0
 
**相关模块：** [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)
 
**所在头文件：** [modular_object_extension_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-manager-h)
