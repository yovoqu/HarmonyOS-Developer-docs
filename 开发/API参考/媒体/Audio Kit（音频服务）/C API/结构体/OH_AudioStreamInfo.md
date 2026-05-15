# OH_AudioStreamInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreaminfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct OH_AudioStreamInfo {...} OH_AudioStreamInfo
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义音频流信息，用于描述基本音频格式。

**起始版本：** 19

**相关模块：** [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)

**所在头文件：** [native_audiostream_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| int32_t samplingRate | 音频流采样率。 |
| [OH_AudioChannelLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout) channelLayout | 音频流声道布局。 |
| [OH_AudioStream_EncodingType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_encodingtype) encodingType | 音频流编码类型。 |
| [OH_AudioStream_SampleFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sampleformat) sampleFormat | 音频流采样格式。 |
