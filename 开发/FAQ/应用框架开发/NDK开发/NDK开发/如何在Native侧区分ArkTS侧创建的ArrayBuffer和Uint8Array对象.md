# 如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-13

问题详情

ArkTS层创建的ArrayBuffer和Uint8Array对象在Native层无法正确区分。

解决措施

1. 使用[napi_is_arraybuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-arraybuffer#napi_is_arraybuffer)接口判断数据是否为ArrayBuffer类型，若类型符合则结果为true。
2. 使用[napi_is_typedarray](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-array#napi_is_typedarray)接口判断Uint8Array类型数据，若类型符合则结果为true。
