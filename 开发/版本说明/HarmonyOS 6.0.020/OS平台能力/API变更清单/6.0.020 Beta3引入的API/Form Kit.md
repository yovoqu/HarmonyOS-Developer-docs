# Form Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-formkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：FormDimension； API声明：Dimension_2_1 差异内容：NA | 类名：FormDimension； API声明：Dimension_2_1 差异内容：20 | api/@ohos.app.form.formInfo.d.ts |
| API废弃版本变更 | 类名：formProvider； API声明：function getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>; 差异内容：NA | 类名：formProvider； API声明：function getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>; 差异内容：20 | api/@ohos.app.form.formProvider.d.ts |
| API废弃版本变更 | 类名：formProvider； API声明：function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>; 差异内容：NA | 类名：formProvider； API声明：function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>; 差异内容：20 | api/@ohos.app.form.formProvider.d.ts |
| 新增API | NA | 类名：FormParam； API声明：ORIGINAL_FORM_KEY = 'ohos.extra.param.key.original_form_id' 差异内容：ORIGINAL_FORM_KEY = 'ohos.extra.param.key.original_form_id' | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：LaunchReason； API声明：FORM_SIZE_CHANGE = 3 差异内容：FORM_SIZE_CHANGE = 3 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：formInfo； API声明：interface RunningFormInfo 差异内容：interface RunningFormInfo | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：RunningFormInfo； API声明：readonly formId: string; 差异内容：readonly formId: string; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：RunningFormInfo； API声明：readonly bundleName: string; 差异内容：readonly bundleName: string; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：RunningFormInfo； API声明：readonly formLocation: FormLocation; 差异内容：readonly formLocation: FormLocation; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：RunningFormInfo； API声明：readonly moduleName: string; 差异内容：readonly moduleName: string; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：RunningFormInfo； API声明：readonly abilityName: string; 差异内容：readonly abilityName: string; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：RunningFormInfo； API声明：readonly formName: string; 差异内容：readonly formName: string; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：RunningFormInfo； API声明：readonly dimension: number; 差异内容：readonly dimension: number; | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：formInfo； API声明：enum FormLocation 差异内容：enum FormLocation | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormLocation； API声明：DESKTOP = 0 差异内容：DESKTOP = 0 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormLocation； API声明：FORM_CENTER = 1 差异内容：FORM_CENTER = 1 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormLocation； API声明：FORM_MANAGER = 2 差异内容：FORM_MANAGER = 2 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormLocation； API声明：NEGATIVE_SCREEN = 3 差异内容：NEGATIVE_SCREEN = 3 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormLocation； API声明：SCREEN_LOCK = 6 差异内容：SCREEN_LOCK = 6 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：FormLocation； API声明：AI_SUGGESTION = 7 差异内容：AI_SUGGESTION = 7 | api/@ohos.app.form.formInfo.d.ts |
| 新增API | NA | 类名：formProvider； API声明：function getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>; 差异内容：function getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>; | api/@ohos.app.form.formProvider.d.ts |
| 新增API | NA | 类名：formProvider； API声明：function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>; 差异内容：function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>; | api/@ohos.app.form.formProvider.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：LiveFormExtensionContext； API声明：startAbilityByLiveForm(want: Want): Promise<void>; 差异内容：startAbilityByLiveForm(want: Want): Promise<void>; | api/application/LiveFormExtensionContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FormExtensionAbility； API声明：onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void; 差异内容：onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void; | api/@ohos.app.form.FormExtensionAbility.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FormExtensionAbility； API声明：onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void; 差异内容：onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void; | api/@ohos.app.form.FormExtensionAbility.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class FormEditExtensionContext 差异内容：export default class FormEditExtensionContext | 类名：global； API声明：declare class FormEditExtensionContext 差异内容：NA | api/application/FormEditExtensionContext.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class FormExtensionContext 差异内容：export default class FormExtensionContext | 类名：global； API声明：declare class FormExtensionContext 差异内容：NA | api/application/FormExtensionContext.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class LiveFormExtensionContext 差异内容：export default class LiveFormExtensionContext | 类名：global； API声明：declare class LiveFormExtensionContext 差异内容：NA | api/application/LiveFormExtensionContext.d.ts |
