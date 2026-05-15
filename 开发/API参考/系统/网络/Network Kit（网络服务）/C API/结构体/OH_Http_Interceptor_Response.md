# OH_Http_Interceptor_Response

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-response
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct OH_Http_Interceptor_Response {
Http_Buffer body;
Http_ResponseCode responseCode;
OH_Http_Interceptor_Headers *headers;
Http_PerformanceTiming performanceTiming;
} OH_Http_Interceptor_Response;
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义拦截器的HTTP响应数据包结构。

**起始版本：** 24

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [http_interceptor_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| Http_Buffer body | 响应体内容，详情请参考[Http_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer)定义。 |
| Http_ResponseCode responseCode | 响应状态码，详情请参考[Http_ResponseCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_responsecode) 枚举定义。 |
| OH_Http_Interceptor_Headers *headers | HTTP响应头信息，详情请参考[OH_Http_Interceptor_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-headers)定义。 |
| Http_PerformanceTiming performanceTiming | 响应性能信息，详情请参考[Http_PerformanceTiming](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-performancetiming)定义。 |
