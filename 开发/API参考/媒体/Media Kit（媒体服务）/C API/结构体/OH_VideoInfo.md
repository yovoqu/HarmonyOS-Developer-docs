# OH_VideoInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_VideoInfo {...} OH_VideoInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

视频信息。
 
用于配置屏幕录制时的视频采集参数和编码参数。该结构体包含视频采集参数（如分辨率、采集格式等）和视频编码参数，适用于需要自定义屏幕录制视频输出参数的场景。开发者根据实际需求配置相关参数后，在调用屏幕录制相关接口时使用。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_VideoCaptureInfo videoCapInfo | 视频采集信息，用于配置屏幕录制时的视频采集区域、分辨率等参数。 |
| OH_VideoEncInfo videoEncInfo | 视频编码参数，用于配置屏幕录制输出的编码格式、比特率和帧率，不同编码配置将影响输出视频的画质、文件大小和编码效率。 |
