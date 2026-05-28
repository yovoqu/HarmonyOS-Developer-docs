# Payment Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace ecnyPaymentService 差异内容： declare namespace ecnyPaymentService | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：ecnyPaymentService； API声明：function requestEcnyPayment(context: common.Context, orderInfo: EcnyOrderInfo): Promise&lt;EcnyPayResult&gt;; 差异内容：function requestEcnyPayment(context: common.Context, orderInfo: EcnyOrderInfo): Promise&lt;EcnyPayResult&gt;; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：ecnyPaymentService； API声明： interface EcnyOrderInfo 差异内容： interface EcnyOrderInfo | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：merchantAppId: string; 差异内容：merchantAppId: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：merchantNo: string; 差异内容：merchantNo: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：acqAgtInstnId?: string; 差异内容：acqAgtInstnId?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：creditorInstitutionId: string; 差异内容：creditorInstitutionId: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：encryptedKey: string; 差异内容：encryptedKey: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：encryptedInfo: string; 差异内容：encryptedInfo: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：encryptionSN?: string; 差异内容：encryptionSN?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：lastWalletId?: string; 差异内容：lastWalletId?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyOrderInfo； API声明：extraInfo?: string; 差异内容：extraInfo?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：ecnyPaymentService； API声明： interface EcnyPayResult 差异内容： interface EcnyPayResult | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyPayResult； API声明：orderNo: string; 差异内容：orderNo: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
| 新增API | NA | 类名：EcnyPayResult； API声明：extraInfo?: string; 差异内容：extraInfo?: string; | api/@hms.core.payment.ecnyPaymentService.d.ts |
