# Class (WebResourceRequest)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourcerequest
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Web组件获取资源请求对象。示例代码参考[onErrorReceive事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onerrorreceive)。
 
> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 8开始支持。 示例效果请以真机运行为准。

  

##### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
WebResourceRequest的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

##### getRequestHeader

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getRequestHeader(): Array&lt;Header&gt;
 
获取资源请求头信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Array&lt;Header&gt; | 返回资源请求头信息。 |
 
 
  

##### getRequestUrl

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getRequestUrl(): string
 
获取资源请求的URL信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 返回资源请求的URL信息。 |
 
 
  

##### isMainFrame

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isMainFrame(): boolean
 
判断资源请求是否为主frame。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源请求是否为主frame。 true表示返回资源请求为主frame，false表示返回资源请求不为主frame。 |
 
 
  

##### isRedirect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isRedirect(): boolean
 
判断资源请求是否被服务端重定向。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源请求是否被服务端重定向。 true表示返回资源请求被服务端重定向，false表示返回资源请求未被服务端重定向。 |
 
 
  

##### isRequestGesture

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isRequestGesture(): boolean
 
获取资源请求是否与手势（如点击）相关联。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| boolean | 返回资源请求是否与手势（如点击）相关联。 true表示返回资源请求与手势（如点击）相关联，false表示返回资源请求与手势（如点击）不相关联。 |
 
 
  

##### getRequestMethod9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getRequestMethod(): string
 
获取请求方法。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 返回请求方法。 |
