# Enterprise Space Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisespacekit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：spaceManager； API声明：interface ProcessConfigInfo 差异内容：interface ProcessConfigInfo | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：ProcessConfigInfo； API声明：processName: string; 差异内容：processName: string; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：ProcessConfigInfo； API声明：disallowPaths: string[]; 差异内容：disallowPaths: string[]; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager； API声明：enum UserDataEnum 差异内容：enum UserDataEnum | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：UserDataEnum； API声明：ENTERPRISE = 0 差异内容：ENTERPRISE = 0 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：UserDataEnum； API声明：PERSONAL = 1 差异内容：PERSONAL = 1 | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager； API声明：function setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise&lt;void&gt;; 差异内容：function setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise&lt;void&gt;; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager； API声明：function getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise&lt;boolean&gt;; 差异内容：function getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise&lt;boolean&gt;; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager； API声明：function getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>; 差异内容：function getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager； API声明：function addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise&lt;void&gt;; 差异内容：function addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise&lt;void&gt;; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
| 新增API | NA | 类名：spaceManager； API声明：function deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string): Promise&lt;void&gt;; 差异内容：function deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string): Promise&lt;void&gt;; | api/@hms.enterpriseSpaceService.spaceManager.d.ts |
