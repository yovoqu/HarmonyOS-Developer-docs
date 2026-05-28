# ServiceCollaborationCallback

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

传给[HMS_ServiceCollaboration_StartCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaboration)或[HMS_ServiceCollaboration_StartCollaborationV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaborationv2)的回调方法，用来传递跨设备互通的状态信息。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)
 
**所在头文件：** [service_collaboration_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t(* OnEvent )(ServiceCollaborationEventCode code, uint32_t extraCode) | 在跨设备互通服务状态变化时被调用。 |
| int32_t(* OnDataCallback )(ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32_t dataSize, char *data) | 在跨设备互通服务数据返回时被调用。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### OnDataCallback

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
int32_t(* ServiceCollaborationCallback::OnDataCallback) (ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32_t dataSize, char *data)
```
 
**描述**
 
在跨设备互通服务数据返回时被调用。
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationEventCode code | 错误码。 |
| ServiceCollaborationDataType dataType | 回传数据类型。 |
| uint32_t dataSize | 数据大小，单位是字节。 |
| char *data | 数据。 |
 
 
  

#### OnEvent

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
int32_t(* ServiceCollaborationCallback::OnEvent) (ServiceCollaborationEventCode code, uint32_t extraCode)
```
 
**描述**
 
在跨设备互通服务状态变化时被调用。
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationEventCode code | 错误码。 |
| uint32_t extraCode | 拓展状态码，携带错误码未提供的额外信息。 |
