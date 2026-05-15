# Class (PermissionRequest)

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-permissionrequest
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Web组件返回授权或拒绝权限功能的对象。示例代码参考[onPermissionRequest事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onpermissionrequest9)。


## constructor9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

PermissionRequest的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## deny9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

deny(): void

拒绝网页所请求的权限。

**系统能力：** SystemCapability.Web.Webview.Core


## getOrigin9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getOrigin(): string

获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 当前请求权限网页的来源。 |


## getAccessibleResource9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getAccessibleResource(): Array<string>

获取网页所请求的权限资源列表，资源列表类型参考[ProtectedResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#protectedresourcetype9)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 网页所请求的权限资源列表。 |


## grant9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

grant(resources: Array<string>): void

对网页所请求的权限进行授权。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resources | Array&lt;string&gt; | 是 | 授予网页请求的权限的资源列表。 |
