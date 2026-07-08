# xeg_control_display_separation.h

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-control-display-separation
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

XEngine控显分离API接口。
 
**引用文件**：<xengine/xeg_control_display_separation.h>
 
**库：** libxengine.so
 
**系统能力：** SystemCapability.Graphic.XEngine
 
**起始版本：** 26.0.0
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| XEG_ControlDisplaySeparationStatus { UNAVAILABLE = 0, AVAILABLE = 1} | 此枚举描述控显分离当前的状态信息。 |
 
 
  

#### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| typedef enum XEG_ControlDisplaySeparationStatus XEG_ControlDisplaySeparationStatus | 此枚举描述控显分离当前的状态信息。 |
| typedef void(*PFN_HMS_XEG_ControlDisplaySeparationStatusCallback) (XEG_ControlDisplaySeparationStatus status) | 控显分离特性监听函数的函数指针定义。 |
| typedef bool(*PFN_HMS_XEG_SetControlDisplaySeparationStatusListener) (PFN_HMS_XEG_ControlDisplaySeparationStatusCallback callback) | 设置控显分离特性全局唯一监听函数的函数指针定义。 |
| typedef void(*PFN_HMS_XEG_RemoveControlDisplaySeparationStatusListener) () | 移除控显分离特性全局唯一监听函数的函数指针定义。 |
| typedef bool(*PFN_HMS_XEG_SetControlDisplaySeparationActive) (bool flag) | 设置控显分离特性使能开关的函数指针定义。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| bool HMS_XEG_SetControlDisplaySeparationStatusListener(PFN_HMS_XEG_ControlDisplaySeparationStatusCallback callback) | 设置控显分离特性全局唯一监听函数。 |
| void HMS_XEG_RemoveControlDisplaySeparationStatusListener() | 移除控显分离特性全局唯一监听函数。 |
| bool HMS_XEG_SetControlDisplaySeparationActive(bool flag) | 设置控显分离特性使能开关。 |
