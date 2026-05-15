# Class (ControllerHandler)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-controllerhandler
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

设置用户新建Web组件的WebviewController对象。示例代码参考[onWindowNew事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onwindownew9)。


## constructor9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

ControllerHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## setWebController9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setWebController(controller: WebviewController): void

设置WebviewController对象，如果不需要打开新窗口请设置为null。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [WebviewController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller) | 是 | 新建Web组件的WebviewController对象，如果不需要打开新窗口请设置为null。 |
