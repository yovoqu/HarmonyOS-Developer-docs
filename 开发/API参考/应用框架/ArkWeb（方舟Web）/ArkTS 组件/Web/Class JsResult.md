# Class (JsResult)

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

JsResult是Web组件在处理JavaScript弹窗事件时返回的结果处理对象，适用于开发者拦截并自定义处理window.alert、window.confirm、window.prompt等弹窗场景。开发者可在[onAlert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onalert)、[onConfirm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onconfirm)或[onPrompt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onprompt9)等事件回调中，通过该对象向Web组件反馈用户的确认、取消或输入内容等操作结果，从而控制弹窗的后续行为。
 
> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 8开始支持。 示例效果请以真机运行为准。

  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
JsResult的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

#### handleCancel

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

handleCancel(): void
 
通知Web组件用户取消弹窗操作。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

#### handleConfirm

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

handleConfirm(): void
 
通知Web组件用户确认弹窗操作。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

#### handlePromptConfirm9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

handlePromptConfirm(result: string): void
 
通知Web组件用户确认弹窗操作及对话框内容。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | string | 是 | 用户输入的对话框内容。 |
