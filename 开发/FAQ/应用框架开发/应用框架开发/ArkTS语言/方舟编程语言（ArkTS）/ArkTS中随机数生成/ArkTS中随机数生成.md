# ArkTS中随机数生成

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-157

#### 问题现象

在ArkTS中如何生成随机数（如用作字段唯一标识的uuid等）？如何生成安全的随机数字字符串？
 
 

#### 背景知识

- **安全的随机数定义**。安全的随机数是指那些难以预测且符合统计随机性的随机数，通常用于加密应用中对安全性要求极高的场景。这些随机数必须满足以下条件：

  **不可预测性**：即使攻击者知道生成随机数的算法及其之前的输出，也无法预测下一个随机数。

  **统计随机性**：随机数序列在统计上应该接近均匀分布，不应表现出任何可识别的模式或偏差。

  **计算效率**：生成随机数的速度应足够快，以满足实际应用的需求。

  **抗攻击性**：能够抵御各种已知的随机数预测攻击，如线性同余生成器（LCG）攻击等。

  常见的用于生成安全随机数的方法：

  
CTR_DRBG（Counter-based Deterministic Random Bit Generator）是一种基于计数器的确定性随机位生成器，广泛应用于密码学和安全领域。CTR_DRBG是NIST（美国国家标准与技术研究院）在SP800-90A和SP800-90B中定义的一种标准随机数生成算法。

 
- 它基于一个初始化向量（IV）和一个密钥来生成伪随机数。CTR_DRBG的设计使得它能够高效地生成大量伪随机数，并且具有良好的统计特性和安全性。

 
 
- **ArkTS中生成随机数**。
**安全要求不高的场景**：可通过工具类util中的接口【util.generateRandomUUID】生成随机的RFC 4122版本4的【string】类型UUID。

  也可以使用【util.generateRandomBinaryUUID】接口生成随机的RFC 4122版本4的【Uint8Array】类型UUID。

 
- **安全要求高的场景**：加解密算法库框架【@ohos.security.cryptoFramework】包提供了安全生成随机数能力，目前支持随机数生成算法（只支持CTR_DRBG算法规格）。

 
> [!NOTE]
> 随机数生成算法目前支持生成长度为[1,INT_MAX]的安全随机数，长度单位为byte。 随机数生成算法使用openssl的RAND_priv_bytes接口生成安全随机数。

 
 
 

#### 解决方案

- 针对安全要求不高的场景（如唯一标识的uuid字符串生成）可以借助工具包@ohos.util提供的随机数生成api。
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">util </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span>

class <span style="color: rgb(0,0,255);">ConstantUtils </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用此函数会生成两个</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">，其中一个</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">进行缓存，一个</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">用于输出</span></em>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">首次调用时，参数是</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">或</span><span style="color: rgb(128,128,128);">false</span><span style="color: rgb(128,128,128);">无区别；下次调用时，如果参数是</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">，依旧缓存上次</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">，并生成新的</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">；如果参数是</span><span style="color: rgb(128,128,128);">false</span><span style="color: rgb(128,128,128);">，将生成两个</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">，其中一个</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">进行缓存，一个</span><span style="color: rgb(128,128,128);">UUID</span><span style="color: rgb(128,128,128);">进行输出</span></em>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">默认</span><span style="color: rgb(128,128,128);">true</span></em>
  <span style="color: rgb(0,0,255);">uuid1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandomUUID</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">uuid2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandomUUID</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>// </em><em><span style="color: rgb(128,128,128);">返回</span><span style="color: rgb(128,128,128);">Uint8Array</span><span style="color: rgb(128,128,128);">类型，参数同</span><span style="color: rgb(128,128,128);">generateRandomUUID</span></em>
  <span style="color: rgb(0,0,255);">uuid3</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Uint8Array </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandomBinaryUUID</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">uuid4</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandomBinaryUUID</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
- 对于安全要求比较高的场景，推荐使用加解密算法库框架@ohos.security.cryptoFramework包生成安全随机数，操作步骤如下：1. 通过接口createRandom生成随机数操作实例。

2. 接受输入长度，通过接口generateRandom，生成指定长度的随机数。

3. 接受DataBlob数据，通过接口setSeed，为随机数生成池设置种子。
```text
import <span style="color: rgb(0,0,255);">cryptoFramework </span>from <span style="color: rgb(255,0,170);">'@ohos.security.cryptoFramework'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos.base'</span><span style="color: rgb(181,106,1);">;</span>

<em>// Generate a random number in promise mode</em>
function <span style="color: rgb(0,0,255);">doRandByPromise</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">rand </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createRandom</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">len </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">; </span><em>// Generate a 4-byte random number</em>
  let <span style="color: rgb(0,0,255);">promiseGenerateRand </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">rand</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandom</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">len</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">promiseGenerateRand</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">randData </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[Promise]: rand result: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">randData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">rand</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setSeed</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">randData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`setSeed failed, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[Promise]: error: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// Generate a random number in callback mode</em>
function <span style="color: rgb(0,0,255);">doRandByCallback</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">rand </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createRandom</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">len </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">; </span><em>// Generate a 4-byte random number</em>
  <span style="color: rgb(0,0,255);">rand</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandom</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">len</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">randData</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[Callback]: err: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[Callback]: generate random result: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">randData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      try <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">rand</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setSeed</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">randData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        let <span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`setSeed failed, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// Generate a random number synchronously</em>
function <span style="color: rgb(0,0,255);">doRandBySync</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">rand </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createRandom</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">len </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// Generate a 24-byte random number</span></em>
  try <span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">randData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">rand</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandomSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">len</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">randData </span><span style="color: rgb(181,106,1);">!= </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[Sync]: rand result: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">randData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'[Sync]: get rand result fail!'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  } </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`do rand failed, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
上面的方法1【doRandBySync】中，【rand.generateRandomSync】用于“同步生成指定长度的随机数”；它的参数是指定生成随机数的长度，单位为字节，范围在1到INT_MAX之间。
 
该方法会同步生成指定长度的随机数，并返回一个DataBlob对象；返回的DataBlob对象中存储了生成的随机数，而DataBlob对象是一个字节数组，可以包含多个字节。当前随机数只能指定长度，无法指定范围，可以将得到的随机数自定义范围。
 
```text
let <span style="color: rgb(0,0,255);">rand </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">cryptoFramework</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createRandom</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<em>// </em><em><span style="color: rgb(128,128,128);">设置生成随机数的字节长度为</span><span style="color: rgb(128,128,128);">1</span></em>
let <span style="color: rgb(0,0,255);">randData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">rand</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandomSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<em>// </em><em><span style="color: rgb(128,128,128);">自定义范围</span><span style="color: rgb(128,128,128);">(0-10</span><span style="color: rgb(128,128,128);">之内</span></em><em>)</em>
let <span style="color: rgb(0,0,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">randData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">255</span><span style="color: rgb(181,106,1);">;</span>
console.info<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">随机数</span><span style="color: rgb(255,0,170);">:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">num</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
