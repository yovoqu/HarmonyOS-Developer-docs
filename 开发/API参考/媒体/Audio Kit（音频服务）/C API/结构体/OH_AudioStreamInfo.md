# OH_AudioStreamInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreaminfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AudioStreamInfo {...} OH_AudioStreamInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义音频流信息结构体，用于描述基本音频格式。
 
**起始版本：** 19
 
**相关模块：** [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)
 
**所在头文件：** [native_audiostream_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t samplingRate | 音频流采样率。单位为赫兹（Hz）。 |
| OH_AudioChannelLayout channelLayout | 音频流声道布局。 |
| OH_AudioStream_EncodingType encodingType | 音频流编码类型。 |
| OH_AudioStream_SampleFormat sampleFormat | 音频流采样格式。 |
