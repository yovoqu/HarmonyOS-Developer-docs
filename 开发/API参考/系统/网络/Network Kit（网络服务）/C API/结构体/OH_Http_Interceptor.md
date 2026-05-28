# OH_Http_Interceptor

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Http_Interceptor {
    int32_t groupId;
    OH_Interceptor_Stage stage;
    OH_Interceptor_Type type;
    OH_Http_InterceptorHandler handler;
    int32_t enabled;
} OH_Http_Interceptor;
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义HTTP全局拦截器的配置信息。
 
**起始版本：** 24
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [http_interceptor_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t groupId | 拦截器组ID。 |
| OH_Interceptor_Stage stage | 拦截器的执行阶段，详情请参考OH_Interceptor_Stage 枚举定义。 |
| OH_Interceptor_Type type | 拦截器的类型，详情请参考OH_Interceptor_Type 枚举定义。 |
| OH_Http_InterceptorHandler handler | 拦截器处理函数，详情请参考OH_Http_InterceptorHandler 函数指针定义。 |
| int32_t enabled | 拦截器的启用状态。0代表未启用，非0代表启用。 |
