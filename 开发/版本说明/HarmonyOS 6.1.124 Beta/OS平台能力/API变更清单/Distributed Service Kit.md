# Distributed Service Kit

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：proxyChannelManager； API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>; 差异内容：NA | 类名：proxyChannelManager； API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise<number>; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function closeProxyChannel(channelId: number): void; 差异内容：NA | 类名：proxyChannelManager； API声明：function closeProxyChannel(channelId: number): void; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function sendData(channelId: number, data: ArrayBuffer): Promise<void>; 差异内容：NA | 类名：proxyChannelManager； API声明：function sendData(channelId: number, data: ArrayBuffer): Promise<void>; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void; 差异内容：NA | 类名：proxyChannelManager； API声明：function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void; 差异内容：NA | 类名：proxyChannelManager； API声明：function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void; 差异内容：NA | 类名：proxyChannelManager； API声明：function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void; 差异内容：NA | 类名：proxyChannelManager； API声明：function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
