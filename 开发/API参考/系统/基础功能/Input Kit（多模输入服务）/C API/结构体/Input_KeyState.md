# Input_KeyState

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keystate
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Input_KeyState Input_KeyState
```
  

##### 概述

定义按键信息，用于标识按键行为。例如，“Ctrl”按键信息包含键值和键类型。
 
**起始版本：** 12
 
**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
 
**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_Input_CreateKeyState | 创建按键状态的枚举对象。通过调用OH_Input_DestroyKeyState销毁按键状态的枚举对象。 |
| OH_Input_DestroyKeyState | 销毁按键状态的枚举对象。 |
