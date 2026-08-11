# OH_AbilityRuntime_ModularObjectDispatcher_TypeDescriptor*

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher-typedescriptor8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AbilityRuntime_ModularObjectDispatcher_TypeDescriptor* OH_AbilityRuntime_ModObjDispatcher_TypeDescriptorHandle
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义ModularObject分发器的类型描述符句柄。
 
该句柄指向类型库元数据的访问接口，可用于查询远端服务定义的接口、方法、枚举和结构体等信息。
 
可通过[OH_AbilityRuntime_ModObjDispatcher_GetTypeDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h#oh_abilityruntime_modobjdispatcher_gettypedescriptor)获取，使用完毕后需通过[OH_AbilityRuntime_TypeDescriptor_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h#oh_abilityruntime_typedescriptor_release)释放。
 
**起始版本：** 26.0.0
 
**相关模块：** [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)
 
**所在头文件：** [modular_object_dispatcher.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h)
