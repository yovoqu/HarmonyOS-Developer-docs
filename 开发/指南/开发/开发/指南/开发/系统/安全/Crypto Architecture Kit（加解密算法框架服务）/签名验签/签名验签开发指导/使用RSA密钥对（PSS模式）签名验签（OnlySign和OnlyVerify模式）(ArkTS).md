# 使用RSA密钥对（PSS模式）签名验签（OnlySign和OnlyVerify模式）(ArkTS)

更新时间：2026-06-16 09:03:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-pss-sig-verify-onlysign-onlyverify

从API版本26.0.0开始，签名验签支持OnlySign/OnlyVerify模式。对应的算法规格请查看[签名验签算法规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-overview#rsa)。

**签名**
1. 调用[cryptoFramework.createMd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatemd)，指定摘要算法SHA256，生成摘要实例（Md）。
2. 调用[Md.update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#update-6)，传入自定义消息，进行摘要更新计算。单次update长度没有限制。
3. 调用[Md.digest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#digest)，获取摘要计算结果。
4. 调用[cryptoFramework.createAsyKeyGenerator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#generatekeypair-1)，生成密钥算法为RSA、密钥长度为1024位、素数个数为2的非对称密钥对象（KeyPair），包括公钥（PubKey）和私钥（PriKey）。

  如何生成RSA非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#rsa)和[随机生成非对称密钥对](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
5. 调用[cryptoFramework.createSign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatesign)，指定字符串参数'RSA|PSS|SHA256|MGF1_SHA256|OnlySign'，创建非对称密钥类型为不带长度的RSA、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1_SHA256，签名模式为OnlySign的Sign实例，用于完成签名操作。
6. 调用[Sign.init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#init-3)，使用私钥（PriKey）初始化Sign实例。
7. 调用[Sign.sign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#sign-1)，生成摘要数据签名。

**验签**
1. 调用[cryptoFramework.createVerify](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreateverify)，指定字符串参数'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify'，创建非对称密钥类型为RSA、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1_SHA256，验签模式为OnlyVerify的Verify实例，用于完成验签操作。
2. 调用[Verify.init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#init-5)，使用公钥（PubKey）初始化Verify实例。
3. 调用[Verify.verify](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#verify-1)，对摘要数据进行验签。

 - 异步方法示例：

  
```ArkTS
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function signMessagePromise(priKey: cryptoFramework.PriKey, digestBlob: cryptoFramework.DataBlob) {
  let signAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlySign';
  let signer = cryptoFramework.createSign(signAlg);
  await signer.init(priKey);
  let signData = await signer.sign(digestBlob);
  return signData;
}

async function verifyMessagePromise(digestBlob: cryptoFramework.DataBlob, signMessageBlob: cryptoFramework.DataBlob,
  pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  await verifier.init(pubKey);
  let res = await verifier.verify(digestBlob, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}

async function main() {
  let messageData: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is rsa onlySign test', 'utf-8').buffer) };
  // 先使用 Md 计算 SHA256 摘要（32字节）
  let md = cryptoFramework.createMd('SHA256');
  await md.update(messageData);
  let digestBlob = await md.digest();
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = await generator.generateKeyPair();
  let signData = await signMessagePromise(keyPair.priKey, digestBlob);
  let verifyResult = await verifyMessagePromise(digestBlob, signData, keyPair.pubKey);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}
```

 - 同步方法示例：

  
```ArkTS
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function signMessagePromise(priKey: cryptoFramework.PriKey, digestBlob: cryptoFramework.DataBlob) {
  let signAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlySign';
  let signer = cryptoFramework.createSign(signAlg);
  signer.initSync(priKey);
  let signData = signer.signSync(digestBlob);
  return signData;
}

function verifyMessagePromise(digestBlob: cryptoFramework.DataBlob, signMessageBlob: cryptoFramework.DataBlob,
  pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  verifier.initSync(pubKey);
  let res = verifier.verifySync(digestBlob, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}

function main() {
  let messageData: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is rsa onlySign test', 'utf-8').buffer) };
  // 先使用 Md 计算 SHA256 摘要（32字节）
  let md = cryptoFramework.createMd('SHA256');
  md.updateSync(messageData);
  let digestBlob = md.digestSync();
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = generator.generateKeyPairSync();
  let signData = signMessagePromise(keyPair.priKey, digestBlob);
  let verifyResult = verifyMessagePromise(digestBlob, signData, keyPair.pubKey);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}
```
