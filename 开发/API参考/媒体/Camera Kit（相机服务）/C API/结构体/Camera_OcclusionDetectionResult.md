# Camera_OcclusionDetectionResult

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-occlusiondetectionresult
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct {...} Camera_OcclusionDetectionResult
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

相机镜头遮挡、脏污检测结果。

**起始版本：** 23

**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| bool isCameraOccluded | 检查相机镜头是否被遮挡。true表示被遮挡，false表示未被遮挡。 |
| bool isCameraLensDirty | 检查相机镜头是否有脏污。true表示有脏污，false表示没有脏污。 |
