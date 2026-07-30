# Account Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace intimate 差异内容：declare namespace intimate | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate； API声明：enum IntimateErrorCode 差异内容：enum IntimateErrorCode | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：ACCOUNT_NOT_LOGGED_IN = 1026900001 差异内容：ACCOUNT_NOT_LOGGED_IN = 1026900001 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：INTERNAL_ERROR = 1026900003 差异内容：INTERNAL_ERROR = 1026900003 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：SERVER_ERROR = 1026900004 差异内容：SERVER_ERROR = 1026900004 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：NETWORK_ERROR = 1026900005 差异内容：NETWORK_ERROR = 1026900005 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：PARAMETER_ERROR = 1026900006 差异内容：PARAMETER_ERROR = 1026900006 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：UNSUPPORTED_REGION = 1026900007 差异内容：UNSUPPORTED_REGION = 1026900007 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：USER_CANCELED = 1026900008 差异内容：USER_CANCELED = 1026900008 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode； API声明：PERMISSION_CHECK_ERROR = 1026900009 差异内容：PERMISSION_CHECK_ERROR = 1026900009 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate； API声明：enum IdType 差异内容：enum IdType | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IdType； API声明：OPEN_ID = 1 差异内容：OPEN_ID = 1 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IdType； API声明：UNION_ID = 2 差异内容：UNION_ID = 2 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate； API声明：interface IntimatesSelectionRequest 差异内容：interface IntimatesSelectionRequest | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest； API声明：maxSelectionCount?: number; 差异内容：maxSelectionCount?: number; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest； API声明：onlySelectIntimateWithHuaweiID?: boolean; 差异内容：onlySelectIntimateWithHuaweiID?: boolean; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest； API声明：idType: IdType; 差异内容：idType: IdType; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest； API声明：idValue: string; 差异内容：idValue: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate； API声明：interface IntimatesSelectionResponse 差异内容：interface IntimatesSelectionResponse | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse； API声明：openID?: string; 差异内容：openID?: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse； API声明：unionID?: string; 差异内容：unionID?: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse； API声明：anonymousAccount?: string; 差异内容：anonymousAccount?: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse； API声明：avatarUri: string; 差异内容：avatarUri: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse； API声明：nickname: string; 差异内容：nickname: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate； API声明：function selectIntimates(context: common.Context, request: IntimatesSelectionRequest): Promise<IntimatesSelectionResponse[]>; 差异内容：function selectIntimates(context: common.Context, request: IntimatesSelectionRequest): Promise<IntimatesSelectionResponse[]>; | api/@hms.core.account.intimate.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.core.account.intimate.d.ts 差异内容：AccountKit | api/@hms.core.account.intimate.d.ts |
