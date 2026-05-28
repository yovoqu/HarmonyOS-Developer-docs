# ArkWeb_ComponentAPI

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-componentapi
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkWeb_ComponentAPI
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Component相关的Native API结构体。
 
**起始版本：** 12
 
**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)
 
**所在头文件：** [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| size_t size | 结构体的大小。 |
 
 
  

#### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| void (*onControllerAttached)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData) | 当Controller成功绑定到Web组件时触发该回调。 |
| void (*onPageBegin)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData) | 网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。 |
| void (*onPageEnd)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData) | 网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。 |
| void (*onDestroy)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData) | 当前Web组件销毁时触发该回调。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### onControllerAttached()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*onControllerAttached)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```
 
**描述：**
 
当Controller成功绑定到Web组件时触发该回调。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| ArkWeb_OnComponentCallback callback | onControllerAttached的回调函数。 |
| void* userData | 用户自定义数据。 |
 
 
  

#### onPageBegin()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*onPageBegin)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```
 
**描述：**
 
网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| ArkWeb_OnComponentCallback callback | onPageBegin的回调函数。 |
| void* userData | 用户自定义数据。 |
 
 
  

#### onPageEnd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*onPageEnd)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```
 
**描述：**
 
网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| ArkWeb_OnComponentCallback callback | onPageEnd的回调函数。 |
| void* userData | 用户自定义数据。 |
 
 
  

#### onDestroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*onDestroy)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```
 
**描述：**
 
当前Web组件销毁时触发该回调。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| ArkWeb_OnComponentCallback callback | onDestroy的回调函数。 |
| void* userData | 用户自定义数据。 |
