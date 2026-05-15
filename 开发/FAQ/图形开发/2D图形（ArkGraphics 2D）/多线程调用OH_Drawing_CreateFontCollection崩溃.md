# 多线程调用OH_Drawing_CreateFontCollection崩溃

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-3

问题详情：

多线程调用OH_Drawing_TypographyCreate函数时，handler = OH_Drawing_CreateTypographyHandler(typoStyle, OH_Drawing_CreateFontCollection())会导致崩溃，而单线程调用则不会。

解决措施：

该接口不支持多线程并发，但可以在异步线程中调用。
