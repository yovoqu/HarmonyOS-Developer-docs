# http_interceptor.h

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义HTTP全局拦截器模块的接口。通过拦截器，开发者可以监控HTTP流量，实现日志记录功能。
 
- **只读拦截器限制**：请勿在只读拦截器中修改请求和响应的内容或释放指针。即使进行修改，该修改也不会对请求生效，但可能会影响后续只读拦截器对数据包内容的读取。此外，在只读拦截器中设置 OH_ABORT 也不会生效。
- **支持的组件**：全局拦截器目前支持 [@ohos.net.http](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http)、[net_http.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-h)、[rcp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp)、[@ohos.request.cacheDownload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request-cachedownload)。
- **触发条件**：
不拦截自动重定向的中间过程(仅暴露最终响应)。
- 不拦截缓存命中时的响应(因无实际网络请求)。

  
 
**引用文件：** <network/netstack/http_interceptor.h>
 
**库：** libhttp_interceptor.so
 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 24
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t OH_Http_AddReadOnlyInterceptor(struct OH_Http_Interceptor *interceptor) | 添加一个HTTP全局只读拦截器。 |
| int32_t OH_Http_RemoveInterceptor(struct OH_Http_Interceptor *interceptor) | 删除指定的HTTP全局拦截器。 |
| int32_t OH_Http_RemoveAllInterceptors(int32_t groupId) | 删除指定组ID的所有HTTP拦截器。 |
| int32_t OH_Http_StartAllInterceptors(int32_t groupId) | 启用指定组ID的所有HTTP拦截器。 |
| int32_t OH_Http_StopAllInterceptors(int32_t groupId) | 停用指定组ID的所有HTTP拦截器。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_Http_AddReadOnlyInterceptor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_Http_AddReadOnlyInterceptor(struct OH_Http_Interceptor *interceptor)
```
 
**描述**
 
添加一个HTTP全局只读拦截器。
 
- 当前仅支持只读响应(OH_STAGE_RESPONSE)拦截器。
- 拦截器一旦添加，将持续生效，直至开发者显式移除。
- 必须调用[OH_Http_RemoveInterceptor](#oh_http_removeinterceptor)移除单个拦截器，或调用[OH_Http_RemoveAllInterceptors](#oh_http_removeallinterceptors)移除整组拦截器以释放资源。
- 拦截器[OH_Http_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor)的成员变量enabled为0，需要调用[OH_Http_StartAllInterceptors](#oh_http_startallinterceptors)启动拦截器。

 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct OH_Http_Interceptor *interceptor | 待添加的拦截器，指向OH_Http_Interceptor结构体的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功；返回值为201表示权限被拒绝；返回值为401表示参数错误（如指针为nullptr，或不支持所添加的拦截器类型）。详细错误码请参考OH_HTTP_RESULT_OK、OH_HTTP_PERMISSION_DENIED和OH_HTTP_PARAMETER_ERROR。 |
 
 
  

#### OH_Http_RemoveInterceptor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_Http_RemoveInterceptor(struct OH_Http_Interceptor *interceptor)
```
 
**描述**
 
删除指定的HTTP全局拦截器。
 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct OH_Http_Interceptor *interceptor | 待删除的拦截器，指向OH_Http_Interceptor结构体的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功；返回值为201表示权限被拒绝；返回值为401表示参数错误（如指针为 nullptr）。详细错误码请参考OH_HTTP_RESULT_OK、OH_HTTP_PERMISSION_DENIED和OH_HTTP_PARAMETER_ERROR。 |
 
 
  

#### OH_Http_RemoveAllInterceptors()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_Http_RemoveAllInterceptors(int32_t groupId)
```
 
**描述**
 
删除指定组ID的所有HTTP拦截器。
 
- 组ID由应用在创建拦截器时自行分配和管理。
- 若应用内部多个模块使用拦截器，必须合理规划组ID，避免冲突。
- 组ID冲突可能导致调用此函数时意外删除其他模块的拦截器。

 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| int32_t groupId | 拦截器组ID。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功；返回值为201表示权限被拒绝。详细错误码请参考OH_HTTP_RESULT_OK和OH_HTTP_PERMISSION_DENIED。 |
 
 
  

#### OH_Http_StartAllInterceptors()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_Http_StartAllInterceptors(int32_t groupId)
```
 
**描述**
 
启用指定组ID的所有HTTP拦截器。
 
- 调用[OH_Http_StopAllInterceptors](#oh_http_stopallinterceptors)停止拦截器。

 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| int32_t groupId | 拦截器组ID。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功；返回值为201表示权限被拒绝。详细错误码请参考OH_HTTP_RESULT_OK和OH_HTTP_PERMISSION_DENIED。 |
 
 
  

#### OH_Http_StopAllInterceptors()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_Http_StopAllInterceptors(int32_t groupId)
```
 
**描述**
 
停用指定组ID的所有HTTP拦截器。
 
- 调用[OH_Http_StartAllInterceptors](#oh_http_startallinterceptors)重新启用拦截器。

 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| int32_t groupId | 拦截器组ID。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功；返回值为201表示权限被拒绝。详细错误码请参考OH_HTTP_RESULT_OK和OH_HTTP_PERMISSION_DENIED。 |
