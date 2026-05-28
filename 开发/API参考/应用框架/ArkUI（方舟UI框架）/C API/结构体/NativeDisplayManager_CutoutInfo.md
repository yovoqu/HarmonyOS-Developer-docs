# NativeDisplayManager_CutoutInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} NativeDisplayManager_CutoutInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。
 
**起始版本：** 12
 
**相关模块：** [OH_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)
 
**所在头文件：** [oh_display_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t boundingRectsLength | 挖孔屏、刘海屏不可用屏幕区域长度。 |
| NativeDisplayManager_Rect* boundingRects | 挖孔屏、刘海屏等区域的边界矩形。 |
| NativeDisplayManager_WaterfallDisplayAreaRects waterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |
