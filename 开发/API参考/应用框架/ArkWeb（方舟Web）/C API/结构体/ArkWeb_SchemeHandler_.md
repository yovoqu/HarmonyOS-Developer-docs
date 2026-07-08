# ArkWeb_SchemeHandler_

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-schemehandler
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkWeb_SchemeHandler_ ArkWeb_SchemeHandler
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkWeb_SchemeHandler是用于注册自定义Scheme（协议）拦截器的结构体，定义了onRequestStart请求开始回调和onRequestStop请求停止回调两个函数指针。通过该结构体，开发者可以拦截Web组件中指定scheme的网络请求：在onRequestStart中判断是否拦截并返回自定义数据，在onRequestStop中执行资源清理。该结构体配合ArkWeb_ResourceHandler和ArkWeb_Response实现完整的请求拦截与自定义响应流程。
 
**起始版本：** 12
 
**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)
 
**所在头文件：** [arkweb_scheme_handler.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-scheme-handler-h)
