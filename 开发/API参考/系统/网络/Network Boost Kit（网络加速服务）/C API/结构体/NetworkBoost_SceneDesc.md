# NetworkBoost_SceneDesc

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-scene_desc
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

业务场景描述信息。
 
**起始版本：** 6.0.2(22)
 
**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
 
**所在头文件：** [network_boost.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-boost)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| NetworkBoost_ServiceType scene | 表示业务场景类型。 |
| NetworkBoost_SceneEvent sceneEvent | 表示业务场景事件。 |
| uint32_t startTime | 表示要经过多长时间进入到sceneEvent事件，单位为s。 - 0表示立即发生sceneEvent事件，默认为0。 - 大于0表示预测未来多长时间进入sceneEvent事件。 |
| uint32_t duration | 预计本次设置的业务场景会持续的时长，单位为s。0表示持续时长未知，以SceneEvent的离开事件表示终止。开发者可以依据实际的场景类型进行选填。 例如：应用即将在10s后进入秒杀场景，预计持续20s。scene可以传入'seckillService'类型，sceneEvent填写SCENE_EVENT_ENTER，startTime可填写10，duration填写20。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

#### scene

**支持设备：** Phone | PC/2in1 | Tablet

```text
NetworkBoost_ServiceType NetworkBoost_SceneDesc::scene
```
 
**描述**
 
表示业务场景类型。
 
  

#### sceneEvent

**支持设备：** Phone | PC/2in1 | Tablet

```text
NetworkBoost_SceneEvent NetworkBoost_SceneDesc::sceneEvent
```
 
**描述**
 
表示业务场景事件。
 
  

#### startTime

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t NetworkBoost_SceneDesc::startTime
```
 
**描述**
 
表示要经过多长时间进入到sceneEvent事件，单位为s。
 
  

#### duration

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t NetworkBoost_SceneDesc::duration
```
 
**描述**
 
预计本次设置的业务场景会持续的时长，单位为s。
