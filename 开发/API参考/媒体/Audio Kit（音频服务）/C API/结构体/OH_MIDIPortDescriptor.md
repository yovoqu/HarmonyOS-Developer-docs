# OH_MIDIPortDescriptor

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiportdescriptor
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} OH_MIDIPortDescriptor
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

端口描述符结构体，用于打开端口时指定端口索引和协议行为。
 
**起始版本：** 24
 
**相关模块：** [OHMIDI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi)
 
**所在头文件：** [native_midi_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-midi-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| uint32_t portIndex | 要打开的端口索引号。 起始版本： 24 |
| OH_MIDIProtocol protocol | 指定要使用的MIDI协议版本（MIDI 1.0或MIDI 2.0）。服务会根据此字段在应用和硬件之间转换数据。应用只需声明期望的协议版本，以下是协议版本与硬件不匹配时的系统处理行为： 1. 在MIDI 2.0设备上请求OH_MIDI_PROTOCOL_1.0：（无损兼容） 应用发送UMP Type 2（MIDI 1.0通道声音）消息，服务直接转发给设备，无数据损失。 2. 在MIDI 1.0设备上请求OH_MIDI_PROTOCOL_2.0：（有损转换） 应用发送UMP Type 4（MIDI 2.0通道声音）消息，服务将Type 4降级转换为Type 2（例如：截断力度值，丢弃逐音符数据），会丢失数据精度，高级消息可能被丢弃。 起始版本： 24 |
