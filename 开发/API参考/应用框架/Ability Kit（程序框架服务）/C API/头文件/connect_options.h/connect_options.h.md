# connect_options.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-connect-options-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明ExtensionAbility的连接选项，包括连接成功、断开连接和连接失败的回调接口。
 
**引用文件：** <AbilityKit/ability_runtime/connect_options.h>
 
**库：** libability_runtime.so
 
**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AbilityRuntime_ConnectOptions | OH_AbilityRuntime_ConnectOptions | 定义OH_AbilityRuntime_ConnectOptions结构体类型。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_AbilityRuntime_ConnectOptions_OnConnectCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityBase_Element *element, OHIPCRemoteProxy *proxy) | OH_AbilityRuntime_ConnectOptions_OnConnectCallback | 连接成功时触发的回调函数。 |
| typedef void (*OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityBase_Element *element) | OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback | 断开连接时触发的回调函数。 |
| typedef void (*OH_AbilityRuntime_ConnectOptions_OnFailedCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityRuntime_ErrorCode code) | OH_AbilityRuntime_ConnectOptions_OnFailedCallback | 连接失败时触发的回调函数。 |
| OH_AbilityRuntime_ConnectOptions* OH_AbilityRuntime_CreateConnectOptions() | - | 创建一个ConnectOptions对象。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_DestroyConnectOptions(OH_AbilityRuntime_ConnectOptions *connectOptions) | - | 销毁指定的ConnectOptions对象。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnConnectCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnConnectCallback onConnectCallback) | - | 在OH_AbilityRuntime_ConnectOptions中设置连接成功回调OH_AbilityRuntime_ConnectOptions_OnConnectCallback。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnDisconnectCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback onDisconnectCallback) | - | 在OH_AbilityRuntime_ConnectOptions中设置断开连接回调OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnFailedCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnFailedCallback onFailedCallback) | - | 在OH_AbilityRuntime_ConnectOptions中设置连接失败回调OH_AbilityRuntime_ConnectOptions_OnFailedCallback。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_AbilityRuntime_ConnectOptions_OnConnectCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_AbilityRuntime_ConnectOptions_OnConnectCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityBase_Element *element, OHIPCRemoteProxy *proxy)
```
 
**描述**
 
连接成功时触发的回调函数。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions *connectOptions | 指向OH_AbilityRuntime_ConnectOptions实例的指针。 |
| AbilityBase_Element *element | 表示ExtensionAbility的组件名称。 |
| OHIPCRemoteProxy *proxy | 表示远端对象实例。 |
 
 
  

#### OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityBase_Element *element)
```
 
**描述**
 
断开连接时触发的回调函数。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions *connectOptions | 指向OH_AbilityRuntime_ConnectOptions实例的指针。 |
| AbilityBase_Element *element | 表示ExtensionAbility的组件名称。 |
 
 
  

#### OH_AbilityRuntime_ConnectOptions_OnFailedCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_AbilityRuntime_ConnectOptions_OnFailedCallback)(OH_AbilityRuntime_ConnectOptions *connectOptions, AbilityRuntime_ErrorCode code)
```
 
**描述**
 
连接失败时触发的回调函数。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions *connectOptions | 指向OH_AbilityRuntime_ConnectOptions实例的指针。 |
| AbilityRuntime_ErrorCode code | 表示失败的错误码。 |
 
 
  

#### OH_AbilityRuntime_CreateConnectOptions()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_AbilityRuntime_ConnectOptions* OH_AbilityRuntime_CreateConnectOptions()
```
 
**描述**
 
创建一个ConnectOptions对象。
 
**起始版本：** 26.0.0
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions* | 返回新创建的OH_AbilityRuntime_ConnectOptions对象。 调用方需调用OH_AbilityRuntime_DestroyConnectOptions销毁返回的对象，避免内存泄漏。 |
 
 
  

#### OH_AbilityRuntime_DestroyConnectOptions()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_DestroyConnectOptions(OH_AbilityRuntime_ConnectOptions *connectOptions)
```
 
**描述**
 
销毁指定的ConnectOptions对象。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions *connectOptions | 待销毁的ConnectOptions对象。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回特定的错误码。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID connectOptions无效。 |
 
 
  

#### OH_AbilityRuntime_ConnectOptions_SetOnConnectCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnConnectCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnConnectCallback onConnectCallback)
```
 
**描述**
 
在[OH_AbilityRuntime_ConnectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-connectoptions)中设置连接成功回调[OH_AbilityRuntime_ConnectOptions_OnConnectCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-connect-options-h#oh_abilityruntime_connectoptions_onconnectcallback)。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions *connectOptions | 指向待设置的OH_AbilityRuntime_ConnectOptions实例的指针。 |
| OH_AbilityRuntime_ConnectOptions_OnConnectCallback onConnectCallback | 表示待设置的OH_AbilityRuntime_ConnectOptions_OnConnectCallback回调函数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回特定的错误码。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR 接口调用成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID 参数校验失败。 |
 
 
  

#### OH_AbilityRuntime_ConnectOptions_SetOnDisconnectCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnDisconnectCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback onDisconnectCallback)
```
 
**描述**
 
在[OH_AbilityRuntime_ConnectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-connectoptions)中设置断开连接回调[OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-connect-options-h#oh_abilityruntime_connectoptions_ondisconnectcallback)。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions *connectOptions | 指向待设置的OH_AbilityRuntime_ConnectOptions实例的指针。 |
| OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback onDisconnectCallback | 表示待设置的OH_AbilityRuntime_ConnectOptions_OnDisconnectCallback回调函数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回特定的错误码。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR 接口调用成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID 参数校验失败。 |
 
 
  

#### OH_AbilityRuntime_ConnectOptions_SetOnFailedCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectOptions_SetOnFailedCallback(OH_AbilityRuntime_ConnectOptions *connectOptions, OH_AbilityRuntime_ConnectOptions_OnFailedCallback onFailedCallback)
```
 
**描述**
 
在[OH_AbilityRuntime_ConnectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-connectoptions)中设置连接失败回调[OH_AbilityRuntime_ConnectOptions_OnFailedCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-connect-options-h#oh_abilityruntime_connectoptions_onfailedcallback)。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AbilityRuntime_ConnectOptions *connectOptions | 指向待设置的OH_AbilityRuntime_ConnectOptions实例的指针。 |
| OH_AbilityRuntime_ConnectOptions_OnFailedCallback onFailedCallback | 表示待设置的OH_AbilityRuntime_ConnectOptions_OnFailedCallback回调函数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回特定的错误码。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR 接口调用成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID 参数校验失败。 |
