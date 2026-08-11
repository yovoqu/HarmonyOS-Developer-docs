# Contacts Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-contactskit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：contact； API声明：function syncContacts(context: Context, mode: ContactSyncMode, progress: ContactSyncProgress, contacts: Array&lt;Contact&gt;): Promise<Array&lt;number&gt;>; 差异内容：function syncContacts(context: Context, mode: ContactSyncMode, progress: ContactSyncProgress, contacts: Array&lt;Contact&gt;): Promise<Array&lt;number&gt;>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明：function queryContactSyncInfo(context: Context): Promise<Array&lt;ContactSyncInfo&gt;>; 差异内容：function queryContactSyncInfo(context: Context): Promise<Array&lt;ContactSyncInfo&gt;>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明：function importContactsViaUI(context: Context, contacts: Array&lt;Contact&gt;): Promise<Array&lt;number&gt;>; 差异内容：function importContactsViaUI(context: Context, contacts: Array&lt;Contact&gt;): Promise<Array&lt;number&gt;>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明：enum ContactSyncMode 差异内容：enum ContactSyncMode | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncMode； API声明：MODE_INCREMENTAL = 1 差异内容：MODE_INCREMENTAL = 1 | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncMode； API声明：MODE_CLOUD_BASED = 2 差异内容：MODE_CLOUD_BASED = 2 | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明：interface ContactSyncProgress 差异内容：interface ContactSyncProgress | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncProgress； API声明：syncId: number; 差异内容：syncId: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncProgress； API声明：currentBatch: number; 差异内容：currentBatch: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncProgress； API声明：totalBatches: number; 差异内容：totalBatches: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明：interface ContactSyncInfo 差异内容：interface ContactSyncInfo | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo； API声明：mode: ContactSyncMode; 差异内容：mode: ContactSyncMode; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo； API声明：syncId: number; 差异内容：syncId: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo； API声明：completedBatches: Array&lt;number&gt;; 差异内容：completedBatches: Array&lt;number&gt;; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo； API声明：totalBatches: number; 差异内容：totalBatches: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo； API声明：lastSyncTime: number; 差异内容：lastSyncTime: number; | api/@ohos.contact.d.ts |
