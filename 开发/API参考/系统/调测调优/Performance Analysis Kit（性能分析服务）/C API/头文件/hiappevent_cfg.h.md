# hiappevent_cfg.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-cfg-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义事件打点配置函数的所有配置项名称。如果开发者想要对应用事件打点功能进行配置，可以直接使用配置项常量。
 
**引用文件：** <hiappevent/hiappevent_cfg.h>
 
**库：** libhiappevent_ndk.z.so
 
**系统能力：** SystemCapability.HiviewDFX.HiAppEvent
 
**起始版本：** 8
 
**相关模块：** [HiAppEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 宏定义

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| DISABLE "disable" | 事件打点开关。默认值为false。true：关闭打点功能，false：不关闭打点功能。 起始版本： 8 |
| MAX_STORAGE "max_storage" | 事件文件目录存储配额大小。默认值为“10M”。 起始版本： 8 |
 
 
  

#### 宏定义说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### DISABLE

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define DISABLE "disable"
```
 
**描述**
 
事件打点开关。默认值为false。true：关闭打点功能，false：不关闭打点功能。
 
**起始版本：** 8
 
  

#### MAX_STORAGE

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define MAX_STORAGE "max_storage"
```
 
**描述**
 
事件文件目录存储配额大小。默认值为“10M”。
 
**起始版本：** 8
