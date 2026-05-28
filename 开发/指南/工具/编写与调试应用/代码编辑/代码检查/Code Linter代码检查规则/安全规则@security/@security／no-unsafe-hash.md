# @security/no-unsafe-hash

更新时间：2026-03-24 06:03:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-hash

该规则禁止不安全的哈希算法，例如MD5、SHA1。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@security/no-unsafe-hash"</span>: <span style="color: rgb(6,125,23);">"error"</span>
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
//正例1
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA256');

//正例2
/**
 * 下载<a href="https://gitcode.com/openharmony-sig/ohos_crypto_js" target="_blank">crypto-js</a>依赖：ohpm install @ohos/crypto-js
 */
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA256('Message').toString();
```
 
 

#### 反例

```text
//反例1.1
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('MD5');

//反例1.2
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA1');

//反例2.1
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.MD5('Message').toString();

//反例2.2
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA1('Message').toString();
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@security/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@security/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
