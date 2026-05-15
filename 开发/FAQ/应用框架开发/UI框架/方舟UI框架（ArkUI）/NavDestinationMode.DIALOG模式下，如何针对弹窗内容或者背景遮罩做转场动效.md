# NavDestinationMode.DIALOG模式下，如何针对弹窗内容或者背景遮罩做转场动效

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-417

问题背景

开发者对默认dialog动画不满意或需自定义转场动画。

解决措施

- 如对默认dialog动画不满意，开发者可以为NavDestination页面设置[systemTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#systemtransition14)属性为SLIDE_RIGHT（从右侧划入）、SLIDE_BOTTOM（从底部划入）等转场效果。
- 如需自定义动画可以为NavDestination页面设置[customTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#customtransition15)属性。


参考链接

示例2（设置NavDestination自定义转场）

示例3（设置指定的NavDestination系统转场）
