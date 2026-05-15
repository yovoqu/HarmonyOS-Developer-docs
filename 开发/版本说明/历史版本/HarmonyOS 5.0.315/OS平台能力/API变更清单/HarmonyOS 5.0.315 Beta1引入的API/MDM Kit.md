# MDM Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-5031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：restrictions； API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void; 差异内容：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS | 类名：restrictions； API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void; 差异内容：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS | api/@ohos.enterprise.restrictions.d.ts |
| 权限变更 | 类名：restrictions； API声明：function getDisallowedPolicy(admin: Want, feature: string): boolean; 差异内容：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS | 类名：restrictions； API声明：function getDisallowedPolicy(admin: Want, feature: string): boolean; 差异内容：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：adminManager； API声明： export enum AdminType 差异内容： export enum AdminType | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：AdminType； API声明：ADMIN_TYPE_BYOD = 0x02 差异内容：ADMIN_TYPE_BYOD = 0x02 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager； API声明：function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void; 差异内容：function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void; | api/@ohos.enterprise.adminManager.d.ts |
