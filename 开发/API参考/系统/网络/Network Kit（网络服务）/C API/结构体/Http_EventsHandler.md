# Http_EventsHandler

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-eventshandler
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Http_EventsHandler {...} Http_EventsHandler
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

监听不同HTTP事件的回调函数。
 
**起始版本：** 20
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Http_OnDataReceiveCallback onDataReceive | 收到响应体时的回调函数，参考Http_OnDataReceiveCallback。 |
| Http_OnProgressCallback onUploadProgress | 上传时调用的回调函数，参考Http_OnProgressCallback。 |
| Http_OnProgressCallback onDownloadProgress | 下载时调用的回调函数，参考Http_OnProgressCallback。 |
| Http_OnHeaderReceiveCallback onHeadersReceive | 收到header时的回调函数，参考Http_OnHeaderReceiveCallback。 |
| Http_OnVoidCallback onDataEnd | 传输结束时的回调函数，参考Http_OnVoidCallback。 |
| Http_OnVoidCallback onCanceled | 请求被取消时的回调函数，参考Http_OnVoidCallback。 |
