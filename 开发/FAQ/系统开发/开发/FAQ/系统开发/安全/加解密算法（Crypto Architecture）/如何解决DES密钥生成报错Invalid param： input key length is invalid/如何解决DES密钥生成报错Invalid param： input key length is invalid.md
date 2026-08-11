# 如何解决DES密钥生成报错Invalid param: input key length is invalid

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-40

#### 问题现象

使用密钥材料“TESTXXXX”进行DES加密，调用[SymKeyGenerator.convertKeySync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#convertkeysync12)生成密钥时报错：
 
```text
<span style="color: rgb(0,0,255);">ConvertSymmKey</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">316</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Invalid </span><span style="color: rgb(181,106,1);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">input key length is invalid</span><span style="color: rgb(181,106,1);">!</span>
```
 
 

#### 背景知识

对称加密算法密钥长度必须按[对称密钥生成和转换规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec)中密钥长度提供，如果密钥长度不足，需要在末尾补'\0'填充长度。
 
 

#### 问题定位

运行以下代码，使用密钥进行DES加密时报错如下图所示，根据报错信息可以判断是Key长度问题引起。
 
```text
const <span style="color: rgb(0,0,255);">keyData </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextEncoder</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">encodeInto</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TESTXXXX'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">symKeyGenerator </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSymKeyGenerator</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'3DES192'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">symKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">symKeyGenerator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">convertKeySync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">keyData</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
报错如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Yz17j9cnQ7eRY7L0RfF9lA/zh-cn_image_0000002628768360.png?HW-CC-KV=V1&HW-CC-Date=20260811T005925Z&HW-CC-Expire=86400&HW-CC-Sign=44ABC9984A84B4FE357A8311F7F5088D0D617C4C09C9645BEDCE55049BCE8C97)

 
 

#### 分析结论

参考背景知识中3DES算法规格的介绍，要求密钥长度必须为192位，即24个字节。而问题代码中的密钥材料“TESTXXXX”只有8个字节，因此需要用'\0'补充剩余长度。
  
| 对称密钥算法 | 密钥长度（bit） | 字符串参数 |
| --- | --- | --- |
| 3DES | 192 | 3DES192 |
 
 
 

#### 修改建议

通过padEnd()补齐密钥长度，该方法会将当前字符串从末尾开始填充给定的字符串（如果需要会重复填充），直到达到给定的长度。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">util </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">cryptoFramework </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CryptoArchitectureKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SolutionOfDESKeyGenerationFailed </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello World'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'HelloWorld'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Welcome'</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(0,0,255);">keyData </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextEncoder</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">encodeInto</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'TESTXXXX'</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padEnd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'0'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">symKeyGenerator </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSymKeyGenerator</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'3DES192'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(0,0,255);">symKey </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">symKeyGenerator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">convertKeySync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">keyData</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'TAG'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`symKey: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">symKey</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
