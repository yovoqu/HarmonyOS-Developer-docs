# Class (ScreenCaptureHandler)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Web组件返回授权或拒绝屏幕捕获功能的对象。示例代码参考[onScreenCaptureRequest事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onscreencapturerequest10)。


## constructor10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

ScreenCaptureHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## deny10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

deny(): void

拒绝网页所请求的屏幕捕获操作。

**系统能力：** SystemCapability.Web.Webview.Core


## getOrigin10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getOrigin(): string

获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 当前请求权限网页的来源。 |


## grant10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

grant(config: ScreenCaptureConfig): void

对网页访问的屏幕捕获操作进行授权。


> [!NOTE]
> 需要配置权限：ohos.permission.MICROPHONE。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ScreenCaptureConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#screencaptureconfig10) | 是 | 屏幕捕获配置。 |
