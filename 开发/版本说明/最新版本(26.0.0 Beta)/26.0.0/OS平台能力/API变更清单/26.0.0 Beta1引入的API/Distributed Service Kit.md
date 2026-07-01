# Distributed Service Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-7001

## Distributed Service Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：linkEnhance； API声明：function createServer(name: string): Server; 差异内容：NA | 类名：linkEnhance； API声明：function createServer(name: string): Server; 差异内容：801 | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增错误码 | 类名：linkEnhance； API声明：function createConnection(deviceId: string, name: string): Connection; 差异内容：NA | 类名：linkEnhance； API声明：function createConnection(deviceId: string, name: string): Connection; 差异内容：801 | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise&lt;number&gt;; 差异内容：NA | 类名：proxyChannelManager； API声明：function openProxyChannel(channelInfo: ChannelInfo): Promise&lt;number&gt;; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function closeProxyChannel(channelId: number): void; 差异内容：NA | 类名：proxyChannelManager； API声明：function closeProxyChannel(channelId: number): void; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
| 新增错误码 | 类名：proxyChannelManager； API声明：function sendData(channelId: number, data: ArrayBuffer): Promise&lt;void&gt;; 差异内容：NA | 类名：proxyChannelManager； API声明：function sendData(channelId: number, data: ArrayBuffer): Promise&lt;void&gt;; 差异内容：801 | api/@ohos.distributedsched.proxyChannelManager.d.ts |
