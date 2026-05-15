# JS Crash类问题优化建议

更新时间：2026-03-12 08:45:02

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-js-crash-opt

## 优化建议1：Source Maps归档保存


生产环境归档SourceMap便于后续源码还原，遇到JS Crash应先进行堆栈轨迹分析。


> [!NOTE]
> 编译时SourceMap的获取位置详见：[sourceMap归档位置介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section666114451518)。


## 优化建议2：崩溃预防机制


可使用errorManager注册错误观测器。注册后可以捕获到应用产生的JS Crash，应用崩溃时进程不会退出。详见errorManager使用指导。
