# 如何实现Worker并发时序同步

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-13

#### 问题现象

通过Worker开启多个子线程并发执行任务，并在子线程中计数，达到阈值触发上传任务。具体操作为：触发事件->存数据库->检查数据库数量->满足上传条件进行上传。
 
```text
<span style="color: rgb(255,255,255);">workerPort</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">onmessage </span><span style="color: rgb(181,106,1);">= </span>async <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">MessageEvents</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">eventData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// 1.</span><span style="color: rgb(128,128,128);">存储数据</span></em>
<em>  <span style="color: rgb(128,128,128);">// 2.</span><span style="color: rgb(128,128,128);">检查数据库</span></em>
<em>  <span style="color: rgb(128,128,128);">// 3.</span><span style="color: rgb(128,128,128);">满足条件，触发上传任务</span></em>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 背景知识

[Worker](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction)：Worker的主要作用是为应用程序提供一个多线程的运行环境，实现应用程序执行过程与宿主线程分离。通过在后台线程运行脚本处理耗时操作，避免计算密集型或高延迟任务阻塞宿主线程。
 
 

#### 解决方案

通过主线程统一控制上传触发+原子计数实现时序同步，所有计数操作集中在主线程完成，避免多Worker并发修改共享状态。
 
完整示例参考如下：
 1. 主线程（Index.ets）。
```ArkTS
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">worker</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">MessageEvents </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">原子计数器（主线程维护）</span></em>
let <span style="color: rgb(255,255,255);">uploadCounter </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(255,255,255);">UPLOAD_THRESHOLD </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(255,255,255);">workerInstance </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">worker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ThreadWorker</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'../workers/Worker.ets'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">接收</span><span style="color: rgb(128,128,128);">Worker</span><span style="color: rgb(128,128,128);">存储完成通知</span></em>
<span style="color: rgb(255,255,255);">workerInstance</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">onmessage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">MessageEvents</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'STORAGE_DONE'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">uploadCounter</span><span style="color: rgb(181,106,1);">++;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">原子递增</span></em>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">主线程判断满足条件后触发上传任务</span></em>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">uploadCounter </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">UPLOAD_THRESHOLD</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">triggerUpload</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">uploadCounter </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">重置计数器</span></em>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">触发</span><span style="color: rgb(128,128,128);">Worker</span><span style="color: rgb(128,128,128);">存储（示例）</span></em>
function <span style="color: rgb(0,0,255);">triggerWorkerStorage</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">workerInstance</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">postMessage</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">上传执行函数</span></em>
function <span style="color: rgb(0,0,255);">triggerUpload</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">执行上传操作</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">count1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">count2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">触发单次</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">triggerWorkerStorage</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">count1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">count1 </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">触发多次</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">count2</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);"><</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">count2 </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">triggerWorkerStorage</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">count2 </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

2. Worker线程（Worker.ets）。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">MessageEvents</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">ThreadWorkerGlobalScope</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">worker </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">workerPort</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ThreadWorkerGlobalScope </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">worker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">workerPort</span><span style="color: rgb(181,106,1);">;</span>
<em>// </em><em><span style="color: rgb(128,128,128);">模拟数据库</span></em>
let <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(255,255,255);">workerPort</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">onmessage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">MessageEvents</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">eventData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">storeSQL</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">eventData</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  try <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">workerPort</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">postMessage</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'STORAGE_DONE'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`worker postMessage error`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">模拟存数据库</span></em>
function <span style="color: rgb(0,0,255);">storeSQL</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">模拟存储数据库</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
