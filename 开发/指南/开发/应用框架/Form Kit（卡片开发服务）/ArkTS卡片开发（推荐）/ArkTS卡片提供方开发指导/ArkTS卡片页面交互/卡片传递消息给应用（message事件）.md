# 卡片传递消息给应用（message事件）

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-formextensionability

在卡片页面中可以通过[postCardAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-postcardaction#postcardaction-1)接口触发message事件拉起[FormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)，通过[onFormEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability#formextensionabilityonformevent)接口回调通知，以完成点击卡片控件后传递消息给应用的功能，然后由FormExtensionAbility刷新卡片内容，下面是这种刷新方式的简单示例。


> [!NOTE]
> 本文主要介绍动态卡片的事件开发。对于静态卡片，请参见FormLink。
