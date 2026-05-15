# 自定义Native Sendable对象的多线程操作场景

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-define-sendable-object

ArkTS支持开发者自定义Native Sendable对象，Sendable对象提供了并发实例间高效的通信能力，即引用传递，适用于开发者自定义大对象需要线程间通信的场景，例如子线程读取数据库数据并返回给宿主线程。

 本示例将详细说明如何使用自定义Native Sendable对象实现并发实例间数据共享。
