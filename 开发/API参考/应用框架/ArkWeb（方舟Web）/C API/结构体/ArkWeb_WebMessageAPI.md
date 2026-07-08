# ArkWeb_WebMessageAPI

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageapi
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkWeb_WebMessageAPI
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkWeb_WebMessageAPI是Web消息相关Native API结构体。该结构体提供了创建和销毁消息、设置和获取消息类型、管理消息数据缓冲区等函数。此API是postMessage桥接的一部分，支持Native代码与HTML页面之间的双向通信。
 
Web消息相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取，调用前建议通过[ARKWEB_MEMBER_MISSING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#宏定义)校验函数指针的可用性，避免SDK与设备ROM不匹配导致崩溃。
 
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
| ArkWeb_WebMessagePtr (*createWebMessage)() | 创建消息。 |
| void (*destroyWebMessage)(ArkWeb_WebMessagePtr* webMessage) | 销毁消息。 |
| void (*setType)(ArkWeb_WebMessagePtr webMessage, ArkWeb_WebMessageType type) | 设置消息类型。 |
| ArkWeb_WebMessageType (*getType)(ArkWeb_WebMessagePtr webMessage) | 获取消息类型。 |
| void (*setData)(ArkWeb_WebMessagePtr webMessage, void* data, size_t dataLength) | 设置数据。 |
| void* (*getData)(ArkWeb_WebMessagePtr webMessage, size_t* dataLength) | 获取数据。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### createWebMessage()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkWeb_WebMessagePtr (*createWebMessage)()
```
 
**描述**
 
创建消息。
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkWeb_WebMessagePtr | 消息结构体指针。 |
 
 
  

#### destroyWebMessage()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*destroyWebMessage)(ArkWeb_WebMessagePtr* webMessage)
```
 
**描述**
 
销毁消息。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkWeb_WebMessagePtr* webMessage | 需要销毁的消息。 |
 
 
  

#### setType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*setType)(ArkWeb_WebMessagePtr webMessage, ArkWeb_WebMessageType type)
```
 
**描述**
 
设置消息类型。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkWeb_WebMessagePtr webMessage | 消息结构体指针。 |
| ArkWeb_WebMessageType type | 消息类型。 |
 
 
  

#### getType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkWeb_WebMessageType (*getType)(ArkWeb_WebMessagePtr webMessage)
```
 
**描述**
 
获取消息类型。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkWeb_WebMessagePtr webMessage | 消息结构体指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkWeb_WebMessageType | 消息类型。 |
 
 
  

#### setData()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*setData)(ArkWeb_WebMessagePtr webMessage, void* data, size_t dataLength)
```
 
**描述**
 
设置数据。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkWeb_WebMessagePtr webMessage | 消息结构体指针。 |
| void* data | 数据指针。 |
| size_t dataLength | 数据长度。 |
 
 
  

#### getData()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* (*getData)(ArkWeb_WebMessagePtr webMessage, size_t* dataLength)
```
 
**描述**
 
获取数据。
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkWeb_WebMessagePtr webMessage | 消息结构体指针。 |
| size_t* dataLength | 出参，数据长度。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| void* | 数据指针。 |
