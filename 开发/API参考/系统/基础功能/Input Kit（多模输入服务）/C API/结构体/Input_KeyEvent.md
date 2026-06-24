# Input_KeyEvent

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keyevent
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Input_KeyEvent Input_KeyEvent
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

按键事件对象，用于表示用户按键操作产生的输入事件，包含按键码、按键状态等信息，可用于处理键盘输入和实现按键响应功能。
 
**起始版本：** 12
 
**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
 
**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_Input_CreateKeyEvent | 创建按键事件对象。通过调用OH_Input_DestroyKeyEvent销毁按键事件对象。 |
| OH_Input_DestroyKeyEvent | 销毁按键事件对象。 |
