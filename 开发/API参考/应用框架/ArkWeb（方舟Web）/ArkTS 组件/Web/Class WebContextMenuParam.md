# Class (WebContextMenuParam)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuparam
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

实现长按页面元素或鼠标右键弹出的菜单信息。示例代码参考[onContextMenuShow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontextmenushow9)。
 
> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 9开始支持。 示例效果请以真机运行为准。

  

##### constructor9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
WebContextMenuParam的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

##### x9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

x(): number
 
弹出菜单的x坐标。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。 单位：px（物理像素）。 |
 
 
  

##### y9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

y(): number
 
弹出菜单的y坐标。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。 单位：px（物理像素）。 |
 
 
  

##### getLinkUrl9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getLinkUrl(): string
 
获取经过安全检查的URL链接地址。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回经过安全检查的URL链接。 |
 
 
  

##### getUnfilteredLinkUrl9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getUnfilteredLinkUrl(): string
 
获取原始URL链接地址。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回原始的URL链接。 |
 
 
  

##### getSourceUrl9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSourceUrl(): string
 
获取sourceUrl链接。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 如果选中的元素有src属性，返回src的URL。返回URL的最大上限为2MB，超出上限时返回空字符串。 |
 
 
  

##### existsImageContents9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

existsImageContents(): boolean
 
是否存在图像内容。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| boolean | 长按位置中有图片返回true，否则返回false。 |
 
 
  

##### getMediaType9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMediaType(): ContextMenuMediaType
 
获取网页元素媒体类型。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| ContextMenuMediaType | 网页元素媒体类型。 |
 
 
  

##### getSelectionText9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSelectionText(): string
 
获取选中文本。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 菜单上下文选中文本内容，不存在则返回空。 |
 
 
  

##### getSourceType9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSourceType(): ContextMenuSourceType
 
获取菜单事件来源。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| ContextMenuSourceType | 菜单事件来源。 |
 
 
  

##### getInputFieldType9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getInputFieldType(): ContextMenuInputFieldType
 
获取网页元素输入框类型。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| ContextMenuInputFieldType | 输入框类型。 |
 
 
  

##### isEditable9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isEditable(): boolean
 
判断网页元素是否可编辑。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| boolean | 网页元素可编辑返回true，不可编辑返回false。 |
 
 
  

##### getEditStateFlags9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getEditStateFlags(): number
 
获取网页元素可编辑标识。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 网页元素可编辑标识，参照ContextMenuEditStateFlags。 |
 
 
  

##### getPreviewWidth13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getPreviewWidth(): number
 
获取预览图的宽。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 预览图的宽。 单位：px（物理像素）。 |
 
 
  

##### getPreviewHeight13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getPreviewHeight(): number
 
获取预览图的高。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 预览图的高。 单位：px（物理像素）。 |
 
 
  

##### getContextMenuMediaType22+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getContextMenuMediaType(): ContextMenuDataMediaType
 
在上报上下文菜单事件时，获取用户点击的网页元素类型。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| ContextMenuDataMediaType | 网页元素媒体类型。 |
