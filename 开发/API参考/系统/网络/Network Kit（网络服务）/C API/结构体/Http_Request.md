# Http_Request

更新时间：2026-03-12 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct Http_Request {...} Http_Request
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

HTTP请求结构体。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| uint32_t requestId | HTTP请求的ID。 |
| char *url | HTTP请求的URL。 |
| [Http_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-requestoptions) *options | HTTP请求配置，指向Http_RequestOptions的指针，参考[Http_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-requestoptions)。 |
