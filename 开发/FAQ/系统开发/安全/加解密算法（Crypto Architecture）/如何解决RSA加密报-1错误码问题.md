# 如何解决RSA加密报-1错误码问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-48

#### 问题现象

使用RSA加密算法进行加密，执行后报-1错误码是什么原因？如何解决？
 
RSA公钥参数如下：
 
```text
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCuo5/hnnCOAERqdJwQM6Uwo2FZ
Gq/JHKRj43QnxxnxUIhnwaHH7PUv8V2v8pNdJl5NYD6qiEiD7i59HI0G5PSj3gjZ
4KuHy/RIN95BZyLtrg2BKzNiGvUV4IPFzE9ZAe0fcEvDPxGZn/vRWLRnQaEeYehc
OUkt2vbKPLwtTWKwzQIDAQAB
-----END PUBLIC KEY-----
```
 
报错信息截图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/q8t_gVLoSfS35ABXJcJNLw/zh-cn_image_0000002658848479.png?HW-CC-KV=V1&HW-CC-Date=20260701T041424Z&HW-CC-Expire=86400&HW-CC-Sign=9AFB4C0BF6997E0189950AA18426A09343599754A675609C56E0E843D116765E)

 
```text
code = "-1"
message = "The input string contains unsupported characters"
```
 
 

#### 背景知识

[RSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec#rsa)是一种非对称加解密算法，使用RSA算法进行加解密可以参考[使用RSA非对称密钥（PKCS1模式）加解密(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1)。
 
- 创建非对称密钥生成器实例API：[cryptoFramework.createAsyKeyGenerator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreateasykeygenerator)。
- 非对称密钥生成器密钥API：[AsyKeyGenerator.generateKeyPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#generatekeypair-1)。
- 创建加解密实例API：[cryptoFramework.createCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatecipher)。
- 初始化加解密实例对象API：[Cipher.init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#init-1)。
- 执行并结束加解密API：[Cipher.doFinal](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#dofinal-1)。

 
 

#### 问题定位
1. 分析错误码-1，使用RSA加密时遇到错误码-1，这通常表示“ERR_UNEXPECTED”，即遇到了一个未被预期或未被特定处理的问题。
2. 根据错误提示信息“The input string contains unsupported characters”可以进一步判断出报错原因是因为输入参数错误。
3. RSA公钥加密输入参数为公钥和明文，明文传入后转换为Uint8Array数据类型，排除明文参数错误，可以确认报错是由传入的公钥参数导致。
4. 公钥数据中除公钥外尚有开头和结尾的标识符字符串，而RSA加密只需要公钥，最终可以确认报-1错误码是因为没有去除公钥数据首尾标识符导致。
 
 

#### 分析结论

RSA加密报-1错误码是因为没有对公钥数据进行去除首尾标识符，从而传入了错误的公钥参数，导致加密方法解析公钥参数失败。
 
 

#### 修改建议

将公钥数据去除'-----BEGIN PUBLIC KEY-----'和'-----END PUBLIC KEY-----'标识符后作为公钥参数执行RSA加密。
 
完整示例代码如下：
 
```text
import { buffer, util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';


<em>// RSA pubKey example. 实际使用需要更换自己的公钥PEM</em>
const pubKeyStr = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCuo5/hnnCOAERqdJwQM6Uwo2FZ\n' +
  'Gq/JHKRj43QnxxnxUIhnwaHH7PUv8V2v8pNdJl5NYD6qiEiD7i59HI0G5PSj3gjZ\n' +
  '4KuHy/RIN95BZyLtrg2BKzNiGvUV4IPFzE9ZAe0fcEvDPxGZn/vRWLRnQaEeYehc\n' +
  'OUkt2vbKPLwtTWKwzQIDAQAB';


<em>// RSA加密方法</em>
async function encryptRSA(message: string, pubKeyStr: string) {
  try {
    <em>// 初始化Base64工具实例</em>
    let base64Helper = new util.Base64Helper();
  <em>  // 公钥转换为Uint8Array，然后包装为DataBlob类型</em>
    let pubKeyBlob: cryptoFramework.DataBlob = { data: base64Helper.decodeSync(pubKeyStr) };
 <em>   // 创建RSA key生成器</em>
    let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
   <em> // 将公钥包装数据pubKeyBlob转换成密钥对类型KeyPair</em>
    let keyPair = await rsaGenerator.convertKey(pubKeyBlob, null);
   <em> // 创建Cipher对象</em>
    let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
    <em>// 初始化加密模式，指定密钥keyPair.pubKey</em>
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyPair.pubKey, null);
   <em> // 包装要加密的明文</em>
    let plainTextBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    <em>// 传入明文，获取加密后的数据</em>
    let encryptBlob = await cipher.doFinal(plainTextBlob);
   <em> // 返回加密后的字符串</em>
<em>    // return base64Helper.encodeToStringSync(encryptBlob.data);</em>
    console.info(`base64Helper: ${base64Helper.encodeToStringSync(encryptBlob.data)}`);
  } catch (e) {
    console.error('[base64Helper] error');
  }
  return undefined;
}


@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('RSA加密')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          encryptRSA('This is a test demo.', pubKeyStr);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
 
 

#### 总结

方法报错问题可以根据错误码和错误提示进行判断错误原因，进行排查修改。
