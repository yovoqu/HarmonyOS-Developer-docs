# WhitePointArray

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager-whitepointarray
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct WhitePointArray {...} WhitePointArray
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供白点数组结构体，白点是在当前色域中表示白色的坐标。
 
**起始版本：** 13
 
**相关模块：** [NativeColorSpaceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager)
 
**所在头文件：** [native_color_space_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-color-space-manager-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| float arr[2] | 表示白点坐标数组。arr[0]表示x坐标，arr[1]表示y坐标，用于在色域空间中精确定义白色基准点，影响色域的显示效果和颜色准确性。 |
