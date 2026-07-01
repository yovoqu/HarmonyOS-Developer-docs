# AbilityRuntime

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明元能力基础框架的相关能力。
 
**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
 
**起始版本：** 13
 
  

#### 文件汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ability_runtime_common.h | 提供AbilityRuntime模块的错误码。 |
| application_context.h | 提供应用级别上下文相关的接口。 |
| context.h | 提供上下文数据结构AbilityRuntime_Context和相关接口用于获取当前上下文的应用文件路径、数据加密等级和进程名等信息。 |
| context_constant.h | 提供AbilityRuntime模块上下文常量的定义。 |
| extension_ability.h | 提供ExtensionAbility回调函数类型声明和入口函数名称声明。 |
| modular_object_extension_manager.h | 声明用于管理ModularObjectExtensionAbility的接口，包括查询ModularObjectExtensionAbility信息、连接与断开连接等能力。开发者可以通过本模块提供的接口查询当前应用内所有已注册的ModularObjectExtensionAbility的信息（包括启动模式、进程模式、线程模式、组件名称及禁用状态等），并根据需要建立或断开与ModularObjectExtensionAbility的通信连接。 |
| start_options.h | 提供应用启动参数数据结构AbilityRuntime_StartOptions以及设置和获取相关函数。 |
