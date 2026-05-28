# Input_InterceptorOptions

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoroptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Input_InterceptorOptions Input_InterceptorOptions
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

事件拦截选项。
 
**起始版本：** 12
 
**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
 
**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_Input_AddKeyEventInterceptor | 添加按键事件的拦截，重复添加只有第一次生效。仅在应用获焦时拦截按键事件。 |
| OH_Input_RemoveKeyEventInterceptor | 移除按键事件拦截。 |
| OH_Input_AddInputEventInterceptor | 添加输入事件拦截，包括鼠标、触屏和轴事件，重复添加只有第一次生效。仅命中应用窗口时拦截输入事件。 |
| OH_Input_RemoveInputEventInterceptor | 移除输入事件拦截，包括鼠标、触屏和轴事件。 |
