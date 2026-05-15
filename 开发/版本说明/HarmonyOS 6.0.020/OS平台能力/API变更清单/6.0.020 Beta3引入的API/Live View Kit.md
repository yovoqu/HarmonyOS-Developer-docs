# Live View Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-liveviewkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：liveViewManager； API声明：export enum BackgroundType 差异内容：export enum BackgroundType | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：BackgroundType； API声明：SYS_BACKGROUND_UNDEFINED = 0 差异内容：SYS_BACKGROUND_UNDEFINED = 0 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：BackgroundType； API声明：SYS_BACKGROUND_FLIGHT_MOON = 100 差异内容：SYS_BACKGROUND_FLIGHT_MOON = 100 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：BackgroundType； API声明：SYS_BACKGROUND_FLIGHT_SUNSET = 101 差异内容：SYS_BACKGROUND_FLIGHT_SUNSET = 101 | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：PrimaryData； API声明：backgroundType?: BackgroundType; 差异内容：backgroundType?: BackgroundType; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：CapsuleData； API声明：tailIcon?: string \| image.PixelMap; 差异内容：tailIcon?: string \| image.PixelMap; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：CapsuleData； API声明：isTailIconDisplayed?: boolean; 差异内容：isTailIconDisplayed?: boolean; | api/@hms.core.liveview.liveViewManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：ProgressCapsule； API声明：content?: string; 差异内容：content?: string; | api/@hms.core.liveview.liveViewManager.d.ts |
