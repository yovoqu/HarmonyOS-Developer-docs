# User Authentication Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-userauthenticationkit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：userAuth； API声明：const PERMANENT_LOCKOUT_DURATION: number = 0x7fffffff; 差异内容：const PERMANENT_LOCKOUT_DURATION: number = 0x7fffffff; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth； API声明：interface AuthLockState 差异内容：interface AuthLockState | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthLockState； API声明：isLocked: boolean; 差异内容：isLocked: boolean; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthLockState； API声明：remainingAuthAttempts: number; 差异内容：remainingAuthAttempts: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：AuthLockState； API声明：lockoutDuration: number; 差异内容：lockoutDuration: number; | api/@ohos.userIAM.userAuth.d.ts |
| 新增API | NA | 类名：userAuth； API声明：function getAuthLockState(authType: UserAuthType): Promise&lt;AuthLockState&gt;; 差异内容：function getAuthLockState(authType: UserAuthType): Promise&lt;AuthLockState&gt;; | api/@ohos.userIAM.userAuth.d.ts |
