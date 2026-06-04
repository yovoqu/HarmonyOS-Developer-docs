# Wear Engine

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-wearengine-6112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：MonitorClient； API声明：queryStatus(deviceRandomId: string, item: MonitorItem): Promise&lt;MonitorData&gt;; 差异内容：NA | 类名：MonitorClient； API声明：queryStatus(deviceRandomId: string, item: MonitorItem): Promise&lt;MonitorData&gt;; 差异内容：801 | api/@hms.health.wearEngine.d.ts |
| 新增错误码 | 类名：MonitorClient； API声明：subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; 差异内容：NA | 类名：MonitorClient； API声明：subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; 差异内容：801 | api/@hms.health.wearEngine.d.ts |
| 新增错误码 | 类名：MonitorClient； API声明：unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; 差异内容：NA | 类名：MonitorClient； API声明：unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback&lt;MonitorEventData&gt;): Promise&lt;void&gt;; 差异内容：801 | api/@hms.health.wearEngine.d.ts |
