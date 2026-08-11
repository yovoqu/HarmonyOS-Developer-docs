# 如何解决ArkUI.Lite开发穿戴应用时异步任务不生效问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-177

#### 问题现象

采用兼容JS的类Web开发范式（ArkUI.Lite）开发穿戴应用时，在app.js的onCreate()中调用异步函数向服务器请求数据，发现异步函数不生效。
 
问题代码示例参考如下：
 
```text
<em>// app.js</em>
export default <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">mockData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">isDataReady</span><span style="color: rgb(181,106,1);">: </span>false
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(132,63,161);"> AceApplication onCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fetchDataAsync</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span> <span style="color: rgb(132,63,161);">同步数据完成</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mockData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isDataReady </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(132,63,161);"> AceApplication onDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">fetchDataAsync</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    return new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">resolve</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">reject</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span> <span style="color: rgb(132,63,161);">开始同步数据</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">setTimeout</span><span style="color: rgb(128,128,128);">模拟网络延迟（</span><span style="color: rgb(128,128,128);">1.5</span><span style="color: rgb(128,128,128);">秒后完成）</span></em>
      <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        const <span style="color: rgb(255,255,255);">mockData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'123'</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mockData</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
控制台只输出了“开始同步数据”的日志，then()中的代码并没有执行：
 
```text
I     app.js -> AceApplication onCreate
I     app.js -> 开始同步数据
```
 
 

#### 背景知识

[JS语法参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-js)：JS文件用来定义HML页面的业务逻辑，支持ECMA规范的JavaScript语言。
 
 

#### 问题定位

查看官网文档确认是否系统能力是否支持。根据官网文档描述轻量级智能穿戴支持的ES6语法有限，而Promise/async/await不在支持范围内，因此无法使用。
 
 

#### 分析结论

轻量级智能穿戴支持的ES6语法有限，不支持Promise/async/await等ES6语法。
 
 

#### 修改建议

使用callback的方式实现异步操作。
 
```json
<em>// app.js</em>
export default <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">mockData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">isDataReady</span><span style="color: rgb(181,106,1);">: </span>false
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(132,63,161);"> AceApplication onCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fetchData</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(132,63,161);"> callback</span><span style="color: rgb(132,63,161);">方式同步数据完成</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`index.js -</span><span style="color: rgb(132,63,161);">></span> <span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mockData</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`index.js -</span><span style="color: rgb(132,63,161);">></span> <span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isDataReady</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(132,63,161);"> AceApplication onDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">fetchData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">callback</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.js -</span><span style="color: rgb(132,63,161);">></span> <span style="color: rgb(132,63,161);">开始同步数据</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用</span><span style="color: rgb(128,128,128);">setTimeout</span><span style="color: rgb(128,128,128);">模拟网络延迟（</span><span style="color: rgb(128,128,128);">1.5</span><span style="color: rgb(128,128,128);">秒后完成）</span></em>
    <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      const <span style="color: rgb(255,255,255);">mockData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'123'</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">mockData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">mockData</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">isDataReady </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">callback</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mockData</span><span style="color: rgb(181,106,1);">, </span>null<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
