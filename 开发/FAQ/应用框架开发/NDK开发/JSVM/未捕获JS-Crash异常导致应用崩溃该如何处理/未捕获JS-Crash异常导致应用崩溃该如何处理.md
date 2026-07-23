# 未捕获JS-Crash异常导致应用崩溃该如何处理

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-10

#### 问题现象

应用运行过程中可能会出现JS crash异常，当出现未被捕获的JS crash异常时应用崩溃。如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/ffwUgXORSvq8dHys1LWCgQ/zh-cn_image_0000002658907825.png?HW-CC-KV=V1&HW-CC-Date=20260723T012523Z&HW-CC-Expire=86400&HW-CC-Sign=AB0CD129B9B85CEC391CF6D8E7A887D9C3B6C57ABA5F8B3F15F4C0299127D56C)

 
 

#### 背景知识

[ErrorManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager)模块提供对错误观察器的注册和注销的能力，在EntryAbility中配置即可实现统一处理（目前taskpool中不支持捕获异常）。
 
 

#### 解决方案
1. 手动try-catch。针对出现异常的代码段手动try-catch捕获异常：

  
```text
error:  TypeError: Get Property index out-of-bounds
```
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">ArrayList </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Hello World'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bold</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">testClick</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(255,255,255);">doublePages </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayList</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">testClick</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">doublePages</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">; </span><em>// index out-of-bounds</em>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`i is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'error: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. ErrorManager模块统一捕获。

  虽然通过try-catch能捕获异常，但整体方案仍然存在一定缺陷，比如添加大量try-catch导致可读性变差、遗漏JS Crash未被捕获。因此建议通过ErrorManager模块统一捕获未知JS Crash。
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">errorManager</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">UIAbility </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hilog </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">window </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">DOMAIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">0x0000</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(255,255,255);">observerId </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>

export default class <span style="color: rgb(0,0,255);">EntryAbility </span>extends <span style="color: rgb(0,0,255);">UIAbility </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">onCreate</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">observer1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">errorManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ErrorObserver </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">onUnhandledException</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">errorMsg</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'onUnhandledException, errorMsg: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">errorMsg</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">onException</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">errorObj</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'onException, name: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">errorObj</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'onException, message: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">errorObj</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        if <span style="color: rgb(255,0,170);">(</span>typeof <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">errorObj</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stack</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'string'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'onException, stack: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">errorObj</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">stack</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(181,106,1);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注册错误观测器。注册后可以捕获到应用产生的</span><span style="color: rgb(128,128,128);">js crash</span><span style="color: rgb(128,128,128);">，应用崩溃时进程不会退出。</span></em>
      <span style="color: rgb(255,255,255);">observerId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">errorManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'error'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">observer1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">paramError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">code </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">paramError </span>as <span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">paramError </span>as <span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`error: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    try <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getApplicationContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setColorMode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ConfigurationConstant</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ColorMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">COLOR_MODE_NOT_SET</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Failed to set colorMode. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">errorManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">off</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'error'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">observerId</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'----------- unregisterErrorObserver success ----------'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'----------- unregisterErrorObserver fail ----------'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">paramError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">code </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">paramError </span>as <span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">paramError </span>as <span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`error: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageCreate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WindowStage</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Main window is created, set main page for this ability</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onWindowStageCreate'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(255,255,255);">windowStage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'pages/Index'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Failed to load the content. Cause: %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Succeeded in loading the content.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onWindowStageDestroy</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// Main window is destroyed, release UI related resources</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onWindowStageDestroy'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onForeground</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// Ability has brought to foreground</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onForeground'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">onBackground</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// Ability has back to background</span></em>
    <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">DOMAIN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'testTag'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'%{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Ability onBackground'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
```


  运行效果：出现JS Crash问题时应用无闪退并在日志中记录堆栈。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/SbyJSD4BShCbe6ZGro3mBg/zh-cn_image_0000002658787889.png?HW-CC-KV=V1&HW-CC-Date=20260723T012523Z&HW-CC-Expire=86400&HW-CC-Sign=42135063F4A1D146F9F191A860CC084DB727A3A38BFDA72EED05FEE976E93C72)
