# MindSpore

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供MindSpore Lite的模型推理相关接口，该模块下的接口是非线程安全的。
 
**系统能力：** SystemCapability.Ai.MindSpore
 
**起始版本：** 9
 
  

##### 文件汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| context.h | 提供了Context相关的接口，可以配置运行时信息，该接口是非线程安全的。 |
| data_type.h | 声明了张量的数据的类型。 |
| format.h | 提供张量数据的排列格式。 |
| model.h | 提供了模型相关接口，可以用于模型创建、模型推理等，该接口是非线程安全的。 |
| status.h | 提供了MindSpore Lite运行时的状态码。 |
| tensor.h | 提供了张量相关的接口，可用于创建和修改张量信息，该接口是非线程安全的。 |
| types.h | 提供了MindSpore Lite支持的模型文件类型和设备类型。 |
