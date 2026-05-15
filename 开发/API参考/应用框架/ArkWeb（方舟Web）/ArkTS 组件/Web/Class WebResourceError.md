# Class (WebResourceError)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceerror
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Web组件资源管理错误信息对象。示例代码参考[onErrorReceive事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onerrorreceive)。


## constructor
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

WebResourceError的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## getErrorCode
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getErrorCode(): number

获取加载资源的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 返回加载资源的错误码。错误码含义参考[WebNetErrorList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-neterrorlist#webneterrorlist)、HTTP协议状态码。 |


## getErrorInfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getErrorInfo(): string

获取加载资源的错误信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 返回加载资源的错误信息。 |
