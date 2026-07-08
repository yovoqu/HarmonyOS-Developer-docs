# Contacts Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-contactskit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：contact； API声明：function selectContact(callback: AsyncCallback<Array&lt;Contact&gt;>): void; 差异内容：ohos.permission.READ_CONTACTS | 类名：contact； API声明：function selectContact(callback: AsyncCallback<Array&lt;Contact&gt;>): void; 差异内容：NA | api/@ohos.contact.d.ts |
| 权限变更 | 类名：contact； API声明：function selectContact(): Promise<Array&lt;Contact&gt;>; 差异内容：ohos.permission.READ_CONTACTS | 类名：contact； API声明：function selectContact(): Promise<Array&lt;Contact&gt;>; 差异内容：NA | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSelectionOptions； API声明：isAutoDismissOnNavigation?: boolean; 差异内容：isAutoDismissOnNavigation?: boolean; | api/@ohos.contact.d.ts |
