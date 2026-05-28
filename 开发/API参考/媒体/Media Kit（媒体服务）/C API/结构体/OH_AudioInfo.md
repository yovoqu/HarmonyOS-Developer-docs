# OH_AudioInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_AudioInfo {...} OH_AudioInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

音频信息。
 
同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_AudioCaptureInfo micCapInfo | 音频麦克风采样信息。 |
| OH_AudioCaptureInfo innerCapInfo | 音频内录采样信息。 |
| OH_AudioEncInfo audioEncInfo | 音频编码信息，原始码流时不需要设置。 |
