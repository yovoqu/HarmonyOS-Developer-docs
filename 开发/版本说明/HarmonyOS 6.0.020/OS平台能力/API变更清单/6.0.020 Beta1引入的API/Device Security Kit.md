# Device Security Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace dlpAntiPeep 差异内容：declare namespace dlpAntiPeep | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep； API声明：enum DlpAntiPeepStatus 差异内容：enum DlpAntiPeepStatus | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：DlpAntiPeepStatus； API声明：PASS = 0 差异内容：PASS = 0 | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：DlpAntiPeepStatus； API声明：HIDE = 1 差异内容：HIDE = 1 | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep； API声明：function isDlpAntiPeepSwitchOn(): Promise&lt;boolean&gt;; 差异内容：function isDlpAntiPeepSwitchOn(): Promise&lt;boolean&gt;; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep； API声明：function on(type: 'dlpAntiPeep', callback: Callback&lt;DlpAntiPeepStatus&gt;): void; 差异内容：function on(type: 'dlpAntiPeep', callback: Callback&lt;DlpAntiPeepStatus&gt;): void; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep； API声明：function off(type: 'dlpAntiPeep', callback?: Callback&lt;DlpAntiPeepStatus&gt;): void; 差异内容：function off(type: 'dlpAntiPeep', callback?: Callback&lt;DlpAntiPeepStatus&gt;): void; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep； API声明：function getDlpAntiPeepInfo(): DlpAntiPeepStatus; 差异内容：function getDlpAntiPeepInfo(): DlpAntiPeepStatus; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：dlpAntiPeep； API声明：function passDlpAntiPeepInfo(): void; 差异内容：function passDlpAntiPeepInfo(): void; | api/@hms.security.dlpAntiPeep.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace trustedAuthentication 差异内容：declare namespace trustedAuthentication | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export enum AuthType 差异内容：export enum AuthType | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthType； API声明：AUTH_TYPE_FACE = 2 差异内容：AUTH_TYPE_FACE = 2 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthType； API声明：AUTH_TYPE_FINGERPRINT = 4 差异内容：AUTH_TYPE_FINGERPRINT = 4 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthType； API声明：AUTH_TYPE_TUI_PIN = 32 差异内容：AUTH_TYPE_TUI_PIN = 32 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export enum PasswordType 差异内容：export enum PasswordType | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordType； API声明：PASSWORD_TYPE_DIGITAL = 0 差异内容：PASSWORD_TYPE_DIGITAL = 0 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordType； API声明：PASSWORD_TYPE_MIXED = 1 差异内容：PASSWORD_TYPE_MIXED = 1 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export enum OperateType 差异内容：export enum OperateType | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：OperateType； API声明：OPERATE_TYPE_BIOMETRIC_AUTH = 1 差异内容：OPERATE_TYPE_BIOMETRIC_AUTH = 1 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：OperateType； API声明：OPERATE_TYPE_CONTENT_AUTH = 2 差异内容：OPERATE_TYPE_CONTENT_AUTH = 2 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export enum TrustedAuthErrorCode 差异内容：export enum TrustedAuthErrorCode | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NO_PERMISSION = 1019100001 差异内容：TRUSTED_AUTH_ERROR_NO_PERMISSION = 1019100001 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_ILLEGAL_ARGUMENT = 1019100002 差异内容：TRUSTED_AUTH_ERROR_ILLEGAL_ARGUMENT = 1019100002 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_PWD_LIMIT_REACHED = 1019100003 差异内容：TRUSTED_AUTH_ERROR_PWD_LIMIT_REACHED = 1019100003 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_PWD_DELETE_FAILED = 1019100004 差异内容：TRUSTED_AUTH_ERROR_PWD_DELETE_FAILED = 1019100004 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_VERIFY_FAILED = 1019100005 差异内容：TRUSTED_AUTH_ERROR_VERIFY_FAILED = 1019100005 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_CHECK_CONFIRM_TEXT_FAILED = 1019100006 差异内容：TRUSTED_AUTH_ERROR_CHECK_CONFIRM_TEXT_FAILED = 1019100006 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NOT_SUPPORT_IMAGE = 1019100007 差异内容：TRUSTED_AUTH_ERROR_NOT_SUPPORT_IMAGE = 1019100007 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_USER_REQ_CANCEL = 1019100008 差异内容：TRUSTED_AUTH_ERROR_USER_REQ_CANCEL = 1019100008 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_EXPORT_DATA_FAILED = 1019100009 差异内容：TRUSTED_AUTH_ERROR_EXPORT_DATA_FAILED = 1019100009 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_IMPORT_DATA_FAILED = 1019100010 差异内容：TRUSTED_AUTH_ERROR_IMPORT_DATA_FAILED = 1019100010 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_INVALID_CONTENT = 1019100011 差异内容：TRUSTED_AUTH_ERROR_INVALID_CONTENT = 1019100011 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_INVALID_AUTH_ID = 1019100012 差异内容：TRUSTED_AUTH_ERROR_INVALID_AUTH_ID = 1019100012 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_SET_PWD_FAILED = 1019100013 差异内容：TRUSTED_AUTH_ERROR_SET_PWD_FAILED = 1019100013 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_MODIFY_PWD_FAILED = 1019100014 差异内容：TRUSTED_AUTH_ERROR_MODIFY_PWD_FAILED = 1019100014 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_RESIGN_FAILED = 1019100015 差异内容：TRUSTED_AUTH_ERROR_BIO_RESIGN_FAILED = 1019100015 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_FEATURE_INITIALIZATION_FAILED = 1019100016 差异内容：TRUSTED_AUTH_FEATURE_INITIALIZATION_FAILED = 1019100016 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export interface PasswordInfo 差异内容：export interface PasswordInfo | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo； API声明：pwdType: PasswordType; 差异内容：pwdType: PasswordType; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo； API声明：pwdMaxLength: number; 差异内容：pwdMaxLength: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo； API声明：pwdMinLength: number; 差异内容：pwdMinLength: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：PasswordInfo； API声明：maxAuthFailCount: number; 差异内容：maxAuthFailCount: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export interface AuthReqParams 差异内容：export interface AuthReqParams | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthReqParams； API声明：reqType: AuthType; 差异内容：reqType: AuthType; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthReqParams； API声明：authContent: Array&lt;string&gt;; 差异内容：authContent: Array&lt;string&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export interface TUILable 差异内容：export interface TUILable | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TUILable； API声明：image: ArrayBuffer; 差异内容：image: ArrayBuffer; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TUILable； API声明：title: string; 差异内容：title: string; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export interface AuthToken 差异内容：export interface AuthToken | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthToken； API声明：authToken: Uint8Array; 差异内容：authToken: Uint8Array; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export interface AuthInfo 差异内容：export interface AuthInfo | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthInfo； API声明：authToken: Uint8Array; 差异内容：authToken: Uint8Array; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：AuthInfo； API声明：authID: bigint; 差异内容：authID: bigint; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：export interface TextCheckResult 差异内容：export interface TextCheckResult | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TextCheckResult； API声明：result: number; 差异内容：result: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TextCheckResult； API声明：lastIndex: number; 差异内容：lastIndex: number; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; 差异内容：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise&lt;AuthToken&gt;; 差异内容：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise&lt;AuthToken&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function importData(data: ArrayBuffer, authID: bigint): Promise&lt;void&gt;; 差异内容：function importData(data: ArrayBuffer, authID: bigint): Promise&lt;void&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function exportData(authID: bigint, label: TUILable): Promise&lt;ArrayBuffer&gt;; 差异内容：function exportData(authID: bigint, label: TUILable): Promise&lt;ArrayBuffer&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：trustedAuthentication； API声明：function checkConfirmUITextFormat(text: string): Promise&lt;TextCheckResult&gt;; 差异内容：function checkConfirmUITextFormat(text: string): Promise&lt;TextCheckResult&gt;; | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：safetyDetect； API声明：function checkSysIntegrityEnhanced(req: SysIntegrityRequest): Promise&lt;SysIntegrityResponse&gt;; 差异内容：function checkSysIntegrityEnhanced(req: SysIntegrityRequest): Promise&lt;SysIntegrityResponse&gt;; | api/@hms.security.safetyDetect.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.security.dlpAntiPeep.d.ts 差异内容：DeviceSecurityKit | api/@hms.security.dlpAntiPeep.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.security.trustedAuthentication.d.ts 差异内容：DeviceSecurityKit | api/@hms.security.trustedAuthentication.d.ts |
