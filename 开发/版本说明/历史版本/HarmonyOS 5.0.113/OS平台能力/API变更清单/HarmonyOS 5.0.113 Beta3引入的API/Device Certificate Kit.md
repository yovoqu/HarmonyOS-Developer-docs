# Device Certificate Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicecertificatekit-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace certificateManagerDialog 差异内容： declare namespace certificateManagerDialog | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明： export enum CertificateDialogErrorCode 差异内容： export enum CertificateDialogErrorCode | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogErrorCode； API声明：ERROR_GENERIC = 29700001 差异内容：ERROR_GENERIC = 29700001 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明： export enum CertificateDialogPageType 差异内容： export enum CertificateDialogPageType | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType； API声明：PAGE_MAIN = 1 差异内容：PAGE_MAIN = 1 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType； API声明：PAGE_CA_CERTIFICATE = 2 差异内容：PAGE_CA_CERTIFICATE = 2 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType； API声明：PAGE_CREDENTIAL = 3 差异内容：PAGE_CREDENTIAL = 3 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：CertificateDialogPageType； API声明：PAGE_INSTALL_CERTIFICATE = 4 差异内容：PAGE_INSTALL_CERTIFICATE = 4 | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManagerDialog； API声明：function openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise&lt;void&gt;; 差异内容：function openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise&lt;void&gt;; | api/@ohos.security.certManagerDialog.d.ts |
| 新增API | NA | 类名：certificateManager； API声明：function getPrivateCertificates(): Promise&lt;CMResult&gt;; 差异内容：function getPrivateCertificates(): Promise&lt;CMResult&gt;; | api/@ohos.security.certManager.d.ts |
