# Device Certificate Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：RevocationCheckOptions； API声明：REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE = 4 差异内容：REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE = 4 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：RevocationCheckOptions； API声明：REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT = 5 差异内容：REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT = 5 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsContentType； API声明：ENVELOPED_DATA = 1 差异内容：ENVELOPED_DATA = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：enum CmsRsaSignaturePadding 差异内容：enum CmsRsaSignaturePadding | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRsaSignaturePadding； API声明：PKCS1_PADDING = 0 差异内容：PKCS1_PADDING = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRsaSignaturePadding； API声明：PKCS1_PSS_PADDING = 1 差异内容：PKCS1_PSS_PADDING = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsSignerConfig； API声明：rsaSignaturePadding?: CmsRsaSignaturePadding; 差异内容：rsaSignaturePadding?: CmsRsaSignaturePadding; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：enum CmsKeyAgreeRecipientDigestAlgorithm 差异内容：enum CmsKeyAgreeRecipientDigestAlgorithm | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsKeyAgreeRecipientDigestAlgorithm； API声明：SHA256 = 0 差异内容：SHA256 = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsKeyAgreeRecipientDigestAlgorithm； API声明：SHA384 = 1 差异内容：SHA384 = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsKeyAgreeRecipientDigestAlgorithm； API声明：SHA512 = 2 差异内容：SHA512 = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：enum CmsRecipientEncryptionAlgorithm 差异内容：enum CmsRecipientEncryptionAlgorithm | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientEncryptionAlgorithm； API声明：AES_128_CBC = 0 差异内容：AES_128_CBC = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientEncryptionAlgorithm； API声明：AES_192_CBC = 1 差异内容：AES_192_CBC = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientEncryptionAlgorithm； API声明：AES_256_CBC = 2 差异内容：AES_256_CBC = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientEncryptionAlgorithm； API声明：AES_128_GCM = 3 差异内容：AES_128_GCM = 3 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientEncryptionAlgorithm； API声明：AES_192_GCM = 4 差异内容：AES_192_GCM = 4 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientEncryptionAlgorithm； API声明：AES_256_GCM = 5 差异内容：AES_256_GCM = 5 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CmsKeyTransRecipientInfo 差异内容：interface CmsKeyTransRecipientInfo | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsKeyTransRecipientInfo； API声明：cert: X509Cert; 差异内容：cert: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CmsKeyAgreeRecipientInfo 差异内容：interface CmsKeyAgreeRecipientInfo | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsKeyAgreeRecipientInfo； API声明：cert: X509Cert; 差异内容：cert: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsKeyAgreeRecipientInfo； API声明：digestAlgorithm?: CmsKeyAgreeRecipientDigestAlgorithm; 差异内容：digestAlgorithm?: CmsKeyAgreeRecipientDigestAlgorithm; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CmsRecipientInfo 差异内容：interface CmsRecipientInfo | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientInfo； API声明：keyTransInfo?: CmsKeyTransRecipientInfo; 差异内容：keyTransInfo?: CmsKeyTransRecipientInfo; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsRecipientInfo； API声明：keyAgreeInfo?: CmsKeyAgreeRecipientInfo; 差异内容：keyAgreeInfo?: CmsKeyAgreeRecipientInfo; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGenerator； API声明：setRecipientEncryptionAlgorithm(algorithm: CmsRecipientEncryptionAlgorithm): void; 差异内容：setRecipientEncryptionAlgorithm(algorithm: CmsRecipientEncryptionAlgorithm): void; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGenerator； API声明：addRecipientInfo(recipientInfo: CmsRecipientInfo): Promise<void>; 差异内容：addRecipientInfo(recipientInfo: CmsRecipientInfo): Promise<void>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsGenerator； API声明：getEncryptedContentData(): Promise<Uint8Array>; 差异内容：getEncryptedContentData(): Promise<Uint8Array>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CmsVerificationConfig 差异内容：interface CmsVerificationConfig | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsVerificationConfig； API声明：trustCerts: Array<X509Cert>; 差异内容：trustCerts: Array<X509Cert>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsVerificationConfig； API声明：signerCerts?: Array<X509Cert>; 差异内容：signerCerts?: Array<X509Cert>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsVerificationConfig； API声明：contentData?: Uint8Array; 差异内容：contentData?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsVerificationConfig； API声明：contentDataFormat?: CmsContentDataFormat; 差异内容：contentDataFormat?: CmsContentDataFormat; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CmsEnvelopedDecryptionConfig 差异内容：interface CmsEnvelopedDecryptionConfig | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsEnvelopedDecryptionConfig； API声明：keyInfo?: PrivateKeyInfo; 差异内容：keyInfo?: PrivateKeyInfo; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsEnvelopedDecryptionConfig； API声明：cert?: X509Cert; 差异内容：cert?: X509Cert; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsEnvelopedDecryptionConfig； API声明：encryptedContentData?: Uint8Array; 差异内容：encryptedContentData?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsEnvelopedDecryptionConfig； API声明：contentDataFormat?: CmsContentDataFormat; 差异内容：contentDataFormat?: CmsContentDataFormat; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：enum CmsCertType 差异内容：enum CmsCertType | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsCertType； API声明：SIGNER_CERTS = 0 差异内容：SIGNER_CERTS = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsCertType； API声明：ALL_CERTS = 1 差异内容：ALL_CERTS = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CmsParser 差异内容：interface CmsParser | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsParser； API声明：setRawData(data: Uint8Array \| string, cmsFormat: CmsFormat): Promise<void>; 差异内容：setRawData(data: Uint8Array \| string, cmsFormat: CmsFormat): Promise<void>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsParser； API声明：getContentType(): CmsContentType; 差异内容：getContentType(): CmsContentType; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsParser； API声明：verifySignedData(config: CmsVerificationConfig): Promise<void>; 差异内容：verifySignedData(config: CmsVerificationConfig): Promise<void>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsParser； API声明：getContentData(): Promise<Uint8Array>; 差异内容：getContentData(): Promise<Uint8Array>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsParser； API声明：getCerts(type: CmsCertType): Promise<Array<X509Cert>>; 差异内容：getCerts(type: CmsCertType): Promise<Array<X509Cert>>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CmsParser； API声明：decryptEnvelopedData(config: CmsEnvelopedDecryptionConfig): Promise<Uint8Array>; 差异内容：decryptEnvelopedData(config: CmsEnvelopedDecryptionConfig): Promise<Uint8Array>; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：function createCmsParser(): CmsParser; 差异内容：function createCmsParser(): CmsParser; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CMErrorCode； API声明：CM_ERROR_ACCESS_UKEY_SERVICE_FAILED = 17500010 差异内容：CM_ERROR_ACCESS_UKEY_SERVICE_FAILED = 17500010 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMErrorCode； API声明：CM_ERROR_PARAMETER_VALIDATION_FAILED = 17500011 差异内容：CM_ERROR_PARAMETER_VALIDATION_FAILED = 17500011 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：Credential； API声明：certPurpose?: CertificatePurpose; 差异内容：certPurpose?: CertificatePurpose; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CMResult； API声明：credentialDetailList?: Array<Credential>; 差异内容：credentialDetailList?: Array<Credential>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：export enum CertificatePurpose 差异内容：export enum CertificatePurpose | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertificatePurpose； API声明：PURPOSE_DEFAULT = 0 差异内容：PURPOSE_DEFAULT = 0 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertificatePurpose； API声明：PURPOSE_ALL = 1 差异内容：PURPOSE_ALL = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertificatePurpose； API声明：PURPOSE_SIGN = 2 差异内容：PURPOSE_SIGN = 2 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertificatePurpose； API声明：PURPOSE_ENCRYPT = 3 差异内容：PURPOSE_ENCRYPT = 3 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：function getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>; 差异内容：function getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：export interface UkeyInfo 差异内容：export interface UkeyInfo | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：UkeyInfo； API声明：certPurpose?: CertificatePurpose; 差异内容：certPurpose?: CertificatePurpose; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode； API声明：ERROR_PARAMETER_VALIDATION_FAILED = 29700006 差异内容：ERROR_PARAMETER_VALIDATION_FAILED = 29700006 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode； API声明：ERROR_NO_AVAILABLE_CERTIFICATE = 29700007 差异内容：ERROR_NO_AVAILABLE_CERTIFICATE = 29700007 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateType； API声明：CREDENTIAL_USER = 2 差异内容：CREDENTIAL_USER = 2 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateType； API声明：CREDENTIAL_APP = 3 差异内容：CREDENTIAL_APP = 3 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateType； API声明：CREDENTIAL_UKEY = 4 差异内容：CREDENTIAL_UKEY = 4 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明：export interface AuthorizeRequest 差异内容：export interface AuthorizeRequest | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：AuthorizeRequest； API声明：certTypes: Array<CertificateType>; 差异内容：certTypes: Array<CertificateType>; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：AuthorizeRequest； API声明：certPurpose?: certificateManager.CertificatePurpose; 差异内容：certPurpose?: certificateManager.CertificatePurpose; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明：export interface CertReference 差异内容：export interface CertReference | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertReference； API声明：certType: CertificateType; 差异内容：certType: CertificateType; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertReference； API声明：keyUri: string; 差异内容：keyUri: string; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明：function openUkeyAuthDialog(context: common.Context, ukeyAuthRequest: UkeyAuthRequest): Promise<void>; 差异内容：function openUkeyAuthDialog(context: common.Context, ukeyAuthRequest: UkeyAuthRequest): Promise<void>; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明：export interface UkeyAuthRequest 差异内容：export interface UkeyAuthRequest | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：UkeyAuthRequest； API声明：keyUri: string; 差异内容：keyUri: string; | api/@ohos.security.certManagerDialog.d.ts |
