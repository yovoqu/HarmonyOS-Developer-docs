# TaskPool指定任务并发度场景

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-async-task-guide

TaskPool支持使用异步队列来控制任务的并发度，能有效避免资源过载，减少任务阻塞，适用于网络请求、视频流处理和数据库操作等场景。

此处提供使用TaskPool创建[异步队列](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#asyncrunner18)的开发指导，以相机预览流采集数据处理的功能为例。

由于处理过程是一个频繁且耗时的任务，当相机采集速度过快时，将丢弃之前的采集数据，仅保留最新的一帧数据进行处理。
