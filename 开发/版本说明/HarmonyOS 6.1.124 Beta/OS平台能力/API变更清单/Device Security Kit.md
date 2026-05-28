# Device Security Kit

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAuthentication； API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; 差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication； API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication； API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication； API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication； API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication； API声明：function exportData(authID: bigint, label: TUILable): Promise&lt;ArrayBuffer&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function exportData(authID: bigint, label: TUILable): Promise&lt;ArrayBuffer&gt;; 差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication； API声明：function checkConfirmUITextFormat(text: string): Promise&lt;TextCheckResult&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function checkConfirmUITextFormat(text: string): Promise&lt;TextCheckResult&gt;; 差异内容：1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_TUI_OCCUPIED = 1019100025 差异内容：TRUSTED_AUTH_ERROR_TUI_OCCUPIED = 1019100025 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：CS_VERIFY_NULL = 0x12001081 差异内容：CS_VERIFY_NULL = 0x12001081 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：CS_VERIFY_ABNORMAL = 0x12001082 差异内容：CS_VERIFY_ABNORMAL = 0x12001082 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FS_MOUNT_ABNORMAL = 0x1C001102 差异内容：FS_MOUNT_ABNORMAL = 0x1C001102 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：DRIVER_CS_ABNORMAL = 0x1C001200 差异内容：DRIVER_CS_ABNORMAL = 0x1C001200 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：DRIVER_MMAP_ABNORMAL = 0x1C001201 差异内容：DRIVER_MMAP_ABNORMAL = 0x1C001201 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：KERNEL_MEMORY_ABNORMAL = 0x1C001300 差异内容：KERNEL_MEMORY_ABNORMAL = 0x1C001300 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：PROCESS_DEBUG_ABNORMAL = 0x1C001401 差异内容：PROCESS_DEBUG_ABNORMAL = 0x1C001401 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：PROCESS_CRASH_ABNORMAL = 0x1C001402 差异内容：PROCESS_CRASH_ABNORMAL = 0x1C001402 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：PROCESS_PRIVILEGE_ESCALATION = 0x1C001403 差异内容：PROCESS_PRIVILEGE_ESCALATION = 0x1C001403 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明：function acquireCodeSign(path: string): string; 差异内容：function acquireCodeSign(path: string): string; | api/@hms.security.securityAudit.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare namespace businessRiskIntelligentDetection 差异内容：NA | 类名：global； API声明：declare namespace businessRiskIntelligentDetection 差异内容：atomicservice | api/@hms.security.businessRiskIntelligentDetection.d.ts |
