# VideoProcessing_Callback

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-callback
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct VideoProcessing_Callback VideoProcessing_Callback
```
  

##### 概述

视频处理回调对象类型。
 
定义一个VideoProcessing_Callback空指针，调用[OH_VideoProcessingCallback_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessingcallback_create)来创建一个回调对象。创建之前该指针必须为空。通过调用[OH_VideoProcessing_RegisterCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_registercallback)来向视频处理实例注册回调对象。
 
**起始版本：** 12
 
**相关模块：** [VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)
 
**所在头文件：** [video_processing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-types-h)
