# syscap_ndk.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap__ndk_8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

查询单个系统能力是否被支持的API。
 
**起始版本：**
 
8
 
**相关模块：**
 
[Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/init)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| canIUse (const char *cap) | 查询指定的系统能力是否被支持。 系统能力（SystemCapability，简称SysCap），指操作系统中每一个相对独立的特性。不同的设备对应不同的系统能力集，每个系统能力对应一个或多个API。开发者可根据系统能力来判断是否可以使用某接口。 |
