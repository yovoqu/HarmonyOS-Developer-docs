# Class (SslErrorHandler)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-sslerrorhandler
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Web组件返回的SSL错误通知事件的处理对象。示例代码参考[onSslErrorEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onsslerrorevent12)事件。


## constructor9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

SslErrorHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## handleCancel9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

handleCancel(): void

通知Web组件取消此请求。

**系统能力：** SystemCapability.Web.Webview.Core


## handleConfirm9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

handleConfirm(): void

通知Web组件继续使用SSL证书。

**系统能力：** SystemCapability.Web.Webview.Core


## handleCancel20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

handleCancel(abortLoading: boolean): void

通知Web组件取消此请求，并根据参数abortLoading决定是否停止加载。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abortLoading | boolean | 是 | 是否在取消请求后停止加载页面。 true表示停止加载页面，false表示继续加载页面。 默认值为false。 |
