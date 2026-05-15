# 安全随机数生成(ArkTS)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number

> [!NOTE]
> 从API version 12开始，轻量级智能穿戴设备支持获取随机数相关操作。

随机数主要用于临时会话密钥生成和非对称加密算法密钥生成等场景。在加解密场景中，安全随机数生成器需要具备随机性、不可预测性与不可重现性。当前系统生成的随机数满足密码学安全伪随机性要求。

开发者可以调用接口，完成以下功能：


在开发前，开发者应该先对加解密基础知识有一定了解，并熟知以下随机数相关的基本概念：


## 支持的算法与规格

随机数生成算法使用OpenSSL的RAND_priv_bytes接口生成安全随机数。
| 算法 | 长度（Byte） |
| --- | --- |
| CTR_DRBG | [1, INT_MAX] |


## 开发步骤

调用[cryptoFramework.createRandom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreaterandom)，生成随机数实例。 （可选）设置DataBlob数据，调用[Random.setSeed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#setseed)，为随机数生成池设置种子。 设置指定字节长度，调用[Random.generateRandom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#generaterandom)或[Random.generateRandomSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#generaterandomsync10)，生成安全随机数。 指定字节长度范围为1~INT_MAX。 通过await返回异步结果：
```text
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function doRand() {
    let rand = cryptoFramework.createRandom();
    let seed = new Uint8Array([1, 2, 3]);
    rand.setSeed({ data: seed });
    let len = 12;
    let randOutput = await rand.generateRandom(len);
    console.info('rand output: ' + randOutput.data);
  }
```

同步返回结果：
```text
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function doRandBySync() {
  let rand = cryptoFramework.createRandom();
  let len = 24; // Generate a 24-byte random number.
  try {
    let randData = rand.generateRandomSync(len);
    if (randData.data.length !== 0) {
      console.info('[Sync]: rand result: ' + randData.data);
    } else {
      console.error('[Sync]: get rand result: fail!');
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`do rand failed: errCode: ${e.code}, message: ${e.message}`);
  }
}
```
