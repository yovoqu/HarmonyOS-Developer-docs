# OH_AVScreenCaptureConfig

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencaptureconfig
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_AVScreenCaptureConfig {...} OH_AVScreenCaptureConfig
```
  

##### 概述

屏幕录制配置参数。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| OH_CaptureMode captureMode | 屏幕录制的模式。 |
| OH_DataType dataType | 屏幕录制流的数据格式。 |
| OH_AudioInfo audioInfo | 音频录制参数。 |
| OH_VideoInfo videoInfo | 视频录制参数。 |
| OH_RecorderInfo recorderInfo | 录制文件参数，当数据格式为OH_CAPTURE_FILE时必须设置。 |
