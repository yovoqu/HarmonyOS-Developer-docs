# ArkTS

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：taskpool； API声明：function getTask(taskId: number, taskName?: string): Task \| undefined; 差异内容：function getTask(taskId: number, taskName?: string): Task \| undefined; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：util； API声明：interface AutoFinalizer 差异内容：interface AutoFinalizer | api/@ohos.util.d.ts |
| 新增API | NA | 类名：AutoFinalizer； API声明：onFinalization(heldValue: T): void; 差异内容：onFinalization(heldValue: T): void; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：util； API声明：class AutoFinalizerCleaner 差异内容：class AutoFinalizerCleaner | api/@ohos.util.d.ts |
| 新增API | NA | 类名：AutoFinalizerCleaner； API声明：static register&lt;T&gt;(obj: AutoFinalizer&lt;T&gt;, heldValue: T): void; 差异内容：static register&lt;T&gt;(obj: AutoFinalizer&lt;T&gt;, heldValue: T): void; | api/@ohos.util.d.ts |
