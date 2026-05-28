# Pen Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-penkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace stylusInteraction 差异内容：declare namespace stylusInteraction | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction； API声明：function on(type: 'squeeze', receiver: Callback&lt;SqueezeEvent&gt;): void; 差异内容：function on(type: 'squeeze', receiver: Callback&lt;SqueezeEvent&gt;): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction； API声明：function off(type: 'squeeze', receiver?: Callback&lt;SqueezeEvent&gt;): void; 差异内容：function off(type: 'squeeze', receiver?: Callback&lt;SqueezeEvent&gt;): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction； API声明：export interface SqueezeEvent 差异内容：export interface SqueezeEvent | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：SqueezeEvent； API声明：timestamp: number; 差异内容：timestamp: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction； API声明：function on(type: 'doubleTap', receiver: Callback&lt;DoubleTapEvent&gt;): void; 差异内容：function on(type: 'doubleTap', receiver: Callback&lt;DoubleTapEvent&gt;): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction； API声明：function off(type: 'doubleTap', receiver?: Callback&lt;DoubleTapEvent&gt;): void; 差异内容：function off(type: 'doubleTap', receiver?: Callback&lt;DoubleTapEvent&gt;): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction； API声明：export interface DoubleTapEvent 差异内容：export interface DoubleTapEvent | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：DoubleTapEvent； API声明：timestamp: number; 差异内容：timestamp: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.officeservice.stylusInteraction.d.ts 差异内容：Penkit | api/@hms.officeservice.stylusInteraction.d.ts |
