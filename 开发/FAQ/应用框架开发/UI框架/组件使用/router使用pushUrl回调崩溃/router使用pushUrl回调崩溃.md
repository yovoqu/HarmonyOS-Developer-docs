# router使用pushUrl回调崩溃

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1416

#### 问题现象

在router.pushUrl的回调中执行router.clear会崩溃。
 
```text
<span style="color: rgb(0,0,255);">router</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">url</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">"login/UserNameLoginPage"</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">router</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clear</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```
 
报错Log信息如下：
 
```text
<span style="color: rgb(0,0,255);">Error </span><span style="color: rgb(181,106,1);">name</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">Error</span>
<span style="color: rgb(0,0,255);">Error </span><span style="color: rgb(181,106,1);">message</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">Internal error</span><span style="color: rgb(181,106,1);">. </span><span style="color: rgb(0,0,255);">UI execution context not found</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(0,0,255);">Error </span><span style="color: rgb(181,106,1);">code</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">100001</span>
```
 
 

#### 背景知识

全局的UI接口是和具体UI实例的执行上下文相关的，在当前接口调用时，通过追溯调用链跟踪到UI的上下文，来确定具体的UI实例。若在非UI页面中或者一些异步回调中调用这类接口，可能无法跟踪到当前UI的上下文，导致接口执行失败。和上下文相关的全局接口请查阅[@ohos.arkui.UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext)模块。
 
 

#### 问题定位

报错日志提示未找到UI执行的上下文信息"UI execution context not found"，即执行router相关接口时未追踪到当前UI上下文。
 
 

#### 分析结论

在异步回调时使用router.clear，未追踪到当前UI的上下文，接口执行失败，程序崩溃。
 
 

#### 修改建议

- 方法一：使用Navigation组件替代router作为应用路由框架，可参考[Router切换Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-router-to-navigation)。
- 方法二：通过使用UIContext中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的router对象，再通过该对象调用对应方法。可参考官网文档中关于[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl)等API的用法说明和示例。

  如果在非UI页面类中调用router时，由于无法直接获取UIContext实例，需在页面初始化后将UIContext存入AppStorage，后续通过AppStorage获取该实例并调用其getRouter()方法获取router对象。如下示例：
```ArkTS
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RouterDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">UIContext</span><span style="color: rgb(128,128,128);">，保存在</span><span style="color: rgb(128,128,128);">AppStorage</span><span style="color: rgb(128,128,128);">中</span></em>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">也可以在</span><span style="color: rgb(128,128,128);">EntryAbility.ets</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">onWindowStageCreate</span><span style="color: rgb(128,128,128);">方法中保存</span><span style="color: rgb(128,128,128);">UIContext</span></em>
    <span style="color: rgb(0,0,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOrCreate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'UIContext'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">跳转页面</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Auth</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gotoLoginPage</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

class <span style="color: rgb(0,0,255);">Auth </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">跳转到登录页</span></em>
  static <span style="color: rgb(0,0,255);">gotoLoginPage</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">AppStorage</span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">UIContext</span></em>
    const <span style="color: rgb(0,0,255);">uiContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'UIContext'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRouter</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">url</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'pages/Index' </span><em>// </em><em><span style="color: rgb(128,128,128);">需自行创建一个</span><span style="color: rgb(128,128,128);">Index</span><span style="color: rgb(128,128,128);">页面</span></em>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
