# Http_EventsHandler

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-eventshandler
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct Http_EventsHandler {...} Http_EventsHandler
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

监听不同HTTP事件的回调函数。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [Http_OnDataReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_ondatareceivecallback) onDataReceive | 收到响应体时的回调函数，参考[Http_OnDataReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_ondatareceivecallback)。 |
| [Http_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onprogresscallback) onUploadProgress | 上传时调用的回调函数，参考[Http_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onprogresscallback)。 |
| [Http_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onprogresscallback) onDownloadProgress | 下载时调用的回调函数，参考[Http_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onprogresscallback)。 |
| [Http_OnHeaderReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onheaderreceivecallback) onHeadersReceive | 收到header时的回调函数，参考[Http_OnHeaderReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onheaderreceivecallback)。 |
| [Http_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onvoidcallback) onDataEnd | 传输结束时的回调函数，参考[Http_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onvoidcallback)。 |
| [Http_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onvoidcallback) onCanceled | 请求被取消时的回调函数，参考[Http_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_onvoidcallback)。 |
