# Connectivity Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-504

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace opp 差异内容： declare namespace opp | api/@ohos.bluetooth.opp.d.ts |
| 新增API | NA | 类名：opp； API声明：function createOppServerProfile(): OppServerProfile; 差异内容：function createOppServerProfile(): OppServerProfile; | api/@ohos.bluetooth.opp.d.ts |
| 新增API | NA | 类名：opp； API声明： interface OppServerProfile 差异内容： interface OppServerProfile | api/@ohos.bluetooth.opp.d.ts |
| 新增API | NA | 类名：connection； API声明：function getRemoteDeviceName(deviceId: string, alias?: boolean): string; 差异内容：function getRemoteDeviceName(deviceId: string, alias?: boolean): string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void; 差异内容：function connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function connectAllowedProfiles(deviceId: string): Promise<void>; 差异内容：function connectAllowedProfiles(deviceId: string): Promise<void>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：access； API声明：function addPersistentDeviceId(deviceId: string): Promise<void>; 差异内容：function addPersistentDeviceId(deviceId: string): Promise<void>; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access； API声明：function deletePersistentDeviceId(deviceId: string): Promise<void>; 差异内容：function deletePersistentDeviceId(deviceId: string): Promise<void>; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access； API声明：function getPersistentDeviceIds(): string[]; 差异内容：function getPersistentDeviceIds(): string[]; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access； API声明：function isValidRandomDeviceId(deviceId: string): boolean; 差异内容：function isValidRandomDeviceId(deviceId: string): boolean; | api/@ohos.bluetooth.access.d.ts |
| kit变更 | NA | ConnectivityKit | api/@ohos.bluetooth.opp.d.ts |
