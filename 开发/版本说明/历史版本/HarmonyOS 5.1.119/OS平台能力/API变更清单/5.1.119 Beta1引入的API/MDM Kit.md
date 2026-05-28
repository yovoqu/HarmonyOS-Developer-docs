# MDM Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：accountManager； API声明：interface DomainAccountPolicy 差异内容：NA | 类名：accountManager； API声明：interface DomainAccountPolicy 差异内容：stagemodelonly | api/@ohos.enterprise.accountManager.d.ts |
| API模型切换 | 类名：DomainAccountPolicy； API声明：authenticationValidityPeriod?: number; 差异内容：NA | 类名：DomainAccountPolicy； API声明：authenticationValidityPeriod?: number; 差异内容：stagemodelonly | api/@ohos.enterprise.accountManager.d.ts |
| API模型切换 | 类名：DomainAccountPolicy； API声明：passwordValidityPeriod?: number; 差异内容：NA | 类名：DomainAccountPolicy； API声明：passwordValidityPeriod?: number; 差异内容：stagemodelonly | api/@ohos.enterprise.accountManager.d.ts |
| API模型切换 | 类名：DomainAccountPolicy； API声明：passwordExpirationNotification?: number; 差异内容：NA | 类名：DomainAccountPolicy； API声明：passwordExpirationNotification?: number; 差异内容：stagemodelonly | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：accountManager； API声明：interface DomainAccountPolicy 差异内容：interface DomainAccountPolicy | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：DomainAccountPolicy； API声明：authenticationValidityPeriod?: number; 差异内容：authenticationValidityPeriod?: number; | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：DomainAccountPolicy； API声明：passwordValidityPeriod?: number; 差异内容：passwordValidityPeriod?: number; | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：DomainAccountPolicy； API声明：passwordExpirationNotification?: number; 差异内容：passwordExpirationNotification?: number; | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：accountManager； API声明：function setDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo, policy: DomainAccountPolicy): void; 差异内容：function setDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo, policy: DomainAccountPolicy): void; | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：accountManager； API声明：function getDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo): DomainAccountPolicy; 差异内容：function getDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo): DomainAccountPolicy; | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：systemManager； API声明：function getUpdateAuthData(admin: Want): Promise&lt;string&gt;; 差异内容：function getUpdateAuthData(admin: Want): Promise&lt;string&gt;; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：interface WifiAccessInfo 差异内容：interface WifiAccessInfo | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：WifiAccessInfo； API声明：ssid: string; 差异内容：ssid: string; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：WifiAccessInfo； API声明：bssid?: string; 差异内容：bssid?: string; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function addDisallowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; 差异内容：function addDisallowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function removeDisallowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; 差异内容：function removeDisallowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function getDisallowedWifiList(admin: Want): Array&lt;WifiAccessInfo&gt;; 差异内容：function getDisallowedWifiList(admin: Want): Array&lt;WifiAccessInfo&gt;; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function addAllowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; 差异内容：function addAllowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function removeAllowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; 差异内容：function removeAllowedWifiList(admin: Want, list: Array&lt;WifiAccessInfo&gt;): void; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function getAllowedWifiList(admin: Want): Array&lt;WifiAccessInfo&gt;; 差异内容：function getAllowedWifiList(admin: Want): Array&lt;WifiAccessInfo&gt;; | api/@ohos.enterprise.wifiManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：InstallParam； API声明：parameters?: Record<string, string>; 差异内容：parameters?: Record<string, string>; | api/@ohos.enterprise.bundleManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：UpdatePackageInfo； API声明：authInfo?: string; 差异内容：authInfo?: string; | api/@ohos.enterprise.systemManager.d.ts |
