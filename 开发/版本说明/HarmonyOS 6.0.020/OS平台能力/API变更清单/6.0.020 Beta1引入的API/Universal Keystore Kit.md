# Universal Keystore Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-universalkeystorekit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：huks； API声明：function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>; 差异内容：function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>; | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：huks； API声明：function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>; 差异内容：function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>; | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：HuksExceptionErrCode； API声明：HUKS_ERR_CODE_INVALID_ARGUMENT = 12000018 差异内容：HUKS_ERR_CODE_INVALID_ARGUMENT = 12000018 | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：HuksUserAuthType； API声明：HUKS_USER_AUTH_TYPE_TUI_PIN = 1 << 5 差异内容：HUKS_USER_AUTH_TYPE_TUI_PIN = 1 << 5 | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：huks； API声明：export enum HuksKeyWrapType 差异内容：export enum HuksKeyWrapType | api/@ohos.security.huks.d.ts |
| 新增API | NA | 类名：HuksKeyWrapType； API声明：HUKS_KEY_WRAP_TYPE_HUK_BASED = 2 差异内容：HUKS_KEY_WRAP_TYPE_HUK_BASED = 2 | api/@ohos.security.huks.d.ts |
