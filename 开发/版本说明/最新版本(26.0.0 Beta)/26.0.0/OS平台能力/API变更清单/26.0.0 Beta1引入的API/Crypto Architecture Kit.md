# Crypto Architecture Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cryptoarchitecturekit-7001

## Crypto Architecture Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：PriKey； API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint \| string \| number; 差异内容：NA | 类名：PriKey； API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint \| string \| number; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PriKey； API声明：getEncodedDer(format: string): DataBlob; 差异内容：NA | 类名：PriKey； API声明：getEncodedDer(format: string): DataBlob; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PriKey； API声明：getEncodedPem(format: string): string; 差异内容：NA | 类名：PriKey； API声明：getEncodedPem(format: string): string; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PubKey； API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint \| string \| number; 差异内容：NA | 类名：PubKey； API声明：getAsyKeySpec(itemType: AsyKeySpecItem): bigint \| string \| number; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：PubKey； API声明：getEncodedPem(format: string): string; 差异内容：NA | 类名：PubKey； API声明：getEncodedPem(format: string): string; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback&lt;KeyPair&gt;): void; 差异内容：NA | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback&lt;KeyPair&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob \| null, priKey: DataBlob \| null, callback: AsyncCallback&lt;KeyPair&gt;): void; 差异内容：NA | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob \| null, priKey: DataBlob \| null, callback: AsyncCallback&lt;KeyPair&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob, priKey: DataBlob): Promise&lt;KeyPair&gt;; 差异内容：NA | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob, priKey: DataBlob): Promise&lt;KeyPair&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob \| null, priKey: DataBlob \| null): Promise&lt;KeyPair&gt;; 差异内容：NA | 类名：AsyKeyGenerator； API声明：convertKey(pubKey: DataBlob \| null, priKey: DataBlob \| null): Promise&lt;KeyPair&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator； API声明：convertKeySync(pubKey: DataBlob \| null, priKey: DataBlob \| null): KeyPair; 差异内容：NA | 类名：AsyKeyGenerator； API声明：convertKeySync(pubKey: DataBlob \| null, priKey: DataBlob \| null): KeyPair; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator； API声明：convertPemKey(pubKey: string \| null, priKey: string \| null): Promise&lt;KeyPair&gt;; 差异内容：NA | 类名：AsyKeyGenerator； API声明：convertPemKey(pubKey: string \| null, priKey: string \| null): Promise&lt;KeyPair&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：AsyKeyGenerator； API声明：convertPemKeySync(pubKey: string \| null, priKey: string \| null): KeyPair; 差异内容：NA | 类名：AsyKeyGenerator； API声明：convertPemKeySync(pubKey: string \| null, priKey: string \| null): KeyPair; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator； API声明：generateSymKey(callback: AsyncCallback&lt;SymKey&gt;): void; 差异内容：NA | 类名：SymKeyGenerator； API声明：generateSymKey(callback: AsyncCallback&lt;SymKey&gt;): void; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator； API声明：generateSymKey(): Promise&lt;SymKey&gt;; 差异内容：NA | 类名：SymKeyGenerator； API声明：generateSymKey(): Promise&lt;SymKey&gt;; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator； API声明：generateSymKeySync(): SymKey; 差异内容：NA | 类名：SymKeyGenerator； API声明：generateSymKeySync(): SymKey; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator； API声明：convertKey(key: DataBlob, callback: AsyncCallback&lt;SymKey&gt;): void; 差异内容：NA | 类名：SymKeyGenerator； API声明：convertKey(key: DataBlob, callback: AsyncCallback&lt;SymKey&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator； API声明：convertKey(key: DataBlob): Promise&lt;SymKey&gt;; 差异内容：NA | 类名：SymKeyGenerator； API声明：convertKey(key: DataBlob): Promise&lt;SymKey&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：SymKeyGenerator； API声明：convertKeySync(key: DataBlob): SymKey; 差异内容：NA | 类名：SymKeyGenerator； API声明：convertKeySync(key: DataBlob): SymKey; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：init(priKey: PriKey, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：Sign； API声明：init(priKey: PriKey, callback: AsyncCallback&lt;void&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：init(priKey: PriKey): Promise&lt;void&gt;; 差异内容：NA | 类名：Sign； API声明：init(priKey: PriKey): Promise&lt;void&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：initSync(priKey: PriKey): void; 差异内容：NA | 类名：Sign； API声明：initSync(priKey: PriKey): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：update(data: DataBlob, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：Sign； API声明：update(data: DataBlob, callback: AsyncCallback&lt;void&gt;): void; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：update(data: DataBlob): Promise&lt;void&gt;; 差异内容：NA | 类名：Sign； API声明：update(data: DataBlob): Promise&lt;void&gt;; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：updateSync(data: DataBlob): void; 差异内容：NA | 类名：Sign； API声明：updateSync(data: DataBlob): void; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：sign(data: DataBlob, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：NA | 类名：Sign； API声明：sign(data: DataBlob, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：sign(data: DataBlob \| null, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：NA | 类名：Sign； API声明：sign(data: DataBlob \| null, callback: AsyncCallback&lt;DataBlob&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：sign(data: DataBlob): Promise&lt;DataBlob&gt;; 差异内容：NA | 类名：Sign； API声明：sign(data: DataBlob): Promise&lt;DataBlob&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：sign(data: DataBlob \| null): Promise&lt;DataBlob&gt;; 差异内容：NA | 类名：Sign； API声明：sign(data: DataBlob \| null): Promise&lt;DataBlob&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：signSync(data: DataBlob \| null): DataBlob; 差异内容：NA | 类名：Sign； API声明：signSync(data: DataBlob \| null): DataBlob; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：setSignSpec(itemType: SignSpecItem, itemValue: number): void; 差异内容：NA | 类名：Sign； API声明：setSignSpec(itemType: SignSpecItem, itemValue: number): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Sign； API声明：getSignSpec(itemType: SignSpecItem): string \| number; 差异内容：NA | 类名：Sign； API声明：getSignSpec(itemType: SignSpecItem): string \| number; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：init(pubKey: PubKey, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：Verify； API声明：init(pubKey: PubKey, callback: AsyncCallback&lt;void&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：init(pubKey: PubKey): Promise&lt;void&gt;; 差异内容：NA | 类名：Verify； API声明：init(pubKey: PubKey): Promise&lt;void&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：initSync(pubKey: PubKey): void; 差异内容：NA | 类名：Verify； API声明：initSync(pubKey: PubKey): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：update(data: DataBlob, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：Verify； API声明：update(data: DataBlob, callback: AsyncCallback&lt;void&gt;): void; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：update(data: DataBlob): Promise&lt;void&gt;; 差异内容：NA | 类名：Verify； API声明：update(data: DataBlob): Promise&lt;void&gt;; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：updateSync(data: DataBlob): void; 差异内容：NA | 类名：Verify； API声明：updateSync(data: DataBlob): void; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：verify(data: DataBlob, signatureData: DataBlob, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：Verify； API声明：verify(data: DataBlob, signatureData: DataBlob, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：verify(data: DataBlob \| null, signatureData: DataBlob, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：Verify； API声明：verify(data: DataBlob \| null, signatureData: DataBlob, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：verify(data: DataBlob, signatureData: DataBlob): Promise&lt;boolean&gt;; 差异内容：NA | 类名：Verify； API声明：verify(data: DataBlob, signatureData: DataBlob): Promise&lt;boolean&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：verify(data: DataBlob \| null, signatureData: DataBlob): Promise&lt;boolean&gt;; 差异内容：NA | 类名：Verify； API声明：verify(data: DataBlob \| null, signatureData: DataBlob): Promise&lt;boolean&gt;; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：verifySync(data: DataBlob \| null, signatureData: DataBlob): boolean; 差异内容：NA | 类名：Verify； API声明：verifySync(data: DataBlob \| null, signatureData: DataBlob): boolean; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：recover(signatureData: DataBlob): Promise<DataBlob \| null>; 差异内容：NA | 类名：Verify； API声明：recover(signatureData: DataBlob): Promise<DataBlob \| null>; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：recoverSync(signatureData: DataBlob): DataBlob \| null; 差异内容：NA | 类名：Verify； API声明：recoverSync(signatureData: DataBlob): DataBlob \| null; 差异内容：17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number): void; 差异内容：NA | 类名：Verify； API声明：setVerifySpec(itemType: SignSpecItem, itemValue: number): void; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增错误码 | 类名：Verify； API声明：getVerifySpec(itemType: SignSpecItem): string \| number; 差异内容：NA | 类名：Verify； API声明：getVerifySpec(itemType: SignSpecItem): string \| number; 差异内容：17620003 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Result； API声明：ERR_INVALID_CALL = 17620004 差异内容：ERR_INVALID_CALL = 17620004 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework； API声明：interface AeadParamsSpec 差异内容：interface AeadParamsSpec | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AeadParamsSpec； API声明：nonce: Uint8Array; 差异内容：nonce: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AeadParamsSpec； API声明：authenticatedData?: Uint8Array; 差异内容：authenticatedData?: Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AeadParamsSpec； API声明：tagLen?: number; 差异内容：tagLen?: number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：Key； API声明：getKeySize(): number; 差异内容：getKeySize(): number; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PriKey； API声明：getKeyData(itemType: AsyKeyDataItem): Promise&lt;Uint8Array&gt;; 差异内容：getKeyData(itemType: AsyKeyDataItem): Promise&lt;Uint8Array&gt;; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PriKey； API声明：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array; 差异内容：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PubKey； API声明：getKeyData(itemType: AsyKeyDataItem): Promise&lt;Uint8Array&gt;; 差异内容：getKeyData(itemType: AsyKeyDataItem): Promise&lt;Uint8Array&gt;; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：PubKey； API声明：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array; 差异内容：getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array; | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：cryptoFramework； API声明：enum AsyKeyDataItem 差异内容：enum AsyKeyDataItem | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem； API声明：EC_PRIVATE_K = 6 差异内容：EC_PRIVATE_K = 6 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem； API声明：EC_PRIVATE_04_X_Y_K = 7 差异内容：EC_PRIVATE_04_X_Y_K = 7 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem； API声明：EC_PUBLIC_X_Y = 8 差异内容：EC_PUBLIC_X_Y = 8 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem； API声明：EC_PUBLIC_04_X_Y = 9 差异内容：EC_PUBLIC_04_X_Y = 9 | api/@ohos.security.cryptoFramework.d.ts |
| 新增API | NA | 类名：AsyKeyDataItem； API声明：EC_PUBLIC_COMPRESS_X = 10 差异内容：EC_PUBLIC_COMPRESS_X = 10 | api/@ohos.security.cryptoFramework.d.ts |
