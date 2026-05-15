# Payment Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace realNameService 差异内容：declare namespace realNameService | api/@hms.core.payment.realNameService.d.ts |
| 新增API | NA | 类名：realNameService； API声明：function startRealNameVerification(context: common.UIAbilityContext \| common.UIExtensionContext, preVerifyId: string): Promise<string>; 差异内容：function startRealNameVerification(context: common.UIAbilityContext \| common.UIExtensionContext, preVerifyId: string): Promise<string>; | api/@hms.core.payment.realNameService.d.ts |
| 新增API | NA | 类名：realNameService； API声明：function startRealNameAuth(context: common.UIAbilityContext \| common.UIExtensionContext): Promise<string>; 差异内容：function startRealNameAuth(context: common.UIAbilityContext \| common.UIExtensionContext): Promise<string>; | api/@hms.core.payment.realNameService.d.ts |
| 新增API | NA | 类名：realNameService； API声明：function startFaceVerification(context: common.UIAbilityContext \| common.UIExtensionContext, preVerifyId: string): Promise<string>; 差异内容：function startFaceVerification(context: common.UIAbilityContext \| common.UIExtensionContext, preVerifyId: string): Promise<string>; | api/@hms.core.payment.realNameService.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.core.payment.realNameService.d.ts 差异内容：PaymentKit | api/@hms.core.payment.realNameService.d.ts |
