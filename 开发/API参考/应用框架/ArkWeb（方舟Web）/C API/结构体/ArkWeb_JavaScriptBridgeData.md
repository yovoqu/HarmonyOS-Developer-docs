# ArkWeb_JavaScriptBridgeData

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptbridgedata
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct {...} ArkWeb_JavaScriptBridgeData
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义JavaScript Bridge数据的基础结构。

**起始版本：** 12

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| const uint8_t* buffer | 指向传输数据的指针。仅支持前端传入String和ArrayBuffer类型，其余类型会被json序列化后，以String类型传递。 |
| size_t size | 传输数据的长度。 |
