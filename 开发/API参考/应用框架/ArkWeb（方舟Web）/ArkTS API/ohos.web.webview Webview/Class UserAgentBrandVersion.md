# Class (UserAgentBrandVersion)

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-useragentbrandversion
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

UserAgentBrandVersion是ArkWeb框架中用于配置User-Agent客户端提示信息中品牌名称和版本号的数据类，配合[UserAgentMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-useragentmetadata)使用。在User-Agent Client Hints机制中，浏览器通过Sec-CH-UA-Full-Version-List等请求标头向服务器报告品牌和版本信息，UserAgentBrandVersion用于定义其中的单个品牌条目。
 
UserAgentBrandVersion提供品牌名称和版本号的设置与获取方法：setBrand/getBrand用于设置和获取品牌名称（如"Chromium"、"ArkWeb"等），setMajorVersion/getMajorVersion用于设置和获取主版本号（如"126"），setFullVersion/getFullVersion用于设置和获取完整版本号（如"126.0.0.0"）。应用可通过修改这些值来定制Web组件向服务器报告的浏览器身份信息。
 
> [!NOTE]
> 本模块首批接口从API version 24开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 24开始支持。 示例效果请以真机运行为准。

  

#### setBrand

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setBrand(brand: string): void
 
设置品牌名称。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brand | string | 是 | 品牌名称，不能为空字符串。 |
 
 
**示例：**
 
完整示例代码参考[setUserAgentClientHintsEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setuseragentclienthintsenabled24)。
 
  

#### getBrand

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getBrand(): string
 
获取品牌名称。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 品牌名称。 |
 
 
**示例：**
 
完整示例代码参考[setUserAgentClientHintsEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setuseragentclienthintsenabled24)。
 
  

#### setMajorVersion

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setMajorVersion(majorVersion: string): void
 
设置主版本号。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| majorVersion | string | 是 | 主版本号，不能为空字符串。 |
 
 
**示例：**
 
完整示例代码参考[setUserAgentClientHintsEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setuseragentclienthintsenabled24)。
 
  

#### getMajorVersion

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMajorVersion(): string
 
获取主版本号。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 主版本号。 |
 
 
**示例：**
 
完整示例代码参考[setUserAgentClientHintsEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setuseragentclienthintsenabled24)。
 
  

#### setFullVersion

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setFullVersion(fullVersion: string): void
 
设置完整版本号。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullVersion | string | 是 | 完整版本号，不能为空字符串。 |
 
 
**示例：**
 
完整示例代码参考[setUserAgentClientHintsEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setuseragentclienthintsenabled24)。
 
  

#### getFullVersion

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getFullVersion(): string
 
获取完整版本号。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 完整版本号。 |
 
 
**示例：**
 
完整示例代码参考[setUserAgentClientHintsEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setuseragentclienthintsenabled24)。
