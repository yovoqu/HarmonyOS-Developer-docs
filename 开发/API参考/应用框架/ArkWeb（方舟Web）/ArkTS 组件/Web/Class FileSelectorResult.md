# Class (FileSelectorResult)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorresult
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通知Web组件的文件选择结果。示例代码参考[onShowFileSelector事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onshowfileselector9)。


## constructor9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

FileSelectorResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core


## handleFileList9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

handleFileList(fileList: Array<string>): void

通知Web组件进行文件选择操作。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileList | Array&lt;string&gt; | 是 | 需要进行操作的文件列表。 |
