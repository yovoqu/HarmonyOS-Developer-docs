# ArkTS的对象数据与Native的对象数据如何绑定，相互持有对象数据时内存如何管理

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-28

在ArkTS侧调用Native侧声明的构造函数创建对象，Native侧解析构造函数参数并返回构造的对象到ArkTS侧。通过napi_wrap绑定ArkTS对象和Native对象时，可以在napi_wrap()最后一个参数中传入nullptr，此时创建的napi_ref是弱引用，由系统管理，不需要用户手动释放。若napi_wrap()需要接收创建的napi_ref，最后一个参数不为nullptr，返回的napi_ref是强引用，需要用户调用napi_remove_wrap()手动释放，否则会内存泄漏。

参考链接

Native与ArkTS对象绑定
