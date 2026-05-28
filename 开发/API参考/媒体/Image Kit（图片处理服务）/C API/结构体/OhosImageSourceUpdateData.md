# OhosImageSourceUpdateData

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceupdatedata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OhosImageSourceUpdateData {...}
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义图像源更新数据选项，由[OH_ImageSource_UpdateData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_updatedata)获取。
 
**起始版本：** 10
 
**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)
 
**所在头文件：** [image_source_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint8_t* buffer = nullptr | 图像源更新数据缓冲区。 |
| size_t bufferSize = 0 | 图像源更新数据缓冲区大小。 |
| uint32_t offset = 0 | 图像源更新数据缓冲区的开端。 |
| uint32_t updateLength = 0 | 图像源更新数据缓冲区的更新数据长度。 |
| int8_t isCompleted = 0 | 图像源更新数据在此节中完成。 |
