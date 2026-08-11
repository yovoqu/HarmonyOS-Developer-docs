# OH_NativeBuffer

更新时间：2026-07-28 11:23:46（官网已下线）

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-avscreencapture-oh-nativebuffer
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_NativeBuffer OH_NativeBuffer
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

提供录屏的视频原始数据缓冲区结构体。OH_NativeBuffer提供录屏的视频原始数据处理能力，支持对录屏过程中产生的视频原始数据进行封装、传输和管理。
 
用于在AVScreenCapture录屏场景中承载获取的视频帧原始数据。可用于录屏数据的二次处理场景，如视频编辑应用中对录屏帧数据进行像素级操作、直播推流场景中对原始码流进行编码推送等。
 
**起始版本：** 10
 
**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
 
**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
