# Camera_MetadataObject

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataobject
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct Camera_MetadataObject {...} Camera_MetadataObject
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

元数据对象基础。

**起始版本：** 11

**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [Camera_MetadataObjectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_metadataobjecttype) type | 元数据对象类型。 |
| int64_t timestamp | 元数据对象时间戳，单位为纳秒（ns）。 |
| [Camera_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-rect)* boundingBox | 检测到的元数据对象的轴对齐边界框。 |
