# ArkTS

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：LightWeightSet； API声明：equal(obj: Object): boolean; 差异内容：NA | 类名：LightWeightSet； API声明：equal(obj: Object): boolean; 差异内容：12 | api/@ohos.util.LightWeightSet.d.ts |
| 错误码变更 | 类名：SequenceRunner； API声明：execute(task: Task): Promise<Object>; 差异内容：10200003,10200006,10200025,10200051,401 | 类名：SequenceRunner； API声明：execute(task: Task): Promise<Object>; 差异内容：10200006,10200025,10200051,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool； API声明：function execute(func: Function, ...args: Object[]): Promise<Object>; 差异内容：10200003,10200006,10200014,401 | 类名：taskpool； API声明：function execute(func: Function, ...args: Object[]): Promise<Object>; 差异内容：10200006,10200014,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool； API声明：function execute(task: Task, priority?: Priority): Promise<Object>; 差异内容：10200003,10200006,10200014,10200051,401 | 类名：taskpool； API声明：function execute(task: Task, priority?: Priority): Promise<Object>; 差异内容：10200006,10200014,10200051,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool； API声明：function executePeriodically(period: number, task: Task, priority?: Priority): void; 差异内容：10200003,10200006,10200014,10200028,10200050,401 | 类名：taskpool； API声明：function executePeriodically(period: number, task: Task, priority?: Priority): void; 差异内容：10200006,10200014,10200028,10200050,401 | api/@ohos.taskpool.d.ts |
