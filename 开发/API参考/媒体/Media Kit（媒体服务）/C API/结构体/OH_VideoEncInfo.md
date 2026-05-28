# OH_VideoEncInfo

更新时间：2026-05-07 09:37:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoencinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_VideoEncInfo {...} OH_VideoEncInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

视频编码参数。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_VideoCodecFormat videoCodec | 视频采集编码格式。 |
| int32_t videoBitrate | 视频采集比特率。单位为比特每秒（bit/s）。 |
| int32_t videoFrameRate | 视频采集帧率。单位为帧率（FPS）。 |
