# ArkUI瀑布流渲染场景

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-waterflow

此处提供使用任务池[TaskPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool)提升[WaterFlow瀑布流](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)渲染性能的开发指导。UI线程查询数据库数据，并将数据渲染到瀑布流组件，数据过大时会导致UI线程长时间等待，影响用户体验。因此，我们可以将数据查询操作放到子线程中，并通过TaskPool的接口返回数据给UI线程。

本示例说明以下场景：


- 模拟子线程[读取数据库数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/batch-database-operations-guide)并返回给UI线程。
- UI线程感知到数据更新，将子线程返回的数据渲染到瀑布流组件。
