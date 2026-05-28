# OH_AVScreenCaptureCallback

更新时间：2026-04-02 08:41:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapturecallback
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_AVScreenCaptureCallback {...} OH_AVScreenCaptureCallback
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

OH_AVScreenCapture中包含所有异步回调函数指针的集合。将该结构体的实例注册到OH_AVScreenCapture实例中，以便处理回调上报的信息，从而保证OH_AVScreenCapture的正常运行。
 
从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h#oh_avscreencapture_onerror)、[OH_AVScreenCapture_OnBufferAvailable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h#oh_avscreencapture_onbufferavailable)替代。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_AVScreenCaptureOnError onError | 监控录屏调用操作错误。 从API version 12开始，推荐使用接口OH_AVScreenCapture_OnError替代。 |
| OH_AVScreenCaptureOnAudioBufferAvailable onAudioBufferAvailable | 监控音频码流是否有数据产生。 从API version 12开始，推荐使用接口OH_AVScreenCapture_OnBufferAvailable替代。 |
| OH_AVScreenCaptureOnVideoBufferAvailable onVideoBufferAvailable | 监控视频码流是否有数据产生。 从API version 12开始，推荐使用接口OH_AVScreenCapture_OnBufferAvailable替代。 |
