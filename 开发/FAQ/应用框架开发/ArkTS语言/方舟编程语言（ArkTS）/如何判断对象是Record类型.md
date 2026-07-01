# 如何判断对象是Record类型

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-170

#### 问题现象

如何判断一个对象是否为Record类型。
 
 

#### 背景知识

Record<K, T>是一种对象类型，其属性键为K，属性值为T。该工具类型可用于将一个类型的属性映射到另一个类型。
 
 

#### 解决方案

在ArkTS中，可以通过typeof、instanceof方法判断是否为对象类型，并排除null、Array、Date等内置对象，再结合Record的定义，判断键值。
 
示例代码如下：
 
```text
type <span style="color: rgb(128,128,128);">IDirection </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'up' </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,0,170);">'down'</span><span style="color: rgb(181,106,1);">;</span>
type <span style="color: rgb(128,128,128);">RecordDirection </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">IDirection</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">isRecord</span><span style="color: rgb(0,0,255);">(</span>
  <span style="color: rgb(0,0,255);">variable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">keyChecker</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">key</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">valueChecker</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">boolean</span>
<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span>typeof <span style="color: rgb(0,0,255);">variable </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,170);">'object' </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">variable </span><span style="color: rgb(181,106,1);">=== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    return false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">keyChecker </span><span style="color: rgb(181,106,1);">=== </span>undefined <span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">valueChecker </span><span style="color: rgb(181,106,1);">=== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">排除数组、排除</span><span style="color: rgb(128,128,128);">Date</span><span style="color: rgb(128,128,128);">对象</span></em>
    return <span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isArray</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">variable</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);"> !</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">variable </span>instanceof <span style="color: rgb(0,0,255);">Date</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">遍历对象的键和值，进行类型检查</span></em>
  const <span style="color: rgb(0,0,255);">arr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Object</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keys</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">variable</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">key </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">keyChecker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">key</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">|| !</span><span style="color: rgb(0,0,255);">valueChecker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">variable</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">key</span><span style="color: rgb(0,0,255);">])) </span><span style="color: rgb(255,0,170);">{</span>
      return false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  return true<span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RecordJudgment </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">cDirection</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">RecordDirection </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(255,0,170);">'up'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">'down'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'check'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          const <span style="color: rgb(0,0,255);">keyChecker </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">key</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">key </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'up' </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">key </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'down'</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(0,0,255);">valueChecker </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> typeof <span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,170);">'number'</span><span style="color: rgb(181,106,1);">;</span>

          const <span style="color: rgb(0,0,255);">result1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">isRecord</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cDirection</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          const <span style="color: rgb(0,0,255);">result2 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">isRecord</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cDirection</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">keyChecker</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">valueChecker</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`flag:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">result1</span><span style="color: rgb(255,0,170);">} ${</span><span style="color: rgb(0,0,255);">result2</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// flag:true true</span></em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
