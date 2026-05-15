# Rcp_SyncInterceptor

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

同步拦截器。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [Rcp_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response) *(* [intercept](#intercept) )([Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) *request, const [Rcp_SyncRequestHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_syncrequesthandler) *next, uint32_t *errCode) | 指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### intercept
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
Rcp_Response*(* Rcp_SyncInterceptor::intercept) (Rcp_Request *request, const Rcp_SyncRequestHandler *next, uint32_t *errCode)
```

**描述**

指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

**起始版本：** 5.0.0(12)

**参数:**


| 名称 | 描述 |
| --- | --- |
| request | 指向[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。 |
| next | 指向下一个同步处理器的指针[Rcp_SyncRequestHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_syncrequesthandler)。 |
| errCode | 表示拦截器的返回值。 |


**返回：**

Rcp_Response* 返回的响应。
