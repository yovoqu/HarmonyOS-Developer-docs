# 在onInterceptRequest接口中，如何异步处理响应数据

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-82

可以使用setResponseIsReady设置资源响应数据是否已经就绪。例如，在异步获取数据后，需调用`setResponseIsReady(true)`通知系统响应数据已准备就绪，具体可参考onInterceptRequest示例代码。
