# OH_AudioInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_AudioInfo {...} OH_AudioInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

音频信息。
 
OH_AudioInfo作为OH_ScreenCaptureConfig的音频配置成员，包含麦克风采集信息、内录采集信息和音频编码信息三个部分，开发者需根据采集场景选择配置麦克风采集信息或内录采集信息，并在需要编码输出时配置音频编码信息。适用于需要在屏幕录制中采集音频数据的场景。
 
同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同，因为两路音频数据将合并为同一音频流输出，采样参数不一致会导致音频同步异常或采集失败。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_AudioCaptureInfo micCapInfo | 音频麦克风采样信息，用于配置麦克风音频采集的采样参数。 |
| OH_AudioCaptureInfo innerCapInfo | 音频内录采样信息，用于配置内录音频采集的采样参数。 |
| OH_AudioEncInfo audioEncInfo | 音频编码信息。采集原始码流时不需要设置编码参数。未设置时默认不进行音频编码。 |
