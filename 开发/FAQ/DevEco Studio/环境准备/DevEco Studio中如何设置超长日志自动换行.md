# DevEco Studio中如何设置超长日志自动换行

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-15

启用Soft-Wrap功能以实现日志消息的自动换行。


![](assets/DevEco%20Studio中如何设置超长日志自动换行/file-20260515130002896-0.png)


日志单条打印的最大长度为4096个字符。建议在应用的日志框架中，对日志长度进行判断，若超过该长度则分段打印，以避免日志丢失。
