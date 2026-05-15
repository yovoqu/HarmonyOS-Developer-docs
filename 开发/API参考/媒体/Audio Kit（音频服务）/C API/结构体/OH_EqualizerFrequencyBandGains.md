# OH_EqualizerFrequencyBandGains

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-equalizerfrequencybandgains
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct {...} OH_EqualizerFrequencyBandGains
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

定义音频编创均衡器效果节点配置参数。

**起始版本：** 22

**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)

**所在头文件：** [native_audio_suite_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| int32_t gains[EQUALIZER_BAND_NUM] | 均衡器频带增益配置，EQUALIZER_BAND_NUM为10，输入范围为[-10, 10]，单位为dB（分贝）。  频带：31Hz、62Hz、125Hz、250Hz、500Hz、1kHz、2kHz、4kHz、8kHz、16kHz。 起始版本： 22 |
