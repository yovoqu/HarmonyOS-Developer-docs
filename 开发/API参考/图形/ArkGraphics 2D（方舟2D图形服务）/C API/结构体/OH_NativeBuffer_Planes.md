# OH_NativeBuffer_Planes

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-planes
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct OH_NativeBuffer_Planes {...} OH_NativeBuffer_Planes
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

OH_NativeBuffer的图像平面格式信息。

**起始版本：** 12

**相关模块：** [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)

**所在头文件：** [native_buffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| uint32_t planeCount | 不同平面的数量。 |
| [OH_NativeBuffer_Plane](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-plane) planes[4] | 图像平面格式信息数组。 |
