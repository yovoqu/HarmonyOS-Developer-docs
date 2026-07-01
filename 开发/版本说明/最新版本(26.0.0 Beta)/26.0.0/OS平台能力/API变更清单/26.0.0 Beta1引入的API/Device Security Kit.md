# Device Security Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAuthentication； API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：1019100024 | api/@hms.security.trustedAuthentication.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace riskControlEngine 差异内容：declare namespace riskControlEngine | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine； API声明：type ValueType = number \| boolean \| string; 差异内容：type ValueType = number \| boolean \| string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine； API声明：interface AppFactorData 差异内容：interface AppFactorData | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：AppFactorData； API声明：factorName: string; 差异内容：factorName: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：AppFactorData； API声明：factorValue: ValueType; 差异内容：factorValue: ValueType; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine； API声明：interface ImportData 差异内容：interface ImportData | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：ImportData； API声明：appFactorData: Array&lt;AppFactorData&gt;; 差异内容：appFactorData: Array&lt;AppFactorData&gt;; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：ImportData； API声明：nonce: string; 差异内容：nonce: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine； API声明：function importRiskFactors(data: ImportData): Promise&lt;void&gt;; 差异内容：function importRiskFactors(data: ImportData): Promise&lt;void&gt;; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine； API声明：interface RiskControlDetectionRequest 差异内容：interface RiskControlDetectionRequest | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：RiskControlDetectionRequest； API声明：policyName: string; 差异内容：policyName: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：RiskControlDetectionRequest； API声明：nonce: string; 差异内容：nonce: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine； API声明：interface RiskControlDetectionResponse 差异内容：interface RiskControlDetectionResponse | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：RiskControlDetectionResponse； API声明：result: string; 差异内容：result: string; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：riskControlEngine； API声明：function getRiskControlResult(req: RiskControlDetectionRequest): Promise&lt;RiskControlDetectionResponse&gt;; 差异内容：function getRiskControlResult(req: RiskControlDetectionRequest): Promise&lt;RiskControlDetectionResponse&gt;; | api/@hms.security.riskControlEngine.d.ts |
| 新增API | NA | 类名：safetyDetect； API声明：enum RiskFactorType 差异内容：enum RiskFactorType | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：HDC_DEBUG_STATE = 'hdcDebugState' 差异内容：HDC_DEBUG_STATE = 'hdcDebugState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：IS_DEVELOPER_MODE = 'isDeveloperMode' 差异内容：IS_DEVELOPER_MODE = 'isDeveloperMode' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：IS_VPN_STATUS = 'isVpnStatus' 差异内容：IS_VPN_STATUS = 'isVpnStatus' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：IS_NET_PROXY_STATUS = 'isNetProxyStatus' 差异内容：IS_NET_PROXY_STATUS = 'isNetProxyStatus' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：SIM_CNT = 'simCnt' 差异内容：SIM_CNT = 'simCnt' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：OOBE_CNT = 'oobeCnt' 差异内容：OOBE_CNT = 'oobeCnt' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：ODID_RESET_CNT = 'odidResetCnt' 差异内容：ODID_RESET_CNT = 'odidResetCnt' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：ODID = 'odid' 差异内容：ODID = 'odid' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：IS_DISPLAY_CAPTURED = 'isDisplayCaptured' 差异内容：IS_DISPLAY_CAPTURED = 'isDisplayCaptured' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：GLOBAL_WINDOW_STATE = 'globalWindowState' 差异内容：GLOBAL_WINDOW_STATE = 'globalWindowState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：BATTERY_CHARGE_STATE = 'batteryChargeState' 差异内容：BATTERY_CHARGE_STATE = 'batteryChargeState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：BATTERY_HEALTH_STATE = 'batteryHealthState' 差异内容：BATTERY_HEALTH_STATE = 'batteryHealthState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorType； API声明：ON_CALL_STATE = 'onCallState' 差异内容：ON_CALL_STATE = 'onCallState' | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect； API声明：interface RiskFactorRequest 差异内容：interface RiskFactorRequest | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorRequest； API声明：nonce: string; 差异内容：nonce: string; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorRequest； API声明：queries: Array&lt;FactorQuery&gt;; 差异内容：queries: Array&lt;FactorQuery&gt;; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect； API声明：interface FactorQuery 差异内容：interface FactorQuery | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：FactorQuery； API声明：factor: RiskFactorType; 差异内容：factor: RiskFactorType; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect； API声明：interface RiskFactorResponse 差异内容：interface RiskFactorResponse | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：RiskFactorResponse； API声明：result: string; 差异内容：result: string; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：safetyDetect； API声明：function queryRiskFactors(req: RiskFactorRequest): Promise&lt;RiskFactorResponse&gt;; 差异内容：function queryRiskFactors(req: RiskFactorRequest): Promise&lt;RiskFactorResponse&gt;; | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_SHARE = 0x0F000002 差异内容：FILE_SHARE = 0x0F000002 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：DATA_DRAG = 0x0F000003 差异内容：DATA_DRAG = 0x0F000003 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：DLP_FILE_ACCESS = 0x0F000006 差异内容：DLP_FILE_ACCESS = 0x0F000006 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_CREATE = 0x1C001104 差异内容：FILE_CREATE = 0x1C001104 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_OPEN = 0x1C001105 差异内容：FILE_OPEN = 0x1C001105 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_CLOSE = 0x1C001106 差异内容：FILE_CLOSE = 0x1C001106 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_DELETE = 0x1C001107 差异内容：FILE_DELETE = 0x1C001107 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_RENAME = 0x1C001108 差异内容：FILE_RENAME = 0x1C001108 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_COPY = 0x1C001109 差异内容：FILE_COPY = 0x1C001109 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_SETOWNER = 0x1C00110A 差异内容：FILE_SETOWNER = 0x1C00110A | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_SETMODE = 0x1C00110B 差异内容：FILE_SETMODE = 0x1C00110B | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_SETEXTATTR = 0x1C00110C 差异内容：FILE_SETEXTATTR = 0x1C00110C | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_DELETEEXTATTR = 0x1C00110D 差异内容：FILE_DELETEEXTATTR = 0x1C00110D | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：FILE_WRITE = 0x1C00110E 差异内容：FILE_WRITE = 0x1C00110E | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：FilterType； API声明：FILE_PATH_REGULAR = 0x00010003 差异内容：FILE_PATH_REGULAR = 0x00010003 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明：function acquireAllClientsInfo(): string; 差异内容：function acquireAllClientsInfo(): string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：enum PrivacySensorType 差异内容：enum PrivacySensorType | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorType； API声明：CAMERA = 0 差异内容：CAMERA = 0 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorType； API声明：MICROPHONE = 1 差异内容：MICROPHONE = 1 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorType； API声明：LOCATION = 2 差异内容：LOCATION = 2 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：enum PrivacySensorState 差异内容：enum PrivacySensorState | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorState； API声明：DEFAULT = 0 差异内容：DEFAULT = 0 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorState； API声明：ENABLED_UNDER_SUPER_PRIVACY = 1 差异内容：ENABLED_UNDER_SUPER_PRIVACY = 1 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：PrivacySensorState； API声明：DISABLED_UNDER_SUPER_PRIVACY = 2 差异内容：DISABLED_UNDER_SUPER_PRIVACY = 2 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：interface SuperPrivacyPolicy 差异内容：interface SuperPrivacyPolicy | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicy； API声明：sensorType: PrivacySensorType; 差异内容：sensorType: PrivacySensorType; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicy； API声明：sensorState: PrivacySensorState; 差异内容：sensorState: PrivacySensorState; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：interface SuperPrivacyPolicyInfo 差异内容：interface SuperPrivacyPolicyInfo | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicyInfo； API声明：superPrivacyMode: SuperPrivacyMode; 差异内容：superPrivacyMode: SuperPrivacyMode; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyPolicyInfo； API声明：superPrivacyPolicies: SuperPrivacyPolicy[]; 差异内容：superPrivacyPolicies: SuperPrivacyPolicy[]; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：function getSuperPrivacyPolicies(): Promise&lt;SuperPrivacyPolicyInfo&gt;; 差异内容：function getSuperPrivacyPolicies(): Promise&lt;SuperPrivacyPolicyInfo&gt;; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：function onSuperPrivacyModeOrPolicyChange(callback: Callback&lt;SuperPrivacyPolicyInfo&gt;): void; 差异内容：function onSuperPrivacyModeOrPolicyChange(callback: Callback&lt;SuperPrivacyPolicyInfo&gt;): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：function offSuperPrivacyModeOrPolicyChange(callback?: Callback&lt;SuperPrivacyPolicyInfo&gt;): void; 差异内容：function offSuperPrivacyModeOrPolicyChange(callback?: Callback&lt;SuperPrivacyPolicyInfo&gt;): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_ID_INVALID = 1019100024 差异内容：TRUSTED_AUTH_ERROR_BIO_ID_INVALID = 1019100024 | api/@hms.security.trustedAuthentication.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.security.riskControlEngine.d.ts 差异内容：DeviceSecurityKit | api/@hms.security.riskControlEngine.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare namespace trustedAuthentication 差异内容：NA | 类名：global； API声明：declare namespace trustedAuthentication 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export enum AuthType 差异内容：NA | 类名：trustedAuthentication； API声明：export enum AuthType 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthType； API声明：AUTH_TYPE_FACE = 2 差异内容：NA | 类名：AuthType； API声明：AUTH_TYPE_FACE = 2 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthType； API声明：AUTH_TYPE_FINGERPRINT = 4 差异内容：NA | 类名：AuthType； API声明：AUTH_TYPE_FINGERPRINT = 4 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthType； API声明：AUTH_TYPE_TUI_PIN = 32 差异内容：NA | 类名：AuthType； API声明：AUTH_TYPE_TUI_PIN = 32 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export enum PasswordType 差异内容：NA | 类名：trustedAuthentication； API声明：export enum PasswordType 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordType； API声明：PASSWORD_TYPE_DIGITAL = 0 差异内容：NA | 类名：PasswordType； API声明：PASSWORD_TYPE_DIGITAL = 0 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordType； API声明：PASSWORD_TYPE_MIXED = 1 差异内容：NA | 类名：PasswordType； API声明：PASSWORD_TYPE_MIXED = 1 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export enum OperateType 差异内容：NA | 类名：trustedAuthentication； API声明：export enum OperateType 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：OperateType； API声明：OPERATE_TYPE_BIOMETRIC_AUTH = 1 差异内容：NA | 类名：OperateType； API声明：OPERATE_TYPE_BIOMETRIC_AUTH = 1 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：OperateType； API声明：OPERATE_TYPE_CONTENT_AUTH = 2 差异内容：NA | 类名：OperateType； API声明：OPERATE_TYPE_CONTENT_AUTH = 2 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export enum TrustedAuthErrorCode 差异内容：NA | 类名：trustedAuthentication； API声明：export enum TrustedAuthErrorCode 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NO_PERMISSION = 1019100001 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NO_PERMISSION = 1019100001 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_ILLEGAL_ARGUMENT = 1019100002 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_ILLEGAL_ARGUMENT = 1019100002 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_PWD_LIMIT_REACHED = 1019100003 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_PWD_LIMIT_REACHED = 1019100003 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_PWD_DELETE_FAILED = 1019100004 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_PWD_DELETE_FAILED = 1019100004 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_VERIFY_FAILED = 1019100005 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_VERIFY_FAILED = 1019100005 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_CHECK_CONFIRM_TEXT_FAILED = 1019100006 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_CHECK_CONFIRM_TEXT_FAILED = 1019100006 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NOT_SUPPORT_IMAGE = 1019100007 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NOT_SUPPORT_IMAGE = 1019100007 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_USER_REQ_CANCEL = 1019100008 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_USER_REQ_CANCEL = 1019100008 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_EXPORT_DATA_FAILED = 1019100009 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_EXPORT_DATA_FAILED = 1019100009 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_IMPORT_DATA_FAILED = 1019100010 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_IMPORT_DATA_FAILED = 1019100010 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_INVALID_CONTENT = 1019100011 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_INVALID_CONTENT = 1019100011 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_INVALID_AUTH_ID = 1019100012 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_INVALID_AUTH_ID = 1019100012 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_SET_PWD_FAILED = 1019100013 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_SET_PWD_FAILED = 1019100013 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_MODIFY_PWD_FAILED = 1019100014 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_MODIFY_PWD_FAILED = 1019100014 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_RESIGN_FAILED = 1019100015 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_RESIGN_FAILED = 1019100015 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_FEATURE_INITIALIZATION_FAILED = 1019100016 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_FEATURE_INITIALIZATION_FAILED = 1019100016 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_GET_REMAIN_TIME = 1019100017 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_GET_REMAIN_TIME = 1019100017 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_DISABLE_BIO_AUTH = 1019100018 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_DISABLE_BIO_AUTH = 1019100018 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_MISMATCH = 1019100019 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_MISMATCH = 1019100019 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_REPEATED_BIND = 1019100020 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_BIO_REPEATED_BIND = 1019100020 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NOT_BIND_BIO = 1019100021 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_NOT_BIND_BIO = 1019100021 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_TUI_OCCUPIED = 1019100025 差异内容：NA | 类名：TrustedAuthErrorCode； API声明：TRUSTED_AUTH_ERROR_TUI_OCCUPIED = 1019100025 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export interface PasswordInfo 差异内容：NA | 类名：trustedAuthentication； API声明：export interface PasswordInfo 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo； API声明：pwdType: PasswordType; 差异内容：NA | 类名：PasswordInfo； API声明：pwdType: PasswordType; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo； API声明：pwdMaxLength: number; 差异内容：NA | 类名：PasswordInfo； API声明：pwdMaxLength: number; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo； API声明：pwdMinLength: number; 差异内容：NA | 类名：PasswordInfo； API声明：pwdMinLength: number; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：PasswordInfo； API声明：maxAuthFailCount: number; 差异内容：NA | 类名：PasswordInfo； API声明：maxAuthFailCount: number; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export interface AuthReqParams 差异内容：NA | 类名：trustedAuthentication； API声明：export interface AuthReqParams 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthReqParams； API声明：reqType: AuthType; 差异内容：NA | 类名：AuthReqParams； API声明：reqType: AuthType; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthReqParams； API声明：authContent: Array&lt;string&gt;; 差异内容：NA | 类名：AuthReqParams； API声明：authContent: Array&lt;string&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export interface TUILable 差异内容：NA | 类名：trustedAuthentication； API声明：export interface TUILable 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TUILable； API声明：image: ArrayBuffer; 差异内容：NA | 类名：TUILable； API声明：image: ArrayBuffer; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TUILable； API声明：title: string; 差异内容：NA | 类名：TUILable； API声明：title: string; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export interface AuthToken 差异内容：NA | 类名：trustedAuthentication； API声明：export interface AuthToken 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthToken； API声明：authToken: Uint8Array; 差异内容：NA | 类名：AuthToken； API声明：authToken: Uint8Array; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export interface AuthInfo 差异内容：NA | 类名：trustedAuthentication； API声明：export interface AuthInfo 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthInfo； API声明：authToken: Uint8Array; 差异内容：NA | 类名：AuthInfo； API声明：authToken: Uint8Array; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：AuthInfo； API声明：authID: bigint; 差异内容：NA | 类名：AuthInfo； API声明：authID: bigint; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：export interface TextCheckResult 差异内容：NA | 类名：trustedAuthentication； API声明：export interface TextCheckResult 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextCheckResult； API声明：result: number; 差异内容：NA | 类名：TextCheckResult； API声明：result: number; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextCheckResult； API声明：lastIndex: number; 差异内容：NA | 类名：TextCheckResult； API声明：lastIndex: number; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise&lt;AuthToken&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise&lt;AuthToken&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise&lt;AuthToken&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function importData(data: ArrayBuffer, authID: bigint): Promise&lt;void&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function importData(data: ArrayBuffer, authID: bigint): Promise&lt;void&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function exportData(authID: bigint, label: TUILable): Promise&lt;ArrayBuffer&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function exportData(authID: bigint, label: TUILable): Promise&lt;ArrayBuffer&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function checkConfirmUITextFormat(text: string): Promise&lt;TextCheckResult&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function checkConfirmUITextFormat(text: string): Promise&lt;TextCheckResult&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function getRemainAuthTimes(authID: bigint): Promise&lt;number&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function getRemainAuthTimes(authID: bigint): Promise&lt;number&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
| API从不支持元服务到支持元服务 | 类名：trustedAuthentication； API声明：function disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise&lt;void&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise&lt;void&gt;; 差异内容：atomicservice | api/@hms.security.trustedAuthentication.d.ts |
