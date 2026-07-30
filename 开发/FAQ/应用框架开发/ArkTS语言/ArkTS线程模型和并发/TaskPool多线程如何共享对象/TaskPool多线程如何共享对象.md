# TaskPool多线程如何共享对象

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-4

#### 问题现象

根据官方文档的描述，TaskPool内存是完全独立的，例如有一个后台任务需要执行数据库操作和网络请求功能，如果多次调用TaskPool执行后台任务是否意味着每次都需要初始化数据库和网络请求工具类？有什么方法可以在线程间共享工具类初始化的数据？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/GDPIeOe0QNeDrr6bax2PBA/zh-cn_image_0000002629058994.png?HW-CC-KV=V1&HW-CC-Date=20260730T072305Z&HW-CC-Expire=86400&HW-CC-Sign=CF3307575CFD70C95FBF6B1F3E9C9DC33D91AA92E82D3A4A3D77E00F205E344A)

 
 

#### 背景知识

- [共享模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable-module)是进程内只会加载一次的模块，使用“use shared“这一指令来标记一个模块是否为共享模块。
- [Sendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)对象为可共享的，其跨线程前后指向同一个JS对象，如果其包含了JS或者Native内容，均可以直接共享，如果底层是Native实现的，则需要考虑线程安全性。

 
 

#### 解决方案

可以使用共享模块内导出Sendable对象来实现进程单例，从而达到线程间共享对象。
 
- SharedModule.ets共享对象定义文件。
```ArkTS
<em>// </em><em><span style="color: rgb(128,128,128);">共享模块</span><span style="color: rgb(128,128,128);">sharedModule.ets</span></em>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">ArkTSUtils </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">声明当前模块为共享模块，只能导出可</span><span style="color: rgb(128,128,128);">Sendable</span><span style="color: rgb(128,128,128);">数据</span></em>
<span style="color: rgb(132,63,161);">'use shared'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">共享模块，</span><span style="color: rgb(128,128,128);">SingletonA</span><span style="color: rgb(128,128,128);">全局唯一</span></em>
<span style="color: rgb(181,106,1);">@Sendable</span>
class <span style="color: rgb(0,0,255);">SingletonA </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">count_</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">lock_</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AsyncLock </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyncLock</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  public async <span style="color: rgb(0,0,255);">getCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">lock_</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockAsync</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">count_</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  public async <span style="color: rgb(0,0,255);">increaseCount</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">异步锁中自增</span><span style="color: rgb(128,128,128);">count</span></em>
    await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">lock_</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockAsync</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">count_</span><span style="color: rgb(181,106,1);">++;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">导出单例共享对象</span></em>
export const <span style="color: rgb(255,255,255);">singletonA </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SingletonA</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
```

- TaskToolSharedPage.ets主线程和线程池访问共享对象页面。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">taskpool </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">singletonA </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./SharedModule'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Concurrent</span>
async function <span style="color: rgb(0,0,255);">increaseCount</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  await <span style="color: rgb(255,255,255);">singletonA</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">increaseCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">singletonA</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`SharedModule: count is: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Concurrent</span>
async function <span style="color: rgb(0,0,255);">printCount</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">singletonA</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`SharedModule: count is: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TaskToolSharedPage </span><span style="color: rgb(181,106,1);">{</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'MainThread print count'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            try <span style="color: rgb(181,106,1);">{</span>
              await <span style="color: rgb(0,0,255);">printCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`MainThread print count.errCode is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Taskpool print count'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            try <span style="color: rgb(181,106,1);">{</span>
              await <span style="color: rgb(255,255,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">execute</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">printCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Taskpool print count.errCode is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'MainThread increase count'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            try <span style="color: rgb(181,106,1);">{</span>
              await <span style="color: rgb(0,0,255);">increaseCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">singletonA</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`MainThread SharedModule: count is: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`MainThread increase count.errCode is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Taskpool increase count'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            try <span style="color: rgb(181,106,1);">{</span>
              await <span style="color: rgb(255,255,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">execute</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">increaseCount</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">singletonA</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Taskpool SharedModule: count is: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">count</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Taskpool increase count.errCode is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/n9833oiRTD-jfV77EX1gBg/zh-cn_image_0000002628899076.png?HW-CC-KV=V1&HW-CC-Date=20260730T072305Z&HW-CC-Expire=86400&HW-CC-Sign=E84EA8D79423EE1D27AA2216AC19F512094E99821AC85283BBCC33D2A57F58B9)
