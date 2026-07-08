# ArkWeb_ProxyMethod

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxymethod
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkWeb_ProxyMethod
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkWeb_ProxyMethod是用于定义JavaScript代理方法的结构体，指定了一个可以从JavaScript调用的Native方法的基本信息。该结构体包含方法名称（methodName）和对应的Native回调函数指针（callback）两个字段。多个ArkWeb_ProxyMethod可以组合成ArkWeb_ProxyObject，以对象的形式整体注入到Web页面中。
 
**起始版本：** 12
 
**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)
 
**所在头文件：** [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char* methodName | 注入的方法名。 |
| ArkWeb_OnJavaScriptProxyCallback callback | Proxy方法执行的回调。 |
| void* userData | 需要在回调中携带的自定义数据。 |
