# User Authentication Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：userAuth； API声明：function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void; 差异内容：12500002,12500005,12500006,12500010,201,401 | 类名：userAuth； API声明：function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void; 差异内容：12500002,12500005,12500006,12500010,12500013,201,401 | api/@ohos.userIAM.userAuth.d.ts |
| 错误码变更 | 类名：UserAuthInstance； API声明：start(): void; 差异内容：12500001,12500002,12500003,12500004,12500005,12500006,12500007,12500009,12500010,12500011,201,401 | 类名：UserAuthInstance； API声明：start(): void; 差异内容：12500001,12500002,12500003,12500004,12500005,12500006,12500007,12500009,12500010,12500011,12500013,201,401 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResultCode； API声明：PIN_EXPIRED = 12500013 差异内容：PIN_EXPIRED = 12500013 | api/@ohos.userIAM.userAuth.d.ts |
