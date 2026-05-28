# MDM Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：securityManager； API声明：function installUserCertificate(admin: Want, certificate: CertBlob, accountId: number): string; 差异内容：function installUserCertificate(admin: Want, certificate: CertBlob, accountId: number): string; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager； API声明：function setAppClipboardPolicy(admin: Want, bundleName: string, accountId: number, policy: ClipboardPolicy): void; 差异内容：function setAppClipboardPolicy(admin: Want, bundleName: string, accountId: number, policy: ClipboardPolicy): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager； API声明：function getAppClipboardPolicy(admin: Want, bundleName: string, accountId: number): string; 差异内容：function getAppClipboardPolicy(admin: Want, bundleName: string, accountId: number): string; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager； API声明：function getUserCertificates(admin: Want, accountId: number): Array&lt;string&gt;; 差异内容：function getUserCertificates(admin: Want, accountId: number): Array&lt;string&gt;; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：ManagedEvent； API声明：MANAGED_EVENT_ACCOUNT_ADDED = 5 差异内容：MANAGED_EVENT_ACCOUNT_ADDED = 5 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：ManagedEvent； API声明：MANAGED_EVENT_ACCOUNT_SWITCHED = 6 差异内容：MANAGED_EVENT_ACCOUNT_SWITCHED = 6 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：ManagedEvent； API声明：MANAGED_EVENT_ACCOUNT_REMOVED = 7 差异内容：MANAGED_EVENT_ACCOUNT_REMOVED = 7 | api/@ohos.enterprise.adminManager.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：EnterpriseAdminExtensionAbility； API声明：onAccountAdded(accountId: number): void; 差异内容：onAccountAdded(accountId: number): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：EnterpriseAdminExtensionAbility； API声明：onAccountSwitched(accountId: number): void; 差异内容：onAccountSwitched(accountId: number): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：EnterpriseAdminExtensionAbility； API声明：onAccountRemoved(accountId: number): void; 差异内容：onAccountRemoved(accountId: number): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
