# Class (ScreenCaptureHandler)

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ScreenCaptureHandler 是 Web 组件提供的屏幕捕获权限处理类，用于响应网页发起的屏幕捕获请求。该类允许开发者通过 grant 或 deny 方法控制是否授予网页屏幕捕获权限，并通过 getOrigin 方法获取请求来源信息，帮助开发者在保护用户隐私的同时，灵活处理网页的屏幕捕获访问需求。示例代码参考[onScreenCaptureRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onscreencapturerequest10)事件。
 
> [!NOTE]
> 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 10开始支持。 示例效果请以真机运行为准。

  

#### constructor10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
ScreenCaptureHandler的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

#### deny10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

deny(): void
 
拒绝网页所请求的屏幕捕获操作。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

#### getOrigin10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getOrigin(): string
 
获取网页来源。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 当前请求权限网页的来源。 |
 
 
  

#### grant10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

grant(config: ScreenCaptureConfig): void
 
对网页访问的屏幕捕获操作进行授权。
 
> [!NOTE]
> 需要配置权限：ohos.permission.MICROPHONE。

 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | ScreenCaptureConfig | 是 | 屏幕捕获配置。 |
