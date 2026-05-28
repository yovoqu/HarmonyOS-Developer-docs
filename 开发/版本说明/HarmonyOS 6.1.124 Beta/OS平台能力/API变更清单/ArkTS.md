# ArkTS

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：taskpool； API声明：function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>; 差异内容：10200006,401 | 类名：taskpool； API声明：function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>; 差异内容：10200006,10200059 | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool； API声明：interface Configs 差异内容：interface Configs | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：Configs； API声明：priority?: Priority; 差异内容：priority?: Priority; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：Configs； API声明：timeout?: number; 差异内容：timeout?: number; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：ArkTSVM； API声明：static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>; 差异内容：static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：ArkTSVM； API声明：static onVMHeapMemoryPressure(callback: Callback&lt;string&gt;, heapMemoryThreshold: HeapMemoryThreshold): boolean; 差异内容：static onVMHeapMemoryPressure(callback: Callback&lt;string&gt;, heapMemoryThreshold: HeapMemoryThreshold): boolean; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：ArkTSVM； API声明：static offVMHeapMemoryPressure(): void; 差异内容：static offVMHeapMemoryPressure(): void; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：util； API声明：interface HeapMemoryThreshold 差异内容：interface HeapMemoryThreshold | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryThreshold； API声明：localHeapThreshold?: number; 差异内容：localHeapThreshold?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryThreshold； API声明：sharedHeapThreshold?: number; 差异内容：sharedHeapThreshold?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryThreshold； API声明：processHeapThreshold?: number; 差异内容：processHeapThreshold?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：util； API声明：interface HeapMemoryInfo 差异内容：interface HeapMemoryInfo | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo； API声明：threadId?: number; 差异内容：threadId?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo； API声明：threadName?: string; 差异内容：threadName?: string; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo； API声明：heapType: string; 差异内容：heapType: string; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo； API声明：heapObjectSize: number; 差异内容：heapObjectSize: number; | api/@ohos.util.d.ts |
