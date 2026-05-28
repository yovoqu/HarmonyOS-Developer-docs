# @security/no-unsafe-mac

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-mac

该规则禁止在[MAC消息认证算法](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/aegis-message-authentication-code-calculation-0000001907018769)中使用不安全的哈希算法，例如SHA1。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@security/no-unsafe-mac"</span>: <span style="color: rgb(6,125,23);">"warn"</span>
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
import cryptoFramework from '@ohos.security.cryptoFramework';
import { CryptoJS } from '@ohos/crypto-js';
cryptoFramework.createMac('SHA256');
CryptoJS.HmacSHA256('Message').toString();
```
 
 

##### 反例

```text
import cryptoFramework from '@ohos.security.cryptoFramework';
import { CryptoJS } from '@ohos/crypto-js';
cryptoFramework.createMac('SHA1');
CryptoJS.HmacSHA1('Message').toString();
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@security/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@security/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
