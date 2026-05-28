# @security/no-unsafe-sm2-cipher

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm2-cipher

此规则禁止在SM2算法中使用不安全的消息摘要算法MD5和SHA1。推荐使用SM2_256|SHA256算法和RSA算法，算法详情参见：[非对称加解密算法](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453)和[非对称密钥加解密算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec#rsa)。
 

#### 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm2-cipher": "warn"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM2_256|SHA256')
```
 
 

#### 反例

```text
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM2_256|SHA1')
cryptoFramework.createCipher('SM2_256|MD5')
```
 
 

#### 规则集

```text
<span style="color: rgb(80,160,79);">plugin:@security/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
