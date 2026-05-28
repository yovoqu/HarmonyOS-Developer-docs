# OH_VideoCaptureInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videocaptureinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_VideoCaptureInfo {...} OH_VideoCaptureInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

视频录制信息。当videoFrameWidth和videoFrameHeight同时为0时，忽略视频相关参数不录制屏幕数据。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| uint64_t displayId | 录制物理屏id，使用该参数需要在capturemode为CAPTURE_SPECIFIED_SCREEN模式下使用。 |
| int32_t* missionIDs | 指定窗口id列表，使用该参数需要在capturemode为CAPTURE_SPECIFIED_WINDOW模式下使用。 |
| int32_t missionIDsLen | 指定窗口ID长度，使用该参数需要在capturemode为CAPTURE_SPECIFIED_WINDOW模式下使用。 |
| int32_t videoFrameWidth | 采集视频的宽度设置，单位px。 |
| int32_t videoFrameHeight | 采集视频的高度设置，单位px。 |
| OH_VideoSourceType videoSource | 视频采集格式设置，目前仅支持RGBA格式。 |
