# native_avbuffer_info.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-info-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明了媒体数据结构AVBuffer属性的定义。
 
**引用文件：** <multimedia/player_framework/native_avbuffer_info.h>
 
**库：** libnative_media_core.so
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 9
 
**相关模块：** [Core](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core)
 
**相关示例：** [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVCodecBufferAttr | OH_AVCodecBufferAttr | 定义OH_AVCodec的缓冲区描述信息。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVCodecBufferFlags | OH_AVCodecBufferFlags | 枚举OH_AVCodec缓冲区标记的类别。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_AVCodecBufferFlags

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVCodecBufferFlags
```
 
**描述**
 
枚举OH_AVCodec缓冲区标记的类别。
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 9
  
| 枚举项 | 描述 |
| --- | --- |
| AVCODEC_BUFFER_FLAGS_NONE = 0 | 表示为普通帧。 |
| AVCODEC_BUFFER_FLAGS_EOS = 1 << 0 | 表示缓冲区是流结束帧。 |
| AVCODEC_BUFFER_FLAGS_SYNC_FRAME = 1 << 1 | 表示缓冲区包含关键帧。 |
| AVCODEC_BUFFER_FLAGS_INCOMPLETE_FRAME = 1 << 2 | 表示缓冲区中的数据只是帧的一部分。 |
| AVCODEC_BUFFER_FLAGS_CODEC_DATA = 1 << 3 | 表示缓冲区包含编解码特定数据。 |
| AVCODEC_BUFFER_FLAGS_DISCARD = 1 << 4 | 表示缓冲区被解码依赖，解码之后的数据可丢弃。 起始版本： 12 |
| AVCODEC_BUFFER_FLAGS_DISPOSABLE = 1 << 5 | 表示缓冲区不被参考可直接丢弃。 起始版本： 12 |
