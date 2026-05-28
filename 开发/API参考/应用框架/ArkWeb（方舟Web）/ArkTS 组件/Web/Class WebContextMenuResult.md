# Class (WebContextMenuResult)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuresult
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

实现长按页面元素或鼠标右键弹出来的菜单所执行的响应事件。示例代码参考[onContextMenuShow事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontextmenushow9)。

> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 9开始支持。 示例效果请以真机运行为准。



#### constructor9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()

WebContextMenuResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core



#### closeContextMenu9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

closeContextMenu(): void

不执行WebContextMenuResult其他接口操作时，需要调用此接口关闭菜单。

**系统能力：** SystemCapability.Web.Webview.Core



#### copyImage9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyImage(): void

当WebContextMenuParam包含图片内容时，用于复制该图片。从API version 24开始支持对canvas图片进行复制。

**系统能力：** SystemCapability.Web.Webview.Core



#### copy9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copy(): void

执行复制文本操作。

**系统能力：** SystemCapability.Web.Webview.Core



#### paste9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

paste(): void

执行粘贴操作。

> [!NOTE]
> 需要配置权限： ohos.permission.READ_PASTEBOARD 。


**系统能力：** SystemCapability.Web.Webview.Core



#### cut9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

cut(): void

执行剪切操作。

**系统能力：** SystemCapability.Web.Webview.Core



#### selectAll9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

selectAll(): void

执行全选操作。

**系统能力：** SystemCapability.Web.Webview.Core



#### undo20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

undo(): void

执行撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core



#### redo20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

redo(): void

执行重做操作，即取消用户上一次的撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core



#### pasteAndMatchStyle20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

pasteAndMatchStyle(): void

执行与此上下文菜单相关的粘贴操作，粘贴的内容会匹配目标格式，以纯文本形式呈现。

> [!NOTE]
> 需要配置权限： ohos.permission.READ_PASTEBOARD 。


**系统能力：** SystemCapability.Web.Webview.Core



#### requestPasswordAutoFill23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

requestPasswordAutoFill(): void

请求密码保险箱中的用户名或密码数据自动填充到当前获得焦点的输入框中。

**系统能力：** SystemCapability.Web.Webview.Core



#### saveImage24+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

saveImage(): void

保存上下文菜单相关的图片，调用后将触发下载流程。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core
