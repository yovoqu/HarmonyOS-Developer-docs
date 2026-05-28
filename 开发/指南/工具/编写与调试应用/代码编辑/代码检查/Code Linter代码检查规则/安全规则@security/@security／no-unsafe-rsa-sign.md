# @security/no-unsafe-rsa-sign

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-rsa-sign

该规则禁止不安全的RSA签名算法，如RSA模数长度小于2048bit、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见： [RSA加解密](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-encryption-and-decryption-asymmetric-0000001907932453)。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@security/no-unsafe-rsa-sign"</span>: <span style="color: rgb(6,125,23);">"error"</span>
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA3072|PSS|SHA256|MGF1_SHA256');
cryptoFramework.createVerify('RSA3072|PSS|SHA256|MGF1_SHA256');
```
 
 

#### 反例

```text
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA512|PKCS1|MD5');
cryptoFramework.createVerify('RSA512|PKCS1|MD5');
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@security/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@security/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
