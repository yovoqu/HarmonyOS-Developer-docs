# Device Security Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace securityAudit 差异内容： declare namespace securityAudit | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明： interface AuditEvent 差异内容： interface AuditEvent | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent； API声明：eventId: number; 差异内容：eventId: number; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent； API声明：version?: string; 差异内容：version?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent； API声明：timestamp?: string; 差异内容：timestamp?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent； API声明：content?: string; 差异内容：content?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent； API声明：userId?: number; 差异内容：userId?: number; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEvent； API声明：deviceId?: string; 差异内容：deviceId?: string; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明： interface AuditEventInfo 差异内容： interface AuditEventInfo | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：AuditEventInfo； API声明：eventId: number; 差异内容：eventId: number; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明：function on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback&lt;AuditEvent&gt;): void; 差异内容：function on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback&lt;AuditEvent&gt;): void; | api/@hms.security.securityAudit.d.ts |
| 新增API | NA | 类名：securityAudit； API声明：function off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback&lt;AuditEvent&gt;): void; 差异内容：function off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback&lt;AuditEvent&gt;): void; | api/@hms.security.securityAudit.d.ts |
