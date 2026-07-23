# 如何解决createX509Cert读取证书文件获取的PublicKey使用报错问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-certificate-4

#### 问题现象

使用certFramework的createX509Cert读取证书文件，使用getPublicKey方法可以成功获取到公钥，但使用此公钥进行初始化报错。
 
```text
let <span style="color: rgb(0,0,255);">publicKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">x509Cert</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPublicKey</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span>
<em>// </em><em><span style="color: rgb(128,128,128);">创建实例化对象</span></em>
let <span style="color: rgb(0,0,255);">cipher </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createCipher</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'RSA1024|PKCS1'</span><span style="color: rgb(0,0,255);">)</span>
<em>// </em><em><span style="color: rgb(128,128,128);">初始化加解密对象</span></em>
<span style="color: rgb(0,0,255);">cipher</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CryptoMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ENCRYPT_MODE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">publicKey</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(0,0,255);">)</span>
```
 
 

#### 背景知识

- 创建X509证书对象：[cert.createX509Cert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert#certcreatex509cert)。
- 获取X509证书公钥：[x509Cert.getPublicKey()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert#getpublickey)。
- 同步获取指定数据生成非对称密钥：[AsyKeyGenerator.convertKeySync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#convertkeysync12-1)。
- 初始化加解密的cipher对象：[cipher.init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#init-1)。

 
 

#### 问题定位
1. 确认获取的公钥是否满足RSA公钥格式。
2. 获取到的公钥有没有加载到RSA密钥对象中。
 
 

#### 分析结论

虽然成功获取到证书中的公钥，但没有将公钥数据通过convertKey方法生成RSA公钥进而加载到密钥对象中，就直接使用此公钥进行初始化操作，导致公钥参数错误引发初始化报错。
 
 

#### 修改建议

将读取证书获取的公钥数据，通过convertKey方法生成RSA公钥，然后再使用此公钥进行初始化、加密数据等操作。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">cryptoFramework </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CryptoArchitectureKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">certFramework </span>from <span style="color: rgb(255,0,170);">'@ohos.security.cert'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">cert </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.DeviceCertificateKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">buffer </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">stringToUint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Uint8Array </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">j </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">j</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">charCodeAt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  return new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

function <span style="color: rgb(0,0,255);">create509</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">encodingBlob</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">certFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">EncodingBlob</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">cb</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">s</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">errorCB</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">certFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createX509Cert</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">encodingBlob</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">x509Cert </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">publicKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">x509Cert</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPublicKey</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'createX509Cert success: publicKey = ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">publicKey</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进行密钥转换</span></em>
    let <span style="color: rgb(0,0,255);">rsaGenerator </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAsyKeyGenerator</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'RSA1024'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">keyPair </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">rsaGenerator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">convertKeySync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">x509Cert</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPublicKey</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建实例化对象</span></em>
    let <span style="color: rgb(0,0,255);">cipher </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createCipher</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'RSA1024|PKCS1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">初始化加解密对象</span></em>
    await <span style="color: rgb(0,0,255);">cipher</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CryptoMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ENCRYPT_MODE</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">keyPair</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    let <span style="color: rgb(0,0,255);">sha1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'32**************d7'</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">plainText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DataBlob </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">sha1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'utf-8'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">cipher</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">doFinal</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">plainText</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'encryptData: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">cb</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'ok'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'error'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">errorCB</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'createX509Cert failed, errCode: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">', errMsg: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">errorCB</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CreateX509Cert </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State</span>
  <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">证书二进制数据，需业务自行赋值。</span></em>
    let <span style="color: rgb(0,0,255);">certData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'-----BEGIN CERTIFICATE-----</span>\r\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(255,0,170);">'-----END CERTIFICATE-----'</span><span style="color: rgb(181,106,1);">;</span>

    let <span style="color: rgb(0,0,255);">encodingBlob</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cert</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">EncodingBlob </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">stringToUint8Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">certData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根据</span><span style="color: rgb(128,128,128);">encodingData</span><span style="color: rgb(128,128,128);">的格式进行赋值，支持</span><span style="color: rgb(128,128,128);">FORMAT_PEM</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">FORMAT_DER</span><span style="color: rgb(128,128,128);">。</span></em>
      <span style="color: rgb(0,0,255);">encodingFormat</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cert</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">EncodingFormat</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">FORMAT_PEM</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">create509</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">encodingBlob</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'ok'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'error:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 总结

使用证书中的公钥数据进行加解密相关操作，需要注意中间流程的公钥数据流转与转换，避免使用错误的公钥数据进行相关操作，相关API的使用需要满足其使用条件。
