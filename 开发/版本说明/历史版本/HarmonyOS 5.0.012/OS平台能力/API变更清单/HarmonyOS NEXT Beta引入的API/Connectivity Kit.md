# Connectivity Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：wifiManager； API声明：function getLinkedInfo(): Promise<WifiLinkedInfo>; 差异内容：201,202,2501000,2501001,801 | 类名：wifiManager； API声明：function getLinkedInfo(): Promise<WifiLinkedInfo>; 差异内容：201,2501000,2501001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void; 差异内容：201,202,2501000,2501001,801 | 类名：wifiManager； API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void; 差异内容：201,2501000,2501001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function isConnected(): boolean; 差异内容：201,202,2501000,801 | 类名：wifiManager； API声明：function isConnected(): boolean; 差异内容：201,2501000,801 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明： enum WifiCategory 差异内容： enum WifiCategory | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory； API声明：DEFAULT = 1 差异内容：DEFAULT = 1 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory； API声明：WIFI6 = 2 差异内容：WIFI6 = 2 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory； API声明：WIFI6_PLUS = 3 差异内容：WIFI6_PLUS = 3 | api/@ohos.wifiManager.d.ts |
