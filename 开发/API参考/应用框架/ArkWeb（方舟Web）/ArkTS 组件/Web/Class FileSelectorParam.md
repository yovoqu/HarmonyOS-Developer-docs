# Class (FileSelectorParam)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorparam
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Web组件获取文件对象。示例代码参考[onShowFileSelector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onshowfileselector9)。

> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 9开始支持。 示例效果请以真机运行为准。



##### constructor9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()

FileSelectorParam的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core



##### getTitle9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getTitle(): string

获取文件选择器标题。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回文件选择器标题。 |




##### getMode9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMode(): FileSelectorMode

获取文件选择器的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FileSelectorMode | 返回文件选择器的模式。 |




##### getAcceptType9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAcceptType(): Array&lt;string&gt;

获取文件过滤类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 返回文件过滤类型。 |




##### isCapture9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isCapture(): boolean

获取是否调用多媒体能力。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否调用多媒体能力。 true表示需要调用摄像头或麦克风等多媒体设备来获取文件（如拍照或录音），false表示仅从存储设备中选择已有文件。 |




##### getMimeTypes18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMimeTypes(): Array&lt;string&gt;

获取文件MIME类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 返回文件MIME类型。 |




##### getSuggestedName23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSuggestedName(): string

获取建议选择的文件名。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的suggestedName。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回建议选择的文件名。 |




##### getDefaultPath23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getDefaultPath(): string

获取文件选择器默认起始路径。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的startIn。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回默认起始路径。 当前端startIn设置为公共目录downloads、pictures时，要注意应分别转化为HarmonyOS系统下的download和images，请参考获取并使用公共目录。 |




##### getDescriptions23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getDescriptions(): Array&lt;string&gt;

获取各组文件类型的描述。为允许的文件类型类别的可选描述。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的description。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 返回文件类型的描述数组。 |




##### isAcceptAllOptionExcluded23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isAcceptAllOptionExcluded(): boolean

获取文件选择器是否包含选项（*/*），即所有文件。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的excludeAcceptAllOption。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否排除“所有文件类型”选项。 true表示排除（不包含“所有文件类型”选项）。false表示不排除，开发者需要在文件选择器中添加“所有文件类型”选项。 |




##### getAcceptableFileTypes23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAcceptableFileTypes(): Array<Array&lt;AcceptableFileType&gt;>

获取文件类型信息。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的types。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Array&lt;AcceptableFileType&gt;> | 返回文件types信息。 |
