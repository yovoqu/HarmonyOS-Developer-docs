# 自定义Native Transferable对象的多线程操作场景

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-coerce-to-native-binding-object

在ArkTS应用开发中，有很多场景需要将ArkTS对象与Native对象进行绑定。ArkTS对象将数据写入Native对象，Native对象再将数据写入目的地。例如，将ArkTS对象中的数据写入C++数据库场景。

 Native Transferable对象有两种模式：共享模式和转移模式。本示例将详细说明如何实现这两种模式。
