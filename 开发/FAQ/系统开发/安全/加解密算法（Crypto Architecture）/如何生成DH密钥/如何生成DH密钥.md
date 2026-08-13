# 如何生成DH密钥

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-51

#### 问题现象

如何生成DH密钥，需要有实现生成DH密钥的具体流程和代码示例。
 
 

#### 背景知识

- DH算法介绍：[DH](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#dh)（Diffie–Hellman key exchange），是一种密钥协商算法，只涉及公钥的交换，它可以提供前向安全性，即使在通信渠道被监听的情况下，也不会暴露双方的私钥。当前支持使用字符串参数和密钥参数两种方式生成DH密钥，且支持根据素数长度和私钥长度生成公共密钥参数。

 
- DH算法规格介绍：
场景一：[使用字符串参数生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#使用字符串参数生成-6)。
- 场景二：[使用密钥参数生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#使用密钥参数生成-6)。

 - DH算法相关接口介绍。

| 名称 | 接口 |
| --- | --- |
| 指定DH算法公共参数。 | DHCommonParamsSpec |
| 指定DH算法私钥参数。 | DHPriKeySpec |
| 指定DH算法公钥参数。 | DHPubKeySpec |
| 指定DH算法全量参数。 | DHKeyPairSpec |
| 通过指定密钥参数，创建非对称密钥生成器。 | createAsyKeyGeneratorBySpec |
| 通过指定算法名称的字符串，创建非对称密钥生成器。 | createAsyKeyGenerator |

 
 

#### 解决方案

- 场景一：调用createAsyKeyGenerator接口通过DH字符串参数生成DH密钥对.
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">cryptoFramework </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CryptoArchitectureKit'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">使用字符串参数生成</span><span style="color: rgb(128,128,128);">DH</span></em><em>密钥</em><span style="color: rgb(128,128,128);">对</span>
export function <span style="color: rgb(0,0,255);">getDHKeyFromStringParams</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  try <span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// 1</span><span style="color: rgb(128,128,128);">、生成密钥对</span></em>
    let <span style="color: rgb(0,0,255);">spec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAsyKeyGenerator</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'DH_modp2048'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">pubKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">priKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromStringparams success, DH public key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromStringparams success, DH priKey key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 场景二：使用密钥参数生成DH密钥。1. 调用DHCommonParamsSpec接口通过p、g、l参数生成密钥公共参数DHCommonParamsSpec。

2. 调用DHKeyPairSpec接口通过私钥参数、公钥参数和公共参数生成DH密钥参数DHKeyPairSpec。

3. 调用createAsyKeyGeneratorBySpec接口通过DH密钥参数生成DH密钥对。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">使用密钥参数生成</span><span style="color: rgb(128,128,128);">DH</span><span style="color: rgb(128,128,128);">密钥对</span></em>
export function <span style="color: rgb(0,0,255);">getDHKeyFromParams</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  try <span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// 1</span><span style="color: rgb(128,128,128);">、生成公共参数</span></em>
    let <span style="color: rgb(0,0,255);">dHCommonParamsSpec</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DHCommonParamsSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">参数仅用于示例，按照实际填写</span></em>
      <span style="color: rgb(0,0,255);">p</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">g</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">l</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">192</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">algName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'DH'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">specType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyKeySpecType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">COMMON_PARAMS_SPEC</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// 2</span><span style="color: rgb(128,128,128);">、生成密钥对参数</span></em>
    let <span style="color: rgb(0,0,255);">dHKeyPairSpec</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DHKeyPairSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">参数仅用于示例，按照实际填写</span></em>
      <span style="color: rgb(0,0,255);">sk</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">pk</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">dHCommonParamsSpec</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">algName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'DH'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">specType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyKeySpecType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">KEY_PAIR_SPEC</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// 3</span><span style="color: rgb(128,128,128);">、生成密钥对</span></em>
    let <span style="color: rgb(0,0,255);">spec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAsyKeyGeneratorBySpec</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">dHKeyPairSpec</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">pubKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">priKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromparams success, DH public key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromparams success, DH priKey key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromparams failed`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


  完整示例参考如下：

  
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">cryptoFramework </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CryptoArchitectureKit'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">使用字符串参数生成</span><span style="color: rgb(128,128,128);">DH</span><span style="color: rgb(128,128,128);">密钥对</span></em>
export function <span style="color: rgb(0,0,255);">getDHKeyFromStringParams</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  try <span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// 1</span><span style="color: rgb(128,128,128);">、生成密钥对</span></em>
    let <span style="color: rgb(0,0,255);">spec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAsyKeyGenerator</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'DH_modp2048'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">pubKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">priKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromStringparams success, DH public key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromStringparams success, DH priKey key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">使用密钥参数生成</span><span style="color: rgb(128,128,128);">DH</span><span style="color: rgb(128,128,128);">密钥对</span></em>
export function <span style="color: rgb(0,0,255);">getDHKeyFromParams</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  try <span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// 1</span><span style="color: rgb(128,128,128);">、生成公共参数</span></em>
    let <span style="color: rgb(0,0,255);">dHCommonParamsSpec</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DHCommonParamsSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">参数仅用于示例，按照实际填写</span></em>
      <span style="color: rgb(0,0,255);">p</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">g</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">l</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">192</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">algName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'DH'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">specType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyKeySpecType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">COMMON_PARAMS_SPEC</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <em>// 2</em><em><span style="color: rgb(128,128,128);">、生成密钥对参数</span></em>
    let <span style="color: rgb(0,0,255);">dHKeyPairSpec</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DHKeyPairSpec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">参数仅用于示例，按照实际填写</span></em>
      <span style="color: rgb(0,0,255);">sk</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">pk</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BigInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">dHCommonParamsSpec</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">algName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'DH'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">specType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyKeySpecType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">KEY_PAIR_SPEC</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// 3</span><span style="color: rgb(128,128,128);">、生成密钥对</span></em>
    let <span style="color: rgb(0,0,255);">spec </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAsyKeyGeneratorBySpec</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">dHKeyPairSpec</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">pubKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">priKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">spec</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyPairSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEncoded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromparams success, DH public key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">pubKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromparams success, DH priKey key = </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">priKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getDHKeyFromparams failed`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Hello World'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'HelloWorld'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">getDHKeyFromStringParams</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">getDHKeyFromParams</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
 

#### 常见FAQ

Q： 使用密钥参数生成DH密钥对参数l有限制吗？
 
A： 私钥长度l为可选参数，默认为0，l值的设置范围需大于2*(96+(素数P位数-1)/1024*16)。
 
Q： 使用密钥参数生成DH密钥对参数p有限制吗？
 
A： 素数p的比特长度必须大于等于512，小于等于10000。
 
 

#### 总结

DH算法生成密钥可以通过使用字符串参数和使用密钥参数两种方式生成。
