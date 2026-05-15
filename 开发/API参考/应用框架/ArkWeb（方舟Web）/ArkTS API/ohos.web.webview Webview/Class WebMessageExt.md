# Class (WebMessageExt)

更新时间：2026-04-13 09:29:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

[WebMessagePort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport)接口接收、发送的数据对象。


## getType10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getType(): WebMessageType

获取数据对象的类型。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [WebMessageType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-e#webmessagetype10) | [WebMessagePort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport)接口所支持的数据类型。 |


## getString10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getString(): string

获取数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 返回字符串类型的数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |


## getNumber10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getNumber(): number

获取数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 返回数值类型的数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |


## getBoolean10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getBoolean(): boolean

获取数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 返回布尔类型的数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |


## getArrayBuffer10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getArrayBuffer(): ArrayBuffer

获取数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回原始二进制数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |


## getArray10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getArray(): Array<string | number | boolean>

获取数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Array&lt;string \| number \| boolean&gt; | 返回数组类型的数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |


## getError10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getError(): Error

获取数据对象的错误类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Error | 返回错误对象类型的数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |


## setType10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setType(type: WebMessageType): void

设置数据对象的类型。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [WebMessageType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-e#webmessagetype10) | 是 | [WebMessagePort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport)接口所支持的数据类型。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


## setString10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setString(message: string): void

设置数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 字符串类型数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


## setNumber10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setNumber(message: number): void

设置数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | number | 是 | 数值类型数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


## setBoolean10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setBoolean(message: boolean): void

设置数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | boolean | 是 | 布尔类型数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


## setArrayBuffer10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setArrayBuffer(message: ArrayBuffer): void

设置数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | ArrayBuffer | 是 | 原始二进制类型数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| ��误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


## setArray10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setArray(message: Array<string | number | boolean>): void

设置数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Array&lt;string \| number \| boolean&gt; | 是 | 数组类型数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


## setError10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setError(message: Error): void

设置数据对象的错误对象类型数据。完整示例代码参考[onMessageEventExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport#onmessageeventext10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Error | 是 | 错误对象类型数据。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
