# HarmonyOS系统实现异步锁的trylock

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-172

#### 问题现象

业务的多线程任务希望使用trylock机制，当已经有其他线程持有锁时放弃当前任务，HarmonyOS提供的异步锁如何实现trylock？
 
 

#### 背景知识

为了解决多并发实例间的数据竞争问题，ArkTS语言基础库引入了[AsyncLock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-locks#asynclock)能力。异步锁通过[lockAsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-locks#lockasync)进行锁操作。该方法首先获取锁，然后调用回调，最后释放锁。
 
[Sendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)定义了ArkTS的可共享对象体系及其规格约束。符合Sendable协议的数据（以下简称Sendable数据）可以在ArkTS并发实例间传递。
 
 

#### 解决方案

通过Sendable在不同线程间传递异步锁及锁上下文，获得锁的子锁信息保存到锁上下文，其他锁判定上下文确定自身是否获取到锁，实现trylock机制。
 
demo实现参考如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">taskpool</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">util </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">systemDateTime </span>from <span style="color: rgb(255,0,170);">'@ohos.systemDateTime'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">threadCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">线程数</span><span style="color: rgb(255,0,170);">: `</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">()</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">InputType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">threadCount </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Red</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'80%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">开始测试</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">threadCount </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">threadCount </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">threadCount </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">doTest</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">threadCount</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">线程数必须大于</span><span style="color: rgb(255,0,170);">0</span><span style="color: rgb(255,0,170);">小于</span><span style="color: rgb(255,0,170);">100'</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Concurrent</span>
function <span style="color: rgb(0,0,255);">lockProcess</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">lock</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Lock</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">lock</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tryLock</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">线程</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">获取锁结果：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

function <span style="color: rgb(0,0,255);">doTest</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">group </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TaskGroup</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">lock </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReentrantLock</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">group</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addTask</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">lockProcess</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`thread-</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">lock</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getLock</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  <span style="color: rgb(0,0,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">execute</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">group</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

export namespace <span style="color: rgb(0,0,255);">locks </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">可重入锁，生成子锁供不同线程使用</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  export class <span style="color: rgb(0,0,255);">ReentrantLock </span><span style="color: rgb(255,0,170);">{</span>
    private <span style="color: rgb(0,0,255);">sysLock</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyncLock </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyncLock</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    private <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">LockContext</span><span style="color: rgb(181,106,1);">;</span>

    <em>/**</em>
<em><span style="color: rgb(128,128,128);">     *</span></em>
<em><span style="color: rgb(128,128,128);">     * @param timeOutMs </span><span style="color: rgb(128,128,128);">锁超时时间，超过时间自动释放</span> <span style="color: rgb(128,128,128);"><</span><span style="color: rgb(128,128,128);">=0</span><span style="color: rgb(128,128,128);">时锁不超时</span></em>
<em><span style="color: rgb(128,128,128);">     */</span></em>
    constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">timeOutMs</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">LockContext</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">timeOutMs</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取单个线程使用的子锁</span></em>
    <span style="color: rgb(0,0,255);">getLock</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Lock </span><span style="color: rgb(255,0,170);">{</span>
      return new <span style="color: rgb(0,0,255);">Lock</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sysLock</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">generateRandomUUID</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">公共的锁上下文</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(181,106,1);">@Sendable</span>
  class <span style="color: rgb(0,0,255);">LockContext </span><span style="color: rgb(255,0,170);">{</span>
    private <span style="color: rgb(0,0,255);">lockTime</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">systemDateTime</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTime</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    private <span style="color: rgb(0,0,255);">lockUuid</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">默认</span><span style="color: rgb(128,128,128);">10s</span><span style="color: rgb(128,128,128);">超时</span></em>
    private <span style="color: rgb(0,0,255);">timeOutMs</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(181,106,1);">;</span>

    constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">timeOutMs</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">timeOutMs </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">timeOutMs </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">timeOutMs</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>

    <span style="color: rgb(0,0,255);">updateLockUuid</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockUuid </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockTime </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">systemDateTime</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTime</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">clearLockUuid</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockUuid </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">isReentrant</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockUuid </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">isLocked</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockUuid </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);"> !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockTimeout</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">lockTimeout</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">timeOutMs </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        return false<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      let <span style="color: rgb(0,0,255);">now </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">systemDateTime</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTime</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      return <span style="color: rgb(0,0,255);">now </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockTime </span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">timeOutMs</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(181,106,1);">@Sendable</span>
  export class <span style="color: rgb(0,0,255);">Lock </span><span style="color: rgb(255,0,170);">{</span>
    private <span style="color: rgb(0,0,255);">sysLock</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyncLock</span><span style="color: rgb(181,106,1);">;</span>
    private <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">LockContext</span><span style="color: rgb(181,106,1);">;</span>
    private <span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>

    constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">sysLock</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ArkTSUtils</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">locks</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AsyncLock</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">LockContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sysLock </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">sysLock</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uuid </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

   <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">     * </span><span style="color: rgb(128,128,128);">尝试上锁，上锁失败失败返回</span><span style="color: rgb(128,128,128);">false</span></em>
<em><span style="color: rgb(128,128,128);">     * @returns</span></em>
<em><span style="color: rgb(128,128,128);">     */</span></em>
    async <span style="color: rgb(0,0,255);">tryLock</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isReentrant</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
        return true<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isLocked</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span>
        await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sysLock</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockAsync</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isLocked</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">updateLockUuid</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isReentrant</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

   <em> <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">     * </span><span style="color: rgb(128,128,128);">解锁，未获取到锁时直接返回</span></em>
<em><span style="color: rgb(128,128,128);">     * @returns</span></em>
<em><span style="color: rgb(128,128,128);">     */</span></em>
    async <span style="color: rgb(0,0,255);">unlock</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isLocked</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isReentrant</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
        await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sysLock</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lockAsync</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isReentrant</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uuid</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clearLockUuid</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
