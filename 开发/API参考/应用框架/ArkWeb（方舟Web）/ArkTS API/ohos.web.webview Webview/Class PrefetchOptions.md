# Class (PrefetchOptions)

更新时间：2026-03-09 07:25:19

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-prefetchoptions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

用来自定义网页的预取行为，包括是否忽略响应头中的Cache-Control: no-store和设置两次预取间的最小时间间隔。


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力：** SystemCapability.Web.Webview.Core


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minTimeBetweenPrefetchesMs21+ | number | 否 | 否 | 设置两次网页预取的最小时间间隔。 每次预取时会计算和上次预取的间隔时间，若小于设置值，则取消本次预取。 默认为500，最大值为500。 设置为负数时，默认为0。 单位: ms |
| ignoreCacheControlNoStore21+ | boolean | 否 | 否 | 设置是否忽略响应头中的Cache-Control: no-store。 默认值：false  设置为true时，会忽略响应头中的Cache-Control: no-store，为false时不会。 |


## constructor21+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

PrefetchOptions的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core
