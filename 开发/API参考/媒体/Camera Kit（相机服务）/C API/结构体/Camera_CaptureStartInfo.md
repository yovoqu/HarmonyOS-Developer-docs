# Camera_CaptureStartInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-capturestartinfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct Camera_CaptureStartInfo {...} Camera_CaptureStartInfo
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

拍照开始信息。

**起始版本：** 12

**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| int32_t captureId | 拍照id。 |
| int64_t time | 预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。 |
