# Wear Engine

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-wearengine-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace wearEngine 差异内容： declare namespace wearEngine | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum WearEngineCapability 差异内容： enum WearEngineCapability | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：WearEngineCapability； API声明：P2P_COMMUNICATION = 1 差异内容：P2P_COMMUNICATION = 1 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：WearEngineCapability； API声明：MONITOR = 2 差异内容：MONITOR = 2 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：WearEngineCapability； API声明：NOTIFICATION = 3 差异内容：NOTIFICATION = 3 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：WearEngineCapability； API声明：SENSOR = 4 差异内容：SENSOR = 4 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum DeviceCapability 差异内容： enum DeviceCapability | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：DeviceCapability； API声明：APP_INSTALLATION = 14 差异内容：APP_INSTALLATION = 14 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：DeviceCapability； API声明：CBT_I = 128 差异内容：CBT_I = 128 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum DeviceCategory 差异内容： enum DeviceCategory | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：DeviceCategory； API声明：DEFAULT = 1 差异内容：DEFAULT = 1 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：DeviceCategory； API声明：WATCH = 2 差异内容：WATCH = 2 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：DeviceCategory； API声明：BAND = 3 差异内容：BAND = 3 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：DeviceCategory； API声明：OTHER_DEVICES = 255 差异内容：OTHER_DEVICES = 255 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface Device 差异内容： interface Device | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：randomId: string; 差异内容：randomId: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：category?: DeviceCategory; 差异内容：category?: DeviceCategory; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：name?: string; 差异内容：name?: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：softwareVersion?: string; 差异内容：softwareVersion?: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：model?: string; 差异内容：model?: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：isSmartWatch?: boolean; 差异内容：isSmartWatch?: boolean; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：isWearEngineCapabilitySupported(capability: WearEngineCapability): Promise&lt;boolean&gt;; 差异内容：isWearEngineCapabilitySupported(capability: WearEngineCapability): Promise&lt;boolean&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：isDeviceCapabilitySupported(capability: DeviceCapability): Promise&lt;boolean&gt;; 差异内容：isDeviceCapabilitySupported(capability: DeviceCapability): Promise&lt;boolean&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Device； API声明：getSerialNumber(): Promise&lt;string&gt;; 差异内容：getSerialNumber(): Promise&lt;string&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface DeviceClient 差异内容： interface DeviceClient | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：DeviceClient； API声明：getConnectedDevices(): Promise<Device[]>; 差异内容：getConnectedDevices(): Promise<Device[]>; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface AppInfo 差异内容： interface AppInfo | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：AppInfo； API声明：bundleName: string; 差异内容：bundleName: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：AppInfo； API声明：fingerprint: string; 差异内容：fingerprint: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum P2pResultCode 差异内容： enum P2pResultCode | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResultCode； API声明：REMOTE_APP_NOT_INSTALLED = 200 差异内容：REMOTE_APP_NOT_INSTALLED = 200 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResultCode； API声明：REMOTE_APP_NOT_RUNNING = 201 差异内容：REMOTE_APP_NOT_RUNNING = 201 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResultCode； API声明：REMOTE_APP_RUNNING = 202 差异内容：REMOTE_APP_RUNNING = 202 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResultCode； API声明：UNKNOWN_ERROR = 203 差异内容：UNKNOWN_ERROR = 203 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResultCode； API声明：COMMUNICATION_FAILURE = 206 差异内容：COMMUNICATION_FAILURE = 206 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResultCode； API声明：COMMUNICATION_SUCCESS = 207 差异内容：COMMUNICATION_SUCCESS = 207 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface P2pResult 差异内容： interface P2pResult | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResult； API声明：code?: number; 差异内容：code?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pResult； API声明：progress?: number; 差异内容：progress?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface P2pMessage 差异内容： interface P2pMessage | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pMessage； API声明：content: Uint8Array; 差异内容：content: Uint8Array; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface P2pFile 差异内容： interface P2pFile | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pFile； API声明：file: fs.File; 差异内容：file: fs.File; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface P2pAppParam 差异内容： interface P2pAppParam | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pAppParam； API声明：remoteApp: AppInfo; 差异内容：remoteApp: AppInfo; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pAppParam； API声明：transformLocalAppInfo?: boolean; 差异内容：transformLocalAppInfo?: boolean; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface P2pClient 差异内容： interface P2pClient | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：isRemoteAppInstalled(deviceRandomId: string, remoteBundleName: string): Promise&lt;boolean&gt;; 差异内容：isRemoteAppInstalled(deviceRandomId: string, remoteBundleName: string): Promise&lt;boolean&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：getRemoteAppVersion(deviceRandomId: string, remoteBundleName: string): Promise&lt;number&gt;; 差异内容：getRemoteAppVersion(deviceRandomId: string, remoteBundleName: string): Promise&lt;number&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise&lt;P2pResult&gt;; 差异内容：startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise&lt;P2pResult&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：sendMessage(deviceRandomId: string, appParam: P2pAppParam, message: P2pMessage): Promise&lt;P2pResult&gt;; 差异内容：sendMessage(deviceRandomId: string, appParam: P2pAppParam, message: P2pMessage): Promise&lt;P2pResult&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：transferFile(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile, callback: AsyncCallback&lt;P2pResult&gt;): void; 差异内容：transferFile(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile, callback: AsyncCallback&lt;P2pResult&gt;): void; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：cancelFileTransfer(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile): Promise&lt;P2pResult&gt;; 差异内容：cancelFileTransfer(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile): Promise&lt;P2pResult&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：registerMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pMessage&gt;): Promise&lt;void&gt;; 差异内容：registerMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pMessage&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：registerFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pFile&gt;): Promise&lt;void&gt;; 差异内容：registerFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pFile&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：unregisterMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pMessage&gt;): Promise&lt;void&gt;; 差异内容：unregisterMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pMessage&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：P2pClient； API声明：unregisterFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pFile&gt;): Promise&lt;void&gt;; 差异内容：unregisterFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback&lt;P2pFile&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum MonitorItem 差异内容： enum MonitorItem | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorItem； API声明：WEAR_STATUS = 'wearStatus' 差异内容：WEAR_STATUS = 'wearStatus' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorItem； API声明：POWER_STATUS = 'powerStatus' 差异内容：POWER_STATUS = 'powerStatus' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorItem； API声明：CHARGE_STATUS = 'chargeStatus' 差异内容：CHARGE_STATUS = 'chargeStatus' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorItem； API声明：AVAILABLE_STORAGE_SPACE = 'availableStorageSpace' 差异内容：AVAILABLE_STORAGE_SPACE = 'availableStorageSpace' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorItem； API声明：POWER_MODE = 'powerMode' 差异内容：POWER_MODE = 'powerMode' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum MonitorEvent 差异内容： enum MonitorEvent | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEvent； API声明：EVENT_CONNECTION_STATUS_CHANGED = 'connectionStatus' 差异内容：EVENT_CONNECTION_STATUS_CHANGED = 'connectionStatus' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEvent； API声明：EVENT_BATTERY_LEVEL_DROPPED = 'lowPower' 差异内容：EVENT_BATTERY_LEVEL_DROPPED = 'lowPower' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEvent； API声明：EVENT_WEAR_STATUS_CHANGED = 'wearStatus' 差异内容：EVENT_WEAR_STATUS_CHANGED = 'wearStatus' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEvent； API声明：EVENT_HEART_RATE_ALARM = 'heartRateAlarm' 差异内容：EVENT_HEART_RATE_ALARM = 'heartRateAlarm' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEvent； API声明：EVENT_CHARGE_STATUS_CHANGED = 'chargeStatus' 差异内容：EVENT_CHARGE_STATUS_CHANGED = 'chargeStatus' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEvent； API声明：EVENT_POWER_MODE_CHANGED = 'powerMode' 差异内容：EVENT_POWER_MODE_CHANGED = 'powerMode' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface MonitorData 差异内容： interface MonitorData | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorData； API声明：code: number; 差异内容：code: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorData； API声明：data?: string; 差异内容：data?: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface MonitorEventData 差异内容： interface MonitorEventData | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEventData； API声明：event: MonitorEvent; 差异内容：event: MonitorEvent; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorEventData； API声明：data: MonitorData; 差异内容：data: MonitorData; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface MonitorClient 差异内容： interface MonitorClient | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorClient； API声明：queryStatus(deviceRandomId: string, item: MonitorItem): Promise&lt;MonitorData&gt;; 差异内容：queryStatus(deviceRandomId: string, item: MonitorItem): Promise&lt;MonitorData&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorClient； API声明：subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; 差异内容：subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：MonitorClient； API声明：unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; 差异内容：unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum NotificationType 差异内容： enum NotificationType | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationType； API声明：NOTIFICATION_WITHOUT_BUTTONS = 50 差异内容：NOTIFICATION_WITHOUT_BUTTONS = 50 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationType； API声明：NOTIFICATION_WITH_ONE_BUTTON = 51 差异内容：NOTIFICATION_WITH_ONE_BUTTON = 51 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationType； API声明：NOTIFICATION_WITH_TWO_BUTTONS = 52 差异内容：NOTIFICATION_WITH_TWO_BUTTONS = 52 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationType； API声明：NOTIFICATION_WITH_THREE_BUTTONS = 53 差异内容：NOTIFICATION_WITH_THREE_BUTTONS = 53 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum ButtonId 差异内容： enum ButtonId | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：ButtonId； API声明：FIRST_BUTTON = 'firstButton' 差异内容：FIRST_BUTTON = 'firstButton' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：ButtonId； API声明：SECOND_BUTTON = 'secondButton' 差异内容：SECOND_BUTTON = 'secondButton' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：ButtonId； API声明：THIRD_BUTTON = 'thirdButton' 差异内容：THIRD_BUTTON = 'thirdButton' | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface NotificationButton 差异内容： interface NotificationButton | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationButton； API声明：buttonId: ButtonId; 差异内容：buttonId: ButtonId; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationButton； API声明：content: string; 差异内容：content: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface Notification 差异内容： interface Notification | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Notification； API声明：type: NotificationType; 差异内容：type: NotificationType; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Notification； API声明：bundleName: string; 差异内容：bundleName: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Notification； API声明：title: string; 差异内容：title: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Notification； API声明：text: string; 差异内容：text: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Notification； API声明：buttons?: NotificationButton[]; 差异内容：buttons?: NotificationButton[]; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum NotificationAction 差异内容： enum NotificationAction | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationAction； API声明：NOTIFICATION_SWITCHED_TO_BACKGROUND = 0 差异内容：NOTIFICATION_SWITCHED_TO_BACKGROUND = 0 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationAction； API声明：NOTIFICATION_DELETED = 1 差异内容：NOTIFICATION_DELETED = 1 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationAction； API声明：FIRST_BUTTON_CLICKED = 2 差异内容：FIRST_BUTTON_CLICKED = 2 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationAction； API声明：SECOND_BUTTON_CLICKED = 3 差异内容：SECOND_BUTTON_CLICKED = 3 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationAction； API声明：THIRD_BUTTON_CLICKED = 4 差异内容：THIRD_BUTTON_CLICKED = 4 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum NotificationErrorCode 差异内容： enum NotificationErrorCode | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationErrorCode； API声明：INTERNAL_ERROR = 255 差异内容：INTERNAL_ERROR = 255 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface NotificationFeedback 差异内容： interface NotificationFeedback | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationFeedback； API声明：action?: NotificationAction; 差异内容：action?: NotificationAction; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationFeedback； API声明：errorCode?: number; 差异内容：errorCode?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface NotificationOptions 差异内容： interface NotificationOptions | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationOptions； API声明：notification: Notification; 差异内容：notification: Notification; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotificationOptions； API声明：onAction(feedback: NotificationFeedback): void; 差异内容：onAction(feedback: NotificationFeedback): void; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface NotifyClient 差异内容： interface NotifyClient | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：NotifyClient； API声明：notify(deviceRandomId: string, options: NotificationOptions): Promise&lt;void&gt;; 差异内容：notify(deviceRandomId: string, options: NotificationOptions): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum SensorType 差异内容： enum SensorType | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorType； API声明：ELECTROCARDIOGRAPHY = 0 差异内容：ELECTROCARDIOGRAPHY = 0 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorType； API声明：PHOTOPLETHYSMOGRAPHY = 1 差异内容：PHOTOPLETHYSMOGRAPHY = 1 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorType； API声明：ACCELEROMETER = 2 差异内容：ACCELEROMETER = 2 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorType； API声明：GYROSCOPE = 3 差异内容：GYROSCOPE = 3 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorType； API声明：MAGNETIC_FIELD = 4 差异内容：MAGNETIC_FIELD = 4 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorType； API声明：HEART_RATE = 6 差异内容：HEART_RATE = 6 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface Sensor 差异内容： interface Sensor | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Sensor； API声明：name: string; 差异内容：name: string; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Sensor； API声明：id: number; 差异内容：id: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Sensor； API声明：type: SensorType; 差异内容：type: SensorType; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Sensor； API声明：accuracy?: number; 差异内容：accuracy?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Sensor； API声明：resolution?: number; 差异内容：resolution?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Sensor； API声明：isUtcTimestampSupported: boolean; 差异内容：isUtcTimestampSupported: boolean; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface SensorData 差异内容： interface SensorData | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorData； API声明：sensorType: SensorType; 差异内容：sensorType: SensorType; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorData； API声明：data: number[]; 差异内容：data: number[]; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorData； API声明：channel?: number; 差异内容：channel?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorData； API声明：timestamp?: number; 差异内容：timestamp?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorData； API声明：utcTimestamp?: number; 差异内容：utcTimestamp?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum SensorErrorCode 差异内容： enum SensorErrorCode | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorErrorCode； API声明：DEVICE_NOT_BEING_WORN = 300 差异内容：DEVICE_NOT_BEING_WORN = 300 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorErrorCode； API声明：DEVICE_LEAD_OFF = 301 差异内容：DEVICE_LEAD_OFF = 301 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorErrorCode； API声明：SENSOR_TURNED_OFF_MANUALLY = 302 差异内容：SENSOR_TURNED_OFF_MANUALLY = 302 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorErrorCode； API声明：SENSOR_OCCUPIED = 303 差异内容：SENSOR_OCCUPIED = 303 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorErrorCode； API声明：SENSOR_NOT_SUPPORTED = 304 差异内容：SENSOR_NOT_SUPPORTED = 304 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface SensorResult 差异内容： interface SensorResult | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorResult； API声明：data?: SensorData[]; 差异内容：data?: SensorData[]; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorResult； API声明：errorCode?: number; 差异内容：errorCode?: number; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface SensorClient 差异内容： interface SensorClient | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorClient； API声明：getSensorList(deviceRandomId: string): Promise<Sensor[]>; 差异内容：getSensorList(deviceRandomId: string): Promise<Sensor[]>; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorClient； API声明：subscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback&lt;SensorResult&gt;): Promise&lt;void&gt;; 差异内容：subscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback&lt;SensorResult&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：SensorClient； API声明：unsubscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback&lt;SensorResult&gt;): Promise&lt;void&gt;; 差异内容：unsubscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback&lt;SensorResult&gt;): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： enum Permission 差异内容： enum Permission | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Permission； API声明：USER_STATUS = 2 差异内容：USER_STATUS = 2 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Permission； API声明：MOTION_SENSOR = 3 差异内容：MOTION_SENSOR = 3 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Permission； API声明：HEALTH_SENSOR = 4 差异内容：HEALTH_SENSOR = 4 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：Permission； API声明：DEVICE_IDENTIFIER = 6 差异内容：DEVICE_IDENTIFIER = 6 | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface AuthorizationBase 差异内容： interface AuthorizationBase | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：AuthorizationBase； API声明：permissions: Permission[]; 差异内容：permissions: Permission[]; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface AuthorizationRequest 差异内容： interface AuthorizationRequest | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface AuthorizationResponse 差异内容： interface AuthorizationResponse | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明： interface AuthClient 差异内容： interface AuthClient | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：AuthClient； API声明：requestAuthorization(request: AuthorizationRequest): Promise&lt;AuthorizationResponse&gt;; 差异内容：requestAuthorization(request: AuthorizationRequest): Promise&lt;AuthorizationResponse&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：AuthClient； API声明：getAuthorization(): Promise&lt;AuthorizationResponse&gt;; 差异内容：getAuthorization(): Promise&lt;AuthorizationResponse&gt;; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function getDeviceClient(context: common.Context): DeviceClient; 差异内容：function getDeviceClient(context: common.Context): DeviceClient; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function getP2pClient(context: common.Context): P2pClient; 差异内容：function getP2pClient(context: common.Context): P2pClient; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function getMonitorClient(context: common.Context): MonitorClient; 差异内容：function getMonitorClient(context: common.Context): MonitorClient; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function getNotifyClient(context: common.Context): NotifyClient; 差异内容：function getNotifyClient(context: common.Context): NotifyClient; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function getSensorClient(context: common.Context): SensorClient; 差异内容：function getSensorClient(context: common.Context): SensorClient; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function getAuthClient(context: common.Context): AuthClient; 差异内容：function getAuthClient(context: common.Context): AuthClient; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function on(type: 'serviceDie', callback: Callback&lt;void&gt;): void; 差异内容：function on(type: 'serviceDie', callback: Callback&lt;void&gt;): void; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function off(type: 'serviceDie', callback?: Callback&lt;void&gt;): void; 差异内容：function off(type: 'serviceDie', callback?: Callback&lt;void&gt;): void; | api/@hms.health.wearEngine.d.ts |
| 新增API | NA | 类名：wearEngine； API声明：function destroy(): Promise&lt;void&gt;; 差异内容：function destroy(): Promise&lt;void&gt;; | api/@hms.health.wearEngine.d.ts |
