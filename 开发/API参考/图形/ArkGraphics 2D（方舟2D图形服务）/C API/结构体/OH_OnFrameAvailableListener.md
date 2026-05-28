# OH_OnFrameAvailableListener

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativeimage-oh-onframeavailablelistener
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_OnFrameAvailableListener {...} OH_OnFrameAvailableListener
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

一个OH_NativeImage的监听者，通过[OH_NativeImage_SetOnFrameAvailableListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-image-h#oh_nativeimage_setonframeavailablelistener)接口注册该监听结构体，当有buffer可获取时，将触发回调给用户。
 
**起始版本：** 11
 
**相关模块：** [OH_NativeImage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativeimage)
 
**所在头文件：** [native_image.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-image-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| void* context | 用户自定义的上下文信息，会在回调触发时返回给用户。 |
| OH_OnFrameAvailable onFrameAvailable | 有buffer可获取时触发的回调函数。 |
 
 
  

##### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_OnFrameAvailable)(void *context) | OH_OnFrameAvailable() | 有buffer可获取时触发的回调函数。 起始版本： 11 系统能力： SystemCapability.Graphic.Graphic2D.NativeImage |
 
 
  

##### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### OH_OnFrameAvailable()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_OnFrameAvailable)(void *context)
```
 
**描述**
 
有buffer可获取时触发的回调函数。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| void *context | 用户自定义的上下文信息，会在回调触发时返回给用户。 |
