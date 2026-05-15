# Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-452

问题分析

aboutToAppear()被调用的时候Tabs组件尚未完成渲染，这会导致preloadItems方法预加载不存在的索引。

解决方案

TabContent中的onWillShow()方法能够实现预加载功能，但是Tabs每次切换时都会触发onWillShow()回调，需要做节流处理。
