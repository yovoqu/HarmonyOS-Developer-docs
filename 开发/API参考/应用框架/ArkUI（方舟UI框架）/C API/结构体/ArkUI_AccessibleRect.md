# ArkUI_AccessibleRect

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerect
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_AccessibleRect
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

节点在屏幕中的矩形区域坐标位置。该结构体用于描述无障碍节点的边界矩形，通过左上角和右下角的坐标定义节点在屏幕上的可视区域，支持无障碍服务获取节点的位置和大小信息。
 
**起始版本：** 13
 
**相关模块：** [ArkUI_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility)
 
**所在头文件：** [native_interface_accessibility.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t leftTopX | 左上角X轴坐标位置。 |
| int32_t leftTopY | 左上角Y轴坐标位置。 |
| int32_t rightBottomX | 右下角X轴坐标位置。 |
| int32_t rightBottomY | 右下角Y轴坐标位置。 |
