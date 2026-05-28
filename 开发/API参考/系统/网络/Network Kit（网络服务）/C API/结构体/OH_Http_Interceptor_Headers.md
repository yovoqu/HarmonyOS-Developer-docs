# OH_Http_Interceptor_Headers

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-headers
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Http_Interceptor_Headers {
    char *data;
    struct OH_Http_Interceptor_Headers *next;
} OH_Http_Interceptor_Headers;
```
  

##### 概述

定义拦截器的请求/响应头信息。
 
**起始版本：** 24
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [http_interceptor_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char *data | 拦截器请求/响应头信息。 |
| struct OH_Http_Interceptor_Headers *next | 指向下一个头信息的指针。 |
