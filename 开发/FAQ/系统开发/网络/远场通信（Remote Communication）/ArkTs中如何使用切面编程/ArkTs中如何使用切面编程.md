# ArkTs中如何使用切面编程

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-7

#### 问题现象

如何在rcp.createSession方法执行前，执行相关逻辑？
 
 

#### 背景知识

应用切面编程（AOP）是一种通过在不修改业务逻辑代码的前提下，将通用功能（如日志、埋点、安全等）动态插入方法执行流程中的编程范式。HarmonyOS主要通过插桩机制来实现切面编程，并提供了[Aspect类](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#aspect11)，该类包含addBefore、addAfter和replace接口。
 
 

#### 解决方案
1. 创建一个proxy.ts作为rcp的封装代理函数。
```text
export function <span style="color: rgb(0,0,255);">createSessionProxy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">rcp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SessionConfiguration</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">rcp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Session </span><span style="color: rgb(255,0,170);">{</span>
  return <span style="color: rgb(0,0,255);">rcp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSession</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. 在业务需要采用拦截器的模块调用该方法。
```text
export function <span style="color: rgb(0,0,255);">injectRcpAspect</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Aspect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addBefore</span><span style="color: rgb(0,0,255);">(</span>
    <span style="color: rgb(0,0,255);">createSessionProxy</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">'createSession'</span><span style="color: rgb(181,106,1);">,</span>
    false<span style="color: rgb(181,106,1);">,</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">下面函数是在</span><span style="color: rgb(128,128,128);">createSession</span><span style="color: rgb(128,128,128);">方法前执行。</span></em>
    <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">object</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">rcp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SessionConfiguration</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`[</span><span style="color: rgb(255,0,170);">切面</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(255,0,170);">创建</span><span style="color: rgb(255,0,170);"> Session</span><span style="color: rgb(255,0,170);">，目标为：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">target</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">，配置为</span><span style="color: rgb(255,0,170);">:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
  <span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
 

#### 总结

[util.Aspect.addBefore()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#addbefore11)只能对ArkTS的类或对象方法做切面，不能作用于native层或系统模块。而rcp其大多方法是native实现，所以不能直接做切面，推荐使用封装代理函数然后插桩做切面。
