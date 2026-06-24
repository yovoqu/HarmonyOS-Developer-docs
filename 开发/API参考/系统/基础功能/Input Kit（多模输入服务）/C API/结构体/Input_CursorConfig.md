# Input_CursorConfig

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-cursorconfig
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Input_CursorConfig Input_CursorConfig
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

自定义鼠标光标配置，用于定义和管理应用程序中鼠标光标的显示样式和交互行为。支持设置不同类型的光标样式（如默认、手形、文本输入等），为用户提供更直观的操作反馈，提升用户体验。
 
**起始版本：** 22
 
**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
 
**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_Input_CursorConfig_Create | 创建自定义鼠标光标配置对象。通过调用OH_Input_CursorConfig_Destroy销毁自定义鼠标光标配置对象。 |
| OH_Input_CursorConfig_Destroy | 销毁自定义鼠标光标配置对象。 |
