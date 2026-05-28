# Class (ProxyRule)

更新时间：2026-03-09 07:25:19

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyrule
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

[insertProxyRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyconfig#insertproxyrule15)中使用的代理规则。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 15开始支持。 示例效果请以真机运行为准。

  

#### getSchemeFilter15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getSchemeFilter(): ProxySchemeFilter
 
获取代理规则中的ProxySchemeFilter信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| ProxySchemeFilter | 代理规则中的ProxySchemeFilter信息。 |
 
 
**示例：**
 
完整示例代码参考[removeProxyOverride](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxycontroller#removeproxyoverride15)。
 
  

#### getUrl15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getUrl(): string
 
获取代理规则中的代理的Url信息。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 代理规则中的代理的Url信息。 |
 
 
**示例：**
 
完整示例代码参考[removeProxyOverride](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxycontroller#removeproxyoverride15)。
