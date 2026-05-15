# Account Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-b061

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AuthenticationErrorCode； API声明：UNSUPPORTED = 1001500004 差异内容：UNSUPPORTED = 1001500004 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：AuthenticationErrorCode； API声明：REQUEST_RESTRICTED = 1001500005 差异内容：REQUEST_RESTRICTED = 1001500005 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：authentication； API声明： export interface ConsistencyRequest 差异内容： export interface ConsistencyRequest | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyRequest； API声明：idType: IdType; 差异内容：idType: IdType; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyRequest； API声明：idValue: string; 差异内容：idValue: string; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyRequest； API声明：mobileNumber: string; 差异内容：mobileNumber: string; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：authentication； API声明： export enum ConsistencyState 差异内容： export enum ConsistencyState | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyState； API声明：CONSISTENT = 0 差异内容：CONSISTENT = 0 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyState； API声明：INCONSISTENT_WITH_DEVICES = 1 差异内容：INCONSISTENT_WITH_DEVICES = 1 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyState； API声明：INCONSISTENT = 2 差异内容：INCONSISTENT = 2 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：authentication； API声明： export interface ConsistencyResult 差异内容： export interface ConsistencyResult | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ConsistencyResult； API声明：state: ConsistencyState; 差异内容：state: ConsistencyState; | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：HuaweiIDProvider； API声明：getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>; 差异内容：getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>; | api/@hms.core.authentication.d.ts |
