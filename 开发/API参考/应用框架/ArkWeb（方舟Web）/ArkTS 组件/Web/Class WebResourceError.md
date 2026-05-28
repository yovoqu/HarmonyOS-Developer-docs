# Class (WebResourceError)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceerror
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Web组件资源管理错误信息对象。示例代码参考[onErrorReceive事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onerrorreceive)。
 
> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 8开始支持。 示例效果请以真机运行为准。

  

##### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
WebResourceError的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

##### getErrorCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getErrorCode(): number
 
获取加载资源的错误码。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 返回加载资源的错误码。错误码含义参考WebNetErrorList、HTTP协议状态码。 |
 
 
  

##### getErrorInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getErrorInfo(): string
 
获取加载资源的错误信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 返回加载资源的错误信息。 |
