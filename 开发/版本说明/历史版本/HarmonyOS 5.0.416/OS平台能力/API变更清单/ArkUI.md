# ArkUI

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-504

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：UIContext； API声明：getTextMenuController(): TextMenuController; 差异内容：getTextMenuController(): TextMenuController; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global； API声明： export class TextMenuController 差异内容： export class TextMenuController | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：TextMenuController； API声明：setMenuOptions(options: TextMenuOptions): void; 差异内容：setMenuOptions(options: TextMenuOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：display； API声明：function createVirtualScreen(config: VirtualScreenConfig): Promise<number>; 差异内容：function createVirtualScreen(config: VirtualScreenConfig): Promise<number>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display； API声明：function destroyVirtualScreen(screenId: number): Promise<void>; 差异内容：function destroyVirtualScreen(screenId: number): Promise<void>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display； API声明：function setVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>; 差异内容：function setVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display； API声明：function makeUnique(screenId: number): Promise<void>; 差异内容：function makeUnique(screenId: number): Promise<void>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display； API声明： interface VirtualScreenConfig 差异内容： interface VirtualScreenConfig | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig； API声明：name: string; 差异内容：name: string; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig； API声明：width: number; 差异内容：width: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig； API声明：height: number; 差异内容：height: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig； API声明：density: number; 差异内容：density: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig； API声明：surfaceId: string; 差异内容：surfaceId: string; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum TextMenuShowMode 差异内容： declare enum TextMenuShowMode | component/text_common.d.ts |
| 新增API | NA | 类名：TextMenuShowMode； API声明：DEFAULT = 0 差异内容：DEFAULT = 0 | component/text_common.d.ts |
| 新增API | NA | 类名：TextMenuShowMode； API声明：PREFER_WINDOW = 1 差异内容：PREFER_WINDOW = 1 | component/text_common.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface TextMenuOptions 差异内容： declare interface TextMenuOptions | component/text_common.d.ts |
| 新增API | NA | 类名：TextMenuOptions； API声明：showMode?: TextMenuShowMode; 差异内容：showMode?: TextMenuShowMode; | component/text_common.d.ts |
