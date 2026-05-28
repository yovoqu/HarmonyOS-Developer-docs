# IAP Kit

更新时间：2026-04-20 06:33:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-6101

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：iap； API声明：function queryEnvironmentStatus(context: common.Context): Promise&lt;void&gt;; 差异内容：NA | 类名：iap； API声明：function queryEnvironmentStatus(context: common.Context): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function queryEnvironmentStatus(context: common.Context, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：iap； API声明：function queryEnvironmentStatus(context: common.Context, callback: AsyncCallback&lt;void&gt;): void; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter): Promise<Array&lt;Product&gt;>; 差异内容：NA | 类名：iap； API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter): Promise<Array&lt;Product&gt;>; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array&lt;Product&gt;>): void; 差异内容：NA | 类名：iap； API声明：function queryProducts(context: common.UIAbilityContext, parameter: QueryProductsParameter, callback: AsyncCallback<Array&lt;Product&gt;>): void; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function queryProducts(context: common.UIAbilityContext, productIds: string[]): Promise<Array&lt;Product&gt;>; 差异内容：NA | 类名：iap； API声明：function queryProducts(context: common.UIAbilityContext, productIds: string[]): Promise<Array&lt;Product&gt;>; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise&lt;CreatePurchaseResult&gt;; 差异内容：NA | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter): Promise&lt;CreatePurchaseResult&gt;; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback&lt;CreatePurchaseResult&gt;): void; 差异内容：NA | 类名：iap； API声明：function createPurchase(context: common.UIAbilityContext, parameter: PurchaseParameter, callback: AsyncCallback&lt;CreatePurchaseResult&gt;): void; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter): Promise&lt;void&gt;; 差异内容：NA | 类名：iap； API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：iap； API声明：function finishPurchase(context: common.UIAbilityContext, parameter: FinishPurchaseParameter, callback: AsyncCallback&lt;void&gt;): void; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise&lt;QueryPurchaseResult&gt;; 差异内容：NA | 类名：iap； API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter): Promise&lt;QueryPurchaseResult&gt;; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback&lt;QueryPurchaseResult&gt;): void; 差异内容：NA | 类名：iap； API声明：function queryPurchases(context: common.UIAbilityContext, parameter: QueryPurchasesParameter, callback: AsyncCallback&lt;QueryPurchaseResult&gt;): void; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增错误码 | 类名：iap； API声明：function isSandboxActivated(context: common.Context): Promise&lt;boolean&gt;; 差异内容：NA | 类名：iap； API声明：function isSandboxActivated(context: common.Context): Promise&lt;boolean&gt;; 差异内容：801 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：global； API声明：declare struct CashierComponent 差异内容：declare struct CashierComponent | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent； API声明：@Require @Prop params: iap.PurchaseParameter; 差异内容：@Require @Prop params: iap.PurchaseParameter; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent； API声明：displayOptions?: cashierComponentManager.CashierDisplayOptions; 差异内容：displayOptions?: cashierComponentManager.CashierDisplayOptions; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent； API声明：purchaseListener: cashierComponentManager.CashierListener; 差异内容：purchaseListener: cashierComponentManager.CashierListener; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierComponent； API声明：build(): void; 差异内容：build(): void; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：global； API声明：declare namespace cashierComponentManager 差异内容：declare namespace cashierComponentManager | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：cashierComponentManager； API声明：interface CashierListener 差异内容：interface CashierListener | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierListener； API声明：onPurchaseSuccess(productId: string, purchaseResult: iap.CreatePurchaseResult): void; 差异内容：onPurchaseSuccess(productId: string, purchaseResult: iap.CreatePurchaseResult): void; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierListener； API声明：onPurchaseFailure(productId: string, error: BusinessError&lt;void&gt;): void; 差异内容：onPurchaseFailure(productId: string, error: BusinessError&lt;void&gt;): void; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：cashierComponentManager； API声明：interface CashierDisplayOptions 差异内容：interface CashierDisplayOptions | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：CashierDisplayOptions； API声明：backgroundColor?: ResourceColor; 差异内容：backgroundColor?: ResourceColor; | api/@hms.core.iap.cashierComponent.d.ets |
| 新增API | NA | 类名：iap； API声明：function showManagedInvoices(context: common.Context, purchaseOrderId: string): Promise&lt;void&gt;; 差异内容：function showManagedInvoices(context: common.Context, purchaseOrderId: string): Promise&lt;void&gt;; | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode； API声明：PURCHASE_NOT_FOUND = 1001860064 差异内容：PURCHASE_NOT_FOUND = 1001860064 | api/@hms.core.iap.d.ts |
| 新增API | NA | 类名：IAPErrorCode； API声明：OPERATION_NOT_SUPPORTED = 1001860065 差异内容：OPERATION_NOT_SUPPORTED = 1001860065 | api/@hms.core.iap.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.core.iap.cashierComponent.d.ets 差异内容：IAPKit | api/@hms.core.iap.cashierComponent.d.ets |
