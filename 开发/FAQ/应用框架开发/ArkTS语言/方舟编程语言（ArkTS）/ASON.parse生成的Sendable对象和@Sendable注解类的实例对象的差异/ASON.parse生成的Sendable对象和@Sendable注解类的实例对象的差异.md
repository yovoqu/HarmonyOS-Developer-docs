# ASON.parse生成的Sendable对象和@Sendable注解类的实例对象的差异

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-179

#### 问题现象

使用ArkTSUtils.ASON.parse生成的Sendable对象，和通过类（@Sendable装饰器）构造函数实例化出来的对象，有什么区别？
 
 

#### 背景知识

[ASON解析与生成](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ason-parsing-generation)：[ASON工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-ason)提供了[Sendable对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)的序列化、反序列化能力。使用ASON.stringify方法可将对象转换为字符串，使用ASON.parse方法可将字符串转换为Sendable对象，从而实现对象在并发任务间的高性能引用传递。
 
 

#### 解决方案

相同点：
 
- 都是Sendable对象，可以跨线程通信。
- 都可以获取和修改属性值，但是无法增加和删除。

 
不同点：ASON.parse生成的Sendable对象无法调用类成员方法。原因是使用ArkTSUtils.ASON.parse()解析JSON生成Sendable对象时，生成的仅是数据结构的副本，不会保留原始类的原型链和方法，所以无法调用方法。
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">lang</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">taskpool </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Sendable</span>
class <span style="color: rgb(0,0,255);">TestClass </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Bob'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">age</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">city</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'ct'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">age </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`name: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> age: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">age</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> city: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">city</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Concurrent</span>
function <span style="color: rgb(0,0,255);">method</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">testClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">testClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Cici'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'modify name to Cici'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'ASON'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          type <span style="color: rgb(128,128,128);">ISendable </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">lang</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ISendable</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">jsonText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'{"name": "John", "age": 30, "city": "ct"}'</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">obj </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ASON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parse</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">jsonText</span><span style="color: rgb(0,0,255);">) </span>as <span style="color: rgb(0,0,255);">ISendable</span><span style="color: rgb(181,106,1);">;</span>

        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在线程中传递</span></em>
          try <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">task </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Task</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">method</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
            await <span style="color: rgb(0,0,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">execute</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">task</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">打印</span><span style="color: rgb(128,128,128);">Cici</span></em>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">e </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">执行失败，</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>

         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取和修改属性值</span></em>
          try <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Alice'</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">打印</span><span style="color: rgb(128,128,128);">Alice</span></em>
            <span style="color: rgb(0,0,255);">jsonText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ASON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">jsonText</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">打印</span><span style="color: rgb(128,128,128);">{"name":"Alice","age":30,"city":"ct"}</span></em>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">e </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">修改失败，</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>

          <em>// </em><em><span style="color: rgb(128,128,128);">无法调用类成员方法</span></em>
          try <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj </span>as <span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">调用成功</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">e </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">调用失败，</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">无法调用，打印：调用失败，</span><span style="color: rgb(128,128,128);">undefined, undefined is not callable</span></em>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
