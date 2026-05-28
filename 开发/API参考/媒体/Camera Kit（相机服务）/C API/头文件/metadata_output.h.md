# metadata_output.h

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明元数据输出概念。
 
**引用文件：** <ohcamera/metadata_output.h>
 
**库：** libohcamera.so
 
**系统能力：** SystemCapability.Multimedia.Camera.Core
 
**起始版本：** 11
 
**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| MetadataOutput_Callbacks | MetadataOutput_Callbacks | 元数据输出的回调。 |
| Camera_MetadataOutput | Camera_MetadataOutput | 元数据输出对象。 可以使用OH_CameraManager_CreateMetadataOutput方法创建指针。 |
 
 
  

##### 函数

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
 
 
  

##### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### OH_MetadataOutput_OnMetadataObjectAvailable()

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
 
 
  

##### OH_MetadataOutput_OnError()

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
 
  

##### OH_MetadataOutput_RegisterCallback()

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
 
 
  

##### OH_MetadataOutput_UnregisterCallback()

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
 
 
  

##### OH_MetadataOutput_Start()

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
 
 
  

##### OH_MetadataOutput_Stop()

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
 
 
  

##### OH_MetadataOutput_Release()

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
 
 
  

##### OH_MetadataOutput_AddMetadataObjectTypes()

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
 
 
  

##### OH_MetadataOutput_RemoveMetadataObjectTypes()

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
