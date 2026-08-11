# 如何使用DSA算法实现签名验签的功能

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-44

#### 问题现象

想要使用DSA算法实现[签名验签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-overview)的功能，具体代码是怎样实现的呢？
 
 

#### 背景知识

- [DSA](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-overview#dsa)：DSA（Digital Signature Algorithm，数字签名算法）的安全性基于整数有限域离散对数问题的困难性，具有较好的兼容性和适用性。
- [createAsyKeyGeneratorBySpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreateasykeygeneratorbyspec10)：指定密钥参数，获取非对称密钥生成器实例。
- 签名验签：当需要判断接收的数据是否被篡改、数据是否为指定对象发送的数据时，可以使用签名验签操作。

 
 

#### 解决方案
1. 配置DSA1024公钥和私钥中包含的公共参数dsaCommonSpec。
2. 设置DSA1024密钥对中包含的全参数。
3. 调用createAsyKeyGeneratorBySpec方法生成DSA算法的非对称密钥生成器。
4. 通过密钥生成器生成DSA非对称密钥对。
5. 使用DSA私钥对数据进行签名。
6. 使用DSA公钥对签名数据进行验签。
 
流程图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/qP9gRDfkTW-4DnuYGoSonQ/zh-cn_image_0000002658968429.png?HW-CC-KV=V1&HW-CC-Date=20260811T005923Z&HW-CC-Expire=86400&HW-CC-Sign=397E75F12BA8C4E0BA5FD3ECE88EAAF05C3AA00C2E4CC5E45F70D8710BB718BA)

 
完整示例参考如下：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">cryptoFramework </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.CryptoArchitectureKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">buffer </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hilog </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>

let <span style="color: rgb(255,255,255);">input</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DataBlob </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'This is Sign test plan'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'utf-8'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">配置</span><span style="color: rgb(128,128,128);">DSA1024</span><span style="color: rgb(128,128,128);">公钥和私钥中包含的公共参数</span></em>
function <span style="color: rgb(0,0,255);">genDsa1024CommonSpecBigE</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">dsaCommonSpec</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DSACommonParamsSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">algName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'DSA'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">specType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AsyKeySpecType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">COMMON_PARAMS_SPEC</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">p</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">q</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">g</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">dsaCommonSpec</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">DSA1024</span><span style="color: rgb(128,128,128);">密钥对中包含的全参数</span></em>
function <span style="color: rgb(0,0,255);">genDsa1024KeyPairSpecBigE</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">dsaCommonSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">genDsa1024CommonSpecBigE</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">dsaKeyPairSpec</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DSAKeyPairSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">algName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'DSA'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">specType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AsyKeySpecType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">KEY_PAIR_SPEC</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">dsaCommonSpec</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">sk</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">pk</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">dsaKeyPairSpec</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

async function <span style="color: rgb(0,0,255);">signMessagePromise</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">priKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PriKey</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">signAlg </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'DSA3702|SHA256'</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">signer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">signAlg</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  await <span style="color: rgb(255,255,255);">signer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">priKey</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">signData </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">signer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">input</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">signData</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

async function <span style="color: rgb(0,0,255);">verifyMessagePromise</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">signMessageBlob</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DataBlob</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">pubKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PubKey</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">verifyAlg </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'DSA3702|SHA256'</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">verifier </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createVerify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">verifyAlg</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  await <span style="color: rgb(255,255,255);">verifier</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">pubKey</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">res </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">verifier</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">verify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">input</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">signMessageBlob</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'test'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'DSA verify result is ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">res</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">res</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

function <span style="color: rgb(0,0,255);">main</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">asyKeyPairSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">genDsa1024KeyPairSpecBigE</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">asyKeyGeneratorBySpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAsyKeyGeneratorBySpec</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">asyKeyPairSpec</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">异步获取非对称密钥生成器生成的密钥</span></em>
  <span style="color: rgb(255,255,255);">asyKeyGeneratorBySpec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPair</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">keyPair</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'test'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'generateKeyPair: error.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'test'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'generateKeyPair: success.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">签名</span></em>
    let <span style="color: rgb(255,255,255);">signData </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">signMessagePromise</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">keyPair</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">priKey</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">验签</span></em>
    let <span style="color: rgb(255,255,255);">verifyResult </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">verifyMessagePromise</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">signData</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">keyPair</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pubKey</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">verifyResult </span><span style="color: rgb(181,106,1);">=== </span>true<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'test'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'verify success'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'test'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'verify failed'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">DSA </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击进行验证</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">main</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
