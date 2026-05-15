# Class (WebSchemeHandlerRequest)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerrequest
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通过WebSchemeHandler拦截到的请求。


## getHeader12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getHeader(): Array<WebHeader>

获取资源请求头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Array&lt;[WebHeader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-i#webheader)&gt; | 返回资源请求头信息。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## getRequestUrl12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getRequestUrl(): string

获取资源请求的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 返回资源请求的URL信息。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## getRequestMethod12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getRequestMethod(): string

获取请求方法。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 返回请求方法。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## getReferrer12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getReferrer(): string

获取referrer。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 获取到的referrer。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## isMainFrame12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isMainFrame(): boolean

判断资源请求是否为主frame。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 判断资源请求是否为主frame，如果资源请求是主frame则返回true，否则返回false。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## hasGesture12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

hasGesture(): boolean

获取资源请求是否与手势（如点击）相关联。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源请求是否与手势（如点击）相关联，如果返回资源请求与手势相关联则返回true，否则返回false。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## getHttpBodyStream12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getHttpBodyStream(): WebHttpBodyStream | null

获取资源请求中的WebHttpBodyStream。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [WebHttpBodyStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream) \| null | 返回资源请求中的WebHttpBodyStream，如果没有则返回null。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## getRequestResourceType12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getRequestResourceType(): WebResourceType

获取资源请求的资源类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [WebResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-e#webresourcetype12) | 返回资源请求的资源类型。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。


## getFrameUrl12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getFrameUrl(): string

获取触发此请求的Frame的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 返回触发此请求的Frame的URL。 |


**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。
