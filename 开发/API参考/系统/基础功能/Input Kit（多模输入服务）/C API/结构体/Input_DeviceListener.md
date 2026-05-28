# Input_DeviceListener

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-devicelistener
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Input_DeviceListener {...} Input_DeviceListener
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义一个结构体用于监听设备热插拔。
 
**起始版本：** 13
 
**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
 
**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Input_DeviceAddedCallback deviceAddedCallback | 定义一个回调函数，用于回调设备热插事件。 |
| Input_DeviceRemovedCallback deviceRemovedCallback | 定义一个回调函数，用于回调设备热拔事件。 |
