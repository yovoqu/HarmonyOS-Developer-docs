# MDM Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：usbManager； API声明：function setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void; 差异内容：ohos.permission.ENTERPRISE_MANAGE_USB | 类名：usbManager； API声明：function setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void; 差异内容：ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS | api/@ohos.enterprise.usbManager.d.ts |
| 权限变更 | 类名：usbManager； API声明：function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy; 差异内容：ohos.permission.ENTERPRISE_MANAGE_USB | 类名：usbManager； API声明：function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy; 差异内容：ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：bluetoothManager； API声明：function addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array&lt;Protocol&gt;, policy: TransferPolicy): void; 差异内容：function addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array&lt;Protocol&gt;, policy: TransferPolicy): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager； API声明：function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array&lt;Protocol&gt;, policy: TransferPolicy): void; 差异内容：function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array&lt;Protocol&gt;, policy: TransferPolicy): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager； API声明：function getDisallowedBluetoothProtocols(admin: Want \| null, accountId: number, policy: TransferPolicy): Array&lt;Protocol&gt;; 差异内容：function getDisallowedBluetoothProtocols(admin: Want \| null, accountId: number, policy: TransferPolicy): Array&lt;Protocol&gt;; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager； API声明：export enum TransferPolicy 差异内容：export enum TransferPolicy | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：TransferPolicy； API声明：SEND_ONLY = 0 差异内容：SEND_ONLY = 0 | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：TransferPolicy； API声明：RECEIVE_ONLY = 1 差异内容：RECEIVE_ONLY = 1 | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：TransferPolicy； API声明：RECEIVE_SEND = 2 差异内容：RECEIVE_SEND = 2 | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：restrictions； API声明：function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void; 差异内容：function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions； API声明：function getDisallowedPolicyForAccount(admin: Want \| null, feature: FeatureForAccount, accountId: number): boolean; 差异内容：function getDisallowedPolicyForAccount(admin: Want \| null, feature: FeatureForAccount, accountId: number): boolean; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice； API声明：LOCAL_INPUT = 2 差异内容：LOCAL_INPUT = 2 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice； API声明：CORE_DUMP = 6 差异内容：CORE_DUMP = 6 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice； API声明：DISK_ERASURE = 8 差异内容：DISK_ERASURE = 8 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions； API声明：enum FeatureForAccount 差异内容：enum FeatureForAccount | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForAccount； API声明：MULTI_WINDOW = 0 差异内容：MULTI_WINDOW = 0 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForAccount； API声明：SUPER_HUB = 2 差异内容：SUPER_HUB = 2 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：ManagedEvent； API声明：MANAGED_EVENT_BUNDLE_UPDATED = 10 差异内容：MANAGED_EVENT_BUNDLE_UPDATED = 10 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：ManagedEvent； API声明：MANAGED_EVENT_POLICIES_CHANGED = 11 差异内容：MANAGED_EVENT_POLICIES_CHANGED = 11 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：interface BundleStatsInfo 差异内容：interface BundleStatsInfo | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：BundleStatsInfo； API声明：bundleName: string; 差异内容：bundleName: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：BundleStatsInfo； API声明：appIndex: number; 差异内容：appIndex: number; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：BundleStatsInfo； API声明：abilityInFgTotalTime: number; 差异内容：abilityInFgTotalTime: number; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function addAllowedNotificationBundles(admin: Want, bundleNames: Array&lt;string&gt;, accountId: number): void; 差异内容：function addAllowedNotificationBundles(admin: Want, bundleNames: Array&lt;string&gt;, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function removeAllowedNotificationBundles(admin: Want, bundleNames: Array&lt;string&gt;, accountId: number): void; 差异内容：function removeAllowedNotificationBundles(admin: Want, bundleNames: Array&lt;string&gt;, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function getAllowedNotificationBundles(admin: Want \| null, accountId: number): Array&lt;string&gt;; 差异内容：function getAllowedNotificationBundles(admin: Want \| null, accountId: number): Array&lt;string&gt;; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function queryTrafficStats(admin: Want, bundleName: string, appIndex: number, accountId: number, networkInfo: statistics.NetworkInfo): Promise<statistics.NetStatsInfo>; 差异内容：function queryTrafficStats(admin: Want, bundleName: string, appIndex: number, accountId: number, networkInfo: statistics.NetworkInfo): Promise<statistics.NetStatsInfo>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array&lt;BundleStatsInfo&gt;; 差异内容：function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array&lt;BundleStatsInfo&gt;; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function addHideLauncherIcon(admin: Want, bundleNames: Array&lt;string&gt;): void; 差异内容：function addHideLauncherIcon(admin: Want, bundleNames: Array&lt;string&gt;): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function removeHideLauncherIcon(admin: Want, bundleNames: Array&lt;string&gt;): void; 差异内容：function removeHideLauncherIcon(admin: Want, bundleNames: Array&lt;string&gt;): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function getHideLauncherIcon(admin: Want \| null): Array&lt;string&gt;; 差异内容：function getHideLauncherIcon(admin: Want \| null): Array&lt;string&gt;; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：bundleManager； API声明：interface BundleStorageStats 差异内容：interface BundleStorageStats | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleStorageStats； API声明：bundleName: string; 差异内容：bundleName: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleStorageStats； API声明：appSize: number; 差异内容：appSize: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleStorageStats； API声明：dataSize: number; 差异内容：dataSize: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager； API声明：function getInstalledBundleStorageStats(admin: Want, bundleNames: Array&lt;string&gt;, accountId: number): Promise<Array&lt;BundleStorageStats&gt;>; 差异内容：function getInstalledBundleStorageStats(admin: Want, bundleNames: Array&lt;string&gt;, accountId: number): Promise<Array&lt;BundleStorageStats&gt;>; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：common； API声明：export interface PolicyChangedEvent 差异内容：export interface PolicyChangedEvent | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent； API声明：bundleName: string; 差异内容：bundleName: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent； API声明：functionName: string; 差异内容：functionName: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent； API声明：parameters: string; 差异内容：parameters: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent； API声明：time: number; 差异内容：time: number; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：deviceSettings； API声明：enum SwitchKey 差异内容：enum SwitchKey | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey； API声明：NEARLINK = 0 差异内容：NEARLINK = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey； API声明：BLUETOOTH = 1 差异内容：BLUETOOTH = 1 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey； API声明：WIFI = 2 差异内容：WIFI = 2 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey； API声明：NFC = 3 差异内容：NFC = 3 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings； API声明：enum SwitchStatus 差异内容：enum SwitchStatus | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchStatus； API声明：ON = 0 差异内容：ON = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchStatus； API声明：OFF = 1 差异内容：OFF = 1 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchStatus； API声明：FORCE_ON = 2 差异内容：FORCE_ON = 2 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings； API声明：function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void; 差异内容：function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility； API声明：onBundleUpdated(bundleName: string, accountId: number): void; 差异内容：onBundleUpdated(bundleName: string, accountId: number): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility； API声明：onAdminPolicyChanged(event: common.PolicyChangedEvent): void; 差异内容：onAdminPolicyChanged(event: common.PolicyChangedEvent): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：securityManager； API声明：function setScreenLockDisabledForAccount(admin: Want, disable: boolean): void; 差异内容：function setScreenLockDisabledForAccount(admin: Want, disable: boolean): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager； API声明：function isScreenLockDisabledForAccount(admin: Want): boolean; 差异内容：function isScreenLockDisabledForAccount(admin: Want): boolean; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager； API声明：function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void; 差异内容：function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager； API声明：function cancelScreenWatermarkImage(admin: Want): void; 差异内容：function cancelScreenWatermarkImage(admin: Want): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：telephonyManager； API声明：function activeSim(admin: Want, slotId: number): void; 差异内容：function activeSim(admin: Want, slotId: number): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager； API声明：function deactiveSim(admin: Want, slotId: number): void; 差异内容：function deactiveSim(admin: Want, slotId: number): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager； API声明：function setDefaultData(admin: Want, slotId: number): void; 差异内容：function setDefaultData(admin: Want, slotId: number): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager； API声明：function getDefaultData(admin: Want): number; 差异内容：function getDefaultData(admin: Want): number; | api/@ohos.enterprise.telephonyManager.d.ts |
