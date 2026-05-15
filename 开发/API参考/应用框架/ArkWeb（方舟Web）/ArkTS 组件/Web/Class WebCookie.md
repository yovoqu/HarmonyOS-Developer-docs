# Class (WebCookie)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcookie
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通过WebCookie可以控制Web组件中的cookie的各种行为，其中每个应用中的所有Web组件共享一个WebCookie。通过controller方法中的getCookieManager方法可以获取WebCookie对象，进行后续的cookie管理操作。


## constructor(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

WebCookie的构造函数。


> [!NOTE]
> 从API version 8开始支持，从API version 23开始废弃。且不再提供新的接口作为替代。

**系统能力：** SystemCapability.Web.Webview.Core


## setCookie(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setCookie()

设置cookie，该方法为同步方法。设置成功返回true，否则返回false。


> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用[setCookie9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#setcookiedeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core


## saveCookie(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

saveCookie()

将当前存在内存中的cookie同步到磁盘中，该方法为同步方法。


> [!NOTE]
> 从API version 8开始支持，从API version 9开始废弃，建议使用[saveCookieAsync9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#savecookieasync)代替。

**系统能力：** SystemCapability.Web.Webview.Core
