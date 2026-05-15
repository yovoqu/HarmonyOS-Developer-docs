# ArkUI

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-b061

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：uiObserver； API声明： export enum TabContentState 差异内容： export enum TabContentState | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentState； API声明：ON_SHOW = 0 差异内容：ON_SHOW = 0 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentState； API声明：ON_HIDE = 1 差异内容：ON_HIDE = 1 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver； API声明： export interface TabContentInfo 差异内容： export interface TabContentInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentInfo； API声明：tabContentId: string; 差异内容：tabContentId: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentInfo； API声明：tabContentUniqueId: number; 差异内容：tabContentUniqueId: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentInfo； API声明：state: TabContentState; 差异内容：state: TabContentState; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentInfo； API声明：index: number; 差异内容：index: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentInfo； API声明：id: string; 差异内容：id: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TabContentInfo； API声明：uniqueId: number; 差异内容：uniqueId: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver； API声明：export function on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void; 差异内容：export function on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver； API声明：export function on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void; 差异内容：export function on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver； API声明：export function off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void; 差异内容：export function off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver； API声明：export function off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void; 差异内容：export function off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：global； API声明： export declare class UIUtils 差异内容： export declare class UIUtils | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：UIUtils； API声明：static getTarget<T extends object>(source: T): T; 差异内容：static getTarget<T extends object>(source: T): T; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：UIObserver； API声明：on(type: 'tabContentUpdate', options: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void; 差异内容：on(type: 'tabContentUpdate', options: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver； API声明：on(type: 'tabContentUpdate', callback: Callback<observer.TabContentInfo>): void; 差异内容：on(type: 'tabContentUpdate', callback: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver； API声明：off(type: 'tabContentUpdate', options: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void; 差异内容：off(type: 'tabContentUpdate', options: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver； API声明：off(type: 'tabContentUpdate', callback?: Callback<observer.TabContentInfo>): void; 差异内容：off(type: 'tabContentUpdate', callback?: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：BaseEvent； API声明：getModifierKeyState?(keys: Array<string>): boolean; 差异内容：getModifierKeyState?(keys: Array<string>): boolean; | component/common.d.ts |
| 新增API | NA | 类名：BaseEvent； API声明：deviceId?: number; 差异内容：deviceId?: number; | component/common.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface AccessibilityHoverEvent 差异内容： declare interface AccessibilityHoverEvent | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityHoverEvent； API声明：type: AccessibilityHoverType; 差异内容：type: AccessibilityHoverType; | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityHoverEvent； API声明：x: number; 差异内容：x: number; | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityHoverEvent； API声明：y: number; 差异内容：y: number; | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityHoverEvent； API声明：displayX: number; 差异内容：displayX: number; | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityHoverEvent； API声明：displayY: number; 差异内容：displayY: number; | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityHoverEvent； API声明：windowX: number; 差异内容：windowX: number; | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityHoverEvent； API声明：windowY: number; 差异内容：windowY: number; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent； API声明：getModifierKeyState?(keys: Array<string>): boolean; 差异内容：getModifierKeyState?(keys: Array<string>): boolean; | component/common.d.ts |
| 新增API | NA | 类名：KeyEvent； API声明：getModifierKeyState?(keys: Array<string>): boolean; 差异内容：getModifierKeyState?(keys: Array<string>): boolean; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod； API声明：onAccessibilityHover(callback: AccessibilityCallback): T; 差异内容：onAccessibilityHover(callback: AccessibilityCallback): T; | component/common.d.ts |
| 新增API | NA | 类名：global； API声明：declare type AccessibilityCallback = (isHover: boolean, event: AccessibilityHoverEvent) => void; 差异内容：declare type AccessibilityCallback = (isHover: boolean, event: AccessibilityHoverEvent) => void; | component/common.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum AccessibilityHoverType 差异内容： declare enum AccessibilityHoverType | component/enums.d.ts |
| 新增API | NA | 类名：AccessibilityHoverType； API声明：HOVER_ENTER = 0 差异内容：HOVER_ENTER = 0 | component/enums.d.ts |
| 新增API | NA | 类名：AccessibilityHoverType； API声明：HOVER_MOVE = 1 差异内容：HOVER_MOVE = 1 | component/enums.d.ts |
| 新增API | NA | 类名：AccessibilityHoverType； API声明：HOVER_EXIT = 2 差异内容：HOVER_EXIT = 2 | component/enums.d.ts |
| 新增API | NA | 类名：AccessibilityHoverType； API声明：HOVER_CANCEL = 3 差异内容：HOVER_CANCEL = 3 | component/enums.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum GridItemAlignment 差异内容： declare enum GridItemAlignment | component/grid.d.ts |
| 新增API | NA | 类名：GridItemAlignment； API声明：DEFAULT = 0 差异内容：DEFAULT = 0 | component/grid.d.ts |
| 新增API | NA | 类名：GridItemAlignment； API声明：STRETCH = 1 差异内容：STRETCH = 1 | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute； API声明：alignItems(alignment: Optional<GridItemAlignment>): GridAttribute; 差异内容：alignItems(alignment: Optional<GridItemAlignment>): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：global； API声明：declare type DrawingLattice = import('../api/@ohos.graphics.drawing').default.Lattice; 差异内容：declare type DrawingLattice = import('../api/@ohos.graphics.drawing').default.Lattice; | component/image.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum ImageContent 差异内容： declare enum ImageContent | component/image.d.ts |
| 新增API | NA | 类名：ImageContent； API声明：EMPTY = 0 差异内容：EMPTY = 0 | component/image.d.ts |
| 新增API | NA | 类名：ResizableOptions； API声明：lattice?: DrawingLattice; 差异内容：lattice?: DrawingLattice; | component/image.d.ts |
| 新增API | NA | 类名：NavPathStack； API声明：removeByNavDestinationId(navDestinationId: string): boolean; 差异内容：removeByNavDestinationId(navDestinationId: string): boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：RefreshOptions； API声明：refreshingContent?: ComponentContent; 差异内容：refreshingContent?: ComponentContent; | component/refresh.d.ts |
