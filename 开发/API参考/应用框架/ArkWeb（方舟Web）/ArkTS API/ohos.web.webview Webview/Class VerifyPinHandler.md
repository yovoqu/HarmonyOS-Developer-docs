# Class (VerifyPinHandler)

更新时间：2026-04-13 09:29:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-verifypinhandler
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Web组件返回的PIN码认证用户处理功能对象。示例代码参考[onVerifyPin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onverifypin22)。
 
> [!NOTE]
> 该组件从API version 22开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 22开始支持。 示例效果请以真机运行为准。

  

##### constructor22+

constructor()
 
VerifyPinHandler的构造函数。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
  

##### confirm22+

confirm(result: PinVerifyResult): void
 
通知Web组件PIN码认证结果。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | PinVerifyResult | 是 | PIN码认证结果。 |
