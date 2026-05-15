# Class (EventResult)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-eventresult
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通知Web组件同层事件消费结果，支持的事件：[触摸事件的类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#touchtype)和[鼠标事件的类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#mouseaction8)，鼠标仅支持[左中右按键](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#mousebutton8)。

如果应用不消费该事件，则应设置消费结果为false，事件将会被Web组件消费；反之如果应用消费了该事件，则应将消费结果设置为true，Web组件将不消费该事件。若应用设置消费结果不符合以上使用规格，将产生与开发者预期不匹配的现象。

触摸事件示例代码参考[onNativeEmbedGestureEvent事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedgestureevent11)。

鼠标事件示例代码参考[onNativeEmbedMouseEvent事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedmouseevent20)。


## constructor12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

EventResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## setGestureEventResult12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setGestureEventResult(result: boolean): void

设置手势事件消费结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 是否消费该手势事件。 true表示消费该手势事件，false表示不消费该手势事件。 传入null或undefined时为true。 |


**示例：**

请参考[onNativeEmbedGestureEvent事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedgestureevent11)。


## setGestureEventResult14+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setGestureEventResult(result: boolean, stopPropagation: boolean): void

设置手势事件消费结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 是否消费该手势事件。 true表示消费该手势事件，false表示不消费该手势事件。 传入null或undefined时为true。 |
| stopPropagation | boolean | 是 | 是否阻止冒泡，在result为true时生效。 true表示阻止冒泡，false表示不阻止冒泡。 传入null或undefined时为true。 |


**示例：**

请参考[onNativeEmbedGestureEvent事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedgestureevent11)。


## setMouseEventResult20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setMouseEventResult(result: boolean, stopPropagation?: boolean): void

设置鼠标事件消费结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 是否消费该鼠标事件。 true表示消费该鼠标事件，false表示不消费该鼠标事件。 传入null或undefined时为true。 |
| stopPropagation | boolean | 否 | 是否阻止冒泡，在result为true时生效。 true表示阻止冒泡，false表示不阻止冒泡。 传入null或undefined时为true。 默认值：true。 |


**示例：**

请参考[onNativeEmbedMouseEvent事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedmouseevent20)。
