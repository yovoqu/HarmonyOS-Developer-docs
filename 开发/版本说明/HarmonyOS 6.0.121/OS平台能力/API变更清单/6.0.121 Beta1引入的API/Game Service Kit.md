# Game Service Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：GameErrorCode； API声明：NOT_MINI_GAME_ERROR = 1002000018 差异内容：NOT_MINI_GAME_ERROR = 1002000018 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：PARAM_ERROR = 1002000019 差异内容：PARAM_ERROR = 1002000019 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：USER_CANCELED = 1002000020 差异内容：USER_CANCELED = 1002000020 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：CALLS_FREQUENT = 1002000021 差异内容：CALLS_FREQUENT = 1002000021 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：PAY_PRODUCT_INVALID = 1002000050 差异内容：PAY_PRODUCT_INVALID = 1002000050 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：PAY_PRODUCT_OWNED = 1002000051 差异内容：PAY_PRODUCT_OWNED = 1002000051 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：PAY_PRODUCT_NOT_OWNED = 1002000052 差异内容：PAY_PRODUCT_NOT_OWNED = 1002000052 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：PAY_PRODUCT_CONSUMED = 1002000053 差异内容：PAY_PRODUCT_CONSUMED = 1002000053 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：PAY_ACCOUNT_REGION_UNSUPPORTED = 1002000054 差异内容：PAY_ACCOUNT_REGION_UNSUPPORTED = 1002000054 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode； API声明：PAY_DEAL_REJECTED = 1002000056 差异内容：PAY_DEAL_REJECTED = 1002000056 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer； API声明：interface MiniGameLoginParam 差异内容：interface MiniGameLoginParam | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGameLoginParam； API声明：gameAppId: string; 差异内容：gameAppId: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGameLoginParam； API声明：extraData?: string; 差异内容：extraData?: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer； API声明：interface MiniGamePlayer 差异内容：interface MiniGamePlayer | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer； API声明：playerId: string; 差异内容：playerId: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer； API声明：playerLevel: number; 差异内容：playerLevel: number; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer； API声明：playerSign: string; 差异内容：playerSign: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer； API声明：signTs: string; 差异内容：signTs: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer； API声明：isAdult: boolean; 差异内容：isAdult: boolean; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer； API声明：extraData?: string; 差异内容：extraData?: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer； API声明：function miniGameLogin(context: common.Context, loginParam: MiniGameLoginParam): Promise&lt;MiniGamePlayer&gt;; 差异内容：function miniGameLogin(context: common.Context, loginParam: MiniGameLoginParam): Promise&lt;MiniGamePlayer&gt;; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer； API声明：function miniGamePay(context: common.Context, parameter: PurchaseParameter): Promise&lt;CreatePurchaseResult&gt;; 差异内容：function miniGamePay(context: common.Context, parameter: PurchaseParameter): Promise&lt;CreatePurchaseResult&gt;; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer； API声明：function on(type: 'miniGameAddictionPrevented', callback: Callback&lt;string&gt;): void; 差异内容：function on(type: 'miniGameAddictionPrevented', callback: Callback&lt;string&gt;): void; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer； API声明：function off(type: 'miniGameAddictionPrevented', callback?: Callback&lt;string&gt;): void; 差异内容：function off(type: 'miniGameAddictionPrevented', callback?: Callback&lt;string&gt;): void; | api/@hms.core.gameservice.gameplayer.d.ts |
