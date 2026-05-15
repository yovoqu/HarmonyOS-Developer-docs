# Navigation中pushPathByName与pushDestinationByName的区别

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-264

pushDestinationByName绑定上下文对象，调用时验证上下文是否一致，而pushPathByName不进行验证。

不同的窗口，运行的UIContext不同。在单窗口场景下使用时，两者仅返回值存在差异；跨窗口使用时需注意UIContext的匹配性。
