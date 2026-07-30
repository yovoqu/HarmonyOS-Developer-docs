# metadata_output.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明元数据输出概念。
 
**引用文件：** <ohcamera/metadata_output.h>
 
**库：** libohcamera.so
 
**系统能力：** SystemCapability.Multimedia.Camera.Core
 
**起始版本：** 11
 
**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| MetadataOutput_Callbacks | MetadataOutput_Callbacks | 元数据输出的回调。 |
| Camera_MetadataOutput | Camera_MetadataOutput | 元数据输出对象。 可以使用OH_CameraManager_CreateMetadataOutput方法创建指针。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_MetadataOutput_OnMetadataObjectAvailable)(Camera_MetadataOutput* metadataOutput, Camera_MetadataObject* metadataObject, uint32_t size) | OH_MetadataOutput_OnMetadataObjectAvailable | 在MetadataOutput_Callbacks中被调用的元数据输出元数据对象可用回调。 |
| typedef void (*OH_MetadataOutput_OnError)(Camera_MetadataOutput* metadataOutput, Camera_ErrorCode errorCode) | OH_MetadataOutput_OnError | 在MetadataOutput_Callbacks中被调用的元数据输出错误回调。 |
| Camera_ErrorCode OH_MetadataOutput_RegisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback) | - | 注册元数据输出更改事件回调。 |
| Camera_ErrorCode OH_MetadataOutput_UnregisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback) | - | 注销元数据输出更改事件回调。 |
| Camera_ErrorCode OH_MetadataOutput_Start(Camera_MetadataOutput* metadataOutput) | - | 启动元数据输出。 |
| Camera_ErrorCode OH_MetadataOutput_Stop(Camera_MetadataOutput* metadataOutput) | - | 停止元数据输出。 |
| Camera_ErrorCode OH_MetadataOutput_Release(Camera_MetadataOutput* metadataOutput) | - | 释放元数据输出实例。 |
| Camera_ErrorCode OH_MetadataOutput_AddMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size) | - | 添加元数据对象类型。 |
| Camera_ErrorCode OH_MetadataOutput_RemoveMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size) | - | 移除元数据对象类型。 |
| typedef void (*OH_MetadataOutput_OnMetadataObjectExtAvailable)(void* context, OH_Camera_MetadataObjectExt** metadataObjectExt, uint32_t size) | OH_MetadataOutput_OnMetadataObjectExtAvailable | 用于监听元数据对象上报事件的回调。使用OH_MetadataOutput_RegisterMetadataObjectExtAvailableCallback进行注册。 |
| typedef void (*OH_MetadataOutput_OnErrorExt)(void* context, Camera_ErrorCode errorCode) | OH_MetadataOutput_OnErrorExt | 在元数据输出期间，用于监听错误事件的回调。 |
| Camera_ErrorCode OH_MetadataOutput_RegisterMetadataObjectExtAvailableCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnMetadataObjectExtAvailable callback) | - | 注册监听元数据对象上报事件的回调。该回调可通过OH_MetadataOutput_UnregisterMetadataObjectExtAvailableCallback注销。 |
| Camera_ErrorCode OH_MetadataOutput_UnregisterMetadataObjectExtAvailableCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnMetadataObjectExtAvailable callback) | - | 注销监听元数据对象上报事件的回调。 |
| Camera_ErrorCode OH_MetadataOutput_RegisterErrorExtCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnErrorExt callback) | - | 注册监听错误事件的回调。该回调可通过OH_MetadataOutput_UnregisterErrorExtCallback注销。 |
| Camera_ErrorCode OH_MetadataOutput_UnregisterErrorExtCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnErrorExt callback) | - | 注销监听错误事件的回调。 |
| bool OH_MetadataOutput_IsLockMetadataObjectTrackingSupported(const Camera_MetadataOutput* metadataOutput) | - | 检查设备是否支持锁定元数据对象（如猫脸、狗脸）追踪功能。 |
| Camera_ErrorCode OH_MetadataOutput_LockMetadataObjectTracking(Camera_MetadataOutput* metadataOutput, Camera_Point* pointOfInterest) | - | 锁定对特定元数据对象（如猫脸、狗脸）的追踪。 该功能以pointOfInterest所指向的点所在的对象为追踪对象，如果该点不存在追踪对象，则功能不生效。 被锁定追踪的对象离开取景范围超过三秒或调用解锁追踪后，锁定追踪自动取消。 |
| Camera_ErrorCode OH_MetadataOutput_UnlockMetadataObjectTracking(Camera_MetadataOutput* metadataOutput) | - | 解锁元数据对象（如猫脸、狗脸）的追踪。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_MetadataOutput_OnMetadataObjectAvailable()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_MetadataOutput_OnMetadataObjectAvailable)(Camera_MetadataOutput* metadataOutput, Camera_MetadataObject* metadataObject, uint32_t size)
```
 
**描述**
 
在[MetadataOutput_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)中被调用的元数据输出元数据对象可用回调。
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 传递回调的元数据输出实例。 |
| Camera_MetadataObject* metadataObject | 回调传递的元数据实例信息。 |
| uint32_t size | 元数据对象的大小。 |
 
 
  

#### OH_MetadataOutput_OnError()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_MetadataOutput_OnError)(Camera_MetadataOutput* metadataOutput, Camera_ErrorCode errorCode)
```
 
