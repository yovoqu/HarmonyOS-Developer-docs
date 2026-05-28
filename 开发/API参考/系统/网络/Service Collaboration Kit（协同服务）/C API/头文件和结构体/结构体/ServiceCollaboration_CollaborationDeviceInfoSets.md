# ServiceCollaboration_CollaborationDeviceInfoSets

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets
**支持设备：** Phone | PC/2in1 | Tablet | TV

##### 概述

通过[HMS_ServiceCollaboration_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_getcollaborationdeviceinfos)获取的对端设备信息对象集合。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)
 
**所在头文件：** [service_collaboration_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint32_t size | 对端设备信息对象集合的大小。 |
| ServiceCollaboration_CollaborationDeviceInfo * deviceInfoSets | 对端设备信息对象集合。 |
 
 
  

##### 结构体成员变量说明

  

##### deviceInfoSets

```text
ServiceCollaboration_CollaborationDeviceInfo* ServiceCollaboration_CollaborationDeviceInfoSets::deviceInfoSets
```
 
**描述**
 
对端设备信息对象集合。
 
  

##### size

```text
uint32_t ServiceCollaboration_CollaborationDeviceInfoSets::size
```
 
**描述**
 
对端设备信息对象集合的大小。
