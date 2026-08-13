# Class (VerifyPinHandler)

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-verifypinhandler
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

VerifyPinHandler是Web组件中处理PIN码验证请求的类。当需要用户PIN码认证时，该处理器通过onVerifyPin事件回调提供给应用，允许应用响应PIN码验证结果。示例代码参考[onVerifyPin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onverifypin22)。
 
> [!NOTE]
> 该组件从API version 22开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 22开始支持。 示例效果请以真机运行为准。

  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
VerifyPinHandler的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

#### confirm

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

confirm(result: PinVerifyResult): void
 
通知Web组件PIN码认证结果。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | PinVerifyResult | 是 | PIN码认证结果。 |
