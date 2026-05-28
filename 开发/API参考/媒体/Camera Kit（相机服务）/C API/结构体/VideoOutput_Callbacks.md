# VideoOutput_Callbacks

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-videooutput-callbacks
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct VideoOutput_Callbacks {...} VideoOutput_Callbacks
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于录像输出的回调。
 
**起始版本：** 11
 
**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)
 
**所在头文件：** [video_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_VideoOutput_OnFrameStart onFrameStart | 录像输出帧启动事件。 |
| OH_VideoOutput_OnFrameEnd onFrameEnd | 录像输出帧结束事件。 |
| OH_VideoOutput_OnError onError | 录像输出错误事件。 |
