# 3DES加密实现兼容java的解密

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-49

#### 问题现象

ArkTS中使用3DES加密算法加密的数据在java侧无法解密，如何解决该问题。
 
 

#### 背景知识

3DES算法的加解密过程分别是对明文/密文数据进行三次DES加密或解密，得到相应的密文或明文。
 
当前支持以字符串参数完成3DES加解密，具体的“字符串参数”由“对称密钥类型（加解密算法+密钥长度）”、“分组模式”和“填充模式”使用符号“|”拼接而成，用于在创建对称加解密实例时，指定算法规格。
 
 

#### 解决方案

ArkTS在生成密文后，需要使用base64的util.Type.BASIC生成无换行符的字符串后传递到java侧进行解密。提供ArkTS代码和java代码。
 
ArkTS侧对“This is a test”进行加密：
```text
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  message: string = '加密';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('encrypt')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          encrypt_3DES();
        })
    }
    .height('100%')
    .width('100%')
  }
}

<em>/**</em>
<em> * 加密消息</em>
<em> *</em>
<em> * @param symKey symKey</em>
<em> * @param plainText plainText</em>
<em> * @returns 加密后的内容</em>
<em> */</em>
async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('3DES192|ECB|PKCS7');
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
  let encryptData = await cipher.doFinal(plainText);
  return encryptData;
}

<em>/**</em>
<em> * 通过key data值获取symKey</em>
<em> * @param symKeyData keyData</em>
<em> * @returns void</em>
<em> */</em>
async function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let symGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let symKey = await symGenerator.convertKey(symKeyBlob);
  console.info('convertKey success');
  return symKey;
}

<em>/**</em>
<em> * 将uint8转换为 string值</em>
<em> * @param uint Uint8Array值</em>
<em> * @returns string值</em>
<em> */</em>
function uint8ToString(uint: Uint8Array): string {
  let base64Helper = new util.Base64Helper();
  let result = base64Helper.encodeToStringSync(uint, util.Type.BASIC);
  console.info('result = ', result);
  return result;

}

<em>/**</em>
<em> * 3DES_ECB模式加密</em>
<em> */</em>
export async function encrypt_3DES() {
 <em> // 此处填写实际值</em>
  let keyData =
    new Uint8Array([238, 249, 61, 55, 128, 220, 183, 224, 139, 253, 248, 239, 239, 41, 71, 25, 235, 206, 230, 162, 249,
      27, 234, 114]);
  <em>// 获取symKey</em>
  let symKey = await genSymKeyByData(keyData);
 <em> // 待加密的信息</em>
  let message = 'This is a test';
 <em> // 将待加密的信息转换为plainText</em>
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
 <em> // 生成加密后的密文</em>
  let encryptText = await encryptMessagePromise(symKey, plainText);
  console.info('encrypt:', uint8ToString(encryptText.data));
}
```
 
 
java侧对加密后的信息“7hp/cpn6R+5adY0ALFfktw==”进行解密：
```text
package org.example;
import org.apache.commons.codec.binary.Base64;
import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class Triple_DES {
   <em> // key值</em>
    private static String keyString="7vk9N4Dct+CL/fjv7ylHGevO5qL5G+py";
   <em> // 待解密的字符串信息</em>
    private static String encryptData="7hp/cpn6R+5adY0ALFfktw==";

   <em> /**</em>
<em>     * 获取解密密钥</em>
<em>     *</em>
<em>     * @return SecretKey</em>
<em>     */</em>
    public static SecretKey makePrivateKey(){
        byte[] keyBytes = Base64.decodeBase64(keyString);
        return new SecretKeySpec(keyBytes, "DESede");
    }

  <em>  /**</em>
<em>     * 解密</em>
<em>     */</em>
    public static String decrypt(SecretKey key) throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {
        Cipher cipher = Cipher.getInstance("DESede/ECB/PKCS5Padding"); <em>// 注意：ECB模式不安全，推荐使用CBC模式并传入IV</em>
        cipher.init(Cipher.DECRYPT_MODE, key);
        String encryptedData = encryptData;<em> // 加密后的数据，通常是Base64编码的字符串</em>
        byte[] encryptedBytes = Base64.decodeBase64(encryptedData);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        return new String(decryptedBytes);
    }

    public static void main(String[] args) throws NoSuchPaddingException, IllegalBlockSizeException, NoSuchAlgorithmException, BadPaddingException, InvalidKeyException {
        System.out.println(decrypt(makePrivateKey()));
    }

}
```
