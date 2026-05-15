# 多线程取消TaskPool任务场景

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-cancel-task

由于任务池[TaskPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool)的任务对象[Task](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#task)不支持跨线程传递，无法在子线程中直接取消任务。从 API version 18 开始，Task新增了[任务ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#属性)属性，支持通过任务ID在子线程中取消任务。开发者可将已创建任务的任务ID存储在[Sendable对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)中，需要取消任务时，通过Sendable对象在子线程中取消任务。详情可参考以下示例。
