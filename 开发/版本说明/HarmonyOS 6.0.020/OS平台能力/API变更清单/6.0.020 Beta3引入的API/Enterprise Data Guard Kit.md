# Enterprise Data Guard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：recoveryKey； API声明：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>; 差异内容：function verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>; | api/@hms.pcService.recoveryKeyService.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>; 差异内容：function getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>; | api/@hms.pcService.recoveryKeyService.d.ts |
