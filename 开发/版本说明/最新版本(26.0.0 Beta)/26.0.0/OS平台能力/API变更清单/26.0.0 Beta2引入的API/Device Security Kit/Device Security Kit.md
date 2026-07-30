# Device Security Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：trustedAuthentication； API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise&lt;AuthInfo&gt;; 差异内容：801 | api/@hms.security.trustedAuthentication.d.ts |
| 新增错误码 | 类名：trustedAuthentication； API声明：function getSecurityLevel(authID?: bigint): Promise&lt;SecurityLevel&gt;; 差异内容：NA | 类名：trustedAuthentication； API声明：function getSecurityLevel(authID?: bigint): Promise&lt;SecurityLevel&gt;; 差异内容：1019100012 | api/@hms.security.trustedAuthentication.d.ts |
| 删除错误码 | 类名：riskControlEngine； API声明：function importRiskFactors(data: ImportData): Promise&lt;void&gt;; 差异内容：1010800001 | 类名：riskControlEngine； API声明：function importRiskFactors(data: ImportData): Promise&lt;void&gt;; 差异内容：NA | api/@hms.security.riskControlEngine.d.ts |
| 删除错误码 | 类名：riskControlEngine； API声明：function getRiskControlResult(req: RiskControlDetectionRequest): Promise&lt;RiskControlDetectionResponse&gt;; 差异内容：1010800001 | 类名：riskControlEngine； API声明：function getRiskControlResult(req: RiskControlDetectionRequest): Promise&lt;RiskControlDetectionResponse&gt;; 差异内容：NA | api/@hms.security.riskControlEngine.d.ts |
| 错误码变更兼容 | 类名：safetyDetect； API声明：function queryRiskFactors(req: RiskFactorRequest): Promise&lt;RiskFactorResponse&gt;; 差异内容：1010800001,1010800004,1010800005,1010800006,1010800007,801 | 类名：safetyDetect； API声明：function queryRiskFactors(req: RiskFactorRequest): Promise&lt;RiskFactorResponse&gt;; 差异内容：1010800004,1010800005,1010800006,1010800007,1010800011,801 | api/@hms.security.safetyDetect.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace contentTrustVerify 差异内容：declare namespace contentTrustVerify | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：export enum ImageFormat 差异内容：export enum ImageFormat | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageFormat； API声明：IMAGE_TYPE_JPEG = 0 差异内容：IMAGE_TYPE_JPEG = 0 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageFormat； API声明：IMAGE_TYPE_DNG = 1 差异内容：IMAGE_TYPE_DNG = 1 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageFormat； API声明：IMAGE_TYPE_HEIF = 2 差异内容：IMAGE_TYPE_HEIF = 2 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：export enum ImageBufferFormat 差异内容：export enum ImageBufferFormat | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageBufferFormat； API声明：IMAGE_DATA_TYPE_DATAFLOW = 0 差异内容：IMAGE_DATA_TYPE_DATAFLOW = 0 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageBufferFormat； API声明：IMAGE_DATA_TYPE_URL = 1 差异内容：IMAGE_DATA_TYPE_URL = 1 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：export enum BufferType 差异内容：export enum BufferType | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：BufferType； API声明：BUFFER_TYPE_DATA = 0 差异内容：BUFFER_TYPE_DATA = 0 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：BufferType； API声明：BUFFER_TYPE_URL = 1 差异内容：BUFFER_TYPE_URL = 1 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：export enum ContentTrustCredentialsErrorCode 差异内容：export enum ContentTrustCredentialsErrorCode | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_BAD_IMAGE_TYPE = 1027200001 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_BAD_IMAGE_TYPE = 1027200001 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_OUT_OF_STORE = 1027200002 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_OUT_OF_STORE = 1027200002 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_WRONG_SIGN_CERT_PARAM = 1027200003 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_WRONG_SIGN_CERT_PARAM = 1027200003 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_CHECK_IMAGE_HASH_FAILED = 1027200004 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_CHECK_IMAGE_HASH_FAILED = 1027200004 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_SIGN_FAILED = 1027200005 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_SIGN_FAILED = 1027200005 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_VERIFY_FAILED = 1027200006 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_VERIFY_FAILED = 1027200006 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_NO_SIGN_ASSERTION = 1027200007 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_NO_SIGN_ASSERTION = 1027200007 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_NO_SIGN_MANIFEST = 1027200008 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_NO_SIGN_MANIFEST = 1027200008 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_WRONG_CERT_CHAINS = 1027200009 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_WRONG_CERT_CHAINS = 1027200009 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_PLATFORM_NOT_SUPPORTED = 1027200010 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_PLATFORM_NOT_SUPPORTED = 1027200010 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_BAD_METADATA = 1027200011 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_BAD_METADATA = 1027200011 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_CLAIM_INVALID = 1027200012 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_CLAIM_INVALID = 1027200012 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_FILE_OPERATION_FAILED = 1027200013 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_FILE_OPERATION_FAILED = 1027200013 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ContentTrustCredentialsErrorCode； API声明：CONTENT_TRUST_CREDENTIAL_ERROR_ILLEGAL_ARGUMENT = 1027200014 差异内容：CONTENT_TRUST_CREDENTIAL_ERROR_ILLEGAL_ARGUMENT = 1027200014 | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：export interface ImageAuthData 差异内容：export interface ImageAuthData | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData； API声明：buffer: Uint8Array; 差异内容：buffer: Uint8Array; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData； API声明：imageSize: number; 差异内容：imageSize: number; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData； API声明：bufferType: BufferType; 差异内容：bufferType: BufferType; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：ImageAuthData； API声明：imageFormat: ImageFormat; 差异内容：imageFormat: ImageFormat; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：function hasImageSignature(data: ImageAuthData): Promise&lt;boolean&gt;; 差异内容：function hasImageSignature(data: ImageAuthData): Promise&lt;boolean&gt;; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：function verifyImageSignature(data: ImageAuthData): Promise&lt;Uint8Array&gt;; 差异内容：function verifyImageSignature(data: ImageAuthData): Promise&lt;Uint8Array&gt;; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：contentTrustVerify； API声明：function parseImageMetadata(manifests: Uint8Array): Promise&lt;string&gt;; 差异内容：function parseImageMetadata(manifests: Uint8Array): Promise&lt;string&gt;; | api/@hms.security.MediaAuthVerify.d.ts |
| 新增API | NA | 类名：securityAudit； API声明：function newAuthClient(callback: Callback&lt;AuditEvent&gt;, configuration: AuthClientConfiguration): AuthClient; 差异内容：function newAuthClient(callback: Callback&lt;AuditEvent&gt;, configuration: AuthClientConfiguration): AuthClient; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：BLUETOOTH_INTERCEPTED = 0x03000200 差异内容：BLUETOOTH_INTERCEPTED = 0x03000200 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：DISC_BURNING = 0x0F000004 差异内容：DISC_BURNING = 0x0F000004 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：MEDIA_FILE_ACCESS = 0x0F000005 差异内容：MEDIA_FILE_ACCESS = 0x0F000005 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：ACCOUNT_MANAGEMENT = 0x10000103 差异内容：ACCOUNT_MANAGEMENT = 0x10000103 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：DEVICE_POWER_ON = 0x16000001 差异内容：DEVICE_POWER_ON = 0x16000001 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：DEVICE_POWER_OFF = 0x16000002 差异内容：DEVICE_POWER_OFF = 0x16000002 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：AUDIO_INTERFACE_ACCESS = 0x1A000001 差异内容：AUDIO_INTERFACE_ACCESS = 0x1A000001 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：VIDEO_INTERFACE_ACCESS = 0x1A000002 差异内容：VIDEO_INTERFACE_ACCESS = 0x1A000002 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：NotifyEvent； API声明：SERIAL_PORT_INTERCEPTED = 0x30000101 差异内容：SERIAL_PORT_INTERCEPTED = 0x30000101 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent； API声明：PROCESS_EXEC = 0x1C801400 差异内容：PROCESS_EXEC = 0x1C801400 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthEvent； API声明：FILE_READ_END = 0x1C801106 差异内容：FILE_READ_END = 0x1C801106 | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明：interface AuthClientConfiguration 差异内容：interface AuthClientConfiguration | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuthClientConfiguration； API声明：timeoutAuthResult: AuthResult; 差异内容：timeoutAuthResult: AuthResult; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明：function acquireAllAuthClientsInfo(): string; 差异内容：function acquireAllAuthClientsInfo(): string; | api/@hms.security.securityAudit.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.security.MediaAuthVerify.d.ts 差异内容：DeviceSecurityKit | api/@hms.security.MediaAuthVerify.d.ts |
