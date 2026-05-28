# Driver Development Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-driverdevelopmentkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;, callback: AsyncCallback<{ deviceId: number; remote: rpc.IRemoteObject; }>): void; 差异内容：NA | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;, callback: AsyncCallback<{ deviceId: number; remote: rpc.IRemoteObject; }>): void; 差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;): Promise<{ deviceId: number; remote: rpc.IRemoteObject; }>; 差异内容：NA | 类名：deviceManager； API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;): Promise<{ deviceId: number; remote: rpc.IRemoteObject; }>; 差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;, callback: AsyncCallback&lt;RemoteDeviceDriver&gt;): void; 差异内容：NA | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;, callback: AsyncCallback&lt;RemoteDeviceDriver&gt;): void; 差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;): Promise&lt;RemoteDeviceDriver&gt;; 差异内容：NA | 类名：deviceManager； API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;): Promise&lt;RemoteDeviceDriver&gt;; 差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager； API声明：function unbindDevice(deviceId: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：deviceManager； API声明：function unbindDevice(deviceId: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager； API声明：function unbindDevice(deviceId: number): Promise&lt;number&gt;; 差异内容：NA | 类名：deviceManager； API声明：function unbindDevice(deviceId: number): Promise&lt;number&gt;; 差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| 新增API | NA | 类名：deviceManager； API声明：function bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;): Promise&lt;RemoteDeviceDriver&gt;; 差异内容：function bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback&lt;number&gt;): Promise&lt;RemoteDeviceDriver&gt;; | api/@ohos.driver.deviceManager.d.ts |
| 新增API | NA | 类名：deviceManager； API声明：function unbindDriverWithDeviceId(deviceId: number): Promise&lt;number&gt;; 差异内容：function unbindDriverWithDeviceId(deviceId: number): Promise&lt;number&gt;; | api/@ohos.driver.deviceManager.d.ts |
