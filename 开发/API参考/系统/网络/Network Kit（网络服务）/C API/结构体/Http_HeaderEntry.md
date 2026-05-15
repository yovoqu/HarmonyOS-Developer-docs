# Http_HeaderEntry

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headerentry
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct Http_HeaderEntry {...} Http_HeaderEntry
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

请求或者响应的标头的所有键值对。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| char *key | 请求或者响应的标头中的键。 |
| [Http_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue) *value | 请求或者响应的标头中的键对应的值，参考[Http_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue)。 |
| struct Http_HeaderEntry *next | 链式存储。指向下一个Http_HeaderEntry。 |
