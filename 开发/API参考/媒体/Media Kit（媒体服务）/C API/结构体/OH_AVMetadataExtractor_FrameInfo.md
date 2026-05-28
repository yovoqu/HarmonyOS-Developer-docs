# OH_AVMetadataExtractor_FrameInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/metadataextractor-oh-avmetadataextractor-frameinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_AVMetadataExtractor_FrameInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义从视频中提取出的帧的信息。
 
**起始版本：** 23
 
**相关模块：** [AVMetadataExtractor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor)
 
**所在头文件：** [avmetadata_extractor_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-base-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int64_t requestTimeUs | 用户传入的请求时间。 |
| int64_t actualTimeUs | 实际提取到的帧的时间；若提取失败，则为-1。 |
| OH_PixelmapNative* image | 从视频中提取出的帧图像；若提取失败，则为空指针。 |
| OH_AVMetadataExtractor_FetchState result | 本次帧提取操作的结果状态。 |
