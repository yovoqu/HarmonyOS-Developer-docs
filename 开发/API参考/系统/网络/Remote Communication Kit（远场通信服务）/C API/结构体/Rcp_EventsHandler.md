# Rcp_EventsHandler

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

监听不同HTTP事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [Rcp_OnDataReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_data_receive_callback)[onDataReceive](#ondatareceive) | 收到响应体时的回调函数。 |
| [Rcp_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback)[onUploadProgress](#onuploadprogress) | 上传时调用的回调函数。 |
| [Rcp_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback)[onDownloadProgress](#ondownloadprogress) | 下载时调用的回调函数。 |
| [Rcp_OnHeaderReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_header_receive_callback)[onHeaderReceive](#onheaderreceive) | 收到header时的回调函数。 |
| [Rcp_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback)[onDataEnd](#ondataend) | 传输结束时的回调函数。 |
| [Rcp_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback)[onCanceled](#oncanceled) | 请求或会话被取消时的回调函数。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### onCanceled
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
Rcp_OnVoidCallback Rcp_EventsHandler::onCanceled
```

**描述**

请求或会话被取消时的回调函数。


### onDataEnd
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
Rcp_OnVoidCallback Rcp_EventsHandler::onDataEnd
```

**描述**

传输结束时的回调函数。


### onDataReceive
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
Rcp_OnDataReceiveCallback Rcp_EventsHandler::onDataReceive
```

**描述**

收到响应体时的回调函数。


### onDownloadProgress
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
Rcp_OnProgressCallback Rcp_EventsHandler::onDownloadProgress
```

**描述**

下载时调用的回调函数。


### onHeaderReceive
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
Rcp_OnHeaderReceiveCallback Rcp_EventsHandler::onHeaderReceive
```

**描述**

收到header时的回调函数。


### onUploadProgress
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
Rcp_OnProgressCallback Rcp_EventsHandler::onUploadProgress
```

**描述**

上传时调用的回调函数。
