# Class (BackForwardCacheSupportedFeatures)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kts-apis-webview-backforwardcachesupportedfeatures
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

选择性允许使用以下特性的页面进入前进后退缓存。完整示例代码参考[enableBackForwardCache](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#enablebackforwardcache12)。


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力：** SystemCapability.Web.Webview.Core


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nativeEmbed12+ | boolean | 否 | 否 | 是否允许使用同层渲染的页面进入前进后退缓存。 如果设置为允许，需要维护为同层渲染元素创建的系统控件的生命周期，避免造成泄漏。 true：允许使用同层渲染的页面进入前进后退缓存，false：不允许使用同层渲染的页面进入前进后退缓存。 默认值：false。 |
| mediaTakeOver12+ | boolean | 否 | 否 | 是否允许使用视频托管的页面进入前进后退缓存。 如果设置为允许，需要维护为视频元素创建的系统控件的生命周期，避免造成泄漏。 true：允许使用视频托管的页面进入前进后退缓存，false：不允许使用视频托管的页面进入前进后退缓存。 默认值：false。 |


## constructor12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

BackForwardCacheSupportedFeatures的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core
