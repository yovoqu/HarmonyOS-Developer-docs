# Device Certificate Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-b123sp18

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：CertificateDialogErrorCode； API声明：ERROR_OPERATION_CANCELED = 29700002 差异内容：ERROR_OPERATION_CANCELED = 29700002 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode； API声明：ERROR_OPERATION_FAILED = 29700003 差异内容：ERROR_OPERATION_FAILED = 29700003 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode； API声明：ERROR_DEVICE_NOT_SUPPORTED = 29700004 差异内容：ERROR_DEVICE_NOT_SUPPORTED = 29700004 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明： export enum CertificateType 差异内容： export enum CertificateType | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateType； API声明：CA_CERT = 1 差异内容：CA_CERT = 1 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明： export enum CertificateScope 差异内容： export enum CertificateScope | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateScope； API声明：CURRENT_USER = 1 差异内容：CURRENT_USER = 1 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise&lt;string&gt;; 差异内容：function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise&lt;string&gt;; | api/@ohos.security.certManagerDialog.d.ts |
