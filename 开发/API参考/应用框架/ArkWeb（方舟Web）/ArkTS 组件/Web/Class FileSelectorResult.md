# Class (FileSelectorResult)

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorresult
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

FileSelectorResult是ArkWeb组件中用于通知Web组件文件选择结果的类。当Web组件中的HTML页面通过<input type="file">等方式发起文件选择请求时，应用可通过FileSelectorResult将用户选择的文件列表回传给Web组件，完成文件选择流程。该类主要在onShowFileSelector事件回调中使用，适用于应用需要自定义文件选择行为的场景，例如拉起系统文件选择器、图库选择器或相机选择器后，将选中的文件结果返回给Web页面。
 
示例代码参考[onShowFileSelector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onshowfileselector9)。
 
> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 9开始支持。 示例效果请以真机运行为准。

  

#### constructor9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
FileSelectorResult的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

#### handleFileList9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

handleFileList(fileList: Array&lt;string&gt;): void
 
通过传入的文件列表（fileList）通知Web组件用户选择的文件，完成文件选择流程。Web组件可以使用传入的文件列表进行后续处理。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileList | Array&lt;string&gt; | 是 | 需要进行操作的文件列表。 |