**描述**
 
在[MetadataOutput_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)中被调用的元数据输出错误回调。
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 传递回调的元数据输出实例。 |
| Camera_ErrorCode errorCode | 元数据输出的错误码。 |
 
 
**参考：**
 
[CAMERA_SERVICE_FATAL_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)
 
  

#### OH_MetadataOutput_RegisterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_RegisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
```
 
**描述**
 
注册元数据输出更改事件回调。
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例。 |
| MetadataOutput_Callbacks* callback | 要注册的元数据输出回调。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |
 
 
  

#### OH_MetadataOutput_UnregisterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_UnregisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
```
 
**描述**
 
注销元数据输出更改事件回调。
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例。 |
| MetadataOutput_Callbacks* callback | 要注销的元数据输出回调。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |
 
 
  

#### OH_MetadataOutput_Start()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_Start(Camera_MetadataOutput* metadataOutput)
```
 
**描述**
 
启动元数据输出。
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 要启动的元数据输出实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |
 
 
  

#### OH_MetadataOutput_Stop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_Stop(Camera_MetadataOutput* metadataOutput)
```
 
**描述**
 
停止元数据输出。
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 要停止的元数据输出实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |
 
 
  

#### OH_MetadataOutput_Release()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_Release(Camera_MetadataOutput* metadataOutput)
```
 
**描述**
 
释放元数据输出实例。
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 要释放的元数据输出实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |
 
 
  

#### OH_MetadataOutput_AddMetadataObjectTypes()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_AddMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
```
 
**描述**
 
添加元数据对象类型。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例。 |
| Camera_MetadataObjectType* types | 用于添加到Camera_MetadataOutput实例的元数据对象类型数组。 |
| uint32_t size | 元数据对象类型数组长度。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |
 
 
  

#### OH_MetadataOutput_RemoveMetadataObjectTypes()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_RemoveMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
```
 
**描述**
 
移除元数据对象类型。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例。 |
| Camera_MetadataObjectType* types | 从Camera_MetadataOutput实例移除的元数据对象类型数组。 |
| uint32_t size | 元数据对象类型数组长度。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |
 
 
  

#### OH_MetadataOutput_OnMetadataObjectExtAvailable()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_MetadataOutput_OnMetadataObjectExtAvailable)(void* context, OH_Camera_MetadataObjectExt** metadataObjectExt, uint32_t size)
```
 
**描述**
 
