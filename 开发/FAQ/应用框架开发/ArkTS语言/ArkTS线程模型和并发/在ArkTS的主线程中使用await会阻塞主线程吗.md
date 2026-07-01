# 在ArkTS的主线程中使用await会堵塞主线程吗

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-43

await会挂起当前异步任务，等待条件满足后唤醒执行，主线程可处理其他任务。
