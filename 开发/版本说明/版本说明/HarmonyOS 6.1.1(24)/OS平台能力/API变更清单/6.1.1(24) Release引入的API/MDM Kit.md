# MDM Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：systemManager； API声明：function getInstallLocalEnterpriseAppEnabled(admin: Want): boolean; 差异内容：admin: Want | 类名：systemManager； API声明：function getInstallLocalEnterpriseAppEnabled(admin: Want \| null): boolean; 差异内容：admin: Want \| null | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager； API声明：function setInstallLocalEnterpriseAppEnabledForAccount(admin: Want, isEnable: boolean, accountId: number): void; 差异内容：function setInstallLocalEnterpriseAppEnabledForAccount(admin: Want, isEnable: boolean, accountId: number): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager； API声明：function getInstallLocalEnterpriseAppEnabledForAccount(admin: Want \| null, accountId: number): boolean; 差异内容：function getInstallLocalEnterpriseAppEnabledForAccount(admin: Want \| null, accountId: number): boolean; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager； API声明：function setActivationLockDisabled(admin: Want, isDisabled: boolean, credential?: string): Promise&lt;void&gt;; 差异内容：function setActivationLockDisabled(admin: Want, isDisabled: boolean, credential?: string): Promise&lt;void&gt;; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager； API声明：function isActivationLockDisabled(admin: Want): Promise&lt;boolean&gt;; 差异内容：function isActivationLockDisabled(admin: Want): Promise&lt;boolean&gt;; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：SettingsItem； API声明：DEVICE_NAME = 0 差异内容：DEVICE_NAME = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings； API声明：enum SettingsMenu 差异内容：enum SettingsMenu | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：ACCOUNT_ID = 0 差异内容：ACCOUNT_ID = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：WIFI = 1 差异内容：WIFI = 1 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：WIFI_PROXY_SETTINGS = 2 差异内容：WIFI_PROXY_SETTINGS = 2 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：WIFI_IP_SETTINGS = 3 差异内容：WIFI_IP_SETTINGS = 3 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：BLUETOOTH = 4 差异内容：BLUETOOTH = 4 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：NETWORK = 5 差异内容：NETWORK = 5 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：MOBILE_NETWORK = 6 差异内容：MOBILE_NETWORK = 6 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SUPER_DEVICE = 7 差异内容：SUPER_DEVICE = 7 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：MORE_CONNECTIVITY_OPTIONS = 8 差异内容：MORE_CONNECTIVITY_OPTIONS = 8 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：HOME_SCREEN_STYLE = 9 差异内容：HOME_SCREEN_STYLE = 9 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：DISPLAY_BRIGHTNESS = 10 差异内容：DISPLAY_BRIGHTNESS = 10 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SOUND_VIBRATION = 11 差异内容：SOUND_VIBRATION = 11 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：NOTIFICATIONS = 12 差异内容：NOTIFICATIONS = 12 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：BIOMETRICS_PASSWORD = 13 差异内容：BIOMETRICS_PASSWORD = 13 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：APPS_AND_SERVICES = 14 差异内容：APPS_AND_SERVICES = 14 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：BATTERY = 15 差异内容：BATTERY = 15 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：STORAGE = 16 差异内容：STORAGE = 16 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：PRIVACY_AND_SECURITY = 17 差异内容：PRIVACY_AND_SECURITY = 17 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：DIGITAL_BALANCE = 18 差异内容：DIGITAL_BALANCE = 18 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SMART_ASSISTANT = 19 差异内容：SMART_ASSISTANT = 19 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：ACCESSIBILITY = 20 差异内容：ACCESSIBILITY = 20 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SYSTEM = 21 差异内容：SYSTEM = 21 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：ABOUT_DEVICE = 22 差异内容：ABOUT_DEVICE = 22 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SYSTEM_NAVIGATION = 23 差异内容：SYSTEM_NAVIGATION = 23 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：LANGUAGE_REGION = 24 差异内容：LANGUAGE_REGION = 24 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：INPUT_METHODS = 25 差异内容：INPUT_METHODS = 25 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：DATE_TIME = 26 差异内容：DATE_TIME = 26 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：DATA_CLONE = 27 差异内容：DATA_CLONE = 27 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：BACKUP_SETTINGS = 28 差异内容：BACKUP_SETTINGS = 28 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：RESET = 29 差异内容：RESET = 29 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SUPERHUB = 30 差异内容：SUPERHUB = 30 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：USER_EXPERIENCE = 31 差异内容：USER_EXPERIENCE = 31 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SCREEN_CAST = 32 差异内容：SCREEN_CAST = 32 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：PRINTERS_SCANNERS = 33 差异内容：PRINTERS_SCANNERS = 33 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：MOBILE_DATA = 34 差异内容：MOBILE_DATA = 34 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：PERSONAL_HOTSPOT = 35 差异内容：PERSONAL_HOTSPOT = 35 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SIM_MANAGEMENT = 36 差异内容：SIM_MANAGEMENT = 36 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：AIRPLANE_MODE = 37 差异内容：AIRPLANE_MODE = 37 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：MANAGE_DATA_USAGE = 38 差异内容：MANAGE_DATA_USAGE = 38 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：VPN_SETTINGS = 39 差异内容：VPN_SETTINGS = 39 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：TEXT_DISPLAY_SIZE = 40 差异内容：TEXT_DISPLAY_SIZE = 40 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：APP_DUPLICATOR = 41 差异内容：APP_DUPLICATOR = 41 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu； API声明：SEARCH = 42 差异内容：SEARCH = 42 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings； API声明：function addHiddenSettingsMenu(admin: Want, menusToHidden: Array&lt;SettingsMenu&gt;): void; 差异内容：function addHiddenSettingsMenu(admin: Want, menusToHidden: Array&lt;SettingsMenu&gt;): void; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings； API声明：function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array&lt;SettingsMenu&gt;): void; 差异内容：function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array&lt;SettingsMenu&gt;): void; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings； API声明：function getHiddenSettingsMenu(admin: Want): Array&lt;SettingsMenu&gt;; 差异内容：function getHiddenSettingsMenu(admin: Want): Array&lt;SettingsMenu&gt;; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：restrictions； API声明：enum FeatureForDevice 差异内容：enum FeatureForDevice | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice； API声明：WIFI_P2P = 0 差异内容：WIFI_P2P = 0 | api/@ohos.enterprise.restrictions.d.ts |
