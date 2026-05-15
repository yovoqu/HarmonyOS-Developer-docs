# Wear Engine Kit

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-wearengine-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：wearEngine； API声明：enum EntryType 差异内容：enum EntryType | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：EntryType； API声明：DISTRIBUTED_SERVICE = 'DistributedService' 差异内容：DISTRIBUTED_SERVICE = 'DistributedService' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：EntryType； API声明：SERVICE = 'Service' 差异内容：SERVICE = 'Service' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：EntryType； API声明：UI = 'UI' 差异内容：UI = 'UI' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pFile； API声明：progress?: number; 差异内容：progress?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：interface StartConfig 差异内容：interface StartConfig | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：StartConfig； API声明：entryType: EntryType; 差异内容：entryType: EntryType; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：StartConfig； API声明：entryName?: string; 差异内容：entryName?: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：registerFileReceiverWithProgress(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>; 差异内容：registerFileReceiverWithProgress(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorItem； API声明：SPORT_STATUS = 'sportStatus' 差异内容：SPORT_STATUS = 'sportStatus' | api/@hms.health.wearEngine.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：P2pClient； API声明：startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise<P2pResult>; 差异内容：startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise<P2pResult>; | 类名：P2pClient； API声明：startRemoteApp(deviceRandomId: string, remoteApp: AppInfo, startConfig: StartConfig): Promise<P2pResult>; 差异内容：startRemoteApp(deviceRandomId: string, remoteApp: AppInfo, startConfig: StartConfig): Promise<P2pResult>; | api/@hms.health.wearEngine.d.ts |
