# Enterprise DataGuard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace recoveryKey 差异内容： declare namespace recoveryKey | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明： export interface EnterpriseRecoveryKeyInfo 差异内容： export interface EnterpriseRecoveryKeyInfo | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo； API声明：enterpriseRecoveryKey: Uint8Array; 差异内容：enterpriseRecoveryKey: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo； API声明：exportPublicKey: Uint8Array; 差异内容：exportPublicKey: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo； API声明：iv: Uint8Array; 差异内容：iv: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：EnterpriseRecoveryKeyInfo； API声明：tag: Uint8Array; 差异内容：tag: Uint8Array; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function getAuthChallenge(): Promise&lt;Uint8Array&gt;; 差异内容：function getAuthChallenge(): Promise&lt;Uint8Array&gt;; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise&lt;number&gt;; 差异内容：function updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise&lt;number&gt;; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function getEnterpriseRecoveryKey(userId: number): Promise&lt;EnterpriseRecoveryKeyInfo&gt;; 差异内容：function getEnterpriseRecoveryKey(userId: number): Promise&lt;EnterpriseRecoveryKeyInfo&gt;; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise&lt;number&gt;; 差异内容：function deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise&lt;number&gt;; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：on(type: 'kiaCopy', callback: Callback&lt;string&gt;): void; 差异内容：on(type: 'kiaCopy', callback: Callback&lt;string&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：off(type: 'kiaCopy', callback?: Callback&lt;string&gt;): void; 差异内容：off(type: 'kiaCopy', callback?: Callback&lt;string&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：on(type: 'kiaRename', callback: Callback&lt;string&gt;): void; 差异内容：on(type: 'kiaRename', callback: Callback&lt;string&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：off(type: 'kiaRename', callback?: Callback&lt;string&gt;): void; 差异内容：off(type: 'kiaRename', callback?: Callback&lt;string&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：on(type: 'kiaCompress', callback: Callback&lt;string&gt;): void; 差异内容：on(type: 'kiaCompress', callback: Callback&lt;string&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：off(type: 'kiaCompress', callback?: Callback&lt;string&gt;): void; 差异内容：off(type: 'kiaCompress', callback?: Callback&lt;string&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：setKiaWatermarkImage(image: Uint8Array, info: string): Promise&lt;void&gt;; 差异内容：setKiaWatermarkImage(image: Uint8Array, info: string): Promise&lt;void&gt;; | api/@hms.pcService.fileGuard.d.ts |
| kit变更 | NA | EnterpriseDataGuardKit | api/@hms.pcService.recoveryKeyService.d.ts |
