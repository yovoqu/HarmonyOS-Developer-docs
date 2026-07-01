# Device Certificate Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-7001

## Device Certificate Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：certificateManagerDialog； API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise&lt;string&gt;; 差异内容：NA | 类名：certificateManagerDialog； API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise&lt;string&gt;; 差异内容：801 | api/@ohos.security.certManagerDialog.d.ts |
| 新增错误码 | 类名：certificateManagerDialog； API声明：function openAuthorizeDialog(context: common.Context): Promise&lt;string&gt;; 差异内容：NA | 类名：certificateManagerDialog； API声明：function openAuthorizeDialog(context: common.Context): Promise&lt;string&gt;; 差异内容：801 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CERT_UNTRUSTED = 19030009 差异内容：ERR_CERT_UNTRUSTED = 19030009 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CERT_HAS_REVOKED = 19030010 差异内容：ERR_CERT_HAS_REVOKED = 19030010 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_UNKNOWN_CRITICAL_EXTENSION = 19030011 差异内容：ERR_UNKNOWN_CRITICAL_EXTENSION = 19030011 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CERT_HOSTNAME_MISMATCH = 19030012 差异内容：ERR_CERT_HOSTNAME_MISMATCH = 19030012 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CERT_EMAIL_ADDRESS_MISMATCH = 19030013 差异内容：ERR_CERT_EMAIL_ADDRESS_MISMATCH = 19030013 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CERT_KEYUSAGE_MISMATCH = 19030014 差异内容：ERR_CERT_KEYUSAGE_MISMATCH = 19030014 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CRL_NOT_FOUND = 19030015 差异内容：ERR_CRL_NOT_FOUND = 19030015 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CRL_NOT_YET_VALID = 19030016 差异内容：ERR_CRL_NOT_YET_VALID = 19030016 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CRL_HAS_EXPIRED = 19030017 差异内容：ERR_CRL_HAS_EXPIRED = 19030017 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CRL_SIGNATURE_FAILURE = 19030018 差异内容：ERR_CRL_SIGNATURE_FAILURE = 19030018 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_CRL_ISSUER_NOT_FOUND = 19030019 差异内容：ERR_CRL_ISSUER_NOT_FOUND = 19030019 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_OCSP_RESPONSE_NOT_FOUND = 19030020 差异内容：ERR_OCSP_RESPONSE_NOT_FOUND = 19030020 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_OCSP_RESPONSE_INVALID = 19030021 差异内容：ERR_OCSP_RESPONSE_INVALID = 19030021 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_OCSP_SIGNATURE_FAILURE = 19030022 差异内容：ERR_OCSP_SIGNATURE_FAILURE = 19030022 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_OCSP_CERT_STATUS_UNKNOWN = 19030023 差异内容：ERR_OCSP_CERT_STATUS_UNKNOWN = 19030023 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertResult； API声明：ERR_NETWORK_TIMEOUT = 19030024 差异内容：ERR_NETWORK_TIMEOUT = 19030024 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：enum CertRevocationFlag 差异内容：enum CertRevocationFlag | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag； API声明：CERT_REVOCATION_PREFER_OCSP = 0 差异内容：CERT_REVOCATION_PREFER_OCSP = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag； API声明：CERT_REVOCATION_CRL_CHECK = 1 差异内容：CERT_REVOCATION_CRL_CHECK = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag； API声明：CERT_REVOCATION_OCSP_CHECK = 2 差异内容：CERT_REVOCATION_OCSP_CHECK = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertRevocationFlag； API声明：CERT_REVOCATION_CHECK_ALL_CERT = 3 差异内容：CERT_REVOCATION_CHECK_ALL_CERT = 3 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：enum OcspDigest 差异内容：enum OcspDigest | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest； API声明：SHA1 = 0 差异内容：SHA1 = 0 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest； API声明：SHA224 = 1 差异内容：SHA224 = 1 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest； API声明：SHA256 = 2 差异内容：SHA256 = 2 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest； API声明：SHA384 = 3 差异内容：SHA384 = 3 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：OcspDigest； API声明：SHA512 = 4 差异内容：SHA512 = 4 | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface X509CertRevokedParams 差异内容：interface X509CertRevokedParams | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams； API声明：revocationFlags: Array&lt;CertRevocationFlag&gt;; 差异内容：revocationFlags: Array&lt;CertRevocationFlag&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams； API声明：crls?: Array&lt;X509CRL&gt;; 差异内容：crls?: Array&lt;X509CRL&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams； API声明：allowDownloadCrl?: boolean; 差异内容：allowDownloadCrl?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams； API声明：ocspResponses?: Array&lt;Uint8Array&gt;; 差异内容：ocspResponses?: Array&lt;Uint8Array&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams； API声明：allowOcspCheckOnline?: boolean; 差异内容：allowOcspCheckOnline?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertRevokedParams； API声明：ocspDigest?: OcspDigest; 差异内容：ocspDigest?: OcspDigest; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CertValidationParams 差异内容：interface CertValidationParams | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：untrustedCerts?: Array&lt;X509Cert&gt;; 差异内容：untrustedCerts?: Array&lt;X509Cert&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：trustedCerts?: Array&lt;X509Cert&gt;; 差异内容：trustedCerts?: Array&lt;X509Cert&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：trustSystemCa?: boolean; 差异内容：trustSystemCa?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：partialChain?: boolean; 差异内容：partialChain?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：allowDownloadIntermediateCa?: boolean; 差异内容：allowDownloadIntermediateCa?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：date?: string; 差异内容：date?: string; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：validateDate?: boolean; 差异内容：validateDate?: boolean; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：ignoreErrs?: Array&lt;CertResult&gt;; 差异内容：ignoreErrs?: Array&lt;CertResult&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：hostnames?: Array&lt;string&gt;; 差异内容：hostnames?: Array&lt;string&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：emailAddresses?: Array&lt;string&gt;; 差异内容：emailAddresses?: Array&lt;string&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：keyUsage?: Array&lt;KeyUsageType&gt;; 差异内容：keyUsage?: Array&lt;KeyUsageType&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：userId?: Uint8Array; 差异内容：userId?: Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationParams； API声明：revokedParams?: X509CertRevokedParams; 差异内容：revokedParams?: X509CertRevokedParams; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：cert； API声明：interface CertValidationResult 差异内容：interface CertValidationResult | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertValidationResult； API声明：readonly certChain: Array&lt;X509Cert&gt;; 差异内容：readonly certChain: Array&lt;X509Cert&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：CertChainValidator； API声明：validateCert(cert: X509Cert, params: CertValidationParams): Promise&lt;CertValidationResult&gt;; 差异内容：validateCert(cert: X509Cert, params: CertValidationParams): Promise&lt;CertValidationResult&gt;; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：X509CertMatchParameters； API声明：privateKey?: string \| Uint8Array; 差异内容：privateKey?: string \| Uint8Array; | api/@ohos.security.cert.d.ts |
| 新增API | NA | 类名：AuthorizeRequest； API声明：keyAlgIDs?: Array&lt;string&gt;; 差异内容：keyAlgIDs?: Array&lt;string&gt;; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：AuthorizeRequest； API声明：issuers?: Array&lt;Uint8Array&gt;; 差异内容：issuers?: Array&lt;Uint8Array&gt;; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：AuthorizeRequest； API声明：uri?: string; 差异内容：uri?: string; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明：function supportsCACertDialog(): boolean; 差异内容：function supportsCACertDialog(): boolean; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CMResult； API声明：uriList?: Array&lt;string&gt;; 差异内容：uriList?: Array&lt;string&gt;; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：export enum CertFileFormat 差异内容：export enum CertFileFormat | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertFileFormat； API声明：PEM_DER = 0 差异内容：PEM_DER = 0 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertFileFormat； API声明：P7B = 1 差异内容：P7B = 1 | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：export interface CertBlob 差异内容：export interface CertBlob | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertBlob； API声明：certData: Uint8Array; 差异内容：certData: Uint8Array; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertBlob； API声明：certFormat?: CertFileFormat; 差异内容：certFormat?: CertFileFormat; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：CertBlob； API声明：certScope?: CertScope; 差异内容：certScope?: CertScope; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：function installUserTrustedCertificate(certificate: CertBlob): Promise&lt;CMResult&gt;; 差异内容：function installUserTrustedCertificate(certificate: CertBlob): Promise&lt;CMResult&gt;; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise&lt;CMResult&gt;; 差异内容：function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise&lt;CMResult&gt;; | api/@ohos.security.certManager.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise&lt;void&gt;; 差异内容：function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise&lt;void&gt;; | api/@ohos.security.certManager.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：X500DistinguishedName； API声明：getName(): string; 差异内容：getName(): string; | 类名：X500DistinguishedName； API声明：getName(type: string, encodingType: EncodingType): Array&lt;string&gt;; 差异内容：getName(type: string, encodingType: EncodingType): Array&lt;string&gt;; | api/@ohos.security.cert.d.ts |
