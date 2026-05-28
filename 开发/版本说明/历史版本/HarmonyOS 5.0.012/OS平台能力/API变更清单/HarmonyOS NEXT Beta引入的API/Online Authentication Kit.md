# Online Authentication Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-onlineauthenticationkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace soter 差异内容： declare namespace soter | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明： export enum KeyType 差异内容： export enum KeyType | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：KeyType； API声明：ECC_P256 = 0 差异内容：ECC_P256 = 0 | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明： class SignedResult 差异内容： class SignedResult | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：SignedResult； API声明：message: Uint8Array; 差异内容：message: Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：SignedResult； API声明：signature: Uint8Array; 差异内容：signature: Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：SignedResult； API声明：saltLength: number; 差异内容：saltLength: number; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function generateAppSecureKeySync(keyType: KeyType): Uint8Array; 差异内容：function generateAppSecureKeySync(keyType: KeyType): Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function generateAppSecureKey(keyType: KeyType): Promise&lt;Uint8Array&gt;; 差异内容：function generateAppSecureKey(keyType: KeyType): Promise&lt;Uint8Array&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function getAppSecureKeySync(keyType: KeyType): Uint8Array; 差异内容：function getAppSecureKeySync(keyType: KeyType): Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function getAppSecureKey(keyType: KeyType): Promise&lt;Uint8Array&gt;; 差异内容：function getAppSecureKey(keyType: KeyType): Promise&lt;Uint8Array&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function hasAppSecureKeySync(keyType: KeyType): boolean; 差异内容：function hasAppSecureKeySync(keyType: KeyType): boolean; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function hasAppSecureKey(keyType: KeyType): Promise&lt;boolean&gt;; 差异内容：function hasAppSecureKey(keyType: KeyType): Promise&lt;boolean&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function generateAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult; 差异内容：function generateAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function generateAuthKey(keyAlias: string, keyType: KeyType): Promise&lt;SignedResult&gt;; 差异内容：function generateAuthKey(keyAlias: string, keyType: KeyType): Promise&lt;SignedResult&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function getAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult; 差异内容：function getAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function getAuthKey(keyAlias: string, keyType: KeyType): Promise&lt;SignedResult&gt;; 差异内容：function getAuthKey(keyAlias: string, keyType: KeyType): Promise&lt;SignedResult&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function hasAuthKeySync(keyAlias: string, keyType: KeyType): boolean; 差异内容：function hasAuthKeySync(keyAlias: string, keyType: KeyType): boolean; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function hasAuthKey(keyAlias: string, keyType: KeyType): Promise&lt;boolean&gt;; 差异内容：function hasAuthKey(keyAlias: string, keyType: KeyType): Promise&lt;boolean&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function generateChallengeSync(keyAlias: string): Uint8Array; 差异内容：function generateChallengeSync(keyAlias: string): Uint8Array; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function generateChallenge(keyAlias: string): Promise&lt;Uint8Array&gt;; 差异内容：function generateChallenge(keyAlias: string): Promise&lt;Uint8Array&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function signWithAuthKeySync(keyAlias: string, authToken: Uint8Array, info: string): SignedResult; 差异内容：function signWithAuthKeySync(keyAlias: string, authToken: Uint8Array, info: string): SignedResult; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function signWithAuthKey(keyAlias: string, authToken: Uint8Array, info: string): Promise&lt;SignedResult&gt;; 差异内容：function signWithAuthKey(keyAlias: string, authToken: Uint8Array, info: string): Promise&lt;SignedResult&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function deleteAuthKeySync(keyAlias: string): void; 差异内容：function deleteAuthKeySync(keyAlias: string): void; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function deleteAuthKey(keyAlias: string): Promise&lt;void&gt;; 差异内容：function deleteAuthKey(keyAlias: string): Promise&lt;void&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function deleteAppSecureKeySync(): void; 差异内容：function deleteAppSecureKeySync(): void; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function deleteAppSecureKey(): Promise&lt;void&gt;; 差异内容：function deleteAppSecureKey(): Promise&lt;void&gt;; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function getVersionSync(): string; 差异内容：function getVersionSync(): string; | api/@hms.security.soter.d.ts |
| 新增API | NA | 类名：soter； API声明：function getVersion(): Promise&lt;string&gt;; 差异内容：function getVersion(): Promise&lt;string&gt;; | api/@hms.security.soter.d.ts |
