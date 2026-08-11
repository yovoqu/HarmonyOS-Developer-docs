# OH_AbilityRuntime_ModularObjectDispatcher_Vector*

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher-vector8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AbilityRuntime_ModularObjectDispatcher_Vector* OH_AbilityRuntime_ModObjDispatcher_VectorHandle
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

向量句柄。
 
该句柄指向一个动态大小的有序元素集合，所有元素类型相同，支持添加元素、按索引获取元素、查询向量大小和清空操作。
 
可通过[OH_AbilityRuntime_ModObjDispatcher_VectorCreate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h#oh_abilityruntime_modobjdispatcher_vectorcreate)创建，使用完毕后需通过[OH_AbilityRuntime_ModObjDispatcher_VectorRelease](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h#oh_abilityruntime_modobjdispatcher_vectorrelease)释放。
 
**起始版本：** 26.0.0
 
**相关模块：** [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)
 
**所在头文件：** [modular_object_dispatcher.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h)
