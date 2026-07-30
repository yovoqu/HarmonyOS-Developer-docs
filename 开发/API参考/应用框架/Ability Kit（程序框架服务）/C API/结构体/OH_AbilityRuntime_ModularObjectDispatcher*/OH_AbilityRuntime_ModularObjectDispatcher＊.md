# OH_AbilityRuntime_ModularObjectDispatcher*

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AbilityRuntime_ModularObjectDispatcher* OH_AbilityRuntime_ModObjDispatcherHandle
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ModularObject分发器的句柄。
 
该句柄指向一个ModularObject分发器实例，可通过[OH_AbilityRuntime_ModObjDispatcher_CreateMainServiceInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h#oh_abilityruntime_modobjdispatcher_createmainserviceinstance)或[OH_AbilityRuntime_ModObjDispatcher_CreateSubInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h#oh_abilityruntime_modobjdispatcher_createsubinstance)创建，使用完毕后需通过[OH_AbilityRuntime_ModObjDispatcher_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h#oh_abilityruntime_modobjdispatcher_release)释放。
 
**起始版本：** 26.0.0
 
**相关模块：** [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)
 
**所在头文件：** [modular_object_dispatcher.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h)