用于监听元数据对象上报事件的回调。使用[OH_MetadataOutput_RegisterMetadataObjectExtAvailableCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h#oh_metadataoutput_registermetadataobjectextavailablecallback)进行注册。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| void* context | 用户提供的上下文指针。 |
| OH_Camera_MetadataObjectExt** metadataObjectExt | 指向元数据对象的二级指针。 |
| uint32_t size | 元数据对象的数量。 |
 
 
  

#### OH_MetadataOutput_OnErrorExt()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_MetadataOutput_OnErrorExt)(void* context, Camera_ErrorCode errorCode)
```
 
**描述**
 
在元数据输出期间，用于监听错误事件的回调。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| void* context | 用户提供的上下文指针。 |
| Camera_ErrorCode errorCode | 元数据输出期间报告的错误码。 |
 
 
  

#### OH_MetadataOutput_RegisterMetadataObjectExtAvailableCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_RegisterMetadataObjectExtAvailableCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnMetadataObjectExtAvailable callback)
```
 
**描述**
 
注册监听元数据对象上报事件的回调。该回调可通过[OH_MetadataOutput_UnregisterMetadataObjectExtAvailableCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h#oh_metadataoutput_unregistermetadataobjectextavailablecallback)注销。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例的指针。 |
| void* context | 用户提供的上下文指针。 |
| OH_MetadataOutput_OnMetadataObjectExtAvailable* callback | 监听元数据对象上报事件的回调的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：操作成功。 CAMERA_INVALID_ARGUMENT：参数缺失或参数类型错误。 |
 
 
  

#### OH_MetadataOutput_UnregisterMetadataObjectExtAvailableCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_UnregisterMetadataObjectExtAvailableCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnMetadataObjectExtAvailable callback)
```
 
**描述**
 
注销监听元数据对象上报事件的回调。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例的指针。 |
| void* context | 用户提供的上下文指针。 |
| OH_MetadataOutput_OnMetadataObjectExtAvailable* callback | 监听元数据对象上报事件的回调的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：操作成功。 CAMERA_INVALID_ARGUMENT：参数缺失或参数类型错误。 |
 
 
  

#### OH_MetadataOutput_RegisterErrorExtCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_RegisterErrorExtCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnErrorExt callback)
```
 
**描述**
 
注册监听错误事件的回调。该回调可通过[OH_MetadataOutput_UnregisterErrorExtCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h#oh_metadataoutput_unregistererrorextcallback)注销。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例的指针。 |
| void* context | 用户提供的上下文指针。 |
| OH_MetadataOutput_OnErrorExt* callback | 监听错误事件的回调的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：操作成功。 CAMERA_INVALID_ARGUMENT：参数缺失或参数类型错误。 |
 
 
  

#### OH_MetadataOutput_UnregisterErrorExtCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_UnregisterErrorExtCallback(Camera_MetadataOutput* metadataOutput, void* context, OH_MetadataOutput_OnErrorExt callback)
```
 
**描述**
 
注销监听错误事件的回调。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例的指针。 |
| void* context | 用户提供的上下文指针。 |
| OH_MetadataOutput_OnErrorExt* callback | 监听错误事件的回调的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：操作成功。 CAMERA_INVALID_ARGUMENT：参数缺失或参数类型错误。 |
 
 
  

#### OH_MetadataOutput_IsLockMetadataObjectTrackingSupported()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool OH_MetadataOutput_IsLockMetadataObjectTrackingSupported(const Camera_MetadataOutput* metadataOutput)
```
 
**描述**
 
检查设备是否支持锁定元数据对象（如猫脸、狗脸）追踪功能。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | MetadataOutput实例的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| bool | true表示支持该功能。 false表示不支持该功能。 |
 
 
  

#### OH_MetadataOutput_LockMetadataObjectTracking()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_LockMetadataObjectTracking(Camera_MetadataOutput* metadataOutput, Camera_Point* pointOfInterest)
```
 
**描述**
 
锁定对特定元数据对象（如猫脸、狗脸）的追踪。
 
 该功能以pointOfInterest所指向的点所在的对象为追踪对象，如果该点不存在追踪对象，则功能不生效。
 
 被锁定追踪的对象离开取景范围超过三秒或调用解锁追踪后，锁定追踪自动取消。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例的指针。 |
| Camera_Point* pointOfInterest | 期望追踪对应位置对象的点的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：操作成功。 CAMERA_INVALID_ARGUMENT：参数缺失或参数类型错误。 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |
 
 
  

#### OH_MetadataOutput_UnlockMetadataObjectTracking()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Camera_ErrorCode OH_MetadataOutput_UnlockMetadataObjectTracking(Camera_MetadataOutput* metadataOutput)
```
 
**描述**
 
解锁元数据对象（如猫脸、狗脸）的追踪。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Camera_MetadataOutput* metadataOutput | 元数据输出实例的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：操作成功。 CAMERA_INVALID_ARGUMENT：参数缺失或参数类型错误。 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |
