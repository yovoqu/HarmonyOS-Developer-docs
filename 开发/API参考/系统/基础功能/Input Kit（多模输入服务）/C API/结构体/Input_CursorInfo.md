# Input_CursorInfo

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-cursorinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Input_CursorInfo Input_CursorInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义鼠标光标信息，用于在输入系统中管理和控制鼠标光标的显示行为和外观属性。包括光标显示状态、光标样式、光标大小档位、光标颜色。
 
**起始版本：** 22
 
**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
 
**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_Input_CursorInfo_Create | 创建鼠标光标信息对象。通过调用OH_Input_CursorInfo_Destroy销毁鼠标光标信息对象。 |
| OH_Input_CursorInfo_Destroy | 销毁鼠标光标信息对象。 |
