# IME Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：TextInputType； API声明：SCREEN_LOCK_PASSWORD 差异内容：SCREEN_LOCK_PASSWORD | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType； API声明：USER_NAME 差异内容：USER_NAME | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType； API声明：NEW_PASSWORD 差异内容：NEW_PASSWORD | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType； API声明：NUMBER_DECIMAL 差异内容：NUMBER_DECIMAL | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：TextInputType； API声明：ONE_TIME_CODE 差异内容：ONE_TIME_CODE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod； API声明：export enum CapitalizeMode 差异内容：export enum CapitalizeMode | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：SENTENCES 差异内容：SENTENCES | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：WORDS 差异内容：WORDS | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：CHARACTERS 差异内容：CHARACTERS | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明：const PATTERN_USER_NAME: number = 10; 差异内容：const PATTERN_USER_NAME: number = 10; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明：const PATTERN_NEW_PASSWORD: number = 11; 差异内容：const PATTERN_NEW_PASSWORD: number = 11; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明：const PATTERN_NUMBER_DECIMAL: number = 12; 差异内容：const PATTERN_NUMBER_DECIMAL: number = 12; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明：const PATTERN_ONE_TIME_CODE: number = 13; 差异内容：const PATTERN_ONE_TIME_CODE: number = 13; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明：export enum GradientMode 差异内容：export enum GradientMode | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：GradientMode； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：GradientMode； API声明：LINEAR_GRADIENT = 1 差异内容：LINEAR_GRADIENT = 1 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明：interface ImmersiveEffect 差异内容：interface ImmersiveEffect | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ImmersiveEffect； API声明：gradientHeight: number; 差异内容：gradientHeight: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ImmersiveEffect； API声明：gradientMode: GradientMode; 差异内容：gradientMode: GradientMode; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明：export enum CapitalizeMode 差异内容：export enum CapitalizeMode | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：SENTENCES 差异内容：SENTENCES | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：WORDS 差异内容：WORDS | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：CapitalizeMode； API声明：CHARACTERS 差异内容：CHARACTERS | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodController； API声明：discardTypingText(): Promise<void>; 差异内容：discardTypingText(): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodAbility； API声明：on(type: 'discardTypingText', callback: Callback<void>): void; 差异内容：on(type: 'discardTypingText', callback: Callback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodAbility； API声明：off(type: 'discardTypingText', callback?: Callback<void>): void; 差异内容：off(type: 'discardTypingText', callback?: Callback<void>): void; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：Panel； API声明：setImmersiveEffect(effect: ImmersiveEffect): void; 差异内容：setImmersiveEffect(effect: ImmersiveEffect): void; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodProperty； API声明：readonly enabledState?: EnabledState; 差异内容：readonly enabledState?: EnabledState; | api/@ohos.inputMethod.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：InputAttribute； API声明：placeholder?: string; 差异内容：placeholder?: string; | api/@ohos.inputMethod.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：InputAttribute； API声明：abilityName?: string; 差异内容：abilityName?: string; | api/@ohos.inputMethod.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：TextConfig； API声明：newEditBox?: boolean; 差异内容：newEditBox?: boolean; | api/@ohos.inputMethod.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：TextConfig； API声明：capitalizeMode?: CapitalizeMode; 差异内容：capitalizeMode?: CapitalizeMode; | api/@ohos.inputMethod.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：EditorAttribute； API声明：readonly placeholder?: string; 差异内容：readonly placeholder?: string; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：EditorAttribute； API声明：readonly abilityName?: string; 差异内容：readonly abilityName?: string; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：EditorAttribute； API声明：readonly capitalizeMode?: CapitalizeMode; 差异内容：readonly capitalizeMode?: CapitalizeMode; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：EditorAttribute； API声明：readonly gradientMode?: GradientMode; 差异内容：readonly gradientMode?: GradientMode; | api/@ohos.inputMethodEngine.d.ts |
