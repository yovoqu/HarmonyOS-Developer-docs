# OH_AudioDeviceDescriptorArray

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiodevicedescriptorarray
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AudioDeviceDescriptorArray {...} OH_AudioDeviceDescriptorArray
```
  

##### 概述

声明音频设备描述符数组。
 
**起始版本：** 12
 
**相关模块：** [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)
 
**所在头文件：** [native_audio_device_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-device-base-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint32_t size | 音频设备描述符数组大小。 |
| OH_AudioDeviceDescriptor** descriptors | 音频设备描述符数组。 |
