# 关于huks.exportKeyItem函数401报错的原因

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-14

#### 问题现象

huks.exportKeyItem导出密钥时，总是报401，Invalid parameters.部分代码如下。加密算法使用的为AES，RSA和SM4算法。
 
- 方法generateKey。
```text
export async function <span style="color: rgb(0,0,255);">generateKey</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksParam</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">getGenerateProperties</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根据所选模式进行切换算法</span></em>
  let <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">properties</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(0,0,255);">exportOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">inData</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(0,0,255);">([])</span>
  <span style="color: rgb(255,0,170);">}</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">确认</span><span style="color: rgb(128,128,128);">Key</span><span style="color: rgb(128,128,128);">是否存在</span></em>
  <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isKeyItemExist</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">keyAlias</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">, </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      try <span style="color: rgb(255,0,170);">{</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">导出密钥</span></em>
        <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">exportKeyItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">keyAlias</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">HuksPropertiesConstants</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">EMPTY_OPTION</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">isInit </span><span style="color: rgb(181,106,1);">= </span>false
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">isInit </span><span style="color: rgb(181,106,1);">= </span>true
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">isInit </span><span style="color: rgb(181,106,1);">= </span>false
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    } </span>else <span style="color: rgb(255,0,170);">{</span>
      await <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateKeyItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">keyAlias</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span>
      await <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">importKeyItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">keyAlias</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
- 方法encryptData。
```text
export async function <span style="color: rgb(0,0,255);">encryptData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">plainText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">isInit</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">generateKey</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
 <em> // <span style="color: rgb(181,106,1);">...</span></em>
  await <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">initSession</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">keyAlias</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">handle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">handle</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  await <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finishSession</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">handle</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.string.encrypt_success'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CommonConstants</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOAST_DURATION</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">encryptResult </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Base64Helper</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">encodeToStringSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">outData</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  return <span style="color: rgb(0,0,255);">encryptResult</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 方法getGenerateProperties。
```text
export function <span style="color: rgb(0,0,255);">getGenerateProperties</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">根据模式不同选择相应的算法参数：</span><span style="color: rgb(128,128,128);">AES</span><span style="color: rgb(128,128,128);">，</span><span style="color: rgb(128,128,128);">RSA</span><span style="color: rgb(128,128,128);">，</span><span style="color: rgb(128,128,128);">SM4</span></em>
  let <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksParam</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  switch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    case <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">:</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_ALGORITHM</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyAlg</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_ALG_AES</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_KEY_SIZE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeySize</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_AES_KEY_SIZE_256</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_PURPOSE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyPurpose</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_KEY_PURPOSE_ENCRYPT </span><span style="color: rgb(181,106,1);">|</span>
        <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyPurpose</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_KEY_PURPOSE_DECRYPT</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      break<span style="color: rgb(181,106,1);">;</span>
    case <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">:</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_ALGORITHM</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyAlg</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_ALG_RSA</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_KEY_SIZE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeySize</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_RSA_KEY_SIZE_2048</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_PURPOSE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyPurpose</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_KEY_PURPOSE_ENCRYPT </span><span style="color: rgb(181,106,1);">|</span>
        <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyPurpose</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_KEY_PURPOSE_DECRYPT</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      break<span style="color: rgb(181,106,1);">;</span>
    case <span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">:</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_ALGORITHM</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyAlg</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_ALG_SM4</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_KEY_SIZE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeySize</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_SM4_KEY_SIZE_128</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksTag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_TAG_PURPOSE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyPurpose</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_KEY_PURPOSE_ENCRYPT </span><span style="color: rgb(181,106,1);">|</span>
        <span style="color: rgb(0,0,255);">huks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HuksKeyPurpose</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">HUKS_KEY_PURPOSE_DECRYPT</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      break<span style="color: rgb(181,106,1);">;</span>
    default<span style="color: rgb(181,106,1);">:</span>
      break<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  return <span style="color: rgb(0,0,255);">properties</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 使用SM4和AES的报错截图：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/xpaxH7_STx6PXZMsutnpuQ/zh-cn_image_0000002658969105.png?HW-CC-KV=V1&HW-CC-Date=20260701T041425Z&HW-CC-Expire=86400&HW-CC-Sign=183DBB1EE4758AA72D34729C7C2D1AA5EA34A8BB1874F25A83083E16E8D5A007)


  使用RSA算法输出正常：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/0wJ5SwOOS9-56m0iSGYwRA/zh-cn_image_0000002658849155.png?HW-CC-KV=V1&HW-CC-Date=20260701T041425Z&HW-CC-Expire=86400&HW-CC-Sign=13A0EA0434B8C3135D39B7BACD5B875CF10B54791329B10B88CCECEC1F3010C4)


 
 

#### 解决方案

加解密的核心代码都是一致的，但是RSA整个过程正常，SM4和AES却报错401。
 
业务需要获取持久化存储的非对称密钥的公钥时可以使用[huks.exportKeyItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksexportkeyitem9)进行公钥导出，但是当前支持ECC/RSA/ED25519/X25519/SM2的[公钥导出](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-arkts)。代码入参均无问题，其中AES和SM4不在huks.exportKeyItem的支持范围内，而支持的RSA算法无问题，因此导致报错的原因应为使用了不正确的加密算法。变更为支持的加解密算法即可解决报错问题。
