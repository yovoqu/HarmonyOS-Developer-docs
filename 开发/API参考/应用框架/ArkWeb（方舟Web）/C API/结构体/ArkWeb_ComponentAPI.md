# ArkWeb_ComponentAPI

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-componentapi
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkWeb_ComponentAPI
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkWeb_ComponentAPI是ArkWeb在Native侧提供的用于监听Web组件生命周期事件的API结构体，继承自基础Native API类型[ArkWeb_AnyNativeAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-anynativeapi)。开发者通过[OH_ArkWeb_GetNativeAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-interface-h#oh_arkweb_getnativeapi)并指定ARKWEB_NATIVE_COMPONENT类型获取该结构体，进而注册Web组件的Controller绑定、页面开始加载、页面加载完成以及组件销毁等事件回调。该结构体适用于需要在Native代码（C/C++）中感知Web组件关键状态变化的场景，例如初始化Native资源、同步页面加载状态、统计埋点或在组件销毁时释放关联资源；相关接口需在UI线程中调用，并建议在调用具体成员函数前通过[ARKWEB_MEMBER_MISSING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#宏定义)宏校验函数指针是否存在。
 
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
