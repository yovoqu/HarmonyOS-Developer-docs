# MDM Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：browser； API声明：function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void; 差异内容：function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：browser； API声明：function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer; 差异内容：function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：browser； API声明：function getSelfManagedBrowserPolicyVersion(): string; 差异内容：function getSelfManagedBrowserPolicyVersion(): string; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：browser； API声明：function getSelfManagedBrowserPolicy(): ArrayBuffer; 差异内容：function getSelfManagedBrowserPolicy(): ArrayBuffer; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：Direction； API声明：FORWARD = 2 差异内容：FORWARD = 2 | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：Action； API声明：REJECT = 2 差异内容：REJECT = 2 | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：DomainFilterRule； API声明：direction?: Direction; 差异内容：direction?: Direction; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：networkManager； API声明：function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void; 差异内容：function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：networkManager； API声明：function getGlobalProxyForAccount(admin: Want, accountId: number): connection.HttpProxy; 差异内容：function getGlobalProxyForAccount(admin: Want, accountId: number): connection.HttpProxy; | api/@ohos.enterprise.networkManager.d.ts |
