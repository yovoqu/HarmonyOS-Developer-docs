# Worker和宿主线程的即时消息通信

更新时间：2026-04-30 09:02:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-communicates-with-mainthread

在ArkTS中，Worker相对于Taskpool存在一定的差异性，有数量限制但是可以长时间存在。一个[Worker](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction)中可能会执行多个不同的任务，每个任务的执行时长或返回结果可能都不同，宿主线程需要根据情况调用Worker中的不同方法，Worker则需要及时地将结果返回给宿主线程。

 下面以Worker响应"hello world"请求为例说明。


 在示例代码中，Worker接收宿主线程的消息，并处理后将结果返回给宿主线程。实现了宿主线程与Worker之间的即时通信，使宿主线程能够方便地使用Worker的运行结果。
