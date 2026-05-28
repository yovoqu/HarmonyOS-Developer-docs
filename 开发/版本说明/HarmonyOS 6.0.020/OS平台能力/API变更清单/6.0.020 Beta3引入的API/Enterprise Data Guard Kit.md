# Enterprise Data Guard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：recoveryKey； API声明：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise&lt;void&gt;; 差异内容：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise&lt;void&gt;; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise&lt;EnterpriseRecoveryKeyInfo&gt;; 差异内容：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise&lt;EnterpriseRecoveryKeyInfo&gt;; | api/@hms.pcService.recoveryKeyService.d.ts |
