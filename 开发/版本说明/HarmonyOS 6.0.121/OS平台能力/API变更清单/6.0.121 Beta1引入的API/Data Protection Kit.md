# Data Protection Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataprotectionkit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace identifySensitiveContent 差异内容：declare namespace identifySensitiveContent | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：identifySensitiveContent； API声明：export interface Policy 差异内容：export interface Policy | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：Policy； API声明：sensitiveLabel: string; 差异内容：sensitiveLabel: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：Policy； API声明：keywords: Array&lt;string&gt;; 差异内容：keywords: Array&lt;string&gt;; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：Policy； API声明：regex: string; 差异内容：regex: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：identifySensitiveContent； API声明：export interface MatchResult 差异内容：export interface MatchResult | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：MatchResult； API声明：readonly sensitiveLabel: string; 差异内容：readonly sensitiveLabel: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：MatchResult； API声明：readonly matchContent: string; 差异内容：readonly matchContent: string; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：MatchResult； API声明：readonly matchNumber: number; 差异内容：readonly matchNumber: number; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：identifySensitiveContent； API声明：function scanFile(filePath: string, identifyPolicies: Array&lt;Policy&gt;): Promise<Array&lt;MatchResult&gt;>; 差异内容：function scanFile(filePath: string, identifyPolicies: Array&lt;Policy&gt;): Promise<Array&lt;MatchResult&gt;>; | api/@ohos.security.identifySensitiveContent.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export enum AccountType 差异内容：export enum AccountType | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AccountType； API声明：CLOUD_ACCOUNT = 1 差异内容：CLOUD_ACCOUNT = 1 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AccountType； API声明：DOMAIN_ACCOUNT = 2 差异内容：DOMAIN_ACCOUNT = 2 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AccountType； API声明：ENTERPRISE_ACCOUNT = 4 差异内容：ENTERPRISE_ACCOUNT = 4 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export interface AuthUser 差异内容：export interface AuthUser | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser； API声明：authAccount: string; 差异内容：authAccount: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser； API声明：authAccountType: AccountType; 差异内容：authAccountType: AccountType; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser； API声明：dlpFileAccess: DLPFileAccess; 差异内容：dlpFileAccess: DLPFileAccess; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：AuthUser； API声明：permExpiryTime: number; 差异内容：permExpiryTime: number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export interface DLPProperty 差异内容：export interface DLPProperty | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：ownerAccount: string; 差异内容：ownerAccount: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：ownerAccountID: string; 差异内容：ownerAccountID: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：ownerAccountType: AccountType; 差异内容：ownerAccountType: AccountType; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：authUserList?: Array&lt;AuthUser&gt;; 差异内容：authUserList?: Array&lt;AuthUser&gt;; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：contactAccount: string; 差异内容：contactAccount: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：offlineAccess: boolean; 差异内容：offlineAccess: boolean; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：everyoneAccessList?: Array&lt;DLPFileAccess&gt;; 差异内容：everyoneAccessList?: Array&lt;DLPFileAccess&gt;; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：expireTime?: number; 差异内容：expireTime?: number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：actionUponExpiry?: ActionType; 差异内容：actionUponExpiry?: ActionType; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：fileId?: string; 差异内容：fileId?: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DLPProperty； API声明：allowedOpenCount?: number; 差异内容：allowedOpenCount?: number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export enum ActionType 差异内容：export enum ActionType | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：ActionType； API声明：NOT_OPEN = 0 差异内容：NOT_OPEN = 0 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：ActionType； API声明：OPEN = 1 差异内容：OPEN = 1 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export interface CustomProperty 差异内容：export interface CustomProperty | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：CustomProperty； API声明：enterprise: string; 差异内容：enterprise: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise&lt;void&gt;; 差异内容：function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise&lt;void&gt;; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：function queryDlpPolicy(dlpFd: number): Promise&lt;string&gt;; 差异内容：function queryDlpPolicy(dlpFd: number): Promise&lt;string&gt;; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise&lt;void&gt;; 差异内容：function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise&lt;void&gt;; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export interface EnterprisePolicy 差异内容：export interface EnterprisePolicy | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：EnterprisePolicy； API声明：policyString: string; 差异内容：policyString: string; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：function setEnterprisePolicy(policy: EnterprisePolicy): void; 差异内容：function setEnterprisePolicy(policy: EnterprisePolicy): void; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export interface DlpConnPlugin 差异内容：export interface DlpConnPlugin | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpConnPlugin； API声明：connectServer(requestId: string, requestData: string, callback: Callback&lt;string&gt;): void; 差异内容：connectServer(requestId: string, requestData: string, callback: Callback&lt;string&gt;): void; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export class DlpConnManager 差异内容：export class DlpConnManager | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpConnManager； API声明：static registerPlugin(plugin: DlpConnPlugin): number; 差异内容：static registerPlugin(plugin: DlpConnPlugin): number; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpConnManager； API声明：static unregisterPlugin(): void; 差异内容：static unregisterPlugin(): void; | api/@ohos.dlpPermission.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.security.identifySensitiveContent.d.ts 差异内容：DataProtectionKit | api/@ohos.security.identifySensitiveContent.d.ts |
