# ArkTS

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：taskpool； API声明：function execute<A extends Array&lt;Object&gt;, R>(func: (...args: A) => R \| Promise&lt;R&gt;, ...args: A): Promise&lt;R&gt;; 差异内容：function execute<A extends Array&lt;Object&gt;, R>(func: (...args: A) => R \| Promise&lt;R&gt;, ...args: A): Promise&lt;R&gt;; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool； API声明：function execute<A extends Array&lt;Object&gt;, R>(task: GenericsTask<A, R>, priority?: Priority): Promise&lt;R&gt;; 差异内容：function execute<A extends Array&lt;Object&gt;, R>(task: GenericsTask<A, R>, priority?: Priority): Promise&lt;R&gt;; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool； API声明：function executeDelayed<A extends Array&lt;Object&gt;, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise&lt;R&gt;; 差异内容：function executeDelayed<A extends Array&lt;Object&gt;, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise&lt;R&gt;; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool； API声明：function executePeriodically<A extends Array&lt;Object&gt;, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void; 差异内容：function executePeriodically<A extends Array&lt;Object&gt;, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool； API声明： class GenericsTask 差异内容： class GenericsTask | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：ParseReturnType； API声明：MAP = 1 差异内容：MAP = 1 | arkts/@arkts.utils.d.ets |
| 删除API | 类名：worker； API声明： class RestrictedWorker 差异内容： class RestrictedWorker | NA | api/@ohos.worker.d.ts |
