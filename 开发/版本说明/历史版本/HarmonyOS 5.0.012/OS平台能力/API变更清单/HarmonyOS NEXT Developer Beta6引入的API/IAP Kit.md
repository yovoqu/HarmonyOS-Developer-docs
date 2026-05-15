# IAP Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-b061

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<CreatePurchaseResult>; 差异内容：1001860000,1001860001,1001860002,1001860003,1001860004,1001860005,1001860007,1001860051,1001860054,1001860056,401 | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise<CreatePurchaseResult>; 差异内容：1001860000,1001860001,1001860002,1001860003,1001860004,1001860005,1001860007,1001860051,1001860054,1001860056,1001860059,1001860060,401 | api/@hms.core.iap.d.ts |
| 错误码变更 | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void; 差异内容：1001860000,1001860001,1001860002,1001860003,1001860004,1001860005,1001860007,1001860051,1001860054,1001860056,401 | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback<CreatePurchaseResult>): void; 差异内容：1001860000,1001860001,1001860002,1001860003,1001860004,1001860005,1001860007,1001860051,1001860054,1001860056,1001860059,1001860060,401 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PurchaseParameter； API声明：promotionalOfferId?: string; 差异内容：promotionalOfferId?: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PurchaseParameter； API声明：applicationUserName?: string; 差异内容：applicationUserName?: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PurchaseParameter； API声明：jwsRepresentation?: string; 差异内容：jwsRepresentation?: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：Product； API声明：promotionalOffers?: PromotionalOffer[]; 差异内容：promotionalOffers?: PromotionalOffer[]; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：iap； API声明： interface PromotionalOffer 差异内容： interface PromotionalOffer | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PromotionalOffer； API声明：offerId: string; 差异内容：offerId: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PromotionalOffer； API声明：paymentMode: OfferPaymentMode; 差异内容：paymentMode: OfferPaymentMode; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PromotionalOffer； API声明：periodUnit?: PeriodUnit; 差异内容：periodUnit?: PeriodUnit; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PromotionalOffer； API声明：periodCount?: number; 差异内容：periodCount?: number; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PromotionalOffer； API声明：localPrice: string; 差异内容：localPrice: string; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：PromotionalOffer； API声明：microPrice: number; 差异内容：microPrice: number; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode； API声明：INVALID_PROMOTIONAL_OFFER = 1001860059 差异内容：INVALID_PROMOTIONAL_OFFER = 1001860059 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode； API声明：INVALID_PURCHASE_SIGNATURE = 1001860060 差异内容：INVALID_PURCHASE_SIGNATURE = 1001860060 | api/@hms.core.iap.d.ts |
