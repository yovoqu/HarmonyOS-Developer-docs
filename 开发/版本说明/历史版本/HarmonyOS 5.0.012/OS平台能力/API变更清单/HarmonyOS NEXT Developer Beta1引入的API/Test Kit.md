# Test Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-testkit-hdc

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：abilityDelegatorRegistry； API声明：function getAbilityDelegator(): AbilityDelegator; 差异内容：NA | 类名：abilityDelegatorRegistry； API声明：function getAbilityDelegator(): AbilityDelegator; 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：abilityDelegatorRegistry； API声明：function getArguments(): AbilityDelegatorArgs; 差异内容：NA | 类名：abilityDelegatorRegistry； API声明：function getArguments(): AbilityDelegatorArgs; 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：abilityDelegatorRegistry； API声明： export enum AbilityLifecycleState 差异内容：NA | 类名：abilityDelegatorRegistry； API声明： export enum AbilityLifecycleState 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState； API声明：UNINITIALIZED 差异内容：NA | 类名：AbilityLifecycleState； API声明：UNINITIALIZED 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState； API声明：CREATE 差异内容：NA | 类名：AbilityLifecycleState； API声明：CREATE 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState； API声明：FOREGROUND 差异内容：NA | 类名：AbilityLifecycleState； API声明：FOREGROUND 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState； API声明：BACKGROUND 差异内容：NA | 类名：AbilityLifecycleState； API声明：BACKGROUND 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：AbilityLifecycleState； API声明：DESTROY 差异内容：NA | 类名：AbilityLifecycleState； API声明：DESTROY 差异内容：9 | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| API废弃版本变更 | 类名：WindowFilter； API声明：actived?: boolean; 差异内容：NA | 类名：WindowFilter； API声明：actived?: boolean; 差异内容：11 | api/@ohos.UiTest.d.ts |
| API废弃版本变更 | 类名：UiWindow； API声明：isActived(): Promise&lt;boolean&gt;; 差异内容：NA | 类名：UiWindow； API声明：isActived(): Promise&lt;boolean&gt;; 差异内容：11 | api/@ohos.UiTest.d.ts |
| 错误码变更 | 类名：UiDriver； API声明：assertComponentExist(by: By): Promise&lt;void&gt;; 差异内容：NA | 类名：UiDriver； API声明：assertComponentExist(by: By): Promise&lt;void&gt;; 差异内容：17000002,17000003,401 | api/@ohos.UiTest.d.ts |
| 权限变更 | 类名：global； API声明： declare namespace abilityDelegatorRegistry 差异内容：N/A | 类名：global； API声明： declare namespace abilityDelegatorRegistry 差异内容：NA | api/@ohos.application.abilityDelegatorRegistry.d.ts |
| 权限变更 | 类名：global； API声明： export interface TestRunner 差异内容：N/A | 类名：global； API声明： export interface TestRunner 差异内容：NA | api/@ohos.application.testRunner.d.ts |
| 新增API | NA | 类名：Driver； API声明：fling(direction: UiDirection, speed: number): Promise&lt;void&gt;; 差异内容：fling(direction: UiDirection, speed: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowFilter； API声明：active?: boolean; 差异内容：active?: boolean; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface UIElementInfo 差异内容： declare interface UIElementInfo | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo； API声明：readonly bundleName: string; 差异内容：readonly bundleName: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo； API声明：readonly type: string; 差异内容：readonly type: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo； API声明：readonly text: string; 差异内容：readonly text: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface UIEventObserver 差异内容： declare interface UIEventObserver | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIEventObserver； API声明：once(type: 'toastShow', callback: Callback&lt;UIElementInfo&gt;): void; 差异内容：once(type: 'toastShow', callback: Callback&lt;UIElementInfo&gt;): void; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIEventObserver； API声明：once(type: 'dialogShow', callback: Callback&lt;UIElementInfo&gt;): void; 差异内容：once(type: 'dialogShow', callback: Callback&lt;UIElementInfo&gt;): void; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum UiDirection 差异内容： declare enum UiDirection | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection； API声明：LEFT = 0 差异内容：LEFT = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection； API声明：RIGHT = 1 差异内容：RIGHT = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection； API声明：UP = 2 差异内容：UP = 2 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiDirection； API声明：DOWN = 3 差异内容：DOWN = 3 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum MouseButton 差异内容： declare enum MouseButton | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：MouseButton； API声明：MOUSE_BUTTON_LEFT = 0 差异内容：MOUSE_BUTTON_LEFT = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：MouseButton； API声明：MOUSE_BUTTON_RIGHT = 1 差异内容：MOUSE_BUTTON_RIGHT = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：MouseButton； API声明：MOUSE_BUTTON_MIDDLE = 2 差异内容：MOUSE_BUTTON_MIDDLE = 2 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On； API声明：within(on: On): On; 差异内容：within(on: On): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On； API声明：inWindow(bundleName: string): On; 差异内容：inWindow(bundleName: string): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On； API声明：description(val: string, pattern?: MatchPattern): On; 差异内容：description(val: string, pattern?: MatchPattern): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Component； API声明：getDescription(): Promise&lt;string&gt;; 差异内容：getDescription(): Promise&lt;string&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise&lt;void&gt;; 差异内容：mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseMoveTo(p: Point): Promise&lt;void&gt;; 差异内容：mouseMoveTo(p: Point): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise&lt;void&gt;; 差异内容：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise&lt;void&gt;; 差异内容：mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：screenCapture(savePath: string, rect?: Rect): Promise&lt;boolean&gt;; 差异内容：screenCapture(savePath: string, rect?: Rect): Promise&lt;boolean&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：createUIEventObserver(): UIEventObserver; 差异内容：createUIEventObserver(): UIEventObserver; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise&lt;void&gt;; 差异内容：mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise&lt;void&gt;; 差异内容：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise&lt;void&gt;; 差异内容：mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：mouseDrag(from: Point, to: Point, speed?: number): Promise&lt;void&gt;; 差异内容：mouseDrag(from: Point, to: Point, speed?: number): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver； API声明：inputText(p: Point, text: string): Promise&lt;void&gt;; 差异内容：inputText(p: Point, text: string): Promise&lt;void&gt;; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UiWindow； API声明：isActive(): Promise&lt;boolean&gt;; 差异内容：isActive(): Promise&lt;boolean&gt;; | api/@ohos.UiTest.d.ts |
