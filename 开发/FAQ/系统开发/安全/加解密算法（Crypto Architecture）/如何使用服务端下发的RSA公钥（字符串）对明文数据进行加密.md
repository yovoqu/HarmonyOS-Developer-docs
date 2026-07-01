# 如何使用服务端下发的RSA公钥（字符串）对明文数据进行加密

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-3

将服务器下发的RSA公钥字符串赋值给`pubKeyStr`，即可实现。具体代码参考如下：
 
```text
import { buffer, util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
<em>/**</em>
<em> * Encrypt using RSA asymmetric key (PKCS1 mode)</em>
<em> * @param message Clear text data to be encrypted</em>
<em> * @returns Encrypted string, encoded in base64 format</em>
<em> */</em>
export async function encryptRSA(message: string) {
  <em>// Server issues RSA public key string (base64 encoding)</em>
  let pubKeyStr = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDFQArGDm5BXM4jHHuZGIb/kUoqrSjXkjqPLgrDmqBFxNyYsyxvyFRO10nStQwdRkQkh5lZ5sqC1G/z6lyDPpEySTBo9S5GLZ2Tj4yinNjcMXmOwiHfyQAQo9LwdlyTedwRchg0fYewWBVTVhGcWPowT1aA+GnQhYwNmaS/iKQsNQIDAQAB";
  <em>// Initialize Base64 tool instance</em>
  let base64Helper = new util.Base64Helper();
  <em>// Convert the public key to Uint8Array and package it as a DataBlob type</em>
  let pubKeyBlob: cryptoFramework.DataBlob = { data: base64Helper.decodeSync(pubKeyStr) };
  <em>// Create RSA key generator</em>
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  <em>// Convert the public key wrapper data pubKeyBlob into a key pair type KeyPair</em>
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, null);
  <em>// Create a Cipher object</em>
  let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
  <em>// Initialize encryption mode and specify the key keyPair. pubKey</em>
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyPair.pubKey, null);
  <em>// Packaging requires encrypted plaintext</em>
  let plainTextBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  <em>// Pass in plaintext and retrieve encrypted data</em>
  let encryptBlob = await cipher.doFinal(plainTextBlob);
  <em>// Return encrypted string</em>
  return base64Helper.encodeToStringSync(encryptBlob.data);
}
```
 
**参考链接**
 
[使用RSA非对称密钥（PKCS1模式）加解密](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1)
