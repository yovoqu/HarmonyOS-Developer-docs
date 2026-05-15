# Class (MediaQuery)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供根据不同媒体类型定义不同的样式。


## matchMediaSync
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

matchMediaSync(condition: string): mediaQuery.MediaQueryListener

设置媒体查询的查询条件，并返回对应的监听句柄。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | string | 是 | 媒体事件的匹配条件，具体可参考[媒体查询语法规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query#语法规则)。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [mediaQuery.MediaQueryListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery#mediaquerylistener) | 媒体事件监听句柄，用于注册和去注册监听回调。 |


**示例：**

完整示例请参考[mediaquery示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery#示例)。
