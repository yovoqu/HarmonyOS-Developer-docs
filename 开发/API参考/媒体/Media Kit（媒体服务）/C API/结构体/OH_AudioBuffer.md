# OH_AudioBuffer

更新时间：2026-05-07 09:37:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiobuffer
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

定义了音频数据的大小、类型、时间戳等配置信息。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| uint8_t* buf | 音频buffer内存。 |
| int32_t size | 音频buffer内存大小。 |
| int64_t timestamp | 音频buffer时间戳。单位为纳秒（ns）。 |
| OH_AudioCaptureSourceType type | 音频录制源类型。 |
