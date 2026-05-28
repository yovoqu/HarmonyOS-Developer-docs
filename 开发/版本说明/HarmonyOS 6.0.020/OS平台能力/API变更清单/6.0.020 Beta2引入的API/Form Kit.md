# Form Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-formkit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：formProvider； API声明：function getFormRect(formId: string): Promise<formInfo.Rect>; 差异内容：function getFormRect(formId: string): Promise<formInfo.Rect>; | api/@ohos.app.form.formProvider.d.ts |
| 删除API | 类名：FormParam； API声明：FORM_WIDTH_VP_KEY = 'ohos.extra.param.key.form_width_vp' 差异内容：FORM_WIDTH_VP_KEY = 'ohos.extra.param.key.form_width_vp' | NA | api/@ohos.app.form.formInfo.d.ts |
| 删除API | 类名：FormParam； API声明：FORM_HEIGHT_VP_KEY = 'ohos.extra.param.key.form_height_vp' 差异内容：FORM_HEIGHT_VP_KEY = 'ohos.extra.param.key.form_height_vp' | NA | api/@ohos.app.form.formInfo.d.ts |
| 删除API | 类名：LiveFormExtensionContext； API声明：setBackgroundImage(res: Resource): Promise&lt;void&gt;; 差异内容：setBackgroundImage(res: Resource): Promise&lt;void&gt;; | NA | api/application/LiveFormExtensionContext.d.ts |
| API从不支持元服务到支持元服务 | 类名：formInfo； API声明：interface OverflowInfo 差异内容：NA | 类名：formInfo； API声明：interface OverflowInfo 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：OverflowInfo； API声明：area: Rect; 差异内容：NA | 类名：OverflowInfo； API声明：area: Rect; 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：OverflowInfo； API声明：duration: number; 差异内容：NA | 类名：OverflowInfo； API声明：duration: number; 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：formInfo； API声明：interface Rect 差异内容：NA | 类名：formInfo； API声明：interface Rect 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect； API声明：left: number; 差异内容：NA | 类名：Rect； API声明：left: number; 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect； API声明：top: number; 差异内容：NA | 类名：Rect； API声明：top: number; 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect； API声明：width: number; 差异内容：NA | 类名：Rect； API声明：width: number; 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect； API声明：height: number; 差异内容：NA | 类名：Rect； API声明：height: number; 差异内容：atomicservice | api/@ohos.app.form.formInfo.d.ts |
| API从不支持元服务到支持元服务 | 类名：formProvider； API声明：function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise&lt;void&gt;; 差异内容：NA | 类名：formProvider； API声明：function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise&lt;void&gt;; 差异内容：atomicservice | api/@ohos.app.form.formProvider.d.ts |
| API从不支持元服务到支持元服务 | 类名：formProvider； API声明：function cancelOverflow(formId: string): Promise&lt;void&gt;; 差异内容：NA | 类名：formProvider； API声明：function cancelOverflow(formId: string): Promise&lt;void&gt;; 差异内容：atomicservice | api/@ohos.app.form.formProvider.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：OverflowInfo； API声明：useDefaultAnimation?: boolean; 差异内容：useDefaultAnimation?: boolean; | api/@ohos.app.form.formInfo.d.ts |
