# Crypto Architecture Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cryptoarchitecturekit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec, callback: AsyncCallback&lt;void&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec \| null, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec \| null, callback: AsyncCallback&lt;void&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec): Promise&lt;void&gt;; 差异内容：NA | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec): Promise&lt;void&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec \| null): Promise&lt;void&gt;; 差异内容：NA | 类名：Cipher； API声明：init(opMode: CryptoMode, key: Key, params: ParamsSpec \| null): Promise&lt;void&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：initSync(opMode: CryptoMode, key: Key, params: ParamsSpec \| null): void; 差异内容：NA | 类名：Cipher； API声明：initSync(opMode: CryptoMode, key: Key, params: ParamsSpec \| null): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：update(data: DataBlob, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：NA | 类名：Cipher； API声明：update(data: DataBlob, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：update(data: DataBlob): Promise&lt;DataBlob&gt;; 差异内容：NA | 类名：Cipher； API声明：update(data: DataBlob): Promise&lt;DataBlob&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：updateSync(data: DataBlob): DataBlob; 差异内容：NA | 类名：Cipher； API声明：updateSync(data: DataBlob): DataBlob; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：doFinal(data: DataBlob, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：NA | 类名：Cipher； API声明：doFinal(data: DataBlob, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：doFinal(data: DataBlob \| null, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：NA | 类名：Cipher； API声明：doFinal(data: DataBlob \| null, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：doFinal(data: DataBlob): Promise&lt;DataBlob&gt;; 差异内容：NA | 类名：Cipher； API声明：doFinal(data: DataBlob): Promise&lt;DataBlob&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：doFinal(data: DataBlob \| null): Promise&lt;DataBlob&gt;; 差异内容：NA | 类名：Cipher； API声明：doFinal(data: DataBlob \| null): Promise&lt;DataBlob&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：doFinalSync(data: DataBlob \| null): DataBlob; 差异内容：NA | 类名：Cipher； API声明：doFinalSync(data: DataBlob \| null): DataBlob; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：setCipherSpec(itemType: CipherSpecItem, itemValue: Uint8Array): void; 差异内容：NA | 类名：Cipher； API声明：setCipherSpec(itemType: CipherSpecItem, itemValue: Uint8Array): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Cipher； API声明：getCipherSpec(itemType: CipherSpecItem): string \| Uint8Array; 差异内容：NA | 类名：Cipher； API声明：getCipherSpec(itemType: CipherSpecItem): string \| Uint8Array; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Kdf； API声明：generateSecret(params: KdfSpec, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：NA | 类名：Kdf； API声明：generateSecret(params: KdfSpec, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Kdf； API声明：generateSecret(params: KdfSpec): Promise&lt;DataBlob&gt;; 差异内容：NA | 类名：Kdf； API声明：generateSecret(params: KdfSpec): Promise&lt;DataBlob&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Kdf； API声明：generateSecretSync(params: KdfSpec): DataBlob; 差异内容：NA | 类名：Kdf； API声明：generateSecretSync(params: KdfSpec): DataBlob; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework； API声明：interface Poly1305ParamsSpec 差异内容：interface Poly1305ParamsSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Poly1305ParamsSpec； API声明：iv: DataBlob; 差异内容：iv: DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Poly1305ParamsSpec； API声明：aad: DataBlob; 差异内容：aad: DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Poly1305ParamsSpec； API声明：authTag: DataBlob; 差异内容：authTag: DataBlob; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework； API声明：interface X963KdfSpec 差异内容：interface X963KdfSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：X963KdfSpec； API声明：key: string \| Uint8Array; 差异内容：key: string \| Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：X963KdfSpec； API声明：info: Uint8Array; 差异内容：info: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：X963KdfSpec； API声明：keySize: number; 差异内容：keySize: number; | api/@ohos.security.cryptoFramework.d.ts |
