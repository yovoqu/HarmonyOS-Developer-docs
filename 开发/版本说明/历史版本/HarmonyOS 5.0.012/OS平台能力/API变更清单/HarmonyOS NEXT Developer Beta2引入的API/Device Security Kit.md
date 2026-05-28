# Device Security Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：trustedAppService； API声明：function getCurrentSecureLocation(timeout: number, priority: LocatingPriority): Promise&lt;SecureLocation&gt;; 差异内容：ohos.permission.APPROXIMATELY_LOCATION | 类名：trustedAppService； API声明：function getCurrentSecureLocation(timeout: number, priority: LocatingPriority): Promise&lt;SecureLocation&gt;; 差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION | api/@hms.security.trustedAppService.d.ts |
