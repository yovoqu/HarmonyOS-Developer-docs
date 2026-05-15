# Class (JsResult)

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Web组件返回的弹窗确认或取消功能对象。示例代码参考[onAlert事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onalert)。


## constructor
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

JsResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## handleCancel
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

handleCancel(): void

通知Web组件用户取消弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core


## handleConfirm
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

handleConfirm(): void

通知Web组件用户确认弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core


## handlePromptConfirm9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

handlePromptConfirm(result: string): void

通知Web组件用户确认弹窗操作及对话框内容。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | string | 是 | 用户输入的对话框内容。 |
