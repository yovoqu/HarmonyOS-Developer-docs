# AbilityRuntime

更新时间：2026-07-28 11:23:46

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
| connect_options.h | 声明ExtensionAbility的连接选项，包括连接成功、断开连接和连接失败的回调接口。 |
| extension_ability.h | 提供ExtensionAbility回调函数类型声明和入口函数名称声明。 |
| modular_object_dispatcher.h | 声明ModularObject分发器接口，提供基于类型库元数据的跨进程延迟绑定调用能力。开发者可以通过本模块从远端Proxy对象创建主服务或子实例分发器，查询远端服务的类型库元数据（接口/方法/枚举/结构体），并通过成员ID（MemberID）动态调用远端方法，创建与操作容器类型（Array/Vector/Set/Map）和结构体。 |
| modular_object_extension_ability.h | 声明ModularObjectExtensionAbility实例的接口，包括注册生命周期回调函数和获取上下文等能力。 |
| modular_object_extension_context.h | 声明ModularObjectExtensionAbility的上下文接口，包括启动UIAbility、销毁ModularObjectExtensionAbility自身、创建和销毁IPC对象等功能。 |
| modular_object_extension_manager.h | 声明用于管理ModularObjectExtensionAbility的接口，包括查询ModularObjectExtensionAbility信息、连接与断开连接等能力。开发者可以通过本模块提供的接口查询当前应用内所有已注册的ModularObjectExtensionAbility的信息（包括启动模式、进程模式、线程模式、组件名称及禁用状态等），并根据需要建立或断开与ModularObjectExtensionAbility的通信连接。 |
| start_options.h | 提供应用启动参数数据结构AbilityRuntime_StartOptions以及设置和获取相关函数。 |
| native_ability_wrapper.h | 提供NativeAbility数据信息相关接口，用于获取Ability实例ID、Ability名称和napi_env等信息。 |
