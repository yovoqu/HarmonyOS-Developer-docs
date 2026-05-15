# ArkWeb_JavaScriptObject

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptobject
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct {...} ArkWeb_JavaScriptObject
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

注入的JavaScript结构体。

**起始版本：** 12

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| const uint8_t* buffer | 注入的JavaScript代码。 |
| size_t size | JavaScript代码长度。 |
| [ArkWeb_OnJavaScriptCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#arkweb_onjavascriptcallback) callback | JavaScript执行完成的回调。 |
| void* userData | 需要在回调中携带的自定义数据。 |
