# Online Authentication Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-onlineauthenticationkit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：did； API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise&lt;ImportDigitalCredentialResponse&gt;; 差异内容：NA | 类名：did； API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise&lt;ImportDigitalCredentialResponse&gt;; 差异内容：201 | api/@hms.security.did.d.ts |
| 新增错误码 | 类名：did； API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise&lt;void&gt;; 差异内容：NA | 类名：did； API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise&lt;void&gt;; 差异内容：201 | api/@hms.security.did.d.ts |
| 新增错误码 | 类名：fido； API声明：function processUAFOperation(context: common.Context, uafRequest: UAFMessage, channelBindings?: ChannelBinding): Promise&lt;UAFMessage&gt;; 差异内容：NA | 类名：fido； API声明：function processUAFOperation(context: common.Context, uafRequest: UAFMessage, channelBindings?: ChannelBinding): Promise&lt;UAFMessage&gt;; 差异内容：1005900018 | api/@hms.security.fido.d.ts |
| 新增错误码 | 类名：fido2； API声明：function getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>; 差异内容：NA | 类名：fido2； API声明：function getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>; 差异内容：1021300009 | api/@hms.security.fido2.d.ts |
| 新增错误码 | 类名：fido2； API声明：function getPlatformAuthenticators(context: common.Context): Promise<Array&lt;AuthenticatorMetadata&gt;>; 差异内容：NA | 类名：fido2； API声明：function getPlatformAuthenticators(context: common.Context): Promise<Array&lt;AuthenticatorMetadata&gt;>; 差异内容：1021300009 | api/@hms.security.fido2.d.ts |
| 新增错误码 | 类名：fido2； API声明：function authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAssertionCredential&gt;; 差异内容：NA | 类名：fido2； API声明：function authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAssertionCredential&gt;; 差异内容：1021300013 | api/@hms.security.fido2.d.ts |
| 权限变更 | 类名：did； API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise&lt;ImportDigitalCredentialResponse&gt;; 差异内容：NA | 类名：did； API声明：function importDigitalCredential(context: common.Context, importDigitalCredentialRequest: ImportDigitalCredentialRequest): Promise&lt;ImportDigitalCredentialResponse&gt;; 差异内容：ohos.permission.ACCESS_DIGITAL_IDENTITY | api/@hms.security.did.d.ts |
| 权限变更 | 类名：did； API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise&lt;void&gt;; 差异内容：NA | 类名：did； API声明：function deleteDigitalCredential(context: common.Context, did?: string, credentialId?: string): Promise&lt;void&gt;; 差异内容：ohos.permission.ACCESS_DIGITAL_IDENTITY | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：CredentialFilter； API声明：credentialCategory?: string; 差异内容：credentialCategory?: string; | api/@hms.security.did.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：EXTENSION_AUTH_TYPE_LIST = 'extension:authTypeList' 差异内容：EXTENSION_AUTH_TYPE_LIST = 'extension:authTypeList' | api/@hms.security.fido2.d.ts |
