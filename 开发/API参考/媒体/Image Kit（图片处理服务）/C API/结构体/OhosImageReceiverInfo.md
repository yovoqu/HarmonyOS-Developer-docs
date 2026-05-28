# OhosImageReceiverInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagereceiverinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OhosImageReceiverInfo {...}
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义ImageReceiver的相关信息。
 
**起始版本：** 10
 
**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)
 
**所在头文件：** [image_receiver_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-receiver-mdk-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t width | 消费端接收图片时的默认图像宽度，用pixels表示。 |
| int32_t height | 消费端接收图片时的默认图像高度，用pixels表示。 |
| int32_t format | 通过接收器创建图像格式OHOS_IMAGE_FORMAT_JPEG。 |
| int32_t capicity | 图片缓存数量的最大值。该参数仅作为期望值，实际capacity由设备硬件决定。 |
