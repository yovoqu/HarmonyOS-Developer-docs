# network_boost.h

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-boost
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

声明用于网络加速的API。提供基本的函数、结构体和const定义。
 
**引用文件：** <NetworkBoostKit/network_boost.h>
 
**库：** libnetwork_boost.so
 
**系统能力：** SystemCapability.Communication.NetworkBoost.Core
 
**起始版本：** 6.0.2(22)
 
**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| struct NetworkBoost_SceneDesc | 业务场景描述信息。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| struct NetworkBoost_SceneEvent{ NB_SCENE_EVENT_ENTER = 0, NB_SCENE_EVENT_UPDATE = 1, NB_SCENE_EVENT_LEAVE = 2 } | 业务事件枚举。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| int32_t HMS_NetworkBoost_SetSceneDesc(NetworkBoost_SceneDesc sceneDesc) | 设置业务场景。 |
