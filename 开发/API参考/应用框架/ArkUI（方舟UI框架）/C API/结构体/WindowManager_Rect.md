# WindowManager_Rect

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-rect
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} WindowManager_Rect
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义窗口矩形结构体，包含窗口位置和宽高信息。
 
**起始版本：** 15
 
**相关模块：** [WindowManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager)
 
**所在头文件：** [oh_window_comm.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-comm-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t posX | 窗口的x轴，单位为px，该参数为整数。 |
| int32_t posY | 窗口的y轴，单位为px，该参数为整数。 |
| uint32_t width | 窗口的宽度，单位为px，该参数为整数。 |
| uint32_t height | 窗口的高度，单位为px，该参数为整数。 |
