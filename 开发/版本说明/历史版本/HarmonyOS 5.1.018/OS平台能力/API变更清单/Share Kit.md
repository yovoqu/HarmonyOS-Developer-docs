# Share Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：systemShare； API声明：enum ShareAbilityName 差异内容：enum ShareAbilityName | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：COPY_TO_PASTEBOARD = 'SystemShare_CopyToPasteboard' 差异内容：COPY_TO_PASTEBOARD = 'SystemShare_CopyToPasteboard' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：SAVE_TO_MEDIA_ASSET = 'SystemShare_SaveToMediaAsset' 差异内容：SAVE_TO_MEDIA_ASSET = 'SystemShare_SaveToMediaAsset' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：SAVE_AS_FILE = 'SystemShare_SaveAsFile' 差异内容：SAVE_AS_FILE = 'SystemShare_SaveAsFile' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：PRINT = 'SystemShare_Print' 差异内容：PRINT = 'SystemShare_Print' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：SAVE_TO_SUPERHUB = 'SystemShare_Superhub' 差异内容：SAVE_TO_SUPERHUB = 'SystemShare_Superhub' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：COLLECTION = 'SystemShare_Collection' 差异内容：COLLECTION = 'SystemShare_Collection' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：HARMONYSHARE = 'SystemShare_HarmonyShare' 差异内容：HARMONYSHARE = 'SystemShare_HarmonyShare' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityName； API声明：ENCRYPT = 'SystemShare_Encrypt' 差异内容：ENCRYPT = 'SystemShare_Encrypt' | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：systemShare； API声明：interface ShareAbilityInfo 差异内容：interface ShareAbilityInfo | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareAbilityInfo； API声明：name: string; 差异内容：name: string; | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：systemShare； API声明：interface ShareOperationResult 差异内容：interface ShareOperationResult | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：ShareOperationResult； API声明：targetAbilityInfo: ShareAbilityInfo; 差异内容：targetAbilityInfo: ShareAbilityInfo; | api/@hms.collaboration.systemShare.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：ShareController； API声明：on(type: 'shareCompleted', callback: Callback&lt;ShareOperationResult&gt;): void; 差异内容：on(type: 'shareCompleted', callback: Callback&lt;ShareOperationResult&gt;): void; | api/@hms.collaboration.systemShare.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：ShareController； API声明：off(type: 'shareCompleted', callback?: Callback&lt;ShareOperationResult&gt;): void; 差异内容：off(type: 'shareCompleted', callback?: Callback&lt;ShareOperationResult&gt;): void; | api/@hms.collaboration.systemShare.d.ts |
