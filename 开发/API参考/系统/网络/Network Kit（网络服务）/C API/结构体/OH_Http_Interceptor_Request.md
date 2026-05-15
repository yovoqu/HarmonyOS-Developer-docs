# OH_Http_Interceptor_Request

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-request
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct OH_Http_Interceptor_Request {
Http_Buffer url;
Http_Buffer method;
OH_Http_Interceptor_Headers *headers;
Http_Buffer body;
} OH_Http_Interceptor_Request;
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义拦截器的HTTP请求数据包结构。

**起始版本：** 24

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [http_interceptor_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| Http_Buffer url | 请求URL，详情请参考[Http_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer)定义。 |
| Http_Buffer method | 请求方法，详情请参考[Http_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer)定义。 |
| OH_Http_Interceptor_Headers *headers | HTTP请求头信息，详情请参考[OH_Http_Interceptor_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-headers)定义。 |
| Http_Buffer body | 请求体内容，详情请参考[Http_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer)定义。 |
