# TaskPool任务与宿主线程通信

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-communicates-with-mainthread

如果Task不仅需要返回最终执行结果，还需定时通知宿主线程状态和数据变化，或分段返回大量数据（如从数据库读取大量数据），可按以下方式实现。

 下面以多个图片加载任务结果实时返回为例说明。
