# OH_MIDIEvent

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midievent
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} OH_MIDIEvent
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

MIDI事件结构体（通用）。适用于原始字节流（MIDI 1.0）和UMP（Universal MIDI Packet）两种数据格式。
 
**起始版本：** 24
 
**相关模块：** [OHMIDI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi)
 
**所在头文件：** [native_midi_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-midi-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| uint64_t timestamp | 时间戳，单位为纳秒。 通过clock_gettime(CLOCK_MONOTONIC, &time)获取基准时间。值为0表示立即发送。 起始版本： 24 |
| size_t length | UMP数据包中的32位字（word）数量。 例如：Type 2/4消息占1个字（64位消息占2个字）。 此字段表示UMP数据中uint32_t字的数量，而非字节数。 起始版本： 24 |
| uint32_t *data | 指向UMP数据的指针，包含原始UMP字（uint32_t）。 此指针必须指向4字节对齐的内存地址，以满足UMP规范对32位边界对齐的要求。 起始版本： 24 |
