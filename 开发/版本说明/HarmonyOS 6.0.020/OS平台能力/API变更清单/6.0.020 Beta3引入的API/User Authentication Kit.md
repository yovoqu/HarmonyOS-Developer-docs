# User Authentication Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：userAuth； API声明：enum UserAuthTipCode 差异内容：enum UserAuthTipCode | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode； API声明：COMPARE_FAILURE = 1 差异内容：COMPARE_FAILURE = 1 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode； API声明：TIMEOUT = 2 差异内容：TIMEOUT = 2 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode； API声明：TEMPORARILY_LOCKED = 3 差异内容：TEMPORARILY_LOCKED = 3 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode； API声明：PERMANENTLY_LOCKED = 4 差异内容：PERMANENTLY_LOCKED = 4 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode； API声明：WIDGET_LOADED = 5 差异内容：WIDGET_LOADED = 5 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthTipCode； API声明：WIDGET_RELEASED = 6 差异内容：WIDGET_RELEASED = 6 | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth； API声明：interface AuthTipInfo 差异内容：interface AuthTipInfo | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthTipInfo； API声明：tipType: UserAuthType; 差异内容：tipType: UserAuthType; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthTipInfo； API声明：tipCode: UserAuthTipCode; 差异内容：tipCode: UserAuthTipCode; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth； API声明：type AuthTipCallback = (authTipInfo: AuthTipInfo) => void; 差异内容：type AuthTipCallback = (authTipInfo: AuthTipInfo) => void; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：UserAuthResultCode； API声明：INVALID_PARAMETERS = 12500008 差异内容：INVALID_PARAMETERS = 12500008 | api/@ohos.userIAM.userAuth.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：UserAuthInstance； API声明：on(type: 'authTip', callback: AuthTipCallback): void; 差异内容：on(type: 'authTip', callback: AuthTipCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：UserAuthInstance； API声明：off(type: 'authTip', callback?: AuthTipCallback): void; 差异内容：off(type: 'authTip', callback?: AuthTipCallback): void; | api/@ohos.userIAM.userAuth.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AuthParam； API声明：skipLockedBiometricAuth?: boolean; 差异内容：skipLockedBiometricAuth?: boolean; | api/@ohos.userIAM.userAuth.d.ts |
