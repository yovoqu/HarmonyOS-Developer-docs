# Region

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-region
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct {...} Region
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

表示本地窗口OHNativeWindow需要更新内容的矩形区域（脏区）。

**起始版本：** 8

**相关模块：** [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow)

**所在头文件：** [external_window.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-external-window-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| * rects | 如果rects是空指针nullptr，默认Buffer大小为脏区。 |
| int32_t rectNumber | 如果rectNumber为0，默认Buffer大小为脏区。 |
