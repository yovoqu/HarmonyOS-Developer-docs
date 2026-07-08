# ArkWeb_JavaScriptValueAPI

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptvalueapi
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkWeb_JavaScriptValueAPI
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkWeb_JavaScriptValueAPI是JavaScript相关Native API结构体。该结构体提供了创建JavaScript值的函数，支持将Native数据转换为JavaScript可识别的格式并返回给HTML。
 
JavaScript相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取，调用前建议通过[ARKWEB_MEMBER_MISSING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#宏定义)校验函数指针的可用性，避免SDK与设备ROM不匹配导致崩溃。
 
**起始版本：** 18
 
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
| ArkWeb_JavaScriptValuePtr (*createJavaScriptValue)(ArkWeb_JavaScriptValueType type, void* data, size_t dataLength) | 创建一个JavaScript值，用于返回给HTML。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### createJavaScriptValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkWeb_JavaScriptValuePtr (*createJavaScriptValue)(ArkWeb_JavaScriptValueType type, void* data, size_t dataLength)
```
 
**描述：**
 
创建一个JavaScript值，用于返回给HTML。
 
**起始版本：** 18
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkWeb_JavaScriptValueType type | JavaScript值的类型。 |
| void* data | JavaScript值的数据缓冲区。 |
| size_t dataLength | JavaScript值的缓冲区大小。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkWeb_JavaScriptValuePtr | 创建出来的JavaScript值。当输入参数无效或内存分配失败时，返回NULL。 |
