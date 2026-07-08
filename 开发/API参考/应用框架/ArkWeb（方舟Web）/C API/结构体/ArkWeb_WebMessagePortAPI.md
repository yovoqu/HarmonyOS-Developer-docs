# ArkWeb_WebMessagePortAPI

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkWeb_WebMessagePortAPI
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkWeb_WebMessagePortAPI是Web消息端口相关Native API结构体。该结构体提供了消息端口的创建、关闭、消息发送和消息接收回调注册等功能。此API是postMessage桥接的核心组件，支持在Native代码和Web页面之间建立持久的双向通信通道。
 
Web消息端口相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取，调用前建议通过[ARKWEB_MEMBER_MISSING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#宏定义)校验函数指针的可用性，避免SDK与设备ROM不匹配导致崩溃。
 
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
| ArkWeb_ErrorCode (*postMessage)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, const ArkWeb_WebMessagePtr webMessage) | 发送消息到HTML。 |
| void (*close)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag) | 关闭消息端口。 |
| void (*setMessageEventHandler)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, ArkWeb_OnMessageEventHandler messageEventHandler, void* userData) | 设置接收HTML消息的回调。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### postMessage()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkWeb_ErrorCode (*postMessage)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, const ArkWeb_WebMessagePtr webMessage)
```
 
**描述：**
 
发送消息到HTML。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const ArkWeb_WebMessagePortPtr webMessagePort | Post Message端口结构体指针。 |
| const char* webTag | Web组件名称。 |
| const ArkWeb_WebMessagePtr webMessage | 需要发送的消息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkWeb_ErrorCode | ARKWEB_SUCCESS 执行成功。 ARKWEB_INVALID_PARAM 参数无效。 ARKWEB_INIT_ERROR 初始化失败，没有找到与webTag绑定的Web组件。 |
 
 
  

#### close()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*close)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag)
```
 
**描述：**
 
关闭消息端口。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const ArkWeb_WebMessagePortPtr webMessagePort | Post Message端口结构体指针。 |
| const char* webTag | Web组件名称。 |
 
 
  

#### setMessageEventHandler()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*setMessageEventHandler)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag,
        ArkWeb_OnMessageEventHandler messageEventHandler, void* userData)
```
 
**描述：**
 
设置接收HTML消息的回调。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const ArkWeb_WebMessagePortPtr webMessagePort | Post Message端口结构体指针。 |
| const char* webTag | Web组件名称。 |
| ArkWeb_OnMessageEventHandler messageEventHandler | 处理消息的回调。 |
| void* userData | 用户自定义数据。 |
