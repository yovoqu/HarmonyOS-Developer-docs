# Share Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：ShareController； API声明：on(event: 'dismiss', callback: () => void): void; 差异内容：NA | 类名：ShareController； API声明：on(event: 'dismiss', callback: () => void): void; 差异内容：401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：ShareController； API声明：off(event: 'dismiss', callback: () => void): void; 差异内容：NA | 类名：ShareController； API声明：off(event: 'dismiss', callback: () => void): void; 差异内容：401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：systemShare； API声明：function getSharedData(want: Want): Promise&lt;SharedData&gt;; 差异内容：1003703001 | 类名：systemShare； API声明：function getSharedData(want: Want): Promise&lt;SharedData&gt;; 差异内容：1003703001,401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：systemShare； API声明：function getWant(data: SharedData, options?: ShareControllerOptions): Promise&lt;Want&gt;; 差异内容：1003703001 | 类名：systemShare； API声明：function getWant(data: SharedData, options?: ShareControllerOptions): Promise&lt;Want&gt;; 差异内容：1003703001,401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：systemShare； API声明：function getContactInfo(want: Want): Promise&lt;ContactInfo&gt;; 差异内容：1003703001 | 类名：systemShare； API声明：function getContactInfo(want: Want): Promise&lt;ContactInfo&gt;; 差异内容：1003703001,401 | api/@hms.collaboration.systemShare.d.ts |
