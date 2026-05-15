# HMAC(ArkTS)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-arkts

HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code）。具体的场景介绍及支持的算法规格，请参考[HMAC介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-overview)。


## 开发步骤

**生成密钥** 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview)。 初始化密钥属性集。 调用[generateKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksgeneratekeyitem9)生成密钥，HMAC支持的规格请参考[密钥生成支持的算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-overview#支持的算法)。 除此之外，开发者也可以参考[密钥导入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview#支持的算法)的规格介绍，导入已有的密钥。 **执行HMAC** 获取密钥别名。 获取待运算的数据。 调用[initSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。 调用[finishSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksfinishsession9)结束密钥会话，获取哈希后的数据。
```text
/*
 * 以下以HMAC密钥的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';

let hmacKeyAlias = 'test_HMAC';
let handle: number;
let plainText = '123456';
let hashData: Uint8Array;

function stringToUint8Array(str: String) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i  {
      console.info(`promise: generate HMAC Key success`);
    }).catch((error: Error) => {
      console.error(`promise: generate HMAC Key failed, ${JSON.stringify(error)}`);
      throw (error as Error);
    })
}
/* 2.执行 HMAC 计算 */
async function hMACData() {
  let options: huks.HuksOptions = {
    properties: getHMACProperties(),
    inData: stringToUint8Array(plainText)
  }

  await huks.initSession(hmacKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: Error) => {
      console.error(`promise: init session failed, ${JSON.stringify(error)}`);
      throw (error as Error);
    })

  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: HMAC data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      hashData = data.outData as Uint8Array;
    }).catch((error: Error) => {
      console.error(`promise: HMAC data failed, ${JSON.stringify(error)}`);
      throw (error as Error);
    })
}

async function executeHMAC() {
  await generateHMACKey();
  await hMACData();
}
```
