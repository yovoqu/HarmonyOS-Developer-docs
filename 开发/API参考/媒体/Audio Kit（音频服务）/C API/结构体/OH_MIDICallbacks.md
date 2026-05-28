# OH_MIDICallbacks

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midicallbacks
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} OH_MIDICallbacks
```
  

##### 概述

客户端回调结构体，包含设备变化和错误处理的回调函数。
 
**起始版本：** 24
 
**相关模块：** [OHMIDI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi)
 
**所在头文件：** [native_midi_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-midi-base-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| OH_MIDICallback_OnDeviceChange onDeviceChange | 处理设备热插拔事件的回调。 起始版本： 24 |
| OH_MIDICallback_OnError onError | 处理关键服务错误的回调。 起始版本： 24 |
