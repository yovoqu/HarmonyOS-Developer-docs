# OH_VideoEncInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoencinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_VideoEncInfo {...} OH_VideoEncInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

视频编码参数。
 
用于配置屏幕录制的视频编码参数，支持设置编码格式、比特率和帧率。videoCodec指定编码格式（如H.264、H.265等），videoBitrate影响视频清晰度和文件大小，videoFrameRate影响视频流畅度。通常在调用屏幕录制接口前设置这些参数。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_VideoCodecFormat videoCodec | 视频编码格式。不同编码格式影响视频的压缩效率与兼容性，具体各格式效果参见OH_VideoCodecFormat枚举说明。 |
| int32_t videoBitrate | 视频编码比特率，单位为比特每秒（bit/s）。取值范围需根据编码格式和实际需求确定，默认取值为10000000，值越大画质越好但文件也越大。 |
| int32_t videoFrameRate | 视频编码帧率，单位为帧每秒（FPS）。常见取值范围为15~60 FPS。 |
