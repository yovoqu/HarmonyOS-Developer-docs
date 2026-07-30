# ArkUI_NativeGestureAPI_3

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-3
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_NativeGestureAPI_3
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义手势模块接口集合，包含[ArkUI_NativeGestureAPI_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-1)、[ArkUI_NativeGestureAPI_2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-2)结构体中的手势接口及新增手势接口。
 
该接口集合支持为ArkUI节点设置并行手势事件回调。回调可从响应链中的冲突手势识别器中选择需要与当前手势并行识别的对象。相关事件数据请参见[ArkUI_ParallelGestureEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-parallelgestureevent)。
 
**起始版本：** 26.0.0
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_gesture.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeGestureAPI_2* gestureApi2 | 指向ArkUI_NativeGestureAPI_2结构体的指针。 |
 
 
  

#### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_ErrorCode (*setGestureParallelTo)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureRecognizer* (*parallelGesture)(ArkUI_ParallelGestureEvent* event)) | 设置并行手势事件的回调函数。触发回调时，开发者可从事件提供的冲突手势识别器中返回一个需要与当前手势并行识别的对象。此接口适用于开发者自定义手势与响应链上其他组件手势需要并行处理的场景。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### setGestureParallelTo()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode (*setGestureParallelTo)(ArkUI_NodeHandle node, void* userData, ArkUI_GestureRecognizer* (*parallelGesture)(ArkUI_ParallelGestureEvent* event))
```
 
**描述：**
 
设置并行手势事件的回调函数。触发回调时，开发者可从事件提供的冲突手势识别器中返回一个需要与当前手势并行识别的对象。此接口适用于开发者自定义手势与响应链上其他组件手势需要并行处理的场景。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 待设置并行手势事件回调函数的ArkUI节点句柄。 |
| void* userData | 自定义数据，在并行手势事件回调函数中传递开发者自定义上下文信息。不需要关联上下文时可传入nullptr；传入非空指针时，开发者需要确保数据的生命周期安全，若数据在回调过程中被释放可能导致回调执行异常。 |
| ArkUI_GestureRecognizer* (*parallelGesture)(ArkUI_ParallelGestureEvent* event) | 并行手势事件的回调函数。event为并行手势事件对象，包含触发该回调时的手势事件信息；parallelGesture返回需要并行识别的手势识别器指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回ARKUI_ERROR_CODE_NO_ERROR表示成功。 返回ARKUI_ERROR_CODE_PARAM_INVALID表示参数错误。 |
