# Driver Development Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-driverdevelopmentkit-b035

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：deviceManager； API声明：function queryDevices(busType?: number): Array<Readonly<Device>>; 差异内容：22900001,401 | 类名：deviceManager； API声明：function queryDevices(busType?: number): Array<Readonly<Device>>; 差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{  deviceId: number;  remote: rpc.IRemoteObject;  }>): void; 差异内容：22900001,401 | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{  deviceId: number;  remote: rpc.IRemoteObject;  }>): void; 差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{  deviceId: number;  remote: rpc.IRemoteObject;  }>; 差异内容：22900001,401 | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{  deviceId: number;  remote: rpc.IRemoteObject;  }>; 差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void; 差异内容：22900001,401 | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void; 差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>; 差异内容：22900001,401 | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>; 差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager； API声明：function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void; 差异内容：22900001,401 | 类名：deviceManager； API声明：function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void; 差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager； API声明：function unbindDevice(deviceId: number): Promise<number>; 差异内容：22900001,401 | 类名：deviceManager； API声明：function unbindDevice(deviceId: number): Promise<number>; 差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
