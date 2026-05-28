# PhotoOutput_Callbacks

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-photooutput-callbacks
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct PhotoOutput_Callbacks {...} PhotoOutput_Callbacks
```
  

##### 概述

拍照输出的回调。
 
**起始版本：** 11
 
**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)
 
**所在头文件：** [photo_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| OH_PhotoOutput_OnFrameStart onFrameStart | 拍照输出帧启动事件。 |
| OH_PhotoOutput_OnFrameShutter onFrameShutter | 拍照输出帧快门事件。 |
| OH_PhotoOutput_OnFrameEnd onFrameEnd | 拍照输出帧结束事件。 |
| OH_PhotoOutput_OnError onError | 拍照输出错误事件。 |
