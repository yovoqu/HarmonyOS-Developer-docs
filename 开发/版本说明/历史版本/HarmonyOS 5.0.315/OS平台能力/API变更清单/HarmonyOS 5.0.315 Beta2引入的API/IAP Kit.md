# IAP Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PurchaseParameter； API声明：quantity?: number; 差异内容：quantity?: number; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：iap； API声明：function createRefundRequest(context: common.Context, purchaseOrderId: string): Promise<void>; 差异内容：function createRefundRequest(context: common.Context, purchaseOrderId: string): Promise<void>; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode； API声明：PURCHASE_ALREADY_REFUNDED = 1001860061 差异内容：PURCHASE_ALREADY_REFUNDED = 1001860061 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode； API声明：REFUND_NOT_ALLOWED = 1001860062 差异内容：REFUND_NOT_ALLOWED = 1001860062 | api/@hms.core.iap.d.ts |
