# 如何判断Sendable对象是类的实例

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-53

#### 问题现象

[Sendable对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)传递到其它线程后，如何判断Sendable对象是类的实例？
 
 

#### 解决方案

使用instanceof需要在导出Sendable类的文件里加上"use shared"，把文件标记成共享的，示例代码如下：
 
```text
<span style="color: rgb(132,63,161);">"use shared"</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Sendable</span>
export class <span style="color: rgb(0,0,255);">Per </span><span style="color: rgb(181,106,1);">{</span>
  static <span style="color: rgb(255,255,255);">staticString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">commonString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'111'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Sendable</span>
export class <span style="color: rgb(0,0,255);">Per1 </span><span style="color: rgb(181,106,1);">{</span>
  static <span style="color: rgb(255,255,255);">staticString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">commonString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'222'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Sendable</span>
export class <span style="color: rgb(0,0,255);">Per2 </span><span style="color: rgb(181,106,1);">{</span>
  static <span style="color: rgb(255,255,255);">staticString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">commonString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'333'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Sendable</span>
export class <span style="color: rgb(0,0,255);">Per3 </span><span style="color: rgb(181,106,1);">{</span>
  static <span style="color: rgb(255,255,255);">staticString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">commonString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'444'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
创建Per类对象，并通过instanceof判断其是否为Sendable类的实例。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">Per</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Per1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Per2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Per3 </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./Per'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">lang</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">taskpool </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Concurrent</span>
function <span style="color: rgb(0,0,255);">init</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Object </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">lang</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ISendable</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">constructorName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">constructor</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">instanceof</span><span style="color: rgb(128,128,128);">进行判断</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data </span>instanceof <span style="color: rgb(255,255,255);">Per</span>
    <span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">data </span>instanceof <span style="color: rgb(255,255,255);">Per1</span>
    <span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">data </span>instanceof <span style="color: rgb(255,255,255);">Per2</span>
    <span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(255,255,255);">data </span>instanceof <span style="color: rgb(255,255,255);">Per3</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">通过</span><span style="color: rgb(132,63,161);">instanceof</span><span style="color: rgb(132,63,161);">进行判断</span><span style="color: rgb(132,63,161);">:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">constructorName</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">对象是</span><span style="color: rgb(132,63,161);">Sendable Class</span><span style="color: rgb(132,63,161);">的实例</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data </span>instanceof <span style="color: rgb(255,255,255);">Object</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">处理普通</span><span style="color: rgb(128,128,128);">Object</span><span style="color: rgb(128,128,128);">类型</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">通过</span><span style="color: rgb(132,63,161);">instanceof</span><span style="color: rgb(132,63,161);">进行判断</span><span style="color: rgb(132,63,161);">:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">constructorName</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">对象是</span><span style="color: rgb(132,63,161);">Object Class</span><span style="color: rgb(132,63,161);">的实例</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  let <span style="color: rgb(255,255,255);">sendableNames</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'Per'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Per1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Per2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'Per3'</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过类名进行判断</span>
  let <span style="color: rgb(255,255,255);">isExist </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">sendableNames</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">includes</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">constructorName</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">isExist</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">通过类名进行判断</span><span style="color: rgb(132,63,161);">:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">constructorName</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">对象是</span><span style="color: rgb(132,63,161);">Sendable Class</span><span style="color: rgb(132,63,161);">的实例</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data </span>instanceof <span style="color: rgb(255,255,255);">Object</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">处理普通</span><span style="color: rgb(128,128,128);">Object</span><span style="color: rgb(128,128,128);">类型</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">通过类名进行判断</span><span style="color: rgb(132,63,161);">:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">constructorName</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">对象是</span><span style="color: rgb(132,63,161);">Object Class</span><span style="color: rgb(132,63,161);">的实例</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

async function <span style="color: rgb(0,0,255);">concurrentFunc</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  try <span style="color: rgb(181,106,1);">{</span>
    const <span style="color: rgb(255,255,255);">task</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Task </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Task</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">init</span><span style="color: rgb(181,106,1);">, </span>new <span style="color: rgb(0,0,255);">Per</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">execute</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">task</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`taskpool execute success`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`taskpool execute error is: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">}`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SendableCheckerDemo </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'Hello World'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bold</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">concurrentFunc</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
