# OH_AudioSuite_PureVoiceChangeOption

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-purevoicechangeoption
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} OH_AudioSuite_PureVoiceChangeOption
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

定义音频编创传统变声选项。
 
**起始版本：** 23
 
**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)
 
**所在头文件：** [native_audio_suite_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| OH_AudioSuite_PureVoiceChangeGenderOption optionGender | 指定传统变声性别。 |
| OH_AudioSuite_PureVoiceChangeType optionType | 指定传统变声类型。 |
| float pitch | 指定传统变声音调。如果使用系统中的默认音调以获得最佳效果, 设置为宏定义中的OH_PURE_VOICE_DEFAULT_PITCH。 设置自定义音调的取值范围为[0.3f, 3.0f]。 |
