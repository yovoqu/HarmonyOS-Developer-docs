# Online Authentication Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-onlineauthenticationkit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace fido2 差异内容：declare namespace fido2 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticatorAttestationResponse 差异内容：interface AuthenticatorAttestationResponse | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponse； API声明：readonly attestationObject: Uint8Array; 差异内容：readonly attestationObject: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponse； API声明：readonly clientDataJson: Uint8Array; 差异内容：readonly clientDataJson: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponse； API声明：publicKeyAlgorithm: Algorithm; 差异内容：publicKeyAlgorithm: Algorithm; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponse； API声明：publicKey?: Uint8Array; 差异内容：publicKey?: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponse； API声明：authenticatorData: Uint8Array; 差异内容：authenticatorData: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponse； API声明：transports: string[]; 差异内容：transports: string[]; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticatorAttestationResponseJson 差异内容：interface AuthenticatorAttestationResponseJson | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponseJson； API声明：clientDataJson: string; 差异内容：clientDataJson: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponseJson； API声明：authenticatorData: string; 差异内容：authenticatorData: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponseJson； API声明：transports: Array&lt;string&gt;; 差异内容：transports: Array&lt;string&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponseJson； API声明：publicKey?: string; 差异内容：publicKey?: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponseJson； API声明：publicKeyAlgorithm: Algorithm; 差异内容：publicKeyAlgorithm: Algorithm; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttestationResponseJson； API声明：attestationObject: string; 差异内容：attestationObject: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticationExtensionsClientOutputsJson 差异内容：interface AuthenticationExtensionsClientOutputsJson | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticatorAssertionResponseJson 差异内容：interface AuthenticatorAssertionResponseJson | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponseJson； API声明：clientDataJson: string; 差异内容：clientDataJson: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponseJson； API声明：authenticatorData: string; 差异内容：authenticatorData: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponseJson； API声明：signature: string; 差异内容：signature: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponseJson； API声明：userHandle?: string; 差异内容：userHandle?: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticatorAssertionResponse 差异内容：interface AuthenticatorAssertionResponse | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponse； API声明：readonly authenticatorData: Uint8Array; 差异内容：readonly authenticatorData: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponse； API声明：readonly signature: Uint8Array; 差异内容：readonly signature: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponse； API声明：readonly userHandle?: Uint8Array; 差异内容：readonly userHandle?: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAssertionResponse； API声明：readonly clientDataJson: Uint8Array; 差异内容：readonly clientDataJson: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticationExtensionsClientOutputs 差异内容：interface AuthenticationExtensionsClientOutputs | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyAttestationCredential 差异内容：interface PublicKeyAttestationCredential | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAttestationCredential； API声明：readonly rawId: Uint8Array; 差异内容：readonly rawId: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAttestationCredential； API声明：readonly response: AuthenticatorAttestationResponse; 差异内容：readonly response: AuthenticatorAttestationResponse; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAttestationCredential； API声明：readonly authenticatorAttachment?: AuthenticatorAttachment; 差异内容：readonly authenticatorAttachment?: AuthenticatorAttachment; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAttestationCredential； API声明：readonly id: string; 差异内容：readonly id: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAttestationCredential； API声明：readonly type: string; 差异内容：readonly type: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAttestationCredential； API声明：readonly clientExtensionResults: AuthenticationExtensionsClientOutputs; 差异内容：readonly clientExtensionResults: AuthenticationExtensionsClientOutputs; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAttestationCredential； API声明：registrationResponseJson: RegistrationResponseJson; 差异内容：registrationResponseJson: RegistrationResponseJson; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface RegistrationResponseJson 差异内容：interface RegistrationResponseJson | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：RegistrationResponseJson； API声明：id: string; 差异内容：id: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：RegistrationResponseJson； API声明：rawId: string; 差异内容：rawId: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：RegistrationResponseJson； API声明：response: AuthenticatorAttestationResponseJson; 差异内容：response: AuthenticatorAttestationResponseJson; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：RegistrationResponseJson； API声明：authenticatorAttachment?: string; 差异内容：authenticatorAttachment?: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：RegistrationResponseJson； API声明：clientExtensionResults: AuthenticationExtensionsClientOutputsJson; 差异内容：clientExtensionResults: AuthenticationExtensionsClientOutputsJson; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：RegistrationResponseJson； API声明：type: string; 差异内容：type: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyCredentialRequestOptions 差异内容：interface PublicKeyCredentialRequestOptions | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRequestOptions； API声明：challenge: Uint8Array; 差异内容：challenge: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRequestOptions； API声明：timeout?: number; 差异内容：timeout?: number; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRequestOptions； API声明：rpId?: string; 差异内容：rpId?: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRequestOptions； API声明：allowCredentials?: Array&lt;PublicKeyCredentialDescriptor&gt;; 差异内容：allowCredentials?: Array&lt;PublicKeyCredentialDescriptor&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRequestOptions； API声明：userVerification?: UserVerificationRequirement; 差异内容：userVerification?: UserVerificationRequirement; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRequestOptions； API声明：hints?: Array&lt;PublicKeyCredentialHint&gt;; 差异内容：hints?: Array&lt;PublicKeyCredentialHint&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRequestOptions； API声明：extensions?: Map<string, Object>; 差异内容：extensions?: Map<string, Object>; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyAssertionCredential 差异内容：interface PublicKeyAssertionCredential | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAssertionCredential； API声明：readonly rawId: Uint8Array; 差异内容：readonly rawId: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAssertionCredential； API声明：readonly response: AuthenticatorAssertionResponse; 差异内容：readonly response: AuthenticatorAssertionResponse; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAssertionCredential； API声明：readonly authenticatorAttachment?: AuthenticatorAttachment; 差异内容：readonly authenticatorAttachment?: AuthenticatorAttachment; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAssertionCredential； API声明：readonly id: string; 差异内容：readonly id: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAssertionCredential； API声明：readonly type: string; 差异内容：readonly type: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAssertionCredential； API声明：clientExtensionResults: AuthenticationExtensionsClientOutputs; 差异内容：clientExtensionResults: AuthenticationExtensionsClientOutputs; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyAssertionCredential； API声明：authenticationResponseJson: AuthenticationResponseJson; 差异内容：authenticationResponseJson: AuthenticationResponseJson; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticationResponseJson 差异内容：interface AuthenticationResponseJson | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticationResponseJson； API声明：id: string; 差异内容：id: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticationResponseJson； API声明：rawId: string; 差异内容：rawId: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticationResponseJson； API声明：response: AuthenticatorAssertionResponseJson; 差异内容：response: AuthenticatorAssertionResponseJson; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticationResponseJson； API声明：authenticatorAttachment?: string; 差异内容：authenticatorAttachment?: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticationResponseJson； API声明：clientExtensionResults: AuthenticationExtensionsClientOutputsJson; 差异内容：clientExtensionResults: AuthenticationExtensionsClientOutputsJson; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticationResponseJson； API声明：type: string; 差异内容：type: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum CredentialMediationRequirement 差异内容：enum CredentialMediationRequirement | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialMediationRequirement； API声明：SILENT = 'silent' 差异内容：SILENT = 'silent' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialMediationRequirement； API声明：OPTIONAL = 'optional' 差异内容：OPTIONAL = 'optional' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialMediationRequirement； API声明：CONDITIONAL = 'conditional' 差异内容：CONDITIONAL = 'conditional' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialMediationRequirement； API声明：REQUIRED = 'required' 差异内容：REQUIRED = 'required' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface CredentialCreationOptions 差异内容：interface CredentialCreationOptions | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialCreationOptions； API声明：mediation?: CredentialMediationRequirement; 差异内容：mediation?: CredentialMediationRequirement; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialCreationOptions； API声明：publicKey: PublicKeyCredentialCreationOptions; 差异内容：publicKey: PublicKeyCredentialCreationOptions; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface CredentialRequestOptions 差异内容：interface CredentialRequestOptions | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialRequestOptions； API声明：mediation?: CredentialMediationRequirement; 差异内容：mediation?: CredentialMediationRequirement; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：CredentialRequestOptions； API声明：publicKey: PublicKeyCredentialRequestOptions; 差异内容：publicKey: PublicKeyCredentialRequestOptions; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum TokenBindingStatus 差异内容：enum TokenBindingStatus | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：TokenBindingStatus； API声明：PRESENT = 'present' 差异内容：PRESENT = 'present' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：TokenBindingStatus； API声明：SUPPORTED = 'supported' 差异内容：SUPPORTED = 'supported' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface TokenBinding 差异内容：interface TokenBinding | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：TokenBinding； API声明：status: TokenBindingStatus; 差异内容：status: TokenBindingStatus; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：TokenBinding； API声明：id: string; 差异内容：id: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum AttestationConveyancePreference 差异内容：enum AttestationConveyancePreference | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AttestationConveyancePreference； API声明：NONE = 'none' 差异内容：NONE = 'none' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AttestationConveyancePreference； API声明：INDIRECT = 'indirect' 差异内容：INDIRECT = 'indirect' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AttestationConveyancePreference； API声明：DIRECT = 'direct' 差异内容：DIRECT = 'direct' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AttestationConveyancePreference； API声明：ENTERPRISE = 'enterprise' 差异内容：ENTERPRISE = 'enterprise' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum UserVerificationRequirement 差异内容：enum UserVerificationRequirement | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：UserVerificationRequirement； API声明：REQUIRED = 'required' 差异内容：REQUIRED = 'required' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：UserVerificationRequirement； API声明：PREFERRED = 'preferred' 差异内容：PREFERRED = 'preferred' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：UserVerificationRequirement； API声明：DISCOURAGED = 'discouraged' 差异内容：DISCOURAGED = 'discouraged' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum ResidentKeyRequirement 差异内容：enum ResidentKeyRequirement | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ResidentKeyRequirement； API声明：DISCOURAGED = 'discouraged' 差异内容：DISCOURAGED = 'discouraged' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ResidentKeyRequirement； API声明：PREFERRED = 'preferred' 差异内容：PREFERRED = 'preferred' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ResidentKeyRequirement； API声明：REQUIRED = 'required' 差异内容：REQUIRED = 'required' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum AuthenticatorAttachment 差异内容：enum AuthenticatorAttachment | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttachment； API声明：PLATFORM = 'platform' 差异内容：PLATFORM = 'platform' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorAttachment； API声明：CROSS_PLATFORM = 'cross-platform' 差异内容：CROSS_PLATFORM = 'cross-platform' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticatorSelectionCriteria 差异内容：interface AuthenticatorSelectionCriteria | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorSelectionCriteria； API声明：authenticatorAttachment?: AuthenticatorAttachment; 差异内容：authenticatorAttachment?: AuthenticatorAttachment; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorSelectionCriteria； API声明：residentKey?: string; 差异内容：residentKey?: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorSelectionCriteria； API声明：requireResidentKey?: boolean; 差异内容：requireResidentKey?: boolean; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorSelectionCriteria； API声明：userVerification?: UserVerificationRequirement; 差异内容：userVerification?: UserVerificationRequirement; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum AuthenticatorTransport 差异内容：enum AuthenticatorTransport | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorTransport； API声明：USB = 'usb' 差异内容：USB = 'usb' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorTransport； API声明：NFC = 'nfc' 差异内容：NFC = 'nfc' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorTransport； API声明：BLE = 'ble' 差异内容：BLE = 'ble' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorTransport； API声明：SMART_CARD = 'smart-card' 差异内容：SMART_CARD = 'smart-card' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorTransport； API声明：HYBRID = 'hybrid' 差异内容：HYBRID = 'hybrid' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorTransport； API声明：INTERNAL = 'internal' 差异内容：INTERNAL = 'internal' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyCredentialDescriptor 差异内容：interface PublicKeyCredentialDescriptor | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialDescriptor； API声明：type: PublicKeyCredentialType; 差异内容：type: PublicKeyCredentialType; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialDescriptor； API声明：id: Uint8Array; 差异内容：id: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialDescriptor； API声明：transports?: Array&lt;AuthenticatorTransport&gt;; 差异内容：transports?: Array&lt;AuthenticatorTransport&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum Algorithm 差异内容：enum Algorithm | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：ES256 = -7 差异内容：ES256 = -7 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：ES384 = -35 差异内容：ES384 = -35 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：ES512 = -36 差异内容：ES512 = -36 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：RS256 = -257 差异内容：RS256 = -257 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：RS384 = -258 差异内容：RS384 = -258 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：RS512 = -259 差异内容：RS512 = -259 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：PS256 = -37 差异内容：PS256 = -37 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：PS384 = -38 差异内容：PS384 = -38 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Algorithm； API声明：PS512 = -39 差异内容：PS512 = -39 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum PublicKeyCredentialHint 差异内容：enum PublicKeyCredentialHint | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialHint； API声明：SECURITY_KEY = 'security-key' 差异内容：SECURITY_KEY = 'security-key' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialHint； API声明：CLIENT_DEVICE = 'client-device' 差异内容：CLIENT_DEVICE = 'client-device' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialHint； API声明：HYBRID = 'hybrid' 差异内容：HYBRID = 'hybrid' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum PublicKeyCredentialType 差异内容：enum PublicKeyCredentialType | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialType； API声明：PUBLIC_KEY = 'public-key' 差异内容：PUBLIC_KEY = 'public-key' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyCredentialParameters 差异内容：interface PublicKeyCredentialParameters | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialParameters； API声明：type: PublicKeyCredentialType; 差异内容：type: PublicKeyCredentialType; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialParameters； API声明：alg: Algorithm; 差异内容：alg: Algorithm; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyCredentialUserEntity 差异内容：interface PublicKeyCredentialUserEntity | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialUserEntity； API声明：id: Uint8Array; 差异内容：id: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialUserEntity； API声明：displayName: string; 差异内容：displayName: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialUserEntity； API声明：name: string; 差异内容：name: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyCredentialRpEntity 差异内容：interface PublicKeyCredentialRpEntity | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRpEntity； API声明：id?: string; 差异内容：id?: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialRpEntity； API声明：name: string; 差异内容：name: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface PublicKeyCredentialCreationOptions 差异内容：interface PublicKeyCredentialCreationOptions | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：rp: PublicKeyCredentialRpEntity; 差异内容：rp: PublicKeyCredentialRpEntity; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：user: PublicKeyCredentialUserEntity; 差异内容：user: PublicKeyCredentialUserEntity; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：challenge: Uint8Array; 差异内容：challenge: Uint8Array; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：pubKeyCredParams: Array&lt;PublicKeyCredentialParameters&gt;; 差异内容：pubKeyCredParams: Array&lt;PublicKeyCredentialParameters&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：timeout?: number; 差异内容：timeout?: number; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：excludeCredentials?: Array&lt;PublicKeyCredentialDescriptor&gt;; 差异内容：excludeCredentials?: Array&lt;PublicKeyCredentialDescriptor&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：authenticatorSelection?: AuthenticatorSelectionCriteria; 差异内容：authenticatorSelection?: AuthenticatorSelectionCriteria; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：hints?: Array&lt;PublicKeyCredentialHint&gt;; 差异内容：hints?: Array&lt;PublicKeyCredentialHint&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：attestation?: AttestationConveyancePreference; 差异内容：attestation?: AttestationConveyancePreference; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：attestationFormats?: Array&lt;string&gt;; 差异内容：attestationFormats?: Array&lt;string&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：PublicKeyCredentialCreationOptions； API声明：extensions?: Map<string, Object>; 差异内容：extensions?: Map<string, Object>; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum Uvm 差异内容：enum Uvm | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Uvm； API声明：UVM_FINGERPRINT = 2 差异内容：UVM_FINGERPRINT = 2 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Uvm； API声明：UVM_PIN = 4 差异内容：UVM_PIN = 4 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：Uvm； API声明：UVM_FACE = 16 差异内容：UVM_FACE = 16 | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：enum ClientCapability 差异内容：enum ClientCapability | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：CONDITIONAL_CREATE = 'conditionalCreate' 差异内容：CONDITIONAL_CREATE = 'conditionalCreate' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：CONDITIONAL_GET = 'conditionalGet' 差异内容：CONDITIONAL_GET = 'conditionalGet' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：HYBRID_TRANSPORT = 'hybridTransport' 差异内容：HYBRID_TRANSPORT = 'hybridTransport' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：PASSKEY_PLATFORM_AUTHENTICATOR = 'passkeyPlatformAuthenticator' 差异内容：PASSKEY_PLATFORM_AUTHENTICATOR = 'passkeyPlatformAuthenticator' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：USER_VERIFYING_PLATFORM_AUTHENTICATOR = 'userVerifyingPlatformAuthenticator' 差异内容：USER_VERIFYING_PLATFORM_AUTHENTICATOR = 'userVerifyingPlatformAuthenticator' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：RELATED_ORIGINS = 'relatedOrigins' 差异内容：RELATED_ORIGINS = 'relatedOrigins' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：SIGNAL_ALL_ACCEPTED_CREDENTIALS = 'signalAllAcceptedCredentials' 差异内容：SIGNAL_ALL_ACCEPTED_CREDENTIALS = 'signalAllAcceptedCredentials' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：SIGNAL_CURRENT_USER_DETAILS = 'signalCurrentUserDetails' 差异内容：SIGNAL_CURRENT_USER_DETAILS = 'signalCurrentUserDetails' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：ClientCapability； API声明：SIGNAL_UNKNOWN_CREDENTIAL = 'signalUnknownCredential' 差异内容：SIGNAL_UNKNOWN_CREDENTIAL = 'signalUnknownCredential' | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：interface AuthenticatorMetadata 差异内容：interface AuthenticatorMetadata | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorMetadata； API声明：readonly aaguid: string; 差异内容：readonly aaguid: string; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorMetadata； API声明：readonly uvm: Uvm; 差异内容：readonly uvm: Uvm; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：AuthenticatorMetadata； API声明：readonly isAvailable: boolean; 差异内容：readonly isAvailable: boolean; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：function getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>; 差异内容：function getClientCapabilities(context: common.Context): Promise<Map<ClientCapability, boolean>>; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：function getPlatformAuthenticators(context: common.Context): Promise<Array&lt;AuthenticatorMetadata&gt;>; 差异内容：function getPlatformAuthenticators(context: common.Context): Promise<Array&lt;AuthenticatorMetadata&gt;>; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：function register(context: common.Context, options: CredentialCreationOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAttestationCredential&gt;; 差异内容：function register(context: common.Context, options: CredentialCreationOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAttestationCredential&gt;; | api/@hms.security.fido2.d.ts |
| 新增API | NA | 类名：fido2； API声明：function authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAssertionCredential&gt;; 差异内容：function authenticate(context: common.Context, options: CredentialRequestOptions, tokenBinding?: TokenBinding): Promise&lt;PublicKeyAssertionCredential&gt;; | api/@hms.security.fido2.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.security.fido2.d.ts 差异内容：OnlineAuthenticationKit | api/@hms.security.fido2.d.ts |
