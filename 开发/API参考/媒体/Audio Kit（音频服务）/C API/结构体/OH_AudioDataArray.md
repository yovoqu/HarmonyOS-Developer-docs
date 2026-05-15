# OH_AudioDataArray

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiodataarray
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct {...} OH_AudioDataArray
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

定义多路输出渲染接口的输入数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。

**起始版本：** 22

**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)

**所在头文件：** [native_audio_suite_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| void **audioDataArray | 需要输出的音频数据地址。 |
| int32_t arraySize | 音频数组大小。 |
| int32_t requestFrameSize | audioDataArray数组中地址的内存大小（单位为字节），应确保每个地址均具有requestFrameSize字节个大小。 |
