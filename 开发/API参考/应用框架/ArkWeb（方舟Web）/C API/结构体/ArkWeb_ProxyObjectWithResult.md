# ArkWeb_ProxyObjectWithResult

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxyobjectwithresult
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkWeb_ProxyObjectWithResult
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkWeb_ProxyObjectWithResult是带返回值的JavaScript代理对象结构体，扩展了ArkWeb_ProxyObject的能力。该结构体将多个ArkWeb_ProxyMethodWithResult组织成对象注入到Web页面中，支持JavaScript调用Native方法后获取返回值。适用于需要向Web前端返回结构化执行结果的API场景。
 
**起始版本：** 18
 
**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)
 
**所在头文件：** [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char* objName | 注入的对象名。 |
| const ArkWeb_ProxyMethodWithResult* methodList | 注入的对象携带的方法结构体数组。 |
| size_t size | 方法结构体数组的长度。 |
