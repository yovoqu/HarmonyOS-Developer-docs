# Input_AxisEvent

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-axisevent
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Input_AxisEvent Input_AxisEvent
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

轴事件对象。用于表示输入设备的轴事件数据，如游戏手柄的摇杆移动、鼠标滚轮滚动等场景。开发者可以通过轴事件获取输入设备的轴值变化，实现精细的输入控制，提升用户交互体验。
 
**起始版本：** 12
 
**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
 
**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_Input_CreateAxisEvent | 创建轴事件对象。通过调用OH_Input_DestroyAxisEvent销毁轴事件对象。 |
| OH_Input_DestroyAxisEvent | 销毁轴事件对象。 |
