# Distributed Service Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：distributedDeviceManager； API声明：function releaseDeviceManager(deviceManager: DeviceManager): void; 差异内容：201 | 类名：distributedDeviceManager； API声明：function releaseDeviceManager(deviceManager: DeviceManager): void; 差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 删除错误码 | 类名：DeviceManager； API声明：getAvailableDeviceListSync(): Array&lt;DeviceBasicInfo&gt;; 差异内容：401 | 类名：DeviceManager； API声明：getAvailableDeviceListSync(): Array&lt;DeviceBasicInfo&gt;; 差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 删除错误码 | 类名：DeviceManager； API声明：stopDiscovering(): void; 差异内容：11600104,401 | 类名：DeviceManager； API声明：stopDiscovering(): void; 差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 权限变更 | 类名：distributedDeviceManager； API声明：function releaseDeviceManager(deviceManager: DeviceManager): void; 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：distributedDeviceManager； API声明：function releaseDeviceManager(deviceManager: DeviceManager): void; 差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace abilityConnectionManager 差异内容：declare namespace abilityConnectionManager | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：interface PeerInfo 差异内容：interface PeerInfo | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo； API声明：deviceId: string; 差异内容：deviceId: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo； API声明：bundleName: string; 差异内容：bundleName: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo； API声明：moduleName: string; 差异内容：moduleName: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo； API声明：abilityName: string; 差异内容：abilityName: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo； API声明：serviceName?: string; 差异内容：serviceName?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：interface ConnectOptions 差异内容：interface ConnectOptions | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectOptions； API声明：needSendData?: boolean; 差异内容：needSendData?: boolean; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectOptions； API声明：startOptions?: StartOptionParams; 差异内容：startOptions?: StartOptionParams; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectOptions； API声明：parameters?: Record<string, string>; 差异内容：parameters?: Record<string, string>; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：interface ConnectResult 差异内容：interface ConnectResult | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectResult； API声明：isConnected: boolean; 差异内容：isConnected: boolean; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectResult； API声明：errorCode?: ConnectErrorCode; 差异内容：errorCode?: ConnectErrorCode; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectResult； API声明：reason?: string; 差异内容：reason?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：export enum ConnectErrorCode 差异内容：export enum ConnectErrorCode | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode； API声明：CONNECTED_SESSION_EXISTS = 0 差异内容：CONNECTED_SESSION_EXISTS = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode； API声明：PEER_APP_REJECTED = 1 差异内容：PEER_APP_REJECTED = 1 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode； API声明：LOCAL_WIFI_NOT_OPEN = 2 差异内容：LOCAL_WIFI_NOT_OPEN = 2 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode； API声明：PEER_WIFI_NOT_OPEN = 3 差异内容：PEER_WIFI_NOT_OPEN = 3 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode； API声明：PEER_ABILITY_NO_ONCOLLABORATE = 4 差异内容：PEER_ABILITY_NO_ONCOLLABORATE = 4 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode； API声明：SYSTEM_INTERNAL_ERROR = 5 差异内容：SYSTEM_INTERNAL_ERROR = 5 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：export enum StartOptionParams 差异内容：export enum StartOptionParams | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：StartOptionParams； API声明：START_IN_FOREGROUND = 0 差异内容：START_IN_FOREGROUND = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：interface EventCallbackInfo 差异内容：interface EventCallbackInfo | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo； API声明：sessionId: number; 差异内容：sessionId: number; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo； API声明：eventType: string; 差异内容：eventType: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo； API声明：reason?: DisconnectReason; 差异内容：reason?: DisconnectReason; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo； API声明：msg?: string; 差异内容：msg?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo； API声明：data?: ArrayBuffer; 差异内容：data?: ArrayBuffer; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：interface CollaborateEventInfo 差异内容：interface CollaborateEventInfo | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventInfo； API声明：sessionId: number; 差异内容：sessionId: number; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventInfo； API声明：eventType: CollaborateEventType; 差异内容：eventType: CollaborateEventType; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventInfo； API声明：eventMsg?: string; 差异内容：eventMsg?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：enum CollaborateEventType 差异内容：enum CollaborateEventType | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventType； API声明：SEND_FAILURE = 0 差异内容：SEND_FAILURE = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventType； API声明：COLOR_SPACE_CONVERSION_FAILURE = 1 差异内容：COLOR_SPACE_CONVERSION_FAILURE = 1 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：enum DisconnectReason 差异内容：enum DisconnectReason | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：DisconnectReason； API声明：PEER_APP_CLOSE_COLLABORATION = 0 差异内容：PEER_APP_CLOSE_COLLABORATION = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：DisconnectReason； API声明：PEER_APP_EXIT = 1 差异内容：PEER_APP_EXIT = 1 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：DisconnectReason； API声明：NETWORK_DISCONNECTED = 2 差异内容：NETWORK_DISCONNECTED = 2 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function on(type: 'connect', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function on(type: 'connect', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function off(type: 'connect', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function off(type: 'connect', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function on(type: 'disconnect', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function on(type: 'disconnect', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function off(type: 'disconnect', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function off(type: 'disconnect', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function on(type: 'receiveMessage', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function on(type: 'receiveMessage', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function off(type: 'receiveMessage', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function off(type: 'receiveMessage', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function on(type: 'receiveData', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function on(type: 'receiveData', sessionId: number, callback: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function off(type: 'receiveData', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; 差异内容：function off(type: 'receiveData', sessionId: number, callback?: Callback&lt;EventCallbackInfo&gt;): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo, connectOptions: ConnectOptions): number; 差异内容：function createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo, connectOptions: ConnectOptions): number; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function destroyAbilityConnectionSession(sessionId: number): void; 差异内容：function destroyAbilityConnectionSession(sessionId: number): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function getPeerInfoById(sessionId: number): PeerInfo \| undefined; 差异内容：function getPeerInfoById(sessionId: number): PeerInfo \| undefined; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function connect(sessionId: number): Promise&lt;ConnectResult&gt;; 差异内容：function connect(sessionId: number): Promise&lt;ConnectResult&gt;; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function disconnect(sessionId: number): void; 差异内容：function disconnect(sessionId: number): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function acceptConnect(sessionId: number, token: string): Promise&lt;void&gt;; 差异内容：function acceptConnect(sessionId: number, token: string): Promise&lt;void&gt;; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function reject(token: string, reason: string): void; 差异内容：function reject(token: string, reason: string): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function sendMessage(sessionId: number, msg: string): Promise&lt;void&gt;; 差异内容：function sendMessage(sessionId: number, msg: string): Promise&lt;void&gt;; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：function sendData(sessionId: number, data: ArrayBuffer): Promise&lt;void&gt;; 差异内容：function sendData(sessionId: number, data: ArrayBuffer): Promise&lt;void&gt;; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：export enum CollaborationKeys 差异内容：export enum CollaborationKeys | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationKeys； API声明：PEER_INFO = 'ohos.collaboration.key.peerInfo' 差异内容：PEER_INFO = 'ohos.collaboration.key.peerInfo' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationKeys； API声明：CONNECT_OPTIONS = 'ohos.collaboration.key.connectOptions' 差异内容：CONNECT_OPTIONS = 'ohos.collaboration.key.connectOptions' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationKeys； API声明：COLLABORATE_TYPE = 'ohos.collaboration.key.abilityCollaborateType' 差异内容：COLLABORATE_TYPE = 'ohos.collaboration.key.abilityCollaborateType' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager； API声明：export enum CollaborationValues 差异内容：export enum CollaborationValues | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationValues； API声明：ABILITY_COLLABORATION_TYPE_DEFAULT = 'ohos.collaboration.value.abilityCollab' 差异内容：ABILITY_COLLABORATION_TYPE_DEFAULT = 'ohos.collaboration.value.abilityCollab' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationValues； API声明：ABILITY_COLLABORATION_TYPE_CONNECT_PROXY = 'ohos.collaboration.value.connectProxy' 差异内容：ABILITY_COLLABORATION_TYPE_CONNECT_PROXY = 'ohos.collaboration.value.connectProxy' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.distributedsched.abilityConnectionManager.d.ts 差异内容：DistributedServiceKit | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
